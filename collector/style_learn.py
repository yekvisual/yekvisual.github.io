"""Üslup öğrenme: onay PR'ındaki ilk bot commit'i ile merge edilen son hal arasındaki
farktan kısa, somut yazım kuralları çıkarır ve style/uslup.md'ye ekler.

Ortam: BASE_SHA (PR'ın tabanı), HEAD_SHA (PR'ın son commit'i).
Botun ilk commit'i, BASE_SHA'dan sonra dalda yapılan ilk commit'tir.
"""

from __future__ import annotations

import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic
from pydantic import BaseModel, Field

KOK = Path(__file__).resolve().parent.parent
USLUP = KOK / "style" / "uslup.md"
MODEL = os.environ.get("YAZIM_MODEL", "claude-sonnet-5-5")


class Kurallar(BaseModel):
    kurallar: list[str] = Field(description="En fazla 5 kural. Her biri tek satır, somut, genellenebilir: 'X deme, Y de' ya da 'Başlıkta ... yapma'. Yazım hatası düzeltmesi gibi tekil şeyleri kural yapma. Düzeltme yoksa boş liste.")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=KOK, check=True, capture_output=True, text=True).stdout


def main() -> int:
    base, head = os.environ.get("BASE_SHA"), os.environ.get("HEAD_SHA")
    if not (base and head):
        print("BASE_SHA/HEAD_SHA yok.", file=sys.stderr)
        return 0
    commitler = git("rev-list", "--reverse", f"{base}..{head}").split()
    if len(commitler) < 2:
        print("Sadece bot commit'i var; düzeltme yok.", file=sys.stderr)
        return 0
    bot_commit = commitler[0]
    fark = git("diff", bot_commit, head, "--", "content/haberler/*.md", "content/haberler/**/*.md")
    if not fark.strip():
        print("Metin farkı yok.", file=sys.stderr)
        return 0
    if len(fark) > 60_000:
        fark = fark[:60_000]

    client = anthropic.Anthropic()
    r = client.messages.parse(
        model=MODEL,
        max_tokens=1500,
        system="Bir yazarın, yapay zekânın yazdığı Türkçe haber taslaklarına yaptığı düzeltmelerden genellenebilir üslup kuralları çıkarıyorsun. Mevcut rehberde zaten olan kuralları tekrar etme.",
        messages=[{"role": "user", "content": f"Mevcut rehber:\n{USLUP.read_text()}\n\nDüzeltme farkı (git diff, - bot, + yazar):\n{fark}"}],
        output_format=Kurallar,
    )
    kurallar = [k.strip() for k in r.parsed_output.kurallar if k.strip()]
    if not kurallar:
        print("Yeni kural çıkmadı.", file=sys.stderr)
        return 0
    tarih = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ek = "".join(f"- ({tarih}) {k}\n" for k in kurallar)
    USLUP.write_text(USLUP.read_text().rstrip() + "\n" + ek)
    print(f"{len(kurallar)} kural eklendi:\n{ek}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
