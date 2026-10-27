---
baslik: "Kandinsky 6.0 Video: sesli ve dudak eşlemeli 5 saniyelik klip, MIT lisansı"
tarih: 2026-10-06
kategori: video
puan: 4
ozet: "Kandinsky Lab, görüntü ve sesi aynı anda üreten Kandinsky 6.0 Video'yu MIT lisansıyla açtı. İki boy var: 3 milyar parametreli Lite ve 29 milyar parametreli Pro. İkisi de 5 saniyelik, 24 fps, 44 kHz sesli ve dudak eşlemeli klip üretiyor; yerleşik büyütme ile 1920×1080'e çıkıyor."
neden_onemli: "Açık kaynaklı video modellerinin çoğu sessiz üretir, sesi sonradan eklersiniz. Kandinsky 6.0 konuşmayı ve dudak hareketini aynı geçişte üretiyor ve MIT lisansı ticari kullanımı serbest bırakıyor. Lite sürümünün 16 GB ekran kartında çalışması, bunu evde deneyebileceğiniz birkaç sesli video modelinden biri yapıyor."
yekvisual_notu: "Henüz kurmadım; ComfyUI desteği olduğu için sıraya aldım. Makale Rusça ve İngilizce istemle eğitildiğini yazıyor, Türkçe konuşmayı ne kadar doğru söyletir bilmiyorum, denemek lazım. 4090'da Pro'nun bir klip için yaklaşık 4 dakika sürmesi bana makul geliyor."
ucretsiz: true
acik_kaynak: true
zorluk: teknik
sirket: Kandinsky Lab
model: Kandinsky 6.0 Video
etiketler: [kandinsky, açık kaynak, video üretim, ses, dudak eşleme, comfyui]
kart: acik-kaynak-modeller
kaynaklar:
  - { ad: "arXiv: Kandinsky 6.0 Video makalesi", url: "https://arxiv.org/abs/2610.05608" }
  - { ad: "GitHub: kandinskylab/kandinsky-6", url: "https://github.com/kandinskylab/kandinsky-6" }
  - { ad: "Hugging Face koleksiyonu", url: "https://huggingface.co/collections/kandinskylab/kandinsky-60-diffusers" }
---

## Neler yeni?

Kandinsky Lab, 6 Ekim'de Kandinsky 6.0 Video'nun kodunu, ağırlıklarını ve Diffusers entegrasyonunu MIT lisansıyla yayınladı. Modelin işi "senkron video ve ses": metinden ya da bir görselden yola çıkıp görüntüyü, sesi ve konuşan karakterin dudak hareketini tek geçişte üretiyor.

- **İki boy:** Lite (3 milyar parametre) ve Pro (29 milyar parametre). Mimari aynı, ölçek farklı. Damıtılmış (distill) hızlı sürümler de var.
- **Çıktı:** 5 saniye, 24 fps, 44 kHz ses. Taban çözünürlük 480×864; yerleşik süper çözünürlük ile 1920×1080.
- **Donanım:** Depodaki tabloya göre 24 GB RTX 4090'da Lite modül aktarımıyla, Pro blok aktarımıyla çalışıyor; 16 GB RTX 5060 Ti'de ikisi de aktarımla çalışıyor. 4090'da damıtılmış Pro bir klibi 235 saniyede, damıtılmış Lite 68 saniyede üretiyor.
- **Araç desteği:** Diffusers, ComfyUI, vLLM-omni, SGLang ve FastVideo.

Makaleye göre Pro, insan değerlendirmesinde VABench ölçümlerinin çoğunda açık kaynaklı LTX 2.5'in önünde ve özellikle konuşma kalitesinde kapalı sistemlerle yarışıyor. Bu, ekibin kendi değerlendirmesi.

## Kimin işine yarar?

- **Evde deneyen üreticiler:** 16 GB'lık bir kartla sesli, konuşan karakter klibi üretmek için şu an en erişilebilir açık seçeneklerden biri.
- **Prodüksiyon ekipleri:** Animatik ya da ön izleme için sesli 5 saniyelik planlar; MIT lisansı müşteri işinde kullanımı sorunsuz kılıyor.
- **Geliştiriciler:** Diffusers ile kendi sunucunuza kurabiliyor, ComfyUI düğümleriyle iş akışına ekleyebiliyorsunuz.

## Nasıl denenir?

Ağırlıklar [Hugging Face koleksiyonunda](https://huggingface.co/collections/kandinskylab/kandinsky-60-diffusers), kurulum ve VRAM ayarları [GitHub deposunda](https://github.com/kandinskylab/kandinsky-6). Kartınız 16–24 GB ise Lite'ın damıtılmış sürümüyle başlayın; "VRAM bütçesi" ön ayarlarını kullanın. İlk denemede bir fotoğraf verip tek cümlelik İngilizce bir replik söyletin ve dudak eşlemesine bakın.

## Sınırlar

5 saniye sabit; uzun sahne için kesitleri birleştirmeniz gerekiyor. Eğitim istemleri Rusça ve İngilizce; başka dillerde konuşma kalitesi belgelenmemiş.
