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
]


def cumleler(url: str, anahtar: str) -> list[str]:
    try:
        r = httpx.get(url, headers={"User-Agent": UA, "Accept-Language": "tr,en;q=0.8"}, timeout=30, follow_redirects=True)
        r.raise_for_status()
    except Exception as e:  # noqa: BLE001
        print(f"  alınamadı {url}: {e}", file=sys.stderr)
        return []
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", r.text, flags=re.S | re.I)
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
            if any(re.search(t["tetik"], x, re.I) for x in eklenen) or any(re.search(r"yalnızca google ai ultra|only .*ultra|coming soon|yakında", x, re.I) for x in cikan):
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
