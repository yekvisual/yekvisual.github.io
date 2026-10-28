"""Kaynak adaptörleri. Her adaptör sources.yaml'daki bir kaydı alır, Oge listesi döndürür.

Hata olursa boş liste döner ve hata `son_hatalar` sözlüğüne yazılır; --check bunu raporlar.
"""

from __future__ import annotations

import os
import re
import time
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

import feedparser
import httpx

from .models import Oge, metin_temizle

# Bazı siteler bot UA'larını engelliyor; tarayıcı UA'sı kullanılır.
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
ZAMAN_ASIMI = 20.0
son_hatalar: dict[str, str] = {}


def _istemci() -> httpx.Client:
    return httpx.Client(headers={"User-Agent": UA}, timeout=ZAMAN_ASIMI, follow_redirects=True)


def _iso(dt: datetime | None) -> str:
    if not dt:
        return ""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.isoformat()


def _feed_tarih(e) -> str:
    for alan in ("published", "updated", "created"):
        ham = e.get(alan)
        if ham:
            try:
                return _iso(parsedate_to_datetime(ham))
            except Exception:
                pass
    for alan in ("published_parsed", "updated_parsed"):
        t = e.get(alan)
        if t:
            return _iso(datetime.fromtimestamp(time.mktime(t), tz=timezone.utc))
    return ""


def _anahtar_uyar(metin: str, anahtar: list[str] | None) -> bool:
    if not anahtar:
        return True
    m = metin.lower()
    return any(a.lower() in m for a in anahtar)


def rss(k: dict, since: datetime) -> list[Oge]:
    try:
        with _istemci() as c:
            r = c.get(k["url"])
            r.raise_for_status()
        f = feedparser.parse(r.content)
        if f.bozo and not f.entries:
            raise ValueError(f"RSS ayrıştırılamadı: {f.bozo_exception}")
    except Exception as e:  # noqa: BLE001
        son_hatalar[k["ad"]] = str(e)[:200]
        return []

    ogeler = []
    for e in f.entries:
        tarih = _feed_tarih(e)
        if tarih and datetime.fromisoformat(tarih) < since:
            continue
        ozet = e.get("summary") or (e.get("content") or [{}])[0].get("value", "")
        if not _anahtar_uyar(e.get("title", "") + " " + ozet, k.get("anahtar")):
            continue
        gorsel = None
        for m in e.get("media_content", []) or []:
            if m.get("url"):
                gorsel = m["url"]
                break
        if not gorsel:
            for l in e.get("links", []):
                if l.get("rel") == "enclosure" and str(l.get("type", "")).startswith("image"):
                    gorsel = l.get("href")
        ogeler.append(
            Oge(kaynak=k["ad"], tur="rss", baslik=e.get("title", ""), url=e.get("link", ""), metin=ozet, tarih=tarih, kategori=k["kategori"], gorsel=gorsel)
        )
    return ogeler


def github(k: dict, since: datetime) -> list[Oge]:
    url = f"https://api.github.com/repos/{k['repo']}/releases?per_page=5"
    basliklar = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):  # Actions'ta saatlik 60 istek sınırını aşmamak için
        basliklar["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    try:
        with _istemci() as c:
            r = c.get(url, headers=basliklar)
            r.raise_for_status()
            veri = r.json()
    except Exception as e:  # noqa: BLE001
        son_hatalar[k["ad"]] = str(e)[:200]
        return []
    ogeler = []
    for rel in veri:
        if rel.get("draft") or rel.get("prerelease"):
            continue
        tarih = rel.get("published_at", "")
        if tarih and datetime.fromisoformat(tarih.replace("Z", "+00:00")) < since:
            continue
        ogeler.append(
            Oge(
                kaynak=k["ad"],
                tur="github",
                baslik=f"{k['ad']} {rel.get('name') or rel.get('tag_name')}",
                url=rel["html_url"],
                metin=rel.get("body") or "",
                tarih=tarih,
                kategori=k["kategori"],
                ek={"repo": k["repo"], "tag": rel.get("tag_name")},
            )
        )
    return ogeler


def huggingface(k: dict, since: datetime) -> list[Oge]:
    url = "https://huggingface.co/api/models"
    params = {"pipeline_tag": k["filtre"], "sort": "trendingScore", "direction": "-1", "limit": 15}
    try:
        with _istemci() as c:
            r = c.get(url, params=params)
            r.raise_for_status()
            veri = r.json()
    except Exception as e:  # noqa: BLE001
        son_hatalar[k["ad"]] = str(e)[:200]
        return []
    ogeler = []
    for m in veri:
        tarih = m.get("createdAt") or m.get("lastModified") or ""
        if tarih and datetime.fromisoformat(tarih.replace("Z", "+00:00")) < since - timedelta(days=14):
            # Trend listesinde yeni olmayanları atla (yeni model: son 2 hafta + since penceresi)
            continue
        mid = m["id"]
        if re.search(r"gguf|lora|pruned|quant|nf4|fp8|int8|distill|uncensored|nsfw", mid, re.I):
            continue  # türev/kuantize paketler; asıl model zaten listede
        ogeler.append(
            Oge(
                kaynak=k["ad"],
                tur="huggingface",
                baslik=mid,
                url=f"https://huggingface.co/{mid}",
                metin=f"Hugging Face {k['filtre']} modeli. Beğeni: {m.get('likes', 0)}, indirme: {m.get('downloads', 0)}. Etiketler: {', '.join((m.get('tags') or [])[:12])}",
                tarih=tarih,
                kategori=k["kategori"],
                ek={"likes": m.get("likes", 0), "downloads": m.get("downloads", 0), "pipeline": k["filtre"]},
            )
        )
    return ogeler


def arxiv(k: dict, since: datetime) -> list[Oge]:
    url = "http://export.arxiv.org/api/query"
    params = {"search_query": k["sorgu"], "sortBy": "submittedDate", "sortOrder": "descending", "max_results": k.get("limit", 25)}
    try:
        with _istemci() as c:
            r = c.get(url, params=params)
            r.raise_for_status()
        f = feedparser.parse(r.content)
    except Exception as e:  # noqa: BLE001
        son_hatalar[k["ad"]] = str(e)[:200]
        return []
    ogeler = []
    for e in f.entries:
        tarih = _feed_tarih(e)
        if tarih and datetime.fromisoformat(tarih) < since:
            continue
        ogeler.append(
            Oge(
                kaynak=k["ad"],
                tur="arxiv",
                baslik=e.get("title", ""),
                url=e.get("link", ""),
                metin=e.get("summary", ""),
                tarih=tarih,
                kategori=k["kategori"],
                ek={"yazarlar": [a.get("name") for a in e.get("authors", [])][:5]},
            )
        )
    return ogeler


def reddit(k: dict, since: datetime) -> list[Oge]:
    """Reddit JSON API'si bot isteklerini engelliyor; günün en iyileri RSS ile alınır."""
    url = f"https://www.reddit.com/r/{k['sub']}/top/.rss"
    try:
        with _istemci() as c:
            for deneme in range(3):
                r = c.get(url, params={"t": "day"})
                if r.status_code != 429:
                    break
                time.sleep(5 * (deneme + 1))  # Reddit hız sınırı: bekle ve yeniden dene
            r.raise_for_status()
        time.sleep(2)  # ardışık subreddit istekleri arasında nefes
        f = feedparser.parse(r.content)
        if not f.entries and f.bozo:
            raise ValueError(f"RSS ayrıştırılamadı: {f.bozo_exception}")
    except Exception as e:  # noqa: BLE001
        son_hatalar[k["ad"]] = str(e)[:200]
        return []
    ogeler = []
    for e in f.entries[: k.get("limit", 8)]:
        tarih = _feed_tarih(e)
        if tarih and datetime.fromisoformat(tarih) < since:
            continue
        icerik = (e.get("content") or [{}])[0].get("value", "") or e.get("summary", "")
        gorsel = None
        m = re.search(r'https://(?:i\.redd\.it|preview\.redd\.it)/[^"\s<]+', icerik)
        if m:
            gorsel = m.group(0).replace("&amp;", "&")
        ogeler.append(
            Oge(
                kaynak=k["ad"],
                tur="reddit",
                baslik=e.get("title", ""),
                url=e.get("link", ""),
                metin=icerik,
                tarih=tarih,
                kategori=k["kategori"],
                gorsel=gorsel,
                ek={"yazar": e.get("author", "")},
            )
        )
    return ogeler


def sayfa(k: dict, since: datetime) -> list[Oge]:
    """RSS vermeyen şirket haber sayfaları: sayfadaki yazı bağlantılarını okur.

    Tarih bilgisi olmadığından her bağlantı yeni sayılır; tekrar ayıklama seen.json ile yapılır
    (ilk çalıştırmada var olanlar da aday olur, puanlama eleği eskiyi düşürür).
    k: ad, url, kategori, desen (bağlantı yolu için regex), dom (true: başsız Chrome).
    """
    import html as _html
    import re as _re
    from urllib.parse import urljoin, urlparse

    try:
        if k.get("dom"):
            from .kapak import _dom
            metin = _dom(k["url"]) or ""
        else:
            with _istemci() as c:
                r = c.get(k["url"])
                r.raise_for_status()
                metin = r.text
    except Exception as e:  # noqa: BLE001
        son_hatalar[k["ad"]] = str(e)[:120]
        return []
    if not metin:
        son_hatalar[k["ad"]] = "sayfa boş"
        return []
    desen = _re.compile(k.get("desen", r"/(blog|news|research|changelog|updates?)/[^/?#]+"), _re.I)
    alan = urlparse(k["url"]).netloc.removeprefix("www.")
    gorulen: set[str] = set()
    ogeler: list[Oge] = []
    for m in _re.finditer(r'<a\b[^>]*href=["\']([^"\'#]+)["\'][^>]*>(.*?)</a>', metin, _re.S | _re.I):
        url = urljoin(k["url"], m.group(1))
        u = urlparse(url)
        if u.netloc.removeprefix("www.") != alan or not desen.search(u.path) or url.rstrip("/") == k["url"].rstrip("/"):
            continue
        baslik = _re.sub(r"\s+", " ", _html.unescape(_re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
        if len(baslik) < 12 or url in gorulen:
            continue
        gorulen.add(url)
        ogeler.append(Oge(kaynak=k["ad"], tur="sayfa", baslik=baslik[:200], url=url, metin="", tarih="", kategori=k["kategori"]))
        if len(ogeler) >= k.get("limit", 12):
            break
    return ogeler


ADAPTORLER = {"rss": rss, "github": github, "huggingface": huggingface, "arxiv": arxiv, "reddit": reddit, "sayfa": sayfa}


def hepsini_topla(kaynaklar: dict, since: datetime) -> tuple[list[Oge], dict[str, int]]:
    """sources.yaml içeriğini gezer; (öğeler, kaynak başına sayı) döndürür."""
    son_hatalar.clear()
    ogeler: list[Oge] = []
    sayac: dict[str, int] = {}
    for tur, liste in kaynaklar.items():
        adaptor = ADAPTORLER.get(tur)
        if not adaptor:
            continue
        for k in liste or []:
            bulunan = adaptor(k, since)
            sayac[k["ad"]] = len(bulunan)
            ogeler.extend(bulunan)
    return ogeler, sayac


def og_gorsel(url: str) -> str | None:
    """Sayfanın og:image adresini bulur (haber kapağı için)."""
    try:
        with _istemci() as c:
            r = c.get(url)
            r.raise_for_status()
        m = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)', r.text, re.I) or re.search(
            r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', r.text, re.I
        )
        return m.group(1) if m else None
    except Exception:  # noqa: BLE001
        return None
