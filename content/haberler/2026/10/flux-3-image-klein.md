---
baslik: "FLUX 3 Image Klein açık kaynak oldu: 8 GB ekran kartında 4K görsel üretimi"
tarih: 2026-10-15
kategori: gorsel
puan: 5
ozet: "Black Forest Labs, 5,6 milyar parametreli FLUX 3 Image Klein'ın ağırlıklarını açtı. Model 4K üretiyor, 10 referans görsele kadar alıyor ve INT8 sürümü 8 GB VRAM'li ekran kartında çalışıyor. Yıllık geliri 5 milyon doların altındaki kişi ve şirketler ticari olarak ücretsiz kullanabiliyor."
neden_onemli: "İndirip kendi bilgisayarınızda çalıştırabildiğiniz bir görsel modelinin 4K çıktı, referansla düzenleme ve kutuyla konum kontrolü sunması, abonelik ödemeden ürün görseli ve kapak üretmek isteyenler için somut bir seçenek. ComfyUI ve Diffusers desteği ilk günden geldiği için mevcut iş akışlarına eklemek de kolay."
yekvisual_notu: "Henüz indirmedim; ComfyUI'de denemek için sıraya aldım. Asıl merak ettiğim şey 8 GB kartta 4K üretimin kaç dakika sürdüğü ve Türkçe karakterli metni görsele ne kadar doğru bastığı; ikisini de ölçmeden yorum yapmıyorum. Lisans eşiği bireysel üretici için rahat, ama metni okuyun."
ucretsiz: true
acik_kaynak: true
zorluk: orta
sirket: Black Forest Labs
model: FLUX 3 Image Klein
etiketler: [flux, black forest labs, görsel üretim, açık kaynak, comfyui, 4k]
kart: acik-kaynak-modeller
kapak: ./flux-3-image-klein/kapak.webp
kapak_kaynak: "Görsel: Black Forest Labs"
kaynaklar:
  - { ad: "Black Forest Labs duyurusu", url: "https://bfl.ai/blog/flux-3-image-klein" }
  - { ad: "Hugging Face: flux-3-image-klein", url: "https://huggingface.co/black-forest-labs/flux-3-image-klein" }
  - { ad: "VentureBeat", url: "https://venturebeat.com/technology/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses" }
---

## Neler yeni?

Black Forest Labs, 15 Ekim'de FLUX 3 Image Klein'ın ağırlıklarını yayınladı. Bu, büyük FLUX 3 Image modelinin küçültülmüş, 5,6 milyar parametreli hali. Şirkete göre büyük modelin ana özellikleri korunmuş:

- **Yerel 4K üretim.** Önce küçük üretip sonra büyütmek yerine doğrudan 4K çıktı alıyorsunuz.
- **Üretim ve düzenleme tek modelde.** Metinden görsel, mevcut görseli değiştirme ve 10'a kadar referans görselle yönlendirme aynı modelde.
- **Sınırlayıcı kutu (bounding box).** Bir öğenin nereye yerleşeceğini ya da düzenlemenin hangi alanla sınırlı kalacağını kutu çizerek belirliyorsunuz.

Bellek ihtiyacı sürüme göre değişiyor: BF16 11,2 GB, FP8 5,6 GB; INT8 sürümü 8 GB VRAM'li GeForce RTX kartlarda çalışıyor. Hız tarafında NVIDIA'nın ComfyUI ölçümü (damıtılmış model, 16 adım, INT8, 1 MP görsel): RTX 5090'da 4,1 sn, RTX 5070'te 7,7 sn, RTX 4070'te 8,9 sn. 2048×2048'de RTX 4070 için süre 50,4 sn. Şirket, modelin açık kaynaklı rakipler arasında metinden görsel, çoklu referans ve düzenlemede ilk sırada olduğunu söylüyor; bu iddia kendi ölçümlerine dayanıyor.

## Kimin işine yarar?

- **Bireysel üreticiler ve küçük ekipler:** Yıllık geliri 5 milyon doların altındaysanız ticari kullanım ücretsiz. Reels kapakları, ürün görselleri, sosyal medya serileri için abonelik yok.
- **Geliştiriciler:** Kendi sunucunuzda çalıştırmak istemiyorsanız API'de 1K görsel 0,009 $; 4K görsel 0,036 $.
- **Büyük şirketler:** Gelir eşiğinin üstündeyseniz kendi sunucunuzda çalıştırmak için ayrı anlaşma gerekiyor; API bu şarta bağlı değil.

## Nasıl denenir?

En kolay yol ComfyUI: model ilk günden destekleniyor. Ağırlıklar Hugging Face'te [black-forest-labs/flux-3-image-klein](https://huggingface.co/black-forest-labs/flux-3-image-klein) adresinde; eğitim için ayrıca "base" sürüm var. Diffusers, TensorRT-LLM, SGLang ve vLLM-Omni ile de çalışıyor; LoRA eğitimi için Ostris'in AI Toolkit'i destekleniyor. 8 GB kartınız varsa INT8 sürümüyle başlayın, önce 1K üretip süreyi görün, sonra 4K'ya çıkın.

## Sınırlar

Hugging Face'teki depoya erişim için kısa bir form istendiğine dair haberler var; indirmeden önce lisans metnini okuyun. Görsel içine metin basma kalitesine dair resmi bir iddia yok.
