export interface ReleaseAsset {
  name: string;
  url: string;
  size: number;
  contentType: string;
  platform: Platform;
}

export interface Release {
  tagName: string;
  name: string;
  publishedAt: string;
  htmlUrl: string;
  body: string;
  assets: ReleaseAsset[];
}

export type Platform = 'windows' | 'macos' | 'linux' | 'other';

const CACHE_TTL_MS = 10 * 60 * 1000;
const cache = new Map<string, { data: Release | null; expires: number }>();

interface GitHubReleaseResponse {
  tag_name: string;
  name: string | null;
  published_at: string;
  html_url: string;
  body: string | null;
  assets: Array<{
    name: string;
    browser_download_url: string;
    size: number;
    content_type: string;
  }>;
}

export function classifyAsset(name: string): Platform {
  const lower = name.toLowerCase();
  if (
    lower.endsWith('.exe') ||
    lower.endsWith('.msi') ||
    lower.includes('windows') ||
    lower.includes('win32') ||
    lower.includes('win64') ||
    lower.includes('win-x64') ||
    lower.includes('x64-installer')
  ) {
    return 'windows';
  }
  if (
    lower.endsWith('.dmg') ||
    lower.endsWith('.pkg') ||
    lower.includes('macos') ||
    lower.includes('darwin') ||
    lower.includes('-apple-') ||
    lower.includes('universal')
  ) {
    return 'macos';
  }
  if (
    lower.endsWith('.appimage') ||
    lower.endsWith('.deb') ||
    lower.endsWith('.rpm') ||
    lower.includes('linux') ||
    lower.includes('ubuntu') ||
    lower.includes('alpine')
  ) {
    return 'linux';
  }
  return 'other';
}

export function formatBytes(bytes: number): string {
  if (!bytes || bytes <= 0) return '';
  const units = ['B', 'KB', 'MB', 'GB'];
  let n = bytes;
  let i = 0;
  while (n >= 1024 && i < units.length - 1) {
    n /= 1024;
    i++;
  }
  return `${n.toFixed(n < 10 && i > 0 ? 1 : 0)} ${units[i]}`;
}

export async function getLatestRelease(repo: string): Promise<Release | null> {
  const now = Date.now();
  const cached = cache.get(repo);
  if (cached && cached.expires > now) {
    return cached.data;
  }

  try {
    const headers: Record<string, string> = {
      Accept: 'application/vnd.github+json',
      'User-Agent': 'chelydra.dev',
    };
    const token = process.env.GITHUB_TOKEN;
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }

    const res = await fetch(`https://api.github.com/repos/${repo}/releases/latest`, {
      headers,
    });

    if (res.status === 404) {
      cache.set(repo, { data: null, expires: now + CACHE_TTL_MS });
      return null;
    }
    if (!res.ok) {
      throw new Error(`GitHub API responded ${res.status}`);
    }

    const json: GitHubReleaseResponse = await res.json();
    const release: Release = {
      tagName: json.tag_name,
      name: json.name || json.tag_name,
      publishedAt: json.published_at,
      htmlUrl: json.html_url,
      body: json.body || '',
      assets: (json.assets || []).map((a) => ({
        name: a.name,
        url: a.browser_download_url,
        size: a.size,
        contentType: a.content_type,
        platform: classifyAsset(a.name),
      })),
    };

    cache.set(repo, { data: release, expires: now + CACHE_TTL_MS });
    return release;
  } catch (err) {
    console.error(`[github] Failed to fetch latest release for ${repo}:`, err);
    // Serve stale cache rather than blowing up the page render.
    if (cached) return cached.data;
    return null;
  }
}
