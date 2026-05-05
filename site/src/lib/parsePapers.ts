import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

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
  sourceLine: number;      // 1-based line number in source markdown
  relation: string | null; // present on adjacent papers
}

const MONTHS = [
  'january', 'february', 'march', 'april', 'may', 'june',
  'july', 'august', 'september', 'october', 'november', 'december',
];

function lastDayOfMonth(y: number, mZeroBased: number): number {
  return new Date(y, mZeroBased + 1, 0).getDate();
}

function parseDate(raw: string): {
  iso: string;
  year: number;
  month: number;
  monthOnly: boolean;
  display: string;
} {
  const s = raw.trim();
  const monthOnly = /^([A-Za-z]+)\s+(\d{4})$/.exec(s);
  if (monthOnly) {
    const monthName = monthOnly[1].toLowerCase();
    const idx = MONTHS.indexOf(monthName);
    if (idx >= 0) {
      const year = parseInt(monthOnly[2], 10);
      const day = lastDayOfMonth(year, idx);
      const iso = `${year}-${String(idx + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
      const display = `${monthName.charAt(0).toUpperCase() + monthName.slice(1)} ${year}`;
      return { iso, year, month: idx + 1, monthOnly: true, display };
    }
  }
  const full = /^([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})$/.exec(s);
  if (full) {
    const monthName = full[1].toLowerCase();
    const idx = MONTHS.indexOf(monthName);
    if (idx >= 0) {
      const day = parseInt(full[2], 10);
      const year = parseInt(full[3], 10);
      const iso = `${year}-${String(idx + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
      const display = `${monthName.charAt(0).toUpperCase() + monthName.slice(1)} ${day}, ${year}`;
      return { iso, year, month: idx + 1, monthOnly: false, display };
    }
  }
  const isoMatch = /^(\d{4})-(\d{1,2})-(\d{1,2})$/.exec(s);
  if (isoMatch) {
    const year = parseInt(isoMatch[1], 10);
    const monthIdx = parseInt(isoMatch[2], 10) - 1;
    const day = parseInt(isoMatch[3], 10);
    const monthName = MONTHS[monthIdx] ?? 'january';
    const iso = `${year}-${String(monthIdx + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
    const display = `${monthName.charAt(0).toUpperCase() + monthName.slice(1)} ${day}, ${year}`;
    return { iso, year, month: monthIdx + 1, monthOnly: false, display };
  }
  const yearMatch = /\b(20\d{2})\b/.exec(s);
  if (yearMatch) {
    const year = parseInt(yearMatch[1], 10);
    return { iso: `${year}-12-31`, year, month: 12, monthOnly: false, display: s };
  }
  return { iso: '0000-01-01', year: 0, month: 0, monthOnly: false, display: s };
}

function splitCsvList(s: string): string[] {
  return s.split(',').map((x) => x.trim()).filter((x) => x.length > 0);
}

function parseKeywords(s: string): string[] {
  return s
    .split(',')
    .map((kw) => kw.trim().replace(/^\[|\]$/g, '').trim())
    .filter((kw) => kw.length > 0);
}

function parseEnv(s: string): string[] {
  // e.g. "[Web]" or "[Desktop], [Mobile]"
  const m = s.match(/\[(.*?)\]/g);
  if (!m) return [];
  return m.map((x) => x.slice(1, -1).trim()).filter(Boolean);
}

function slugify(s: string): string {
  return s
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
}

function arxivIdFromLink(link: string): string | null {
  const m = /arxiv\.org\/(?:abs|pdf|html)\/(\d{4}\.\d{4,5})/i.exec(link);
  return m ? m[1] : null;
}

// Title line: "- [<title>](<link>)"
const TITLE_LINE_RE = /^- \[(.*?)\]\((.*?)\)\s*$/;
// Field line: "    - <emoji> <Field>: <value>" OR plain authors line "    - <text>"
const INDENT_LINE_RE = /^ {2,}- (.*)$/;

interface FieldMap {
  authors?: string;
  institutions?: string;
  date?: string;
  publisher?: string;
  env?: string;
  key?: string;
  tldr?: string;
  relation?: string;
}

function classifyField(raw: string): { kind: keyof FieldMap | null; value: string } {
  const trimmed = raw.replace(/ /g, ' ').trimStart();
  // Each field is "<emoji or text>: <value>" — try labels in order
  const labels: Array<[keyof FieldMap, RegExp]> = [
    ['institutions', /^🏛️?\s*Institutions:\s*(.*)$/u],
    ['date',         /^📅\s*Date:\s*(.*)$/u],
    ['publisher',    /^📑\s*Publisher:\s*(.*)$/u],
    ['env',          /^💻\s*Env:\s*(.*)$/u],
    ['key',          /^🔑\s*Key:\s*(.*)$/u],
    ['tldr',         /^📖\s*TLDR:\s*(.*)$/su],
    ['relation',     /^📌\s*Relation:\s*(.*)$/u],
  ];
  for (const [k, re] of labels) {
    const m = re.exec(trimmed);
    if (m) return { kind: k, value: m[1].trim() };
  }
  return { kind: null, value: trimmed };
}

export function parsePapersMd(
  markdown: string,
  source: 'canonical' | 'adjacent',
): Paper[] {
  const lines = markdown.split('\n');
  const out: Paper[] = [];
  const seenSlugs = new Set<string>();
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const titleMatch = TITLE_LINE_RE.exec(line);
    if (!titleMatch) { i++; continue; }
    const titleStartLine = i + 1; // 1-based
    const title = titleMatch[1].trim();
    const link = titleMatch[2].trim();
    i++;
    const fields: FieldMap = {};
    let firstSubLine = true;
    while (i < lines.length) {
      const sub = lines[i];
      // blank line ends entry
      if (sub.trim() === '') break;
      // next title line ends entry
      if (TITLE_LINE_RE.test(sub)) break;
      const im = INDENT_LINE_RE.exec(sub);
      if (!im) break;
      const inner = im[1];
      const cls = classifyField(inner);
      if (cls.kind) {
        // For TLDR, keep consuming subsequent indented continuation lines if any.
        if (cls.kind === 'tldr') {
          let buf = cls.value;
          let j = i + 1;
          while (j < lines.length) {
            const next = lines[j];
            if (next.trim() === '') break;
            if (TITLE_LINE_RE.test(next)) break;
            if (INDENT_LINE_RE.test(next)) {
              // a new subfield begins; stop
              const innerNext = INDENT_LINE_RE.exec(next)![1];
              if (classifyField(innerNext).kind !== null) break;
            }
            // otherwise append
            buf += ' ' + next.trim();
            j++;
          }
          fields.tldr = buf;
          i = j - 1;
        } else {
          fields[cls.kind] = cls.value;
        }
      } else if (firstSubLine && !fields.authors) {
        fields.authors = inner.trim();
      }
      firstSubLine = false;
      i++;
    }

    // Build a Paper (skip if no title)
    if (!title) continue;
    const dateInfo = parseDate(fields.date ?? '');
    const arxivId = arxivIdFromLink(link);
    let baseSlug = arxivId ? `arxiv-${arxivId.replace('.', '-')}` : slugify(title);
    if (!baseSlug) baseSlug = `paper-${out.length}`;
    let slug = baseSlug;
    let dedup = 1;
    while (seenSlugs.has(slug)) {
      dedup += 1;
      slug = `${baseSlug}-${dedup}`;
    }
    seenSlugs.add(slug);

    out.push({
      slug,
      title,
      link,
      authors: splitCsvList(fields.authors ?? ''),
      institutions: splitCsvList(fields.institutions ?? ''),
      date: dateInfo.display,
      dateISO: dateInfo.iso,
      year: dateInfo.year,
      month: dateInfo.month,
      monthOnly: dateInfo.monthOnly,
      publisher: (fields.publisher ?? '').trim(),
      envs: parseEnv(fields.env ?? ''),
      keywords: parseKeywords(fields.key ?? ''),
      tldr: (fields.tldr ?? '').trim(),
      arxivId,
      source,
      sourceLine: titleStartLine,
      relation: fields.relation?.trim() ?? null,
    });
  }
  out.sort((a, b) => (a.dateISO < b.dateISO ? 1 : a.dateISO > b.dateISO ? -1 : 0));
  return out;
}

let _cache: { canonical: Paper[]; adjacent: Paper[] } | null = null;
export function loadAllPapers(): { canonical: Paper[]; adjacent: Paper[] } {
  if (_cache) return _cache;
  const repoRoot = path.resolve(__dirname, '..', '..', '..');
  const canonicalPath = path.join(repoRoot, 'ALL_PAPERS.md');
  const adjacentPath = path.join(repoRoot, 'ADJACENT_PAPERS.md');
  const canonical = parsePapersMd(fs.readFileSync(canonicalPath, 'utf8'), 'canonical');
  const adjacent = fs.existsSync(adjacentPath)
    ? parsePapersMd(fs.readFileSync(adjacentPath, 'utf8'), 'adjacent')
    : [];
  _cache = { canonical, adjacent };
  return _cache;
}

export function repoFileUrl(p: Paper): string {
  const file = p.source === 'adjacent' ? 'ADJACENT_PAPERS.md' : 'ALL_PAPERS.md';
  return `https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List/blob/main/${file}#L${p.sourceLine}`;
}
