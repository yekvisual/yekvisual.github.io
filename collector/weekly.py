"""Haftalık özet: son 7 günün haberlerinden content/ozetler/YYYY-hNN.md üretir,
NEWSLETTER_API_KEY varsa Buttondown ile bülten olarak gönderir.

  python -m collector.weekly            # yaz (varsa bülten gönder)
  python -m collector.weekly --dry-run  # sadece göster
"""

from __future__ import annotations

import os
import re
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from pathlib import Path

import anthropic
import httpx
import yaml
from pydantic import BaseModel, Field

KOK = Path(__file__).resolve().parent.parent
HABERLER = KOK / "content" / "haberler"
OZETLER = KOK / "content" / "ozetler"
USLUP = (KOK / "style" / "uslup.md").read_text()
MODEL = os.environ.get("YAZIM_MODEL", "claude-sonnet-5-5")
SITE = "https://yekvisual.github.io"


class Ozet(BaseModel):
    baslik: str = Field(description="Örn. 'Haftalık Özet · 20–26 Ekim 2026'")
    ozet: str = Field(description="1–2 cümle, bülten konu satırı olarak da kullanılır")
    govde: str = Field(description="Markdown. Başlıklar: 'Haftanın en önemlisi', kategori bazlı 2–4 bölüm, 'Bu hafta ne denedim?' (yekvisual notlarından). Her habere /gundem/... linki ver. 200–400 kelime.")


def hafta_basi() -> datetime:
    """Bu haftanın pazartesi 00:00'ı (Türkiye saati), UTC olarak. Özet pazartesiden pazara."""
    simdi = datetime.now(ZoneInfo("Europe/Istanbul"))
    pazartesi = (simdi - timedelta(days=simdi.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    return pazartesi.astimezone(timezone.utc)


def haftanin_haberleri(gun: int | None = None) -> list[dict]:
    esik = datetime.now(timezone.utc) - timedelta(days=gun) if gun else hafta_basi()
    liste = []
    for p in HABERLER.rglob("*.md"):
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", p.read_text(), re.S)
        if not m:
            continue
        fm = yaml.safe_load(m.group(1))
        if fm.get("ornek"):
            continue
        tarih = datetime.fromisoformat(str(fm["tarih"])).replace(tzinfo=timezone.utc)
        if tarih < esik:
            continue
        liste.append({**fm, "id": str(p.relative_to(HABERLER)).removesuffix(".md"), "govde": m.group(2)[:800]})
    return sorted(liste, key=lambda h: (-h.get("puan", 0), h["tarih"]))


def yaz(haberler: list[dict]) -> Ozet:
    client = anthropic.Anthropic()
    metin = "\n\n".join(
        f"### {h['baslik']}\nURL: /gundem/{h['id']}/\nKategori: {h['kategori']} · Puan: {h.get('puan')}\nÖzet: {h['ozet']}\nNeden önemli: {h.get('neden_onemli', '')}\nyekvisual notu: {h.get('yekvisual_notu', '')}"
        for h in haberler
    )
    bugun = datetime.now(timezone.utc)
    r = client.messages.parse(
        model=MODEL,
        max_tokens=4000,
        system=f"Sen yekvisual'ın yazarısın. Üslup rehberi:\n\n{USLUP}",
        messages=[{"role": "user", "content": f"Bugün {bugun:%d.%m.%Y}. Bu haftanın haberleri aşağıda. Haftalık özet yaz.\n\n{metin}"}],
        output_format=Ozet,
    )
    return r.parsed_output


def bulten_gonder(ozet: Ozet, dosya_id: str) -> None:
    """Buttondown API ile e-posta gönderir. Anahtar yoksa atlar."""
    key = os.environ.get("NEWSLETTER_API_KEY")
    if not key:
        print("NEWSLETTER_API_KEY yok; bülten gönderilmedi.", file=sys.stderr)
        return
    govde = ozet.govde.replace("](/gundem/", f"]({SITE}/gundem/") + f"\n\n---\nTamamı: {SITE}/haftalik/{dosya_id}/"
    r = httpx.post(
        "https://api.buttondown.com/v1/emails",
        headers={"Authorization": f"Token {key}"},
        json={"subject": ozet.baslik, "body": govde, "status": "about_to_send"},
        timeout=30,
    )
    print(f"Bülten: {r.status_code} {r.text[:120]}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    dry = "--dry-run" in (argv or sys.argv[1:])
    haberler = haftanin_haberleri()
    if len(haberler) < 2:
        print(f"Bu hafta yalnızca {len(haberler)} haber var; özet yazılmadı.", file=sys.stderr)
        return 0
    ozet = yaz(haberler)
    bugun = datetime.now(timezone.utc)
    dosya_id = f"{bugun:%Y}-h{bugun.isocalendar().week:02d}"
    hedef = OZETLER / f"{dosya_id}.md"
    fm = yaml.safe_dump({"baslik": ozet.baslik, "tarih": f"{bugun:%Y-%m-%d}", "ozet": ozet.ozet}, allow_unicode=True, sort_keys=False)
    icerik = f"---\n{fm}---\n\n{ozet.govde.strip()}\n"
    if dry:
        print(icerik)
        return 0
    OZETLER.mkdir(parents=True, exist_ok=True)
    hedef.write_text(icerik)
    print(f"Yazıldı: {hedef.relative_to(KOK)}", file=sys.stderr)
    bulten_gonder(ozet, dosya_id)
    return 0


if __name__ == "__main__":
    sys.exit(main())
