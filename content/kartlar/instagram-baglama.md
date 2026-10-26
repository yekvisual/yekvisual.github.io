---
baslik: Reels'in kendi kendine paylaşılsın, sen sadece çek
ozet: Videoları bir klasöre at; her gün aynı saatte sıradaki Reels olarak paylaşılsın, bilgisayarın kapalıyken bile.
ikon: 📲
sira: 4
zorluk: orta
kategori: otomasyon
araclar: [reels-bot, github-actions]
etiketler: [instagram, reels, otomatik paylaşım, github actions, meta api]
gorsel: ./medya/instagram-baglama.webp
---

## Ne bu?

Instagram'ın **resmi API'si** üzerinden, şifre vermeden ve "bot gibi" giriş yapmadan, kendi hesabına otomatik Reels paylaşabiliyorsun. [reels-bot](https://github.com/yekvisual/reels-bot) tam olarak bunu yapan, ücretsiz ve açık bir araç: videoları `videos/` klasörüne numaralı koyuyorsun (`001_tanitim.mp4`, yanına `001_tanitim.txt` açıklama), GitHub Actions her gün saat 19:00'da sıradakini paylaşıyor; bilgisayarının açık olması gerekmiyor.

## Ne işe yarar?

- Bir hafta sonu 30 video üretip bir ayı planlamak.
- Tatildeyken bile hesabın düzenli paylaşım yapmak.
- Üretim hattının sonuna takmak: Remotion video üretir → klasöre düşer → paylaşım kendiliğinden olur.

## İlk adım

1. Instagram hesabını **Profesyonel** hesaba çevir (Ayarlar → Hesap türü).
2. [developers.facebook.com](https://developers.facebook.com/apps) üzerinden bir uygulama aç ve erişim anahtarı al; adımlar reels-bot'un README'sinde tek tek yazıyor.
3. reels-bot'u kendi GitHub hesabına kopyala, anahtarı gir, ilk videoyu elle tetikle. Her şey 10–15 dakika.

> Bu sitenin haftalık özetleri de yakında aynı hatla Instagram'a düşecek.
