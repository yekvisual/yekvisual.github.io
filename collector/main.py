"""Toplayıcı komut satırı.

  python -m collector --check      kaynak sağlık kontrolü (AI yok)
  python -m collector --dry-run    topla + ele + puanla, dosya yazma
  python -m collector              tam çalıştırma: haberleri content/ altına yazar
  python -m collector --since 3    son 3 günü tara (varsayılan 2)
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

from . import dedupe, fetch
from .models import Oge

KOK = Path(__file__).resolve().parent.parent
KAYNAKLAR = KOK / "sources.yaml"

# Maliyet sınırı: bir çalıştırmada AI'a gönderilecek en fazla öğe.
MAKS_OGE = int(os.environ.get("MAKS_OGE", "60"))


def kaynaklari_yukle() -> dict:
    return yaml.safe_load(KAYNAKLAR.read_text())


def kontrol(args) -> int:
    since = datetime.now(timezone.utc) - timedelta(days=args.since)
    kaynaklar = kaynaklari_yukle()
    _, sayac = fetch.hepsini_topla(kaynaklar, since)
    hatali = 0
    print(f"{'Kaynak':32} {'Öğe':>4}  Durum")
    print("-" * 60)
    for tur, liste in kaynaklar.items():
        for k in liste or []:
            ad = k["ad"]
            hata = fetch.son_hatalar.get(ad)
            durum = f"HATA: {hata}" if hata else "ok"
            if hata:
                hatali += 1
            print(f"{ad:32} {sayac.get(ad, 0):>4}  {durum}")
    print("-" * 60)
    print(f"{len(sayac)} kaynak, {hatali} hatalı, son {args.since} günde {sum(sayac.values())} öğe")
    return 1 if hatali else 0


def topla(args) -> tuple[list[Oge], list[list[Oge]], dict]:
    since = datetime.now(timezone.utc) - timedelta(days=args.since)
    kaynaklar = kaynaklari_yukle()
    ogeler, sayac = fetch.hepsini_topla(kaynaklar, since)
    seen = dedupe.yukle()
    yeni, gruplar = dedupe.ele(ogeler, seen)
    print(f"Toplanan: {len(ogeler)}  ·  Görülmemiş: {len(yeni)}  ·  Grup: {len(gruplar)}", file=sys.stderr)
    for ad, h in fetch.son_hatalar.items():
        print(f"  ! {ad}: {h}", file=sys.stderr)
    # Resmi duyurular (rss/github) önce, sonra topluluk/HF sinyali; sonra tavan uygula
    TUR_AGIRLIK = {"rss": 3.0, "github": 3.0, "reddit": 2.0, "huggingface": 1.0, "arxiv": 0.5}

    def agirlik(g: list[Oge]) -> float:
        o = g[0]
        return TUR_AGIRLIK.get(o.tur, 1.0) + min((o.ek.get("likes") or 0) / 200, 2.0) + len(g) * 2
    gruplar.sort(key=agirlik, reverse=True)
    if len(gruplar) > MAKS_OGE:
        print(f"  tavan: {len(gruplar)} gruptan ilk {MAKS_OGE} işlenecek", file=sys.stderr)
        gruplar = gruplar[:MAKS_OGE]
    return [g[0] for g in gruplar], gruplar, seen


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="collector", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check", action="store_true", help="kaynak sağlık kontrolü")
    p.add_argument("--dry-run", action="store_true", help="dosya yazma, sonucu göster")
    p.add_argument("--since", type=int, default=2, help="kaç günlük öğe (varsayılan 2)")
    p.add_argument("--no-ai", action="store_true", help="AI katmanını atla, sadece ham listeyi göster")
    args = p.parse_args(argv)

    if args.check:
        return kontrol(args)

    yeni, gruplar, seen = topla(args)
    if args.no_ai or not os.environ.get("ANTHROPIC_API_KEY"):
        if not args.no_ai:
            print("ANTHROPIC_API_KEY yok; ham liste gösteriliyor.", file=sys.stderr)
        for g in gruplar:
            o = g[0]
            ek = f" (+{len(g) - 1} kaynak)" if len(g) > 1 else ""
            print(f"[{o.tur:11}] {o.kaynak:22} {o.baslik[:80]}{ek}")
        return 0

    from . import ai, write  # AI katmanı yalnızca gerektiğinde yüklenir

    sonuclar = ai.isle(gruplar)
    yayin, onay, atilan = write.uygula(sonuclar, gruplar, seen, dry_run=args.dry_run)
    print(f"Yayın: {len(yayin)}  ·  Onaya: {len(onay)}  ·  Atılan: {len(atilan)}", file=sys.stderr)
    if not args.dry_run:
        dedupe.kaydet(seen)
    return 0


if __name__ == "__main__":
    sys.exit(main())
