---
baslik: Kod yazmadan, kodla video üretmek
ozet: Remotion ve HyperFrames ile videoyu bir web sayfası gibi tarif ediyorsun, gerisini yapay zekâ yazıyor.
ikon: 🎬
sira: 1
zorluk: orta
kategori: video
araclar: [remotion, hyperframes, claude-code]
etiketler: [remotion, hyperframes, claude code, motion graphics]
gorsel: ./medya/kodla-video.webp
---

## Ne bu?

Video kurgu programında saatlerce keyframe çekmek yerine videoyu **kodla tarif ediyorsun**: "3 saniye logo açılsın, sonra şu başlık alttan kaysın, arkada şu müzik çalsın." [Remotion](https://www.remotion.dev) bunu React ile, [HyperFrames](https://hyperframes.dev) ise düz HTML/CSS ile yapıyor. Kodu senin yazman gerekmiyor; Claude'a ne istediğini anlatıyorsun, o yazıyor, sen sonucu izleyip "başlığı büyüt, rengi değiştir" diyorsun.

## Ne işe yarar?

- Aynı şablondan **onlarca farklı video** üretmek (her ürün, her şehir, her öğrenci için ayrı video).
- Verilerden video yapmak: tablo veriyorsun, animasyonlu grafik videosu alıyorsun.
- Reels/Shorts için alt yazılı, logolu, tutarlı görünümlü içerikleri dakikalar içinde çıkarmak.

## İlk adım

1. Bilgisayarına [Claude Code](https://claude.com/claude-code) ve Node.js kur.
2. Boş bir klasörde Claude'a şunu de: *"Remotion ile 10 saniyelik, dikey (9:16), koyu arka planlı bir Reels videosu oluştur. Başlık 'Merhaba' olsun ve alttan yukarı kaysın."*
3. `npm run dev` ile tarayıcıda önizle, beğenmediğin her şeyi Claude'a söyle, render al.

> Bu sitedeki haber kapaklarının bir kısmı da aynı mantıkla, koddan üretiliyor.
