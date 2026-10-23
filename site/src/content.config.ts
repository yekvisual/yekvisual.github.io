import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { KATEGORILER, ZORLUKLAR } from './lib/taxonomy';

const kategori = z.enum(Object.keys(KATEGORILER) as [string, ...string[]]);
const zorluk = z.enum(Object.keys(ZORLUKLAR) as [string, ...string[]]);

const kaynak = z.object({ ad: z.string(), url: z.string().url() });

// Haber ve denemelerde kullanılan medya. `src` göreli dosya yolu (görsel/video)
// ya da YouTube linki olabilir.
const medya = z.object({
  tip: z.enum(['gorsel', 'video', 'youtube']),
  src: z.string(),
  alt: z.string().default(''),
  kaynak: z.string().optional(),
});

const haberler = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../content/haberler' }),
  schema: ({ image }) =>
    z.object({
      baslik: z.string(),
      tarih: z.coerce.date(),
      kategori,
      puan: z.number().int().min(0).max(5),
      ozet: z.string(),
      neden_onemli: z.string().optional(),
      yekvisual_notu: z.string().optional(),
      ucretsiz: z.boolean().nullable().default(null),
      acik_kaynak: z.boolean().nullable().default(null),
      zorluk: zorluk.default('yeni'),
      sirket: z.string().optional(),
      model: z.string().optional(),
      etiketler: z.array(z.string()).default([]),
      kart: z.string().optional(),
      kapak: image().optional(),
      kapak_kaynak: z.string().optional(),
      medya: z.array(medya).default([]),
      kaynaklar: z.array(kaynak).default([]),
      denemeler: z.array(medya).default([]),
      ornek: z.boolean().default(false),
    }),
});

const kartlar = defineCollection({
  loader: glob({ pattern: '*.md', base: '../content/kartlar' }),
  schema: ({ image }) =>
    z.object({
    baslik: z.string(),
    ozet: z.string(),
    ikon: z.string(),
    sira: z.number().int(),
    zorluk,
    kategori,
    araclar: z.array(z.string()).default([]),
    etiketler: z.array(z.string()).default([]),
    gorsel: image().optional(),
  }),
});

const araclar = defineCollection({
  loader: glob({ pattern: '*.yaml', base: '../content/araclar' }),
  schema: z.object({
    ad: z.string(),
    url: z.string().url(),
    aciklama: z.string(),
    kategori,
    ucretsiz: z.boolean().nullable().default(null),
    acik_kaynak: z.boolean().nullable().default(null),
    zorluk,
    eklenme: z.coerce.date(),
    etiketler: z.array(z.string()).default([]),
  }),
});

const ozetler = defineCollection({
  loader: glob({ pattern: '*.md', base: '../content/ozetler' }),
  schema: z.object({
    baslik: z.string(),
    tarih: z.coerce.date(),
    ozet: z.string(),
  }),
});

export const collections = { haberler, kartlar, araclar, ozetler };
