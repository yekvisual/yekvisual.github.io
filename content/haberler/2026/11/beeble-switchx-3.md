---
baslik: "Oyuncuya dokunmadan mekânı değiştirin: Beeble SwitchX 3.0 elde kamerada, 4K'da"
tarih: 2026-11-11
kategori: video
puan: 4
ozet: "Beeble, 11 Kasım'da video-videoya model SwitchX 3.0'ı yayınladı. Model çekilmiş bir planda oyuncunun performansını kare kare koruyup mekânı, ışığı ve arka plandaki her şeyi değiştiriyor. Yenilikler: tek işte dört referans görsel, hareket eden arka planlar, elde ve koşarak çekilmiş planlarda işaretsiz kamera takibi ve daha iyi prompt kontrolü. Çıktı 4K'ya kadar, kredi fiyatı 2.0 ile aynı; kullanmak için ücretli plan gerekiyor."
neden_onemli: "Yeşil perdede ya da yanlış mekânda çekilmiş bir planın arka planını değiştirmek bugün maske, kamera takibi (match move) ve kompozit olmak üzere üç ayrı iş demek. SwitchX 3.0 bunu tek işleme indirmeyi vaat ediyor: oyuncunun pikselleri kaynaktan geliyor, yalnızca çevresi ve ışığı yeniden üretiliyor. Elde çekimde takibin tutması ve kare sayısıyla en-boy oranının kaynakla birebir aynı kalması, sonucu doğrudan kurgu zaman çizelgesine koyabilmek için önemli."
yekvisual_notu: "12 yıldır post-prodüksiyonda arka plan değişimini key, track ve kompozit adımlarıyla yapıyorum; SwitchX'in iddiası bu üçünü tek işe indirmek. İlk deneyeceğim şey elde çekilmiş, saçı ve el hareketi bol bir röportaj planı: kenarlarda titreme var mı, yüzdeki yeni ışık mekânla tutuyor mu, kare kare bakmak lazım. Henüz denemedim; 4K ve 10-bit çıktının yalnızca Professional planda olması da denemenin maliyetini belirleyecek."
ucretsiz: false
acik_kaynak: false
zorluk: orta
sirket: Beeble
model: SwitchX 3.0
etiketler: [beeble, switchx, video düzenleme, vfx, arka plan değiştirme, kamera takibi, yeşil perde, minimax]
kapak: ./beeble-switchx-3/kapak.webp
kapak_kaynak: "Görsel: Beeble"
medya:
  - { tip: video, src: ./beeble-switchx-3/ofis-metro.mp4, alt: "Solda kaynak çekim, sağda SwitchX 3.0: kanepede kameraya konuşan sunucu aynı performansla metro vagonuna taşınıyor. 10 sn, sessiz.", kaynak: "Video: Beeble" }
  - { tip: video, src: ./beeble-switchx-3/elde-kamera.mp4, alt: "Solda kaynak, sağda SwitchX 3.0: buğday tarlasında elde kamerayla takip edilen kadın, gece pazarına taşınıyor; arka plan kamera hareketine kilitli. 5 sn, sessiz.", kaynak: "Video: Beeble" }
  - { tip: gorsel, src: ./beeble-switchx-3/dort-referans.webp, alt: "Tek işte verilen dört referans: meydan, iki reklam panosu kartı ve sıralamayı gösteren storyboard.", kaynak: "Görsel: Beeble" }
  - { tip: video, src: ./beeble-switchx-3/dort-referans.mp4, alt: "Solda yeşil perde çekimi, sağda SwitchX 3.0: dört referansla kurulan meydan; dev ekran kartları storyboard sırasıyla oynatıyor. 5 sn, sessiz.", kaynak: "Video: Beeble" }
kaynaklar:
  - { ad: "Beeble Updates: SwitchX 3.0", url: "https://beeble.ai/updates/2026-11-11-switchx-3" }
  - { ad: "Beeble Research: Introducing SwitchX 3.0", url: "https://beeble.ai/research/switchx-3-0" }
  - { ad: "Beeble: Fiyatlandırma ve plan karşılaştırması", url: "https://beeble.ai/pricing" }
  - { ad: "Beeble YouTube: SwitchX 3.0 tanıtım filmi", url: "https://www.youtube.com/watch?v=EC02tPJfAsA" }
---

## Neler yeni?

Beeble, video efekti (VFX) araçları geliştiren bir şirket. SwitchX ise şirketin video-videoya modeli: çekilmiş bir videoyu alıp oyuncuyu yerinde bırakıyor, arka planı, ışığı ve sahnedeki diğer şeyleri değiştiriyor. 11 Kasım'da yayınlanan 3.0, Beeble'ın deyişiyle SwitchX'in şimdiye kadarki en büyük güncellemesi.

Beeble'a göre SwitchX 3.0, MiniMax'ın genel amaçlı video modeli H3'ün üzerine kuruldu. Şirket modeli kendi veri setiyle ve kendi mimarisiyle yalnızca video-videoya prodüksiyon işi için yeniden kurduğunu, sonuna da orijinal görüntüyü ayrıntı için yeniden okuyan ve 4K'ya kadar çıkan bir son geçiş eklediğini söylüyor.

Değişmeyen çekirdek **Source-Locked Rendering**: model, oyuncunun alfa maskesini (oyuncuyu arka plandan ayıran siyah-beyaz maske) kullanarak performansı kare kare, piksel piksel kaynağa kilitliyor. Değişen yalnızca çevre ve oyuncunun üzerine düşen ışık.

3.0'daki dört yenilik:

- **Dört referans görsel.** Tek bir işte en çok dört görsel verebiliyorsunuz: setin geniş planı, bir dekor parçasının yakını, hatta bir storyboard. Beeble'ın örneklerinde yeşil perdede çekilmiş bir kadın, meydan fotoğrafı, iki reklam kartı ve bir storyboard ile bir meydana taşınıyor; dev ekran kartları storyboard'daki sırayla oynatıyor. Başka bir örnekte bir kat planı ve her oda için bir görselle yeşil perdeli koridor yürüyüşü tek planlık, kesintisiz bir geçişe dönüşüyor.
- **Hareket eden arka planlar.** Arka plan artık 2.0'dakinden çok daha hareketli: geçen trafik, yürüyen kalabalık, patlama, yanan ateş, duman, yağan kar. Örneklerde boş bir meydan yolcularla doluyor, gündüz çekilmiş bir planda gece oluyor ve pencerenin ardından sokak lambaları, evler akıp geçiyor.
- **Kamera takibi.** Elde, dairesel (orbit) ve koşarak çekilmiş planlarda yeni arka plan dünyaya sabit kalıyor; Beeble bunun için işaretleyiciye (tracking marker) ya da ayrı bir match move adımına gerek olmadığını söylüyor.
- **Prompt kontrolü.** Sahnede ne olacağını, nasıl hareket edeceğini ve ne zaman olacağını yazabiliyorsunuz. Beeble'ın örnek promptları: "O koşarak geçerken güvercinler havalansın" ve "O yaklaştıkça tavan lambaları tek tek yansın."

**Teknik ayrıntılar.** Beeble'ın araştırma sayfasına göre çıktı 4K'ya kadar ve 10-bit renkte; kare sayısı kaynakla birebir aynı, en-boy oranı değişmiyor. Fiyat sayfasına göre SwitchX 3.0'da bir video en çok 360 kare olabiliyor (30 fps'te 12 saniye; 2.0'da sınır 480 kare). Önce 720p'de deneyip beğendiğiniz sonucu daha yüksek çözünürlükte bitirebiliyorsunuz.

## Kimin işine yarar?

- **Kurgu ve post-prodüksiyon ekipleri:** Yanlış mekânda ya da yeşil perdede çekilmiş bir planı, yeniden çekmeden ve ayrı bir kompozit adımı kurmadan başka bir mekâna taşımak için.
- **Reklam ve tanıtım filmi yapanlar:** Ürünü ya da sunucuyu aynı tutup mekânı, günün saatini ya da hava durumunu değiştirmek için; dört referansla markanın görsellerini sahneye yerleştirmek için.
- **Küçük bütçeli dizi ve kısa film ekipleri:** Pahalı bir mekân çekimi yerine sade bir alanda ya da yeşil perdede çekip ortamı sonradan kurmak için.

## Nasıl denenir?

SwitchX 3.0, Beeble'ın bulut uygulamasında iki yerden açılıyor: Beeble'ın düğüm tabanlı iş akışı aracı Canvas'ta bir düğüm olarak ya da ayrı SwitchX sayfasında. Kaynak videoyu yükleyip referans görselleri ve promptu veriyorsunuz.

**Ücretsiz mi?** Hayır. Beeble'ın fiyat sayfasına göre ücretli planı olmayan hesaplar ayda 90 kredi alıyor, ama bu kredi yalnızca VFX Pass Generator ve 3D Relight'ta geçiyor; SwitchX için en az Creator planı gerekiyor. Plan ve kredi bilgileri:

| | Creator | Professional |
|---|---|---|
| Aylık fiyat | 19 $ (yıllık ödemede ayda 16 $) | 75 $ (yıllık ödemede ayda 60 $) |
| Aylık kredi | 540 | 2.400 |
| 720p | saniyesi 6 kredi | saniyesi 6 kredi |
| 1080p | saniyesi 20 kredi | saniyesi 20 kredi |
| 2160p (4K) | yok | saniyesi 80 kredi |
| Dışa aktarma | MP4 | MP4 ve 10-bit MOV |

Beeble'ın kendi hesabıyla 30 fps'te 4 saniyelik videoda Creator'ın aylık kredisi 1080p'de 6 videoya, Professional'ınki 4K'da 7 videoya yetiyor. Kredi fiyatı SwitchX 2.0 ile aynı. Ücretli planlarda ticari kullanım lisansı var. Beeble ücretli kullanıcıların içeriğiyle model eğitmediğini yazıyor. Türkiye'den erişimi kendimiz kontrol etmedik.

## Sınırlar

- **Uzunluk.** Bir videoda en çok 360 kare var; daha uzun bir planı parçalara bölmek gerekiyor.
- **4K yalnızca Professional'da.** Creator planında en yüksek çözünürlük 1080p, 10-bit çıktı da yok.
- **Örnekler Beeble'ın.** "Mükemmel kamera takibi" ve hareket eden arka planlar şirketin seçtiği planlarda gösterildi; bağımsız bir karşılaştırma henüz yok. Hızlı hareket, saç ve yarı saydam kenarlarda nasıl davrandığını denemek lazım.
- **Işık oyuncuya da değiyor.** Performans kaynağa kilitli, ama Beeble oyuncunun yeni mekâna göre yeniden ışıklandırıldığını söylüyor. Yüz rengi ve ten tonunun hassas olduğu işlerde sonucu kare kare kontrol etmek gerekiyor.
- **API ayrı.** Bireysel planlar API erişimi içermiyor; Beeble'ın yerel masaüstü ürünü Beeble Studio da ayrı lisanslanıyor.
