"""Claude katmanı: (1) eleme + puan, (2) Türkçe yazım + yekvisual notu.

Modeller ortam değişkeniyle değiştirilebilir:
  ELEME_MODEL  (varsayılan claude-haiku-4-5)   ucuz, toplu
  YAZIM_MODEL  (varsayılan claude-sonnet-5-5)  yalnızca puan >= 2 olanlar
Daha iyi metin için YAZIM_MODEL=claude-opus-5-5 yeterli.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Literal

import anthropic
from pydantic import BaseModel, Field

from .models import Oge

KOK = Path(__file__).resolve().parent.parent
USLUP = (KOK / "style" / "uslup.md").read_text()
KARTLAR = [p.stem for p in (KOK / "content" / "kartlar").glob("*.md")]

ELEME_MODEL = os.environ.get("ELEME_MODEL", "claude-haiku-4-5")
YAZIM_MODEL = os.environ.get("YAZIM_MODEL", "claude-sonnet-5-5")
ELEME_PARTI = 15
YAYIN_ESIGI = 4  # >= doğrudan yayın
ONAY_ESIGI = 2  # >= onay PR'ı; altı atılır

Kategori = Literal["gorsel", "video", "ses", "3d", "araclar", "acik-kaynak", "otomasyon", "arastirma"]
Zorluk = Literal["yeni", "orta", "teknik"]

client = anthropic.Anthropic()

# Toplam kullanım; main sonunda maliyet tahmini için yazdırılır.
kullanim = {"eleme_in": 0, "eleme_out": 0, "yazim_in": 0, "yazim_out": 0}


class Eleme(BaseModel):
    i: int = Field(description="Öğenin listedeki sıra numarası")
    alakali: bool = Field(description="Yapay zekâ ile görsel/video/ses/3D üretimi, içerik üretim araçları ya da Claude/ajan otomasyonu ile ilgili mi?")
    puan: int = Field(ge=0, le=5, description="Önem: 5 = herkesin bilmesi gereken büyük çıkış; 4 = önemli yeni model/özellik; 3 = ilginç ama niş; 2 = küçük güncelleme; 1 = önemsiz; 0 = alakasız/spam")
    kategori: Kategori
    gerekce: str = Field(description="Tek cümle")


class ElemeListesi(BaseModel):
    sonuclar: list[Eleme]


class Kaynak(BaseModel):
    ad: str
    url: str


class Haber(BaseModel):
    baslik: str = Field(description="50–80 karakter, Türkçe")
    slug: str = Field(description="URL için küçük harf, tire ile ayrılmış, ASCII, en fazla 60 karakter")
    ozet: str = Field(description="2–4 cümle; ne çıktı, kim çıkardı, ne yapıyor")
    neden_onemli: str = Field(description="1–3 cümle; okurun işine nasıl yarar")
    yekvisual_notu: str = Field(description="1–3 cümle, birinci tekil şahıs, üslup rehberine uygun")
    govde: str = Field(description="Markdown; 'Neler yeni?', 'Nasıl denenir?', 'Sınırlar' gibi 2–3 kısa başlık. Toplam 80–200 kelime. Kaynakta olmayan bilgi yok.")
    kategori: Kategori
    zorluk: Zorluk
    ucretsiz: bool | None = Field(description="Ücretsiz katman var mı; bilinmiyorsa null")
    acik_kaynak: bool | None = Field(description="Ağırlıklar/kod açık mı; bilinmiyorsa null")
    sirket: str | None
    model: str | None = Field(description="Model ya da ürün adı")
    etiketler: list[str] = Field(description="3–6 küçük harf etiket")
    kart: str | None = Field(description=f"İlgili başlangıç kartı; şunlardan biri ya da null: {', '.join(KARTLAR)}")
    youtube: str | None = Field(description="Kaynak metinde geçen bir YouTube tanıtım linki varsa, yoksa null")


ELEME_SISTEM = f"""Sen yekvisual.github.io için haber eleyicisin. Site, yapay zekâ ile GÖRSEL, VİDEO, SES, 3D ve içerik üretimini; bu iş için araçları; Claude ve ajanlarla otomasyonu takip eder. Okur: sıfırdan başlayanlar ve içerik üreticileri.

Alakalı: yeni görsel/video/ses/3D modelleri, bunların yeni özellikleri, ücretsiz ya da açık kaynak çıkışlar, ComfyUI/Remotion/DaVinci gibi araçların önemli sürümleri, Canva/Adobe gibi uygulamalara gelen üretken özellikler, Claude Code / ajan otomasyonu gelişmeleri, içerik üreticisinin işini değiştirecek şeyler.
Alakasız: genel LLM haberleri (sohbet modeli çıkışı, benchmark), kurumsal anlaşmalar, finans, yalnızca metin üretimi, güvenlik, politika, kişisel paylaşımlar, reklam, ufak hata düzeltmeleri.

Puanlama katı olsun: 5 çok nadirdir (ayda 1–2). Reddit/HF gibi topluluk kaynaklarında gerçek bir model/araç çıkışı yoksa en fazla 2.
Kategori: gorsel, video, ses, 3d, araclar (uygulama/servis), acik-kaynak (yerelde çalışan model), otomasyon (Claude/ajan/bot), arastirma (makale)."""

YAZIM_SISTEM = f"""Sen yekvisual'ın yazarısın. Aşağıdaki üslup rehberine harfiyen uy. Verilen kaynak metinlerden Türkçe bir haber üret. Kaynakta olmayan hiçbir sayı, tarih, özellik ya da fiyat ekleme; bilmiyorsan null bırak ya da "belirtilmemiş" de.

{USLUP}"""


def _metin(o: Oge, limit: int = 1500) -> str:
    return f"Kaynak: {o.kaynak} ({o.tur})\nBaşlık: {o.baslik}\nURL: {o.url}\nTarih: {o.tarih[:10]}\nMetin: {o.metin[:limit]}\nEk: {json.dumps(o.ek, ensure_ascii=False)[:300]}"


def ele(gruplar: list[list[Oge]]) -> list[Eleme]:
    """Grupları partiler halinde eler. Sonuç listesi gruplarla aynı sırada."""
    sonuc: list[Eleme] = []
    for p in range(0, len(gruplar), ELEME_PARTI):
        parti = gruplar[p : p + ELEME_PARTI]
        liste = "\n\n".join(f"### {i}\n{_metin(g[0], 700)}" + (f"\nAynı olay için {len(g) - 1} ek kaynak var." if len(g) > 1 else "") for i, g in enumerate(parti))
        r = client.messages.parse(
            model=ELEME_MODEL,
            max_tokens=4000,
            system=ELEME_SISTEM,
            messages=[{"role": "user", "content": f"Her öğe için karar ver. {len(parti)} öğe var, hepsini döndür.\n\n{liste}"}],
            output_format=ElemeListesi,
        )
        kullanim["eleme_in"] += r.usage.input_tokens
        kullanim["eleme_out"] += r.usage.output_tokens
        harita = {e.i: e for e in r.parsed_output.sonuclar}
        for i in range(len(parti)):
            sonuc.append(harita.get(i) or Eleme(i=i, alakali=False, puan=0, kategori=parti[i][0].kategori, gerekce="cevap yok"))
    return sonuc


def yaz(grup: list[Oge], eleme: Eleme) -> Haber:
    kaynaklar = "\n\n".join(f"--- Kaynak {i + 1} ---\n{_metin(o)}" for i, o in enumerate(grup[:4]))
    r = client.messages.parse(
        model=YAZIM_MODEL,
        max_tokens=4000,
        system=YAZIM_SISTEM,
        messages=[
            {
                "role": "user",
                "content": f"Eleme notu: puan {eleme.puan}/5, kategori {eleme.kategori}, gerekçe: {eleme.gerekce}\n\n{kaynaklar}\n\nBu kaynaklardan tek bir Türkçe haber yaz.",
            }
        ],
        output_format=Haber,
    )
    kullanim["yazim_in"] += r.usage.input_tokens
    kullanim["yazim_out"] += r.usage.output_tokens
    return r.parsed_output


def isle(gruplar: list[list[Oge]]) -> list[tuple[Eleme, Haber | None]]:
    """Tüm grupları eler, eşiği geçenleri yazar. Gruplarla aynı sırada döner."""
    elemeler = ele(gruplar)
    sonuc: list[tuple[Eleme, Haber | None]] = []
    for g, e in zip(gruplar, elemeler):
        if e.alakali and e.puan >= ONAY_ESIGI:
            try:
                sonuc.append((e, yaz(g, e)))
            except anthropic.APIError as hata:
                print(f"  ! yazım hatası ({g[0].baslik[:50]}): {hata}", file=sys.stderr)
                sonuc.append((e, None))
        else:
            sonuc.append((e, None))
    print(
        f"Token: eleme {kullanim['eleme_in']}/{kullanim['eleme_out']}, yazım {kullanim['yazim_in']}/{kullanim['yazim_out']}  ·  ~${maliyet():.3f}",
        file=sys.stderr,
    )
    return sonuc


# $/1M token; claude-api referansından (2026-09). Model değişirse güncelle.
FIYAT = {
    "claude-haiku-4-5": (1.0, 5.0),
    "claude-sonnet-5-5": (2.0, 10.0),
    "claude-opus-5-5": (4.0, 20.0),
}


def maliyet() -> float:
    ei, eo = FIYAT.get(ELEME_MODEL, (4.0, 20.0))
    yi, yo = FIYAT.get(YAZIM_MODEL, (4.0, 20.0))
    return (kullanim["eleme_in"] * ei + kullanim["eleme_out"] * eo + kullanim["yazim_in"] * yi + kullanim["yazim_out"] * yo) / 1e6
