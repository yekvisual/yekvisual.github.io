---
baslik: "16 referans görselle 4K üretin: MiniMax'ın açık kaynak modeli H3-Image"
tarih: 2026-11-11
kategori: gorsel
puan: 4
ozet: "MiniMax, 11 Kasım'da görsel üretme ve düzenleme modeli H3-Image'ı ağırlıklarıyla birlikte yayınladı. Şirkete göre model 4096×4096 piksellik bir görseli 10 saniyenin altında üretiyor ve düzenlemede 16 referans görsele kadar alıyor. Hugging Face'ten indirip ComfyUI ile kendi makinenizde çalıştırabiliyor ya da MiniMax'ın API'si ve Hailuo üzerinden kullanabiliyorsunuz. Lisans Türkiye'de ücretsiz kullanıma izin veriyor; yıllık geliri 1 milyon doları aşanlar için yazılı izin şart."
neden_onemli: "Bugün yaygın görsel modellerin çoğu 1–2K üretiyor; büyük baskı, ekran ya da kırpma payı için ayrı bir büyütme adımı gerekiyor. H3-Image 16 megapikseli doğrudan, büyütücü kullanmadan üretiyor ve bunu indirilebilir bir modelde yapıyor. Dikey 9:16'da da çıktı 3072×5472. Ama donanım ağır, kullanıcı oylarında da liderlerin epey gerisinde: hız ve çözünürlük iddiasını kalite karşılaştırmasıyla birlikte okumak gerekiyor."
yekvisual_notu: "Denedim, MiniMax'ın Hugging Face'teki ücretsiz demosunda. Türkçe yazdığım iki istemi sahne tarifi olarak anlamadı: istemin kendisini afiş yazısı gibi bastı, harfleri de bozdu. Aynı simitçi sahnesini İngilizce tarif edince tabeladaki 'Taze Simit 15 ₺' yazısı TL işaretine kadar doğru çıktı, fotoğraf da inandırıcıydı; yalnız simitler susamsız, burgu çörek gibiydi. 4 MP görsel kuyruk dahil 10–16 saniyede geldi. 4K'yı deneyemedim: tek bir 4K görsel ücretsiz GPU kotasını aştı."
ucretsiz: true
acik_kaynak: true
zorluk: teknik
sirket: MiniMax
model: MiniMax H3-Image
etiketler: [minimax, minimax h3, görsel üretim, görsel düzenleme, 4k, açık kaynak, comfyui, hailuo]
kart: acik-kaynak-modeller
kapak: ./minimax-h3-image/kapak.webp
kapak_kaynak: "Görsel: MiniMax (H3-Image ile üretilen örnekler)"
medya:
  - { tip: gorsel, src: ./minimax-h3-image/on-referans-oturma-odasi.webp, alt: "On referansla düzenleme: üstte boş, güneş alan bir oda ve dokuz ayrı mobilya; altta model bunları tek bir oturma odasında birleştirmiş.", kaynak: "Görsel: MiniMax" }
  - { tip: gorsel, src: ./minimax-h3-image/3d-render-film-karesi.webp, alt: "Tek referansla düzenleme: solda dokusuz, gri bir 3D ay üssü render'ı; sağda aynı sahne fotogerçekçi bir film karesi olarak.", kaynak: "Görsel: MiniMax" }
denemeler:
  - { tip: gorsel, src: ./minimax-h3-image/deneme-simitci-ingilizce.webp, alt: "İngilizce istem: Karaköy'de buğulu camın ardında simit tezgâhı, el yazısı tabelada 'Taze Simit 15 ₺'. 1824×2304 (4 MP), 15,8 sn. Yazı ve TL işareti doğru; simitler susamsız, burgu çörek gibi.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./minimax-h3-image/deneme-simitci-turkce.webp, alt: "Aynı sahne Türkçe istemle: model istemi sahne olarak değil afiş yazısı olarak bastı; 'Aaraköy', '15 €' gibi bozulmalar var. 15,9 sn.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./minimax-h3-image/deneme-ogretmenler-gunu.webp, alt: "Türkçe istem: 1970'lerde köy okulu, kara tahtada 'Öğretmenler Günü kutlu olsun'. Yine sahne yerine yazı afişi çıktı, harfler bozuk. 9,9 sn.", kaynak: "YEK Lab denemesi" }
kaynaklar:
  - { ad: "MiniMax: H3-Image duyurusu", url: "https://minimax.io/blog/minimax-h3-image" }
  - { ad: "Hugging Face: MiniMaxAI/MiniMax-H3-Image", url: "https://huggingface.co/MiniMaxAI/MiniMax-H3-Image" }
  - { ad: "MiniMax-H3-Image Community lisansı", url: "https://huggingface.co/MiniMaxAI/MiniMax-H3-Image/blob/main/LICENSE" }
  - { ad: "MiniMax API: görsel üretim kılavuzu", url: "https://platform.minimax.io/docs/guides/image-generation" }
  - { ad: "MiniMax API: fiyatlar", url: "https://platform.minimax.io/docs/guides/pricing" }
  - { ad: "ComfyUI eğitimi: MiniMax-H3-Image", url: "https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image" }
  - { ad: "Hugging Face: Comfy-Org/MiniMax-H3-Image", url: "https://huggingface.co/Comfy-Org/MiniMax-H3-Image" }
  - { ad: "vLLM-Omni: H3-Image donanım ve gecikme ölçümleri", url: "https://recipes.vllm.ai/MiniMaxAI/MiniMax-H3-Image" }
  - { ad: "Hailuo: MiniMax H3-Image", url: "https://hailuoai.video/tools/minimax-h3-image" }
  - { ad: "Artificial Analysis: metinden görsele sıralaması", url: "https://artificialanalysis.ai/text-to-image/arena/leaderboard-text" }
---

## Neler yeni?

MiniMax, 11 Kasım'da görsel modeli H3-Image'ı duyurdu. Model, şirketin açık video modeli MiniMax H3'ün üzerine kurulu; [Pika H3 Flex](/gundem/2026/10/pika-h3-flex/) de aynı aileden. H3-Image metinden görsel üretiyor, referans görselden üretiyor ve görsel düzenliyor; üretim ve düzenleme aynı model dosyasında.

MiniMax'ın duyurusuna ve model kartına göre öne çıkanlar:

- **Doğrudan 16 megapiksel.** Model her en-boy oranında yaklaşık 16 megapiksel üretiyor: kare için 4096×4096, dikey 9:16 için 3072×5472, 21:9 için 6272×2688. Büyütücü (upscaler) kullanılmıyor. Model kartına göre en iyi sonuç 16 megapiksel civarında; çalışma aralığı yaklaşık 4–20 megapiksel.
- **10 saniyenin altında 4K.** MiniMax, 4096×4096 bir görselin 10 saniyenin altında çıktığını ve bunun yaygın alternatiflerden 5 kata kadar hızlı olduğunu söylüyor. Hangi donanımda ölçüldüğünü duyuruda yazmıyor. vLLM-Omni'nin ölçümünde dört NVIDIA H200 ekran kartıyla 4736×3552 bir görsel 3,84 saniye sürmüş.
- **16 referans görsel.** Düzenlemede en çok 16 görsel verebiliyorsunuz; istemde bunlara `<Picture 1>`, `<Picture 2>` diye sırayla atıf yapıyorsunuz. Model kartındaki örneklerden birinde boş bir oda ve dokuz mobilya tek bir oturma odasında birleştiriliyor.
- **6 adımda üretim.** Model 6 örnekleme adımına damıtılmış; negatif istem desteklenmiyor.
- **İstem genişletici.** Model ayrıntılı, İngilizce bir sahne tarifi bekliyor. MiniMax'ın API'si kısa bir istemi, hangi dilde yazılmış olursa olsun, üretimden önce bu tür bir tarife çeviriyor. Yerelde aynı işi isteğe bağlı MiniMax-H3-Image-PE modeli yapıyor.

MiniMax ayrıca modelin açık modeller arasında isteme en iyi uyan model olduğunu, "yapay zekâ görüntüsü" denen aşırı pürüzsüz görünümden uzak, ayrıntılı ve gerçekçi sonuç verdiğini söylüyor. Bu iddialar için ad verilmiş bir kıyaslama ya da puan yayınlamadı.

**Kullanıcı oylarında nerede?** Artificial Analysis'in, kullanıcıların iki görseli kimin ürettiğini bilmeden karşılaştırdığı metinden görsele sıralamasında 17 Kasım itibarıyla H3-Image 1066 puanla 25., Highspeed sürümü 1072 puanla 24. sırada. Yani hız ve çözünürlükte iddialı, ama kör oylamada liderlerin epey gerisinde.

## Kimin işine yarar?

- **Baskı ve büyük ekran işi yapanlar:** Afiş, billboard, sahne ekranı gibi yüksek çözünürlük isteyen işlerde ayrı bir büyütme adımı olmadan başlamak için.
- **Dikey içerik üretenler:** 9:16'da 3072×5472 çıktı, Reels ya da Story görselinde kırpıp yeniden kadraj yapmak için bol pay bırakıyor.
- **Mekân ve ürün görselleştirenler:** Bir odayı ve ayrı ayrı çekilmiş mobilyaları ya da ürünleri tek sahnede birleştirmek; dokusuz bir 3D render'ı fotogerçekçi kareye çevirmek.
- **Kendi sunucusunu kuranlar:** Ağırlıklar indirilebilir; Diffusers, SGLang, vLLM-Omni, LightX2V, DiffSynth-Studio ve ComfyUI destekleniyor.

## Nasıl denenir?

**Hailuo ve API.** MiniMax, modelin Hailuo AI'da, MiniMax Code'da ve API platformunda olduğunu söylüyor. Hailuo'daki tanıtım sayfası ise erişimin hesabınızdaki model seçicide görünmesine bağlı olduğunu yazıyor. API'de iki model var: standart MiniMax-H3-Image ve daha hızlı MiniMax-H3-Image-Highspeed. Şirkete göre standart mod alternatiflerin 1,5–2 katı, Highspeed 3–4 katı hızda.

**Kendi bilgisayarınızda.** En kolay yol ComfyUI: şablon kütüphanesinde "MiniMax-H3-Image Text to Image" ve "MiniMax-H3-Image Image Edit" iş akışları var (ComfyUI 0.45.0 ve sonrası). Comfy'nin sıkıştırılmış dosyaları toplam yaklaşık 55 GB: 21 GB görsel modeli, 25,3 GB metin kodlayıcısı, 7,3 GB istem genişletici ve 1,2 GB VAE. Şablon, belleği az makinelerde hata vermesin diye 4 megapikselden başlıyor; tam çözünürlüğe siz çıkıyorsunuz.

**Ücretsiz mi?** Ağırlıkları indirip kendi makinenizde kullanmak ücretsiz (lisans koşulları aşağıda). API ücretli. MiniMax'ın fiyat sayfasındaki örnek hesaba göre standart modelde 1K görsel yaklaşık 0,022 $, 2K 0,023 $, 4K 0,069 $; Highspeed'de 4K 0,13 $. Fiyat, istemin uzunluğuna göre biraz değişiyor. Lansman haftasında 16,6 megapiksel ve üzeri görsellerde uygulanan %50 indirim 17 Kasım'da sona erdi. Hailuo'da ücretsiz kota olup olmadığını MiniMax açıklamadı.

## Donanım

H3-Image ev bilgisayarı için ağır bir model. Model kartı ekran belleği için bir rakam vermiyor; ölçümler vLLM-Omni'nin sayfasında:

- **Dosya boyutu.** Görsel modeli BF16'da 68,65 GB; metin kodlayıcısı MiniMax H3'ün deposundan ayrıca iniyor, 66,7 GB. vLLM-Omni'ye göre diskte toplam yaklaşık 127 GB. Model 33,1 milyar parametreli.
- **Tek kart.** Bir H200'de görsel modeli bellekte tutup metin kodlayıcısını dışarı alınca en yüksek bellek kullanımı 73,4 GiB, 2048×2048 görsel 3,2 saniye. Katmanları sırayla belleğe alan modda bellek 14,7 GiB'e iniyor, süre 8,3 saniyeye çıkıyor.
- **Tüketici kartı.** Topluluktan gelen bir rapora göre tek bir RTX 4090 (24 GB) bu katman katman yükleme moduyla görsel üretebilmiş. vLLM-Omni bunun bellek, hız ya da düzenleme desteği için bir ölçüm olmadığını not ediyor.
- **Mac.** MiniMax, ComfyUI ve vLLM-Omni Apple Silicon için bir destek ya da ölçüm vermiyor.

## Lisans ve sınırlar

H3-Image, MiniMax-H3-Image Community lisansıyla yayınlandı. Lisans metnine göre:

- **Bölge.** Lisans AB, İngiltere, Güney Kore ve ABD'yi kapsam dışı bırakıyor; bu ülkelerde modelin de çıktılarının da kullanımı lisansa aykırı. Türkiye kapsamda.
- **Ticari kullanım.** Kullanım bedava, ama sizin ya da bağlı şirketlerinizin yıllık geliri 1 milyon doları aşıyorsa veya modeli başkalarına hizmet olarak sunuyorsanız MiniMax'tan önceden yazılı izin almanız gerekiyor. Bu eşik video modeli H3'teki 20 milyon dolardan çok daha düşük. Modeli kullanan ticari bir ürünün arayüzünde "MiniMax-H3-Image" ibaresi görünmeli.
- **Çıktılar.** MiniMax ürettiğiniz görseller üzerinde hak iddia etmiyor; sorumluluk sizde. Çıktıları başka bir yapay zekâ modelini geliştirmek için kullanamıyorsunuz.
- **Etiketleme.** Kabul edilebilir kullanım politikası, modelle üretilen içeriği kamuya açık bir yerde yayınlarken makine üretimi olduğunu açıkça belirtmeyi şart koşuyor. Sosyal medyada paylaşacaksanız gönderide yapay zekâ ile üretildiğini yazın.
- **Değerlendirme.** Hız, isteme uyma ve gerçekçilik iddiaları MiniMax'ın kendi ölçümü. Kör oylamada model şimdilik ilk 20'nin dışında.
- **Yazı.** Model kartındaki yazı örnekleri Çince ve İngilizce; Türkçe yazıyı aşağıda denedim.

## Denedim: Türkçe istem, İngilizce istem

MiniMax'ın Hugging Face'teki resmi demosunda (ücretsiz GPU kotasıyla, varsayılan 4 MP ayarında) üç görsel ürettim; her istemden tek sürüm.

- **Türkçe istemler sahneye dönmedi.** "Karaköy'de sabah, simit tezgâhı…" ve "1970'lerden bir köy okulu sınıfı…" istemlerinin ikisinde de model sahneyi çizmek yerine istemin kendisini büyük harflerle afişe dizdi; "Aaraköy", "15 €", "Kış ışdcı" gibi bozulmalar çıktı.
- **İngilizce istemde tabela kusursuz.** Aynı simitçi sahnesini İngilizce tarif ettim, tabeladaki yazıyı Türkçe bıraktım. "Taze Simit 15 ₺" doğru yazıldı, TL işareti bile yerinde; buğulu cam ve yağmur damlaları inandırıcı. Simitler ise susamsız, burgu çörek gibi: yerel nesneleri tanıması sınırlı.
- **Hız.** 4 MP (1824×2304) görsel, demo kuyruğu dahil 10–16 saniyede geldi.
- **4K'yı deneyemedim.** Tek bir 4K görsel, ücretsiz kotanın izin verdiğinden fazla GPU süresi istedi (278 saniye).

Kısacası: istemi İngilizce yazın, görselde görünmesini istediğiniz Türkçe yazıyı tırnak içinde verin.
