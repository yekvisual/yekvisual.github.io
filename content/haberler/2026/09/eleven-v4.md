---
baslik: "Eleven v4 ile 10 saniyelik kayıttan ses klonu; Türkçe dahil 90'dan fazla dil"
tarih: 2026-09-28
kategori: ses
puan: 4
ozet: "ElevenLabs'in yeni konuşma modelleri Eleven v4 ve v4 Turbo çıktı. 90'dan fazla dil destekliyor, Türkçe listede var. Anlık ses klonu için 10 saniyelik kayıt yetiyor; [laughs], [light rain] gibi satır içi etiketlerle ve doğal dille yönlendirme daha isabetli. Turbo'nun ilk sese kadar gecikmesi yaklaşık 150 ms."
neden_onemli: "Seslendirme, dublaj ve sesli asistan işlerinde iki şey para ve zaman yiyor: kaliteli klon için uzun kayıt gereksinimi ve tonlamayı tutturmak için tekrar tekrar üretmek. 10 saniyelik klon ve etiketle yönlendirme bu iki maliyeti düşürüyor; Türkçe desteği sayesinde Reels seslendirmesi ya da kurumsal eğitim videosu için doğrudan kullanılabiliyor."
yekvisual_notu: "v4'ü henüz Türkçe metinle denemedim; merak ettiğim, vurgu ve soru tonlamasının etiketlerle ne kadar düzeldiği. Aynı paragrafı v3 ve v4 ile üretip burada paylaşacağım. Ücretsiz planda v4'ün açık olup olmadığını doğrulamadım."
ucretsiz: null
acik_kaynak: false
zorluk: yeni
sirket: ElevenLabs
model: Eleven v4
etiketler: [elevenlabs, seslendirme, ses klonu, türkçe, metinden ses]
kapak: ./eleven-v4/kapak.webp
kapak_kaynak: "Görsel: ElevenLabs"
kaynaklar:
  - { ad: "ElevenLabs blog: Eleven v4", url: "https://elevenlabs.io/blog/eleven-v4" }
  - { ad: "ElevenLabs belgeleri: Modeller", url: "https://elevenlabs.io/docs/overview/models" }
---

## Neler yeni?

ElevenLabs, 28 Eylül'de Eleven v4 ve Eleven v4 Turbo'yu yayınladı. İki model de ElevenAgents, ElevenCreative ve API'de kullanılabiliyor. Öne çıkanlar:

- **Dil:** 90'dan fazla dil; önceki nesilde 70'ti. Belgelerdeki listede Türkçe (tr) var.
- **Klonlama:** Anlık ses klonu (Instant Voice Clone) 10 saniyelik kayıtla çalışıyor. Yüksek kalite isteyenler için Profesyonel Ses Klonu (PVC) desteği de v4'te var.
- **Yönlendirme:** Konuşmanın nasıl söyleneceğini doğal dille tarif ediyorsunuz; metnin içine `[laughs]`, `[said angrily in French accent]`, `[light rain]`, `[phone buzzing]` gibi etiketler koyabiliyorsunuz. Şirket, modelin bu etiketlere önceki modellerden daha sadık olduğunu söylüyor.
- **Hız:** v4'te medyan gecikme yaklaşık 100 ms; Turbo'da ilk sese kadar yaklaşık 150 ms. Bu, sesli asistanlarda "iki kişinin konuşması arasındaki duraklamadan daha kısa" demek.
- **Sınır:** Tek istekte 10.000 karakter, yaklaşık 10 dakika ses.

Fiyatlandırma duyuruda ayrıca belirtilmiyor; mevcut plan ve karakter kotaları geçerli görünüyor.

## Kimin işine yarar?

- **İçerik üreticileri:** Kendi sesinizi 10 saniyelik kayıtla klonlayıp Reels ve YouTube seslendirmelerini Türkçe üretmek.
- **Prodüksiyon ekipleri:** Dublaj ve belgesel anlatımında etiketlerle gülme, iç çekme, ortam sesi eklemek; ikinci bir ses kaydı almadan tonlamayı değiştirmek.
- **Kurumsal ekipler:** Sesli asistan ve çağrı akışlarında Turbo'nun düşük gecikmesi; çok dilli eğitim içeriğinde tek modelle 90+ dil.

## Nasıl denenir?

[elevenlabs.io](https://elevenlabs.io) üzerinde hesap açıp metinden ses ekranında model olarak Eleven v4'ü seçin. Türkçe bir paragraf yapıştırın, bir cümleye `[sighs]` ekleyin ve farkı dinleyin. Klon için sessiz bir odada 10 saniyelik temiz kayıt yeterli. API'de aynı modelleri `model_id` ile çağırıyorsunuz.

## Sınırlar

Türkçe için kalite ölçümü yayımlanmamış; dil listesinde olmak, her dilde aynı doğallık demek değil. Klonladığınız sesin size ait olması ya da izin almış olmanız gerekiyor.
