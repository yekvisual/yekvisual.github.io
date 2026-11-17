export const SITE = {
  ad: 'YEK Lab',
  slogan: 'Yapay zekâ ile görsel, video ve içerik üretimi: gündem, model sıralaması, iş akışları.',
  aciklama:
    'Yeni çıkan görsel, video ve ses modelleri; düzenli güncellenen model sıralaması; prodüksiyon ekipleri için yapay zekâ iş akışları. Sade ve güncel.',
  url: import.meta.env.SITE_URL || 'https://yekvisual.github.io',
  alanAdi: 'yeklab.com.tr',
  kurucu: 'Yunus Emre Kaplan',
  instagram: 'https://instagram.com/yekvisual',
  instagramKullanici: '@yekvisual',
  x: 'https://x.com/yekvisual',
  xKullanici: '@yekvisual',
  eposta: 'iletisim@yeklab.com.tr',
  github: 'https://github.com/yekvisual/yekvisual.github.io',
  // Buttondown bülten kullanıcı adı (buttondown.com/<ad>). Form bu adrese gönderir;
  // haftalık gönderim için NEWSLETTER_API_KEY secret'ı gerekir.
  bultenKullanici: '', // Buttondown kullanıcı adı girilince form ve Cumartesi gönderimi açılır
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

// Haberleri sitede yayınlandığı güne göre (yeniden eskiye) sıralar; aynı gün içinde duyuru tarihine bakar.
export function yayinSirasi<T extends { data: { tarih: Date; yayin?: Date } }>(a: T, b: T) {
  const ya = (a.data.yayin ?? a.data.tarih).valueOf(), yb = (b.data.yayin ?? b.data.tarih).valueOf();
  return yb - ya || b.data.tarih.valueOf() - a.data.tarih.valueOf();
}
