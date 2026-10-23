---
baslik: Ücretsiz ve açık kaynak modeller
ozet: Görsel ve video üretmek için abonelik şart değil. FLUX, Wan, Stable Diffusion gibi modeller kendi bilgisayarında, sınırsız ve ücretsiz çalışıyor.
ikon: 🆓
sira: 8
zorluk: teknik
kategori: acik-kaynak
araclar: [comfyui, flux, wan]
etiketler: [açık kaynak, comfyui, flux, wan, stable diffusion, yerel, ücretsiz]
---

## Ne bu?

Büyük şirketlerin ücretli servislerinin yanında, ağırlıkları **herkese açık** modeller var: görsel için FLUX ve Stable Diffusion aileleri, video için Wan ve HunyuanVideo gibi modeller. Bunları [ComfyUI](https://www.comfy.org) gibi ücretsiz bir programla kendi bilgisayarında çalıştırıyorsun. Kredi yok, filigran yok, aylık ücret yok; görseller bilgisayarından dışarı çıkmıyor.

## Ne işe yarar?

- Yüzlerce varyasyon denemek, abonelik kredisi bitmeden.
- Kendi tarzını öğreten küçük eğitimler (LoRA) yapmak: aynı karakter, aynı ürün, aynı çizim dili.
- Ücretli servislerin izin vermediği ince kontroller: poz, kompozisyon, referans görsel, maske.

## Ne gerekiyor?

- **Ekran kartı:** En rahat deneyim 12 GB+ belleği olan NVIDIA kartlarla. Apple Silicon Mac'ler (16 GB+ RAM) görsel modellerde iyi, videoda yavaş.
- Ekran kartın zayıfsa: Hugging Face üzerindeki ücretsiz denemeler veya saatlik GPU kiralayan servisler.

## İlk adım

1. ComfyUI'nin masaüstü sürümünü kur.
2. Şablonlar menüsünden bir FLUX şablonu seç; model dosyasını kendisi indirir.
3. İlk prompt'unu yaz ve "Çalıştır". Yeni bir model çıktığında bu sitede nasıl kurulacağını da anlatacağız.
