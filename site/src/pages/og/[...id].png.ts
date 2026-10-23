// Sosyal paylaşım (Open Graph) kartları. Build sırasında her haber, kart ve
// özet için gazete stilinde (kâğıt zemin, mürekkep, turuncu çizgi) 1200×630 PNG üretir.
import type { APIContext } from 'astro';
import { getCollection } from 'astro:content';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { kategoriAdi } from '../../lib/taxonomy';

interface Veri {
  baslik: string;
  ustYazi: string;
  altYazi?: string;
}

const PAPER = '#d9d2c8';
const INK = '#1d1d1b';
const ACCENT = '#c03f13';

export async function getStaticPaths() {
  const [haberler, kartlar, ozetler] = await Promise.all([
    getCollection('haberler'),
    getCollection('kartlar'),
    getCollection('ozetler'),
  ]);
  const yollar: { params: { id: string }; props: Veri }[] = [
    { params: { id: 'site' }, props: { baslik: 'Yapay zekâyla üretmeyi öğren. Yeni çıkanı kaçırma.', ustYazi: 'Yapay zekâ ile üretim · Türkçe' } },
    { params: { id: 'kart/liste' }, props: { baslik: 'Bilmeniz gerekenler', ustYazi: 'Sıfırdan başlayanlar için' } },
  ];
  for (const h of haberler) {
    yollar.push({ params: { id: h.id }, props: { baslik: h.data.baslik, ustYazi: kategoriAdi(h.data.kategori), altYazi: h.data.sirket } });
  }
  for (const k of kartlar) {
    yollar.push({ params: { id: `kart/${k.id}` }, props: { baslik: k.data.baslik, ustYazi: `Bilmeniz gerekenler · ${String(k.data.sira).padStart(2, '0')}` } });
  }
  for (const o of ozetler) {
    yollar.push({ params: { id: `ozet/${o.id}` }, props: { baslik: o.data.baslik, ustYazi: 'Pazar eki · Haftalık özet' } });
  }
  return yollar;
}

// Build sırasında import.meta.url dist/ içini gösterir; fontlar proje kökünden okunur.
const fontlar = Promise.all([
  readFile(path.resolve(process.cwd(), 'src/assets/fonts/InstrumentSerif-400.ttf')),
  readFile(path.resolve(process.cwd(), 'src/assets/fonts/Newsreader-500.ttf')),
  readFile(path.resolve(process.cwd(), 'src/assets/fonts/GrenzeGotisch-700.ttf')),
]);

export async function GET({ props }: APIContext) {
  const { baslik, ustYazi, altYazi } = props as Veri;
  const [instrument, newsreader, grenze] = await fontlar;
  const uzun = baslik.length > 55;

  const cizgi = (kalin = 1) => ({ type: 'div', props: { style: { height: kalin, background: INK, width: '100%' } } });

  const svg = await satori(
    {
      type: 'div',
      props: {
        style: {
          width: 1200,
          height: 630,
          display: 'flex',
          flexDirection: 'column',
          padding: '44px 64px 48px',
          background: PAPER,
          color: INK,
          fontFamily: 'Newsreader',
        },
        children: [
          {
            type: 'div',
            props: {
              style: { display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', fontSize: 22, letterSpacing: 2, textTransform: 'uppercase', fontFamily: 'Instrument Serif' },
              children: [
                { type: 'div', props: { children: 'Türkiye' } },
                { type: 'div', props: { style: { fontFamily: 'Grenze Gotisch', fontSize: 64, letterSpacing: 0, textTransform: 'none' }, children: 'yekvisual' } },
                { type: 'div', props: { children: 'yekvisual.github.io' } },
              ],
            },
          },
          { type: 'div', props: { style: { display: 'flex', flexDirection: 'column', gap: 3, marginTop: 14 }, children: [cizgi(2), cizgi(1)] } },
          {
            type: 'div',
            props: {
              style: { display: 'flex', alignItems: 'center', gap: 14, marginTop: 34, fontSize: 24, letterSpacing: 3, textTransform: 'uppercase', fontFamily: 'Instrument Serif', color: ACCENT },
              children: [{ type: 'div', props: { style: { width: 36, height: 4, background: ACCENT } } }, ustYazi],
            },
          },
          {
            type: 'div',
            props: {
              style: { fontFamily: 'Instrument Serif', fontSize: uzun ? 70 : 86, lineHeight: 0.98, letterSpacing: -1, marginTop: 18, display: 'flex', flex: 1, alignItems: 'flex-start', maxWidth: 1060 },
              children: baslik,
            },
          },
          cizgi(1),
          {
            type: 'div',
            props: {
              style: { display: 'flex', justifyContent: 'space-between', marginTop: 14, fontSize: 24, fontStyle: 'italic' },
              children: [
                { type: 'div', props: { children: altYazi ?? 'Yapay zekâ ile görsel, video ve içerik üretimi' } },
                { type: 'div', props: { style: { fontFamily: 'Instrument Serif', textTransform: 'uppercase', letterSpacing: 2, fontStyle: 'normal' }, children: 'Sıfırdan başlayanlar için' } },
              ],
            },
          },
        ],
      },
    },
    {
      width: 1200,
      height: 630,
      fonts: [
        { name: 'Instrument Serif', data: instrument, weight: 400, style: 'normal' },
        { name: 'Newsreader', data: newsreader, weight: 500, style: 'normal' },
        { name: 'Grenze Gotisch', data: grenze, weight: 700, style: 'normal' },
      ],
    },
  );

  const png = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } }).render().asPng();
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
}
