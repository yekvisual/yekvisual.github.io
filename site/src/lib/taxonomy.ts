// Kategori ve etiket sözlüğü. Collector (Python) ile aynı anahtarlar kullanılır;
// yeni kategori eklerken sources.yaml ve collector/ai.py'yi de güncelleyin.
// `renk`: etiket rengi; `gradyan`: görselsiz haberlerde kapak yedeği.
export const KATEGORILER: Record<string, { ad: string; renk: string; gradyan: string; aciklama: string }> = {
  gorsel: { ad: 'Görsel', renk: '#7a4b00', gradyan: 'linear-gradient(135deg,#1f3a5f 0%,#ff9f1c 58%,#fff4b0 100%)', aciklama: 'Görsel üretme ve düzenleme modelleri' },
  video: { ad: 'Video', renk: '#1f3a5f', gradyan: 'linear-gradient(135deg,#1b1a18 0%,#1f3a5f 55%,#ffd43b 100%)', aciklama: 'Video üretme, düzenleme ve animasyon' },
  ses: { ad: 'Ses & Müzik', renk: '#9b2c4a', gradyan: 'linear-gradient(135deg,#9b2c4a 0%,#ff7a45 60%,#ffefb3 100%)', aciklama: 'Seslendirme, müzik ve ses efektleri' },
  '3d': { ad: '3D', renk: '#5c5954', gradyan: 'linear-gradient(135deg,#45433f 0%,#8a867f 55%,#fff4b0 100%)', aciklama: '3D model, sahne ve doku üretimi' },
  araclar: { ad: 'Araçlar', renk: '#8a3d00', gradyan: 'linear-gradient(135deg,#c2540a 0%,#ff9f1c 55%,#ffefb3 100%)', aciklama: 'Uygulamalar, eklentiler ve servisler' },
  'acik-kaynak': { ad: 'Açık Kaynak', renk: '#1e6b3c', gradyan: 'linear-gradient(135deg,#1e6b3c 0%,#ffd43b 70%,#fff4b0 100%)', aciklama: 'Kendi bilgisayarında çalışan modeller' },
  otomasyon: { ad: 'Otomasyon', renk: '#4a3a86', gradyan: 'linear-gradient(135deg,#4a3a86 0%,#ff7a45 70%,#ffd43b 100%)', aciklama: 'İş akışı ve ajan otomasyonları' },
  arastirma: { ad: 'Araştırma', renk: '#1f3a5f', gradyan: 'linear-gradient(135deg,#1f3a5f 0%,#5b7fb5 55%,#ffefb3 100%)', aciklama: 'Makaleler ve yeni teknikler' },
};

export const ZORLUKLAR: Record<string, { ad: string; aciklama: string }> = {
  yeni: { ad: 'Yeni başlayan', aciklama: 'Teknik bilgi gerekmez' },
  orta: { ad: 'Orta', aciklama: 'Biraz kurcalamak gerekir' },
  teknik: { ad: 'Teknik', aciklama: 'Kod veya kurulum ister' },
};

// Model panelindeki erişim türleri
export const ERISIM: Record<string, { ad: string; sinif: string }> = {
  ucretsiz: { ad: 'Ücretsiz', sinif: 'etiket-ucretsiz' },
  sinirli: { ad: 'Sınırlı ücretsiz', sinif: 'etiket-ucretsiz' },
  deneme: { ad: 'Deneme kredisi', sinif: 'etiket-deneme' },
  ucretli: { ad: 'Ücretli', sinif: 'etiket-ucretli' },
  acik: { ad: 'Açık kaynak', sinif: 'etiket-acik' },
};

export function kategoriAdi(id: string) {
  return KATEGORILER[id]?.ad ?? id;
}
export function kategoriRenk(id: string) {
  return KATEGORILER[id]?.renk ?? '#8a867f';
}
export function kategoriGradyan(id: string) {
  return KATEGORILER[id]?.gradyan ?? KATEGORILER.araclar.gradyan;
}
export function zorlukAdi(id: string) {
  return ZORLUKLAR[id]?.ad ?? id;
}
export function erisimAdi(id: string) {
  return ERISIM[id]?.ad ?? id;
}
export function erisimSinif(id: string) {
  return ERISIM[id]?.sinif ?? 'etiket-ucretli';
}
