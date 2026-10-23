# yekvisual.github.io

Yapay zekâ ile görsel, video ve içerik üretimi: sıfırdan başlayanlar için
"Bilmeniz Gerekenler" kartları ve otomatik toplanan, Türkçe yazılan gündem.
Site: <https://yekvisual.github.io>

## Nasıl çalışır

```
sources.yaml ──► collector/ (GitHub Actions, günde 3 kez)
                   topla → tekrarı ele → Claude: ele + puanla → Claude: Türkçe yaz + yekvisual notu
                   ├─ puan 4–5 → content/haberler → main'e commit → site yayınlanır
                   ├─ puan 2–3 → "Onay bekleyenler" PR'ı → merge = yayın
                   └─ puan 0–1 → atılır (data/seen.json)
content/ ──► site/ (Astro) ──► GitHub Pages
denemeler/gelen/<ad>/ ──► denemeler.yml ──► ilgili habere "Ben denedim"
onay PR merge ──► uslup.yml ──► style/uslup.md'ye kural ekler
Pazar ──► weekly.yml ──► content/ozetler + bülten
```

## Klasörler

| Yol | Ne |
|---|---|
| `content/kartlar/` | Bilmeniz Gerekenler kartları (elle yazılır) |
| `content/haberler/YYYY/MM/` | Haberler; `<slug>.md` + `<slug>/` medya klasörü |
| `content/araclar/` | Araç dizini (YAML) |
| `content/ozetler/` | Haftalık özetler |
| `style/uslup.md` | Yazım üslubu; her AI isteğine girer |
| `sources.yaml` | Taranan kaynaklar |
| `collector/` | Toplayıcı (Python) |
| `data/seen.json` | İşlenmiş öğeler (tekrarı önler) |
| `denemeler/gelen/` | Kendi denemelerini buraya at |
| `site/` | Astro sitesi |

## Kurulum (bir kez)

1. **Secrets** (Settings → Secrets and variables → Actions → Secrets):
   - `ANTHROPIC_API_KEY`: <https://console.anthropic.com> üzerinden
   - `NEWSLETTER_API_KEY`: Buttondown API anahtarı (isteğe bağlı, bülten için)
2. **Variables** (isteğe bağlı): `ELEME_MODEL` (varsayılan `claude-haiku-4-5`),
   `YAZIM_MODEL` (varsayılan `claude-sonnet-5-5`; daha iyi metin için `claude-opus-5-5`), `MAKS_OGE` (varsayılan 60).
3. **Pages**: Settings → Pages → Source: *GitHub Actions*.
4. Actions sekmesinden workflow'ları etkinleştir; **Haberleri topla → Run workflow → kontrol** ile kaynakları test et.

## Günlük kullanım

- **Onay PR'ları:** Bot kararsız kaldığı haberleri PR olarak açar. Metni düzenle, merge et.
  İstemediğin dosyayı sil ya da PR'ı kapat. Düzeltmelerin üslup rehberine işlenir.
- **Deneme eklemek:** `denemeler/gelen/<model-adi>/` klasörüne görsel/video ve isteğe bağlı
  `prompt.txt` koy (GitHub'da "Add file → Upload files" yeterli). Bot ilgili habere ekler.
- **Kart düzenlemek:** `content/kartlar/*.md` dosyalarını düzenle; push'ta site güncellenir.
- **Araç eklemek:** `content/araclar/<id>.yaml`.

## Yerel çalıştırma

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m collector --check              # kaynak sağlığı
.venv/bin/python -m collector --dry-run --no-ai    # ham liste
ANTHROPIC_API_KEY=... .venv/bin/python -m collector --dry-run   # AI dahil, dosya yazmaz
cd site && npm install && npm run dev              # site: http://localhost:4321
```

## Maliyet

Altyapı (GitHub Actions + Pages) ücretsiz. Tek ücretli kalem Claude API; her
çalıştırma sonunda token kullanımı ve tahmini tutar log'a yazılır. Varsayılan
modellerle günde ~60 öğe eleme + ~5–10 haber yazımı için tahmin: **ayda 3–6 $**.
`MAKS_OGE` ile tavan düşürülebilir.
