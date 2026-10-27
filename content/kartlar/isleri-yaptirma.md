---
baslik: "Her sabah 08:00'de hazır bir brifing almak"
ozet: Takvim, e-posta, raporlar, haftalık kontroller. Bir kez tarif ediyorsunuz, her gün ya da her hafta kendiliğinden çalışıyor.
ikon: ⏰
sira: 6
zorluk: yeni
kategori: otomasyon
araclar: [claude, claude-code, github-actions]
etiketler: [otomasyon, zamanlama, takvim, e-posta, routine, cron]
gorsel: ./medya/isleri-yaptirma.webp
---

## Ne bu?

Claude'a bir işi **tarif edip zamanlayabiliyorsunuz**: "Her pazartesi 08:00'de bu haftaki takvimimi özetle ve hazırlık listesi çıkar", "Her akşam Drive'daki yeni dosyaları kontrol et", "Her ayın 1'inde şu klasörden rapor üret". İş buluttaki bir Claude tarafından yapılıyor; bilgisayarınızın açık olması gerekmiyor.

## Ne işe yarar?

- **Sabah brifingi:** Takvim + e-posta + haberler tek özet olarak.
- **İçerik takibi:** Bu sitenin gündemi de böyle tutuluyor: kaynaklar günde üç kez taranıyor, yenilikler Türkçe yazılıyor.
- **Takvim işleri:** Toplantı sonrası notları özetleyip ilgili kişilere e-posta taslağı hazırlamak.
- **Kontroller:** Siteniz ayakta mı, bir ürünün fiyatı değişti mi, yeni başvuru geldi mi?

## İlk adım

1. [claude.ai](https://claude.ai) üzerinde Google Takvim ve Gmail bağlayıcılarını açın.
2. Claude Code'da `/schedule` yazıp şöyle bir görev tarif edin: *"Her sabah 08:00'de bugünkü takvimimi ve okunmamış önemli e-postaları 5 maddede özetle."*
3. Birkaç gün izleyin, isteğinizi düzeltin. Sonra ikinci işi ekleyin.
