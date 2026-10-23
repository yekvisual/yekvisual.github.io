import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';
import { SITE, haberYolu } from '../lib/site';
import { kategoriAdi } from '../lib/taxonomy';

export async function GET(context: APIContext) {
  const haberler = (await getCollection('haberler')).sort((a, b) => b.data.tarih.valueOf() - a.data.tarih.valueOf());
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
