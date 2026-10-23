"""Tekrar eleme: data/seen.json'daki kayıtlar ve aynı çalıştırmadaki benzer başlıklar."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from .models import Oge

SEEN_YOLU = Path(__file__).resolve().parent.parent / "data" / "seen.json"
SAKLAMA_GUNU = 120


def yukle() -> dict:
    if SEEN_YOLU.exists():
        return json.loads(SEEN_YOLU.read_text())
    return {}


def kaydet(seen: dict) -> None:
    # Eski kayıtları budayarak dosyayı küçük tut.
    simdi = datetime.now(timezone.utc)
    temiz = {}
    for k, v in seen.items():
        try:
            if (simdi - datetime.fromisoformat(v["tarih"])).days <= SAKLAMA_GUNU:
                temiz[k] = v
        except Exception:  # noqa: BLE001
            temiz[k] = v
    SEEN_YOLU.parent.mkdir(parents=True, exist_ok=True)
    SEEN_YOLU.write_text(json.dumps(temiz, ensure_ascii=False, indent=1, sort_keys=True) + "\n")


def isaretle(seen: dict, oge: Oge, karar: str, ekstra: dict | None = None) -> None:
    seen[oge.id] = {"url": oge.url, "baslik": oge.baslik[:120], "tarih": datetime.now(timezone.utc).isoformat(), "karar": karar, **(ekstra or {})}


_DUR = {"the", "a", "an", "of", "for", "and", "with", "to", "in", "on", "is", "new", "ve", "ile", "için", "bir"}


def _kelimeler(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9çğıöşü]+", s.lower()) if len(w) > 2 and w not in _DUR}


def benzer(a: str, b: str, esik: float = 0.6) -> bool:
    """Jaccard benzerliği; aynı haberi farklı kaynaklardan yakalamak için kaba ama yeterli."""
    x, y = _kelimeler(a), _kelimeler(b)
    if not x or not y:
        return False
    return len(x & y) / len(x | y) >= esik


def ele(ogeler: list[Oge], seen: dict) -> tuple[list[Oge], list[list[Oge]]]:
    """Daha önce görülenleri atar; kalanları benzer başlıklara göre gruplar.

    Döndürür: (yeni tekil öğeler, gruplar). Her grup aynı olayı anlatan öğelerdir;
    ilk eleman asıl, diğerleri ek kaynak olarak kullanılır.
    """
    yeni = [o for o in ogeler if o.id not in seen]
    # Görülen URL'lerin başlıklarıyla da karşılaştır (aynı haber farklı adresle gelebilir)
    gorulen_basliklar = [v.get("baslik", "") for v in seen.values()]
    yeni = [o for o in yeni if not any(benzer(o.baslik, b, 0.75) for b in gorulen_basliklar)]

    gruplar: list[list[Oge]] = []
    for o in yeni:
        for g in gruplar:
            if benzer(o.baslik, g[0].baslik):
                g.append(o)
                break
        else:
            gruplar.append([o])
    return [g[0] for g in gruplar], gruplar
