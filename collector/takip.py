"""Takip: belirli sayfalardaki konuyla ilgili cümleleri izler, değişince GitHub issue açar.

Her takip: ad, haber dosyası, sayfalar ve anahtar kelime. Sayfadaki anahtar kelimeyi içeren
cümleler data/takip.json'da saklanır; bir sonraki çalıştırmada fark varsa (eklenen/çıkan cümle)
ve "tetik" kelimelerinden biri yeni cümlelerde geçiyorsa issue açılır.

  python -m collector.takip            # kontrol et, değişiklik varsa issue aç
  python -m collector.takip --kuru     # yalnızca göster
"""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import httpx

KOK = Path(__file__).resolve().parent.parent
DURUM = KOK / "data" / "takip.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/130 Safari/537.36"

TAKIPLER = [
    {
        "ad": "genie-4-erisim",
        "haber": "content/haberler/2026/10/genie-4.md",
        "baslik": "Genie 4 erişimi değişti: Pro/Ultra kullanıcılarına açılmış olabilir",
        "anahtar": r"genie",
        # Bu kelimelerden biri YENİ bir cümlede geçerse haber güncellenmeli
        "tetik": r"genie 4|ai pro|google ai pro|now available|available now|kullanıma sunuldu|artık|rolling out|kullanılabilir",
        "sayfalar": [
            "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/",
            "https://one.google.com/about/google-ai-plans/",
            "https://gemini.google/subscriptions/",
            "https://labs.google/projectgenie",
        ],
    },
    {
        "ad": "kimi-k3-1-agirliklar",
        "haber": "content/haberler/2026/10/kimi-k3-1-pro.md",
        "baslik": "Kimi K3.1 ağırlıkları Hugging Face'te: boyut ve evde çalışma iddiasını doğrula",
        "anahtar": r"K3",
        "tetik": r"K3\.?1",
        "her_degisiklik": True,
        "sayfalar": [
            "https://huggingface.co/api/models?author=moonshotai&search=K3",
            "https://huggingface.co/moonshotai",
        ],
    },
    {
        "ad": "eleven-v4-plan",
        "haber": "content/haberler/2026/09/eleven-v4.md",
        "baslik": "Eleven v4 planlarında değişiklik: ücretsiz planda var mı?",
        "anahtar": r"v4|free|ücretsiz",
        "tetik": r"v4",
        "sayfalar": ["https://elevenlabs.io/pricing", "https://elevenlabs.io/docs/overview/models"],
    },
    {
        "ad": "kling-4-fiyat",
        "haber": "content/haberler/2026/10/kling-4-0.md",
        "baslik": "Kling 4.0 fiyat/kredi değişti: haber ve model tablosunu güncelle",
        "anahtar": r"credit|kredi|\$|month|aylık|free|4\.0",
        "tetik": r"credit|kredi|\$|free|4\.0",
        "sayfalar": ["dom:https://klingai.com/global/membership/membership-plan"],
    },
    {
        "ad": "nano-banana-gemini",
        "haber": "content/haberler/2026/10/nano-banana-2-1.md",
        "baslik": "Nano Banana erişimi/sınırı değişti (Gemini)",
        "anahtar": r"nano banana",
        "tetik": r"nano banana",
        "sayfalar": ["https://gemini.google/overview/image-generation/", "https://gemini.google/subscriptions/"],
    },
    {
        "ad": "davinci-mcp-ucretsiz",
        "haber": "content/haberler/2026/09/davinci-resolve-21-1.md",
        "baslik": "DaVinci Resolve: yapay zekâ asistanı/MCP bağlantısı ücretsiz sürüme gelmiş olabilir",
        "anahtar": r"MCP|assistant|asistan|Claude|Studio",
        "tetik": r"MCP|assistant|Claude",
        "sayfalar": ["https://www.blackmagicdesign.com/products/davinciresolve/whatsnew", "https://www.blackmagicdesign.com/products/davinciresolve"],
    },
]


def cumleler(url: str, anahtar: str) -> list[str]:
    dom = url.startswith("dom:")
    url = url.removeprefix("dom:")
    if dom:
        from .kapak import _dom
        metin = _dom(url) or ""
        if not metin:
            print(f"  DOM alınamadı {url}", file=sys.stderr)
            return []
    else:
        try:
            r = httpx.get(url, headers={"User-Agent": UA, "Accept-Language": "tr,en;q=0.8"}, timeout=30, follow_redirects=True)
            r.raise_for_status()
            metin = r.text
        except Exception as e:  # noqa: BLE001
            print(f"  alınamadı {url}: {e}", file=sys.stderr)
            return []
    if metin.lstrip().startswith("["):
        # JSON liste (ör. Hugging Face API): her öğenin kimliği bir "cümle"
        try:
            return sorted({str(o.get("id") or o.get("modelId")) for o in json.loads(metin) if re.search(anahtar, str(o.get("id") or o.get("modelId")), re.I)})
        except Exception:  # noqa: BLE001
            pass
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", metin, flags=re.S | re.I)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = re.sub(r"\s+", " ", t)
    parca = re.split(r"(?<=[.!?])\s+", t)
    return sorted({p.strip()[:300] for p in parca if re.search(anahtar, p, re.I) and 20 < len(p) < 600})


def issue_ac(baslik: str, govde: str) -> None:
    if not os.environ.get("GH_TOKEN") and not os.environ.get("GITHUB_TOKEN"):
        print("GH_TOKEN yok; issue açılmadı.\n" + govde, file=sys.stderr)
        return
    subprocess.run(["gh", "issue", "create", "--title", baslik, "--body", govde, "--label", "takip"], check=False)


def main(argv: list[str]) -> int:
    kuru = "--kuru" in argv
    durum = json.loads(DURUM.read_text()) if DURUM.exists() else {}
    degisti = False
    for t in TAKIPLER:
        eski = durum.get(t["ad"], {})
        yeni: dict[str, list[str]] = {}
        rapor = []
        for url in t["sayfalar"]:
            c = cumleler(url, t["anahtar"])
            if not c and url in eski:
                yeni[url] = eski[url]  # geçici hata: eskisini koru
                continue
            yeni[url] = c
            if url not in eski:
                continue  # ilk görüş: yalnızca kaydet
            eklenen = [x for x in c if x not in eski[url]]
            cikan = [x for x in eski[url] if x not in c]
            if not (eklenen or cikan):
                continue
            if t.get("her_degisiklik") or any(re.search(t["tetik"], x, re.I) for x in eklenen) or any(re.search(t.get("kalkan", r"yalnızca google ai ultra|only .*ultra|coming soon|yakında"), x, re.I) for x in cikan):
                rapor.append(f"### {url}\n\n**Yeni:**\n" + "\n".join(f"- {x}" for x in eklenen) + "\n\n**Kalkan:**\n" + "\n".join(f"- {x}" for x in cikan))
        if rapor:
            govde = (f"`{t['haber']}` haberini güncelleyip ana sayfada öne çıkarma zamanı olabilir.\n\n" + "\n\n".join(rapor))
            print(govde)
            if not kuru:
                issue_ac(t["baslik"], govde)
        if yeni != eski:
            durum[t["ad"]] = yeni
            degisti = True
    if degisti and not kuru:
        DURUM.write_text(json.dumps(durum, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
