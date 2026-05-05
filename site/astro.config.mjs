import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import solid from '@astrojs/solid-js';

const SITE_URL = process.env.SITE_URL ?? 'https://OSU-NLP-Group.github.io';
const BASE = process.env.BASE_PATH ?? '/GUI-Agents-Paper-List';

export default defineConfig({
  site: SITE_URL,
  base: BASE,
  trailingSlash: 'ignore',
  integrations: [
    tailwind({ applyBaseStyles: false }),
    solid(),
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
