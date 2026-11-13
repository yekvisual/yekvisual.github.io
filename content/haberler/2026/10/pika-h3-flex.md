---
baslik: "Pika H3 Flex açık ağırlıklı oldu: sesli ve konuşmalı video, kendi bilgisayarınızda"
tarih: 2026-10-29
kategori: video
puan: 5
ozet: "Pika, MiniMax H3 üzerine eğittiği H3 Flex'in ağırlıklarını Hugging Face'te yayınladı. Model görüntüyü ve sesi (efekt, ortam sesi, diyalog) birlikte, 6 adımda üretiyor; yerelde 480p ve 768p, 5–15 saniye. Lisans Türkiye'de ücretsiz kullanıma izin veriyor; AB, İngiltere, Kore ve ABD kapsam dışında."
neden_onemli: "Mayıs 2025'te Google, Veo 3 ile konuşan ve sesli video üretimini gösterdiğinde bireysel kullanıcılar için bu yalnızca ABD'de, aylık 249,99 dolarlık Google AI Ultra aboneliğiyle mümkündü. Benzer bir yetenek artık indirip kendi bilgisayarınızda, kredi ve kullanım sınırı olmadan çalıştırabileceğiniz bir modelde. Bedeli donanım: dosyalar büyük ve üretim yavaş."
yekvisual_notu: "Mac'te ComfyUI ile denedim ve çalıştırmak için ComfyUI'de küçük bir düzeltme yapmam gerekti; aşağıda anlattım. 8 saniyelik dikey bir video 46 dakika sürdü. Sonuç bedava bir model için çok iyi: diyalog anlaşılır, sahne tutarlı. İstemdeki her hareketi yapmıyor; satıcı tepsiyi hiç indirmedi."
ucretsiz: true
acik_kaynak: true
zorluk: teknik
sirket: Pika
model: Pika H3 Flex
etiketler: [pika, minimax h3, video üretim, sesli video, açık ağırlık, comfyui]
kart: acik-kaynak-modeller
kapak: ./pika-h3-flex/kapak.webp
kapak_kaynak: "Görsel: YEK Lab denemesi (Pika H3 Flex ile üretildi)"
denemeler:
  - { tip: video, src: ./pika-h3-flex/simit.mp4, alt: "768×1344, 8 sn, sesli (sesi açın). Mac'te 46,5 dk. İskele, martılar, satıcının seslenmesi ve kameranın yaklaşması istendiği gibi; tepsiyi göğse indirme hareketini yapmadı, arkadaki gemi vapur değil yolcu gemisi.", kaynak: "YEK Lab denemesi" }
  - { tip: video, src: ./pika-h3-flex/bocek.mp4, alt: "768×1344, 10 sn, iki karakterli diyalog (sesi açın). Mac'te 73,2 dk. Replikler, sırayla konuşma ve son anda kırıntının karıncanın kafasına düşmesi istendiği gibi.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./pika-h3-flex/bozuk-ve-duzgun.webp, alt: "Aynı istem, 1344×768, 3 sn. Üstte ComfyUI'nin varsayılan ayarıyla Mac'te bozulan kareler; altta düzeltmeden sonra.", kaynak: "YEK Lab denemesi" }
kaynaklar:
  - { ad: "Hugging Face: Pika-Labs/Pika-H3-Flex", url: "https://huggingface.co/Pika-Labs/Pika-H3-Flex" }
  - { ad: "Pika teknik yazısı", url: "https://pika.art/blog/pika-h3-flex-research" }
  - { ad: "ComfyUI eğitimi: Pika H3 Flex", url: "https://docs.comfy.org/tutorials/video/pika/pika-h3-flex" }
  - { ad: "MiniMax H3 Community lisansı", url: "https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/42ed227ee7df40d41602854ae760620d6eb651fe/LICENSE" }
---

## Neler yeni?

Pika, 29 Ekim'de H3 Flex'in ağırlıklarını Hugging Face'te yayınladı. Model, MiniMax'ın açık video modeli MiniMax H3'ün üzerine eğitilmiş iki uyarlayıcıdan (LoRA) oluşuyor:

- **Görüntü ve ses birlikte.** Ses efekti, ortam sesi, müzik ve karakter diyaloğu videoyla aynı anda, senkron üretiliyor (32 kHz stereo).
- **6 adımda üretim.** Damıtılmamış H3 20–50 adım istiyor; H3 Flex 6 adımla bitiriyor.
- **Referansla yönlendirme.** İlk kare, son kare ya da ikisi birden verilebiliyor; Ref2VA uyarlayıcısı 9 görsel, 3 video ve 3 ses dosyasına kadar referans alıyor.
- **Çok sahneli istem.** Saniye saniye kamera hareketi ve kesme yazılabiliyor.

Yerelde çıktı 480p ya da 768p, 24 fps, 5–15 saniye. 1080p, 2K ve 4K yalnızca Pika'nın ücretli API'sinde, taslak videodan büyütme olarak var.

## Kimin işine yarar?

- **Güçlü bilgisayarı olan üreticiler:** Kredi yok, kullanım sınırı yok. Reels için kısa, sesli sahne denemeleri ve taslaklar.
- **Reklam ve hikâye taslağı hazırlayanlar:** Çok sahneli istem ve referans görselle ürün filmi ya da kısa skeç taslağı.
- **Geliştiriciler:** Pika'nın kendi komut satırı paketi var; Diffusers ve ComfyUI da destekliyor.

## Nasıl denenir?

En kolay yol ComfyUI: şablon kütüphanesinde **Pika H3 Flex: Text to Video** iş akışı hazır geliyor. Pika'nın resmi testleri 80 GB'lık H100 ekran kartında; varsayılan 480p/5 sn üretim yaklaşık 66–69 GB ekran belleği kullanmış. ComfyUI'nin önerdiği sıkıştırılmış NVIDIA dosyaları toplam yaklaşık 42 GB, Mac'te çalışan bf16 dosyaları yaklaşık 100 GB. Adım adım kurulum için [kılavuzumuza](/bilmeniz-gerekenler/pika-h3-flex-kurulum/) bakın.

## Sınırlar

- **Lisans bölgesi:** MiniMax H3 Community lisansı AB, İngiltere, Kore ve ABD'yi kapsam dışı bırakıyor; bu bölgelerde kullanım ve çıktıların kullanımı lisans dışı. Türkiye kapsamda.
- **Ticari kullanım:** Yıllık geliri 20 milyon doları aşan ürünler için MiniMax'tan yazılı izin gerekiyor; ticari ürünlerde arayüzde "MiniMax H3" ibaresi gösterilmeli.
- **Donanım:** Ev bilgisayarı için ağır bir model. Resmi olarak yalnızca NVIDIA H100'de test edilmiş; Mac için resmi destek yok.
- **Çözünürlük:** Yerelde en fazla 768p.

## Ben denedim

Mac Studio'da (M3 Ultra, 256 GB birleşik bellek) ComfyUI ile bf16 dosyalarını kullandım. İlk denemede 5 saniyelik video baştan sona gri gürültü çıktı; sesi de anlamsız bir uğultuydu. Kısa denemelerle sorunu daralttım: 1 saniye düzgün, 3 saniye bozuk. Sebep ComfyUI'nin Mac'teki dikkat (attention) hesabı: bellek bol olduğu için hesabı bölmüyor, ara tensör 2³¹ elemanı aşıyor ve Apple'ın ekran işlemcisi bu boyutta hata vermeden yanlış sonuç üretiyor. Parçaları bu sınırın altında tutan birkaç satırlık bir düzeltmeyle 3 saniye de 8 saniye de düzgün çıktı. Düzeltme kılavuzda.

Süreler (6 adım): 1344×768'de 1 sn 4,3 dk, 3 sn 10,5 dk; 768×1344'te 8 sn 46,5 dk, 10 sn 73,2 dk. Uzunluk arttıkça süre hızla artıyor. Simitçi videosunda satıcının seslenmesi net; konuşmayı Whisper ile yazıya döktüğümde kelimesi kelimesine çıktı. İstemdeki her hareketi yapmadı: satıcı tepsiyi göğsüne indirmedi, vapur yerine yolcu gemisi geldi. İki karakterli böcek sahnesinde ise replikler doğru sırayla geldi ve istemdeki son hareket (kırıntının karıncanın kafasına düşmesi) yerindeydi.
