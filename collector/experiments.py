"""Denemeler: denemeler/gelen/<ad>/ klasörlerini ilgili habere "Ben denedim" olarak ekler.

Klasör adı modelin/aracın adı olmalı (örn. "veo-3", "flux-kontext"). İçinde:
  - görseller (jpg/png/webp) ve/veya videolar (mp4/mov)
  - prompt.txt (isteğe bağlı: kullanılan prompt ve kısa not)
Eşleşen haber bulunamazsa content/haberler altında ayrı bir "Deneme" yazısı açılır.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic
import yaml
from PIL import Image
from pydantic import BaseModel, Field
from slugify import slugify

KOK = Path(__file__).resolve().parent.parent
GELEN = KOK / "denemeler" / "gelen"
ISLENDI = KOK / "denemeler" / "islendi"
HABERLER = KOK / "content" / "haberler"
USLUP = (KOK / "style" / "uslup.md").read_text()
MODEL = os.environ.get("YAZIM_MODEL", "claude-sonnet-5-5")
GORSEL = {".jpg", ".jpeg", ".png", ".webp"}
VIDEO = {".mp4", ".mov", ".webm", ".m4v"}
VIDEO_MAKS_SN = 8
VIDEO_MAKS_BAYT = 5_000_000


class Eslesme(BaseModel):
    haber_id: str | None = Field(description="Listeden eşleşen haberin id'si; hiçbiri uymuyorsa null")
    metin: str = Field(description="'Ben denedim' bölümü: 2–5 cümle, birinci tekil şahıs, prompt'u ve gözlemi anlatır. Üslup rehberine uygun.")
    baslik: str = Field(description="Eşleşme yoksa yeni deneme yazısının başlığı; varsa boş")
    kategori: str = Field(description="gorsel | video | ses | 3d | araclar | acik-kaynak | otomasyon")


def _haberler(son_gun: int = 45) -> list[tuple[Path, dict, str]]:
    esik = datetime.now(timezone.utc).timestamp() - son_gun * 86400
    out = []
    for p in HABERLER.rglob("*.md"):
        if p.stat().st_mtime < esik:
            continue
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", p.read_text(), re.S)
        if m:
            out.append((p, yaml.safe_load(m.group(1)), m.group(2)))
    return out


def _gorsel_sikistir(src: Path, hedef: Path) -> None:
    im = Image.open(src).convert("RGB")
    if im.width > 1600:
        im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    im.save(hedef, "WEBP", quality=80, method=6)


def _video_sikistir(src: Path, hedef: Path) -> None:
    """Kısa, sessiz, 720p mp4 döngü. ffmpeg gerekir."""
    cmd = [
        "ffmpeg", "-y", "-i", str(src), "-t", str(VIDEO_MAKS_SN), "-an",
        "-vf", "scale='min(1280,iw)':-2", "-c:v", "libx264", "-crf", "28", "-preset", "slow",
        "-movflags", "+faststart", "-pix_fmt", "yuv420p", str(hedef),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    if hedef.stat().st_size > VIDEO_MAKS_BAYT:
        cmd[cmd.index("-crf") + 1] = "34"
        subprocess.run(cmd, check=True, capture_output=True)


def isle_klasor(klasor: Path, client: anthropic.Anthropic) -> None:
    ad = klasor.name
    prompt = (klasor / "prompt.txt").read_text() if (klasor / "prompt.txt").exists() else ""
    dosyalar = sorted(p for p in klasor.iterdir() if p.suffix.lower() in GORSEL | VIDEO)
    if not dosyalar:
        print(f"  {ad}: medya yok, atlandı", file=sys.stderr)
        return

    haberler = _haberler()
    liste = "\n".join(f"- id: {str(p.relative_to(HABERLER)).removesuffix('.md')} | {fm['baslik']} | model: {fm.get('model', '')} | şirket: {fm.get('sirket', '')}" for p, fm, _ in haberler)
    r = client.messages.parse(
        model=MODEL,
        max_tokens=2000,
        system=f"Sen yekvisual'sın; kendi denemeni anlatıyorsun. Üslup rehberi:\n\n{USLUP}",
        messages=[
            {
                "role": "user",
                "content": f"Deneme klasörü: '{ad}'. {len(dosyalar)} medya dosyası ({', '.join(p.suffix for p in dosyalar)}).\nNot/prompt:\n{prompt or '(yok)'}\n\nSon haberler:\n{liste or '(yok)'}\n\nBu deneme hangi habere ait? 'Ben denedim' metnini yaz.",
            }
        ],
        output_format=Eslesme,
    )
    es = r.parsed_output

    if es.haber_id:
        hedef = HABERLER / f"{es.haber_id}.md"
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", hedef.read_text(), re.S)
        fm, govde = yaml.safe_load(m.group(1)), m.group(2)
    else:
        bugun = datetime.now(timezone.utc)
        slug = slugify(es.baslik or f"deneme-{ad}")[:60]
        hedef = HABERLER / f"{bugun:%Y}" / f"{bugun:%m}" / f"{slug}.md"
        fm = {
            "baslik": es.baslik or f"Denedim: {ad}",
            "tarih": f"{bugun:%Y-%m-%d}",
            "kategori": es.kategori,
            "puan": 3,
            "ozet": es.metin.split(". ")[0] + ".",
            "zorluk": "yeni",
            "etiketler": ["deneme", ad],
            "kaynaklar": [],
        }
        govde = ""

    medya_dir = hedef.parent / hedef.stem
    medya_dir.mkdir(parents=True, exist_ok=True)
    girdiler = fm.get("denemeler") or []
    for i, src in enumerate(dosyalar, 1):
        if src.suffix.lower() in GORSEL:
            out = medya_dir / f"deneme-{i}.webp"
            _gorsel_sikistir(src, out)
            girdiler.append({"tip": "gorsel", "src": f"./{hedef.stem}/{out.name}", "alt": f"Deneme {i}", "kaynak": "yekvisual"})
        else:
            out = medya_dir / f"deneme-{i}.mp4"
            try:
                _video_sikistir(src, out)
                girdiler.append({"tip": "video", "src": f"./{hedef.stem}/{out.name}", "alt": f"Deneme {i}", "kaynak": "yekvisual"})
            except Exception as e:  # noqa: BLE001
                print(f"  video sıkıştırılamadı {src.name}: {e}", file=sys.stderr)
    fm["denemeler"] = girdiler
    fm["yekvisual_notu"] = fm.get("yekvisual_notu") or es.metin
    if "## Ben denedim" not in govde:
        govde = govde.rstrip() + f"\n\n## Ben denedim\n\n{es.metin}\n" + (f"\n**Prompt:** {prompt.strip()}\n" if prompt.strip() else "")
    on = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000)
    hedef.write_text(f"---\n{on}---\n\n{govde.strip()}\n")

    ISLENDI.mkdir(parents=True, exist_ok=True)
    shutil.move(str(klasor), str(ISLENDI / f"{datetime.now(timezone.utc):%Y%m%d}-{ad}"))
    print(f"  ✓ {ad} → {hedef.relative_to(KOK)}", file=sys.stderr)


def main() -> int:
    if not GELEN.exists():
        return 0
    klasorler = [p for p in GELEN.iterdir() if p.is_dir()]
    if not klasorler:
        print("İşlenecek deneme yok.", file=sys.stderr)
        return 0
    client = anthropic.Anthropic()
    for k in klasorler:
        isle_klasor(k, client)
    return 0


if __name__ == "__main__":
    sys.exit(main())
