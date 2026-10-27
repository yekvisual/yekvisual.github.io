// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import pagefind from 'astro-pagefind';

export default defineConfig({
  site: 'https://yeklab.com.tr',
  trailingSlash: 'always',
  integrations: [sitemap(), pagefind()],
  vite: {
    // İçerik repo kökündeki content/ klasöründe durur (site/ dışında).
    server: { fs: { allow: ['..'] } },
  },
});
