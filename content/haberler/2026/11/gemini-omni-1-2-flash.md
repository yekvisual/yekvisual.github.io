---
baslik: "15 saniyelik video Google Vids'te ücretsiz: Gemini Omni 1.2 Flash'ı denedik"
tarih: 2026-11-09
kategori: video
puan: 4
ozet: "Google, 5 Kasım'da video modeli Gemini Omni 1.2 Flash'ı çıkardı: klip artık 3 ile 15 saniye arası, ses videoyla birlikte üretiliyor ve klibi sohbetle düzeltebiliyorsunuz. Google'a göre Google hesabı olan herkes Vids'te ayda 3 adet 15 saniyelik video üretebiliyor. Vids'te beş prompt denedik; hepsini aşağıda birebir paylaşıyoruz."
neden_onemli: "15 saniye, bir Reels'e ya da bir dersin açılışına yetecek uzunluk. Vids'teki ücretsiz kota, aboneliği olmayanların da modeli denemesine imkân veriyor. Denemelerimizde en iyi sonucu kesmesiz planlar ve anlatım animasyonları verdi; bu da eğitim içeriği hazırlayanlar için doğrudan kullanılabilir bir araç demek."
yekvisual_notu: "Galata'dan Boğaz'a kesmesiz drone uçuşu beklediğimden iyi çıktı; tek cümleyle geceye çevirdiğimde kamera yolu neredeyse aynı kaldı. Fotosentez anlatımında seslendirme kelimesi kelimesine doğruydu, ama istemediğim bir alt yazı ekledi ve onu bozdu. Denemeleri ücretli bir hesapla yaptım; ücretsiz kotayı kendim ölçmedim."
ucretsiz: true
acik_kaynak: false
zorluk: yeni
sirket: Google
model: Gemini Omni 1.2 Flash
etiketler: [gemini, omni, google vids, video üretim, sesli video, google]
kapak: ./gemini-omni-1-2-flash/kapak.webp
kapak_kaynak: "Görsel: YEK Lab denemesi (Gemini Omni 1.2 Flash ile üretildi)"
medya:
  - { tip: video, src: ./gemini-omni-1-2-flash/galata-fpv.mp4, alt: "Galata Kulesi'nden Boğaz'a kesmesiz FPV drone uçuşu. 15 sn, 1080p, sesli (sesi açın). Hiç kesme yok; vapur, martılar ve Boğaz Köprüsü yerinde. Son 5 saniyede kamera neredeyse sabit kalıyor.", kaynak: "YEK Lab denemesi" }
  - { tip: video, src: ./gemini-omni-1-2-flash/galata-gece-yagmur.mp4, alt: "Aynı klip, tek cümlelik düzenlemeyle gece ve yağmur. Kamera yolu neredeyse birebir korundu; yağmur hafif. Klip 15 saniyeden 10 saniyeye kısaldı.", kaynak: "YEK Lab denemesi" }
denemeler:
  - { tip: video, src: ./gemini-omni-1-2-flash/fotosentez.mp4, alt: "Fotosentez anlatımı. 15 sn, 1080×1920, sesli (sesi açın). Seslendirme ve etiketler doğru; alttaki alt yazıyı biz istemedik ve içindeki “karbondioksitle” bozuk.", kaynak: "YEK Lab denemesi" }
  - { tip: video, src: ./gemini-omni-1-2-flash/ogretmen.mp4, alt: "Kameraya konuşan öğretmen. 10 sn, 720p üretildi, dışa aktarımda 1080p (sesi açın). Konuşma doğru, yüz gerçekçi, el hareketleri doğal.", kaynak: "YEK Lab denemesi" }
  - { tip: video, src: ./gemini-omni-1-2-flash/tebesir.mp4, alt: "Tebeşirle “Öğretmenler Günü Kutlu Olsun”. 15 sn, 1080p. El ve tebeşir gerçekçi; ama ilk karede “menler” zaten yazılı ve son kelime “Ols” + kalp oldu.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./gemini-omni-1-2-flash/vids-omni-panel.webp, alt: "Google Vids'te “Yapay zeka video klibi” paneli: Oluştur, Düzenle ve Animasyon ekle sekmeleri; altta model, çözünürlük, en-boy ve süre ayarı.", kaynak: "YEK Lab ekran görüntüsü" }
kaynaklar:
  - { ad: "Google: Gemini Omni 1.2 Flash duyurusu", url: "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/" }
  - { ad: "Google: Omni 1.2 Flash Google Vids'te", url: "https://blog.google/products-and-platforms/products/workspace/omni-1-2-flash-google-vids/" }
  - { ad: "Google Workspace Updates", url: "https://workspaceupdates.googleblog.com/2026/11/gemini-omni-12-flash-now-in-vids-with-15second-generations-and-improved-quality.html" }
  - { ad: "Google Cloud: Gemini Omni 1.2 Flash genel kullanımda", url: "https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available" }
  - { ad: "AI Studio: Omni belgeleri", url: "https://aistudio.google.com/docs/omni" }
  - { ad: "Segmind: Gemini Omni 1.2 Flash incelemesi", url: "https://blog.segmind.com/gemini-omni-1-2-flash-review/" }
---

## Neler yeni?

Google, 5 Kasım'da [Ekim'de yazdığımız Omni Flash'ın](/gundem/2026/10/gemini-omni-flash/) yeni sürümünü, Gemini Omni 1.2 Flash'ı yayınladı. Değişenler:

- **Süre.** Klip 3 ile 15 saniye arasında, saniye saniye seçiliyor. 1.1'de üst sınır 10 saniyeydi. Videonun sonuna ekleme yaparak toplamı 30 saniyeye çıkarabiliyorsunuz.
- **Ses.** Ses videoyla birlikte üretiliyor. Google'a göre konuşmalar daha doğal, dudak senkronu daha iyi ve birden fazla konuşmacı ayrı seslerle konuşabiliyor. Ses dosyası referans olarak verilemiyor; var olan bir videonun sesi de düzenlenemiyor.
- **Sohbetle düzenleme.** Klibi baştan üretmeden ürünü, arka planı, ışığı, havayı ya da en-boy oranını tek tek değiştirebiliyorsunuz.
- **Tutarlılık.** Google'a göre kamera hareket ettiğinde yüzler, kıyafetler, ambalaj yazıları ve marka renkleri daha az bozuluyor; istenmeyen ani kesmeler azaldı.
- **Girdiler.** Yalnız metin, tek görsel, ilk ve son kare olarak iki görsel, en çok 6 referans görseli (2 karakter, karakter başına 3), hareket referansı olarak 3 saniyeye kadar video ya da düzenlemek için 15 saniyeye kadar video.
- **Biçim.** 16:9 ya da 9:16; kare format yok. Model 360p ya da 720p üretiyor, sonra 1080p ya da 4K'ya büyütülebiliyor. Vids'te 720p ve 1080p seçenekleri var.
- **Fiyat.** API'de 720p için saniyesi 0,07 $; 15 saniyelik klip yaklaşık 1,05 $. Bu, 1.1'e göre %30 daha ucuz.
- **Damga.** Tüm çıktılarda gözle görünmeyen SynthID damgası var. Vids'ten indirdiğimiz videolarda sağ altta küçük bir Gemini yıldızı da görünüyor.

**Nerede var?** Google'ın açıklamasına göre Google hesabı olan herkes Vids'te ayda 3 adet 15 saniyelik video üretebiliyor. Gemini uygulamasında yalnız AI Ultra abonelerine açılıyor. Flow, Gemini API, AI Studio, Vertex ve Google Ads'de de var. API'de model kimliği `gemini-omni-1.2-flash`; 1.1, 3 Aralık'ta otomatik olarak 1.2'ye yönlendirilecek.

## Vids'te nasıl denenir?

1. [vids.new](https://vids.new) adresinden yeni bir video açın; açılış penceresinde Yatay ya da Dikey seçin.
2. "Yapay zeka ile video (Omni)" kartına tıklayın. Sağda "Yapay zeka video klibi" paneli açılıyor: Oluştur, Düzenle ve Animasyon ekle sekmeleri.
3. Altta ayarlar var: çözünürlük 720p ya da 1080p, en-boy Manzara ya da Dikey, süre kaydırıcıyla 3–15 saniye. Varsayılan 10 saniye; sayfa yenilenince ayarlar 720p ve 10 saniyeye geri dönüyor.
4. Promptu yazıp gönderin. Bizde her klip 1,5–2 dakikada hazır oldu.
5. Klibin altında Ekle, Uzat, Düzenle, Yükselt (yalnız 720p klipte) ve Yeniden oluştur düğmeleri var. **Klibi zaman çizelgesine ekleyin;** eklenmeyen klipler sekme kapanınca siliniyor.
6. Dosya > İndir menüsünden MP4 ya da GIF alın. İndirilen dosya tüm zaman çizelgesini içeriyor; tek bir klibi ayrı indirme seçeneği yok.

Denemeleri ücretli bir Google planı olan hesapla yaptık; beş üretim sorunsuz geçti, uyarı çıkmadı. Ücretsiz bir hesapta kotanın nasıl göründüğünü ölçmedik.

## Denediğimiz 5 prompt

**1. Galata'dan Boğaz'a kesmesiz drone uçuşu** (15 sn, 1080p)

```text
FPV drone flight in a single unbroken continuous shot, no scene cuts, vertical 9:16. Starts at the top of Galata Tower in Istanbul at golden hour, dives down over the rooftops of Karaköy, skims low across the Bosphorus water past a white ferry with seagulls flying alongside, and rises toward the Bosphorus Bridge. Ambient wind, seagull calls and a distant ferry horn. No music, no dialogue, no subtitles, no text.
```

En iyi sonuç. Hiç kesme yok; sahne analiziyle de kontrol ettik. Galata, Karaköy çatıları, Türk bayraklı bir şehir hatları vapuru, martılar ve Boğaz Köprüsü var. Son 5 saniyede kamera neredeyse sabit kalıyor. Seste rüzgâr ve martı var.

**2. Aynı klibi geceye çevirmek** (düzenleme, 10 sn)

```text
Make it night with heavy rain and city lights reflecting on the water. Keep everything else the same.
```

Kamera yolu ilk klibe neredeyse birebir uydu, sahne gece ve yağmurlu oldu. Yağmur istediğimizden hafif. Klip 15 saniyeden 10 saniyeye kısaldı.

**3. Fotosentez anlatımı** (15 sn, 1080×1920)

```text
Clean flat 2D educational motion-graphics explainer, vertical 9:16. In a single continuous shot, no scene cuts. A green leaf in the center; the sun appears top left and yellow arrows labelled "Işık" flow into the leaf; blue arrows labelled "Su" rise from the roots; grey arrows labelled "Karbondioksit" enter from the air; then the leaf releases bubbles labelled "Oksijen" and a glowing label "Glikoz" appears inside the leaf. A warm female Turkish narrator says: "Bitkiler ışık, su ve karbondioksitle kendi besinlerini üretir. Buna fotosentez denir." Calm background music. All text spelled exactly as given, no other text.
```

Seslendirme istediğimiz cümleyi kelimesi kelimesine söyledi; Işık, Su, Karbondioksit, Oksijen ve Glikoz etiketleri doğru. Ama promptta alt yazıyı yasaklamadığımız için kendiliğinden bir alt yazı ekledi ve orada "karbondioksitle" bozuldu ("su ve öncim ker kendi besinlerini…").

**4. Kameraya konuşan öğretmen** (10 sn, 720p)

```text
A friendly female teacher in her thirties stands in a bright, sunlit Turkish classroom with a whiteboard behind her. Vertical 9:16, single continuous shot, no scene cuts, medium close-up with a slow push-in. She looks into the camera, smiles and says in natural Turkish: "Merhaba arkadaşlar! Bugün yapay zekâyla on beş saniyelik bir video yapmayı öğreneceğiz." Clear lip-sync, soft room tone. No music, no subtitles, no captions, no on-screen text.
```

Konuşma doğru, yüz gerçekçi, kamera yavaşça yaklaşıyor, el hareketleri doğal. Bağımsız testler gerçekçi insanı zayıf alan sayıyordu; bu denemede iyi çıktı.

**5. Tebeşirle kelime kelime yazı** (15 sn, 1080p)

```text
A dark green school chalkboard filling the frame, vertical 9:16, single continuous shot, no scene cuts, static camera. White chalk handwriting appears word by word, one word at a time, in sync with soft chalk scratching sounds: "Öğretmenler", then "Günü", then "Kutlu", then "Olsun". At the end a small chalk heart is drawn under the text. No music, no dialogue, no subtitles, no captions. All text spelled exactly as given, no other text.
```

El ve tebeşir gerçekçi; ö, ğ ve ü doğru. Ama ilk karede "menler" zaten yazılı, son kelime "Ols" ve bir kalp oldu: "un" yerine kalbi çizdi. Tahtada silik yazı izleri de var. Orta karar.

## Prompt ipuçları

Google'ın resmi rehberinden ve kendi denemelerimizden:

- **Sahneyi tarif edin.** Kamera hareketini, ışığı ve havayı yazın. "Hareket etsin" gibi belirsiz istekler zayıf sonuç veriyor.
- **Tek plan istiyorsanız söyleyin.** "In a single continuous shot. No scene cuts." yazmazsanız model kendiliğinden kesme yapıyor. Bu kalıpla üç klipte de kesme olmadı.
- **Alt yazıyı yasaklayın.** Konuşmalı videolarda "No subtitles, no captions" yazmazsanız kendiliğinden alt yazı ekleyebiliyor, Türkçe alt yazı da bozuk çıkıyor.
- **Düzenlemeyi kısa tutun.** Tek bir değişiklik isteyin ve sonuna "Keep everything else the same." ekleyin. Uzun açıklamalar istenmeyen değişikliklere yol açıyor; bu kalıpla kamera hareketi korundu.
- **İstemediğinizi cümle içinde söyleyin.** Negatif prompt alanı yok: "No dialogue", "No extra sound effects".
- **Sesi tarif edin.** Örneğin "Include calm background music".
- **Zamanlamayı yazın.** "After 3 seconds, ..." ya da `[0-5s] ... [5-10s] ... [10-15s] ...`.
- **Ekrandaki yazıyı tırnak içinde verin.** Sonuna "All text spelled exactly as given, no other text" ekleyin (bağımsız test eden Segmind'in önerisi).
- **Kelime kelime yazıda kısa metin verin.** Son kelimede hata yapabiliyor; son kelimeden sonra 2–3 saniye boşluk bırakın.

## Sınırlar

- **İstenmeyen alt yazı.** Fotosentez klibinde istemediğimiz alt yazıyı ekledi ve içindeki Türkçe bozuk çıktı.
- **Son kelime hatası.** Tebeşir klibinde "Olsun" yerine "Ols" ve kalp çıktı.
- **Düzenleme süreyi kısaltabiliyor.** Gece düzenlemesinde 15 saniyelik klip 10 saniyeye indi.
- **Ses.** Ses dosyasını referans veremiyorsunuz, var olan videonun sesini düzenleyemiyorsunuz.
- **Google'ın kabul ettiği zayıflıklar.** Hızlı spor hareketleri, karmaşık fizik ve senaryonun hızla değiştiği sahneler.
- **Ücretsiz kota.** Ücretsizlik bilgisi Google'ın blog duyurusuna dayanıyor; Workspace güncellemeler sayfası ise kişisel hesaplar için yalnız AI Pro ve Ultra'yı sayıyor. Denemelerimizi ücretli bir hesapla yaptığımız için ücretsiz kotayı doğrulamadık.
