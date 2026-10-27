// Build öncesi: @yekvisual'ın son paylaşımlarını reels-bot deposundaki instagram/son.json'dan
// alır, küçük görselleri public/instagram/ altına indirir, src/data/instagram.json'a yazar.
// Ağ yoksa ya da dosya yoksa mevcut JSON korunur; build hiç durmaz.
import { mkdir, writeFile, readFile } from 'node:fs/promises';
import path from 'node:path';

const KAYNAK = process.env.INSTAGRAM_JSON ?? 'https://raw.githubusercontent.com/yekvisual/reels-bot/main/instagram/son.json';
const KOK = process.cwd();
const hedefJson = path.join(KOK, 'src/data/instagram.json');
const hedefDizin = path.join(KOK, 'public/instagram');

async function calistir() {
  let liste;
  try {
    const r = await fetch(KAYNAK, { signal: AbortSignal.timeout(15000) });
    if (!r.ok) throw new Error(`HTTP ${r.status}`);
    liste = await r.json();
  } catch (e) {
    console.warn(`instagram: liste alınamadı (${e.message}); mevcut veri korunuyor.`);
    return;
  }
  if (!Array.isArray(liste)) return;
  await mkdir(hedefDizin, { recursive: true });
  const sonuc = [];
  for (const o of liste.slice(0, 6)) {
    if (!o.id || !o.permalink) continue;
    const dosya = `${o.id}.jpg`;
    try {
      const gorselUrl = o.yerel ?? `${KAYNAK.replace(/son\.json$/, '')}${dosya}`;
      const r = await fetch(gorselUrl, { signal: AbortSignal.timeout(20000) });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      await writeFile(path.join(hedefDizin, dosya), Buffer.from(await r.arrayBuffer()));
    } catch (e) {
      console.warn(`instagram: ${dosya} indirilemedi (${e.message})`);
      continue;
    }
    sonuc.push({ id: o.id, permalink: o.permalink, baslik: (o.caption ?? '').split('\n')[0].slice(0, 80), tarih: o.timestamp, tip: o.media_type, gorsel: `/instagram/${dosya}` });
  }
  if (sonuc.length) {
    await writeFile(hedefJson, JSON.stringify(sonuc, null, 2));
    console.log(`instagram: ${sonuc.length} paylaşım güncellendi.`);
  }
}

await calistir();
