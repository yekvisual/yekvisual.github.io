---
baslik: "Claude Code ile konuşan kafa videosuna 45 efekt: denedik, çoğu tutuyor"
tarih: 2026-10-28
kategori: video
puan: 4
ozet: "Ücretsiz claude-video-effects becerisi, kameraya konuşan bir videoya yörüngede dönen kartlar, kişinin arkasına yazı, sözle tetiklenen spot ışığı gibi 45 efekt ekliyor. Bu bilgisayarda kurup 14 saniyelik bir klipte altı efekti denedik: kurulum 6 dakika, her efekt 8 ile 22 saniye arasında hazır."
neden_onemli: "Reels ve kısa videolarda bu tür efektler After Effects'te dakikalar, bazen saatler alıyor. Burada efekt bir komutla uygulanıyor, kişi takibi ve arka plan ayırma otomatik. Kendi Instagram görsellerinizi kartlara koyabildiğiniz için tanıtım videoları hızla kişiselleşiyor."
yekvisual_notu: "Altı efekti kendi bilgisayarımda denedim; sonuçlar aşağıda. En temiz çalışan, kişinin arkasına yazı yerleştirmek. Yörünge ve profil ızgarası efektlerine kendi Instagram görsellerimi verdim, gayet iyi oturdu. Widget efekti hazır sahte verilerle geliyor ve bir kenar hatası yaptı; kullanmadan önce kendi verinizi girmeniz gerekiyor."
ucretsiz: true
acik_kaynak: true
zorluk: orta
sirket: Vibha Ramprakash (bağımsız geliştirici)
model: claude-video-effects
etiketler: [claude code, video efekti, reels, beceri, açık kaynak, ffmpeg, mediapipe]
kart: kodla-video
kapak: ./claude-video-effects/kapak.webp
kapak_kaynak: "Görsel: YEK Lab denemesi (kaynak klip: MART PRODUCTION, Pexels)"
medya:
  - { tip: video, src: "./claude-video-effects/05_stack_spotlight-orbit-backdrop.mp4", alt: "Üç efekt üst üste: spot ışığı, yörüngede kendi Instagram görsellerimiz, arkada yazı", kaynak: "YEK Lab denemesi" }
denemeler:
  - { tip: video, src: "./claude-video-effects/02_backdrop-word.mp4", alt: "Kişinin arkasına yazı (backdrop-word): en temiz sonuç", kaynak: "YEK Lab" }
  - { tip: video, src: "./claude-video-effects/01_orbit.mp4", alt: "Yörünge (orbit): kartlar kendi Instagram görsellerimiz", kaynak: "YEK Lab" }
  - { tip: video, src: "./claude-video-effects/03_spotlight.mp4", alt: "Sözle tetiklenen spot ışığı: omuz kenarında maske bandı belli oluyor", kaynak: "YEK Lab" }
  - { tip: video, src: "./claude-video-effects/06_place-in-grid.mp4", alt: "Profil ızgarası (place-in-grid): kendi Instagram görsellerimizle, sahte izlenme sayıları kapatıldı", kaynak: "YEK Lab" }
  - { tip: video, src: "./claude-video-effects/04_glass-widgets.mp4", alt: "Cam widgetlar: hazır sahte veriler ve şapkayı kişi sanan kenar hatası (3,5. saniye)", kaynak: "YEK Lab" }
kaynaklar:
  - { ad: "GitHub: claude-video-effects", url: "https://github.com/Vibha-Ramprakash/claude-video-effects" }
  - { ad: "Test klibi: A Man Talking (MART PRODUCTION, Pexels)", url: "https://www.pexels.com/video/a-man-talking-7261920/" }
---

## Ne bu?

claude-video-effects, Claude Code için yazılmış ücretsiz bir beceri. Kameraya konuşan bir videoyu verip `/effects orbit` gibi bir komut yazıyorsunuz; beceri yüzü takip ediyor, kişiyi arka plandan ayırıyor ve efekti uyguluyor. Efektler üst üste kullanılabiliyor, orijinal ses korunuyor. Repo 22 Ekim'de açıldı ve MIT lisanslı.

Efekt sayısı konusunda kafa karışıklığı var: repo açıklaması 36 diyor, README 45. Kodu saydık: 45 efekt kayıtlı, açıklama eski kalmış.

## Nasıl denedik?

- **Makine:** Mac Studio (M3 Ultra), Python 3.11, ffmpeg.
- **Kurulum:** Repoyu indirip gereken paketleri (OpenCV, MediaPipe) kurmak 52 saniye sürdü; yüz takibi ve arka plan ayırma modelleri repoyla hazır geliyor. Kelime zamanlaması için gereken konuşma tanıma ilk çalıştırmada kendiliğinden kuruluyor. Klonlamadan ilk çıktıya toplam 6 dakika.
- **Klip:** Pexels'ten serbest lisanslı, 14 saniyelik, dikey bir "kameraya konuşan adam" klibi. Pexels kliplerinin neredeyse hiçbirinde ses yok; spot ışığını bir söze bağlayabilmek için klibe bilgisayara okuttuğumuz İngilizce bir ses ekledik. Dudak senkronu yok, yalnız test için.
- **Görseller:** Yörünge ve profil ızgarası efektlerinin kartlarına kendi Instagram gönderilerimizin görsellerini verdik.

## Sonuçlar

| Efekt | Süre | Sonuç |
|---|---|---|
| Arkaya yazı (backdrop-word) | 7,6 sn | En temizi; saç kenarında hafif hale |
| Spot ışığı (spotlight) | 10,9 sn | Sözle tetikleniyor; omuz kenarında açık renkli maske bandı |
| Yörünge (orbit) | 14,3 sn | Kartlar başın önünden ve arkasından dönüyor; öndekiler ellerin üstüne biniyor |
| Cam widgetlar (glass-widgets) | 22,2 sn | Duvardaki şapkayı kişinin parçası sanıp kartta delik açtı |
| Üçü üst üste | 20,7 sn | Katmanlar düzgün birleşti |

Süreler, 14 saniyelik 1080×1920 klip için. Yüz takibi altı çıktının hepsinde tuttu, ses seviyesi korundu.

## Dikkat edilecekler

- **Sahte veriler.** Widget efekti "Edited by Claude", "197K" gibi hazır içerikle geliyor; profil ızgarası da her karenin üstüne uydurma izlenme sayıları basıyor. Bunları kendi verinizle değiştirmeden ya da kapatmadan yayınlamayın; biz ızgaradaki sayıları kapattık.
- **Kenarlar.** Arka plan ayırma kusursuz değil; düz bir duvar önünde çekim daha temiz sonuç verir.
- **Küçük bir proje.** Tek bir geliştiricinin birkaç günlük işi; güncellemeler sık, bir sonraki sürümde komutlar değişebilir.

## Nasıl denenir?

Claude Code kurulu bir bilgisayarda repoyu Claude'un beceri klasörüne indirin, kurulum betiğini çalıştırın, sonra Claude Code'a videonuzu verip `/effects` yazın. Kod yazmanıza gerek yok; ne istediğinizi anlatmanız yetiyor.
