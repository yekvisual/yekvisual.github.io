---
baslik: "Comfy Agent: akışı tarif edin, ComfyUI düğümlerini yapay zekâ kursun"
tarih: 2026-10-01
kategori: araclar
puan: 4
ozet: "ComfyUI ekibi, tuvalin içinde çalışan bir asistan olan Comfy Agent'ı yayınladı. Ne istediğinizi yazıyorsunuz; asistan iş akışını planlıyor, düğümleri yerleştirip bağlıyor, çalıştırıyor ve hata verirse düzeltiyor. İlk gün Comfy Cloud'da herkese açık, beta aşamasında; masaüstü sürümü birkaç hafta içinde geleceği söyleniyor."
neden_onemli: "ComfyUI en esnek açık kaynak görsel ve video aracı, ama düğüm grafiği kurmak ve bozulan iş akışını onarmak yeni başlayanların en çok takıldığı yer. Asistanın bu işi üstlenmesi, 'bu üretimi üç farklı video modeliyle karşılaştır' ya da 'ürün çekimi iş akışımı şu 20 görsele uygula' gibi işleri tek cümleye indiriyor."
yekvisual_notu: "Henüz denemedim; Comfy Cloud'daki ücretsiz sohbet hakkıyla basit bir metinden görsel akışını kurdurup ne çıkardığına bakacağım. Asıl beklediğim masaüstü sürümü; kendi ekran kartımda, kendi özel düğümlerimle çalışıp çalışmayacağı belli değil. Her mesaj Comfy'nin sunucusundan geçtiği için tamamen çevrimdışı bir seçenek değil."
ucretsiz: null
acik_kaynak: false
zorluk: orta
sirket: Comfy Org
model: Comfy Agent
etiketler: [comfyui, comfy agent, otomasyon, iş akışı, ajan, görsel üretim]
kapak: ./comfy-agent/kapak.webp
kapak_kaynak: "Görsel: Comfy Org"
kaynaklar:
  - { ad: "Comfy blog: Comfy Agent duyurusu", url: "https://blog.comfy.org/p/comfy-agent-the-first-agent-for-craft" }
  - { ad: "comfy.org/agent", url: "https://comfy.org/agent" }
  - { ad: "Digital Production", url: "https://www.digitalproduction.com/2026/10/09/comfy-agent-ai-comfyui-workflows/" }
---

## Neler yeni?

Comfy Org, 1 Ekim'de Comfy Agent'ı duyurdu. Asistan ComfyUI arayüzünün içinde çalışıyor ve duyuruya göre şunları yapıyor: tekniği planlayıp değerlendirme, iş akışı kurma, hataları düzeltme, model ve dosya bulma, teknik terimleri açıklama. Mevcut bir grafiği yeniden yapılandırabiliyor, yüklediğiniz görselleri "görerek" anlıyor. Duyurudaki örnek istekler:

- "Aynı üretimi 3 video modeliyle daha karşılaştır."
- "Bu iş akışı ne yapıyor, nerede yavaş?"
- "Ürün çekimi iş akışımı şu 20 görsele yeniden uygula."

Beş sohbeti paralel açabiliyorsunuz; her birinin kendi geçmişi var. Bir kez yazıp tekrar çağırdığınız "beceriler" (skills) tanımlayabiliyor, bunları herkese açık ya da özel tutabiliyorsunuz. Arka planda Anthropic'in modelleri çalışıyor; yerel dil modeli desteği yol haritasında.

Erişim: Comfy Cloud'da (cloud.comfy.org) beta olarak herkese açık. Yeni hesaplara deneme için bir miktar ücretsiz sohbet veriliyor, sonrası Comfy Kredisi'nden düşüyor; fiyat token bazlı. Digital Production'ın aktardığı Cloud planları aylık 20, 35 ve 100 $. Masaüstü sürümü "birkaç hafta içinde" deniyor; yerel ekran kartı, özel düğüm desteği ve asistanın kendi düğüm yazması yol haritasında.

## Kimin işine yarar?

- **ComfyUI'ye yeni başlayanlar:** Düğüm mantığını öğrenirken bozulan akışı asistana onarttırmak öğrenme süresini kısaltır.
- **İleri kullanıcılar:** Aynı istemi farklı modellerle karşılaştırma, toplu üretim, akışı hız için inceleme gibi tekrar işleri.
- **Ekipler:** Ortak "beceri" tanımlayıp ekibin herkesinin aynı iş akışını aynı şekilde çalıştırmasını sağlamak.

## Nasıl denenir?

[cloud.comfy.org](https://cloud.comfy.org) üzerinde hesap açın, sağdaki Agent panelinden deneme sohbetini kullanın. İlk görev olarak "bir ürün fotoğrafının arka planını değiştiren akış kur" gibi tek adımlı bir şey isteyin; sonucu düğüm düğüm okuyun, asistanın ne eklediğini anlamak sonraki akışlarda işinize yarar.

## Sınırlar

Beş paralel sohbet beş paralel GPU işi demek değil; eksik model ve dosyaları yine sizin sağlamanız gerekiyor. Yerel kurulum geldiğinde bile mesajlar Comfy'nin çevrimiçi servisinden geçiyor; tamamen çevrimdışı çalışmıyor.
