---
baslik: "Qwen-Image-2.1: üretim ve düzenleme tek modelde, doğrudan şeffaf PNG"
tarih: 2026-09-20
kategori: acik-kaynak
puan: 4
ozet: "Alibaba'nın Qwen ekibi, görsel üretimi ve düzenlemeyi tek modelde birleştiren 7 milyar parametreli Qwen-Image-2.1'i Hugging Face'te yayınladı. Doğrudan şeffaf arka planlı (RGBA) görsel üretebiliyor, 10 referans görsele kadar alıyor. Ağırlıklar açık ama lisans araştırma amaçlı; ticari kullanım için Alibaba ile ayrı anlaşma gerekiyor. 9 Ekim'de 8 adımda üreten Turbo sürümü eklendi."
neden_onemli: "Şeffaf arka planlı görseli doğrudan üretmek, arka plan silme adımını ortadan kaldırıyor; logo, çıkartma, kapak öğesi işlerinde bu başlı başına zaman. Üretim ve düzenlemenin aynı 7 milyarlık modelde olması, iki ayrı model indirip bellekte tutma yükünü kaldırıyor. Turbo sürümü 40 yerine 8 adımda çalıştığı için zayıf kartlarda bekleme süresini kısaltıyor."
yekvisual_notu: "2.1'i henüz kurmadım; Türkçe metin basma ve şeffaf çıkartma testini ComfyUI'de yapıp paylaşacağım. Model kartı VRAM rakamı vermiyor, CPU'ya aktarma seçeneği var; 16 GB kartta kaç saniye sürdüğünü ölçmeden yorum yapmıyorum. Lisansın araştırma amaçlı olduğunu müşteri işinde kullanmadan önce not edin."
ucretsiz: true
acik_kaynak: true
zorluk: teknik
sirket: Alibaba (Qwen)
model: Qwen-Image-2.1
etiketler: [qwen, alibaba, açık kaynak, görsel üretim, görsel düzenleme, şeffaf png, comfyui]
kart: acik-kaynak-modeller
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

Model kartı VRAM gereksinimi ve karşılaştırma tablosu yayımlamıyor. ComfyUI'de resmî düğüm olup olmadığını doğrulamadım; önceki Qwen-Image sürümleri destekleniyordu.
