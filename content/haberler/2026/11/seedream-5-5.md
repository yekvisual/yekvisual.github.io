---
baslik: "Arka planı silmeden şeffaf görsel, 100 tura kadar düzenleme: Seedream 5.5"
tarih: 2026-11-12
kategori: gorsel
puan: 4
ozet: "ByteDance'in Seed ekibi 9 Kasım'da görsel modeli Seedream 5.5'i duyurdu. Model şeffaf ya da yarı saydam arka planlı görseli doğrudan üretiyor, aynı görsel üzerinde 100 tura kadar düzenlemeye dayanıyor ve küçük, sık yazıyı daha az bozuyor. Dola, BytePlus Playground ve Dreamina'da deneyebiliyorsunuz; Pro sürümü sonra gelecek."
neden_onemli: "Çıkartma, ürün kesimi ya da logo gibi bir görseli tasarıma yerleştirmek için şimdiye kadar ayrı bir arka plan silme adımı gerekiyordu; saç teli ve cam gibi kenarlar da çoğu zaman bozuluyordu. Seedream 5.5 bu katmanı baştan şeffaf üretiyor. Art arda düzenlemede dokunulmayan alanların piksel piksel korunması da aynı görseli adım adım geliştirmek isteyenler için önemli: her turda renk kayması ve bulanıklaşma birikmiyor."
yekvisual_notu: "Magnific'te denedim. Şeffaf çıktı duman, ağaç dalı, çıkartma ve ürün kesiminde gerçekten silme adımını atlatıyor; ama cam, su ve sabun köpüğünün içi opak çıkıyor. Aynı fotoğrafı 20 tur düzenledim: yüz ve kadraj yerinde kaldı, Türkçe harfler (Ç, ü, ı) doğru yazıldı. Bir turda ise gözlüğü çıkar deyince kadının gözlerini de kapattı. Ayrıntılar ve istemler aşağıda."
ucretsiz: null
acik_kaynak: false
zorluk: yeni
sirket: ByteDance
model: Seedream 5.5
etiketler: [seedream, bytedance, görsel üretim, görsel düzenleme, şeffaf arka plan, dreamina]
kapak: ./seedream-5-5/kapak.webp
kapak_kaynak: "Görsel: ByteDance Seed (Seedream 5.5 ile üretildi)"
medya:
  - { tip: gorsel, src: ./seedream-5-5/kucuk-yazi-gazete.webp, alt: "ByteDance'in yazı örneği: Shakespeare üzerine gazete sayfası. Başlıklar, sütunlarca küçük metin, portre ve Globe Tiyatrosu çizimi tek görselde.", kaynak: "Görsel: ByteDance Seed" }
kaynaklar:
  - { ad: "ByteDance Seed: Seedream 5.5 duyurusu", url: "https://seed.bytedance.com/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5" }
  - { ad: "ByteDance Seed: Seedream 5.5 model sayfası", url: "https://seed.bytedance.com/en/seedream5_5" }
  - { ad: "Dreamina: Seedream 5.5", url: "https://dreamina.capcut.com/seedream/seedream-5-5" }
  - { ad: "Runware: Seedream 5.5 belgeleri", url: "https://runware.ai/docs/models/bytedance-seedream-5-5" }
  - { ad: "Crypto Briefing: Seedream 5.5'in yayılımı", url: "https://cryptobriefing.com/bytedance-seedream-5-5-image-model-rollout/" }
---

## Neler yeni?

ByteDance'in yapay zekâ araştırma ekibi Seed, 9 Kasım'da görsel üretme ve düzenleme modeli Seedream 5.5'i duyurdu. Duyuruya göre öne çıkanlar:

- **Şeffaf çıktı.** Model alfa kanalı olan, yani tamamen ya da kısmen şeffaf arka planlı görseli doğrudan üretiyor. Ayrı bir arka plan silme adımı gerekmiyor. Model sayfasındaki örnekler arasında çıkartma setleri, birbirine yapboz gibi oturan peluş karakterler, şeffaf zeminli yazı tasarımı ve bir görseli şeffaf katmanlara ayırma var.
- **100 tura kadar düzenleme.** Aynı görsel üzerinde art arda yaptığınız düzenlemelerde, dokunmadığınız alanlar piksel düzeyinde aynı kalıyor ve renk kayması olmuyor. ByteDance bunun aynı görselde 100 tur düzenlemeye kadar dayandığını söylüyor. Örneklerde odadaki mobilya ve ışığı, bir kişinin saçını ve kıyafetini, bir saatin kadranındaki verileri tek tek değiştiriyor.
- **Daha doğal ışık ve doku.** Işık, malzeme ve cilt dokusu daha doğal; aşırı parlaklık, patlamış ışık ve lekeli doku azaldı.
- **Küçük ve sık yazı.** Karmaşık harf biçimlerinde ve sık dizilmiş küçük metinde (Çince ve İngilizce) ilerleme var. ByteDance'in ölçümünde ağır yazı bozulması oranı %0,4'e, hafif bozulma oranı %1,7'ye indi.

ByteDance, modeli kendi MagicArena platformunda e-ticaret, pazarlama, film ve televizyon, oyun, ofis işleri ve moda tasarımı olmak üzere altı kullanım alanında Seedream 5.0 Pro ile karşılaştırdı ve altısında da kaliteyi daha yüksek buldu. Film-televizyon ve ofis işlerinde kullanılabilir sonuç oranı önceki sürümün iki katından fazla. GPT Image 2.5 Sunburst ve [Nano Banana 2.1](/gundem/2026/10/nano-banana-2-1/) ile karşılaştırmada yazı yapısında önde olduğunu söylüyor. Bu sonuçların hepsi ByteDance'in kendi ölçümü; bağımsız bir test henüz yok.

**Teknik ayrıntılar.** ByteDance çözünürlüğü ve referans görsel sayısını açıklamadı. Modeli sunan sağlayıcıların sayfalarına göre:

- **Çözünürlük.** 1K, 1,5K ve 2K; 4K seçeneği yok. Higgsfield ve Runware'de en yüksek ayar 2K.
- **Referans görsel.** Üretim ve düzenlemede en çok 10 referans görsel (Runware).
- **Biçim.** Şeffaf arka plan için PNG ya da WebP gerekiyor. Higgsfield'da arka plan için "otomatik", "şeffaf" ve "opak" seçenekleri var.

ByteDance, Seedream 5.5 serisinin Pro sürümünün sonra geleceğini söylüyor; tarih vermiyor.

## Kimin işine yarar?

- **İçerik üreticileri:** Çıkartma, emoji seti, karakter ya da ürün görselini doğrudan şeffaf alıp Canva, CapCut ya da kurgu programında başka bir zemine yerleştirmek için.
- **E-ticaret ve reklam ekipleri:** Ürünü sabit tutup ışığı, rengi ya da malzemeyi tur tur değiştirmek; arka planı ayrı katman olarak almak.
- **Afiş ve bilgi kartı hazırlayanlar:** Küçük puntolu ve çok sütunlu metin içeren görsellerde daha az harf bozulması.

## Nasıl denenir?

- **Dola:** Model sayfasındaki "Try Dola" bağlantısı [dola.com/chat](https://www.dola.com/chat/) adresindeki sohbet ekranına gidiyor.
- **Dreamina:** "AI Image" bölümünde istemi yazın, model listesinden "Image 5.5" (Seedream 5.5) seçin, en-boy oranını, çözünürlüğü ve görsel sayısını ayarlayıp üretin. Sonra renk, biçim ya da yazıyı yeni bir istekle düzeltin. Dreamina, modelin hesabınızda görünüp görünmediğinin ve kredi maliyetinin hesaba göre değiştiğini yazıyor.
- **BytePlus Playground:** Geliştiriciler için, [ai.byteplus.com](https://ai.byteplus.com/en/playground) üzerinden.
- **Higgsfield:** 12 Kasım itibarıyla model listesinde Seedream 5.5 var.

**Ücretsiz mi?** Netleşmedi. ByteDance fiyat açıklamadı; Dreamina'nın sayfasında da kredi bilgisi yok. Basına yansıyan haberlere göre Dreamina ve CapCut'ta zaman zaman sınırsız üretim kampanyaları yapılıyor, ama kalıcı bir ücretsiz kotası doğrulanmadı. API tarafında Runware, 1,5K'ya kadar görsel için 0,02 $, 2K için 0,035 $ fiyat yazıyor; referans görsel başına 0,008 $ ekleniyor. Türkiye'den erişimi kendimiz kontrol etmedik.

## Sınırlar

- **4K yok.** Bugünkü sağlayıcılarda en yüksek çözünürlük 2K. Büyük baskı ya da 4K ekran için büyütme gerekiyor.
- **Yazı örnekleri Çince ve İngilizce.** ByteDance yalnızca bu iki dilde iyileşme iddia ediyor; başka dillerdeki yazıyı denemek lazım.
- **Karşılaştırmalar ByteDance'in.** Kalite ve yazı bozulması oranları şirketin kendi platformunda ölçüldü.
- **Katman adları karışabiliyor.** Runware'in belgelerine göre görseli katmanlara ayırırken model katmanlara kendisi ad veriyor ve bu adlarda Çince karışabiliyor; süslü ya da çok küçük yazılar metin katmanı olarak tanınmayabiliyor.
- **Erişim aşamalı.** Model önce ByteDance'in kendi ürünlerinde açıldı; ABD'ye ve başka pazarlara ne zaman tam olarak açılacağı belli değil.

## Denedim: şeffaf çıktı ve 20 tur düzenleme

Seedream 5.5'i Magnific üzerinden 2K çözünürlükte denedim. Şeffaflık Magnific'te ek bir ayarla açılıyor ve fiyatı opak görselle aynı.

**Şeffaf çıktı (12 istem).** Her istemin sonuna "Arka plan şeffaf." ekledim.

- **İyi çıkanlar:** duman (gerçekten yarı saydam), çiçekli ağaç dalı, beyaz spor ayakkabı (gölgesi de yarı saydam), çıkartmalar, dantel delikleri, yuvarlak etiket. Etiketteki "ŞEFFAF", "İSTANBUL" ve "Görsel Üretim Atölyesi" yazıları doğru çıktı.
- **Orta:** saç. Teller tek tek korunuyor, ama uçlarda açık renkli bir hale var ve koyu zeminde belli oluyor.
- **Kötü:** cam bardak, su sıçraması ve sabun köpüğü. Dış kenar temiz, ama içleri opak; arkadaki zemin camın içinden görünmüyor.
- **İstenmeyen eklemeler:** kediye pizza ve konfeti, etikete ikinci bir "ŞEFFAF", yuvarlak istenen dantel kare çıktı.

Örnek istemler:

> Kalın beyaz kenarlı çıkartma: güneş gözlüklü turuncu kedi. Arka plan şeffaf.

> Havada kıvrılarak yükselen ince, yarı saydam beyaz duman bulutu; uçlarında silikleşen ince duman telleri. Fotoğraf. Arka plan şeffaf.

> Dört ayrı çıkartmadan oluşan set: ince belli bir çay bardağı, susamlı bir simit, bir martı ve Galata Kulesi. Her biri kalın beyaz kenarlı, aralarında boşluk var. Arka plan şeffaf.

> Buzlu bir bardak limonata; cam bardak ve buz küpleri yarı saydam, üstünde nane yaprağı, bardakta su damlaları. Stüdyo ürün fotoğrafı. Arka plan şeffaf.

**20 tur düzenleme.** Önce bir fotoğraf ürettim, sonra her turda bir önceki çıktıyı referans verip tek bir şeyi değiştirdim:

> İstanbul'da sade bir kafe. Pencere kenarındaki küçük yuvarlak mermer masada oturan, lacivert ceketli, gözlüklü, omuz hizasında koyu kahverengi saçlı otuzlu yaşlarda bir kadın, kameraya dönük. Masada beyaz bir fincan kahve. Arkada açık kırmızı tuğla duvar ve üstünde "KAHVE" yazan küçük siyah bir tabela, köşede yeşil bir saksı bitkisi. Pencereden uzakta Galata Kulesi görünüyor. Gündüz, doğal ışık, fotoğraf.

Her turun kalıbı:

> Bu fotoğrafta yalnızca tek bir değişiklik yap: [değişiklik]. Kadının yüzü, kimliği, pozu, kadraj, ışık ve diğer tüm nesneler aynen kalsın.

Turlar sırayla: ceket yeşil, tabakta simit, duvar gri sıva, gün batımı ışığı, gözlüğü çıkar, fincan kırmızı, gözlerini açsın, pencerede karlı kış, saçlar küt, tabelada "ÇAY", saksıda kaktüs, karşı sandalyede yaşlı bir adam, kareli masa örtüsü, tavanda ampul, kırmızı atkı, menü kartı ("Günün çorbası: Mercimek", "90 TL"), pervazda uyuyan kedi, gece ve kar, duvar saati, cam vazoda lale.

- **Tutan:** 20 turun sonunda kadın açıkça aynı kişi, kadraj hiç kaymadı, ayrıntı bulanıklaşmadı. "ÇAY" ve menü kartındaki ü, ç, ı doğru yazıldı.
- **Tutmayan:** "Gözlüğü çıkar" deyince kadının gözlerini de kapattı; bir tur daha verip düzelttim. Pencereye kış manzarası istediğimde içerideki gün batımı ışığını da kışa çevirdi. Gece turunda birkaç kar tanesi içeri düştü.
- Düzenleme pikselleri koruyan bir mod değil; her tur görseli yeniden üretiyor. Ölçtüğüm kadarıyla dokunulmayan yüz her turda çok az kayıyor, ama 20 turda gözle görülür bir bozulma yok.

