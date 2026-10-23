export const SITE = {
  ad: 'yekvisual',
  slogan: 'Yapay zekâ ile görsel, video ve içerik üretimi. Sıfırdan başlayanlar için.',
  aciklama:
    'Yeni çıkan görsel, video ve ses modelleri; ücretsiz araçlar; Claude ile otomasyon. Türkçe, sade ve güncel.',
  url: 'https://yekvisual.github.io',
  instagram: 'https://instagram.com/yekvisual',
  instagramKullanici: '@yekvisual',
  github: 'https://github.com/yekvisual/yekvisual.github.io',
  // Buttondown benzeri bülten servisinin form adresi. Faz 5'te doldurulacak.
  bultenFormUrl: '',
};

export function tarihTR(d: Date) {
  return new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' }).format(d);
}

export function tarihKisa(d: Date) {
  return new Intl.DateTimeFormat('tr-TR', { day: 'numeric', month: 'short' }).format(d);
}

export function haberYolu(id: string) {
  return `/gundem/${id}/`;
}

export function kartYolu(id: string) {
  return `/bilmeniz-gerekenler/${id}/`;
}
