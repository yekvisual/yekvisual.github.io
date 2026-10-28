---
baslik: "FLUX 3 Image Klein açık kaynak oldu: 8 GB ekran kartında 4K görsel üretimi"
tarih: 2026-10-15
kategori: gorsel
puan: 5
ozet: "Black Forest Labs, 5,6 milyar parametreli FLUX 3 Image Klein'ın ağırlıklarını açtı. Model 4K üretiyor, 10 referans görsele kadar alıyor ve INT8 sürümü 8 GB VRAM'li ekran kartında çalışıyor. Yıllık geliri 5 milyon doların altındaki kişi ve şirketler ticari olarak ücretsiz kullanabiliyor."
neden_onemli: "İndirip kendi bilgisayarınızda çalıştırabildiğiniz bir görsel modelinin 4K çıktı, referansla düzenleme ve kutuyla konum kontrolü sunması, abonelik ödemeden ürün görseli ve kapak üretmek isteyenler için somut bir seçenek. ComfyUI ve Diffusers desteği ilk günden geldiği için mevcut iş akışlarına eklemek de kolay."
yekvisual_notu: "Mac Studio'da ComfyUI ile denedim: 1K görsel yarım dakikada, 4K görsel 10 dakikada çıkıyor. Tabela, logo gibi kısa Türkçe yazıyı hatasız basıyor; takvim gibi yazısı çok bir afişte dağılıyor. Reels kapağı ve ürün görseli için işime yarar. 8 GB kart iddiasını elimde öyle bir kart olmadığı için ölçemedim."
ucretsiz: true
acik_kaynak: true
zorluk: orta
sirket: Black Forest Labs
model: FLUX 3 Image Klein
etiketler: [flux, black forest labs, görsel üretim, açık kaynak, comfyui, 4k]
kart: acik-kaynak-modeller
kapak: ./flux-3-image-klein/kapak.webp
kapak_kaynak: "Görsel: Black Forest Labs"
denemeler:
  - { tip: gorsel, src: ./flux-3-image-klein/deneme-1.webp, alt: "2048×2048, 16 adım: 3 dk 26 sn. İstem: “Küçük bir atölye kapısında ahşap tabela, üzerinde 'YEK Lab' yazıyor, altında küçük harflerle 'görsel · video · ses', sıcak akşam ışığı, fotoğraf”. Yazı harfi harfine doğru; tabela kapıda değil, duvarda.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./flux-3-image-klein/deneme-2.webp, alt: "3840×2160 (4K), 16 adım: 10 dk 22 sn. Gün batımında Boğaz, vapur ve martılar. Siluette iki Galata Kulesi var.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./flux-3-image-klein/deneme-3.webp, alt: "Aynı 4K görselden küçültmeden kırpılmış 1200×1200 piksellik bölüm: kule ve minarelerde ayrıntı net.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./flux-3-image-klein/deneme-4.webp, alt: "1024×1024: 34 sn. Karda yürüyen kaplan, gün doğumu, bıyıklarda kırağı.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./flux-3-image-klein/deneme-5.webp, alt: "1024×1024: 34 sn. Beyaz zeminde seramik kahve fincanı, e-ticaret fotoğrafı.", kaynak: "YEK Lab denemesi" }
  - { tip: gorsel, src: ./flux-3-image-klein/deneme-6.webp, alt: "768×1024: 25 sn. Başlık “Hafta Sonu Laboratuvarı” doğru; istemdeki “Kasım ayı atölye takvimi afişi” ifadesini afişe yazmış, takvimdeki sayılar ve gün adları anlamsız.", kaynak: "YEK Lab denemesi" }
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

Hugging Face'teki depo indirmeden önce kısa bir lisans formu ve Hugging Face hesabıyla oturum açmayı istiyor; formu doldurduğumda erişim hemen açıldı. Lisans metnini okuyun. Görsel içine metin basma kalitesine dair resmi bir iddia yok.

## Ben denedim

Mac Studio'da (M3 Ultra, 256 GB) ComfyUI ile bf16 sürümünü resmi iş akışının ayarlarıyla denedim: 16 adım, istem geliştirici kapalı. 1024×1024 görsel 33–34 saniye, 2048×2048 görsel 3 dakika 26 saniye, 3840×2160 görsel 10 dakika 22 saniye sürdü. Mac'te INT8 sürümü çalışmadığı için bu süreler NVIDIA'nın RTX 4070 ölçümünün (1 MP'de 8,9 sn, 2048×2048'de 50,4 sn) yaklaşık dört katı. 2048 ve üstünde ComfyUI son adımda hata verdi; VAE Decode yerine VAE Decode (Tiled) düğümünü kullanınca düzeldi.

Kısa Türkçe yazıda başarılı: tabeladaki "YEK Lab" ve "görsel · video · ses" iki çözünürlükte de hatasız çıktı, "ö" dahil. Yazı çoğalınca dağılıyor: afişte başlık doğru ama takvimdeki sayılar anlamsız. İstemdeki tarifi de afişe yazı olarak bastı. İstanbul görselinde ayrıntı net, ama siluette iki Galata Kulesi var; gerçek bir yeri çizdirirken dikkat edin. 8 GB'lık ekran kartında deneyemedim.
