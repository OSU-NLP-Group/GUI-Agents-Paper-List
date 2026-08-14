export interface SourceAction {
  key: string;
  label: string;
  glyph: string;
  url: string;
}

// Keep this order aligned with the canonical `link` priority in CLAUDE.md.
const SOURCE_DEFINITIONS: Array<Omit<SourceAction, 'url'>> = [
  { key: 'homepage',       label: 'Homepage',   glyph: '🌐' },
  { key: 'arxiv',          label: 'arXiv',      glyph: '📄' },
  { key: 'openreview',     label: 'OpenReview', glyph: '🔍' },
  { key: 'publisher_page', label: 'Publisher',  glyph: '📑' },
  { key: 'code',           label: 'Code',       glyph: '⌨' },
  { key: 'dataset',        label: 'Dataset',    glyph: '🗂' },
];

export function buildSourceActions(
  sources: Record<string, string | undefined>,
  fallbackUrl?: string,
): SourceAction[] {
  const present = SOURCE_DEFINITIONS
    .filter((source) => sources[source.key])
    .map((source) => ({ ...source, url: sources[source.key]! }));

  if (present.length > 0) return present;
  if (fallbackUrl) {
    return [{ key: 'link', label: 'Open paper', glyph: '↗', url: fallbackUrl }];
  }
  return [];
}
