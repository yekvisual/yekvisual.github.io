---
baslik: "Notlarınızı ve kaynaklarınızı etkileşimli bir siteye çevirin: Gemini Notebook"
tarih: 2026-11-16
yayin: 2026-11-17
kategori: araclar
puan: 4
ozet: "Google, 16 Kasım'da Gemini Notebook'a kaynaklardan etkileşimli site üretme özelliğini ekledi. Not defterinin sohbetine \"make me a site\" yazıp ne istediğinizi anlatıyorsunuz; Gemini Notebook yüklediğiniz kaynaklardan çalışan bir sayfa kuruyor: etkileşimli bir periyodik tablo, satış panosu ya da proje takip listesi gibi. Özellik 16 Kasım itibarıyla dünya genelinde web'de 18 yaş üstü kullanıcılara açılmaya başladı; mobil uygulamaya sonra gelecek."
neden_onemli: "Bir konuyu anlatmak için şimdiye kadar ya düz bir özet alıyordunuz ya da sayfayı kendiniz kodluyordunuz. Burada kaynaklarınızdan tıklanabilen, içine not alınabilen, kendini sınayan bir sayfa çıkıyor. Ders hazırlayan, bir projeyi ekibine anlatan ya da elindeki veriyi müşteriye göstermek isteyen biri için kod bilmeden ilk taslağa ulaşmanın kısa yolu."
yekvisual_notu: "Denedim: sitemizdeki 24 araç sayfasını kaynak olarak verip 'Hangi iş için hangi yapay zekâ aracı?' diye bir rehber site istedim. Yaklaşık dört dakikada iş seçme düğmeleri, ücretsiz filtresi, arama kutusu ve 24 araç kartı olan, gayet derli toplu bir sayfa çıktı; kartlardaki değerlendirmeler kaynaklardan alınmış. Paylaşmadan önce bilmeniz gereken: siteyi gören, not defterinin kaynaklarına da erişiyor."
ucretsiz: true
acik_kaynak: false
zorluk: yeni
sirket: Google
model: Gemini Notebook
etiketler: [gemini, google, gemini notebook, etkileşimli site, sunum, eğitim, pano]
kapak: ./gemini-notebook-site/kapak.webp
kapak_kaynak: "Görsel: Google"
medya:
  - { tip: video, src: ./gemini-notebook-site/site-uretimi.mp4, alt: "Google'ın tanıtım videosu (48 sn, sesli): yedi kaynaklı bir kimya not defterinden periyodik tabloyu anlatan, sonunda kısa bir sınav bulunan site; ardından dört kaynaktan proje takip panosu ve beş kaynaktan çeyrek dönem satış panosu üretiliyor.", kaynak: "Google" }
denemeler:
  - { tip: gorsel, src: ./gemini-notebook-site/deneme-kurgu-filtresi.webp, alt: "Kurgu/Montaj seçilince kalan beş araç: DaVinci Resolve, Runway, Remotion, HyperFrames, Claude Code. Her kartta fiyat etiketi, seviye, ne işe yaradığı, nasıl erişildiği ve sitemizdeki değerlendirmenin özeti.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./gemini-notebook-site/deneme-video-kartlari.webp, alt: "Video üretim kartlarından bir bölüm: Replicate, Kling 4.0, Google Flow, MiniMax Hailuo, Seedance 2.5, Pika H3 Flex.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./gemini-notebook-site/deneme-arac-rehberi.webp, alt: "Gemini Notebook'un sitemizdeki 24 araç sayfasından ürettiği 'Hangi iş için hangi yapay zekâ aracı?' sitesi: iş seçme düğmeleri, ücretsiz filtresi, arama kutusu ve araç kartları. Üretim yaklaşık 4 dakika sürdü.", kaynak: "YEK Lab denemesi" }
kaynaklar:
  - { ad: "Google: Gemini Notebook ile etkileşimli siteler", url: "https://blog.google/innovation-and-ai/products/gemini-notebook/interactive-sites" }
  - { ad: "Gemini Notebook Yardım: Site oluşturma", url: "https://support.google.com/gemininotebook/answer/18945748" }
  - { ad: "Gemini Notebook Yardım: Planlar ve sınırlar", url: "https://support.google.com/gemininotebook/answer/16213268" }
  - { ad: "Gemini Notebook Yardım: Kullanım sınırları", url: "https://support.google.com/gemininotebook/answer/17670842" }
  - { ad: "Gemini Notebook Yardım: Gemini Notebook hakkında", url: "https://support.google.com/gemininotebook/answer/16164461" }
  - { ad: "Gemini Notebook", url: "https://notebook.google.com/" }
---

## Neler yeni?

Gemini Notebook, Google'ın kaynak yükleyip onlar üzerine sohbet ettiğiniz not defteri uygulaması. PDF, web sitesi, YouTube videosu, ses dosyası, Google Dokümanlar ve Slaytlar gibi kaynakları bir not defterine topluyorsunuz; Sohbette yanıtlar bu kaynaklara dayanıyor ve satır içi kaynak gösteriliyor. 16 Kasım'dan itibaren bu kaynaklardan etkileşimli bir site de üretebiliyor.

Google'ın verdiği örnekler:

- **Sınava hazırlık için görsel anlatımlar:** etkileşimli bir periyodik tablo ya da tarih şeridi.
- **Veriyi keşfetmek için panolar:** örneğin çeyrek dönem satış performansı.
- **Proje takip listeleri:** işleri ve son tarihleri izlemek için.

Google'ın görsellerinde ve tanıtım videosundaki periyodik tablo sitesinde bir arama kutusu, element gruplarına göre filtreler, seçilen elementin bilgi kartı ve sayfanın sonunda altı soruluk kısa bir sınav görünüyor. Yardım sayfasına göre site, işaretlediğiniz kutuları, aldığınız notları ve doldurduğunuz alanları kaydediyor; tekrar açtığınızda kaldığınız yerden devam ediyorsunuz.

## Nasıl yapılır?

1. [notebook.google.com](https://notebook.google.com/) adresinde bir not defteri açın ya da yenisini oluşturup kaynaklarınızı ekleyin. Site üretmek için not defterinde düzenleme yetkiniz olmalı.
2. **Chat** panelinde "make me a site" yazıp ne istediğinizi tarif edin. Google'ın videosundaki örnek: "Make me a site to help me understand the periodic table."
3. Üretim biraz sürebiliyor; bu sırada not defterinde çalışmaya devam edebiliyorsunuz.
4. Site **Studio** panelinde çıkıyor. Tam ekran için sitenin yanındaki **More** menüsünden **Open in new tab** seçin.

**Paylaşmak ve indirmek.** Aynı menüden **Share** ile bağlantı alabiliyor, **Download** ile siteyi indirebiliyorsunuz. Herkese açık paylaşım için kişisel bir Google hesabı ve not defterinde sahip ya da düzenleyici olmanız gerekiyor. Bağlantıyı açacak kişinin not defterinin tamamına erişimi olmalı: not defterini o kişiyle ya da "bağlantıya sahip herkes" ile paylaşmanız gerekiyor. Paylaşılan sitede herkes yalnızca kendi girdiğini görüyor; siz de başkalarının girdilerini görmüyorsunuz. Siteyi silerseniz ya da paylaşımı kapatırsanız eski bağlantılar çalışmıyor.

## Ücretsiz mi, kimler kullanabilir?

- **Kimler:** Google'a göre özellik 16 Kasım'dan itibaren dünya genelinde web'de, 18 yaş üstü Gemini Notebook kullanıcılarına, Google Workspace aboneleri dahil kademeli olarak açılıyor. Mobil uygulamaya "yakında" gelecek. Google, yaşınızı Google hesabınızda doğrulamanızı istiyor.
- **Plan:** Duyuruda ve site üretiminin yardım sayfasında ücretli plan şartı yok; belirtilen şart 18 yaş. Gemini Notebook'u Gmail hesabıyla ücretsiz kullanabiliyorsunuz.
- **Kota:** Site üretmek kullanım sınırınızdan düşüyor. Gemini Notebook'ta sınırlar istemin karmaşıklığına, kullanılan modele ve özelliğe göre hesaplanıyor; kota 5 saatte bir yenileniyor, haftalık bir üst sınır da var. Google AI Plus'ta sınır standardın 2 katı, Pro'da 4 katı; Ultra'da aboneliğe göre Pro'nun 5 ya da 20 katı.
- **Kaynak sayısı:** Plansız hesapta en çok 100 not defteri ve not defteri başına 50 kaynak (notlar hariç); Plus'ta 100, Pro'da 300 kaynak.
- **Türkiye:** Gemini Notebook'un desteklenen ülkeleri arasında Türkiye var; uygulama 80'den fazla dili destekliyor.

## Dikkat edilecekler

- **Paylaşım kaynakları da açar.** Siteyi gören kişinin not defterinin tamamına erişmesi gerekiyor. Müşteri verisi ya da yayımlanmamış bir çalışma içeren not defterlerinden site paylaşmadan önce bunu hesaba katın.
- **Örnekler İngilizce.** Google'ın istem kalıbı İngilizce; Türkçe istemle ve Türkçe kaynaklarla nasıl sonuç verdiğini denemek lazım.
- **Doğruluğu kontrol edin.** Site kaynaklarınızdan üretiliyor, ama Gemini Notebook'un kendi arayüzündeki uyarıda yazdığı gibi hata yapabiliyor; özellikle sayı içeren panolarda değerleri kaynakla karşılaştırın.
- **Şimdilik yalnız web.** Telefonda site üretmek için mobil uygulamaya gelmesini beklemek gerekiyor.

## Denedim: 24 araç sayfasından seçim rehberi

Sitemizdeki 24 araç sayfasının bağlantısını tek seferde kaynak olarak ekledim ve sohbet kutusuna şunu yazdım: "Bana bir site yap: Hangi iş için hangi yapay zekâ aracı? Ziyaretçi önce yapmak istediği işi seçsin; seçince o işe uygun araçlar kart olarak çıksın; üstte ücretsiz olanları gösteren bir filtre olsun; yalnız kaynaklardaki bilgileri kullan."

- **Süre.** Site Studio panelinde yaklaşık dört dakikada hazır oldu; bu sırada sohbet ve diğer işler kullanılabiliyor.
- **Sonuç.** İş seçme düğmeleri (görsel, video, seslendirme, müzik, kurgu, otomasyon), arama kutusu, "yalnızca ücretsiz olanlar" anahtarı, özet sayılar ve her araç için bir kart: ne işe yaradığı, nasıl erişildiği, ücret durumu ve kaynak sayfadaki değerlendirmenin özeti. İstemediğim bir dil filtresini de kendisi ekledi.
- **Sitenin yapısı.** Üstte altı iş düğmesi var ve yanlarında kaç araç olduğu yazıyor: Görsel Üret 9, Video Üret 10, Seslendirme 3, Müzik 2, Kurgu/Montaj 5, Otomasyon/Kod 9 (bir araç birden çok işte görünebiliyor). Altında araç adına ya da amaca göre arama kutusu ve "yalnızca ücretsiz olanları göster" anahtarı duruyor. Özet kutuları 24 aracın 16'sının ücretsiz ya da freemium olduğunu gösteriyor (4'ü tamamen ücretsiz, 12'si freemium).
- **Bir kartın içi.** Aracın adı ve tek satırlık tanımı, sağ üstte "Ücretsiz / Freemium / Ücretli" etiketi, erişim ve seviye etiketleri, "Ne işe yarar?", aracın resmi sitesine bağlantı veren "Nasıl erişilir?" ve kaynak sayfadaki değerlendirmenin kısa özeti. En altta aracın hangi işlerde göründüğü yazıyor; Kurgu/Montaj seçince örneğin DaVinci Resolve, Runway, Remotion, HyperFrames ve Claude Code kalıyor.
- **Ad.** Not defterine biz ad vermedik; kaynaklara bakıp kendine "YEK Lab Yapay Zekâ Araçları Rehberi" adını verdi.
- **Doğruluk.** Kartlardaki bilgiler kaynak sayfalardan geliyor; yine de yayınlamadan önce birkaç kartı kaynakla karşılaştırmak gerekir.
- **Paylaşım.** Siteyi paylaşmak, not defterini paylaşmak demek: gören kişi kaynakları da görebiliyor. Kişisel ya da iş belgelerinden yapılan siteleri paylaşırken buna dikkat edin.

Denemeyi ücretli Google AI Pro hesabımla yaptım.
