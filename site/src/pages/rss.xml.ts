import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { SITE, haberYolu, yayinSirasi } from '../lib/site';
import { kategoriAdi } from '../lib/taxonomy';

export async function GET(context: APIContext) {
  const haberler = (await getCollection('haberler')).sort(yayinSirasi);
  return rss({
    title: SITE.ad,
    description: SITE.aciklama,
    site: context.site!,
    items: haberler.map((h) => ({
      title: h.data.baslik,
      pubDate: h.data.tarih,
      description: h.data.ozet,
      link: haberYolu(h.id),
      categories: [kategoriAdi(h.data.kategori), ...h.data.etiketler],
    })),
    customData: '<language>tr-TR</language>',
  });
}
