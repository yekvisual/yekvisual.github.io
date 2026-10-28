"""Toplayıcının ortak veri yapıları."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode

IZLEME_PARAMLARI = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "ref", "fbclid", "gclid"}


def url_normalize(url: str) -> str:
    """İzleme parametrelerini, parçayı ve sondaki eğik çizgiyi atar."""
    p = urlsplit(url.strip())
    q = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True) if k.lower() not in IZLEME_PARAMLARI]
    yol = p.path.rstrip("/") or "/"
    return urlunsplit((p.scheme.lower() or "https", p.netloc.lower().removeprefix("www."), yol, urlencode(q), ""))


def metin_temizle(s: str | None, limit: int = 1200) -> str:
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit]


@dataclass
class Oge:
    """Bir kaynaktan gelen ham öğe. AI katmanına bu haliyle gider."""

    kaynak: str
    tur: str  # rss | github | huggingface | arxiv | reddit | sayfa
    baslik: str
    url: str
    metin: str = ""
    tarih: str = ""  # ISO 8601
    kategori: str = "araclar"
    gorsel: str | None = None  # og:image ya da kaynaktan gelen görsel adresi
    ek: dict = field(default_factory=dict)  # yıldız, indirme, puan gibi sinyaller

    def __post_init__(self):
        self.url = url_normalize(self.url)
        self.baslik = metin_temizle(self.baslik, 300)
        self.metin = metin_temizle(self.metin)
        if not self.tarih:
            self.tarih = datetime.now(timezone.utc).isoformat()

    @property
    def id(self) -> str:
        return hashlib.sha1(self.url.encode()).hexdigest()[:16]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["id"] = self.id
        return d
