export const SITE = {
  ad: 'YEK Lab',
  slogan: 'Yapay zekâ ile görsel, video ve içerik üretimi: gündem, model sıralaması, iş akışları.',
  aciklama:
    'Yeni çıkan görsel, video ve ses modelleri; her Pazar güncellenen model sıralaması; prodüksiyon ekipleri için yapay zekâ iş akışları. Türkçe, sade, güncel.',
  url: import.meta.env.SITE_URL || 'https://yekvisual.github.io',
  alanAdi: 'yeklab.com.tr',
  kurucu: 'Yunus Emre Kaplan',
  // Danışmanlık ve konuşma davetleri için e-posta; boşsa yalnızca Instagram gösterilir.
  iletisimEposta: '',
  instagram: 'https://instagram.com/yekvisual',
  instagramKullanici: '@yekvisual',
  github: 'https://github.com/yekvisual/yekvisual.github.io',
  // Buttondown bülten kullanıcı adı (buttondown.com/<ad>). Form bu adrese gönderir;
  // haftalık gönderim için NEWSLETTER_API_KEY secret'ı gerekir.
  bultenKullanici: 'yekvisual',
  get bultenFormUrl() {
    return this.bultenKullanici ? `https://buttondown.com/api/emails/embed-subscribe/${this.bultenKullanici}` : '';
  },
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
