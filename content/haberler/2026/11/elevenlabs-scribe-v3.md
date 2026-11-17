---
baslik: "Röportaj dökümünde kim ne dedi, daha az hatayla: ElevenLabs Scribe v3"
tarih: 2026-11-10
kategori: ses
puan: 4
ozet: "ElevenLabs 10 Kasım'da iki yeni konuşmadan yazıya modeli duyurdu. Kayıtlı ses için Scribe v3, 102 dilde ölçülen testte Scribe v2'ye göre %27 daha az kelime hatası yapıyor ve konuşmacıları daha doğru ayırıyor. Canlı ses için Scribe v3 Live ilk kez gerçek zamanlı konuşmacı etiketi getiriyor. İkisi de ElevenLabs uygulamasında artık varsayılan model; API'de saati 0,20 $ ve 0,22 $."
neden_onemli: "Röportaj, panel ya da belgesel kurgusunun ilk adımı dökümdür: kim, ne zaman, ne dedi. Konuşmacıların karıştığı ya da isimlerin yanlış yazıldığı bir döküm, kurgu masasında saatlerce düzeltme demek. Scribe v3'ün iddiası tam bu iki noktada: üç ve daha fazla kişinin konuştuğu kayıtta konuşmacı ayırma hatası %17 daha az, özel isim ve terimler için de 1.000 kelimelik bir liste verebiliyorsunuz. Dökümü SRT olarak alabildiğiniz için altyazının ilk taslağı da aynı adımdan çıkıyor."
yekvisual_notu: "Denedim: 50 saniyelik Türkçe bir kaydı ElevenLabs uygulamasına (varsayılan model v3) ve karşılaştırma için bilgisayarımdaki Whisper'a verdim. v3 'Seedance 2.5', 'Kling 4.0', 'ElevenLabs' ve 'Kapalıçarşı'yı doğru yazdı, 'zekâ'nın şapkasını bile koydu; Whisper bunların yarısını bozdu. Tek hatası 'kendi sesimle' yerine 'kendi sesimde' oldu. Ücretsiz planda bu kayıt 689 kredi tuttu, yaklaşık yarım dakikada bitti."
ucretsiz: true
acik_kaynak: false
zorluk: yeni
sirket: ElevenLabs
model: Scribe v3, Scribe v3 Live
etiketler: [elevenlabs, scribe, konuşmadan yazıya, transkripsiyon, altyazı, röportaj, konuşmacı ayırma]
kapak: ./elevenlabs-scribe-v3/kapak.webp
kapak_kaynak: "Görsel: ElevenLabs"
denemeler:
  - { tip: gorsel, src: ./elevenlabs-scribe-v3/deneme-v3.webp, alt: "ElevenLabs uygulamasında 50 saniyelik Türkçe kaydın deşifresi. Özel isimler (Seedance 2.5, Kling 4.0, ElevenLabs, Kapalıçarşı) doğru; tek hata 'sesimle' yerine 'sesimde'.", kaynak: "YEK Lab denemesi" }
kaynaklar:
  - { ad: "ElevenLabs Blog: Scribe v3 ve v3 Live duyurusu", url: "https://elevenlabs.io/blog/scribe-v3" }
  - { ad: "ElevenLabs Belgeleri: Modeller", url: "https://elevenlabs.io/docs/overview/models" }
  - { ad: "ElevenLabs Belgeleri: Konuşmadan yazıya", url: "https://elevenlabs.io/docs/overview/capabilities/speech-to-text" }
  - { ad: "ElevenLabs: API fiyatları", url: "https://elevenlabs.io/pricing/api" }
  - { ad: "ElevenLabs: Planlar", url: "https://elevenlabs.io/pricing" }
---

## Neler yeni?

ElevenLabs 10 Kasım'da iki konuşmadan yazıya (transkripsiyon) modeli duyurdu: kayıtlı ses için **Scribe v3**, canlı ses için **Scribe v3 Live**. Duyuruya göre öne çıkanlar:

- **Daha az kelime hatası.** Scribe v3, 102 dilden oluşan FLEURS testinin şirket içi bir sürümünde Scribe v2'ye göre %27 daha az kelime hatası yapıyor ve test edilen her dilde iyileşiyor. Örnekler: Almancada %42, İspanyolcada %35, İngilizcede %23 daha az hata.
- **Konuşmacıları daha doğru ayırma.** "Kim ne dedi" etiketlemesinde (konuşmacı ayırma, İngilizcesiyle diarization) hata Scribe v2'ye göre genelde %12, üç ve daha fazla kişinin konuştuğu kayıtlarda %17 daha az. ElevenLabs bunu test ettiği modeller arasındaki en düşük hata olarak sunuyor.
- **Canlı seste konuşmacı etiketi.** Scribe v3 Live, gerçek zamanlı dökümde ilk kez konuşmacıları ayırıyor. ElevenLabs'in İngilizce gerçek kayıtlarla yaptığı testte hata oranı %3,1; karşılaştırılan öteki canlı modellerde %5,9 ile %7,3 arası. Anlam değiştiren hatalar Scribe v2 Realtime'a göre %43 daha az.
- **Çıktı üzerinde daha çok kontrol.** Kayıtta hangi dillerin geçtiğine dair ipucu verebiliyor, sayıların rakamla mı yazıyla mı yazılacağını seçebiliyorsunuz. Kayıtta geçeceğini bildiğiniz marka adı, kısaltma ve terimleri 1.000 kelimeye kadar bir listeyle modele önceden verebiliyorsunuz. "Bütün tarihleri GGGG-AA-GG biçiminde yaz" gibi düz cümleyle yazılmış biçim kuralları da dökümün üzerine uygulanabiliyor.
- **Cümle ortasında dil değişimi.** Scribe v3 Live'da konuşmanın ortasında dil değiştiren kayıtlar için çok dilli bir mod var.

Belgelere göre Scribe v3, v2'nin özelliklerini koruyor: kelime ya da harf düzeyinde zaman kodu, 32 konuşmacıya kadar ayırma, konuşma dışındaki ses olaylarını etiketleme, SRT, DOCX ve PDF olarak dışa aktarma. Ses dosyasının yanında MP4, MOV, MKV gibi video dosyaları da doğrudan yüklenebiliyor; tek dosyada sınır 5 GB ve 15 saat.

Duyurudaki bütün karşılaştırmalar ElevenLabs'in kendi ölçümü. Şirket, konuşmacı ayırma için 16 dilde gerçek toplantı, telefon görüşmesi ve sesli notlardan bir veri seti hazırladığını ve bunu yakında açık kaynak olarak paylaşacağını söylüyor. Rakip modellerin adını vermiyor.

## Kimin işine yarar?

- **Röportaj ve belgesel kurgucuları:** Uzun kayıtları kurgudan önce yazıya dökmek, kim ne dedi diye ayırmak ve kâğıt üzerinde kurgu (paper edit) yapmak için.
- **Altyazı hazırlayanlar:** Zaman kodlu dökümü SRT olarak alıp kurgu programına altyazı taslağı olarak yüklemek için.
- **Podcast ve panel kaydı yapanlar:** Üç ve daha fazla kişinin konuştuğu kayıtlarda, iyileşmenin en büyük olduğu alan konuşmacı ayırma.
- **Canlı yayın ve sesli asistan geliştirenler:** Scribe v3 Live'ın konuşmacı etiketi ve konuşmanın bitip bitmediğini yalnızca sessizliğe değil konuşmanın bağlamına da bakarak anlaması bu iş için.

## Nasıl denenir?

- **ElevenLabs uygulaması:** Duyuruya göre iki model de uygulamada artık varsayılan; uygulamanın konuşmadan yazıya (Speech to Text) aracı bunları kullanıyor.
- **API:** Model adları `scribe_v3` ve `scribe_v3_live`. Scribe v2 kullanan bir entegrasyonda yalnızca model adını değiştirmek yetiyor.
- **ElevenAgents:** Scribe v3 Live, ElevenLabs'in sesli asistan platformunda da kullanılabiliyor.

**Ücretsiz mi?** Sınırlı olarak evet. ElevenLabs'in ücretsiz planı ayda 10.000 kredi veriyor ve konuşmadan yazıya bu planda da var. Fiyat sayfasına göre döküm dakikası yaklaşık 330 kredi; yani ücretsiz planla ayda kabaca yarım saatlik kayıt yazıya dökülebiliyor. API'de Scribe v3'ün saati 0,20 $, Scribe v3 Live'ınki 0,22 $. Terim listesi ve düz cümleyle biçim kuralı (transcript editing) ayrıca ücretli: Scribe v3'te saat başına sırasıyla 0,05 $ ve 0,07 $. Kayıttaki sessiz bölümler de ücrete dahil.

**Dil desteği.** Ölçüm 102 dilde yapıldı; belgelerde desteklenen dil sayısı "90'dan fazla" olarak geçiyor. Türkçe bu listede var. ElevenLabs, v3 için Türkçeye özel bir hata oranı paylaşmadı.

## Sınırlar

- **Ölçümler şirketin.** Bütün oranlar ElevenLabs'in kendi testleri; bağımsız bir karşılaştırma henüz yok. FLEURS da kısa ve temiz okunmuş cümlelerden oluşuyor, gürültülü saha kaydını yansıtmıyor.
- **Canlı modelin sonuçları ayrı.** ElevenLabs, canlı konuşmacı ayırma sonuçlarının farklı yöntemle ölçüldüğünü ve kayıtlı ses sonuçlarıyla karşılaştırılamayacağını kendisi belirtiyor.
- **Ek özellikler ek ücretli.** Terim listesi ve biçim kuralları saat ücretinin üstüne ekleniyor.
- **Veri nerede işleniyor?** Modeller varsayılan olarak ABD'de çalışıyor. Avrupa Birliği, Hindistan ve Singapur'da ayrı ortamlar veri konumu şartı olan kurumsal müşterilere sunuluyor. Ses ve metni işlem biter bitmez silen bir mod da (Zero Retention Mode) var. Kurum arşivi gibi hassas kayıtlarda bunları baştan kontrol etmek gerekiyor.

## Denedim: aynı kayıt, üç model

Özel isimler, sayılar ve ş, ğ, ı harfleriyle dolu, yaklaşık 50 saniyelik bir metni kendi sesimle okudum ve aynı kaydı üç yere verdim: ElevenLabs uygulamasına (duyuruya göre varsayılan model artık Scribe v3), ElevenLabs'in eski deşifre modeline (Scribe v1) ve bilgisayarımda çalışan açık kaynak Whisper'a (large-v3-turbo).

| Kelime | Scribe v3 (uygulama) | Scribe v1 | Whisper |
|---|---|---|---|
| ElevenLabs | ElevenLabs | ElevenLabs | Levenlap |
| Seedance 2.5 | Seedance 2.5 | CDense 2.5 | Seedance 2.5 |
| Kling 4.0 | Kling 4.0 | Clinq 4.0 | Clink 4.0 |
| Kapalıçarşı | Kapalıçarşı | Kapalıçarşı | Kapalı çarşı |
| tebeşir | tebeşir | tebeşir | tebeşhir |
| sürüme | sürüme | sürüme | sürme |
| kendi sesimle | kendi **sesimde** | kendi sesimle | kendi sesimle |

- **Özel isimler.** Asıl fark burada: v3 bütün marka ve model adlarını doğru yazdı. v1 "CDense", "Clinq" yazdı; Whisper ise şirketin kendi adını bile "Levenlap" yaptı.
- **Türkçe yazım.** v3 "yapay zekâ"yı şapkalı yazdı, soru cümlesinden sonra iki nokta koydu, "ş, ğ, ı" harflerini tek tek doğru dizdi.
- **Hata.** v3'ün tek hatası "kendi sesimle" yerine "kendi sesimde" oldu; bu kelimeyi diğer iki model doğru duydu. Yani v3 kusursuz değil, son okuma yine gerekiyor.
- **Süre ve maliyet.** v3 kaydı uygulamada yaklaşık yarım dakikada çıkardı; ücretsiz plandaki 10.000 kredinin 689'unu harcadı. Whisper aynı kaydı bilgisayarda 15 saniyede, ücretsiz çıkardı ama özel isimlerde zayıf.

Uygulama hangi modelin kullanıldığını ekranda göstermiyor; v3 olduğunu ElevenLabs'in "uygulamada varsayılan" açıklamasına dayanarak söylüyorum.
