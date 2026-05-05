/** @jsxImportSource solid-js */
import { onMount, onCleanup, createSignal } from 'solid-js';
import * as echarts from 'echarts';
import type { BrowserPaper } from './PaperBrowser';

interface Props {
  papers: BrowserPaper[];
  basePath: string;
}

function isDark(): boolean {
  return document.documentElement.classList.contains('dark');
}

// Two themed palettes — earthy warm tones for light, cool muted tones for dark.
// Each theme uses a single hue family per chart for visual quietness.
function paperColors() {
  return isDark()
    ? {
        bg: 'transparent',
        text: '#e9e6df',
        muted: '#a39e92',
        faint: 'rgba(255,255,255,0.04)',
        bar: '#6b8cf0',                 // accent dark
        barAlt: '#9ab0d4',
        line: '#8aa5e8',
        envColors: {                    // for the trend chart by env
          Web: '#6b8cf0',
          Mobile: '#d49363',
          Desktop: '#7fb39a',
          'General GUI': '#c79bd0',
        } as Record<string, string>,
        donut: ['#6b8cf0', '#7fb39a', '#d49363', '#c79bd0'],
        treemapTones: ['#3a4878', '#43547e', '#4d5f84', '#576b8b', '#617791', '#6c8298', '#778d9e', '#8198a4'],
        cardBorder: 'rgba(233,230,223,0.08)',
        tooltipBg: '#1a1f29',
        tooltipBorder: 'rgba(255,255,255,0.08)',
      }
    : {
        bg: 'transparent',
        text: '#33312a',
        muted: '#8a8472',
        faint: 'rgba(0,0,0,0.04)',
        bar: '#3057c4',
        barAlt: '#7388be',
        line: '#3057c4',
        envColors: {
          Web: '#3057c4',
          Mobile: '#a6622b',
          Desktop: '#3f7a55',
          'General GUI': '#8a527e',
        } as Record<string, string>,
        donut: ['#3057c4', '#3f7a55', '#a6622b', '#8a527e'],
        // single-hue earthy treemap progression (dark → light terracotta)
        treemapTones: ['#5e3a2a', '#6e4530', '#7e5037', '#8e5b3e', '#9e6745', '#ad734d', '#bb8056', '#c98e62'],
        cardBorder: 'rgba(35,33,28,0.08)',
        tooltipBg: '#fbf6ec',
        tooltipBorder: 'rgba(35,33,28,0.12)',
      };
}

const SHARED_TEXT = {
  fontFamily: 'ui-sans-serif, system-ui, -apple-system, "Segoe UI", Inter, sans-serif',
};

function tooltipBase(c: ReturnType<typeof paperColors>) {
  return {
    backgroundColor: c.tooltipBg,
    borderColor: c.tooltipBorder,
    borderWidth: 1,
    padding: [8, 12],
    textStyle: {
      color: c.text,
      fontSize: 12,
      ...SHARED_TEXT,
    },
    extraCssText: 'box-shadow: 0 4px 14px rgba(0,0,0,0.06); border-radius: 6px;',
  };
}

function quarterKey(iso: string): string {
  const [y, m] = iso.split('-');
  const q = Math.floor((parseInt(m, 10) - 1) / 3) + 1;
  return `${y} Q${q}`;
}

function buildQuarterly(papers: BrowserPaper[]) {
  const envs = ['Web', 'Mobile', 'Desktop', 'General GUI'];
  const buckets = new Map<string, Record<string, number>>();
  for (const p of papers) {
    if (!p.dateISO || p.year < 2000) continue;
    const k = quarterKey(p.dateISO);
    if (!buckets.has(k)) {
      const init: Record<string, number> = { Total: 0 };
      for (const e of envs) init[e] = 0;
      buckets.set(k, init);
    }
    const row = buckets.get(k)!;
    row.Total += 1;
    for (const e of p.envs) {
      if (e in row) row[e] += 1;
    }
  }
  const keys = Array.from(buckets.keys()).sort();
  return { keys, envs, buckets };
}

export default function StatsCharts(props: Props) {
  let trendEl!: HTMLDivElement;
  let kwEl!: HTMLDivElement;
  let envEl!: HTMLDivElement;
  let instEl!: HTMLDivElement;
  let authorEl!: HTMLDivElement;
  let pubEl!: HTMLDivElement;
  const charts: echarts.ECharts[] = [];

  const [, setTick] = createSignal(0);

  function build() {
    for (const c of charts) c.dispose();
    charts.length = 0;
    const c = paperColors();

    // === 1. Quarterly trend — clean stacked area, no rainbow ===
    const { keys, envs, buckets } = buildQuarterly(props.papers);
    const trend = echarts.init(trendEl, null, { renderer: 'canvas' });
    trend.setOption({
      backgroundColor: c.bg,
      textStyle: SHARED_TEXT,
      tooltip: {
        ...tooltipBase(c),
        trigger: 'axis',
        axisPointer: { type: 'line', lineStyle: { color: c.muted, type: 'dashed' } },
      },
      legend: {
        data: envs,
        textStyle: { color: c.muted, fontSize: 11, ...SHARED_TEXT },
        top: 4,
        right: 12,
        icon: 'roundRect',
        itemWidth: 10,
        itemHeight: 10,
        itemGap: 14,
      },
      grid: { left: 36, right: 16, top: 36, bottom: 48, containLabel: true },
      xAxis: {
        type: 'category', data: keys, boundaryGap: false,
        axisLabel: { color: c.muted, fontSize: 10, ...SHARED_TEXT, rotate: 45, margin: 12 },
        axisLine: { lineStyle: { color: c.faint } },
        axisTick: { show: false },
      },
      yAxis: {
        type: 'value',
        axisLabel: { color: c.muted, fontSize: 10, ...SHARED_TEXT },
        axisLine: { show: false },
        axisTick: { show: false },
        splitLine: { lineStyle: { color: c.faint, type: 'solid' } },
      },
      series: envs.map((e) => ({
        name: e, type: 'area', stack: 'env',
        type_: 'line',
      })).map((s, i) => ({
        name: s.name, type: 'line' as const, stack: 'env',
        smooth: 0.5, symbol: 'none' as const,
        lineStyle: { width: 0, color: c.envColors[s.name] },
        areaStyle: { color: c.envColors[s.name], opacity: isDark() ? 0.55 : 0.7 },
        emphasis: { focus: 'series' as const },
        data: keys.map((k) => buckets.get(k)![s.name]),
      })),
    });
    charts.push(trend);

    // === 2. Keyword treemap — limited, clean, single-hue ===
    const kwCounter = new Map<string, number>();
    for (const p of props.papers) for (const k of p.keywords) kwCounter.set(k, (kwCounter.get(k) ?? 0) + 1);
    const topKw = Array.from(kwCounter.entries()).sort((a, b) => b[1] - a[1]).slice(0, 30);
    const maxKw = topKw[0]?.[1] ?? 1;
    const kwChart = echarts.init(kwEl, null, { renderer: 'canvas' });
    kwChart.setOption({
      backgroundColor: c.bg,
      textStyle: SHARED_TEXT,
      tooltip: {
        ...tooltipBase(c),
        formatter: (info: any) => `<span style="font-weight:600">${info.name}</span><br/><span style="color:${c.muted}">${info.value} papers</span>`,
      },
      series: [{
        type: 'treemap', roam: false, nodeClick: false, breadcrumb: { show: false },
        width: '100%', height: '100%',
        label: {
          show: true,
          formatter: (info: any) => {
            const v = info.value as number;
            const ratio = v / maxKw;
            // hide labels on smallest tiles
            if (ratio < 0.15) return '';
            return ratio > 0.4 ? `{name|${info.name}}\n{count|${v}}` : `{name|${info.name}}`;
          },
          rich: {
            name: { color: '#fbf6ec', fontSize: 12, fontWeight: 600, ...SHARED_TEXT, lineHeight: 18 },
            count: { color: 'rgba(251,246,236,0.7)', fontSize: 11, ...SHARED_TEXT },
          },
        },
        upperLabel: { show: false },
        itemStyle: {
          borderColor: isDark() ? '#0f1217' : '#f7efdf',
          borderWidth: 3,
          gapWidth: 3,
        },
        levels: [{
          itemStyle: {
            borderColor: isDark() ? '#0f1217' : '#f7efdf',
            borderWidth: 3, gapWidth: 3,
          },
        }],
        data: topKw.map(([k, v], i) => {
          // Map by count to a tone in the palette (more prominent → darker)
          const toneIdx = Math.max(0, Math.min(c.treemapTones.length - 1,
            c.treemapTones.length - 1 - Math.floor((v / maxKw) * c.treemapTones.length)));
          return { name: k, value: v, itemStyle: { color: c.treemapTones[toneIdx] } };
        }),
      }],
    });
    kwChart.on('click', (params: any) => {
      if (!params || !params.name) return;
      window.location.href = `${props.basePath}/papers?key=${encodeURIComponent(params.name)}`;
    });
    charts.push(kwChart);

    // === 3. Environment donut — minimal, no inline labels, no legend marker noise ===
    const envCounter = new Map<string, number>();
    for (const p of props.papers) for (const e of p.envs) envCounter.set(e, (envCounter.get(e) ?? 0) + 1);
    const envChart = echarts.init(envEl, null, { renderer: 'canvas' });
    const envEntries = Array.from(envCounter.entries());
    envChart.setOption({
      backgroundColor: c.bg,
      textStyle: SHARED_TEXT,
      tooltip: {
        ...tooltipBase(c),
        formatter: (p: any) => `<span style="font-weight:600">${p.name}</span><br/><span style="color:${c.muted}">${p.value} papers (${p.percent}%)</span>`,
      },
      legend: {
        bottom: 6, left: 'center',
        textStyle: { color: c.muted, fontSize: 11, ...SHARED_TEXT },
        icon: 'circle', itemWidth: 8, itemHeight: 8, itemGap: 16,
      },
      series: [{
        type: 'pie', radius: ['54%', '78%'], center: ['50%', '46%'],
        avoidLabelOverlap: true,
        itemStyle: {
          borderColor: isDark() ? '#161a21' : '#fbf6ec',
          borderWidth: 4,
        },
        label: {
          show: true,
          formatter: (p: any) => `{n|${p.name}}\n{v|${p.value}}`,
          rich: {
            n: { color: c.text, fontSize: 12, fontWeight: 600, ...SHARED_TEXT, lineHeight: 18 },
            v: { color: c.muted, fontSize: 11, ...SHARED_TEXT },
          },
          alignTo: 'edge', edgeDistance: 6,
        },
        labelLine: { lineStyle: { color: c.muted, width: 1 }, length: 10, length2: 10 },
        data: envEntries.map(([k, v], i) => ({
          name: k, value: v,
          itemStyle: { color: c.envColors[k] ?? c.donut[i % c.donut.length] },
        })),
      }],
    });
    envChart.on('click', (params: any) => {
      window.location.href = `${props.basePath}/papers?env=${encodeURIComponent(params.name)}`;
    });
    charts.push(envChart);

    // === 4. Top institutions — single accent hue, count labels at end of bars ===
    const instCounter = new Map<string, number>();
    for (const p of props.papers) for (const i of p.institutions) instCounter.set(i, (instCounter.get(i) ?? 0) + 1);
    const topInst = Array.from(instCounter.entries()).sort((a, b) => b[1] - a[1]).slice(0, 25).reverse();
    const instChart = echarts.init(instEl, null, { renderer: 'canvas' });
    instChart.setOption({
      backgroundColor: c.bg,
      textStyle: SHARED_TEXT,
      tooltip: {
        ...tooltipBase(c),
        formatter: (p: any) => `<span style="font-weight:600">${p.name}</span><br/><span style="color:${c.muted}">${p.value} papers</span>`,
      },
      grid: { left: 4, right: 36, top: 4, bottom: 8, containLabel: true },
      xAxis: { type: 'value', show: false },
      yAxis: {
        type: 'category', data: topInst.map(([k]) => k),
        axisLabel: { color: c.text, fontSize: 11, ...SHARED_TEXT, margin: 12 },
        axisLine: { show: false }, axisTick: { show: false },
      },
      series: [{
        type: 'bar', data: topInst.map(([, v]) => v),
        barWidth: '60%',
        itemStyle: {
          color: {
            type: 'linear', x: 0, y: 0, x2: 1, y2: 0,
            colorStops: [
              { offset: 0, color: c.bar + (isDark() ? '88' : '40') },
              { offset: 1, color: c.bar },
            ],
          },
          borderRadius: [0, 3, 3, 0],
        },
        label: {
          show: true, position: 'right',
          color: c.muted, fontSize: 10, ...SHARED_TEXT, distance: 6,
        },
        emphasis: { itemStyle: { color: c.bar } },
      }],
    });
    instChart.on('click', (params: any) => {
      window.location.href = `${props.basePath}/papers?inst=${encodeURIComponent(params.name)}`;
    });
    charts.push(instChart);

    // === 5. Top authors ===
    const aCounter = new Map<string, number>();
    for (const p of props.papers) for (const a of p.authors) aCounter.set(a, (aCounter.get(a) ?? 0) + 1);
    const topA = Array.from(aCounter.entries()).sort((a, b) => b[1] - a[1]).slice(0, 25).reverse();
    const aChart = echarts.init(authorEl, null, { renderer: 'canvas' });
    aChart.setOption({
      backgroundColor: c.bg,
      textStyle: SHARED_TEXT,
      tooltip: {
        ...tooltipBase(c),
        formatter: (p: any) => `<span style="font-weight:600">${p.name}</span><br/><span style="color:${c.muted}">${p.value} papers</span>`,
      },
      grid: { left: 4, right: 36, top: 4, bottom: 8, containLabel: true },
      xAxis: { type: 'value', show: false },
      yAxis: {
        type: 'category', data: topA.map(([k]) => k),
        axisLabel: { color: c.text, fontSize: 11, ...SHARED_TEXT, margin: 12 },
        axisLine: { show: false }, axisTick: { show: false },
      },
      series: [{
        type: 'bar', data: topA.map(([, v]) => v),
        barWidth: '60%',
        itemStyle: {
          color: {
            type: 'linear', x: 0, y: 0, x2: 1, y2: 0,
            colorStops: [
              { offset: 0, color: c.bar + (isDark() ? '88' : '40') },
              { offset: 1, color: c.bar },
            ],
          },
          borderRadius: [0, 3, 3, 0],
        },
        label: {
          show: true, position: 'right',
          color: c.muted, fontSize: 10, ...SHARED_TEXT, distance: 6,
        },
      }],
    });
    aChart.on('click', (params: any) => {
      window.location.href = `${props.basePath}/papers?author=${encodeURIComponent(params.name)}`;
    });
    charts.push(aChart);

    // === 6. Publication venues ===
    // Collapse presentation variants — (Poster) / (Oral) / (Spotlight) etc.
    // and "Findings of …" / workshop/track suffixes — into one venue bucket.
    const pCounter = new Map<string, number>();
    for (const p of props.papers) {
      if (!p.publisher || /^arxiv$/i.test(p.publisher.trim())) continue;
      let v = p.publisher.trim();
      v = v.replace(/\s*\([^)]*\)\s*$/g, '').trim();
      v = v.replace(/^Findings of\s+/i, '').trim();
      v = v.replace(/\s+(Workshop|Track|Datasets and Benchmarks Track|Findings)\b.*$/i, '').trim();
      if (!v) continue;
      pCounter.set(v, (pCounter.get(v) ?? 0) + 1);
    }
    const topP = Array.from(pCounter.entries()).sort((a, b) => b[1] - a[1]).slice(0, 15).reverse();
    const pChart = echarts.init(pubEl, null, { renderer: 'canvas' });
    pChart.setOption({
      backgroundColor: c.bg,
      textStyle: SHARED_TEXT,
      tooltip: {
        ...tooltipBase(c),
        formatter: (p: any) => `<span style="font-weight:600">${p.name}</span><br/><span style="color:${c.muted}">${p.value} papers</span>`,
      },
      grid: { left: 4, right: 36, top: 4, bottom: 8, containLabel: true },
      xAxis: { type: 'value', show: false },
      yAxis: {
        type: 'category', data: topP.map(([k]) => k),
        axisLabel: { color: c.text, fontSize: 11, ...SHARED_TEXT, margin: 12 },
        axisLine: { show: false }, axisTick: { show: false },
      },
      series: [{
        type: 'bar', data: topP.map(([, v]) => v),
        barWidth: '60%',
        itemStyle: {
          color: {
            type: 'linear', x: 0, y: 0, x2: 1, y2: 0,
            colorStops: [
              { offset: 0, color: c.bar + (isDark() ? '88' : '40') },
              { offset: 1, color: c.bar },
            ],
          },
          borderRadius: [0, 3, 3, 0],
        },
        label: {
          show: true, position: 'right',
          color: c.muted, fontSize: 10, ...SHARED_TEXT, distance: 6,
        },
      }],
    });
    charts.push(pChart);
  }

  function resizeAll() { for (const c of charts) c.resize(); }

  onMount(() => {
    build();
    const ro = new ResizeObserver(() => resizeAll());
    [trendEl, kwEl, envEl, instEl, authorEl, pubEl].forEach((el) => ro.observe(el));
    const mo = new MutationObserver(() => { build(); setTick((x) => x + 1); });
    mo.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
    onCleanup(() => { ro.disconnect(); mo.disconnect(); for (const c of charts) c.dispose(); });
  });

  return (
    <div class="space-y-14">
      <section>
        <div class="flex items-baseline justify-between mb-1">
          <h2 class="text-base font-semibold text-ink-700 dark:text-ink-50">Quarterly publication trend</h2>
          <span class="text-xs text-ink-400 dark:text-ink-300">stacked by environment</span>
        </div>
        <p class="text-xs text-ink-400 dark:text-ink-300 mb-4">Number of papers added to the list per calendar quarter, from the earliest preprint date.</p>
        <div ref={(el) => (trendEl = el)} class="w-full h-[340px]"></div>
      </section>

      <section class="grid lg:grid-cols-[minmax(0,1fr)_minmax(0,1.4fr)] gap-12">
        <div>
          <h2 class="text-base font-semibold text-ink-700 dark:text-ink-50 mb-1">Environment split</h2>
          <p class="text-xs text-ink-400 dark:text-ink-300 mb-4">Click a slice to filter the browse.</p>
          <div ref={(el) => (envEl = el)} class="w-full h-[360px]"></div>
        </div>
        <div>
          <h2 class="text-base font-semibold text-ink-700 dark:text-ink-50 mb-1">Top keywords</h2>
          <p class="text-xs text-ink-400 dark:text-ink-300 mb-4">Tile area is paper count. Darker tiles are more frequent. Click to filter.</p>
          <div ref={(el) => (kwEl = el)} class="w-full h-[480px]"></div>
        </div>
      </section>

      <section class="grid lg:grid-cols-2 gap-12">
        <div>
          <h2 class="text-base font-semibold text-ink-700 dark:text-ink-50 mb-1">Top 25 institutions</h2>
          <p class="text-xs text-ink-400 dark:text-ink-300 mb-4">Click a name to filter.</p>
          <div ref={(el) => (instEl = el)} class="w-full h-[560px]"></div>
        </div>
        <div>
          <h2 class="text-base font-semibold text-ink-700 dark:text-ink-50 mb-1">Top 25 authors</h2>
          <p class="text-xs text-ink-400 dark:text-ink-300 mb-4">Click a name to filter.</p>
          <div ref={(el) => (authorEl = el)} class="w-full h-[560px]"></div>
        </div>
      </section>

      <section>
        <h2 class="text-base font-semibold text-ink-700 dark:text-ink-50 mb-1">Publication venues</h2>
        <p class="text-xs text-ink-400 dark:text-ink-300 mb-4">Top 15 venues, excluding arXiv-only entries.</p>
        <div ref={(el) => (pubEl = el)} class="w-full h-[400px]"></div>
      </section>
    </div>
  );
}
