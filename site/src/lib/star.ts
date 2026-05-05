import { REPO_OWNER, REPO_NAME } from './site';

let cached: number | null | undefined;

export async function getStarCount(): Promise<number | null> {
  if (cached !== undefined) return cached;
  const envCount = process.env.STAR_COUNT;
  if (envCount && /^\d+$/.test(envCount)) {
    cached = parseInt(envCount, 10);
    return cached;
  }
  // If STAR_COUNT is unset, skip the network call. Fetching inside an Astro
  // build can hang network-isolated environments; pass STAR_COUNT explicitly
  // when building (the local deploy script does this via `gh api`).
  if (!process.env.GITHUB_FETCH_STARS) {
    cached = null;
    return null;
  }
  try {
    const ac = new AbortController();
    const t = setTimeout(() => ac.abort(), 3000);
    const res = await fetch(`https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}`, {
      headers: { 'User-Agent': 'gui-agents-paper-list-site' },
      signal: ac.signal,
    });
    clearTimeout(t);
    if (!res.ok) {
      cached = null;
      return null;
    }
    const data = (await res.json()) as { stargazers_count?: number };
    cached = typeof data.stargazers_count === 'number' ? data.stargazers_count : null;
    return cached;
  } catch {
    cached = null;
    return null;
  }
}
