---
baslik: Tekrar eden işleri yerine yaptırmak
ozet: Takvim, e-posta, raporlar, haftalık kontroller... Bir kez tarif ediyorsun, her gün/hafta kendi kendine çalışıyor.
ikon: ⏰
sira: 6
zorluk: yeni
kategori: otomasyon
araclar: [claude, claude-code, github-actions]
etiketler: [otomasyon, zamanlama, takvim, e-posta, routine, cron]
---

## Ne bu?

Claude'a bir işi **tarif edip zamanlayabiliyorsun**: "Her pazartesi 08:00'de bu haftaki takvimimi özetle ve hazırlık listesi çıkar", "Her akşam Drive'daki yeni dosyaları kontrol et", "Her ayın 1'inde şu klasörden rapor üret". İş buluttaki bir Claude tarafından yapılıyor; bilgisayarının açık olması gerekmiyor.

## Ne işe yarar?

- **Sabah brifingi:** Takvim + e-posta + haberler tek özet olarak.
- **İçerik takibi:** Bu site tam olarak böyle çalışıyor: günde 3 kez kaynakları tarayan bir görev, yenilikleri bulup Türkçe yazıyor.
- **Takvim işleri:** Toplantı sonrası notları özetleyip ilgili kişilere e-posta taslağı hazırlamak.
- **Kontroller:** Siteniz ayakta mı, bir ürünün fiyatı değişti mi, yeni başvuru geldi mi?

## İlk adım

1. [claude.ai](https://claude.ai) üzerinde Google Takvim ve Gmail bağlayıcılarını aç.
2. Claude Code'da `/schedule` yazıp şöyle bir görev tarif et: *"Her sabah 08:00'de bugünkü takvimimi ve okunmamış önemli e-postaları 5 maddede özetle."*
3. Birkaç gün izle, isteğini düzelt. Sonra ikinci işi ekle.
