"""AI çıktısını content/haberler altına Markdown olarak yazar; kapağı indirir.

Karma yayın: her haber content/haberler altına yazılır; hangilerinin doğrudan
yayınlanacağı, hangilerinin onay PR'ına gideceği data/son_calistirma.json'a
yazılır ve collect.yml bu listeye göre commit/PR yapar.
  puan >= YAYIN_ESIGI  -> "yayin"  (main'e commit)
  ONAY_ESIGI <= puan   -> "onay"   (PR; merge = yayın)
  altı                 -> yazılmaz, seen.json'a 'atildi' olarak işlenir
"""

from __future__ import annotations

import io
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import httpx
import yaml
from PIL import Image
from slugify import slugify

from . import dedupe, fetch
from .ai import Eleme, Haber, ONAY_ESIGI, YAYIN_ESIGI
from .models import Oge

KOK = Path(__file__).resolve().parent.parent
HABERLER = KOK / "content" / "haberler"
MANIFEST = KOK / "data" / "son_calistirma.json"
KAPAK_GENISLIK = 1600
KAPAK_MAKS_BAYT = 400_000


def _kapak_indir(url: str, hedef: Path) -> bool:
    """og:image'ı indirir, 1600px genişliğe küçültür, webp kaydeder."""
    try:
        with httpx.Client(headers={"User-Agent": fetch.UA}, timeout=20, follow_redirects=True) as c:
            r = c.get(url)
            r.raise_for_status()
        im = Image.open(io.BytesIO(r.content))
        im = im.convert("RGB")
        if im.width < 600 or im.height < 300:
            return False  # ikon/avatar boyutunda; kapak olmaz
        if im.width > KAPAK_GENISLIK:
            im = im.resize((KAPAK_GENISLIK, round(im.height * KAPAK_GENISLIK / im.width)), Image.LANCZOS)
        hedef.parent.mkdir(parents=True, exist_ok=True)
        for q in (82, 70, 55):
            im.save(hedef, "WEBP", quality=q, method=6)
            if hedef.stat().st_size <= KAPAK_MAKS_BAYT:
                break
        return True
    except Exception as e:  # noqa: BLE001
        print(f"  kapak indirilemedi ({url[:60]}): {e}", file=sys.stderr)
        return False


def _frontmatter(h: Haber, grup: list[Oge], e: Eleme, kapak: str | None, kapak_kaynak: str | None) -> dict:
    o = grup[0]
    tarih = (o.tarih or datetime.now(timezone.utc).isoformat())[:10]
    fm: dict = {
        "baslik": h.baslik,
        "tarih": tarih,
        "kategori": h.kategori,
        "puan": e.puan,
        "ozet": h.ozet,
        "neden_onemli": h.neden_onemli,
        "yekvisual_notu": h.yekvisual_notu,
        "ucretsiz": h.ucretsiz,
        "acik_kaynak": h.acik_kaynak,
        "zorluk": h.zorluk,
        "etiketler": h.etiketler,
    }
    if h.sirket:
        fm["sirket"] = h.sirket
    if h.model:
        fm["model"] = h.model
    if h.kart:
        fm["kart"] = h.kart
    if kapak:
        fm["kapak"] = kapak
        fm["kapak_kaynak"] = kapak_kaynak or f"Görsel: {o.kaynak}"
    if h.youtube:
        fm["medya"] = [{"tip": "youtube", "src": h.youtube, "alt": "Tanıtım videosu", "kaynak": h.sirket or o.kaynak}]
    gorulen = set()
    fm["kaynaklar"] = []
    for k in grup[:5]:
        if k.url in gorulen:
            continue
        gorulen.add(k.url)
        fm["kaynaklar"].append({"ad": k.kaynak, "url": k.url})
    return fm


def _yaz(hedef: Path, fm: dict, govde: str) -> None:
    hedef.parent.mkdir(parents=True, exist_ok=True)
    on = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000)
    hedef.write_text(f"---\n{on}---\n\n{govde.strip()}\n")


def uygula(sonuclar: list[tuple[Eleme, Haber | None]], gruplar: list[list[Oge]], seen: dict, dry_run: bool = False):
    yayin, onay, atilan = [], [], []
    simdi = datetime.now(timezone.utc)
    for (e, h), grup in zip(sonuclar, gruplar):
        o = grup[0]
        if h is None:
            atilan.append(o)
            for k in grup:
                dedupe.isaretle(seen, k, "atildi", {"puan": e.puan})
            print(f"  ✗ {e.puan} {o.baslik[:70]}  ({e.gerekce[:60]})", file=sys.stderr)
            continue

        kok = HABERLER
        slug = slugify(h.slug or h.baslik)[:60]
        tarih = (o.tarih or simdi.isoformat())[:10]
        yil, ay = tarih[:4], tarih[5:7]
        hedef = kok / yil / ay / f"{slug}.md"
        if hedef.exists():
            hedef = kok / yil / ay / f"{slug}-{o.id[:4]}.md"
        isaret = "★" if e.puan >= YAYIN_ESIGI else "?"
        print(f"  {isaret} {e.puan} {h.baslik}  → {hedef.relative_to(KOK)}", file=sys.stderr)

        kapak = kapak_kaynak = None
        if not dry_run:
            kapak_yolu = hedef.parent / hedef.stem / "kapak.webp"
            gorsel_url = o.gorsel or (fetch.og_gorsel(o.url) if o.tur in ("rss", "github", "huggingface") else None)
            if gorsel_url and _kapak_indir(gorsel_url, kapak_yolu):
                kapak = f"./{hedef.stem}/kapak.webp"
                kapak_kaynak = f"Görsel: {h.sirket or o.kaynak}"
            else:
                # Betikle yüklenen sayfalar için başsız Chrome + video karesi
                from . import kapak as kapak_bulucu
                if kapak_bulucu.bul([k.url for k in grup if k.url], kapak_yolu):
                    kapak = f"./{hedef.stem}/kapak.webp"
                    kapak_kaynak = f"Görsel: {h.sirket or o.kaynak}"
            _yaz(hedef, _frontmatter(h, grup, e, kapak, kapak_kaynak), h.govde)

        # Kural: görselsiz haber yayınlanmaz. Kapak yoksa puanı ne olursa olsun onaya düşer;
        # onay PR'ında kapak eklenmeden birleştirilirse site derlemesi başarısız olur.
        if not dry_run and not kapak:
            print(f"    ! kapak bulunamadı, onaya düştü: {hedef.name}", file=sys.stderr)
            onay.append(hedef)
            for k in grup:
                dedupe.isaretle(seen, k, "onay", {"puan": e.puan, "dosya": str(hedef.relative_to(KOK)), "kapak": False})
            continue
        (yayin if e.puan >= YAYIN_ESIGI else onay).append(hedef)
        for k in grup:
            dedupe.isaretle(seen, k, "yayin" if e.puan >= YAYIN_ESIGI else "onay", {"puan": e.puan, "dosya": str(hedef.relative_to(KOK))})
    if not dry_run:
        import json

        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(
            json.dumps(
                {
                    "zaman": simdi.isoformat(),
                    "yayin": [str(p.relative_to(KOK)) for p in yayin],
                    "onay": [str(p.relative_to(KOK)) for p in onay],
                    "atilan": len(atilan),
                },
                ensure_ascii=False,
                indent=1,
            )
            + "\n"
        )
    return yayin, onay, atilan
