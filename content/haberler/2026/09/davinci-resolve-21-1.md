---
baslik: "DaVinci Resolve 21.1: Claude'a medya düzenletip toplu render aldırmak"
tarih: 2026-09-08
kategori: araclar
puan: 5
ozet: "Blackmagic Design, IBC 2026'da DaVinci Resolve 21.1'i yayınladı. Sürüm; Claude, Claude Code ve ChatGPT Codex gibi yapay zekâ asistanlarının Resolve'a bağlanmasını sağlıyor: projeyi analiz etme, medyayı düzenleme, ayar değiştirme, uzun çekimden özet kurgu çıkarma ve toplu render gündelik dille isteniyor. Güncelleme ücretsiz."
neden_onemli: "Kurgucuların zamanının büyük kısmı yaratıcı karar değil, dosya düzenleme ve render kuyruğu gibi tekrar işlerine gidiyor. Asistanın bu işleri Resolve'un kendi fonksiyonlarıyla yapması, dışarıdan betik yazmayı bilmeyen kurgucuya da otomasyon kapısı açıyor. 20 yeni betik API'si ve konsol, ileri kullanıcılar için ayrı bir kazanım."
yekvisual_notu: "Studio 21.1 bende kurulu ve Claude Code bağlantısı tanımlı; uzun çekimden özet kurgu çıkarma işini gerçek bir çekimle henüz denemedim, deneyip burada paylaşacağım. Kurgu kararını asistana bırakmayı düşünmüyorum, dosya düzeni ve render kuyruğu için bakıyorum. Ücretsiz sürümde bu bağlantının olmadığını unutmayın."
ucretsiz: false
acik_kaynak: false
zorluk: orta
sirket: Blackmagic Design
model: DaVinci Resolve 21.1
etiketler: [davinci resolve, blackmagic, kurgu, claude, mcp, otomasyon, render]
kart: ai-ile-video-edit
kaynaklar:
  - { ad: "Blackmagic Design basın bülteni", url: "https://www.blackmagicdesign.com/media/partial/release/20260908-03" }
  - { ad: "DaVinci Resolve: Yenilikler", url: "https://www.blackmagicdesign.com/products/davinciresolve/whatsnew" }
  - { ad: "CineD", url: "https://www.cined.com/davinci-resolve-21-1-released-ai-assistant-integration-via-mcp-individual-hdr-trims-and-python-scripting-moves-to-studio/" }
---

## Neler yeni?

Blackmagic Design, 8 Eylül'de Amsterdam'daki IBC 2026 fuarında DaVinci Resolve 21.1'i duyurdu. Bültenin ana maddesi yapay zekâ asistanı desteği: "DaVinci Resolve 21.1 artık Claude, Claude Code ve ChatGPT Codex gibi yapay zekâ asistanlarıyla entegrasyonu destekliyor." Asistanlara şunları yaptırabiliyorsunuz: projeyi analiz etme, medyayı düzenleme, ayarları değiştirme, uzun çekimden özet (highlight) kurgu çıkarma, istenmeyen klipleri kaldırma ve teslim dosyalarını toplu render etme.

CineD'nin aktarımına göre bağlantı, Studio sürümüne gömülü bir MCP sunucusuyla kuruluyor; yani asistan sizin bilgisayarınızda çalışıp Resolve'un fonksiyonlarına erişiyor. Aynı kaynak, Python betik desteğinin ücretsiz sürümden çıkarılıp Studio'ya taşındığını yazıyor.

Diğer maddeler: 20 yeni betik API'si ve yerleşik konsol; Fusion'da 25'ten fazla yeni Krokodove aracı; fotoğraf sayfasında Fujifilm GFX ve X serisi, Leica SL ve Sony desteği; Dolby Vision, HDR10+ ve HDR Vivid için ayrı trim geçişleri. Toplamda 100'den fazla yeni araç ve kontrol.

Blackmagic CEO'su Grant Petty'nin sözleriyle müşteriler "özet kurgu çıkarma, medya düzenleme ya da toplu render gibi tekrar işlerini Claude ya da ChatGPT'ye bırakıp yaratıcı kararlara odaklanabiliyor."

## Kimin işine yarar?

- **Kurgucular:** Çekim günü dönüşü onlarca klibi konuya göre klasörleme, farklı formatlarda teslim dosyası üretme gibi işler tek cümleye iniyor.
- **İçerik üreticileri:** Uzun bir podcast ya da etkinlik kaydından özet kurgu taslağı çıkarmak için başlangıç noktası.
- **Prodüksiyon ekipleri:** Yeni betik API'leri ve konsol ile kendi otomasyonlarını yazanlar daha fazla fonksiyona erişiyor.

## Nasıl denenir?

Güncelleme [Blackmagic'in sitesinden](https://www.blackmagicdesign.com/products/davinciresolve) ücretsiz indiriliyor. Asistan bağlantısı için Studio sürümü gerekiyor; sonra Claude Code ya da ChatGPT Codex'te Resolve'u bir MCP sunucusu olarak tanıtıyorsunuz. İlk iş olarak "bu projedeki klipleri çekim tarihine göre klasörle" gibi geri alınabilir bir görev verin; render gibi uzun işlere geçmeden sonucu kontrol edin. Kurulum adımları bu sitedeki DaVinci kartında.

## Sınırlar

Ücretsiz Resolve'da asistan bağlantısı ve Python betikleri yok; Studio ücretli. Asistanın kurgu "zevki" yok, verdiği özet kurguyu taslak olarak görün.
