// Sosyal paylaşım (Open Graph) kartları. Build sırasında her haber, kart ve
// özet için 1200×630 PNG üretir: açık zemin, serif başlık, amber vurgu, sağ üstte güneş.
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

const BG = '#fbfaf8';
const INK = '#1b1a18';
const INK2 = '#45433f';
const MUTED = '#8a867f';
const ACCENT = '#c2540a';

export async function getStaticPaths() {
  const [haberler, kartlar, ozetler, modeller] = await Promise.all([
    getCollection('haberler'),
    getCollection('kartlar'),
    getCollection('ozetler'),
    getCollection('modeller'),
  ]);
  const yollar: { params: { id: string }; props: Veri }[] = [
    { params: { id: 'site' }, props: { baslik: 'Yapay zekâ korkutuyor mu? Deneyince geçiyor.', ustYazi: 'Görsel · Video · Ses · Otomasyon' } },
    { params: { id: 'kart/liste' }, props: { baslik: 'Bu hafta sonu deneyebileceğin şeyler', ustYazi: 'Sıfırdan başlayanlar için' } },
    { params: { id: 'modeller' }, props: { baslik: 'Bu hafta hangi modeli seçmelisin?', ustYazi: 'Şu an en iyi modeller' } },
  ];
  for (const h of haberler) {
    yollar.push({ params: { id: h.id }, props: { baslik: h.data.baslik, ustYazi: kategoriAdi(h.data.kategori), altYazi: h.data.sirket } });
  }
  for (const k of kartlar) {
    yollar.push({ params: { id: `kart/${k.id}` }, props: { baslik: k.data.baslik, ustYazi: `Bilmeniz gerekenler · ${String(k.data.sira).padStart(2, '0')}` } });
  }
  for (const o of ozetler) {
    yollar.push({ params: { id: `ozet/${o.id}` }, props: { baslik: o.data.baslik, ustYazi: 'Haftalık özet' } });
  }
  for (const m of modeller) {
    yollar.push({ params: { id: `modeller/${m.id}` }, props: { baslik: `${m.data.ad} için bu hafta hangi modeli seçmelisin?`, ustYazi: 'Şu an en iyi modeller' } });
  }
  return yollar;
}

// Build sırasında import.meta.url dist/ içini gösterir; fontlar proje kökünden okunur.
const fontlar = Promise.all([readFile(path.resolve(process.cwd(), 'src/assets/fonts/Newsreader-500.ttf'))]);

export async function GET({ props }: APIContext) {
  const { baslik, ustYazi, altYazi } = props as Veri;
  const [newsreader] = await fontlar;
  const uzun = baslik.length > 55;

  const svg = await satori(
    {
      type: 'div',
      props: {
        style: {
          width: 1200,
          height: 630,
          display: 'flex',
          flexDirection: 'column',
          padding: '52px 64px 48px',
          background: BG,
          color: INK,
          fontFamily: 'Newsreader',
          position: 'relative',
        },
        children: [
          {
            type: 'div',
            props: {
              style: {
                position: 'absolute',
                right: -140,
                top: -160,
                width: 520,
                height: 520,
                borderRadius: 260,
                background: 'radial-gradient(circle at center, #fff4b0 0%, #ffd43b 26%, #ff9f1c 52%, #ff7a45 68%, rgba(251,250,248,0) 82%)',
                opacity: 0.85,
              },
            },
          },
          {
            type: 'div',
            props: {
              style: { display: 'flex', alignItems: 'center', gap: 4, fontSize: 40, fontWeight: 500 },
              children: [{ type: 'span', props: { children: 'yekvisual' } }, { type: 'span', props: { style: { color: ACCENT }, children: '.' } }],
            },
          },
          {
            type: 'div',
            props: {
              style: { display: 'flex', alignItems: 'center', gap: 14, marginTop: 44, fontSize: 24, color: ACCENT, letterSpacing: 2, textTransform: 'uppercase' },
              children: [{ type: 'div', props: { style: { width: 28, height: 4, background: ACCENT, borderRadius: 2 } } }, ustYazi],
            },
          },
          {
            type: 'div',
            props: {
              style: { fontSize: uzun ? 64 : 80, lineHeight: 1.05, letterSpacing: -1.5, marginTop: 18, display: 'flex', flex: 1, alignItems: 'flex-start', maxWidth: 1000, color: INK },
              children: baslik,
            },
          },
          {
            type: 'div',
            props: {
              style: { display: 'flex', justifyContent: 'space-between', marginTop: 14, fontSize: 24, color: INK2 },
              children: [
                { type: 'div', props: { children: altYazi ?? 'Yapay zekâ ile görsel, video ve içerik üretimi' } },
                { type: 'div', props: { style: { color: MUTED }, children: 'yekvisual.github.io' } },
              ],
            },
          },
        ],
      },
    },
    {
      width: 1200,
      height: 630,
      fonts: [{ name: 'Newsreader', data: newsreader, weight: 500, style: 'normal' }],
    },
  );

  const png = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } }).render().asPng();
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
}
