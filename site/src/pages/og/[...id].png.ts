// Sosyal paylaşım (Open Graph) kartları. Build sırasında her haber, kart ve
// özet için sitenin koyu/neon stilinde 1200×630 PNG üretir.
import type { APIContext } from 'astro';
import { getCollection } from 'astro:content';
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { kategoriAdi, kategoriRenk } from '../../lib/taxonomy';

interface Veri {
  baslik: string;
  ustYazi: string;
  renk: string;
  altYazi?: string;
}

export async function getStaticPaths() {
  const [haberler, kartlar, ozetler] = await Promise.all([
    getCollection('haberler'),
    getCollection('kartlar'),
    getCollection('ozetler'),
  ]);
  const yollar: { params: { id: string }; props: Veri }[] = [
    {
      params: { id: 'site' },
      props: { baslik: 'Yapay zekâyla üretmeyi öğren. Yeni çıkanı kaçırma.', ustYazi: 'yekvisual', renk: '#a78bfa' },
    },
    {
      params: { id: 'kart/liste' },
      props: { baslik: 'Bilmeniz gerekenler', ustYazi: 'Sıfırdan başlayanlar için', renk: '#22d3ee' },
    },
  ];
  for (const h of haberler) {
    yollar.push({
      params: { id: h.id },
      props: {
        baslik: h.data.baslik,
        ustYazi: kategoriAdi(h.data.kategori),
        renk: kategoriRenk(h.data.kategori),
        altYazi: h.data.sirket,
      },
    });
  }
  for (const k of kartlar) {
    yollar.push({
      params: { id: `kart/${k.id}` },
      props: { baslik: k.data.baslik, ustYazi: 'Bilmeniz gerekenler', renk: kategoriRenk(k.data.kategori) },
    });
  }
  for (const o of ozetler) {
    yollar.push({
      params: { id: `ozet/${o.id}` },
      props: { baslik: o.data.baslik, ustYazi: 'Haftalık özet', renk: '#f472b6' },
    });
  }
  return yollar;
}

// Build sırasında import.meta.url dist/ içini gösterir; fontlar proje kökünden okunur.
const fontlar = Promise.all([
  readFile(path.resolve(process.cwd(), 'src/assets/fonts/Syne-800.ttf')),
  readFile(path.resolve(process.cwd(), 'src/assets/fonts/Inter-600.ttf')),
]);

export async function GET({ props }: APIContext) {
  const { baslik, ustYazi, renk, altYazi } = props as Veri;
  const [syne, inter] = await fontlar;
  const uzun = baslik.length > 60;

  const svg = await satori(
    {
      type: 'div',
      props: {
        style: {
          width: 1200,
          height: 630,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          padding: 64,
          background: 'linear-gradient(160deg, #15152a 0%, #07070c 100%)',
          color: '#fff',
          fontFamily: 'Inter',
          position: 'relative',
        },
        children: [
          {
            type: 'div',
            props: {
              style: {
                position: 'absolute',
                top: -200,
                right: -150,
                width: 700,
                height: 700,
                borderRadius: 9999,
                background: renk,
                opacity: 0.35,
                filter: 'blur(120px)',
              },
            },
          },
          {
            type: 'div',
            props: {
              style: {
                position: 'absolute',
                bottom: -250,
                left: -100,
                width: 600,
                height: 600,
                borderRadius: 9999,
                background: '#a78bfa',
                opacity: 0.22,
                filter: 'blur(120px)',
              },
            },
          },
          {
            type: 'div',
            props: {
              style: { display: 'flex', alignItems: 'center', gap: 16, fontSize: 26, fontWeight: 600, color: renk, letterSpacing: 2, textTransform: 'uppercase' },
              children: [
                { type: 'div', props: { style: { width: 14, height: 14, borderRadius: 4, background: renk } } },
                ustYazi,
              ],
            },
          },
          {
            type: 'div',
            props: {
              style: {
                fontFamily: 'Syne',
                fontWeight: 800,
                fontSize: uzun ? 56 : 68,
                lineHeight: 1.08,
                letterSpacing: -1.5,
                maxWidth: 1000,
                display: 'flex',
              },
              children: baslik,
            },
          },
          {
            type: 'div',
            props: {
              style: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: 28 },
              children: [
                {
                  type: 'div',
                  props: {
                    style: { fontFamily: 'Syne', fontWeight: 800, fontSize: 36, letterSpacing: -1, display: 'flex' },
                    children: [
                      { type: 'span', props: { children: 'yek' } },
                      { type: 'span', props: { style: { color: renk }, children: 'visual' } },
                    ],
                  },
                },
                { type: 'div', props: { style: { color: 'rgba(255,255,255,.6)' }, children: altYazi ?? 'yekvisual.github.io' } },
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
        { name: 'Syne', data: syne, weight: 800, style: 'normal' },
        { name: 'Inter', data: inter, weight: 600, style: 'normal' },
      ],
    },
  );

  const png = new Resvg(svg, { fitTo: { mode: 'width', value: 1200 } }).render().asPng();
  return new Response(new Uint8Array(png), { headers: { 'Content-Type': 'image/png' } });
}
