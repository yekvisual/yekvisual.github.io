---
baslik: "Tek cümleyle GIF yapmak: ChatGPT Images 2.6 ve yeni Mac uygulamasını denedik"
tarih: 2026-11-09
kategori: gorsel
puan: 4
ozet: "ChatGPT'nin görsel modeli Images 2.6 artık yazdığınız bir cümleden döngü GIF üretiyor. Plus hesapla, yeni Mac uygulamasında dört GIF denedik: tebeşirle yazılan \"Öğretmenler Günü Kutlu Olsun\" harfi harfine doğru çıktı, ama GIF'ler küçük. Aynı uygulamada Çalışma modunda sunum, sohbet içinde oyun ve SVG ikon da denedik."
neden_onemli: "Kısa bir hareketli görsel için şimdiye kadar ya bir animasyon programı ya da ayrı bir video modeli gerekiyordu. Images 2.6 GIF'i doğrudan sohbette üretiyor ve üretilen GIF'i yeni bir cümleyle düzeltmenize izin veriyor. Ders materyali, kutlama paylaşımı ya da sunum için hızlı bir hareketli görsel isteyenlere kestirme bir yol."
yekvisual_notu: "Tebeşir GIF'i beni şaşırttı: harfler tek tek beliriyor, sonunda kalp de var. 24 Kasım için hazır bir paylaşım. Ama kare başına 360–510 piksel düşüyor; Reels'te tam ekran değil, bir kartın içinde göstermek gerek. Sohbet içinde hazırlanan oyunu da öğrenciye vermeden önce mutlaka kendiniz oynayın."
ucretsiz: null
acik_kaynak: false
zorluk: yeni
sirket: OpenAI
model: ChatGPT Images 2.6
etiketler: [chatgpt, openai, images 2.6, gif, görsel üretim, mac]
kapak: ./chatgpt-images-2-6-gif/kapak.webp
kapak_kaynak: "Görsel: YEK Lab denemesi (ChatGPT Images 2.6 ile üretildi)"
medya:
  - { tip: video, src: ./chatgpt-images-2-6-gif/tebesir-gif.mp4, alt: "Images 2.6'nın ürettiği GIF, videoya çevrilip üç kez döngüye alındı. İstem: “Kara tahtada tebeşirle yazılan \"Öğretmenler Günü Kutlu Olsun\" yazısı, harfler tek tek belirsin, sonunda küçük bir kalp çizilsin. Döngü GIF.” Özgün GIF 358×355 piksel, 12 kare, 4,2 saniye.", kaynak: "YEK Lab denemesi" }
denemeler:
  - { tip: video, src: ./chatgpt-images-2-6-gif/gif-uretimi-ekran.mp4, alt: "Tebeşir GIF'inin üretimi, Mac uygulamasının ekran kaydı (yaklaşık 2,5 dakika, 7,5 kat hızlandırıldı). Sonda sheet görünümü ve kare şeridiyle GIF görüntüleyici.", kaynak: "YEK Lab denemesi" }
  - { tip: video, src: ./chatgpt-images-2-6-gif/vapur-duzenleme.mp4, alt: "Çay, buhar ve Boğaz'dan geçen vapur istediğimiz ilk GIF'in düzenlenmiş hali. Düzenleme isteği: “Vapurun bacasından duman çıksın, vapur yavaşça geçsin.” 380×337 piksel, 12 kare; duman da vapurun ilerlemesi de geldi.", kaynak: "YEK Lab denemesi" }
  - { tip: video, src: ./chatgpt-images-2-6-gif/logo-gif.mp4, alt: "YEK Lab logosunu yükleyip sıçrayarak gelmesini ve parlamasını istedik. 362×362 piksel, şeffaf arka plan (burada açık zemine yerleştirildi). Logo bozulmadı; hareket sade: büyüyerek giriş ve bir parlama.", kaynak: "YEK Lab denemesi" }
  - { tip: video, src: ./chatgpt-images-2-6-gif/calisma-modu-sunum.mp4, alt: "Çalışma modunda “Öğretmenler Günü için 5 slaytlık bir sunum hazırla.” isteği. 2 dk 51 sn süren iş 12 kat hızlandırıldı; sonunda uygulama içi slayt görüntüleyici.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./chatgpt-images-2-6-gif/kesir-oyunu-hata.webp, alt: "Sohbet içinde açılan “Kesir Macerası” oyunu, 2. soru. Dört parçadan ikisi boyalı ve oyun da “Boyalı: 2, Toplam: 4” yazıyor; ama 1/4 cevabını doğru sayıyor.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./chatgpt-images-2-6-gif/svg-ikon.webp, alt: "“Açık kitap” ikonunu SVG olarak istedik; 52 saniyede indirilebilir bir SVG dosyası geldi. Dosyayı Images 2.6'nın dışa aktarması değil, ChatGPT'nin yazdığı kod üretiyor.", kaynak: "YEK Lab denemesi" }
kaynaklar:
  - { ad: "OpenAI, X duyurusu (4 Kasım 2026)", url: "https://x.com/OpenAI/status/2118124944928432327" }
  - { ad: "The Next Web: ChatGPT Images 2.6 ile GIF", url: "https://thenextweb.com/news/chatgpt-animated-gifs-images-2-6-openai" }
  - { ad: "ChatGPT: Yenilikler", url: "https://learn.chatgpt.com/docs/whats-new" }
  - { ad: "TechBriefly: ChatGPT Classic'in kapanması", url: "https://techbriefly.com/2026/11/05/openai-to-end-chatgpt-classic-for-mac-on-january-30-2027/" }
---

## Neler yeni?

OpenAI, 4 Kasım'da ChatGPT'nin görsel modelini Images 2.6'ya güncelledi. Öne çıkan yenilik GIF: "döngü GIF yap" diye biten bir istek yazdığınızda ChatGPT hareketli bir görsel üretiyor ve bunu ayrı bir görüntüleyicide açıyor. Biz denemeleri Plus hesapla, yeni ChatGPT Mac uygulamasında (sürüm 26.1103) yaptık. Ücretsiz planda GIF'in açık olup olmadığını doğrulamadık.

## GIF'i nasıl yapıyor?

GIF aslında tek bir görsel olarak üretiliyor: 3×3 ya da 4×3 karelik bir sayfa (ChatGPT buna "sheet" diyor), 1536×1024 ya da 1448×1086 piksel. Kareler sırayla oynatılınca GIF oluyor. Bu yüzden kare başına yaklaşık 360–510 piksel düşüyor; GIF küçük.

Görüntüleyicide şunlar var:

- Hız ayarı: 0,25× ile 2× arası.
- Kare şeridi ve "Düzenle" düğmesi.
- Sheet ile GIF arasında geçiş; sheet görünümünde "İşaretle" ve "Yorum ekle".
- İndirme ve paylaşma.

Dört GIF ürettik, Plus hesapta hiç uyarı çıkmadı:

| İstek | Süre | Sonuç |
|---|---|---|
| Çay bardağından yükselen buhar, arkada Boğaz'dan geçen vapur | 90 sn'den kısa | 508×337 px, 9 kare, 1,26 sn. İstek iyi anlaşıldı; sahnede Ortaköy, köprü ve simit var. |
| Aynı GIF'e "Vapurun bacasından duman çıksın, vapur yavaşça geçsin" | 75 sn'den kısa | 380×337 px, 12 kare, 2,16 sn. Duman da vapurun ilerlemesi de geldi. |
| Tebeşirle "Öğretmenler Günü Kutlu Olsun", sonunda kalp | yaklaşık 100 sn | 358×355 px, 12 kare, 4,2 sn. Harfler tek tek beliriyor, ğ ve ü hatasız, kalp de var. En güçlü örnek. |
| Yüklediğimiz logo sıçrayarak gelsin, parlasın, şeffaf arka plan | 90 sn'den kısa | 362×362 px, 12 kare, 1,32 sn, şeffaf. Logo bozulmadı; hareket sade. |

## Mac uygulamasında denediklerimiz

- **Çalışma modunda sunum.** Yeni sohbet ekranının üstünde "Sohbet | Çalışma" anahtarı var. Çalışma modunda "Öğretmenler Günü için 5 slaytlık bir sunum hazırla." dedik. İş 2 dk 51 sn sürdü; bu sırada web'de arama yaptı ve 4 görsel üretti. Sonuç, her slaytında konuşmacı notu olan 5 slaytlık bir PowerPoint dosyası. "Neden 24 Kasım?" slaytındaki iki tarih (1928 Millet Mektepleri Talimatnamesi, 1981'de resmî kutlama) doğru. Dosya uygulamanın içindeki slayt görüntüleyicide açılıyor; PPTX olarak indirebiliyor ya da doğrudan Google Slides, PowerPoint ya da Keynote'ta açabiliyorsunuz. Limit uyarısı çıkmadı.
- **Sohbet içinde oyun.** "5. sınıf öğrencisine kesirleri öğreten küçük etkileşimli bir oyun yap." isteğine 33 saniyede sohbetin içinde oynanabilen bir oyun geldi: 6 soru, puan ve her sorudan sonra açıklama. Ama 2. soruda hata var: dört parçadan ikisi boyalı, oyun da "Boyalı: 2, Toplam: 4" yazıyor, buna rağmen 1/4'ü doğru sayıyor. Oyunu öğrenciye vermeden önce kendiniz baştan sona oynayın.
- **SVG ikon.** "Okul için basit, düz renkli bir 'açık kitap' ikonu üret. SVG dosyası olarak indirebileyim." dedik. 52 saniyede şeffaf, vektörel bir SVG dosyası geldi. Ama dosyayı ChatGPT kod yazarak üretiyor; Images 2.6'nın görüntüleyicisinde SVG indirme seçeneği yok. Yani SVG istediğinizde alabiliyorsunuz, ama bu görsel modelinin bir özelliği değil.
- **Hızlı sohbet.** Option+Space ile ekranın sağ altında küçük bir sohbet kutusu açılıyor. "Bugün İstanbul'da hava nasıl?" sorusu 31 saniyede, kaynaklı ve doğru cevaplandı.
- **Codex.** Codex'e geçiş sol üstteki "ChatGPT ⌄" menüsünden yapılıyor: "ChatGPT · Oluştur, öğren ve keşfet" ve "Codex · Oluştur, hata ayıkla ve yayınla". Codex modunda giriş kutusunda "Codex ile çalış" yazıyor ve kenar çubuğuna kod simgesi ekleniyor.
- **Kenar çubuğu.** Ana sayfa, Zamanlananlar (görev planlama), Kitaplık ve Eklentiler simgeleri var; "…" menüsünde Projeler, GPT'ler ve Kod incelemesi duruyor.

## Diğer yenilikler

- **Aralık'ta ortak kota.** OpenAI'nin 2 Kasım'da kullanıcılara gönderdiği e-postaya göre Plus, Pro ve Business planlarında ChatGPT ve Codex Aralık'tan itibaren tek bir kullanım bütçesini paylaşacak; kalan miktar Ayarlar > Kullanım'da görünecek. Pro'da Instant modeli sınırsız ve kotaya sayılmıyor. Sohbet ve Çalışma'yı birleştiren arayüz önce küçük bir test grubuna açılıyor.
- **GPT-6.1 Terra (26 Ekim).** Plus, Pro, Business, Enterprise ve Edu planlarında Çalışma modu ve Codex'e görsel muhakeme ve bilgisayar kullanımı geldi. Ayrıntılar [Terra haberimizde](/gundem/2026/10/gpt-6-1-terra/).
- **iCloud Mail ve Takvim (27 Ekim).** Tüm planlarda web, masaüstü ve iOS'ta e-posta bulma, takvime bakma ve takvimi güncelleme.
- **Mobilde hesap değiştirme (30 Ekim).** iOS ve Android'de iki hesap açık kalabiliyor; sohbet, bellek ve abonelik ayrı. Ayarlar > Hesap değiştir.
- **Classic kapanıyor.** Eski Mac uygulaması ChatGPT Classic, uygulama içi duyuruya göre 30 Ocak 2027'de kapanacak.

## Sınırlar

- **GIF küçük.** Kare başına yaklaşık 360–510 piksel. Telefonda tam ekran kullanmak yerine bir kartın ya da slaytın içinde gösterin.
- **Etkileşimli içerik hata yapabiliyor.** Kesir oyunu yanlış cevabı doğru saydı.
- **SVG kodla geliyor.** Images 2.6'nın kendi dışa aktarması değil; karmaşık bir görseli SVG'ye çevirmesini beklemeyin.
- **Plan.** Denemeler Plus hesapla yapıldı. GIF'in ücretsiz planda açık olup olmadığını doğrulamadık.
