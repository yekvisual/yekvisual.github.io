---
baslik: "DaVinci ve Claude ile kurguyu otomatize etmek"
ozet: "\"Sessiz yerleri kes, altyazı ekle, 9:16 dışa aktar\" komutunu verin, angarya işleri sisteme devredin."
ikon: 🎞️
sira: 2
zorluk: orta
kategori: video
araclar: [davinci-resolve, claude-code]
etiketler: [davinci resolve, claude, kurgu, renk, mcp]
gorsel: ./medya/ai-ile-video-edit.webp
---

## Ne bu?

DaVinci Resolve'un bir **programlama arayüzü** var: zaman çizelgesine klip ekleme, kesme, renk düğümü oluşturma, LUT uygulama, render alma gibi her şey komutla yapılabiliyor. Claude bu arayüze bir bağlayıcı (MCP) üzerinden erişince, "bu klibin sessiz yerlerini kes", "tüm kliplere şu LUT'u uygula ve 9:16 olarak dışa aktar" gibi isteklerinizi doğrudan uyguluyor.

## Ne işe yarar?

- 40 videoyu aynı ayarla, aynı logoyla, aynı formatta dışa aktarmak.
- Uzun bir kaydı konuşmanın durduğu yerlerden bölüp Reels parçaları çıkarmak.
- "Daha sıcak, biraz daha kontrastlı" gibi tariflerle renk düzeltmesi yapmak ve bunu bir LUT olarak kaydetmek.
- Resolve'un yeni sürümlerinde ne değiştiğini Claude'a sorup öğrenmek.

## İlk adım

1. DaVinci Resolve (ücretsiz sürüm yeterli) ve Claude Code kurulu olsun.
2. Claude Code'a Resolve bağlayıcısını ekleyin; ilk komutta Claude sizi yönlendirir.
3. Açık bir projede deneyin: *"Zaman çizelgesindeki klipleri listele ve toplam süreyi söyle."* Çalışıyorsa gerisi hayal gücünüze kalmış.
