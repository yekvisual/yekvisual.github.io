---
baslik: "5 dakikada grafik animasyonu üretmek: Remotion"
ozet: Videoyu kelimelerle tarif edin, kodu Claude yazsın. Kod bilmenize gerek yok; Remotion ve HyperFrames gerisini hallediyor.
ikon: 🎬
sira: 1
zorluk: orta
kategori: video
araclar: [remotion, hyperframes, claude-code]
etiketler: [remotion, hyperframes, claude code, motion graphics]
gorsel: ./medya/kodla-video.webp
---

## Ne bu?

Video kurgu programında saatlerce keyframe çekmek yerine videoyu **kodla tarif ediyorsunuz**: "3 saniye logo açılsın, sonra şu başlık alttan kaysın, arkada şu müzik çalsın." [Remotion](https://www.remotion.dev) bunu React ile, [HyperFrames](https://hyperframes.dev) ise düz HTML/CSS ile yapıyor. Kodu sizin yazmanız gerekmiyor; Claude'a ne istediğinizi anlatıyorsunuz, o yazıyor, siz sonucu izleyip "başlığı büyüt, rengi değiştir" diyorsunuz.

## Ne işe yarar?

- Aynı şablondan **onlarca farklı video** üretmek (her ürün, her şehir, her öğrenci için ayrı video).
- Verilerden video yapmak: tablo veriyorsunuz, animasyonlu grafik videosu alıyorsunuz.
- Reels/Shorts için alt yazılı, logolu, tutarlı görünümlü içerikleri dakikalar içinde çıkarmak.

## İlk adım

1. Bilgisayarınıza [Claude Code](https://claude.com/claude-code) ve Node.js kurun.
2. Boş bir klasörde Claude'a şunu deyin: *"Remotion ile 10 saniyelik, dikey (9:16), koyu arka planlı bir Reels videosu oluştur. Başlık 'Merhaba' olsun ve alttan yukarı kaysın."*
3. `npm run dev` ile tarayıcıda önizleyin, beğenmediğiniz her şeyi Claude'a söyleyin, render alın.

> Bu sitenin Instagram videoları da aynı mantıkla, koddan üretiliyor.
