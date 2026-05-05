import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as yaml from 'js-yaml';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// ─────────────────────────────────────────────────────────────────
// Source store: papers.yaml + adjacent.yaml in the repo root.
// (The legacy ALL_PAPERS.md / ADJACENT_PAPERS.md mirrors were
// retired; everything reads YAML directly.)
// ─────────────────────────────────────────────────────────────────

export interface PaperSources {
  arxiv?: string;
  openreview?: string;
  publisher_page?: string;
  homepage?: string;
  code?: string;
  dataset?: string;
  // Future-proof for ad-hoc keys.
  [k: string]: string | undefined;
}

export interface Paper {
  slug: string;
  title: string;
  link: string;
  authors: string[];
  institutions: string[];
  date: string;            // canonical display string
  dateISO: string;         // ISO YYYY-MM-DD (last day of month if month-only)
  year: number;
  month: number;           // 1-12
  monthOnly: boolean;
  publisher: string;
  envs: string[];          // [] for adjacent papers
  keywords: string[];
  tldr: string;
  arxivId: string | null;
  source: 'canonical' | 'adjacent';
  /** 1-based line in the source YAML — used for "edit on GitHub" links. */
  sourceLine: number;
  relation: string | null; // present on adjacent papers
  bibtex: string | null;
  bibtexConfirmed: boolean;
  sources: PaperSources;
}

interface RawEntry {
  title?: unknown;
  link?: unknown;
  authors?: unknown;
  institutions?: unknown;
  date?: unknown;
  publisher?: unknown;
  envs?: unknown;
  keywords?: unknown;
  tldr?: unknown;
  relation?: unknown;
  arxiv_id?: unknown;
  bibtex?: unknown;
  bibtex_confirmed?: unknown;
  sources?: unknown;
}

const MONTHS = [
  'january', 'february', 'march', 'april', 'may', 'june',
  'july', 'august', 'september', 'october', 'november', 'december',
];

function lastDayOfMonth(y: number, mZeroBased: number): number {
  return new Date(y, mZeroBased + 1, 0).getDate();
}

/** Expand a YAML date string into the metadata the site needs.
 *
 * Accepted forms:
 *   "YYYY-MM-DD"    full date, day known
 *   "YYYY-MM"       month known, day unknown   → monthOnly = true
 *   "YYYY"          year only                  → yearOnly  = true
 *   ""              missing                    → missing   = true
 *   "Month DD, YYYY"  legacy display passthrough
 *
 * For sorting/histogram we still produce an `iso` placeholder for
 * partial dates: "YYYY-MM-31" / "YYYY-12-31". The flags let the UI
 * render "March 2024" / "2024" / "Date unknown" appropriately.
 */
function expandDate(raw: string): {
  iso: string;
  year: number;
  month: number;
  monthOnly: boolean;
  yearOnly: boolean;
  missing: boolean;
  display: string;
} {
  const s = (raw ?? '').trim();
  // Empty / missing
  if (!s) {
    return { iso: '', year: 0, month: 0, monthOnly: false, yearOnly: false, missing: true, display: 'Date unknown' };
  }
  // ISO YYYY-MM-DD
  let m = /^(\d{4})-(\d{1,2})-(\d{1,2})$/.exec(s);
  if (m) {
    const year = parseInt(m[1], 10);
    const monthIdx = parseInt(m[2], 10) - 1;
    const day = parseInt(m[3], 10);
    const monthName = MONTHS[monthIdx] ?? 'january';
    return {
      iso: `${year}-${String(monthIdx + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`,
      year, month: monthIdx + 1,
      monthOnly: false, yearOnly: false, missing: false,
      display: `${monthName.charAt(0).toUpperCase() + monthName.slice(1)} ${day}, ${year}`,
    };
  }
  // ISO YYYY-MM
  m = /^(\d{4})-(\d{1,2})$/.exec(s);
  if (m) {
    const year = parseInt(m[1], 10);
    const monthIdx = parseInt(m[2], 10) - 1;
    const day = lastDayOfMonth(year, monthIdx);
    const monthName = MONTHS[monthIdx] ?? 'january';
    return {
      iso: `${year}-${String(monthIdx + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`,
      year, month: monthIdx + 1,
      monthOnly: true, yearOnly: false, missing: false,
      display: `${monthName.charAt(0).toUpperCase() + monthName.slice(1)} ${year}`,
    };
  }
  // Year-only "YYYY"
  m = /^(\d{4})$/.exec(s);
  if (m) {
    const y = parseInt(m[1], 10);
    return {
      iso: `${y}-12-31`, year: y, month: 12,
      monthOnly: false, yearOnly: true, missing: false,
      display: `${y}`,
    };
  }
  // Month DD, YYYY (legacy display string passthrough)
  m = /^([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})$/.exec(s);
  if (m) {
    const idx = MONTHS.indexOf(m[1].toLowerCase());
    if (idx >= 0) {
      const day = parseInt(m[2], 10);
      const year = parseInt(m[3], 10);
      return {
        iso: `${year}-${String(idx + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`,
        year, month: idx + 1,
        monthOnly: false, yearOnly: false, missing: false,
        display: s,
      };
    }
  }
  // Anything else — treat as missing rather than guessing.
  return { iso: '', year: 0, month: 0, monthOnly: false, yearOnly: false, missing: true, display: 'Date unknown' };
}

function arrayOfStrings(v: unknown): string[] {
  if (!v) return [];
  if (Array.isArray(v)) return v.map((x) => String(x).trim()).filter(Boolean);
  if (typeof v === 'string') {
    return v.split(',').map((x) => x.trim()).filter(Boolean);
  }
  return [];
}

function extractArxivId(link: string): string | null {
  const m = /arxiv\.org\/(?:abs|pdf|html)\/(\d{4}\.\d{4,5})/i.exec(link);
  return m ? m[1] : null;
}

function slugFromTitle(title: string): string {
  return title
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
}

/** Best-effort line numbers for "edit on GitHub" links into the YAML.
 *  We scan the raw text for "- title: <…>" lines in the same order
 *  the parser consumed them. */
function buildLineIndex(rawYaml: string): number[] {
  const lines: number[] = [];
  const re = /^- title:/gm;
  let m: RegExpExecArray | null;
  while ((m = re.exec(rawYaml)) !== null) {
    let line = 1;
    for (let i = 0; i < m.index; i++) if (rawYaml.charCodeAt(i) === 10) line++;
    lines.push(line);
  }
  return lines;
}

export function parsePapersYaml(
  rawYaml: string,
  source: 'canonical' | 'adjacent',
): Paper[] {
  const docs = (yaml.load(rawYaml) ?? []) as RawEntry[];
  if (!Array.isArray(docs)) return [];
  const lineIndex = buildLineIndex(rawYaml);
  const seenSlugs = new Set<string>();
  const out: Paper[] = [];
  docs.forEach((entry, i) => {
    if (!entry || typeof entry !== 'object') return;
    const title = String(entry.title ?? '').trim();
    if (!title) return;
    const link = String(entry.link ?? '').trim();
    const authors = arrayOfStrings(entry.authors);
    const institutions = arrayOfStrings(entry.institutions);
    const dateInfo = expandDate(String(entry.date ?? ''));
    const publisher = String(entry.publisher ?? '').trim();
    const envs = arrayOfStrings(entry.envs);
    const keywords = arrayOfStrings(entry.keywords);
    const tldr = String(entry.tldr ?? '').trim();
    const arxivId = (typeof entry.arxiv_id === 'string' && entry.arxiv_id) || extractArxivId(link);
    const bibtex = typeof entry.bibtex === 'string' ? (entry.bibtex as string).trim() : null;
    const bibtexConfirmed = entry.bibtex_confirmed === true;
    const sourcesRaw = (entry.sources && typeof entry.sources === 'object') ? entry.sources as Record<string, unknown> : {};
    const sources: PaperSources = {};
    for (const [k, v] of Object.entries(sourcesRaw)) {
      if (typeof v === 'string' && v.trim()) sources[k] = v.trim();
    }
    if (arxivId && !sources.arxiv) sources.arxiv = `https://arxiv.org/abs/${arxivId}`;

    let baseSlug = arxivId ? `arxiv-${arxivId.replace('.', '-')}` : slugFromTitle(title);
    if (!baseSlug) baseSlug = `paper-${out.length}`;
    let slug = baseSlug;
    let dedup = 1;
    while (seenSlugs.has(slug)) { dedup++; slug = `${baseSlug}-${dedup}`; }
    seenSlugs.add(slug);

    out.push({
      slug, title, link,
      authors, institutions,
      date: dateInfo.display,
      dateISO: dateInfo.iso,
      year: dateInfo.year,
      month: dateInfo.month,
      monthOnly: dateInfo.monthOnly,
      publisher, envs, keywords, tldr,
      arxivId, source,
      sourceLine: lineIndex[i] ?? 1,
      relation: typeof entry.relation === 'string' ? entry.relation : null,
      bibtex,
      bibtexConfirmed,
      sources,
    });
  });
  out.sort((a, b) => (a.dateISO < b.dateISO ? 1 : a.dateISO > b.dateISO ? -1 : 0));
  return out;
}

let _cache: { canonical: Paper[]; adjacent: Paper[] } | null = null;
export function loadAllPapers(): { canonical: Paper[]; adjacent: Paper[] } {
  if (_cache) return _cache;
  const repoRoot = path.resolve(__dirname, '..', '..', '..');
  const canonicalPath = path.join(repoRoot, 'papers.yaml');
  const adjacentPath = path.join(repoRoot, 'adjacent.yaml');
  const canonical = parsePapersYaml(fs.readFileSync(canonicalPath, 'utf8'), 'canonical');
  const adjacent = fs.existsSync(adjacentPath)
    ? parsePapersYaml(fs.readFileSync(adjacentPath, 'utf8'), 'adjacent')
    : [];
  _cache = { canonical, adjacent };
  return _cache;
}

export function repoFileUrl(p: Paper): string {
  const file = p.source === 'adjacent' ? 'adjacent.yaml' : 'papers.yaml';
  return `https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List/blob/main/${file}#L${p.sourceLine}`;
}
