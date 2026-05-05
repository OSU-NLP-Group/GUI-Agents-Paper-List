export const SITE_TITLE = 'GUI Agents Papers';
export const SITE_DESCRIPTION =
  'A curated, searchable list of research papers on GUI agents — models, frameworks, benchmarks, datasets, and more.';
export const REPO_OWNER = 'OSU-NLP-Group';
export const REPO_NAME = 'GUI-Agents-Paper-List';
export const REPO_URL = `https://github.com/${REPO_OWNER}/${REPO_NAME}`;
export const REPO_RAW_BLOB = `${REPO_URL}/blob/main`;

export const ENV_ORDER = ['Web', 'Mobile', 'Desktop', 'General GUI'] as const;
export const ENV_EMOJI: Record<string, string> = {
  Web: '🌐',
  Mobile: '📱',
  Desktop: '🖥️',
  'General GUI': '🖼️',
};
