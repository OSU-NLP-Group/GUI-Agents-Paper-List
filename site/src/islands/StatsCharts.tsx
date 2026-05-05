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

function paperColors() {
  return isDark()
    ? {
        bg: 'transparent',
        text: '#e9e6df',
        muted: '#a39e92',
        grid: 'rgba(255,255,255,0.06)',
        accent: '#6b8cf0',
        palette: ['#6b8cf0', '#e0b25b', '#85c5a3', '#d09080', '#9aa6c2', '#c79bd0', '#7fb3c6', '#cabf86'],
      }
    : {
        bg: 'transparent',
        text: '#33312a',
        muted: '#6b6759',
        grid: 'rgba(0,0,0,0.06)',
        accent: '#3057c4',
        palette: ['#3057c4', '#a36b1e', '#3f7a55', '#a04a3a', '#5b6791', '#8a527e', '#3d6a78', '#7a6c2d'],
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

    // 1. Quarterly trend stacked
    const { keys, envs } = buildQuarterly(props.papers);
    const buckets = buildQuarterly(props.papers).buckets;
    const trend = echarts.init(trendEl, null, { renderer: 'canvas' });
    trend.setOption({
      backgroundColor: c.bg,
      tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
      legend: { data: ['Total', ...envs], textStyle: { color: c.text }, top: 0 },
      grid: { left: 40, right: 16, top: 36, bottom: 60 },
      xAxis: {
        type: 'category', data: keys,
        axisLabel: { color: c.muted, rotate: 45 },
        axisLine: { lineStyle: { color: c.grid } },
      },
      yAxis: { type: 'value', axisLabel: { color: c.muted }, splitLine: { lineStyle: { color: c.grid } } },
      series: [
        {
          name: 'Total',
          type: 'line', smooth: true, symbol: 'circle', symbolSize: 5,
          lineStyle: { width: 2.2, color: c.accent },
          itemStyle: { color: c.accent },
          areaStyle: { color: c.accent, opacity: 0.08 },
          data: keys.map((k) => buckets.get(k)!.Total),
          z: 3,
        },
        ...envs.map((e, idx) => ({
          name: e, type: 'line' as const, smooth: true, symbol: 'none' as const,
          lineStyle: { width: 1.4, color: c.palette[(idx + 1) % c.palette.length] },
          itemStyle: { color: c.palette[(idx + 1) % c.palette.length] },
          data: keys.map((k) => buckets.get(k)![e]),
          emphasis: { focus: 'series' as const },
        })),
      ],
    });
    charts.push(trend);

    // 2. Keyword treemap — area scaled to count, click to filter
    const kwCounter = new Map<string, number>();
    for (const p of props.papers) for (const k of p.keywords) kwCounter.set(k, (kwCounter.get(k) ?? 0) + 1);
    const topKw = Array.from(kwCounter.entries()).sort((a, b) => b[1] - a[1]).slice(0, 50);
    const kwChart = echarts.init(kwEl, null, { renderer: 'canvas' });
    kwChart.setOption({
      backgroundColor: c.bg,
      tooltip: { formatter: (info: any) => `<strong>${info.name}</strong><br/>${info.value} papers` },
      series: [{
        type: 'treemap',
        roam: false,
        nodeClick: 'link',
        breadcrumb: { show: false },
        label: {
          show: true,
          formatter: '{b}',
          color: c.text,
          fontSize: 12,
        },
        upperLabel: { show: false },
        itemStyle: {
          borderColor: isDark() ? '#0f1217' : '#fbf6ec',
          borderWidth: 2,
          gapWidth: 2,
        },
        levels: [{
          itemStyle: {
            borderColor: isDark() ? '#0f1217' : '#fbf6ec',
            borderWidth: 2,
            gapWidth: 2,
          },
        }],
        data: topKw.map(([k, v], i) => ({
          name: k, value: v,
          itemStyle: { color: c.palette[i % c.palette.length] },
        })),
      }],
    });
    kwChart.on('click', (params: any) => {
      if (!params || !params.name) return;
      window.location.href = `${props.basePath}/papers?key=${encodeURIComponent(params.name)}`;
    });
    charts.push(kwChart);

    // 3. Env donut
    const envCounter = new Map<string, number>();
    for (const p of props.papers) for (const e of p.envs) envCounter.set(e, (envCounter.get(e) ?? 0) + 1);
    const envChart = echarts.init(envEl, null, { renderer: 'canvas' });
    envChart.setOption({
      backgroundColor: c.bg,
      tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
      legend: { bottom: 0, textStyle: { color: c.text } },
      series: [{
        type: 'pie', radius: ['45%', '72%'], center: ['50%', '46%'],
        avoidLabelOverlap: true,
        itemStyle: { borderColor: isDark() ? '#0f1217' : '#f7efdf', borderWidth: 3 },
        label: { color: c.text, formatter: '{b}\n{c}' },
        data: Array.from(envCounter.entries()).map(([k, v], i) => ({
          name: k, value: v, itemStyle: { color: c.palette[i % c.palette.length] },
        })),
      }],
    });
    envChart.on('click', (params: any) => {
      window.location.href = `${props.basePath}/papers?env=${encodeURIComponent(params.name)}`;
    });
    charts.push(envChart);

    // 4. Top institutions (25)
    const instCounter = new Map<string, number>();
    for (const p of props.papers) for (const i of p.institutions) instCounter.set(i, (instCounter.get(i) ?? 0) + 1);
    const topInst = Array.from(instCounter.entries()).sort((a, b) => b[1] - a[1]).slice(0, 25).reverse();
    const instChart = echarts.init(instEl, null, { renderer: 'canvas' });
    instChart.setOption({
      backgroundColor: c.bg,
      tooltip: { trigger: 'item' },
      grid: { left: 130, right: 24, top: 8, bottom: 24 },
      xAxis: { type: 'value', axisLabel: { color: c.muted }, splitLine: { lineStyle: { color: c.grid } } },
      yAxis: { type: 'category', data: topInst.map(([k]) => k), axisLabel: { color: c.text, fontSize: 11 }, axisLine: { lineStyle: { color: c.grid } } },
      series: [{ type: 'bar', data: topInst.map(([, v]) => v), itemStyle: { color: c.palette[2], borderRadius: [0, 3, 3, 0] } }],
    });
    instChart.on('click', (params: any) => {
      window.location.href = `${props.basePath}/papers?inst=${encodeURIComponent(params.name)}`;
    });
    charts.push(instChart);

    // 5. Top authors (25)
    const aCounter = new Map<string, number>();
    for (const p of props.papers) for (const a of p.authors) aCounter.set(a, (aCounter.get(a) ?? 0) + 1);
    const topA = Array.from(aCounter.entries()).sort((a, b) => b[1] - a[1]).slice(0, 25).reverse();
    const aChart = echarts.init(authorEl, null, { renderer: 'canvas' });
    aChart.setOption({
      backgroundColor: c.bg,
      tooltip: { trigger: 'item' },
      grid: { left: 140, right: 24, top: 8, bottom: 24 },
      xAxis: { type: 'value', axisLabel: { color: c.muted }, splitLine: { lineStyle: { color: c.grid } } },
      yAxis: { type: 'category', data: topA.map(([k]) => k), axisLabel: { color: c.text, fontSize: 11 }, axisLine: { lineStyle: { color: c.grid } } },
      series: [{ type: 'bar', data: topA.map(([, v]) => v), itemStyle: { color: c.palette[3], borderRadius: [0, 3, 3, 0] } }],
    });
    aChart.on('click', (params: any) => {
      window.location.href = `${props.basePath}/papers?author=${encodeURIComponent(params.name)}`;
    });
    charts.push(aChart);

    // 6. Publishers (top 15, excluding arXiv)
    const pCounter = new Map<string, number>();
    for (const p of props.papers) {
      if (!p.publisher || /^arxiv$/i.test(p.publisher.trim())) continue;
      const v = p.publisher.replace(/\s*\(.*?\)\s*$/, '');
      pCounter.set(v, (pCounter.get(v) ?? 0) + 1);
    }
    const topP = Array.from(pCounter.entries()).sort((a, b) => b[1] - a[1]).slice(0, 15).reverse();
    const pChart = echarts.init(pubEl, null, { renderer: 'canvas' });
    pChart.setOption({
      backgroundColor: c.bg,
      tooltip: { trigger: 'item' },
      grid: { left: 130, right: 24, top: 8, bottom: 24 },
      xAxis: { type: 'value', axisLabel: { color: c.muted }, splitLine: { lineStyle: { color: c.grid } } },
      yAxis: { type: 'category', data: topP.map(([k]) => k), axisLabel: { color: c.text, fontSize: 11 }, axisLine: { lineStyle: { color: c.grid } } },
      series: [{ type: 'bar', data: topP.map(([, v]) => v), itemStyle: { color: c.palette[5], borderRadius: [0, 3, 3, 0] } }],
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
    <div class="space-y-12">
      <section>
        <h2 class="text-lg font-semibold mb-3 text-ink-700 dark:text-ink-50">Quarterly publication trend</h2>
        <p class="text-sm text-ink-500 dark:text-ink-200 mb-3">Total + per-environment counts. Hover for breakdown.</p>
        <div ref={(el) => (trendEl = el)} class="w-full h-[360px] surface rounded-lg p-4"></div>
      </section>
      <section class="grid lg:grid-cols-[1fr_1.4fr] gap-8">
        <div>
          <h2 class="text-lg font-semibold mb-3 text-ink-700 dark:text-ink-50">Environment split</h2>
          <p class="text-sm text-ink-500 dark:text-ink-200 mb-3">Click a slice to filter.</p>
          <div ref={(el) => (envEl = el)} class="w-full h-[360px] surface rounded-lg p-4"></div>
        </div>
        <div>
          <h2 class="text-lg font-semibold mb-3 text-ink-700 dark:text-ink-50">Top keywords</h2>
          <p class="text-sm text-ink-500 dark:text-ink-200 mb-3">Tile area is paper count. Click a tile to filter the browse.</p>
          <div ref={(el) => (kwEl = el)} class="w-full h-[640px] surface rounded-lg p-4"></div>
        </div>
      </section>
      <section class="grid lg:grid-cols-2 gap-8">
        <div>
          <h2 class="text-lg font-semibold mb-3 text-ink-700 dark:text-ink-50">Top 25 institutions</h2>
          <div ref={(el) => (instEl = el)} class="w-full h-[600px] surface rounded-lg p-4"></div>
        </div>
        <div>
          <h2 class="text-lg font-semibold mb-3 text-ink-700 dark:text-ink-50">Top 25 authors</h2>
          <div ref={(el) => (authorEl = el)} class="w-full h-[600px] surface rounded-lg p-4"></div>
        </div>
      </section>
      <section>
        <h2 class="text-lg font-semibold mb-3 text-ink-700 dark:text-ink-50">Publication venues</h2>
        <p class="text-sm text-ink-500 dark:text-ink-200 mb-3">Top 15 venues, excluding arXiv-only entries.</p>
        <div ref={(el) => (pubEl = el)} class="w-full h-[420px] surface rounded-lg p-4"></div>
      </section>
    </div>
  );
}
