---
baslik: "Kendi bilgisayarınızda sesli video: Pika H3 Flex kurulumu"
ozet: Açık ağırlıklı Pika H3 Flex'i ComfyUI ile kurun; görüntüsü, sesi ve diyaloğu birlikte üretilen videoları kredi ödemeden yapın. Mac'te çalıştırmak için gereken düzeltme ve videodaki istemler de burada.
ikon: 🎬
sira: 10
zorluk: teknik
kategori: acik-kaynak
araclar: [comfyui, pika]
etiketler: [pika, pika h3 flex, minimax h3, comfyui, kurulum, sesli video, açık ağırlık, yerel, ücretsiz]
gorsel: ./medya/pika-h3-flex-kurulum.webp
---

## Ne bu?

[Pika H3 Flex](/gundem/2026/10/pika-h3-flex/), Pika'nın 29 Ekim 2026'da ağırlıklarını açtığı video modeli. Görüntüyü ve sesi birlikte üretiyor: ortam sesi, efekt, müzik ve karakterlerin konuşması videoyla senkron geliyor. Dosyaları bir kez indirdikten sonra her şey bilgisayarınızda çalışıyor: kredi yok, kullanım sınırı yok.

Lisans (MiniMax H3 Community) Türkiye'de ücretsiz kullanıma izin veriyor. AB, İngiltere, Kore ve ABD lisansın kapsamı dışında. Yıllık geliri 20 milyon doları aşan ticari ürünler için MiniMax'tan izin gerekiyor. İndirmeden önce lisans metnini okuyun.

Bu sayfadaki adımları Mac'te kendimiz uyguladık; NVIDIA tarafındaki dosya listesi ComfyUI'nin resmi eğitiminden.

## Ne gerekiyor?

Bu ağır bir model. Kısa bir video için bile bilgisayarınızın uzun süre tam güçte çalışmasını bekleyin.

| | NVIDIA ekran kartlı PC | Apple Silicon Mac |
|---|---|---|
| Dosya türü | INT8 / NVFP4 | bf16 / fp16 |
| İndirme | ~42 GB | ~100 GB |
| Bellek | Resmi testler 80 GB'lık H100'de. Ev kartları için resmi rakam yok | Biz 256 GB'lık Mac Studio'da denedik. 128 GB'ın altında zorlanır, denemedik |
| Ek iş | Yok | ComfyUI'de küçük bir düzeltme (5. adım) |

- Mac'te INT8 ve NVFP4 dosyaları çalışmıyor; bf16/fp16 dosyaları kullanın.
- Mac'te ComfyUI'yi GitHub'dan kurun (masaüstü uygulaması değil). 5. adımdaki düzeltme ComfyUI'nin kod dosyasına yapılıyor; masaüstü uygulamasında bu dosya uygulamanın içinde kalıyor ve her güncellemede siliniyor.

## Kurulum: 6 adım

### 1. ComfyUI'yi kurun ya da güncelleyin

Pika H3 Flex şablonu yeni sürümlerde var. NVIDIA'da [comfy.org/download](https://www.comfy.org/download) adresindeki masaüstü uygulaması yeterli. Mac'te [GitHub'daki kurulum talimatıyla](https://github.com/comfyanonymous/ComfyUI#installing) kurun; zaten kuruluysa `git pull` ile güncelleyin.

### 2. Model dosyalarını indirin

Dosyalar Hugging Face'te [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) deposunda; lisans formu istemiyor. Beş dosyayı ComfyUI'nin `models` klasöründe aşağıdaki yerlere koyun:

| Klasör | NVIDIA | Mac |
|---|---|---|
| `models/diffusion_models/` | `minimax_h3_fl2va_pruned_int8_convrot` (21,0 GB) | `minimax_h3_fl2va_pruned_bf16` (40,2 GB) |
| `models/text_encoders/` | `qwen3vl_32b_minimax_h3_nvfp4_awq` (15,7 GB) | `qwen3vl_32b_minimax_h3_bf16` (51,5 GB) |
| `models/vae/` | `minimax_h3_video_vae_int8_convrot` (2,8 GB) | `minimax_h3_video_vae_fp16` (5,2 GB) |
| `models/vae/` | `minimax_h3_audio_vae_fp32` (0,6 GB) | aynı |
| `models/loras/` | `pika_h3_flex_fl2va_v1_bf16` (2,0 GB) | aynı |

Hepsinin uzantısı `.safetensors`. Terminal kullanıyorsanız (Mac örneği):

```bash
hf download Comfy-Org/MiniMax-H3 \
  diffusion_models/minimax_h3_fl2va_pruned_bf16.safetensors \
  text_encoders/qwen3vl_32b_minimax_h3_bf16.safetensors \
  vae/minimax_h3_video_vae_fp16.safetensors \
  vae/minimax_h3_audio_vae_fp32.safetensors \
  loras/pika_h3_flex_fl2va_v1_bf16.safetensors \
  --local-dir ~/ComfyUI/models
```

İndirme yarıda kesilirse aynı komutu tekrar çalıştırın; kaldığı yerden devam ediyor.

### 3. Şablonu açın

ComfyUI'de **Template Library → Video → Pika H3 Flex: Text to Video** şablonunu açın. Eksik dosya uyarısı çıkarsa yukarıdaki listeyle karşılaştırın.

**Mac'te:** Şablon NVIDIA dosyalarıyla geliyor. Ana kutuyu çift tıklayıp açın ve üç yükleyicide dosya adını değiştirin: **Load Diffusion Model** → `..._pruned_bf16`, **Load CLIP** → `..._bf16`, video için **Load VAE** → `..._fp16`.

### 4. İstemi yazın

Şablondaki istem üç bölümden oluşuyor; aynı düzeni koruyun:

- `integrated_multimodal_description:` Sahne, kamera hareketi ve olaylar, sırasıyla. Konuşan karakterleri `(S1)`, `(S2)` diye etiketleyin, repliği `<d>[Turkish] Taze simit!</d>` biçiminde yazın; köşeli parantez içinde dil adı İngilizce.
- `overall_soundscape:` Ortam sesleri ve efektler.
- `non_diegetic_music:` Arka plan müziği; istemiyorsanız `N/A`.

İstem İngilizce yazılıyor; yalnızca replikler istediğiniz dilde. Hareketleri sırayla ve tek tek yazın, "normal hızda, ağır çekim yok" ekleyin.

### 5. Mac düzeltmesi (yalnızca Mac)

Bu adımı atlarsanız 3 saniyeden uzun videolar baştan sona gri gürültü olarak çıkıyor, ses de anlamsız bir uğultu. ComfyUI hata vermiyor. Sebep: ComfyUI Mac'te dikkat (attention) hesabını bölüp bölmeyeceğine boş belleğe bakarak karar veriyor; bellek bolsa bölmüyor. Ara tensör 2³¹ elemanı aşınca Apple'ın ekran işlemcisi hata vermeden yanlış sonuç üretiyor. `--use-split-cross-attention` seçeneği de aynı nedenle işe yaramıyor.

`ComfyUI/comfy/ldm/modules/attention.py` dosyasında `def attention_sub_quad` bölümünü bulun. İçinde şu iki satır var:

```python
    if query_chunk_size is None:
        query_chunk_size = 512
```

Hemen altına şunu ekleyin (girinti dört boşluk):

```python
    if query.device.type == "mps":
        sinir = 2 ** 30
        kv = kv_chunk_size or k_tokens
        while query_chunk_size > 128 and batch_x_heads * query_chunk_size * kv > sinir:
            query_chunk_size //= 2
        if batch_x_heads * query_chunk_size * kv > sinir:
            kv_chunk_size = max(256, sinir // (batch_x_heads * query_chunk_size))
```

ComfyUI'yi kapatıp yeniden açın. ComfyUI'yi her güncellediğinizde bu satırların yerinde olup olmadığına bakın.

### 6. Ayarlayın ve çalıştırın

- **Süre:** Saniye kutusu. Model 5–15 saniye için eğitilmiş; ilk denemeyi kısa tutup süreyi görün.
- **Oran:** Reels için *9:16 (Portrait Widescreen)*. Varsayılan çözünürlükle dikeyde 768×1344 çıkıyor.
- **Adım ve sampler:** Şablondaki gibi kalsın (6 adım, lcm). ComfyUI'nin eğitimine göre adım sayısını artırmak ayrıntı eklemiyor; turbo ya da Lightning LoRA eklemek görüntüyü bozuyor.

Çıktı `ComfyUI/output/video/` klasörüne sesli MP4 olarak kaydediliyor.

## Ne kadar sürer?

| Video | Apple M3 Ultra, bf16 (bizim ölçüm) |
|---|---|
| 1344×768, 1 sn | 4,3 dk |
| 1344×768, 3 sn | 10,5 dk |
| 768×1344, 8 sn | 46,5 dk |
| 768×1344, 10 sn | 73,2 dk |

Süre, videonun uzunluğuyla orantılı değil, daha hızlı artıyor. ComfyUI, 5 saniyelik 1344×768 bir videonun "tek kartta yaklaşık bir dakikada" bittiğini söylüyor; hangi kart olduğunu belirtmiyor. NVIDIA'da kendimiz denemedik.

## Videodaki istemler

Videodaki iki sahne bu istemlerle üretildi. Seed değerini şablondaki **RandomNoise** düğümüne yazın. Aynı ayarlarla benzer sonuç alırsınız; farklı donanım birebir aynı videoyu vermeyebilir.

**Simitçi** (9:16, 8 sn, seed 7):

```text
integrated_multimodal_description: [Shot 1] A live-action vertical shot on a weathered wooden ferry pier by the sea in soft early-morning light. A middle-aged street vendor with a grey flat cap and a rolled-up white shirt walks slowly toward the camera, balancing a large round wooden tray stacked with fresh, glossy, sesame-crusted simit bread rings on his head. Behind him, gulls glide over calm blue water and a white passenger ferry slides slowly past in the distance. He stops in the center of the frame, lowers the tray to chest height with both hands, looks into the camera with a warm grin and calls out in a loud, cheerful, slightly raspy voice (S1), <d>[Turkish] Taze simit! Sıcak sıcak simit!</d> A gull lands on the pier railing beside him and cries once. The camera slowly pushes in from a medium shot to a close-up of his smiling face and the steaming simit on the tray. One continuous shot, no cuts. Photoreal 35mm film look, natural colours, light grain. Normal real-time speed, no slow motion. No text, no logos, no real landmarks.

overall_soundscape: Morning harbour ambience: gentle waves lapping against the wooden pier, footsteps on old boards, several gull cries, distant city hum and one deep, long ferry horn in the background.

non_diegetic_music: N/A
```

**Böcekler** (9:16, 10 sn, seed 11):

```text
integrated_multimodal_description: [Shot 1] Stylized 3D animation, Pixar-inspired cartoon rendering with soft subsurface scattering, macro photography look with shallow depth of field and creamy green bokeh. Early morning in a garden: a big glossy green leaf covered with tiny dew drops fills the lower half of the vertical frame. On the leaf stand two small insect characters facing each other, both with big expressive eyes and clearly animated mouths. On the left, a small energetic red-brown ant (S1) holding a bread crumb above its head. On the right, a round, relaxed ladybug (S2) with a shiny red shell and black dots, leaning back on a dew drop. The ant lowers the crumb, leans toward the ladybug with wide excited eyes and says in a fast, high-pitched, excited voice (S1), <d>[Turkish] Duydun mu? Bu videoyu bir bilgisayar kendi kendine yapmış!</d> The ladybug slowly raises one eyebrow, glances at the camera and answers in a calm, deep, slightly smug voice (S2), <d>[Turkish] Bedava mı? O zaman beni bir dahakine daha yakışıklı çizsin.</d> The ant laughs and drops the crumb on its own head. The camera holds a gentle static macro shot with a very slow push-in. One continuous shot, no cuts. Normal real-time speed. No text, no logos.

overall_soundscape: Quiet morning garden ambience: soft birdsong in the distance, a faint breeze through leaves, a tiny drip of a dew drop, and a small soft thud when the crumb lands.

non_diegetic_music: N/A
```

## Takılırsanız

- **Video gri gürültü, ses uğultu:** Mac'teyseniz 5. adımdaki düzeltme eksik. NVIDIA'da dosyaların eksiksiz indiğini kontrol edin.
- **İstediğiniz hareketi yapmıyor:** Simitçi tepsiyi göğsüne indirmedi; gemi istediğimiz vapur değil yolcu gemisi çıktı. Önemli hareketi istemin başına yakın ve tek başına yazın, seed'i değiştirip tekrar deneyin.
- **Bellek yetmiyor:** Süreyi kısaltın ya da çözünürlüğü düşürün. Mac'te başka ağır uygulamaları kapatın.
- **Daha yüksek çözünürlük:** Yerelde en fazla 768p. 1080p ve üstü yalnızca Pika'nın ücretli API'sinde.
