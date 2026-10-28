"""Kapak görseli bulucu.

Bir haber için verilen kaynak sayfalardan gerçek bir görsel çıkarır:
  1. Sayfanın og:image / twitter:image etiketi (httpx ile).
  2. Sayfa betikle yükleniyorsa başsız Chrome ile DOM'u alıp og:image, en büyük <img>
     ya da ilk <video> kaynağını bulur; videodan ffmpeg ile kare alır.
Sonuç 16:10 kırpılmış, en fazla 1536 px genişlikte webp olarak kaydedilir.

Komut satırı:  python -m collector.kapak <hedef.webp> <url> [url ...]
Çıkış kodu 0 = kapak kaydedildi, 1 = bulunamadı.
"""

from __future__ import annotations

import io
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import httpx
from PIL import Image

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
MIN_GENISLIK = 700
MIN_YUKSEKLIK = 360
GENISLIK = 1536
ORAN = 16 / 10
ATLA = re.compile(r"logo|icon|avatar|favicon|sprite|badge|button|emoji|1x1|pixel|tracking|cdn-thumbnails\.huggingface|opengraph\.githubassets|social-thumbnails|/og-image|opengraph", re.I)
CHROME_ADAYLARI = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
]


def _chrome() -> str | None:
    for c in CHROME_ADAYLARI:
        if c.startswith("/") and Path(c).exists():
            return c
        if not c.startswith("/") and shutil.which(c):
            return c
    return None


def _indir(url: str) -> bytes | None:
    try:
        with httpx.Client(headers={"User-Agent": UA}, timeout=30, follow_redirects=True) as c:
            r = c.get(url)
            r.raise_for_status()
            return r.content
    except Exception as e:  # noqa: BLE001
        print(f"  indirilemedi ({url[:70]}): {e}", file=sys.stderr)
        return None


def _meta_gorsel(html: str) -> str | None:
    for pat in (
        r'property=["\']og:image(?::secure_url)?["\'][^>]*?content=["\']([^"\']+)',
        r'content=["\']([^"\']+)["\'][^>]*?property=["\']og:image',
        r'name=["\']twitter:image["\'][^>]*?content=["\']([^"\']+)',
    ):
        m = re.search(pat, html, re.I)
        if m and m.group(1).startswith("http"):
            return m.group(1)
    return None


def _dom(url: str) -> str | None:
    chrome = _chrome()
    if not chrome:
        return None
    with tempfile.TemporaryDirectory() as td:
        try:
            r = subprocess.run(
                [chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-first-run", f"--user-data-dir={td}",
                 "--virtual-time-budget=15000", "--window-size=1600,1000", "--dump-dom", url],
                capture_output=True, text=True, timeout=90,
            )
            return r.stdout if r.stdout and len(r.stdout) > 2000 else None
        except Exception as e:  # noqa: BLE001
            print(f"  chrome dom alınamadı: {e}", file=sys.stderr)
            return None


def _adaylar(html: str, taban: str) -> list[str]:
    """DOM'dan görsel ve video adayları (büyük olanlar önce; sıra korunur)."""
    urls: list[str] = []
    for m in re.finditer(r'<(img|video|source)[^>]+(?:src|srcset|poster)=["\']([^"\']+)', html, re.I):
        u = m.group(2).split()[0]
        if u.startswith("//"):
            u = "https:" + u
        elif u.startswith("/"):
            u = re.match(r"https?://[^/]+", taban).group(0) + u
        if not u.startswith("http") or ATLA.search(u):
            continue
        if u not in urls:
            urls.append(u)
    # Düz metin içindeki medya adresleri (betikle yüklenenler)
    for m in re.finditer(r'https://[^\s"\'<>)]+\.(?:jpg|jpeg|png|webp|mp4|webm)(?:\?[^\s"\'<>)]*)?', html, re.I):
        u = m.group(0).split("#")[0]
        if not ATLA.search(u) and u not in urls:
            urls.append(u)
    return urls[:40]


def _duz_mu(im: Image.Image) -> bool:
    """Logo/kartvizit gibi tek renk ağırlıklı görseller: piksel sapması düşük."""
    from PIL import ImageStat
    k = im.convert("L").resize((160, 100))
    return sum(ImageStat.Stat(k).stddev) < 28


def _kaydet(im: Image.Image, hedef: Path) -> bool:
    im = im.convert("RGB")
    if im.width < MIN_GENISLIK or im.height < MIN_YUKSEKLIK:
        return False
    if _duz_mu(im):
        print("  düz/logo görsel atlandı", file=sys.stderr)
        return False
    if im.width > GENISLIK:
        im = im.resize((GENISLIK, round(im.height * GENISLIK / im.width)), Image.LANCZOS)
    w, h = im.size
    th = round(w / ORAN)
    if h >= th:
        y = (h - th) // 2
        im = im.crop((0, y, w, y + th))
    else:
        tw = round(h * ORAN)
        x = (w - tw) // 2
        im = im.crop((x, 0, x + tw, h))
        if im.width < MIN_GENISLIK:
            return False
    hedef.parent.mkdir(parents=True, exist_ok=True)
    for q in (84, 72, 60):
        im.save(hedef, "WEBP", quality=q, method=6)
        if hedef.stat().st_size <= 400_000:
            break
    return True


def _video_kare(url: str, hedef: Path) -> bool:
    if not shutil.which("ffmpeg"):
        return False
    with tempfile.TemporaryDirectory() as td:
        kare = Path(td) / "kare.jpg"
        try:
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "3", "-i", url, "-frames:v", "1", "-q:v", "2", str(kare)],
                           timeout=120, check=True)
            return _kaydet(Image.open(kare), hedef)
        except Exception as e:  # noqa: BLE001
            print(f"  video karesi alınamadı: {e}", file=sys.stderr)
            return False


def _gorsel_dene(url: str, hedef: Path) -> bool:
    if re.search(r"\.(mp4|webm)(\?|$)", url, re.I):
        return _video_kare(url, hedef)
    veri = _indir(url)
    if not veri:
        return False
    try:
        return _kaydet(Image.open(io.BytesIO(veri)), hedef)
    except Exception:  # noqa: BLE001
        return False


def bul(urls: list[str], hedef: Path, sayfa_ici: bool = False) -> str | None:
    """Sırayla kaynakları dener; başarılıysa kullanılan görsel adresini döndürür.
    sayfa_ici=True: og:image'ı atlar, sayfadaki büyük medyayı (görsel/video) kullanır."""
    for url in urls:
        if not url.startswith("http"):
            continue
        html = _indir(url)
        html = html.decode("utf-8", "ignore") if html else ""
        og = _meta_gorsel(html) if html and not sayfa_ici else None
        if og and _gorsel_dene(og, hedef):
            return og
        dom = _dom(url)
        if not dom:
            continue
        og = None if sayfa_ici else _meta_gorsel(dom)
        adaylar = ([og] if og else []) + _adaylar(dom, url)
        for a in adaylar[:12]:
            if _gorsel_dene(a, hedef):
                return a
    return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    args = sys.argv[2:]
    sayfa_ici = "--sayfa" in args
    args = [a for a in args if a != "--sayfa"]
    sonuc = bul(args, Path(sys.argv[1]), sayfa_ici)
    print(sonuc or "KAPAK BULUNAMADI")
    sys.exit(0 if sonuc else 1)
