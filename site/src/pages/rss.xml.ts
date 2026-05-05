import rss from '@astrojs/rss';
import { loadAllPapers } from '../lib/parsePapers';
import { SITE_DESCRIPTION, SITE_TITLE } from '../lib/site';

export async function GET(context: { site: URL | undefined }) {
  const { canonical } = loadAllPapers();
  const recent = canonical.slice(0, 60);
  const base = (import.meta as any).env.BASE_URL.replace(/\/$/, '');
  const origin = (context.site ?? new URL('https://osu-nlp-group.github.io')).toString().replace(/\/$/, '');
  const siteWithBase = new URL(base + '/', origin + '/');
  return rss({
    title: SITE_TITLE,
    description: SITE_DESCRIPTION,
    site: siteWithBase,
    items: recent.map((p) => ({
      title: p.title,
      link: `${origin}${base}/papers/${p.slug}/`,
      description: p.tldr || `${p.publisher} — ${p.authors.slice(0, 4).join(', ')}`,
      pubDate: new Date(p.dateISO),
      categories: [...p.envs, ...p.keywords.slice(0, 6)],
    })),
    customData: '<language>en</language>',
  });
}
