---
baslik: "Kodla animasyon ve uzun işler için daha hızlı model: Claude Fable 5.2 çıktı"
tarih: 2026-11-12
kategori: araclar
puan: 4
ozet: "Anthropic, 9 Kasım'da Claude Fable 5.2'yi ve aynı temel modelin sınırlı erişimli sürümü Mythos 5.2'yi yayınladı. Şirkete göre Fable 5.2 yanıtları yüzde 30'a kadar daha hızlı veriyor; kodlama, akıl yürütme ve görsel anlamada 5.1'in belirgin önünde. Ücretsiz planda yok; API fiyatı 5.1'e göre yüzde 20 düştü ve Pro'da 16 Kasım'a kadar dahil."
neden_onemli: "Fable 5.2 görsel ya da video üretmiyor; metin ve kod yazıyor. Ama Anthropic onu ürün sayfasında 3D, donanım ve hareket tasarımı için en iyi modeli olarak tanıtıyor: kodla animasyon, sesli anlatım videosu ve etkileşimli 3D sahne. Remotion gibi araçlarla video hazırlayan, kurgu işlerini betikle otomatikleştiren ya da uzun PDF'lerle çalışan içerik üreticileri için doğrudan ilgili bir güncelleme."
yekvisual_notu: "Denedim: Opus 5.5 ile aynı iki istemi verdim (3D ışık stüdyosu ve Boğaz'da vapur). Sonuçlar başa baş; süre de ikisinde yirmi dakika civarı. Fable'ı ikinci kez denediğimde aynı iş 8 dakikada bitti. Tek deneme bir şey kanıtlamıyor; ayrıntılar ve istemlerin tam metni aşağıda."
ucretsiz: false
acik_kaynak: false
zorluk: orta
sirket: Anthropic
model: Claude Fable 5.2
etiketler: [claude, anthropic, fable 5.2, mythos 5.2, kodla video, remotion, api]
kart: kodla-video
kapak: ./claude-fable-5-2/kapak.webp
kapak_kaynak: "Görsel: Anthropic"
kaynaklar:
  - { ad: "Anthropic: Claude Fable 5.2 ve Mythos 5.2 duyurusu", url: "https://www.anthropic.com/claude-fable-and-mythos-5-2" }
  - { ad: "Anthropic: Claude Fable ürün sayfası", url: "https://www.anthropic.com/claude/fable" }
  - { ad: "Claude Yardım Merkezi: Fable 5.2 lansman teklifleri", url: "https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers" }
  - { ad: "Claude Yardım Merkezi: Planınızda Fable modelleri", url: "https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan" }
  - { ad: "Runway MCP", url: "https://runway.com/mcp" }
---

## Neler yeni?

Anthropic, 9 Kasım'da Claude Fable 5.2'yi ve Claude Mythos 5.2'yi duyurdu. İkisi aynı temel model. Fable 5.2 siber güvenlik ve biyoloji konularında sıkı güvenlik önlemleriyle herkese açık; Mythos 5.2 bu önlemleri daha gevşek olan sürüm ve yalnız Anthropic'in Siber Güvenlik ve Yaşam Bilimleri doğrulama programlarına kabul edilen kurumlara açılıyor. Bu yazı, sizin kullanabileceğiniz Fable 5.2 hakkında.

Anthropic'in açıkladıkları:

- **Hız.** Yanıtlar Fable 5.1'e göre yüzde 30'a kadar daha hızlı geliyor.
- **Daha az token.** Claude uygulamalarında ve Claude Code'da varsayılan olan orta çaba ayarında, zor işleri 5.1'den daha az token harcayarak bitiriyor. Çaba ayarı, modelin bir iş üzerinde ne kadar düşüneceğini belirliyor: düşük, orta, yüksek, çok yüksek ve en yüksek.
- **Kodlama, akıl yürütme ve görsel anlama.** Üç alanda da 5.1'e göre iyileşme var.

Anthropic'in kendi ölçümleri (Fable 5.2 ile 5.1):

| Test | Ne ölçüyor? | 5.2 | 5.1 |
|---|---|---|---|
| FrontierCode 2.0 | Ajan olarak kodlama (iki model de çok yüksek çabada) | %49,1 | %32,4 |
| FrontierSWE v2 | Ajan olarak yazılım işleri | %69,9 | %56,3 |
| Remote Labor Index | Uzaktan yapılan gerçek iş görevleri | %41,3 | %17,9 |
| Humanity's Last Exam (araçlarla) | Çok zor akademik sorular | %74,2 | %65,6 |
| Chartography (araçsız) | Görsel anlama | %73,4 | %44,8 |

## 3D, animasyon ve hareket tasarımı

Fable ürün sayfasında "3D, donanım ve hareket tasarımı" başlıklı ayrı bir bölüm var. Anthropic, Fable 5.2'yi gerçek dünya ve ekran için nesne tasarlamada en iyi modeli olarak tanıtıyor ve şunları sayıyor:

- Ayrıntılı görselleri ve PDF'leri okumak,
- Etkileşimli 3D dünyalar kurmak,
- Donanım parçaları tasarlamak,
- Simülasyon ve animasyon hazırlamak,
- Kodla sesli, eğitici anlatım videoları üretmek.

Duyuruda Unity'den bir alıntı da var: en net gelişmeyi sıfırdan daha kaliteli 3D sahneler kurmakta ve bir görsel referanstan bir deneyimi yeniden oluşturmakta görmüşler.

Burada bir ayrımı bilmekte fayda var: **Fable 5.2 görsel ya da video üretmiyor; çıktısı metin ve kod.** Animasyon ve video, modelin yazdığı kodun (örneğin bir Remotion projesinin ya da bir web sayfasının) bilgisayarınızda çalıştırılmasıyla ortaya çıkıyor. Kodla video hazırlamanın nasıl işlediğini [Remotion kartımızda](/bilmeniz-gerekenler/kodla-video/) adım adım anlattık.

Claude'un içinden görsel ya da video üretmek istiyorsanız ayrı bir yol var: Runway'in MCP bağlayıcısı. Claude.ai'ye ya da Claude Desktop'a eklenip Runway hesabınızla giriş yapılıyor; sohbette ne istediğinizi yazıyorsunuz, sonuç aynı sohbete geliyor. Üretimler Runway kredinizden düşüyor ve kullanabileceğiniz modeller Runway planınıza bağlı.

## Kimin işine yarar?

- **Kodla video ve animasyon hazırlayanlar.** Remotion, HTML ya da Three.js ile anlatım videosu, grafik animasyonu veya 3D sahne kuruyorsanız ilk denemeniz gereken alan bu.
- **Kurguyu otomatikleştirenler.** DaVinci Resolve ya da Premiere için betik yazdırmak, dosya düzenlemek, uzun ve çok adımlı işleri bir ajana, yani işi kendi başına adım adım yürüten bir modele bırakmak. Anthropic, Fable 5.2'yi günlerce süren belirsiz mühendislik işlerini yürütebilen bir ana ajan olarak tanıtıyor.
- **Uzun belgeyle çalışanlar.** Ayrıntılı görsel ve PDF okumadaki iyileşme, senaryo, rapor ya da şartname gibi uzun dosyalardan özet ve tablo çıkarırken işe yarayabilir.

Anthropic'in kendisi de günlük kodlama ve bilgi işlerinin çoğu için Claude Opus 5.5'i öneriyor. Fable modelleri kullanım limitinizi daha hızlı tüketiyor; Fable'ı zor ve uzun işlere saklamak mantıklı.

## Nasıl denenir?

**Uygulamada.** Fable 5.2, Ücretsiz planda yok. Normalde planlara göre şöyle:

- **Pro ve Team standart koltuk:** Fable, plan limitlerine dahil değil; kullandıkça ödenen kullanım kredisiyle açılıyor.
- **Max, Ultra, Team ve kurumsal premium koltuk:** Haftalık limitin yüzde 50'sine kadar Fable ek ücret olmadan kullanılabiliyor; sonrası kullanım kredisiyle.

**Lansman haftası teklifleri (9–16 Kasım).** Ücretli aboneliği 9 Kasım'daki lansmandan önce başlamış olanlar için:

- **Pro ve Team standart koltuk:** Fable modelleri 16 Kasım 23.59'a kadar (ABD Pasifik saati; Türkiye saatiyle 17 Kasım 10.59) haftalık limitin yüzde 50'sine kadar dahil. Buna ek olarak, aynı tarihte sona eren bir Fable limit sıfırlaması.
- **Max, Ultra ve premium koltuklar:** Abonelik süresine göre 1 ile 3 arasında Fable limit sıfırlaması (6 aydan az 1, 6–12 ay 2, 12 aydan fazla 3). Bunlar 8 Mart 2027'ye kadar geçerli.

Sıfırlamayı Ayarlar > Kullanım sayfasından kullanıyorsunuz. Varsayılan modeliniz değişmiyor; Fable'ı model seçiciden kendiniz seçmeniz gerekiyor.

**API'de.** Model kimliği `claude-fable-5-2`. Fiyat milyon token başına girdi 8 dolar, çıktı 40 dolar (5.1'de 10 ve 50 dolardı); önbellekten okunan girdi 0,20 dolar. Hızlı mod 2,5 kata kadar daha hızlı, fiyatı girdi 16, çıktı 80 dolar; Claude Code'da, Claude Platform'da, Google Cloud'da ve Microsoft Foundry'de var. Model AWS, Google Cloud ve Microsoft Foundry üzerinden de kullanılabiliyor.

## Sınırlar

- **Rakamlar Anthropic'in.** Hız ve test sonuçlarının hepsi şirketin kendi ölçümleri; bağımsız bir test henüz yok. Aynı tabloda bazı testlerde rakipler önde: örneğin iş akışı testi AutomationBench'te Gemini 4 Carbon (%53,9) Fable 5.2'yi (%51,4) geçiyor.
- **Görsel ve video üretmiyor.** Hareketli içerik ancak kodla, ya da Runway gibi bir bağlayıcıyla geliyor.
- **Limitleri hızlı tüketiyor.** Pro'da lansman haftası bitince Fable kullanım kredisine geçiyor.
- **Veri saklama.** Fable kullanımında güvenlik denetimi için 30 günlük veri saklama varsayılan olarak zorunlu; sıfır veri saklama yalnız uygun kurumsal müşterilere açık.
- **Bazı konular başka modele yönlendiriliyor.** Güvenlik önlemlerine takılan siber güvenlik soruları Opus 4.8'e, biyoloji soruları Opus 5'e aktarılabiliyor. Anthropic'e göre yanlış engellemeler 5.1'e göre yaklaşık yüzde 55 azaldı.

## Denedim: Opus 5.5 ile aynı istem

Fable 5.2'ye ve Opus 5.5'e aynı iki istemi verdim; ikisi de Claude Code'da, kendi bilgisayarımda çalıştı. Çıktıları kaydedip yan yana koydum: [Instagram'daki karşılaştırma](https://www.instagram.com/yekvisual/).

| | Opus 5.5 | Fable 5.2 (1. deneme) | Fable 5.2 (2. deneme) |
|---|---|---|---|
| Işık stüdyosu | 13 dk 20 sn · 5 düzeltme turu | 7 dk 57 sn · 2 tur | 2 dk 53 sn · 1 tur |
| Boğaz'da vapur | 6 dk 26 sn · 2 tur | 13 dk 1 sn · 6 tur | 5 dk 7 sn · 1 tur |
| **Toplam** | **19 dk 46 sn · 7 tur** | **20 dk 58 sn · 8 tur** | **8 dk 0 sn · 2 tur** |

Bilmeniz gerekenler:

- **Süreyi ve turları modeller kendisi ölçtü** ve "düzeltme turu"nu kendileri tanımladı. Tanımlar birebir aynı değil.
- **Her istem her modelde bir kez denendi.** Fable'ı ikinci kez, ayrı bir oturumda denedim; Opus'u ikinci kez denemedim. Bu yüzden "hangisi daha hızlı" sorusunun cevabı bu deneme değil; ikinci deneme yalnız tek ölçümün ne kadar oynak olduğunu gösteriyor.
- **Opus istemden biraz saptı:** stilleri 1,5 yerine 1,4 saniyede değiştirdi ve bunu notuna yazdı. Fable iki denemede de isteme uydu.
- **Videodaki yüzleri sonradan kadına çevirdim.** Üç sayfada da yalnız baş ve omuz modeline dokundum; ışık, zamanlama ve liste kodu modellerin yazdığı gibi kaldı.
- Vapurda en iyi kesitleri seçtim; Opus'un videosunda görüntünün bir an beyaza patladığı kısmı almadım.

### İstem 1 · Işık stüdyosu

> Ekteki görsel, bir Instagram videosunun üç karesi: aynı kişinin yüzünde ışık stilleri sırayla değişiyor, solda numaralı bir liste büyüyor. Bu fikri Three.js ile gerçek zamanlı 3D sahne olarak yeniden kur.
> - Ortada, ışığı güzel gösteren stilize bir insan başı ve omuzları olsun. Geometri ya da shader ile kurabilirsin; dışarıdan model indirme.
> - 13 ışık stili sırayla gelsin, her biri 1,5 saniye: Rembrandt, kelebek (paramount), yarım (split), loop, kontra (arkadan), siluet, altın saat, mavi saat, high key, low key, neon, pencere ışığı, alttan ışık.
> - Işıklar fiziksel olarak doğru yönden gelsin, gölgeler doğru düşsün.
> - Solda o ana kadarki ışıkların numaralı listesi büyüsün, o anki madde vurgulansın.
> - Toplam 20 saniye; sonunda tüm stillerin küçük bir ızgarası görünsün.

### İstem 2 · Boğaz'da vapur

> Three.js ile gün batımında İstanbul Boğazı'nı kur.
> - Ön planda ilerleyen bir şehir hatları vapuru, bacasından çıkan duman parçacıkları.
> - Suda dalga simülasyonu ve güneş yansıması; uçuşan martılar.
> - Ufukta cami ve köprü siluetleri (basit geometriyle).
> - Kamera 20 saniyelik sinematik bir yol izlesin; sonunda başa dönsün.
> - Normal açılışta fareyle kamera çevrilebilsin; kayıt modunda kamera sabit yolu izlesin.

İki istemin sonuna aynı teknik kuralları ekledim: tek bir `index.html` dosyası, dikey 1080×1920 tuval ve videoya kaydedebilmek için saniyeye göre kare çizen bir `renderAt(t)` fonksiyonu.

