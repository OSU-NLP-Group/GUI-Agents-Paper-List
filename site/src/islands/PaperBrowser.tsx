/** @jsxImportSource solid-js */
import { createEffect, createMemo, createSignal, For, Show, onMount, onCleanup, untrack } from 'solid-js';
import MiniSearch from 'minisearch';

export interface BrowserPaper {
  slug: string;
  title: string;
  link: string;
  authors: string[];
  institutions: string[];
  date: string;
  dateISO: string;
  year: number;
  publisher: string;
  envs: string[];
  keywords: string[];
  tldr: string;
  arxivId: string | null;
  source: 'canonical' | 'adjacent';
  sourceLine: number;
}

interface Props {
  papers: BrowserPaper[];
  basePath: string;
  repoBlobUrl: string;
}

const ENV_ICON: Record<string, string> = {
  Web: '🌐',
  Mobile: '📱',
  Desktop: '🖥️',
  'General GUI': '🖼️',
};

type ChipMode = 'AND' | 'OR';

function uniqueCount<T extends string | number>(items: T[]): Map<T, number> {
  const m = new Map<T, number>();
  for (const it of items) m.set(it, (m.get(it) ?? 0) + 1);
  return m;
}

// Collapse presentation/track variants of the same venue for facet purposes.
// Keeps the canonical "Venue Year" bucket and drops:
//   - parenthetical presentation tags: (Poster), (Oral), (Spotlight), (Highlight), (Workshop), …
//   - leading "Findings of " prefix on ACL/EMNLP/NAACL findings tracks
//   - " Workshop" / " Track" / " Datasets and Benchmarks Track" tails (kept canonical to ACL/NeurIPS year)
function normalizePublisher(raw: string): string {
  let s = raw.trim();
  if (!s) return s;
  // strip trailing "(Poster)" / "(Oral)" / "(Spotlight)" / "(Highlight)" etc.
  s = s.replace(/\s*\([^)]*\)\s*$/g, '').trim();
  // drop "Findings of " prefix
  s = s.replace(/^Findings of\s+/i, '').trim();
  // collapse "ACL 2024 Workshop on X" / "NeurIPS 2024 Datasets and Benchmarks Track" → "ACL 2024" / "NeurIPS 2024"
  s = s.replace(/\s+(Workshop|Track|Datasets and Benchmarks Track|Findings)\b.*$/i, '').trim();
  return s;
}

function readUrlState(): {
  q: string;
  envs: Set<string>;
  keys: Set<string>;
  authors: Set<string>;
  institutions: Set<string>;
  publishers: Set<string>;
  yearFrom: number | null;
  yearTo: number | null;
  sort: 'date-desc' | 'date-asc' | 'title';
  keyMode: ChipMode;
  includeAdjacent: boolean;
} {
  const url = new URL(window.location.href);
  const ps = url.searchParams;
  const csv = (k: string) =>
    new Set((ps.getAll(k).flatMap((v) => v.split(',')).map((v) => v.trim()).filter(Boolean)));
  const num = (k: string) => {
    const v = ps.get(k);
    if (!v) return null;
    const n = parseInt(v, 10);
    return Number.isFinite(n) ? n : null;
  };
  return {
    q: ps.get('q') ?? '',
    envs: csv('env'),
    keys: csv('key'),
    authors: csv('author'),
    institutions: csv('inst'),
    publishers: csv('pub'),
    yearFrom: num('from'),
    yearTo: num('to'),
    sort: (ps.get('sort') as any) ?? 'date-desc',
    keyMode: (ps.get('keyMode') as ChipMode) ?? 'AND',
    includeAdjacent: ps.get('adj') === '1',
  };
}

function writeUrlState(state: ReturnType<typeof readUrlState>) {
  const url = new URL(window.location.href);
  const ps = url.searchParams;
  const setOrDelete = (k: string, v: string) => {
    if (v) ps.set(k, v);
    else ps.delete(k);
  };
  const join = (s: Set<string>) => Array.from(s).join(',');
  setOrDelete('q', state.q);
  setOrDelete('env', join(state.envs));
  setOrDelete('key', join(state.keys));
  setOrDelete('author', join(state.authors));
  setOrDelete('inst', join(state.institutions));
  setOrDelete('pub', join(state.publishers));
  setOrDelete('from', state.yearFrom != null ? String(state.yearFrom) : '');
  setOrDelete('to', state.yearTo != null ? String(state.yearTo) : '');
  setOrDelete('sort', state.sort === 'date-desc' ? '' : state.sort);
  setOrDelete('keyMode', state.keyMode === 'AND' ? '' : state.keyMode);
  setOrDelete('adj', state.includeAdjacent ? '1' : '');
  history.replaceState(null, '', url.toString());
}

export default function PaperBrowser(props: Props) {
  const initial = typeof window !== 'undefined' ? readUrlState() : {
    q: '', envs: new Set<string>(), keys: new Set<string>(),
    authors: new Set<string>(), institutions: new Set<string>(),
    publishers: new Set<string>(),
    yearFrom: null, yearTo: null,
    sort: 'date-desc' as const, keyMode: 'AND' as ChipMode,
    includeAdjacent: false,
  };

  const [q, setQ] = createSignal(initial.q);
  const [envs, setEnvs] = createSignal<Set<string>>(initial.envs);
  const [keys, setKeys] = createSignal<Set<string>>(initial.keys);
  const [authors, setAuthors] = createSignal<Set<string>>(initial.authors);
  const [institutions, setInstitutions] = createSignal<Set<string>>(initial.institutions);
  const [publishers, setPublishers] = createSignal<Set<string>>(initial.publishers);
  const [yearFrom, setYearFrom] = createSignal<number | null>(initial.yearFrom);
  const [yearTo, setYearTo] = createSignal<number | null>(initial.yearTo);
  const [sort, setSort] = createSignal<'date-desc' | 'date-asc' | 'title'>(initial.sort);
  const [keyMode, setKeyMode] = createSignal<ChipMode>(initial.keyMode);
  const [includeAdjacent, setIncludeAdjacent] = createSignal<boolean>(initial.includeAdjacent);

  const [keyFacetSearch, setKeyFacetSearch] = createSignal('');
  const [authorFacetSearch, setAuthorFacetSearch] = createSignal('');
  const [instFacetSearch, setInstFacetSearch] = createSignal('');
  const [pubFacetSearch, setPubFacetSearch] = createSignal('');

  const PAGE_SIZE = 60;
  const [showLimit, setShowLimit] = createSignal(PAGE_SIZE);
  const [filtersOpen, setFiltersOpen] = createSignal(false);
  let sentinelEl: HTMLDivElement | undefined;
  let observer: IntersectionObserver | undefined;

  // Index search corpus
  const ms = new MiniSearch<BrowserPaper>({
    fields: ['title', 'authorsStr', 'institutionsStr', 'tldr', 'keywordsStr', 'publisher'],
    storeFields: ['slug'],
    searchOptions: {
      boost: { title: 3, keywordsStr: 2, authorsStr: 1.4 },
      fuzzy: 0.18,
      prefix: true,
      combineWith: 'AND',
    },
    extractField: (doc, field) => {
      switch (field) {
        case 'authorsStr': return doc.authors.join(' ');
        case 'institutionsStr': return doc.institutions.join(' ');
        case 'keywordsStr': return doc.keywords.join(' ');
        default: return (doc as any)[field] ?? '';
      }
    },
    idField: 'slug',
  });
  ms.addAll(props.papers);

  // sync URL
  let urlSyncTimer: number | null = null;
  const persist = () => {
    if (urlSyncTimer != null) window.clearTimeout(urlSyncTimer);
    urlSyncTimer = window.setTimeout(() => {
      writeUrlState({
        q: q(), envs: envs(), keys: keys(), authors: authors(),
        institutions: institutions(), publishers: publishers(),
        yearFrom: yearFrom(), yearTo: yearTo(), sort: sort(),
        keyMode: keyMode(), includeAdjacent: includeAdjacent(),
      });
    }, 200);
  };

  const candidates = createMemo(() => {
    const adj = includeAdjacent();
    return adj ? props.papers : props.papers.filter((p) => p.source === 'canonical');
  });

  const searchHits = createMemo<Set<string> | null>(() => {
    const query = q().trim();
    if (!query) return null;
    const results = ms.search(query, { fuzzy: 0.18, prefix: true, combineWith: 'AND' });
    return new Set(results.map((r) => String(r.id)));
  });

  const filtered = createMemo<BrowserPaper[]>(() => {
    const envSel = envs();
    const keySel = keys();
    const authorSel = authors();
    const instSel = institutions();
    const pubSel = publishers();
    const yf = yearFrom();
    const yt = yearTo();
    const hits = searchHits();
    const adjOn = includeAdjacent();
    const km = keyMode();
    persist();
    let out = candidates().filter((p) => {
      if (hits && !hits.has(p.slug)) return false;
      if (!adjOn && p.source !== 'canonical') return false;
      if (envSel.size > 0 && !p.envs.some((e) => envSel.has(e))) return false;
      if (keySel.size > 0) {
        if (km === 'AND') {
          for (const k of keySel) if (!p.keywords.includes(k)) return false;
        } else {
          if (!p.keywords.some((k) => keySel.has(k))) return false;
        }
      }
      if (authorSel.size > 0 && !p.authors.some((a) => authorSel.has(a))) return false;
      if (instSel.size > 0 && !p.institutions.some((i) => instSel.has(i))) return false;
      if (pubSel.size > 0 && !pubSel.has(normalizePublisher(p.publisher))) return false;
      if (yf != null && p.year < yf) return false;
      if (yt != null && p.year > yt) return false;
      return true;
    });

    const s = sort();
    if (s === 'date-asc') out = [...out].sort((a, b) => (a.dateISO < b.dateISO ? -1 : 1));
    else if (s === 'title') out = [...out].sort((a, b) => a.title.localeCompare(b.title));
    // date-desc is the default order
    return out;
  });

  // facet counts derived from current candidate set (excluding adjacent toggle if off)
  const allEnvs = createMemo(() => {
    const c = uniqueCount(candidates().flatMap((p) => p.envs));
    return Array.from(c.entries()).sort((a, b) => b[1] - a[1]);
  });
  const allKeys = createMemo(() => {
    const c = uniqueCount(candidates().flatMap((p) => p.keywords));
    return Array.from(c.entries()).sort((a, b) => b[1] - a[1]);
  });
  const allAuthors = createMemo(() => {
    const c = uniqueCount(candidates().flatMap((p) => p.authors));
    return Array.from(c.entries()).sort((a, b) => b[1] - a[1]);
  });
  const allInstitutions = createMemo(() => {
    const c = uniqueCount(candidates().flatMap((p) => p.institutions));
    return Array.from(c.entries()).sort((a, b) => b[1] - a[1]);
  });
  const allPublishers = createMemo(() => {
    const c = uniqueCount(candidates().map((p) => normalizePublisher(p.publisher)).filter(Boolean));
    return Array.from(c.entries()).sort((a, b) => b[1] - a[1]);
  });
  const yearBounds = createMemo(() => {
    const ys = candidates().map((p) => p.year).filter((y) => y > 0);
    if (ys.length === 0) return [2018, new Date().getFullYear()] as [number, number];
    return [Math.min(...ys), Math.max(...ys)] as [number, number];
  });

  const toggle = (s: () => Set<string>, setS: (v: Set<string>) => void, val: string) => {
    const next = new Set(s());
    if (next.has(val)) next.delete(val); else next.add(val);
    setS(next);
    setShowLimit(PAGE_SIZE);
  };
  const clearAll = () => {
    setQ(''); setEnvs(new Set<string>()); setKeys(new Set<string>()); setAuthors(new Set<string>());
    setInstitutions(new Set<string>()); setPublishers(new Set<string>());
    setYearFrom(null); setYearTo(null); setSort('date-desc');
    setKeyMode('AND'); setShowLimit(PAGE_SIZE);
  };

  const activeFilterCount = createMemo(() =>
    envs().size + keys().size + authors().size + institutions().size + publishers().size +
    (yearFrom() != null ? 1 : 0) + (yearTo() != null ? 1 : 0)
  );

  // Reset the visible-page limit whenever the active filter set / sort changes.
  // (Year / institution / publisher / etc. all flow through this.)
  createEffect(() => {
    // Track each filter signal explicitly.
    envs(); keys(); authors(); institutions(); publishers();
    yearFrom(); yearTo(); sort(); includeAdjacent(); keyMode();
    untrack(() => setShowLimit(PAGE_SIZE));
  });

  // popstate sync (back/forward)
  const onPop = () => {
    const s = readUrlState();
    setQ(s.q); setEnvs(s.envs); setKeys(s.keys); setAuthors(s.authors);
    setInstitutions(s.institutions); setPublishers(s.publishers);
    setYearFrom(s.yearFrom); setYearTo(s.yearTo); setSort(s.sort);
    setKeyMode(s.keyMode); setIncludeAdjacent(s.includeAdjacent);
    setShowLimit(PAGE_SIZE);
  };
  onMount(() => {
    window.addEventListener('popstate', onPop);
    // Infinite-scroll sentinel: when within ~600px of the bottom marker, load
    // the next page. We rebind the observer whenever the sentinel ref changes
    // (Solid creates the element after mount).
    if (typeof IntersectionObserver !== 'undefined' && sentinelEl) {
      observer = new IntersectionObserver(
        (entries) => {
          for (const entry of entries) {
            if (!entry.isIntersecting) continue;
            const total = filtered().length;
            const cur = showLimit();
            if (cur < total) setShowLimit(Math.min(cur + PAGE_SIZE, total));
          }
        },
        { rootMargin: '600px 0px 600px 0px' },
      );
      observer.observe(sentinelEl);
    }
  });
  onCleanup(() => {
    window.removeEventListener('popstate', onPop);
    observer?.disconnect();
  });

  const filterSection = (
    label: string,
    items: () => [string, number][],
    selected: () => Set<string>,
    setSelected: (v: Set<string>) => void,
    facetSearch: () => string,
    setFacetSearch: (v: string) => void,
    showSearch = true,
    cap = 12,
    headerExtra: (() => any) | null = null,
  ) => {
    const [open, setOpen] = createSignal(true);
    const [showAll, setShowAll] = createSignal(false);
    const filteredItems = createMemo(() => {
      const f = facetSearch().trim().toLowerCase();
      const list = f ? items().filter(([k]) => k.toLowerCase().includes(f)) : items();
      // bring selected to top
      const sel = selected();
      return [
        ...list.filter(([k]) => sel.has(k)),
        ...list.filter(([k]) => !sel.has(k)),
      ];
    });
    return (
      <section class="border-b border-paper-300/60 dark:border-ink-600/60 py-3">
        <div class="flex items-center justify-between gap-2">
          <button class="flex-1 flex items-center justify-between text-xs font-semibold uppercase tracking-[0.16em] text-ink-500 dark:text-ink-200 hover:text-ink-700 dark:hover:text-ink-50" onClick={() => setOpen(!open())}>
            <span>{label} <Show when={selected().size > 0}><span class="ml-1 text-accent dark:text-accent-dark normal-case tracking-normal font-medium">· {selected().size}</span></Show></span>
            <span class="text-ink-400 mr-2">{open() ? '−' : '+'}</span>
          </button>
          {headerExtra && headerExtra()}
        </div>
        <Show when={open()}>
          <div class="mt-2.5 space-y-1.5">
            <Show when={showSearch && items().length > cap}>
              <input type="search" placeholder="Filter…" class="input text-xs py-1.5" value={facetSearch()} onInput={(e) => setFacetSearch(e.currentTarget.value)} />
            </Show>
            <ul class="space-y-1 max-h-72 overflow-y-auto pr-1">
              <For each={(showAll() ? filteredItems() : filteredItems().slice(0, cap))}>
                {([name, count]) => (
                  <li>
                    <button
                      class={`w-full flex items-center justify-between gap-2 px-2 py-1 rounded text-sm text-left transition-colors ${
                        selected().has(name)
                          ? 'bg-accent/10 dark:bg-accent-dark/15 text-accent dark:text-accent-dark'
                          : 'hover:bg-paper-200/60 dark:hover:bg-ink-700/40 text-ink-600 dark:text-ink-100'
                      }`}
                      onClick={() => toggle(selected, setSelected, name)}
                    >
                      <span class="truncate flex items-center gap-1.5">
                        <Show when={selected().has(name)}>
                          <svg viewBox="0 0 16 16" width="11" height="11" fill="currentColor" aria-hidden="true"><path d="M13.5 4.5l-7 7-3-3 1-1 2 2 6-6z"/></svg>
                        </Show>
                        {name}
                      </span>
                      <span class="text-xs text-ink-400 shrink-0">{count}</span>
                    </button>
                  </li>
                )}
              </For>
            </ul>
            <Show when={filteredItems().length > cap}>
              <button class="text-xs text-ink-400 hover:text-accent dark:hover:text-accent-dark mt-1" onClick={() => setShowAll(!showAll())}>
                {showAll() ? 'Show fewer' : `Show all ${filteredItems().length}`}
              </button>
            </Show>
          </div>
        </Show>
      </section>
    );
  };

  return (
    <div class="grid grid-cols-1 lg:grid-cols-[18rem_1fr] gap-6">
      {/* Mobile filter toggle */}
      <button
        class="lg:hidden btn-ghost border border-paper-300/80 dark:border-ink-600/60 self-start"
        onClick={() => setFiltersOpen(!filtersOpen())}
      >
        Filters {activeFilterCount() > 0 ? `· ${activeFilterCount()}` : ''} {filtersOpen() ? '▴' : '▾'}
      </button>

      {/* Sidebar */}
      <aside class={`${filtersOpen() ? 'block' : 'hidden lg:block'} lg:sticky lg:top-20 self-start max-h-[calc(100vh-6rem)] overflow-y-auto pr-1`}>
        <div class="flex items-center justify-between pb-2">
          <span class="text-xs font-semibold uppercase tracking-[0.18em] text-ink-400 dark:text-ink-300">Filters</span>
          <Show when={activeFilterCount() > 0 || q()}>
            <button class="text-xs link" onClick={clearAll}>Clear all</button>
          </Show>
        </div>

        {filterSection('Environment', allEnvs as any, envs, setEnvs, () => '', () => {}, false, 8)}
        {filterSection('Keywords', allKeys as any, keys, setKeys, keyFacetSearch, setKeyFacetSearch, true, 12, () => (
          <Show when={keys().size > 1}>
            <button class="text-[10px] uppercase tracking-wider px-1.5 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40" onClick={(e: any) => { e.stopPropagation(); setKeyMode(keyMode() === 'AND' ? 'OR' : 'AND'); }}>{keyMode()}</button>
          </Show>
        ))}
        {filterSection('Author', allAuthors as any, authors, setAuthors, authorFacetSearch, setAuthorFacetSearch)}
        {filterSection('Institution', allInstitutions as any, institutions, setInstitutions, instFacetSearch, setInstFacetSearch)}
        {filterSection('Publisher', allPublishers as any, publishers, setPublishers, pubFacetSearch, setPubFacetSearch)}

        <section class="py-3">
          <div class="text-xs font-semibold uppercase tracking-[0.16em] text-ink-500 dark:text-ink-200 mb-2">Year</div>
          <div class="flex items-center gap-2 text-sm">
            <input type="number" min={yearBounds()[0]} max={yearBounds()[1]} placeholder={String(yearBounds()[0])} value={yearFrom() ?? ''} onInput={(e) => setYearFrom(e.currentTarget.value ? parseInt(e.currentTarget.value, 10) : null)} class="input text-sm py-1.5 w-20" />
            <span class="text-ink-400">–</span>
            <input type="number" min={yearBounds()[0]} max={yearBounds()[1]} placeholder={String(yearBounds()[1])} value={yearTo() ?? ''} onInput={(e) => setYearTo(e.currentTarget.value ? parseInt(e.currentTarget.value, 10) : null)} class="input text-sm py-1.5 w-20" />
          </div>
        </section>

        <section class="py-3">
          <label class="flex items-center gap-2 text-sm text-ink-600 dark:text-ink-100 cursor-pointer">
            <input type="checkbox" checked={includeAdjacent()} onChange={(e) => setIncludeAdjacent(e.currentTarget.checked)} class="rounded border-paper-300 dark:border-ink-600" />
            <span>Include adjacent papers</span>
          </label>
        </section>
      </aside>

      {/* Main */}
      <div>
        <div class="flex flex-wrap items-center gap-3 mb-4">
          <div class="flex-1 min-w-[14rem] relative">
            <input
              type="search"
              placeholder="Search title, authors, TLDR, keywords…"
              class="input pl-9"
              value={q()}
              onInput={(e) => { setQ(e.currentTarget.value); setShowLimit(PAGE_SIZE); }}
            />
            <svg viewBox="0 0 24 24" width="16" height="16" class="absolute left-3 top-1/2 -translate-y-1/2 text-ink-400" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
          </div>
          <select value={sort()} onChange={(e) => setSort(e.currentTarget.value as any)} class="input w-auto py-2">
            <option value="date-desc">Newest first</option>
            <option value="date-asc">Oldest first</option>
            <option value="title">Title (A–Z)</option>
          </select>
          <div class="text-sm text-ink-400 dark:text-ink-300 ml-auto">
            {filtered().length.toLocaleString()} {filtered().length === 1 ? 'paper' : 'papers'}
          </div>
        </div>

        {/* Active filter chips */}
        <Show when={activeFilterCount() > 0}>
          <div class="mb-4 flex flex-wrap gap-1.5">
            <For each={Array.from(envs())}>{(v) => (
              <button class="chip chip-active" onClick={() => toggle(envs, setEnvs, v)}>
                {ENV_ICON[v] ?? '·'} {v} <span class="ml-1">×</span>
              </button>
            )}</For>
            <For each={Array.from(keys())}>{(v) => (
              <button class="chip chip-active" onClick={() => toggle(keys, setKeys, v)}>{v} <span class="ml-1">×</span></button>
            )}</For>
            <For each={Array.from(authors())}>{(v) => (
              <button class="chip chip-active" onClick={() => toggle(authors, setAuthors, v)}>{v} <span class="ml-1">×</span></button>
            )}</For>
            <For each={Array.from(institutions())}>{(v) => (
              <button class="chip chip-active" onClick={() => toggle(institutions, setInstitutions, v)}>{v} <span class="ml-1">×</span></button>
            )}</For>
            <For each={Array.from(publishers())}>{(v) => (
              <button class="chip chip-active" onClick={() => toggle(publishers, setPublishers, v)}>{v} <span class="ml-1">×</span></button>
            )}</For>
          </div>
        </Show>

        <Show when={filtered().length === 0}>
          <div class="surface rounded-lg p-8 text-center">
            <p class="text-ink-500 dark:text-ink-200">No papers match these filters.</p>
            <button class="btn-ghost mt-3" onClick={clearAll}>Clear all filters</button>
          </div>
        </Show>

        <ul class="grid gap-4">
          <For each={filtered().slice(0, showLimit())}>
            {(p) => <li><PaperCardClient paper={p} basePath={props.basePath} repoBlobUrl={props.repoBlobUrl} onChip={(kw) => toggle(keys, setKeys, kw)} /></li>}
          </For>
        </ul>

        {/* Infinite-scroll sentinel + lightweight progress indicator */}
        <div ref={(el) => (sentinelEl = el)} aria-hidden="true" class="h-10"></div>

        <Show when={filtered().length > 0}>
          <Show when={filtered().length > showLimit()} fallback={
            <div class="mt-2 text-center text-xs text-ink-400 dark:text-ink-300">
              All {filtered().length.toLocaleString()} {filtered().length === 1 ? 'paper' : 'papers'} loaded.
            </div>
          }>
            <div class="mt-2 text-center">
              <div class="inline-flex items-center gap-2 text-xs text-ink-400 dark:text-ink-300">
                <span class="inline-block w-3 h-3 rounded-full border-2 border-current border-r-transparent animate-spin"></span>
                <span>Loading more · showing {showLimit().toLocaleString()} of {filtered().length.toLocaleString()}</span>
              </div>
              {/* Manual fallback for when IntersectionObserver isn't available */}
              <noscript>
                <button class="btn-ghost border border-paper-300/80 dark:border-ink-600/60 mt-2" onClick={() => setShowLimit(showLimit() + PAGE_SIZE)}>
                  Show more
                </button>
              </noscript>
            </div>
          </Show>
        </Show>
      </div>
    </div>
  );
}

interface CardProps {
  paper: BrowserPaper;
  basePath: string;
  repoBlobUrl: string;
  onChip: (kw: string) => void;
}

// LaTeX-ready BibTeX. Three cases:
//   1. arXiv-only (no formal venue) → @misc with eprint / archivePrefix /
//      primaryClass; never include booktitle.
//   2. Conference / workshop publication → @inproceedings with normalized
//      booktitle (no "(Poster)" / "(Oral)" / "(Spotlight)" / etc.).
//   3. Journal-like venue (TMLR, JMLR, …) → @article with journal field.
// Title is double-braced so LaTeX preserves capitalization on names like
// "GUI", "OSWorld", "SeeAct".
function bibKey(p: BrowserPaper): string {
  const lastName = (p.authors[0] ?? 'unknown').split(/\s+/).pop()!.toLowerCase().replace(/[^a-z]/g, '') || 'anon';
  const titleWord = p.title.split(/\s+/).find((w) => w.length > 3)?.toLowerCase().replace(/[^a-z0-9]/g, '') ?? 'paper';
  const year = p.year > 0 ? p.year : '';
  return `${lastName}${year}${titleWord}`;
}

function escapeBibValue(s: string): string {
  // BibTeX special chars that are safer escaped inside a brace value.
  return s
    .replace(/\\/g, '\\textbackslash ')
    .replace(/([&%$#_{}])/g, '\\$1')
    .replace(/~/g, '\\~{}')
    .replace(/\^/g, '\\^{}');
}

function normalizeBibVenue(publisher: string): string {
  let v = publisher.trim();
  v = v.replace(/\s*\([^)]*\)\s*$/g, '').trim();          // drop (Poster) etc.
  return v;
}

const JOURNAL_VENUES = /^(TMLR|JMLR|TPAMI|TASLP|TACL|Nature|Science|PNAS|IEEE\s|ACM\s)/i;

function buildBibtex(p: BrowserPaper): string {
  const key = bibKey(p);
  const authors = p.authors.length > 0 ? p.authors.map(escapeBibValue).join(' and ') : 'Unknown';
  const titleEsc = escapeBibValue(p.title);
  const year = p.year > 0 ? String(p.year) : '';

  const venue = normalizeBibVenue(p.publisher || '');
  const isArxivOnly = !venue || /^arxiv$/i.test(venue);
  const isJournal = JOURNAL_VENUES.test(venue);

  const fields: Array<[string, string]> = [];
  fields.push(['title', `{${titleEsc}}`]);
  fields.push(['author', `{${authors}}`]);
  if (year) fields.push(['year', `{${year}}`]);

  if (isArxivOnly && p.arxivId) {
    fields.push(['eprint', `{${p.arxivId}}`]);
    fields.push(['archivePrefix', `{arXiv}`]);
    // primaryClass is a best-guess; we don't have it parsed, so leave omitted.
    fields.push(['url', `{https://arxiv.org/abs/${p.arxivId}}`]);
    return formatBib('@misc', key, fields);
  }
  if (isArxivOnly) {
    fields.push(['howpublished', `{${escapeBibValue(p.publisher || 'Preprint')}}`]);
    fields.push(['url', `{${p.link}}`]);
    return formatBib('@misc', key, fields);
  }
  if (isJournal) {
    fields.push(['journal', `{${escapeBibValue(venue)}}`]);
    if (p.arxivId) fields.push(['eprint', `{${p.arxivId}}`]);
    fields.push(['url', `{${p.link}}`]);
    return formatBib('@article', key, fields);
  }
  // Conference / workshop default
  fields.push(['booktitle', `{${escapeBibValue(venue)}}`]);
  if (p.arxivId) {
    fields.push(['eprint', `{${p.arxivId}}`]);
    fields.push(['archivePrefix', `{arXiv}`]);
  }
  fields.push(['url', `{${p.link}}`]);
  return formatBib('@inproceedings', key, fields);
}

function formatBib(kind: string, key: string, fields: Array<[string, string]>): string {
  const indented = fields.map(([k, v]) => `  ${k} = ${v}`).join(',\n');
  return `${kind}{${key},\n${indented}\n}`;
}
function buildReportUrl(p: BrowserPaper): string {
  const issueBody = [
    `**Paper title:** ${p.title}`,
    `**Paper link:** ${p.link}`,
    `**Source line:** ${p.source === 'adjacent' ? 'ADJACENT_PAPERS.md' : 'ALL_PAPERS.md'}#L${p.sourceLine}`,
    '',
    '### What is incorrect or missing?',
    '<!-- Please describe the issue (e.g., wrong authors, wrong date, wrong publisher, missing keyword, broken link). -->',
    '',
  ].join('\n');
  const params = new URLSearchParams({
    title: `[Metadata] ${p.title}`,
    body: issueBody,
    labels: 'metadata-correction',
    template: 'metadata-correction.yml',
  });
  return `https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List/issues/new?${params.toString()}`;
}

function PaperCardClient(props: CardProps) {
  const p = props.paper;
  const detailHref = `${props.basePath}/papers/${p.slug}`;
  const reportUrl = buildReportUrl(p);
  // Show a separate arXiv button only when the canonical paper link isn't
  // already an arXiv URL — otherwise "Open paper" and "arXiv" go to the same
  // place and the duplicate button is just noise.
  const linkIsArxiv = /arxiv\.org/.test(p.link);
  const showArxiv = !linkIsArxiv && !!p.arxivId;
  const [expanded, setExpanded] = createSignal(false);
  const [bibCopied, setBibCopied] = createSignal(false);

  const visibleAuthors = () => expanded() ? p.authors : p.authors.slice(0, 3);
  const moreAuthors = () => Math.max(0, p.authors.length - 3);
  const visibleInstitutions = () => expanded() ? p.institutions : p.institutions.slice(0, 3);
  const moreInstitutions = () => Math.max(0, p.institutions.length - 3);
  const visibleKeywords = () => expanded() ? p.keywords : p.keywords.slice(0, 8);

  function copyBibtex(e: MouseEvent) {
    e.preventDefault();
    const text = buildBibtex(p);
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        setBibCopied(true);
        setTimeout(() => setBibCopied(false), 1500);
      });
    }
  }

  return (
    <article class={`card p-5 ${p.source === 'adjacent' ? 'opacity-95' : ''} ${expanded() ? 'border-paper-400/80 dark:border-ink-400/40' : ''}`}>
      <div class="flex items-start gap-3">
        <div class="flex-1 min-w-0">
          <h3 class="text-base sm:text-[17px] font-semibold leading-snug text-ink-700 dark:text-ink-50 tracking-[-0.005em]">
            <a href={detailHref} class="hover:text-accent dark:hover:text-accent-dark transition-colors">{p.title}</a>
          </h3>
          <p class="mt-1 text-sm text-ink-500 dark:text-ink-200 break-words">
            {visibleAuthors().join(', ')}
            <Show when={!expanded() && moreAuthors() > 0}>
              <button
                class="ml-1 text-ink-400 dark:text-ink-300 hover:text-accent dark:hover:text-accent-dark"
                onClick={() => setExpanded(true)}
                aria-label="Show all authors"
              >+{moreAuthors()} more</button>
            </Show>
          </p>
        </div>
        <div class="shrink-0 flex items-center gap-2">
          <For each={p.envs}>{(env) => (
            <span class="text-base" title={env} aria-label={env}>{ENV_ICON[env] ?? '🖼️'}</span>
          )}</For>
          <Show when={p.source === 'adjacent'}>
            <span class="text-[10px] uppercase tracking-wider px-1.5 py-0.5 rounded bg-paper-200 dark:bg-ink-700 text-ink-500 dark:text-ink-200 border border-paper-300/60 dark:border-ink-600/60">adj</span>
          </Show>
          <button
            type="button"
            class="ml-1 inline-flex items-center justify-center w-6 h-6 rounded text-ink-400 dark:text-ink-300 hover:text-accent dark:hover:text-accent-dark hover:bg-paper-200/60 dark:hover:bg-ink-700/40"
            onClick={() => setExpanded(!expanded())}
            aria-label={expanded() ? 'Collapse' : 'Expand'}
            aria-expanded={expanded() ? 'true' : 'false'}
          >
            <svg viewBox="0 0 16 16" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class={`transition-transform ${expanded() ? 'rotate-180' : ''}`} aria-hidden="true">
              <path d="M3 6l5 5 5-5"/>
            </svg>
          </button>
        </div>
      </div>

      <p class="mt-2 text-xs text-ink-400 dark:text-ink-300 tabular-nums">
        <span>{p.date}</span>
        <span class="mx-1.5 text-ink-300/60 dark:text-ink-400/60">·</span>
        <span>{p.publisher}</span>
        <Show when={p.institutions.length > 0}>
          <span class="mx-1.5 text-ink-300/60 dark:text-ink-400/60">·</span>
          <span class="text-ink-500 dark:text-ink-200">
            {visibleInstitutions().join(', ')}
            <Show when={!expanded() && moreInstitutions() > 0}>
              <button
                class="ml-1 text-ink-400 dark:text-ink-300 hover:text-accent dark:hover:text-accent-dark"
                onClick={() => setExpanded(true)}
                aria-label="Show all institutions"
              >+{moreInstitutions()}</button>
            </Show>
          </span>
        </Show>
      </p>

      <Show when={p.tldr}>
        <p class={`mt-2.5 text-sm text-ink-600 dark:text-ink-100 leading-relaxed ${expanded() ? '' : 'clamp-3'}`}>{p.tldr}</p>
      </Show>

      <Show when={p.keywords.length > 0}>
        <div class="mt-3 flex flex-wrap gap-1.5">
          <For each={visibleKeywords()}>{(kw) => (
            <button class="chip" onClick={() => props.onChip(kw)}>{kw}</button>
          )}</For>
          <Show when={!expanded() && p.keywords.length > 8}>
            <button
              class="text-xs text-ink-400 dark:text-ink-300 hover:text-accent dark:hover:text-accent-dark"
              onClick={() => setExpanded(true)}
            >+{p.keywords.length - 8} more</button>
          </Show>
        </div>
      </Show>

      <Show when={expanded()}>
        <div class="mt-4 pt-4 border-t border-paper-300/60 dark:border-ink-600/60">
          <div class="flex flex-wrap items-center gap-2 text-xs">
            <a
              class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-md bg-accent text-paper-50 dark:bg-accent-dark dark:text-ink-900 hover:opacity-90 font-medium"
              href={p.link} target="_blank" rel="noopener"
            >
              <span>Open paper</span><span aria-hidden="true">↗</span>
            </a>
            <Show when={showArxiv}>
              <a class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-md border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40" href={`https://arxiv.org/abs/${p.arxivId}`} target="_blank" rel="noopener">arXiv</a>
            </Show>
            <button
              type="button"
              class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-md border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40"
              onClick={copyBibtex}
              aria-label="Copy BibTeX to clipboard"
            >
              <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              <span>{bibCopied() ? 'BibTeX copied' : 'Copy BibTeX'}</span>
            </button>
            <a class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-md border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40" href={reportUrl} target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" width="12" height="12" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg>
              Report issue
            </a>
          </div>
        </div>
      </Show>

      <Show when={!expanded()}>
        <div class="mt-3.5 flex items-center justify-between gap-3 text-xs">
          <button
            class="link font-medium"
            onClick={() => setExpanded(true)}
            type="button"
          >Expand ↓</button>
          <a class="text-ink-400 dark:text-ink-300 hover:text-accent dark:hover:text-accent-dark" href={p.link} target="_blank" rel="noopener">Open ↗</a>
        </div>
      </Show>
    </article>
  );
}
