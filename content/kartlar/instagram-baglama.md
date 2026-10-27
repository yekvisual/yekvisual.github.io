---
baslik: Reels paylaşımını otomatiğe bağlamak
ozet: Videoları bir klasöre atın; her gün aynı saatte sıradaki Reels olarak paylaşılsın, bilgisayarınız kapalıyken bile.
ikon: 📲
sira: 4
zorluk: orta
kategori: otomasyon
araclar: [reels-bot, github-actions]
etiketler: [instagram, reels, otomatik paylaşım, github actions, meta api]
gorsel: ./medya/instagram-baglama.webp
---

## Ne bu?

Instagram'ın **resmi API'si** üzerinden, şifre vermeden ve sahte giriş yapmadan, kendi hesabınıza zamanlanmış Reels paylaşabiliyorsunuz. [reels-bot](https://github.com/yekvisual/reels-bot) tam olarak bunu yapan, ücretsiz ve açık bir araç: videoları `videos/` klasörüne numaralı koyuyorsunuz (`001_tanitim.mp4`, yanına `001_tanitim.txt` açıklama), GitHub Actions her gün saat 19:00'da sıradakini paylaşıyor; bilgisayarınızın açık olması gerekmiyor.

## Ne işe yarar?

- Bir hafta sonu 30 video üretip bir ayı planlamak.
- Tatildeyken bile hesabınızın düzenli paylaşım yapması.
- Üretim hattının sonuna takmak: Remotion video üretir → klasöre düşer → paylaşım kendiliğinden olur.

## İlk adım

1. Instagram hesabınızı **Profesyonel** hesaba çevirin (Ayarlar → Hesap türü).
2. [developers.facebook.com](https://developers.facebook.com/apps) üzerinden bir uygulama açın ve erişim anahtarı alın; adımlar aracın README'sinde tek tek yazıyor.
3. Aracı kendi GitHub hesabınıza kopyalayın, anahtarı girin, ilk videoyu elle tetikleyin. Her şey 10–15 dakika.

> Bu sitenin haftalık özetleri de yakında aynı hatla Instagram'a düşecek.
