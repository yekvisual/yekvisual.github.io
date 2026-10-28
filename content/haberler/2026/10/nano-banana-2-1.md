---
baslik: "Nano Banana 2.1 Gemini'de: 14 referansla tutarlı karakter, 4K yarı fiyata"
tarih: 2026-10-06
kategori: gorsel
puan: 4
ozet: "Google'ın yeni görsel üretim ve düzenleme modeli Nano Banana 2.1, Gemini uygulaması, AI Studio ve API'de yayında. 1K, 2K ve 4K üretiyor, 1:8 ve 8:1 gibi uç en-boy oranlarını destekliyor; API'de 4K görsel fiyatı önceki modele göre yarıya indi."
neden_onemli: "Aynı karakteri ve ürünü seri görsellerde sabit tutmak sosyal medya ve reklam işlerinin en çok zaman yiyen kısmı. Konuşa konuşa düzenleme, maske ve karalama ile düzeltme, 14 referans görsel desteği bu işi telefondan yapılabilir hale getiriyor. Fiyat düşüşü de API ile toplu üretim yapan ekipler için doğrudan maliyet demek."
yekvisual_notu: "2.1'i henüz kendi istemlerimle denemedim; Instagram kapağı için aynı karakteri üç gönderide sabit tutma testini yapıp paylaşacağım. Model kartı küçük puntolu metinde ve uzun paragraflarda hâlâ sorun olduğunu açıkça yazıyor, yani Türkçe afiş metni için beklentiyi düşük tutun. Gemini'nin ücretsiz katmanında kaç üretim hakkı verdiğini doğrulamadım."
ucretsiz: null
acik_kaynak: false
zorluk: yeni
sirket: Google
model: Nano Banana 2.1
etiketler: [nano banana, google, gemini, görsel düzenleme, karakter tutarlılığı, 4k]
kapak: ./nano-banana-2-1/kapak.webp
kapak_kaynak: "Görsel: Google"
kaynaklar:
  - { ad: "Google DeepMind model kartı", url: "https://deepmind.google/models/model-cards/nano-banana-2-1/" }
  - { ad: "Gemini API değişiklik günlüğü", url: "https://ai.google.dev/gemini-api/docs/changelog" }
  - { ad: "The Decoder", url: "https://the-decoder.com/googles-new-image-model-nano-banana-2-1-generates-better-images-for-less-money/" }
---

## Neler yeni?

Google, 6 Ekim'de Nano Banana 2.1'i yayına aldı. Şubatta çıkan Nano Banana 2'nin yerini alıyor ve Google'a göre görsel kalite, istemi anlama, konuşma boyunca karakter tutarlılığı ve metin basma konularında ilerleme var. Model kartında öne çıkanlar:

- **Düzenleme türleri:** Genel düzenleme, stil değiştirme, karakter ve nesne düzenleme, maskeyle ve karalamayla (doodle) düzenleme, birden çok referans görselle düzenleme.
- **Tutarlılık:** Çok karakterli sahnelerde ve ürün görsellerinde aynı kişi ve aynı ürünü korumaya yönelik özel başlıklar var. The Decoder'ın aktardığına göre tek seferde 14 referans görsel alıyor, 4 karakteri ve 10 nesneyi sabit tutuyor.
- **Çözünürlük ve oran:** 1K, 2K ve 4K; 1:4, 4:1, 1:8, 8:1 gibi uç en-boy oranları da destekleniyor.
- **Dil:** Model kartı "birkaç dilde yerelleştirilmiş metin basma" diyor; dilleri saymıyor.

Fiyat tarafında The Decoder'ın hesabı: API'de 1K görsel 3,36 sent (önceki 6,70), 2K 5,04 sent, 4K 7,56 sent (önceki 15,10). Eski model `gemini-3.1-flash-image` 29 Ekim'de kapanıyor.

## Kimin işine yarar?

- **İçerik üreticileri:** Aynı karakterle seri gönderi, panoramik kapak ya da dikey hikâye görseli üretirken telefondan Gemini uygulaması yetiyor.
- **Reklam ve e-ticaret ekipleri:** Ürünü sabit tutup arka planı, ışığı ve sahneyi değiştirme işi için 14 referans sınırı geniş.
- **Geliştiriciler:** Gemini API ve AI Studio'da; toplu üretimde yarıya inen 4K fiyatı önemli.

## Nasıl denenir?

Gemini uygulamasında görsel üretimini seçip bir referans fotoğraf yükleyin, sonra "aynı kişiyi kafede otururken göster" gibi ardışık isteklerle tutarlılığı sınayın. API için [AI Studio](https://aistudio.google.com) üzerinden `gemini-nano-banana-2.1` modelini seçiyorsunuz.

## Sınırlar

Model kartı, küçük metinlerde ve uzun paragraflarda zayıf kaldığını, girdi ile çıktı arasında karakter tutarlılığının her zaman kusursuz olmadığını belirtiyor. Nano Banana Pro ayrı bir model olarak duruyor; en yüksek kaliteyi isteyenler için hâlâ o öneriliyor.
