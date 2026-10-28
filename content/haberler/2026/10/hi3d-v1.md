---
baslik: "Hi3D V1.0 açık kaynak: kaba 3D modeli fotoğrafa bakarak ayrıntılandırıyor"
tarih: 2026-10-23
kategori: 3d
puan: 4
ozet: "Hi3D, eski adı Sparc3D olan 3D modelinin ilk sürümünü açık kaynak yaptı. Model bir nesnenin referans fotoğrafı ile kaba 3D modelini alıp çok daha ayrıntılı bir geometri üretiyor; kod ve ağırlıklar GitHub ve Hugging Face'te."
neden_onemli: "Yapay zekâyla üretilen 3D modellerin en zayıf yanı ayrıntı; Hi3D bu adımı açık ve ücretsiz bir araca çeviriyor. Ürün görselleştirme, oyun varlığı ve 3D baskı için hazırlanan modellerde son rötuşu otomatikleştirebilir."
yekvisual_notu: "Henüz denemedim; bu bilgisayarda çalışmıyor, NVIDIA ekran kartı istiyor. Paylaşımlarda 'fotoğraftan tam 3D model' deniyor ama doğrusu bu değil: kaba bir model gerekiyor ve çıktı yalnız geometri, doku yok. 3D baskıya uygunluk iddiası da şimdilik yalnız şirketin basın bülteninde."
ucretsiz: true
acik_kaynak: true
zorluk: teknik
sirket: Hi3D
model: Hi3D V1.0
etiketler: [hi3d, sparc3d, 3d model, açık kaynak, 3d baskı, hugging face]
kart: acik-kaynak-modeller
kapak: ./hi3d-v1/kapak.webp
kapak_kaynak: "Görsel: Hi3D, model kartındaki karşılaştırma (sağ sütun Hi3D)"
kaynaklar:
  - { ad: "Hugging Face: Hi3Dv1.0", url: "https://huggingface.co/hi3d-official/Hi3Dv1.0" }
  - { ad: "GitHub: Hi3Dv1.0", url: "https://github.com/hi3d-official/Hi3Dv1.0" }
  - { ad: "TechNode Global", url: "https://technode.global/?p=995995" }
  - { ad: "OrcaRouter: 3D baskı iddiasının incelemesi", url: "https://www.orcarouter.ai/blog/hi3d-v1-0-3d-printing-reality-check" }
---

## Neler yeni?

Hi3D, 23 Ekim'de V1.0 sürümünü açık kaynak olarak yayınladı. Model, Sparc3D adıyla bilinen çalışmanın üzerine kurulu ve şirkete göre yaklaşık 2 milyon özenle seçilmiş 3D varlıkla eğitildi.

Ne yaptığını doğru anlamak önemli:

- **Girdi:** Bir referans fotoğraf ve aynı nesnenin kaba bir 3D modeli. Kaba modeli başka bir araçla (örneğin Hunyuan3D-2 mini) üretebiliyorsunuz.
- **Çıktı:** Daha ayrıntılı bir geometri. Doku, malzeme ya da renk üretmiyor; çıktının ölçeği normalize ediliyor.
- **Çözünürlük:** 512, 1024 ve 1536; yüksek çözünürlük birden çok geçişle çalışıyor.

Yani "fotoğraftan tam 3D model" değil; 3D üretim hattının son adımındaki ayrıntılandırma aracı.

## Kimin işine yarar?

Yapay zekâyla 3D model üreten ve sonucu yeterince ayrıntılı bulmayanların: ürün görselleştirme, oyun varlıkları, koleksiyon figürleri, 3D baskı hazırlığı. Açık olduğu için kendi sunucunuzda, verinizi dışarı çıkarmadan çalıştırabilirsiniz.

## Nasıl denenir?

Kod GitHub'da, ağırlıklar Hugging Face'te. Model kartına göre Linux, Python 3.10 ve en az compute capability 8.0 olan bir NVIDIA ekran kartı gerekiyor; CPU ile çalışmıyor, Mac'te de çalışmıyor. Şirketin ölçümleri 96 GB'lık bir NVIDIA H20 ile yapılmış ve daha küçük kartlar için bellek ihtiyacı belirtilmemiş. Kod yazmadan denemek için şirketin sitesinde ücretsiz üretim imkânı var.

## Lisans

Hi3D Open License 1.0: ticari kullanım serbest. Ancak ürününüz aylık 200 bin aktif kullanıcıyı ya da aylık 1 milyon dolar geliri geçerse 60 gün içinde ayrı lisans istemeniz gerekiyor; ticari entegrasyonlarda "Powered by Hi3D 1.0" yazısı zorunlu. Bu, OSI onaylı standart bir açık kaynak lisansı değil.

## Sınırlar

Basın bülteni çıktıların yüzde 90'ının 3D baskı için dilimlenebildiğini söylüyor; bu rakam model kartında ve kodda yok, bağımsız bir inceleme de tekrar üretilemediğini yazıyor. Eğitim kodu yayınlanmadı.
