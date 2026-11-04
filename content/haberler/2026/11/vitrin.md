---
baslik: "Sitenizi tek komutla Reels videosuna çevirin: /vitrin"
tarih: 2026-11-04
kategori: video
puan: 4
ozet: "YEK Lab'ın ilk açık kaynak becerisi /vitrin, bir projeyi ya da web sitesini Reels, TikTok ve Shorts için 15–25 saniyelik dikey bir tanıtım videosuna çeviriyor. 20 binin üzerinde yıldızlı brag projesinden uyarlandı; yayınlamadan önce iki sitede denedik ve takıldığı yerleri talimata işledik."
neden_onemli: "Bir projeyi bitirmek bir iş, onu anlatan kısa bir video yapmak ayrı bir iş. /vitrin siteyi geziyor, gerçek renkleri, fontları ve arayüzü topluyor, müziği yazıp dikey videoyu render ediyor. Kurgu programı açmadan, kendi sitenizin görünümünü koruyan bir taslak video elde ediyorsunuz."
yekvisual_notu: "Bu beceriyi ben yazdım; tarafsız bir değerlendirme değil, deneme notu olarak okuyun. Aşağıdaki video kendi sitem için tek komutla çıktı, sonradan yalnızca eksik kalan bir çekince eklenip yeniden render edildi. Müziği modelin kendisi üretiyor ve bazen iyi, bazen vasat; paylaşmadan önce mutlaka bir kez dinleyin."
ucretsiz: true
acik_kaynak: true
zorluk: orta
sirket: YEK Lab
model: /vitrin
etiketler: [claude code, beceri, reels, dikey video, remotion, açık kaynak, tanıtım videosu]
kart: kodla-video
kapak: ./vitrin/kapak.webp
kapak_kaynak: "Görsel: YEK Lab denemesi"
medya:
  - { tip: video, src: "./vitrin/vitrin-yeklab.mp4", alt: "/vitrin yeklab.com.tr komutunun ürettiği 20 saniyelik dikey video", kaynak: "YEK Lab denemesi" }
kaynaklar:
  - { ad: "GitHub: yekvisual/vitrin", url: "https://github.com/yekvisual/vitrin" }
  - { ad: "GitHub: latent-spaces/brag (uyarlanan proje)", url: "https://github.com/latent-spaces/brag" }
---

## Ne bu?

/vitrin, Claude Code gibi kodlama ajanları için yazılmış ücretsiz bir beceri. Bir proje klasöründe `/vitrin`, ya da bir site için `/vitrin siteniz.com` yazıyorsunuz. Ajan siteyi telefon görünümünde geziyor, renkleri ve fontları sayfanın kendisinden okuyor, arayüzden birkaç parçayı gerçek verisiyle yeniden kuruyor. Ardından bir plan yazıyor: bir kanca, iki üç öne çıkan nokta ve bir kapanış. Müziği kesmeler vuruşa denk gelecek şekilde üretiyor ve videoyu render ediyor. Sonuçta bir klasörde video, kapak görseli, plan ve paylaşım metni duruyor.

Temeli [latent-spaces/brag](https://github.com/latent-spaces/brag). GitHub'da 20 binin üzerinde yıldızı olan, projeyi okuyup tanıtım videosu çıkaran bir beceri; özünde iyi yazılmış, yüz satırlık bir talimat dosyası. /vitrin onu MIT lisansıyla dikey video için baştan uyarlıyor:

- **Varsayılan 1080×1920.** Yazılar, Reels arayüzünün alt, üst ve sağda kapattığı bölgelere konmuyor.
- **Kapak ilk kare.** Kanca videonun ilk karesinde okunur durumda; profil ızgarasının 3:4 kırpmasına göre yerleşiyor.
- **Sessiz izlenebilir.** Hikâye sesi kapalı izleyene de anlaşılıyor.
- **Yazım.** Büyük harfte i'yi İ'ye çeviriyor ama yabancı adları ("REMOTION") bozmuyor; sayıları 1.310 ve %40 biçiminde yazıyor.

## Nasıl denedik?

Talimatı yayınlamadan önce, sohbet geçmişini görmeyen ayrı bir ajana yalnızca talimat dosyasını verip iki video ürettirdik: biri bu site için, diğeri henüz açılmamış bir yapay zekâ reklam aracının tanıtım sitesi için. Her videoyu kare kare kontrol edip ajanın talimatı yanlış anladığı ya da talimatın hiç söylemediği yerleri not ettik. Yukarıdaki video, bu sitenin testi.

## Neler takıldı?

| Ne oldu | Talimata ne eklendi |
|---|---|
| Sayarak açılan puanlar, ara karelerde gerçek modellere uydurma değerler yazdı ("Kling 4.0: 696") | Gerçek sayılarda sayarak açılma yok |
| Sitedeki "ön değerlendirme" notu videoya taşınmadı; sıralama kesinmiş gibi okundu | Kaynaktaki çekinceler videoda da kalır |
| Bir sitede süreci anlatan örnek görselin etiketi, başlığa gerçek sonuç gibi yazıldı | Örnek, sonuç değildir; açılmamış ürünlerde erişim durumu ekranda kalır |
| Büyük harf dönüşümü "Remotion"ı "REMOTİON" yaptı | Yabancı adlar çevrilmez |
| Font hiç yüklenmemişti, satır yedek fonttan geldiği için her harf "doğru" göründü | Font yüklemesi tarayıcıda ayrıca doğrulanır |
| Video tam renk aralığında (yuvj420p) çıktı; Instagram ve TikTok'ta renk kayabilir | Render BT.709, sınırlı aralıkla yapılır ve kontrol edilir |
| 120 BPM'de sekizlik notalar 7,5 kareye düştü, kesmeler vuruşu kaçırdı | Tempo 90, 100, 120 ya da 150 seçilir |

İkinci test bir şeyi daha gösterdi: sitenin hareketli arka planı gibi yeniden kurulması zor parçalarda ajan yakın bir taklit yapıyor, sitede olmayan küçük bir ara adım ekleyebiliyor. Sonucu yayınlamadan önce siteyle yan yana izlemek gerekiyor.

## Dikkat edilecekler

- **Müzik.** Hazır müzik yok; model her seferinde yeniden yazıyor. Ses yüksekliği ölçülüyor ama kulakla dinlenmiyor; kötüyse videoyu sessiz paylaşıp platformun müziğini ekleyin.
- **Başkasının sitesi.** Beceri her siteyle çalışır, ama başka bir markanın sitesinden ürettiğiniz videoyu paylaşmadan önce sahibine haber verin.
- **Sonuç modele bağlı.** Becerinin kendisi bir talimat dosyası; videoyu kullandığınız model üretiyor, kalite modele göre değişiyor.
- **Yeni bir proje.** 2 Kasım'da yayınlandı; geri bildirimle talimat değişmeye devam edecek.

## Nasıl denenir?

Claude Code'da iki komutla kuruluyor:

```text
/plugin marketplace add yekvisual/vitrin
/plugin install vitrin@vitrin
```

Sonra bir proje klasöründe `/vitrin`, ya da bir site için `/vitrin siteniz.com` yazın. Bilgisayarda FFmpeg ve Node.js kurulu olmalı. Ton değiştirmek için `/vitrin --ton zarif` gibi seçenekler var. Cursor, Codex ya da Gemini CLI kullanıyorsanız kurulum `npx skills add` ile yapılıyor; ayrıntılar [repoda](https://github.com/yekvisual/vitrin).
