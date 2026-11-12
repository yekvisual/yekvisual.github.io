---
baslik: "Kimi K3.1 Pro çıktı: Claude'a en yakın açık ağırlıklı model, ama evde çalışmıyor"
tarih: 2026-10-23
kategori: acik-kaynak
puan: 5
ozet: "Moonshot AI'ın 2,8 trilyon parametreli yeni modeli Terminal-Bench 4.0'da Claude Opus 5.5'in bir puan gerisinde. Ağırlıklar 4 Kasım'da Hugging Face'te açıldı (1,56 TB); API fiyatı milyon token başına 2 $ giriş, 10 $ çıkış."
neden_onemli: "Açık ağırlıklı bir modelin en iyi kapalı modellerle aynı masaya oturması, API fiyatını ve şirketlerin kendi sunucusunda çalıştırma seçeneğini doğrudan etkiliyor. Ekipler için bu, veriyi dışarı çıkarmadan güçlü bir model kullanma ihtimali demek; bireysel kullanıcı için de Kimi uygulamasında ücretsiz deneyebileceği bir Claude alternatifi."
yekvisual_notu: "Henüz denemedim; benchmark tablosu etkileyici ama kurgu ve metin işlerinde Claude'dan nerede ayrıldığını görmek için birkaç haftalık deneme lazım. Evde çalıştırma hayalini şimdilik unutun: tam model 1,56 TB. Topluluğun ağır budanmış sürümü bile 322 GB ve 512 GB'lık bir Mac Studio istiyor; üstelik kalitesi belirgin biçimde düşüyor."
ucretsiz: null
acik_kaynak: true
zorluk: teknik
sirket: Moonshot AI
model: Kimi K3.1 Pro
etiketler: [kimi, moonshot, açık kaynak, dil modeli, api]
kart: acik-kaynak-modeller
kapak: ./kimi-k3-1-pro/kapak.webp
kapak_kaynak: "Görsel: Moonshot AI"
kaynaklar:
  - ad: Kimi blogu, K3.1 Pro duyurusu
    url: https://www.kimi.com/en/blog/kimi-k3-1-pro
  - ad: Hugging Face, model kartı ve ağırlıklar
    url: https://huggingface.co/moonshotai/Kimi-K3.1-Pro
  - ad: Kimi K3.1 Pro lisansı
    url: https://huggingface.co/moonshotai/Kimi-K3.1-Pro/blob/main/LICENSE
---

## Neler yeni?

Moonshot AI, 23 Ekim'de Kimi K3.1 Pro'yu duyurdu. Model 2,8 trilyon parametreli bir "uzman karışımı" (MoE): toplam 896 uzmandan her istekte yalnızca 16'sı çalışıyor, bu yüzden boyutuna göre hızlı. Bağlam penceresi 1 milyon token; yani uzun senaryoları, tam bir kitap taslağını ya da saatlerce süren bir toplantı dökümünü tek seferde verebiliyorsunuz. Çok modlu: görsel ve video anlıyor, bir sahneyi izleyip ne olduğunu anlatabiliyor.

Ölçümlerde tablo şöyle: Terminal-Bench 4.0'da 65,7 puan; Claude Opus 5.5 66,4, GPT-6 Astra 58,2. BenchCAD'in üç alt testinde 92,7 / 96,2 / 95,9. Ağırlıklar 4 Kasım 2026'da Hugging Face'te açıldı: 96 parça, toplam 1,56 TB, MXFP4 hassasiyetle eğitilmiş.

**Lisans:** MIT tabanlı ama iki ek koşulu var. Modeli hizmet olarak sunup 12 ayda 20 milyon doları aşan şirketler Moonshot'la ayrı anlaşma yapmak zorunda. Aylık 100 milyon kullanıcıyı ya da aylık 20 milyon dolar geliri aşan ürünler arayüzde "Kimi K3.1-Pro" yazmak zorunda. Şirket içi kullanım bu koşullardan muaf.

## Kimin işine yarar?

- **Ekipler ve şirketler:** Verinin dışarı çıkmaması gereken işlerde, modeli kendi sunucunuzda çalıştırma yolu açılıyor. Ciddi donanım gerektiriyor: tam model 1,56 TB ve Moonshot'ın önerdiği yol vLLM ya da SGLang ile çok GPU'lu bir sunucu. NVIDIA'nın NVFP4 sürümü ve topluluğun GGUF dosyaları da var. Bu, bir sunucu kiralama ya da kurma kararı demek.
- **Geliştiriciler:** API fiyatı milyon token başına 2 $ giriş, 10 $ çıkış. Uzun belge işleyen uygulamalar için 1 milyon token bağlam asıl cazibe.
- **Bireysel kullanıcılar:** Kimi uygulamasında sınırlı ücretsiz kullanım var; Türkçe soru sorup cevap alabiliyorsunuz.

## Nasıl denenir?

En kolay yol [kimi.com](https://kimi.com) üzerinden uygulamaya girip ücretsiz hakkınızla birkaç gerçek işinizi vermek: bir metni Türkçe özetletin, bir video karesi yükleyip ne gördüğünü sorun. API'yi denemek isterseniz Moonshot'ın geliştirici panelinden anahtar alıyorsunuz. Ağırlıklar Hugging Face'te [moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) adresinde. Mac'te denemek isteyenler için topluluğun uzmanlarının %80'i budanmış MLX sürümü var: 322 GB, 512 GB'lık M3 Ultra'da saniyede yaklaşık 7 token; yazarı da kalitenin, özellikle kod dışında, belirgin düştüğünü söylüyor. Kendi bilgisayarınızda çalıştırmayı planlıyorsanız, önce daha küçük açık modellerle (bu sitedeki "Abonelik ödemeden" kartına bakın) elinizi alıştırmanızı öneririm.
