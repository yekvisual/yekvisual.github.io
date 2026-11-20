---
baslik: "Genie 4, mekân keşfini değiştirebilir: tek fotoğraftan içinde gezilen set"
tarih: 2026-10-27
yayin: 2026-10-28
kategori: video
puan: 5
ozet: "Google DeepMind'ın yeni dünya modeli Genie 4, tek bir fotoğraftan içinde gerçek zamanlı gezilebilen bir sahne kuruyor; hava, kamera ve sahneye eklenenler metinle değiştiriliyor. Set ekipleri için anlamı: mekâncının çektiği bir kareden yönetmen ve görüntü yönetmeni mekânın içinde dolaşıp açı arayabilir. Şimdilik seçili test kullanıcılarına açık."
neden_onemli: "Mekân seçimi ve ekibi mekâna tekrar götürmek bir yapımın en çok zaman ve para yiyen adımlarından. Bir fotoğraftan gezilebilen bir sahne, birkaç aday mekân arasında karar vermeyi ve kadraj üzerine konuşmayı mekâna gitmeden başlatabilir; final kararın yerini tutmaz ama turu kısaltabilir."
yekvisual_notu: "Henüz erişimim yok; bekleme listesine yazıldım. Erişim gelince ilk deneyeceğim şey bir mekân fotoğrafından kamerayı gezdirip kadraj aramak, sonra aynı mekâna dönüldüğünde sahnenin aynı kalıp kalmadığına bakmak. DeepMind kendisi uzun oturumda nesne tutarlılığının kaydığını söylüyor; mekân keşfinde işe yarayıp yaramayacağını bu belirleyecek."
ucretsiz: null
acik_kaynak: false
zorluk: orta
sirket: Google DeepMind
model: Genie 4
etiketler: [genie, deepmind, dünya modeli, mekân keşfi, previz, set, görüntü yönetmeni, google]
kapak: ./genie-4/kapak.webp
kapak_kaynak: "Görsel: Google DeepMind, Genie 4 tanıtım videosu"
medya:
  - { tip: video, src: "./genie-4/genie3-genie4-karsilastirma.mp4", alt: "Genie 3 ile Genie 4 aynı istemle yan yana", kaynak: "Google DeepMind" }
kaynaklar:
  - { ad: "Google: Genie 4 kullanıma açıldı (18 Kasım)", url: "https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/" }
  - { ad: "Google: Genie 4 Gemini API'de (19 Kasım)", url: "https://blog.google/innovation-and-ai/technology/developers-tools/genie-4-in-gemini-api/" }
  - { ad: "Google DeepMind duyurusu", url: "https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/" }
---

> **Güncelleme, 20 Kasım:** Genie 4, 18 Kasım'da Project Genie içinde Google AI Ultra abonelerine açılmaya başladı; Google AI Pro aboneleri için bekleme listesi var. 19 Kasım'dan beri Gemini API'de geliştiricilere de açık. Ayrıntılar aşağıda "Nasıl denenir?" bölümünde.

## Neler yeni?

Google DeepMind, 27 Ekim'de Genie 4'ü duyurdu. Genie bir "dünya modeli": bir sahneyi üretmekle kalmıyor, içinde gerçek zamanlı hareket etmenize ve sahneyi konuşarak değiştirmenize izin veriyor. Duyuruya göre:

- **Tek fotoğraftan sahne.** DeepMind'ın ifadesiyle tek bir iki boyutlu arşiv fotoğrafı, temellendirilmiş bir simülasyona dönüşebiliyor.
- **Klavyeyle gezinme.** Kamera standart klavye kontrolleriyle hareket ettiriliyor; test kullanıcıları kamera açısı ayarlamayı denemiş.
- **Metinle anlık değişiklik.** Hava durumunu değiştirmek, kamerayı taşımak, sahneye yeni bir insan ya da nesne eklemek bir cümleyle yapılıyor.
- **Daha gerçekçi fizik ve hareket.** Aerodinamik, çarpışma ve insan hareketi önceki sürüme göre daha doğal; aşağıdaki videoda Genie 3 ile farkı görebilirsiniz.
- **Yerleşik ses ve bir ajan.** Ortam sesi ve olaylara göre değişen diyalog; içeride Gemini 3.8 Flash tabanlı bir ajan sahneyi izleyip hedefleri adımlara bölüyor.

Üretilen her video ve ses SynthID filigranı taşıyor.

## Set gözüyle: mekân keşfi

Bir yapımda mekân süreci kabaca şöyle işler: mekâncı aday mekânları gezip fotoğraflar, yönetmen ve ekip bu fotoğraflardan seçim yapar, sonra yönetmen, yardımcı yönetmen, görüntü yönetmeni ve sanat yönetmeni seçilen mekâna bir kez daha gider ve açıları, ışığı, dekoru orada konuşur. En çok zaman ve para da bu iki adımda harcanır: birkaç aday arasında karar vermek ve kalabalık bir ekibi mekâna tekrar götürmek.

Genie 4 bu zinciri bugünkü haliyle bile kısaltabilecek bir yerde duruyor:

- **Mekâncı** her aday mekân için en iyi karesini paylaşır; her kare gezilebilen bir sahneye dönüşür.
- **Yönetmen ve yardımcısı** adaylar arasında, ekip daha yola çıkmadan, mekânın içinde dolaşarak karar verebilir; "kamera buradan girerse oyuncu nereden çıkar" sorusu masada konuşulur.
- **Görüntü yönetmeni** kabaca açı ve kamera yolu arayabilir.
- **Sanat yönetmeni** için en ilginç kısım nesneler. Genie 4 sahneye yeni bir nesne eklemeye izin veriyor; böylece "buraya bir masa, köşeye bir lamba girse" denemesi bugün yapılabiliyor. Mekânda var olan bir nesneyi yerinden oynatmak ya da kaldırmak ise duyuruda yok. Bu da gelirse dekor yerleşimi, mekâna gitmeden planlanabilir hale gelir.

## Bugün nerede duruyor?

Mekân keşfi için dürüst sınırlar da var:

- **Tek kare.** Bugün sahne tek bir fotoğraftan kuruluyor. Fotoğrafın görmediği arka taraf, oda içi ya da köşe dönüşü modelin tahmini; gerçek mekânla aynı olmayabilir.
- **Lens yok.** Kamera gezdirilebiliyor ama duyuruda lens, odak uzaklığı ya da kadraj ölçüsü kontrolü yok. Görüntü yönetmeni için şimdilik "bu köşeden bakınca nasıl duruyor" düzeyinde bir fikir verir, lens seçimi değil.
- **Tutarlılık.** DeepMind'a göre görsel ayrıntılar ve nesne kalıcılığı, oturum uzadıkça ya da art arda düzenlemelerde kayabiliyor. Bir mekâna "geri dönüldüğünde" aynı kalıp kalmadığı bu yüzden belirsiz.
- **Diğerleri.** Karmaşık fiziksel etkileşimler, ses doğruluğu, okunur yazı ve mekânsal doğruluk hâlâ araştırma konusu.

Yani Genie 4 bugün mekân keşfinin yerini almaz; ama hangi mekâna gidileceğine ve orada neye bakılacağına mekâna gitmeden karar vermeyi kolaylaştırabilir. DeepMind de test kullanıcılarının modeli ön görselleştirme için hızlı bir "taslak modu" olarak kullandığını söylüyor.

## Nasıl denenir?

- **Project Genie (labs.google/projectgenie):** 18 Kasım'dan beri uygun Google AI Ultra abonelerine kademeli olarak açılıyor. Google AI Pro aboneleri aynı sayfadan bekleme listesine yazılabiliyor. Google hangi ülkelerde açık olduğunu yazmadı; Türkiye'den erişimi henüz denemedik.
- **Gemini API ve Google AI Studio:** 19 Kasım'dan beri geliştiricilere açık. Çıktı 720p, 24 kare/saniye ve sesli. Fiyat milyon token başına girişte 1,50 $, video çıktısında 17,50 $; ücretsiz katmanda yok.
- Project Genie'de bir de ajan var: anlatmak istediğiniz hikâyeyi ya da simülasyonu tarif ediyorsunuz, ajan fikri sizinle birlikte geliştirip görüntü ve ses üretiyor. Topluluğun kurduğu dünyaları açıp ortamını, karakterlerini ve sesini değiştirebiliyorsunuz.
- Üretilen içeriğe Google'ın SynthID filigranı ekleniyor.
