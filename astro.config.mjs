import { defineConfig } from 'astro/config';
import node from '@astrojs/node';

// SSR via the Node adapter so project pages can fetch live release data
// from the GitHub API at request time. Static pages prerender by default;
// individual routes opt into SSR with `export const prerender = false`.
export default defineConfig({
  adapter: node({ mode: 'standalone' }),
  site: 'https://chelydra.dev',
  compressHTML: true,
});
