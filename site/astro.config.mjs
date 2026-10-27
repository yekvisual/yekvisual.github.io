// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import pagefind from 'astro-pagefind';

export default defineConfig({
  // Alan adı: deploy.yml SITE_URL değişkenini verir (yeklab.com.tr); yerelde ve değişken yokken github.io.
  site: process.env.SITE_URL || 'https://yekvisual.github.io',
  trailingSlash: 'always',
  integrations: [sitemap(), pagefind()],
  vite: {
    // İçerik repo kökündeki content/ klasöründe durur (site/ dışında).
    server: { fs: { allow: ['..'] } },
  },
});
