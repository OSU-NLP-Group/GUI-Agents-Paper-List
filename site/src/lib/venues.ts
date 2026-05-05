// Canonical-venue list for publisher normalization.
//
// We do NOT try to be clever with generic regex stripping (that's how
// "Findings of ACL 2024", "ICLR 2024 Workshop on Foo", and "LLMAgents
// @ ICLR 2024" all got accidentally collapsed into "ACL 2024" or
// "ICLR 2024"). Instead we keep an explicit list of known venue
// families and only collapse a publisher into a canonical "<family>
// <year>" bucket when the publisher string is *exactly* a known
// family + a year (with optional presentation parenthetical).
// Anything else — workshops, findings tracks, sub-tracks, unknown
// venues — is preserved as-is so it gets its own facet bucket.
//
// To add a venue: append to VENUE_FAMILIES below. Aliases (e.g. NIPS
// → NeurIPS) live in the `aliases` array.

export interface VenueFamily {
  /** Canonical display name. */
  canonical: string;
  /** Strings (case-insensitive equality) treated as this family. */
  aliases?: string[];
  /** True for venues that do not carry a year in their publisher
   *  field (e.g. arXiv, TMLR before yearly issues, …). */
  yearless?: boolean;
  /** True for journal-style venues — used by BibTeX to pick @article. */
  journal?: boolean;
}

export const VENUE_FAMILIES: VenueFamily[] = [
  // Special preprint server
  { canonical: 'arXiv', yearless: true },

  // ML / AI
  { canonical: 'ICLR' },
  { canonical: 'NeurIPS', aliases: ['NIPS'] },
  { canonical: 'ICML' },
  { canonical: 'AAAI' },
  { canonical: 'IJCAI' },
  { canonical: 'AISTATS' },
  { canonical: 'COLT' },
  { canonical: 'COLM' },
  { canonical: 'UAI' },
  { canonical: 'AutoML' },
  { canonical: 'MLSys' },

  // NLP
  { canonical: 'ACL' },
  { canonical: 'EMNLP' },
  { canonical: 'NAACL' },
  { canonical: 'EACL' },
  { canonical: 'COLING' },
  { canonical: 'CoNLL' },
  { canonical: 'AACL' },

  // CV
  { canonical: 'CVPR' },
  { canonical: 'ECCV' },
  { canonical: 'ICCV' },
  { canonical: 'WACV' },
  { canonical: 'BMVC' },
  { canonical: '3DV' },

  // Speech
  { canonical: 'Interspeech' },
  { canonical: 'ICASSP' },
  { canonical: 'ASRU' },
  { canonical: 'SLT' },

  // Robotics
  { canonical: 'CoRL' },
  { canonical: 'RSS' },
  { canonical: 'ICRA' },
  { canonical: 'IROS' },
  { canonical: 'HRI' },

  // HCI
  { canonical: 'CHI' },
  { canonical: 'UIST' },
  { canonical: 'CSCW' },
  { canonical: 'IUI' },
  { canonical: 'MobileHCI' },

  // Web / Data Mining / IR
  { canonical: 'WWW', aliases: ['TheWebConf'] },
  { canonical: 'KDD' },
  { canonical: 'WSDM' },
  { canonical: 'CIKM' },
  { canonical: 'SIGIR' },
  { canonical: 'RecSys' },

  // Multimedia
  { canonical: 'ACM MM', aliases: ['ACMMM', 'ACM Multimedia'] },

  // Systems / Security / SE
  { canonical: 'OSDI' },
  { canonical: 'SOSP' },
  { canonical: 'NSDI' },
  { canonical: 'ATC' },
  { canonical: 'EuroSys' },
  { canonical: 'USENIX Security' },
  { canonical: 'NDSS' },
  { canonical: 'IEEE S&P', aliases: ['Oakland', 'IEEE Symposium on Security and Privacy'] },
  { canonical: 'CCS' },
  { canonical: 'ICSE' },
  { canonical: 'FSE', aliases: ['ESEC/FSE'] },
  { canonical: 'ASE' },
  { canonical: 'ISSTA' },

  // Journals (yearless or year inside; mark journal=true)
  { canonical: 'TMLR', yearless: true, journal: true },
  { canonical: 'JMLR', yearless: true, journal: true },
  { canonical: 'TACL', yearless: true, journal: true },
  { canonical: 'TPAMI', yearless: true, journal: true, aliases: ['IEEE TPAMI'] },
  { canonical: 'TASLP', yearless: true, journal: true },
  { canonical: 'TOCHI', yearless: true, journal: true },
  { canonical: 'CACM', yearless: true, journal: true, aliases: ['Communications of the ACM'] },
  { canonical: 'Nature', yearless: true, journal: true },
  { canonical: 'Science', yearless: true, journal: true },
  { canonical: 'PNAS', yearless: true, journal: true },
];

const ALIAS_TO_CANONICAL = new Map<string, VenueFamily>();
for (const v of VENUE_FAMILIES) {
  ALIAS_TO_CANONICAL.set(v.canonical.toLowerCase(), v);
  for (const a of v.aliases ?? []) ALIAS_TO_CANONICAL.set(a.toLowerCase(), v);
}

/** Strip a trailing presentation tag like "(Poster)", "(Oral)",
 *  "(Spotlight)", "(Highlight)" — these never change which venue
 *  bucket a paper belongs to. We also strip "(Findings)" because the
 *  Findings track is normally surfaced via a "Findings of …" prefix
 *  rather than a parenthetical. */
function stripPresentation(s: string): string {
  return s.replace(/\s*\((?:Poster|Oral|Spotlight|Highlight|Findings)\)\s*$/i, '').trim();
}

/** Look up a venue family by exact (case-insensitive) head string,
 *  e.g. "ICLR", "NIPS", "ACM Multimedia". Returns null when not in
 *  the maintained list. */
export function lookupVenueFamily(head: string): VenueFamily | null {
  return ALIAS_TO_CANONICAL.get(head.trim().toLowerCase()) ?? null;
}

/**
 * Normalize a paper publisher string for facet / chart bucketing.
 *
 * The function only collapses a string into a canonical bucket when
 * we are *confident* it's the main track of a known venue. Anything
 * else — workshops, sub-tracks, unknown venues — is preserved as-is
 * so it shows up under its own facet entry. This is intentional: the
 * cost of being conservative is a slightly longer facet list; the
 * cost of being clever was, e.g., merging "LLMAgents @ ICLR 2024"
 * into "ICLR 2024".
 *
 * Rules (in order):
 *   1. Empty / arXiv / arxiv → "arXiv"
 *   2. "<family-alias> <year>"            → "<canonical> <year>"
 *      (presentation parentheticals are stripped first)
 *   3. "Findings of <family-alias> <year>" → "Findings of <canonical> <year>"
 *   4. yearless journals (TMLR, JMLR, …)  → canonical
 *   5. anything else                       → original (trimmed)
 */
export function normalizePublisher(raw: string | null | undefined): string {
  const trimmed = (raw ?? '').trim();
  if (!trimmed) return '';

  if (/^arxiv$/i.test(trimmed)) return 'arXiv';

  const stripped = stripPresentation(trimmed);
  if (!stripped) return trimmed;

  // "<head> <year>"
  const m = /^(.+?)\s+(19|20)(\d{2})$/.exec(stripped);
  if (m) {
    const head = m[1].trim();
    const year = m[2] + m[3];
    // 3. "Findings of X 2024"
    const fm = /^Findings of\s+(.+)$/i.exec(head);
    if (fm) {
      const inner = fm[1].trim();
      const fam = lookupVenueFamily(inner);
      return `Findings of ${fam ? fam.canonical : inner} ${year}`;
    }
    // 2. exact family match
    const fam = lookupVenueFamily(head);
    if (fam && !fam.yearless) return `${fam.canonical} ${year}`;
    // not a known main-track venue — keep original (workshop / track / etc.)
    return stripped;
  }

  // 4. yearless journals / preprints (e.g. "TMLR")
  const fam = lookupVenueFamily(stripped);
  if (fam && fam.yearless) return fam.canonical;

  // 5. fall through
  return stripped;
}

/** Variant used in BibTeX `journal` / `booktitle` / nothing logic. */
export function bibtexVenueKind(raw: string): 'misc' | 'article' | 'inproceedings' {
  const norm = normalizePublisher(raw);
  if (!norm || /^arxiv$/i.test(norm)) return 'misc';
  // strip year suffix to look up the family for the journal-flag
  const m = /^(.+?)\s+(19|20)\d{2}$/.exec(norm);
  const head = m ? m[1].trim() : norm;
  // Findings of X 2024 → look up X
  const inner = /^Findings of\s+(.+)$/i.exec(head)?.[1]?.trim() ?? head;
  const fam = lookupVenueFamily(inner);
  if (fam?.journal) return 'article';
  return 'inproceedings';
}
