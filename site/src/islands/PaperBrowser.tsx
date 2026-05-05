/** @jsxImportSource solid-js */
import { createEffect, createMemo, createSignal, For, Show, onMount, onCleanup, untrack } from 'solid-js';
import MiniSearch from 'minisearch';
import { normalizePublisher, bibtexVenueKind } from '../lib/venues';
import { Select, Toggle } from './UiPrimitives';

export interface BrowserPaper {
  slug: string;
  title: string;
  link: string;
  authors: string[];
  institutions: string[];
  date: string;
  dateISO: string;
  year: number;
  month: number;
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
type SortKey = 'date-desc' | 'date-asc' | 'title-asc' | 'title-desc' | 'random' | 'relevance';

// Deterministic PRNG so "Random" shuffle is stable while filters
// don't change. Tiny — no dependency.
function mulberry32(a: number): () => number {
  return function () {
    a = (a + 0x6D2B79F5) | 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function uniqueCount<T extends string | number>(items: T[]): Map<T, number> {
  const m = new Map<T, number>();
  for (const it of items) m.set(it, (m.get(it) ?? 0) + 1);
  return m;
}


// "YYYY-MM" — also accepts a bare "YYYY" for back-compat.
function isValidMonthStr(s: string): boolean {
  return /^\d{4}-(?:0[1-9]|1[0-2])$/.test(s);
}
function coerceMonthStr(raw: string | null): string | null {
  if (!raw) return null;
  const s = raw.trim();
  if (isValidMonthStr(s)) return s;
  if (/^\d{4}$/.test(s)) return `${s}-01`;
  return null;
}

function readUrlState(): {
  q: string;
  envs: Set<string>;
  keys: Set<string>;
  authors: Set<string>;
  institutions: Set<string>;
  publishers: Set<string>;
  fromMonth: string | null;
  toMonth: string | null;
  sort: SortKey;
  keyMode: ChipMode;
  includeAdjacent: boolean;
} {
  const url = new URL(window.location.href);
  const ps = url.searchParams;
  const csv = (k: string) =>
    new Set((ps.getAll(k).flatMap((v) => v.split(',')).map((v) => v.trim()).filter(Boolean)));
  return {
    q: ps.get('q') ?? '',
    envs: csv('env'),
    keys: csv('key'),
    authors: csv('author'),
    institutions: csv('inst'),
    publishers: csv('pub'),
    fromMonth: coerceMonthStr(ps.get('from')),
    toMonth: coerceMonthStr(ps.get('to')),
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
  setOrDelete('from', state.fromMonth ?? '');
  setOrDelete('to', state.toMonth ?? '');
  setOrDelete('sort', state.sort === 'date-desc' ? '' : state.sort);
  setOrDelete('keyMode', state.keyMode === 'AND' ? '' : state.keyMode);
  setOrDelete('adj', state.includeAdjacent ? '1' : '');
  history.replaceState(null, '', url.toString());
}

const MONTH_NAMES = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
function fmtMonth(m: string): string {
  // "YYYY-MM" → "Mon YYYY"
  const mm = /^(\d{4})-(\d{2})$/.exec(m);
  if (!mm) return m;
  const idx = parseInt(mm[2], 10) - 1;
  return `${MONTH_NAMES[idx]} ${mm[1]}`;
}

export default function PaperBrowser(props: Props) {
  const initial = typeof window !== 'undefined' ? readUrlState() : {
    q: '', envs: new Set<string>(), keys: new Set<string>(),
    authors: new Set<string>(), institutions: new Set<string>(),
    publishers: new Set<string>(),
    fromMonth: null as string | null, toMonth: null as string | null,
    sort: 'date-desc' as const, keyMode: 'AND' as ChipMode,
    includeAdjacent: false,
  };

  const [q, setQ] = createSignal(initial.q);
  const [envs, setEnvs] = createSignal<Set<string>>(initial.envs);
  const [keys, setKeys] = createSignal<Set<string>>(initial.keys);
  const [authors, setAuthors] = createSignal<Set<string>>(initial.authors);
  const [institutions, setInstitutions] = createSignal<Set<string>>(initial.institutions);
  const [publishers, setPublishers] = createSignal<Set<string>>(initial.publishers);
  const [fromMonth, setFromMonth] = createSignal<string | null>(initial.fromMonth);
  const [toMonth, setToMonth] = createSignal<string | null>(initial.toMonth);
  const [sort, setSort] = createSignal<SortKey>(initial.sort);
  const [keyMode, setKeyMode] = createSignal<ChipMode>(initial.keyMode);
  const [includeAdjacent, setIncludeAdjacent] = createSignal<boolean>(initial.includeAdjacent);

  const [keyFacetSearch, setKeyFacetSearch] = createSignal('');
  const [authorFacetSearch, setAuthorFacetSearch] = createSignal('');
  const [instFacetSearch, setInstFacetSearch] = createSignal('');
  const [pubFacetSearch, setPubFacetSearch] = createSignal('');
  const [toast, setToast] = createSignal<string | null>(null);
  const showToast = (msg: string) => {
    setToast(msg);
    setTimeout(() => setToast(null), 1800);
  };

  const PAGE_SIZE = 60;
  const [showLimit, setShowLimit] = createSignal(PAGE_SIZE);
  const [filtersOpen, setFiltersOpen] = createSignal(false);
  const [shortcutHelpOpen, setShortcutHelpOpen] = createSignal(false);
  let sentinelEl: HTMLDivElement | undefined;
  let searchInput: HTMLInputElement | undefined;
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
        fromMonth: fromMonth(), toMonth: toMonth(), sort: sort(),
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

  // "YYYY-MM" of a paper, derived from its year+month fields. Falls
  // back to "YYYY-12" for entries with year only.
  const paperMonth = (p: BrowserPaper): string => {
    const y = p.year > 0 ? p.year : 0;
    const m = p.month > 0 ? p.month : 12;
    return `${y}-${String(m).padStart(2, '0')}`;
  };

  const filtered = createMemo<BrowserPaper[]>(() => {
    const envSel = envs();
    const keySel = keys();
    const authorSel = authors();
    const instSel = institutions();
    const pubSel = publishers();
    const fm = fromMonth();
    const tm = toMonth();
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
      if (fm || tm) {
        const pm = paperMonth(p);
        if (fm && pm < fm) return false;
        if (tm && pm > tm) return false;
      }
      return true;
    });

    const s = sort();
    if (s === 'date-asc') {
      out = [...out].sort((a, b) => (a.dateISO < b.dateISO ? -1 : 1));
    } else if (s === 'title-asc') {
      out = [...out].sort((a, b) => a.title.localeCompare(b.title));
    } else if (s === 'title-desc') {
      out = [...out].sort((a, b) => b.title.localeCompare(a.title));
    } else if (s === 'random') {
      // Deterministic shuffle keyed by current filter set so the order
      // is stable across rerenders within the same filter, but changes
      // when the user interacts.
      const seed = (q() + Array.from(envs()).join() + Array.from(keys()).join()).length || 1;
      const r = mulberry32(seed);
      out = [...out].map((x) => [r(), x] as [number, BrowserPaper])
        .sort((a, b) => a[0] - b[0])
        .map(([, x]) => x);
    } else if (s === 'relevance' && hits) {
      // MiniSearch already returns results in descending score order;
      // we filtered to hits but lost the order. Re-rank by score map.
      const scoreMap = new Map<string, number>();
      const ranked = ms.search(q(), { fuzzy: 0.18, prefix: true, combineWith: 'AND' });
      ranked.forEach((r, i) => scoreMap.set(String(r.id), ranked.length - i));
      out = [...out].sort((a, b) => (scoreMap.get(b.slug) ?? 0) - (scoreMap.get(a.slug) ?? 0));
    }
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
  // Month-grain histogram of all candidate papers, used both for the
  // bounds of the date slider and for the inline preview chart.
  const monthHistogram = createMemo<{
    months: string[];                 // sorted "YYYY-MM"
    counts: Record<string, number>;
  }>(() => {
    const counts: Record<string, number> = {};
    for (const p of candidates()) {
      if (p.year <= 0) continue;
      const k = paperMonth(p);
      counts[k] = (counts[k] ?? 0) + 1;
    }
    const months = Object.keys(counts).sort();
    return { months, counts };
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
    setFromMonth(null); setToMonth(null); setSort('date-desc');
    setKeyMode('AND'); setShowLimit(PAGE_SIZE);
  };

  const activeFilterCount = createMemo(() =>
    envs().size + keys().size + authors().size + institutions().size + publishers().size +
    (fromMonth() != null || toMonth() != null ? 1 : 0)
  );

  // Reset the visible-page limit whenever the active filter set / sort changes.
  createEffect(() => {
    envs(); keys(); authors(); institutions(); publishers();
    fromMonth(); toMonth(); sort(); includeAdjacent(); keyMode();
    untrack(() => setShowLimit(PAGE_SIZE));
  });

  // popstate sync (back/forward)
  const onPop = () => {
    const s = readUrlState();
    setQ(s.q); setEnvs(s.envs); setKeys(s.keys); setAuthors(s.authors);
    setInstitutions(s.institutions); setPublishers(s.publishers);
    setFromMonth(s.fromMonth); setToMonth(s.toMonth); setSort(s.sort);
    setKeyMode(s.keyMode); setIncludeAdjacent(s.includeAdjacent);
    setShowLimit(PAGE_SIZE);
  };
  // Keyboard shortcuts
  const onKey = (e: KeyboardEvent) => {
    const target = e.target as HTMLElement | null;
    const inField = !!target && (
      target.tagName === 'INPUT' ||
      target.tagName === 'TEXTAREA' ||
      (target as any).isContentEditable
    );
    if (!inField && e.key === '/' && !e.metaKey && !e.ctrlKey) {
      e.preventDefault();
      searchInput?.focus();
      searchInput?.select();
      return;
    }
    if (e.key === 'Escape') {
      if (shortcutHelpOpen()) { setShortcutHelpOpen(false); return; }
      if (target === searchInput) { (target as HTMLInputElement).blur(); return; }
      if (q() || activeFilterCount() > 0) clearAll();
      return;
    }
    if (!inField && (e.key === '?' || (e.shiftKey && e.key === '/'))) {
      e.preventDefault();
      setShortcutHelpOpen(!shortcutHelpOpen());
      return;
    }
    if (!inField && (e.key === 'j' || e.key === 'k')) {
      e.preventDefault();
      const cards = Array.from(document.querySelectorAll('article.card'));
      if (cards.length === 0) return;
      const focused = document.activeElement?.closest('article.card');
      let idx = focused ? cards.indexOf(focused) : -1;
      idx = e.key === 'j' ? Math.min(idx + 1, cards.length - 1) : Math.max(idx - 1, 0);
      const next = cards[idx] as HTMLElement | undefined;
      if (next) {
        next.scrollIntoView({ behavior: 'smooth', block: 'center' });
        const link = next.querySelector('h3 a') as HTMLElement | null;
        link?.focus();
      }
    }
  };

  onMount(() => {
    window.addEventListener('popstate', onPop);
    window.addEventListener('keydown', onKey);
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
    window.removeEventListener('keydown', onKey);
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
    <div class="grid grid-cols-1 lg:grid-cols-[18rem_1fr] gap-6 relative">
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

        <DateRangeSection
          histogram={monthHistogram()}
          from={fromMonth()}
          to={toMonth()}
          setFrom={setFromMonth}
          setTo={setToMonth}
        />

        <section class="py-4">
          <Toggle
            checked={includeAdjacent()}
            onChange={setIncludeAdjacent}
            label="Include adjacent papers"
            hint="Non-canonical entries that inform GUI research"
          />
        </section>
      </aside>

      {/* Main */}
      <div>
        <div class="flex flex-wrap items-center gap-3 mb-4">
          <div class="flex-1 min-w-[14rem] relative">
            <input
              type="search"
              placeholder="Search title, authors, TLDR, keywords…  ( / )"
              class="input pl-9 pr-9"
              value={q()}
              ref={(el) => (searchInput = el)}
              onInput={(e) => { setQ(e.currentTarget.value); setShowLimit(PAGE_SIZE); }}
            />
            <svg viewBox="0 0 24 24" width="16" height="16" class="absolute left-3 top-1/2 -translate-y-1/2 text-ink-400" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
            <Show when={!q()}>
              <kbd class="hidden sm:inline-block absolute right-3 top-1/2 -translate-y-1/2 px-1.5 py-0.5 text-[10px] font-mono rounded border border-paper-300/80 dark:border-ink-600/60 text-ink-400 dark:text-ink-300 leading-none">/</kbd>
            </Show>
          </div>
          <Select<SortKey>
            ariaLabel="Sort papers"
            value={sort()}
            onChange={setSort}
            options={[
              { value: 'date-desc',  label: 'Newest first' },
              { value: 'date-asc',   label: 'Oldest first' },
              { value: 'title-asc',  label: 'Title  A → Z' },
              { value: 'title-desc', label: 'Title  Z → A' },
              { value: 'random',     label: 'Random' },
              { value: 'relevance',  label: 'Best match', disabled: !q().trim(), hint: q().trim() ? '' : 'type to search' },
            ]}
          />
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
            <Show when={fromMonth() || toMonth()}>
              <button class="chip chip-active" onClick={() => { setFromMonth(null); setToMonth(null); }}>
                {fromMonth() ? fmtMonth(fromMonth()!) : '…'} – {toMonth() ? fmtMonth(toMonth()!) : '…'}
                <span class="ml-1">×</span>
              </button>
            </Show>
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
            {(p) => <li><PaperCardClient paper={p} basePath={props.basePath} repoBlobUrl={props.repoBlobUrl} onChip={(kw) => toggle(keys, setKeys, kw)} onToast={showToast} query={q().trim()} /></li>}
          </For>
          {/* Skeleton placeholders shown while the next page is fetching */}
          <Show when={filtered().length > showLimit()}>
            <For each={Array.from({ length: Math.min(3, filtered().length - showLimit()) })}>
              {() => (
                <li>
                  <article class="card p-5">
                    <div class="flex items-start gap-3">
                      <div class="flex-1 space-y-2">
                        <div class="skeleton h-4 w-3/4"></div>
                        <div class="skeleton h-4 w-1/2"></div>
                        <div class="skeleton h-3 w-1/3 mt-3"></div>
                      </div>
                      <div class="skeleton h-5 w-5 rounded-full"></div>
                    </div>
                    <div class="skeleton h-3 w-full mt-4"></div>
                    <div class="skeleton h-3 w-11/12 mt-2"></div>
                    <div class="skeleton h-3 w-2/3 mt-2"></div>
                    <div class="flex gap-2 mt-4">
                      <div class="skeleton h-5 w-16 rounded-full"></div>
                      <div class="skeleton h-5 w-20 rounded-full"></div>
                      <div class="skeleton h-5 w-14 rounded-full"></div>
                    </div>
                  </article>
                </li>
              )}
            </For>
          </Show>
        </ul>

        {/* Infinite-scroll sentinel + lightweight progress indicator */}
        <div ref={(el) => (sentinelEl = el)} aria-hidden="true" class="h-10"></div>

        <Show when={filtered().length > 0}>
          <Show when={filtered().length > showLimit()} fallback={
            <div class="mt-2 text-center text-xs text-ink-400 dark:text-ink-300">
              All {filtered().length.toLocaleString()} {filtered().length === 1 ? 'paper' : 'papers'} loaded.
            </div>
          }>
            <div class="mt-2 text-center text-xs text-ink-400 dark:text-ink-300">
              <span>Loading more · showing {showLimit().toLocaleString()} of {filtered().length.toLocaleString()}</span>
              <noscript>
                <button class="btn-ghost border border-paper-300/80 dark:border-ink-600/60 mt-2 ml-2" onClick={() => setShowLimit(showLimit() + PAGE_SIZE)}>
                  Show more
                </button>
              </noscript>
            </div>
          </Show>
        </Show>
      </div>

      {/* Global toast portal — single global affordance for cross-card events */}
      <Show when={toast()}>
        <div class="toast" role="status" aria-live="polite">
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M5 12l5 5L20 7"/>
          </svg>
          <span>{toast()}</span>
        </div>
      </Show>

      {/* Keyboard-shortcut cheatsheet (?) */}
      <Show when={shortcutHelpOpen()}>
        <div
          class="fixed inset-0 z-[60] bg-ink-900/40 dark:bg-black/60 backdrop-blur-sm flex items-center justify-center p-4"
          onClick={() => setShortcutHelpOpen(false)}
          role="dialog"
          aria-modal="true"
        >
          <div
            class="surface rounded-lg max-w-md w-full p-6 shadow-2xl"
            onClick={(e: any) => e.stopPropagation()}
          >
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-base font-semibold text-ink-700 dark:text-ink-50">Keyboard shortcuts</h3>
              <button class="text-ink-400 hover:text-ink-600 dark:hover:text-ink-50" onClick={() => setShortcutHelpOpen(false)} aria-label="Close">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>
              </button>
            </div>
            <dl class="grid grid-cols-[auto_1fr] gap-x-6 gap-y-3 text-sm">
              <dt><kbd class="px-1.5 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 text-xs font-mono">/</kbd></dt>
              <dd class="text-ink-600 dark:text-ink-100">Focus search</dd>
              <dt class="flex gap-1"><kbd class="px-1.5 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 text-xs font-mono">j</kbd><kbd class="px-1.5 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 text-xs font-mono">k</kbd></dt>
              <dd class="text-ink-600 dark:text-ink-100">Move between papers</dd>
              <dt><kbd class="px-1.5 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 text-xs font-mono">Esc</kbd></dt>
              <dd class="text-ink-600 dark:text-ink-100">Clear filters &amp; close</dd>
              <dt><kbd class="px-1.5 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 text-xs font-mono">?</kbd></dt>
              <dd class="text-ink-600 dark:text-ink-100">Open this help</dd>
            </dl>
          </div>
        </div>
      </Show>
    </div>
  );
}

// ────────────────────────────────────────────────────────────────────────
// DateRangeSection — month-grain dual-thumb slider with a paper-count
// histogram preview, presets, and live YYYY-MM labels.
// ────────────────────────────────────────────────────────────────────────

interface DateRangeProps {
  histogram: { months: string[]; counts: Record<string, number> };
  from: string | null;
  to: string | null;
  setFrom: (v: string | null) => void;
  setTo: (v: string | null) => void;
}

function monthAddOffset(ym: string, offset: number): string {
  const [y, m] = ym.split('-').map((x) => parseInt(x, 10));
  const total = (y * 12 + (m - 1)) + offset;
  const ny = Math.floor(total / 12);
  const nm = (total % 12 + 12) % 12;
  return `${ny}-${String(nm + 1).padStart(2, '0')}`;
}

function DateRangeSection(props: DateRangeProps) {
  const [open, setOpen] = createSignal(true);

  // axis = months from the candidate set, padded to a full year on each
  // side so the bars don't crowd the very edges of the track.
  const axis = createMemo<string[]>(() => {
    const { months } = props.histogram;
    if (months.length === 0) {
      // fallback: 5 years up to current
      const now = new Date();
      const end = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;
      const out: string[] = [];
      for (let i = 60; i >= 0; i--) out.push(monthAddOffset(end, -i));
      return out;
    }
    const start = months[0];
    const end = months[months.length - 1];
    // span end - start in months
    const [sy, sm] = start.split('-').map((x) => parseInt(x, 10));
    const [ey, em] = end.split('-').map((x) => parseInt(x, 10));
    const span = (ey - sy) * 12 + (em - sm);
    const out: string[] = [];
    for (let i = 0; i <= span; i++) out.push(monthAddOffset(start, i));
    return out;
  });

  const minIdx = 0;
  const maxIdx = () => Math.max(0, axis().length - 1);
  const ymToIdx = (ym: string | null): number => {
    if (!ym) return -1;
    const i = axis().indexOf(ym);
    if (i >= 0) return i;
    // closest within bounds
    if (axis().length === 0) return -1;
    if (ym < axis()[0]) return 0;
    if (ym > axis()[axis().length - 1]) return maxIdx();
    return 0;
  };
  const idxToYm = (idx: number): string | null => {
    if (idx < 0 || idx >= axis().length) return null;
    return axis()[idx];
  };

  const fromIdx = () => {
    const v = ymToIdx(props.from);
    return v < 0 ? minIdx : v;
  };
  const toIdx = () => {
    const v = ymToIdx(props.to);
    return v < 0 ? maxIdx() : v;
  };

  const [hoverIdx, setHoverIdx] = createSignal<number | null>(null);
  let trackEl: HTMLDivElement | undefined;

  const widthPct = (idx: number) => (idx / Math.max(1, maxIdx())) * 100;

  function setFromIdx(idx: number) {
    const clamped = Math.max(minIdx, Math.min(idx, toIdx()));
    const ym = idxToYm(clamped);
    if (clamped === minIdx) props.setFrom(null);
    else props.setFrom(ym);
  }
  function setToIdx(idx: number) {
    const clamped = Math.max(fromIdx(), Math.min(idx, maxIdx()));
    const ym = idxToYm(clamped);
    if (clamped === maxIdx()) props.setTo(null);
    else props.setTo(ym);
  }

  function trackPosToIdx(clientX: number): number {
    if (!trackEl) return 0;
    const rect = trackEl.getBoundingClientRect();
    const ratio = Math.max(0, Math.min(1, (clientX - rect.left) / rect.width));
    return Math.round(ratio * maxIdx());
  }

  // bar heights — log-ish scale (sqrt) so the long tail of low-count
  // early months doesn't collapse to invisible.
  const histBars = createMemo(() => {
    const counts = props.histogram.counts;
    const max = Math.max(1, ...axis().map((m) => counts[m] ?? 0));
    return axis().map((m) => {
      const c = counts[m] ?? 0;
      const h = c === 0 ? 0 : Math.max(8, (Math.sqrt(c / max)) * 100);
      return { m, count: c, h };
    });
  });

  // pointer drag for thumbs
  function startDrag(thumb: 'from' | 'to', e: PointerEvent) {
    e.preventDefault();
    const move = (ev: PointerEvent) => {
      const idx = trackPosToIdx(ev.clientX);
      if (thumb === 'from') setFromIdx(idx);
      else setToIdx(idx);
    };
    const up = () => {
      window.removeEventListener('pointermove', move);
      window.removeEventListener('pointerup', up);
      window.removeEventListener('pointercancel', up);
    };
    window.addEventListener('pointermove', move);
    window.addEventListener('pointerup', up);
    window.addEventListener('pointercancel', up);
  }

  function trackClick(e: MouseEvent) {
    const idx = trackPosToIdx(e.clientX);
    // snap to nearer thumb
    const dFrom = Math.abs(idx - fromIdx());
    const dTo = Math.abs(idx - toIdx());
    if (dFrom <= dTo) setFromIdx(idx);
    else setToIdx(idx);
  }

  function trackKey(thumb: 'from' | 'to', e: KeyboardEvent) {
    let delta = 0;
    if (e.key === 'ArrowLeft') delta = -1;
    else if (e.key === 'ArrowRight') delta = 1;
    else if (e.key === 'PageDown') delta = -12;
    else if (e.key === 'PageUp') delta = 12;
    else if (e.key === 'Home') {
      e.preventDefault();
      thumb === 'from' ? setFromIdx(minIdx) : setToIdx(minIdx);
      return;
    } else if (e.key === 'End') {
      e.preventDefault();
      thumb === 'from' ? setFromIdx(maxIdx()) : setToIdx(maxIdx());
      return;
    } else { return; }
    e.preventDefault();
    if (thumb === 'from') setFromIdx(fromIdx() + delta);
    else setToIdx(toIdx() + delta);
  }

  // Presets
  function applyPreset(months: number) {
    const last = axis()[maxIdx()];
    if (!last) return;
    const start = monthAddOffset(last, -(months - 1));
    props.setFrom(start);
    props.setTo(null);
  }
  function applyYear(year: number) {
    props.setFrom(`${year}-01`);
    props.setTo(null);
  }
  function clearRange() {
    props.setFrom(null);
    props.setTo(null);
  }

  const labelLeft = () => fmtMonth(idxToYm(fromIdx()) ?? '');
  const labelRight = () => fmtMonth(idxToYm(toIdx()) ?? '');
  const isActive = () => props.from != null || props.to != null;

  return (
    <section class="border-b border-paper-300/60 dark:border-ink-600/60 py-3">
      <div class="flex items-center justify-between gap-2">
        <button
          class="flex-1 flex items-center justify-between text-xs font-semibold uppercase tracking-[0.16em] text-ink-500 dark:text-ink-200 hover:text-ink-700 dark:hover:text-ink-50"
          onClick={() => setOpen(!open())}
        >
          <span>Date <Show when={isActive()}><span class="ml-1 text-accent dark:text-accent-dark normal-case tracking-normal font-medium">· {labelLeft()} – {labelRight()}</span></Show></span>
          <span class="text-ink-400 mr-2">{open() ? '−' : '+'}</span>
        </button>
        <Show when={isActive()}>
          <button class="text-[10px] uppercase tracking-wider px-1.5 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40" onClick={clearRange}>Reset</button>
        </Show>
      </div>

      <Show when={open()}>
        <div class="mt-3 select-none">
          {/* Presets */}
          <div class="mb-3 flex flex-wrap gap-1">
            <button class="text-[11px] px-2 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40 transition-colors" onClick={() => applyPreset(3)}>3 mo</button>
            <button class="text-[11px] px-2 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40 transition-colors" onClick={() => applyPreset(6)}>6 mo</button>
            <button class="text-[11px] px-2 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40 transition-colors" onClick={() => applyPreset(12)}>12 mo</button>
            <button class="text-[11px] px-2 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40 transition-colors" onClick={() => applyYear(new Date().getFullYear())}>{new Date().getFullYear()}</button>
            <button class="text-[11px] px-2 py-0.5 rounded border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40 transition-colors" onClick={() => applyYear(new Date().getFullYear() - 1)}>{new Date().getFullYear() - 1}</button>
          </div>

          {/* Slider — track + histogram + thumbs all share the same
              horizontal padding so thumbs never escape the track and
              histogram bars line up with the track exactly. */}
          <div class="relative px-2.5">
            {/* Hover tooltip floats above the histogram */}
            <Show when={hoverIdx() != null}>
              <div
                class="pointer-events-none absolute -top-1 px-1.5 py-0.5 rounded text-[10px] bg-ink-700 text-paper-50 dark:bg-paper-50 dark:text-ink-700 whitespace-nowrap shadow-sm z-10"
                style={{ left: `calc(${widthPct(hoverIdx()!)}% + 0.625rem)`, transform: 'translateX(-50%)' }}
              >
                {fmtMonth(idxToYm(hoverIdx()!) ?? '')} · {props.histogram.counts[idxToYm(hoverIdx()!) ?? ''] ?? 0}
              </div>
            </Show>

            {/* Histogram, anchored flush above the track */}
            <div class="relative h-10">
              <div class="absolute inset-x-0 bottom-0 top-0 flex items-end gap-px">
                <For each={histBars()}>
                  {(bar, i) => {
                    const inRange = () => i() >= fromIdx() && i() <= toIdx();
                    return (
                      <div
                        class={`flex-1 rounded-t-sm transition-colors ${
                          bar.count === 0
                            ? 'bg-transparent'
                            : inRange()
                              ? 'bg-accent/65 dark:bg-accent-dark/65'
                              : 'bg-ink-300/35 dark:bg-ink-400/25'
                        }`}
                        style={{ height: `${bar.h}%` }}
                        title={`${fmtMonth(bar.m)} · ${bar.count} ${bar.count === 1 ? 'paper' : 'papers'}`}
                      />
                    );
                  }}
                </For>
              </div>
            </div>

            {/* Track + thumbs */}
            <div
              class="relative h-5 cursor-pointer"
              ref={(el) => (trackEl = el)}
              onClick={trackClick}
              onMouseMove={(e) => setHoverIdx(trackPosToIdx(e.clientX))}
              onMouseLeave={() => setHoverIdx(null)}
            >
              {/* Background track */}
              <div class="absolute left-0 right-0 top-1/2 -translate-y-1/2 h-1 rounded-full bg-ink-200/50 dark:bg-ink-700/60"></div>
              {/* Active range */}
              <div
                class="absolute top-1/2 -translate-y-1/2 h-1 rounded-full bg-accent dark:bg-accent-dark"
                style={{ left: `${widthPct(fromIdx())}%`, right: `${100 - widthPct(toIdx())}%` }}
              ></div>
              {/* Thumbs — translate-x-1/2 keeps the thumb visually
                  centered on its track position even at the extremes
                  (the parent's px-2.5 gives the gutter room). */}
              <button
                type="button"
                class="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 w-4 h-4 rounded-full bg-paper-50 dark:bg-nightbg-soft border-2 border-accent dark:border-accent-dark shadow hover:scale-110 focus:outline-none focus-visible:ring-2 focus-visible:ring-accent/50 dark:focus-visible:ring-accent-dark/50 transition-transform"
                style={{ left: `${widthPct(fromIdx())}%` }}
                onPointerDown={(e: PointerEvent) => startDrag('from', e)}
                onKeyDown={(e: KeyboardEvent) => trackKey('from', e)}
                aria-label="Start month"
                aria-valuemin={minIdx}
                aria-valuemax={maxIdx()}
                aria-valuenow={fromIdx()}
                aria-valuetext={labelLeft()}
                role="slider"
              />
              <button
                type="button"
                class="absolute top-1/2 -translate-y-1/2 -translate-x-1/2 w-4 h-4 rounded-full bg-paper-50 dark:bg-nightbg-soft border-2 border-accent dark:border-accent-dark shadow hover:scale-110 focus:outline-none focus-visible:ring-2 focus-visible:ring-accent/50 dark:focus-visible:ring-accent-dark/50 transition-transform"
                style={{ left: `${widthPct(toIdx())}%` }}
                onPointerDown={(e: PointerEvent) => startDrag('to', e)}
                onKeyDown={(e: KeyboardEvent) => trackKey('to', e)}
                aria-label="End month"
                aria-valuemin={minIdx}
                aria-valuemax={maxIdx()}
                aria-valuenow={toIdx()}
                aria-valuetext={labelRight()}
                role="slider"
              />
            </div>
          </div>

          {/* Range labels — placed inside the same gutter as the slider */}
          <div class="mt-1 px-2.5 flex items-center justify-between text-[11px] tabular-nums text-ink-500 dark:text-ink-200">
            <span>{labelLeft()}</span>
            <span class="text-ink-400 dark:text-ink-300">→</span>
            <span>{labelRight()}</span>
          </div>
        </div>
      </Show>
    </section>
  );
}

interface CardProps {
  paper: BrowserPaper;
  basePath: string;
  repoBlobUrl: string;
  onChip: (kw: string) => void;
  onToast?: (msg: string) => void;
  query?: string;
}

// LaTeX-ready BibTeX. Three cases:
//   1. arXiv-only (no formal venue) → @misc with eprint / archivePrefix /
//      primaryClass; never include booktitle.
//   2. Conference / workshop publication → @inproceedings with normalized
//      booktitle (no "(Poster)" / "(Oral)" / "(Spotlight)" / etc.).
//   3. Journal-like venue (TMLR, JMLR, …) → @article with journal field.
// Title is double-braced so LaTeX preserves capitalization on names like
// "GUI", "OSWorld", "SeeAct".
// Build a highlighted JSX-safe representation of `text` with all distinct
// tokens of `query` wrapped in <mark>. Tokens shorter than 2 chars are
// ignored so common letters don't paint over the whole string.
function highlight(text: string, query: string | undefined): any {
  if (!text) return text;
  if (!query) return text;
  const tokens = query
    .split(/\s+/)
    .map((t) => t.trim())
    .filter((t) => t.length >= 2);
  if (tokens.length === 0) return text;
  const escaped = tokens.map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
  const re = new RegExp(`(${escaped.join('|')})`, 'gi');
  const parts = text.split(re);
  return parts.map((part, idx) =>
    idx % 2 === 1 ? <mark class="search-hl">{part}</mark> : part
  );
}

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

function buildBibtex(p: BrowserPaper): string {
  const key = bibKey(p);
  const authors = p.authors.length > 0 ? p.authors.map(escapeBibValue).join(' and ') : 'Unknown';
  const titleEsc = escapeBibValue(p.title);
  const year = p.year > 0 ? String(p.year) : '';

  const venue = normalizePublisher(p.publisher);
  const kind = bibtexVenueKind(p.publisher);

  const fields: Array<[string, string]> = [];
  fields.push(['title', `{${titleEsc}}`]);
  fields.push(['author', `{${authors}}`]);
  if (year) fields.push(['year', `{${year}}`]);

  if (kind === 'misc' && p.arxivId) {
    fields.push(['eprint', `{${p.arxivId}}`]);
    fields.push(['archivePrefix', `{arXiv}`]);
    fields.push(['url', `{https://arxiv.org/abs/${p.arxivId}}`]);
    return formatBib('@misc', key, fields);
  }
  if (kind === 'misc') {
    fields.push(['howpublished', `{${escapeBibValue(p.publisher || 'Preprint')}}`]);
    fields.push(['url', `{${p.link}}`]);
    return formatBib('@misc', key, fields);
  }
  if (kind === 'article') {
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
    const done = () => {
      setBibCopied(true);
      props.onToast?.('BibTeX copied');
      setTimeout(() => setBibCopied(false), 1800);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(() => {
        const ta = document.createElement('textarea');
        ta.value = text; document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); done(); } finally { ta.remove(); }
      });
    } else {
      const ta = document.createElement('textarea');
      ta.value = text; document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } finally { ta.remove(); }
    }
  }

  return (
    <article class={`card p-5 ${p.source === 'adjacent' ? 'opacity-95' : ''} ${expanded() ? 'border-paper-400/80 dark:border-ink-400/40' : ''}`}>
      <div class="flex items-start gap-3">
        <div class="flex-1 min-w-0">
          <h3 class="text-base sm:text-[17px] font-semibold leading-snug text-ink-700 dark:text-ink-50 tracking-[-0.005em]">
            <a href={detailHref} class="hover:text-accent dark:hover:text-accent-dark transition-colors">{highlight(p.title, props.query)}</a>
          </h3>
          <p class="mt-1 text-sm text-ink-500 dark:text-ink-200 break-words">
            {highlight(visibleAuthors().join(', '), props.query)}
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
        <p class={`mt-2.5 text-sm text-ink-600 dark:text-ink-100 leading-relaxed ${expanded() ? '' : 'clamp-3'}`}>{highlight(p.tldr, props.query)}</p>
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

      <div class="expand-section mt-0" data-open={expanded() ? 'true' : 'false'}>
       <div class="expand-section__inner">
        <div class={`mt-4 pt-4 border-t border-paper-300/60 dark:border-ink-600/60 ${bibCopied() ? 'copy-pulse copy-glow-source' : ''} rounded-md`}>
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
              class={`inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-md border transition-colors ${
                bibCopied()
                  ? 'border-accent/60 dark:border-accent-dark/60 text-accent dark:text-accent-dark bg-accent/5 dark:bg-accent-dark/10'
                  : 'border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40'
              }`}
              onClick={copyBibtex}
              aria-label="Copy BibTeX to clipboard"
            >
              <Show when={bibCopied()} fallback={
                <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              }>
                <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                  <path class="copied-check" d="M5 12l5 5L20 7"/>
                </svg>
              </Show>
              <span>{bibCopied() ? 'BibTeX copied' : 'Copy BibTeX'}</span>
            </button>
            <a class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-md border border-paper-300/80 dark:border-ink-600/60 hover:bg-paper-200/60 dark:hover:bg-ink-700/40" href={reportUrl} target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" width="12" height="12" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg>
              Report issue
            </a>
          </div>
        </div>
       </div>
      </div>

      <div class="mt-3.5 flex items-center justify-between gap-3 text-xs">
        <button
          class="font-medium inline-flex items-center gap-1 text-accent dark:text-accent-dark hover:opacity-90"
          onClick={() => setExpanded(!expanded())}
          aria-expanded={expanded() ? 'true' : 'false'}
          type="button"
        >
          <svg viewBox="0 0 16 16" width="11" height="11" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class={`transition-transform duration-200 ${expanded() ? 'rotate-180' : ''}`} aria-hidden="true"><path d="M3 6l5 5 5-5"/></svg>
          <span>{expanded() ? 'Hide details' : 'Show details'}</span>
        </button>
        <a class="text-ink-400 dark:text-ink-300 hover:text-accent dark:hover:text-accent-dark" href={p.link} target="_blank" rel="noopener">Open ↗</a>
      </div>
    </article>
  );
}
