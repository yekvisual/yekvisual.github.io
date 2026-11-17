---
baslik: "Mekân fotoğraflarından gezilebilir 3D set: World Labs Atlas araçlarıyla yayında"
tarih: 2026-11-12
kategori: 3d
puan: 4
ozet: "World Labs, 1 Eylül'de tanıttığı dünya modeli Atlas'ı 12 Kasım'da araçları ve geliştirici API'siyle birlikte yayınladı. Viewfinder'da tek bir görselden ya da en çok 64 fotoğraftan bir mekânı yeniden kuruyor, içinde kamera yolu çizip video alıyor, sahneyi Gaussian splat olarak indiriyorsunuz. Yanında Chisel, Relight ve Splats to Mesh araçları, bir API ve Blender eklentisi var."
neden_onemli: "Keşif çekiminde (location scout) çekilen fotoğraflar çoğu zaman bir klasörde kalıyor. Atlas bunları içinde kamera gezdirilebilen bir sete çevirmeyi vaat ediyor: çekimden önce kamera hareketini denemek, plan listesini çıkarmak ya da ön görselleştirme (previz) yapmak için. Fotoğraf sayısı arttıkça model daha az uyduruyor; tek görselden ise mekânın görünmeyen kısımlarını kendisi tamamlıyor. Splat ve mesh çıktısının Blender'a ve oyun motorlarına gidebilmesi, sonucu tek bir platformda kilitli bırakmıyor."
yekvisual_notu: "Denedim: küçük bir kayıt odasını telefonla 18 karede çekip Atlas'ın Viewfinder aracına verdim. Kamera ve derinlik tahmini bir dakikadan kısa sürdü; gezilebilir 3D sahne (splat) ise tahmin edilen 15 dakikada bitmedi; 18. dakikada hâlâ işleniyordu, bir saat dolmadan hazırdı. Sonuç: duvar panelleri, sandalye, zemin ve masa kenarı net ve yerinde; fotoğraflamadığım tavan ise renkli bir sise dönüştü. Yeni hesaba verilen 10.000 ücretsiz kredinin 5.000'i bu tek sahneye gitti; kayıt için telefon doğrulaması istiyor."
ucretsiz: true
acik_kaynak: false
zorluk: orta
sirket: World Labs
model: Atlas
etiketler: [world labs, atlas, dünya modeli, 3d sahne, gaussian splat, previz, viewfinder, blender]
kapak: ./world-labs-atlas/kapak.webp
kapak_kaynak: "Görsel: World Labs"
medya:
  - { tip: video, src: ./world-labs-atlas/kamera-yolu-splat.mp4, alt: "World Labs'in Atlas tanıtım filminden: yeniden kurulan bir avluda kamera yolu anahtar karelerle çiziliyor, yörünge hareketi render ediliyor, sonra sahne Gaussian splat'e çevriliyor. 14 sn, sessiz.", kaynak: "Video: World Labs" }
  - { tip: video, src: ./world-labs-atlas/film-vfx.mp4, alt: "Atlas sayfasındaki film ve VFX örneği: üretilen dünyalarda nokta bulutundan görüntüye geçen kamera hareketleri. 12 sn, sessiz.", kaynak: "Video: World Labs" }
denemeler:
  - { tip: gorsel, src: ./world-labs-atlas/deneme-girdi.webp, alt: "Atlas'a verdiğim 18 telefon fotoğrafından üçü: dar bir kayıt odası, akustik paneller, masa ve sandalyeler.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./world-labs-atlas/deneme-splat.webp, alt: "Atlas'ın bu fotoğraflardan kurduğu 3D sahne (Gaussian splat), içinden bakış. Paneller, sandalye ve zemin net; fotoğraflanmayan tavan renkli bir sise dönüşmüş.", kaynak: "YEK Lab denemesi" }
kaynaklar:
  - { ad: "World Labs: Atlas", url: "https://www.worldlabs.ai/atlas" }
  - { ad: "World Labs Blog: duyurular (12 Kasım 2026)", url: "https://www.worldlabs.ai/blog" }
  - { ad: "World Labs Blog: Atlas: A World Model for Spatial Intelligence (1 Eylül 2026)", url: "https://www.worldlabs.ai/blog/atlas" }
  - { ad: "Atlas belgeleri: Faturalandırma", url: "https://docs.atlas.worldlabs.ai/billing" }
  - { ad: "Atlas belgeleri: Splat oluşturma", url: "https://docs.atlas.worldlabs.ai/scene-to-splats" }
  - { ad: "Atlas belgeleri: Blender", url: "https://docs.atlas.worldlabs.ai/blender" }
  - { ad: "Atlas belgeleri: Görev özeti", url: "https://docs.atlas.worldlabs.ai/task-overview" }
  - { ad: "World Labs: Hakkında", url: "https://www.worldlabs.ai/about" }
---

## Neler yeni?

World Labs, yapay zekâ araştırmacısı Fei-Fei Li'nin Justin Johnson, Ben Mildenhall ve Christoph Lassner'la birlikte kurduğu, eylül sonunda AMD'ye katıldığını duyuran bir şirket. Şirket 1 Eylül'de Atlas adlı "dünya modelini" tanıtmıştı: üç boyutlu bir mekânı görsellerden üreten, yeniden kuran ve içinde istenen açıdan yeni görüntüler çıkaran bir model. 12 Kasım'daki duyuruyla Atlas, onu kullanan araçlar ve geliştirici API'siyle birlikte yayına girdi.

World Labs'in teknik yazısına göre Atlas metin, görsel, video ve 3D üzerinde sıfırdan eğitilmiş tek bir model. Kamera konumunu doğrudan girdi olarak alıyor; yani "sola dön" gibi bir yazıyla değil, kameranın tam yeri ve açısıyla yönlendiriliyor. Ne kadar çok fotoğraf verirseniz o kadar az uyduruyor: şirkete göre çoğu zaman iki üç görsel bile mekânı sadık biçimde kurmaya yetiyor, tek görselde ise görünmeyen kısımları kendisi tamamlıyor.

Atlas'la birlikte çıkan araçlar:

- **Viewfinder.** Fotoğraflarınızı ya da ürettiğiniz görselleri yüklüyorsunuz, Atlas sahneyi yeniden kuruyor ve içinde kamerayı serbestçe gezdirebiliyorsunuz. Kamera yolunu anahtar karelerle (keyframe) çizip video olarak render ediyorsunuz; üç ya da daha fazla anahtar karede yol başa dönerek döngü yapabiliyor. Uygulamanın arayüzüne göre bir sahneye en çok 64 görsel girilebiliyor.
- **Chisel.** Sahneyi kaba bloklarla kurup (grayboxing) yapısını siz belirliyorsunuz; nesneleri taşıdıkça her kamera görünümü güncelleniyor.
- **Relight.** Splat sahnelerin ışığını değiştirmeye yönelik bir araç.
- **Splats to Mesh.** Gaussian splat'i gerçek geometrisi olan bir mesh'e çeviriyor; API belgelerine göre çıktı GLB, isteğe bağlı doku ya da köşe rengi ve çarpışma kutularıyla.
- **API ve Blender.** Geliştirici API'si Atlas'ın görevlerini kendi uygulamanıza ya da iş akışınıza bağlıyor. World Labs'in Blender eklentisiyle sahneyi Blender içinde üretip düzenleyebiliyorsunuz.

**Gaussian splat ne?** Bir sahneyi milyonlarca küçük, yarı saydam renkli noktayla temsil eden 3D biçim. Fotoğrafa yakın görünüyor ve bilgisayarda gerçek zamanlı dönebiliyor; ama klasik bir 3D model gibi düzenlenebilir yüzeyi yok. Splats to Mesh bu yüzden var.

**Dışa aktarma.** Viewfinder'dan iki şey indiriyorsunuz: görseller, derinlik haritaları ve kamera bilgileri ("Spatial Context") ile Gaussian splat. Splat SPZ ya da PLY olarak iniyor. Belgelere göre Blender 5.3 splat'leri doğrudan açıyor; dosyayı görüntü alanına sürüklemek yetiyor.

## Kimin işine yarar?

- **Film ve reklam ekipleri:** Mekân fotoğraflarından gezilebilir bir set kurup çekimden önce kamera hareketini, objektif açısını ve plan sırasını denemek için. World Labs'in Film ve VFX örneği de tam bunu anlatıyor: bir set kurup kamerayı içinde yönetmek ve gereken planları render etmek.
- **Mimari ve iç mimari:** Fotoğraflardan ya da kaba bir blok sahneden mekânı kurup her açıdan gezmek, sonra mesh olarak kendi programınıza almak için.
- **Oyun ve etkileşimli içerik yapanlar:** Bir görselden üretilen dünyayı mesh'e çevirip oyun motoruna taşımak için.
- **Robotik araştırmacıları:** Gerçek ya da üretilmiş sahnelerden simülasyon ortamı kurmak için.

## Nasıl denenir?

- **Viewfinder:** [atlas.worldlabs.ai](https://atlas.worldlabs.ai/workflows/viewfinder) üzerinden tarayıcıda açılıyor. Fotoğraf yükleyin ya da görsel üretin, sahneyi kurun, kamera yolu çizip render alın.
- **Fotoğraf çekerken:** Belgeler aynı mekânı birbirini örten, net, ışığı ve pozlaması benzer karelerle çekmeyi, sahnenin olabildiğince sabit kalmasını öneriyor. Balık gözü ya da güçlü bozulmalı objektifle çekilen görsellerin önce düzeltilmesi gerekiyor.
- **API:** [docs.atlas.worldlabs.ai](https://docs.atlas.worldlabs.ai/quickstart) adresinde hızlı başlangıç, komut satırı aracı, MCP sunucusu ve Blender eklentisinin kurulumu var.

**Ücretsiz mi?** Netleşmedi. Atlas Studio'nun abonelikli olduğu belgelerde geçiyor, ama plan fiyatlarını yayımlanmış bir sayfada bulamadık. API tarafında fiyatlar kredi üzerinden: 1 dolar 1.000 kredi ve satın alınan kredinin süresi dolmuyor. Bir sahneyi Gaussian splat'e çevirmek 15–25 dakika sürüyor ve 5.000 kredi (5 $) tutuyor; görsel düzenleme 125 kredi (0,125 $), görsel büyütme 10 kredi (0,01 $), istem iyileştirme 20 kredi (0,02 $). World Labs fiyat tablosunun değişebileceğini belirtiyor. Türkiye'den erişimi kendimiz kontrol etmedik.

## Sınırlar

- **Model boşlukları uyduruyor.** Az fotoğrafla ya da tek görselle başlarsanız, görünmeyen alanları Atlas tahmin ediyor. Gerçek bir mekânın birebir kopyasını istiyorsanız daha çok ve birbirini örten fotoğraf gerekiyor; belgeler tek bir oda için 8–16 görünüm öneriyor.
- **Çözünürlük.** API'de üretilen yeni görünümler dört sabit boyuttan birinde çıkıyor (1280×720, 960×720, 528×704, 720×1280). Final plan değil, previz ve deneme için düşünmek daha doğru.
- **Splat düzenlenebilir bir model değil.** Yakından ve tek bir açıdan görülen yüzeyler bulanık kalabiliyor; iki görünümde farklı duran bir nesne çift görüntüye dönüşebiliyor. Mesh'e çevirmek ayrı bir adım.
- **Kapasite sınırları belli değil.** World Labs'in hız sınırı sayfası dakika ve saat başına görev sınırlarını henüz "açıklanacak" olarak gösteriyor.
- **Karşılaştırmalar World Labs'in.** Yeniden kurmada uzman modelleri geçtiği iddiası şirketin kendi ölçümü; bağımsız bir test henüz yok.


## Denedim: 18 fotoğraftan bir oda

Atlas'a Google hesabıyla girdim; kayıt sırasında telefon numarası ve SMS doğrulaması istedi. Yeni hesaba 10.000 ücretsiz Studio kredisi tanımlandı.

- **Girdi.** Küçük bir kayıt odasını telefonla 18 karede, her karede biraz yana kayarak çektim. Viewfinder HEIC dahil fotoğrafları kabul ediyor ama hepsini 528×704 piksele küçültüyor; tek seferde en fazla 64 kare.
- **Kamera ve derinlik.** "Reconstruct" seçeneğinde (aynı mekânın örtüşen fotoğrafları) her karenin konumu ve derinliği bir dakikadan kısa sürede çıktı; sahne önce nokta bulutu olarak beliriyor. Bu adım kare başına 2 kredi.
- **Splat.** Gezilebilir 3D sahne 5.000 kredi tutuyor; arayüz "yaklaşık 15 dakika" diyor; bizde 18. dakikada hâlâ işleniyordu, bir saat dolmadan hazırdı. Atlas en az 12 kare öneriyor.
- **Sonuç.** Fotoğraflarda iyi görünen her şey (duvar panelleri, sandalye, zemin, masa kenarı) yerli yerinde ve içinde dolaşılabiliyor. Hiç fotoğraflamadığım tavan ise renkli bir sise dönüştü: Atlas görmediğini uyduruyor ama inandırıcı değil. Mekân çekerken tavanı ve köşeleri de kadraja almak gerekiyor.
- **Kamera hareketli video.** Video için sahnede elle kamera yolu kurmak gerekiyor; bu denemede ona girmedim.
