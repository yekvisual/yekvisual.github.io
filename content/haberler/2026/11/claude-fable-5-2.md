---
baslik: "Kodla animasyon ve uzun işler için daha hızlı model: Claude Fable 5.2 çıktı"
tarih: 2026-11-12
kategori: araclar
puan: 4
ozet: "Anthropic, 9 Kasım'da Claude Fable 5.2'yi ve aynı temel modelin sınırlı erişimli sürümü Mythos 5.2'yi yayınladı. Şirkete göre Fable 5.2 yanıtları yüzde 30'a kadar daha hızlı veriyor; kodlama, akıl yürütme ve görsel anlamada 5.1'in belirgin önünde. Ücretsiz planda yok; API fiyatı 5.1'e göre yüzde 20 düştü ve Pro'da 16 Kasım'a kadar dahil."
neden_onemli: "Fable 5.2 görsel ya da video üretmiyor; metin ve kod yazıyor. Ama Anthropic onu ürün sayfasında 3D, donanım ve hareket tasarımı için en iyi modeli olarak tanıtıyor: kodla animasyon, sesli anlatım videosu ve etkileşimli 3D sahne. Remotion gibi araçlarla video hazırlayan, kurgu işlerini betikle otomatikleştiren ya da uzun PDF'lerle çalışan içerik üreticileri için doğrudan ilgili bir güncelleme."
yekvisual_notu: "Henüz denemedim. İlk olarak Reels'te kullandığım Remotion şablonuna aynı istemle yeni bir sahne yazdırıp Fable 5.2'yi Opus 5.5 ile süre ve düzeltme sayısında karşılaştıracağım; ardından bir DaVinci kurgu betiği ve 100 sayfalık bir PDF'ten tablo çıkarma geliyor. Bu haftaki ek kullanım, bunları limit derdi olmadan denemek için iyi bir fırsat."
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
