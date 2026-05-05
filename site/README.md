# GUI Agents Paper List — Static Site

Astro site that presents `papers.yaml` and `adjacent.yaml` as a searchable, filterable web UI. Deployed to GitHub Pages.

The site is a **presentation layer only** — it reads from the markdown source of truth in this repo and never adds metadata of its own.

## Develop

```bash
cd site
npm install
npm run dev
```

The dev server reads `../papers.yaml` and `../adjacent.yaml` directly. Edit either, save, refresh.

## Build

```bash
npm run build
npm run preview
```

Output goes to `site/dist/`.

### Environment variables

| Var | Purpose | Default |
|---|---|---|
| `BASE_PATH` | URL base path (project pages need `/REPO_NAME`) | `/GUI-Agents-Paper-List` |
| `SITE_URL` | Origin of the deployed site | `https://OSU-NLP-Group.github.io` |
| `STAR_COUNT` | Pre-fetched star count (skips a runtime GitHub API call) | unset → fetched at build |

For local dev, run with `BASE_PATH=` to serve at the root:

```bash
BASE_PATH= npm run dev
```

## Deploy

`.github/workflows/deploy-site.yml` (in repo root, not in `site/`) builds and publishes to GitHub Pages on every push that touches the source markdown or the site code, plus a daily cron that refreshes the star count.

To enable on first use:

1. Repo **Settings → Pages → Source** → "GitHub Actions".
2. Push the workflow + this `site/` directory to `main`.

## Stack

- **Astro 4** — static-first framework with islands.
- **Solid.js** — tiny reactive runtime for the interactive browse + stats islands.
- **MiniSearch** — BM25 full-text search built at page-load time.
- **ECharts** — interactive charts on `/stats` (lazy-loaded).
- **Tailwind CSS** — utility styles, warm-paper light + dark night themes.

## Structure

```
site/
├── src/
│   ├── lib/
│   │   ├── parsePapers.ts   # YAML loader (papers.yaml + adjacent.yaml)
│   │   ├── site.ts          # repo URLs, env metadata
│   │   └── star.ts          # GitHub star fetcher
│   ├── layouts/Base.astro   # top bar + footer + theme bootstrap
│   ├── components/
│   │   ├── TopBar.astro     # sticky bar with Star CTA + theme toggle
│   │   ├── Footer.astro
│   │   ├── ThemeToggle.astro# pill toggle (light = warm paper, dark = navy)
│   │   └── PaperCard.astro  # static paper card (used on landing/detail/adjacent)
│   ├── islands/
│   │   ├── PaperBrowser.tsx # /papers — search + filters + URL sync
│   │   └── StatsCharts.tsx  # /stats — interactive ECharts
│   ├── pages/
│   │   ├── index.astro      # landing
│   │   ├── papers/
│   │   │   ├── index.astro  # browse (Solid island)
│   │   │   └── [slug].astro # paper detail (static)
│   │   ├── stats.astro
│   │   ├── adjacent.astro
│   │   ├── about.astro
│   │   └── 404.astro
│   └── styles/global.css
├── public/favicon.svg
├── astro.config.mjs
├── tailwind.config.mjs
└── tsconfig.json
```

## Theme

The theme defaults to the warm-paper light scheme. The pill toggle in the top right switches to a dark scheme; the choice is persisted to `localStorage` and applied via an inline script before paint to avoid flashes.
