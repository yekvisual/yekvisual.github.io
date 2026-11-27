---
baslik: "MAGI-2 ile çektiğiniz videoyu düzenlemek: 7 istem ve denenecek yerler"
ozet: "Kendi çekiminizde mekânı, havayı, kıyafeti, ışığı değiştirin; yüz, dudak ve hareket aynı kalsın. Reels'te kullandığımız 7 istemin tam metni, ayarlar, ücretsiz denenecek yerler ve PDF."
ikon: 🪄
sira: 11
zorluk: yeni
kategori: video
araclar: [seedance]
etiketler: [magi-2, sand.ai, higgsfield, vidmuse, seedance, videodan videoya, video düzenleme, istem, prompt, ücretsiz]
gorsel: ./medya/magi-2-video-duzenleme.webp
---

## Ne bu?

MAGI-2, Sand.ai'nin video modeli. Bu sayfada onu **videodan videoya** kullandık: parkta masada konuşurken çektiğimiz tek bir çekimi 4–9 saniyelik kliplere bölüp her birinde arka planı, havayı, kıyafeti, ışığı ya da elimizdeki nesneyi değiştirdik. Yüz, gözlük, el hareketleri ve dudaklar aynı kaldı, yani kendi sesiniz videoya oturmaya devam ediyor.

Aynı klipleri Seedance 2.5 ile de dönüştürdük. [Reels'te](https://www.instagram.com/reel/DgP5BP6TDfc/) ikisi alt alta duruyor; düzenlemelerin hepsi MAGI-2'de **₺83**, Seedance 2.5'te **₺837** tuttu. Yaklaşık onda biri.

**PDF olarak indirin:** [MAGI-2 istemleri ve rehber (PDF)](/indir/magi-2-video-duzenleme.pdf)

## Nerede denenir? Ücretsiz olan var mı?

| Nerede | Ücretsiz mi? | Not |
|---|---|---|
| [Higgsfield](https://higgsfield.ai/ai/video?model=magi_2) | Lansmanda "ücretsiz deneyin" duyuruldu; hesabınızda **free generations** anahtarı görünüyorsa birkaç üretim ücretsiz. Görünmüyorsa ücretli | MAGI-2'yi web'de sunan ana yer; bu sayfadaki her şeyi burada yaptık. Higgsfield'in 25 Kasım tarihli sayfasına göre saniyesi 2,5 kredi, yani 4 saniyelik bir klip 10 kredi. En küçük plan aylık 19 dolar, 270 kredi. |
| [VidMuse](https://vidmuse.ai/en/magi-2) | Ücretsiz planda tek seferlik 100 kredi; çıktı 720p ve filigranlı, yalnız kişisel kullanım | Sand.ai'nin kendi sitesindeki "Try on VidMuse" bağlantısı, resmi ortak. Plan bilgisi Higgsfield'in aktardığı; VidMuse'un sayfası otomatik okumaya kapalı olduğundan biz doğrulayamadık. Videodan videoya düzenleme orada var mı, denemedik. |
| [Sand.ai API](https://platform.sand.ai) | Hayır | Geliştiriciler için; üretilen saniye başına 0,08 dolar (Higgsfield ve bağımsız incelemelerin aktardığı fiyat). |
| [GitHub](https://github.com/SandAI-org/MAGI-2-preview) / [Hugging Face](https://huggingface.co/sand-ai/MAGI-2-preview) | Açık kaynak, kendi sunucunuzda ücretsiz | Önizleme sürümünün dosyaları yaklaşık 300 GB. Ev bilgisayarına göre değil; veri merkezi ekran kartı ister. |

**Dikkat:** Aramada "magi2", "magi-2 free" gibi adlarla çıkan pek çok site Sand.ai'ye ait değil. Kart bilgisi vermeden önce adresin yukarıdakilerden biri olduğuna bakın.

## Nerelerde işinize yarar?

- **Mekân:** Yeşil perde olmadan arka planı sahile, ofise, stüdyoya taşımak. Evde çektiğiniz konuşmayı başka bir yerde geçiyormuş gibi göstermek.
- **Hava ve mevsim:** Sonbahar çekimini karlı bir güne çevirmek; aynı çekimden yaz ve kış sürümü çıkarmak.
- **Kıyafet ve karakter:** Kazakla çektiğiniz videoda takım elbise giymek; kostüm ya da üniforma denemek.
- **Işık:** Gün ışığındaki çekime gece stüdyosu, neon ya da sıcak lamba havası vermek.
- **Nesne ve ürün:** Elinizdeki kalemi ürününüzle değiştirmek, masaya tabak, kitap, cihaz koymak. Ürün tanıtımı ve reklam denemeleri için hızlı.
- **Efekt:** Arkada uçuşan tüyler, kar, duman gibi şeyleri sonradan eklemek.
- **Dönem ve sanat sahnesi:** Kendinizi bir tablonun ya da tarihi bir mekânın içine koymak. Tarih anlatan içerik ve ders videoları için.
- **Ön deneme:** Gerçek çekime çıkmadan önce mekân ve kıyafet seçeneklerini görmek.

## Ayarlar (Higgsfield)

1. **Video → Create Video → Model** menüsünden **MAGI-2**'yi seçin.
2. Klibinizi **video referansı** olarak yükleyin, "ilk kare" (start image) olarak değil. İkisi birlikte kullanılamıyor.
3. **Süre:** Klibinizin süresi. 4 ile 30 saniye arası, tam saniye. Klibiniz 4 saniyeden kısaysa sonuna çekimin devamını ekleyip 4 saniyeye tamamlayın, sonra kurguda kırpın.
4. **En-boy:** 16:9. **Çözünürlük:** 1080p (tek seçenek).
5. **Enhance prompt:** kapalı. Açık olunca site istemi kendisi zenginleştiriyor; yazdığınız metnin aynen gitmesi için kapattık.
6. **Generate audio:** kapalı. Kendi sesinizi kurguda geri koyacaksınız.
7. İstemi yapıştırıp üretin. Her yeniden deneme ayrıca ücretleniyor.

## Her istemin sonuna eklenen cümle

Bu cümle yüzü, dudakları ve kadrajı sabit tutuyor. Aşağıdaki 7 istemin hepsinin sonuna aynen ekleyin:

```text
Keep the man exactly as he is: same face, glasses, beard, hair bun, body position, hand gestures, lip movements and timing. Keep the camera angle and framing locked, no camera movement. Keep the wooden table in the foreground. The change is fully visible from the very first frame. Photorealistic.
```

Kendinize göre uyarlayın: "glasses, beard, hair bun" kısmını kendi görünüşünüzle, "wooden table" kısmını önünüzde ne varsa onunla değiştirin. "The change is fully visible from the very first frame" cümlesi önemli: kurguda klibin yalnız baş kısmını kullanacaksanız değişiklik ilk karede görünmeli.

## Reels'teki 7 istem

### 1. Mekân: tropik sahil (4 sn)

```text
Change the location to a sunny tropical beach. Replace the park behind him with a turquoise sea with gentle waves, white sand and palm trees under a clear blue sky, bright midday sunlight.
```

### 2. Hava: karlı Alaska (4 sn)

```text
Change the weather and location to a snowy Alaskan wilderness in a heavy snowfall. Thick snowflakes fall throughout the shot, behind him a snow-covered spruce forest and distant white mountains, a layer of snow on the table, on the bench and on his shoulders and hair, cold overcast blue light, visible breath vapor when he speaks.
```

### 3. Kıyafet: takım elbise (4 sn)

```text
Change his clothing to an elegant black suit with a white shirt and a dark tie. Change the location to the inside of a clean public restroom: white tiled walls, a row of sinks with mirrors and toilet stalls behind him, cool fluorescent lighting.
```

Bu istemde ortak cümledeki "Keep the man exactly as he is" kısmını "Keep his face, glasses, beard, hair bun, body position, hand gestures, lip movements and timing exactly the same" diye yazdık, çünkü "olduğu gibi kalsın" ifadesi kıyafeti de kapsıyor.

### 4. Efekt: köy avlusu ve tavuklar (4 sn)

```text
Change the location to a rustic Anatolian village yard: an old stone house, a wooden fence, haystacks and dirt ground. Behind him several chickens run around and explode one after another in comic puffs of white feathers and smoke, feathers flying through the air. He does not react to them.
```

### 5. Işık: gece YouTuber stüdyosu (4 sn)

```text
Change the location and lighting to a YouTuber studio at night: a dark room with purple and blue RGB LED strips, a glowing neon sign and shelves with gadgets behind him, a softbox key light on his face with a soft rim light, shallow depth of field.
```

### 6. Nesne: çöp şiş, Osmanlı konağı (4 sn)

```text
Replace the pencil in his hand with a çöp şiş: a thin wooden skewer with small grilled lamb cubes. Add a plate of the same skewers with flatbread on the table in front of him. Change the location to the interior of a historic Ottoman mansion: carved wooden ceiling, patterned carpets, low sofas with cushions, warm light from tall windows.
```

### 7. Kapanış: Son Akşam Yemeği (9 sn)

```text
Transform the scene into Leonardo da Vinci's The Last Supper. He sits at the center of a long table covered with a white tablecloth, with bread, plates and cups on it. Robed disciples sit on both sides of him along the table, gesturing and talking to each other. Behind them a Renaissance hall with a coffered ceiling and three windows opening onto a pale landscape, symmetrical one-point perspective, warm fresco-like colors.
```

Bu istemde ortak cümledeki "Keep the wooden table in the foreground" beyaz örtülü masayla çelişebilir. Sonuç tuhaf çıkarsa o cümleyi çıkarın.

## Bilmeniz gerekenler

- Çıktı yalnız 1080p. 4K çekiminiz 1080p'ye iner.
- En kısa üretim 4 saniye. Daha kısa bir kesit için klibi uzatıp sonra kırpın.
- Biz sabit kamerayla çektik. Elde ya da hareketli kamerayla nasıl sonuç verdiğini denemedik.
- İstemler İngilizce yazıldı; "çöp şiş" gibi Türkçe bir yemek adını tarifle birlikte yazınca anladı.
- Sesi modele bırakmayın, kurguda orijinal sesinizi geri koyun.
