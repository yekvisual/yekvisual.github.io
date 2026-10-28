---
baslik: "Qwen-Image-2.1: üretim ve düzenleme tek modelde, doğrudan şeffaf PNG"
tarih: 2026-09-20
kategori: acik-kaynak
puan: 4
ozet: "Alibaba'nın Qwen ekibi, görsel üretimi ve düzenlemeyi tek modelde birleştiren 7 milyar parametreli Qwen-Image-2.1'i Hugging Face'te yayınladı. Doğrudan şeffaf arka planlı (RGBA) görsel üretebiliyor, 10 referans görsele kadar alıyor. Ağırlıklar açık ama lisans araştırma amaçlı; ticari kullanım için Alibaba ile ayrı anlaşma gerekiyor. 9 Ekim'de 8 adımda üreten Turbo sürümü eklendi."
neden_onemli: "Şeffaf arka planlı görseli doğrudan üretmek, arka plan silme adımını ortadan kaldırıyor; logo, çıkartma, kapak öğesi işlerinde bu başlı başına zaman. Üretim ve düzenlemenin aynı 7 milyarlık modelde olması, iki ayrı model indirip bellekte tutma yükünü kaldırıyor. Turbo sürümü 40 yerine 8 adımda çalıştığı için zayıf kartlarda bekleme süresini kısaltıyor."
yekvisual_notu: "Mac Studio'da Diffusers ile denedim: şeffaf logo gerçekten tek adımda, temiz kenarlarla çıkıyor; kısa Türkçe yazı da hatasız. Ama 1K görsel 2 dakika sürüyor ve kaplan gibi canlılarda anatomi bozulabiliyor. Logo ve çıkartma için işime yarar. 16 GB kartta deneyemedim. Lisansın araştırma amaçlı olduğunu müşteri işinde kullanmadan önce not edin."
ucretsiz: true
acik_kaynak: true
zorluk: teknik
sirket: Alibaba (Qwen)
model: Qwen-Image-2.1
etiketler: [qwen, alibaba, açık kaynak, görsel üretim, görsel düzenleme, şeffaf png, comfyui]
kart: acik-kaynak-modeller
kapak: ./qwen-image-2-1/kapak.webp
kapak_kaynak: "Görsel: Qwen (Alibaba)"
denemeler:
  - { tip: gorsel, src: ./qwen-image-2-1/deneme-1.webp, alt: "1024×1024, 40 adım: 2 dk 2 sn. İstem: “Küçük bir atölye kapısında ahşap tabela, üzerinde 'YEK Lab' yazıyor, altında küçük harflerle 'görsel · video · ses', sıcak akşam ışığı, fotoğraf”. Yazı doğru, akşam ışığı var; tabela kapıda değil, duvarın önünde.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./qwen-image-2-1/deneme-2.webp, alt: "Şeffaf arka planlı logo, 1024×1024: 2 dk 3 sn. Dosyanın arka planı gerçekten şeffaf (piksellerin %95'i), arka plan silme yapılmadı.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./qwen-image-2-1/deneme-3.webp, alt: "1024×1024: 2 dk 2 sn. Beyaz zeminde seramik kahve fincanı; istemde kahve vardı, fincan boş.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./qwen-image-2-1/deneme-4.webp, alt: "Düzenleme: önceki fincana “fincanı maviye çevir” dedim, 2 dk 21 sn. Fincanın biçimi ve çiçekleri korundu ama bütün görsel maviye boyandı, zemin pütürlü bir dokuya döndü.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./qwen-image-2-1/deneme-5.webp, alt: "1024×1024: 2 dk 1 sn. Karda kaplan: kırağı ve tüy dokusu iyi, gövde ve ön bacaklarda anatomi bozuk.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./qwen-image-2-1/deneme-6.webp, alt: "768×1024: 1 dk 28 sn. Başlık “Hafta Sonu Laboratuvarı” doğru, geri kalan yazıların hepsi anlamsız.", kaynak: "YEK Lab denemesi" }
kaynaklar:
  - { ad: "Hugging Face: Qwen/Qwen-Image-2.1", url: "https://huggingface.co/Qwen/Qwen-Image-2.1" }
  - { ad: "Hugging Face: Qwen/Qwen-Image-2.1-Turbo", url: "https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo" }
  - { ad: "DataNorth", url: "https://datanorth.ai/news/qwen-releases-qwen-image-2-1" }
---

## Neler yeni?

Qwen ekibi, 20 Eylül'de Qwen-Image-2.1'i yayınladı. Model kartındaki başlık "Yerel şeffaflık, birleşik üretim ve düzenleme". Ayrıntılar:

- **Tek model, iki iş.** Metinden görsel üretimi ve mevcut görseli düzenleme aynı modelde. Görsel üretim bileşeni 7 milyar parametre, 32 tek akışlı DiT katmanı.
- **Şeffaf çıktı.** Metinden doğrudan RGBA görsel üretiyor; arka plan silme adımı yok.
- **Referans görsel.** Düzenlemede 10'a kadar referans görsel; kişi ve ürün kimliğini koruma, tipografi, portre ışığı ve ince ayrıntıda iyileştirme iddiası var.
- **Oranlar.** 1:1, 4:3, 3:4, 3:2, 2:3, 16:9 ve 9:16. DataNorth'un aktardığına göre yerel 2K, 2752×2752'ye kadar.
- **Turbo.** 9 Ekim'de eklenen Qwen-Image-2.1-Turbo, aynı 7 milyarlık modelin 40 yerine 8 gürültü giderme adımında üreten hızlandırılmış sürümü.

Lisans "Qwen Research License": ağırlıklar indirilebiliyor ama model kartına göre ticari kullanım için ayrı bir anlaşma gerekiyor. Önceki Qwen-Image Apache 2.0'dı; bu bir değişiklik.

## Kimin işine yarar?

- **Tasarımcılar ve içerik üreticileri:** Çıkartma, logo taslağı, kapak öğesi gibi şeffaf arka plan gerektiren işler için tek adım.
- **Evde çalıştıranlar:** Diffusers ile `QwenImage21Pipeline` üzerinden kuruluyor; `enable_model_cpu_offload()` ile belleği düşürebiliyorsunuz. CUDA ve Apple Silicon (mps) destekleniyor.
- **Araştırma ve iç deneme yapan ekipler:** Lisans tam olarak bu kullanım için; müşteriye teslim edilen işte kullanacaksanız hukuk ekibinize sorun.

## Nasıl denenir?

Ağırlıklar [Hugging Face'te](https://huggingface.co/Qwen/Qwen-Image-2.1). Diffusers kurulumu için model kartındaki örnek kod yeterli; `torch>=2.4.0` ve `transformers>=5.17` istiyor. Hızlı denemek istiyorsanız [Turbo sürümüyle](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo) 8 adımda başlayın. İlk testte Türkçe bir slogan içeren şeffaf bir çıkartma isteyin; hem metin basma hem şeffaflık tek üretimde görünüyor.

## Sınırlar

Model kartı VRAM gereksinimi ve karşılaştırma tablosu yayımlamıyor. ComfyUI'nin 0.43.0 sürümünün kaynak kodunda Qwen-Image-2.1 desteği var; ben Diffusers ile denedim.

## Ben denedim

Mac Studio'da (M3 Ultra, 256 GB) Diffusers ile bf16 ve 40 adımda denedim. 1024×1024 görsel yaklaşık 2 dakika sürdü; aynı istemlerle denediğim [FLUX 3 Image Klein](/gundem/2026/10/flux-3-image-klein/) 16 adımda 34 saniyede bitiyor. Üretim sırasında model grafik belleğinde yaklaşık 49 GB yer kaplıyor.

Şeffaflık iddiası doğru: "YEK Lab" logosunu arka plan silmeden, temiz kenarlı bir PNG olarak verdi. Tabeladaki kısa Türkçe yazı da hatasız, ışık FLUX'tan daha doğal. Zayıf tarafları da var: afişte başlık dışındaki her yazı anlamsız, kaplanın anatomisi bozuk. "Fincanı maviye çevir" düzenlemesinde fincan korunsa da bütün görsel maviye boyandı. Turbo sürümünü ve 16 GB'lık kartı denemedim.
