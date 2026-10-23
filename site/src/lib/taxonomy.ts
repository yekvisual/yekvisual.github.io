// Kategori ve etiket sözlüğü. Collector (Python) ile aynı anahtarlar kullanılır;
// yeni kategori eklerken sources.yaml ve collector/ai.py'yi de güncelleyin.
export const KATEGORILER: Record<string, { ad: string; renk: string; aciklama: string }> = {
  gorsel: { ad: 'Görsel', renk: '#f472b6', aciklama: 'Görsel üretme ve düzenleme modelleri' },
  video: { ad: 'Video', renk: '#a78bfa', aciklama: 'Video üretme, düzenleme ve animasyon' },
  ses: { ad: 'Ses & Müzik', renk: '#34d399', aciklama: 'Seslendirme, müzik ve ses efektleri' },
  '3d': { ad: '3D', renk: '#fb923c', aciklama: '3D model, sahne ve doku üretimi' },
  araclar: { ad: 'Araçlar', renk: '#22d3ee', aciklama: 'Uygulamalar, eklentiler ve servisler' },
  'acik-kaynak': { ad: 'Açık Kaynak', renk: '#facc15', aciklama: 'Kendi bilgisayarında çalışan modeller' },
  otomasyon: { ad: 'Otomasyon', renk: '#60a5fa', aciklama: 'İş akışı, bot ve ajan otomasyonları' },
  arastirma: { ad: 'Araştırma', renk: '#c084fc', aciklama: 'Makaleler ve yeni teknikler' },
};

export const ZORLUKLAR: Record<string, { ad: string; aciklama: string }> = {
  yeni: { ad: 'Yeni başlayan', aciklama: 'Teknik bilgi gerekmez' },
  orta: { ad: 'Orta', aciklama: 'Biraz kurcalamak gerekir' },
  teknik: { ad: 'Teknik', aciklama: 'Kod veya kurulum ister' },
};

export function kategoriAdi(id: string) {
  return KATEGORILER[id]?.ad ?? id;
}
export function kategoriRenk(id: string) {
  return KATEGORILER[id]?.renk ?? '#94a3b8';
}
export function zorlukAdi(id: string) {
  return ZORLUKLAR[id]?.ad ?? id;
}
