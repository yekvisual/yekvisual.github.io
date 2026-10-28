---
baslik: "Gemini video Omni Flash'a geçti: konuşarak düzeltme, Veo 3.1 Preview kapandı"
tarih: 2026-10-22
kategori: video
puan: 4
ozet: "Google, Gemini API'deki Veo 3.1 Preview uç noktalarını 22 Ekim'de kapattı ve yerine Gemini Omni Flash'ı gösterdi. Omni Flash tek seferlik üretim yerine çok turlu düzenleme sunuyor: üretilen videoyu 'arka planı değiştir', 'açıyı yükselt' gibi isteklerle baştan üretmeden düzeltiyorsunuz. Gemini uygulamasındaki video üretimi de bu modelle çalışıyor."
neden_onemli: "Yapay zekâ videosunda en büyük zaman kaybı, küçük bir ayrıntı için tüm klibi yeniden üretmek. Üretilen klibi sohbetle düzeltebilmek, deneme sayısını ve maliyeti düşürüyor. API tarafında Veo 3.1 Preview kullanan geliştiricilerin ise entegrasyonu taşıması gerekiyor."
yekvisual_notu: "Omni Flash'ı henüz denemedim. Asıl merak ettiğim, 'sadece ışığı değiştir' dediğimde karakterin yüzünün yerinde kalıp kalmadığı; bunu Gemini uygulamasında deneyip paylaşacağım. Türkçe konuşma üretip üretmediğini de doğrulamadım."
ucretsiz: false
acik_kaynak: false
zorluk: yeni
sirket: Google
model: Gemini Omni Flash
etiketler: [gemini, omni flash, veo, video üretim, video düzenleme, google]
kapak: ./gemini-omni-flash/kapak.webp
kapak_kaynak: "Görsel: Google"
kaynaklar:
  - { ad: "Gemini API: Video üretimi belgeleri", url: "https://ai.google.dev/gemini-api/docs/video" }
  - { ad: "Gemini uygulaması: Video üretimi", url: "https://gemini.google/overview/video-generation/" }
  - { ad: "VentureBeat", url: "https://venturebeat.com/technology/googles-gemini-omni-flash-hits-the-api-turning-enterprise-video-production-into-a-conversation" }
---

## Neler yeni?

Google'ın API belgelerine göre `veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview` ve `veo-3.1-lite-generate-preview` modelleri 22 Ekim 2026'da kapatıldı. Önerilen geçiş yolu iki tane: Gemini Omni Flash (`gemini-omni-1.1-flash`) ya da Gemini Enterprise Agent Platform üzerindeki kararlı Veo 3.1 modelleri. Yani Veo bitmedi; ama Gemini API'nin ve Gemini uygulamasının varsayılan video modeli artık Omni Flash.

Omni Flash'ı farklı kılan şey çok turlu düzenleme: Google'ın belgeleri "öğe değiştirme ya da bakış açısı değişikliği" gibi işleri Interactions API ile tur tur yaptırabildiğinizi yazıyor. Model metin, görsel, ses ve video girdilerini birlikte alıyor. Ağustos sonunda kararlı sürüme geçerken video uzatma, ilk ve son kareden ara doldurma ve 360p'den 4K'ya çözünürlük seçimi eklenmişti. VentureBeat'in aktardığı fiyat: 720p'de saniye başına 0,10 $, yani 10 saniyelik klip yaklaşık 1 $.

Gemini uygulamasının Türkçe sayfasında da model "Gemini Omni 1.1 Flash" olarak geçiyor: 10 saniyelik video, doğal ses, 5 fotoğrafa kadar fotoğraftan video ve "düzeltmesini istediğiniz noktaları söylemeniz yeterli" ifadesi. Google AI aboneliği gerekiyor.

## Kimin işine yarar?

- **İçerik üreticileri:** Gemini uygulamasında ürettiğiniz 10 saniyelik klibi tek cümleyle düzeltmek, Reels taslakları için pratik.
- **Pazarlama ekipleri:** Ürün çekimini yeniden ışıklandırmak, kadrajı değiştirmek, kostümü değiştirmek gibi işler baştan üretim gerektirmiyor.
- **Geliştiriciler:** Veo 3.1 Preview'a bağlı kodunuz varsa artık çalışmıyor; Omni Flash'a ya da kurumsal Veo uç noktalarına geçmeniz gerekiyor.

## Nasıl denenir?

Gemini uygulamasında (abonelik gerekiyor) video üretimini seçip bir fotoğraf yükleyin, 10 saniyelik bir sahne isteyin, sonra "aynı sahne, akşam ışığı" diye düzeltin. API tarafında [AI Studio](https://aistudio.google.com)'da `gemini-omni-1.1-flash` modelini seçiyorsunuz. Üretilen klipleri kurguya almak için bu sitedeki DaVinci kartına bakın.

## Sınırlar

Omni Flash'ın önceki sürümü yalnızca 720p üretiyordu; Ağustos'taki 4K seçeneğinin uygulama tarafında olup olmadığı belgelerde net değil. Ses girdisi kabul edip etmediğini de doğrulamadım.
