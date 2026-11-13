---
baslik: Abonelik ödemeden, kendi bilgisayarında üretmek
ozet: Görsel ve video üretmek için abonelik şart değil. FLUX 3 Klein, Pika H3 Flex, Wan gibi modeller kendi bilgisayarınızda, sınırsız ve ücretsiz çalışıyor.
ikon: 🆓
sira: 8
zorluk: teknik
kategori: acik-kaynak
araclar: [comfyui, flux, wan]
etiketler: [açık kaynak, comfyui, flux, wan, stable diffusion, yerel, ücretsiz]
gorsel: ./medya/acik-kaynak-modeller.webp
---

## Ne bu?

Büyük şirketlerin ücretli servislerinin yanında, ağırlıkları **herkese açık** modeller var: görsel için FLUX 3 Image Klein gibi FLUX modelleri ve Stable Diffusion ailesi, video için Pika H3 Flex, Wan ve HunyuanVideo gibi modeller. Bunları [ComfyUI](https://www.comfy.org) gibi ücretsiz bir programla kendi bilgisayarınızda çalıştırıyorsunuz. Kredi yok, filigran yok, aylık ücret yok; görseller bilgisayarınızdan dışarı çıkmıyor.

## Ne işe yarar?

- Yüzlerce varyasyon denemek, abonelik kredisi bitmeden.
- Kendi tarzınızı öğreten küçük eğitimler (LoRA) yapmak: aynı karakter, aynı ürün, aynı çizim dili.
- Ücretli servislerin izin vermediği ince kontroller: poz, kompozisyon, referans görsel, maske.

## Ne gerekiyor?

- **Ekran kartı:** Rakam modele göre değişiyor. FLUX 3 Klein, NVIDIA kartta 8 GB ekran belleğiyle çalışıyor; Apple Silicon Mac'te 32 GB ve üstü birleşik bellek istiyor. Video modelleri çok daha ağır: Pika H3 Flex Mac'te 128 GB'ın altında zorlanıyor.
- Ekran kartınız zayıfsa: Hugging Face üzerindeki ücretsiz denemeler veya saatlik GPU kiralayan servisler.

## İlk adım

1. ComfyUI'nin masaüstü sürümünü kurun.
2. Şablonlar menüsünden bir FLUX şablonu seçin; model dosyasını kendisi indirir.
3. İlk prompt'unuzu yazın ve "Çalıştır" deyin. Kurulumunu adım adım anlattığımız iki model: [FLUX 3 Klein](/bilmeniz-gerekenler/flux-3-klein-kurulum/) ve [Pika H3 Flex](/bilmeniz-gerekenler/pika-h3-flex-kurulum/).
