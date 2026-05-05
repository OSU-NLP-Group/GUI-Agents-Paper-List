import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import solid from '@astrojs/solid-js';
import sitemap from '@astrojs/sitemap';

const SITE_URL = process.env.SITE_URL ?? 'https://OSU-NLP-Group.github.io';
const BASE = process.env.BASE_PATH ?? '/GUI-Agents-Paper-List';

export default defineConfig({
  site: SITE_URL,
  base: BASE,
  trailingSlash: 'ignore',
  integrations: [
    tailwind({ applyBaseStyles: false }),
    solid(),
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      filter: (page) =>
        !page.includes('/404') && !page.endsWith('rss.xml') && !page.endsWith('rss.xml/'),
      serialize(item) {
        if (!item || !item.url) return undefined;
        if (/\/papers\/?$/.test(item.url)) item.priority = 0.9;
        else if (/\/(stats|adjacent|about)\/?$/.test(item.url)) item.priority = 0.7;
        else if (/\/papers\//.test(item.url)) item.priority = 0.6;
        else item.priority = 1.0;
        return item;
      },
    }),
  ],
  build: {
    format: 'directory',
  },
  vite: {
    ssr: {
      noExternal: ['echarts'],
    },
  },
});
