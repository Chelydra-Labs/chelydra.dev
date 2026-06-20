# chelydra.dev

Source for [chelydra.dev](https://chelydra.dev) &mdash; the home for **Chelydra Labs** open-source projects.

Built with [Astro](https://astro.build) in SSR mode (Node adapter), deployed on [Railway](https://railway.com) via Railpack.

## Stack

- **Astro 5** (SSR via `@astrojs/node`, `mode: 'standalone'`)
- **Content Collections** for project pages (`src/content/projects/*.md`)
- **Live release data** fetched at request time from the GitHub Releases API, cached ~10 min
- **Inter** + **JetBrains Mono** (self-hosted via `@fontsource-variable`)
- Brand tokens per [`DESIGN.md`](./DESIGN.md)

## Add a project

Drop a Markdown file in `src/content/projects/`:

```md
---
title: My Project
tagline: One-line elevator pitch.
description: Longer description for SEO / cards.
repo: Chelydra-Labs/my-project
license: MIT
language: Rust
order: 2
featured: true
---

## What it is

Markdown body for the project page.
```

The filename becomes the URL (`my-project.md` &rarr; `/projects/my-project`). The latest release + downloads are pulled automatically from `repo`. No code changes needed.

## Local development

```bash
npm install
npm run dev      # http://localhost:4321
```

Optional env (see `.env.example`):

- `GITHUB_TOKEN` &mdash; raises the unauthenticated rate limit (60&rarr;5000/hr) for release fetches
- `CONTACT_EMAIL` &mdash; override the default `turtle@chelydra.dev`

## Regenerate favicons / OG image

After replacing `src/assets/logo.png`:

```bash
python scripts/generate-favicons.py
```

Outputs `favicon.ico`, PNG icons, and `og-image.png` to `public/`.

## Deploy

Railway auto-deploys from `main`. The Node SSR server starts via:

```bash
node ./dist/server/entry.mjs
```

Astro respects `HOST` and `PORT` (Railway injects `PORT`). Healthcheck at `/health`.

## Email protection

The contact address is never shipped in plaintext HTML. The `EmailLink` component renders a munged form, then an inline script decodes the address from a base64 payload on the client and installs the real `mailto:` href. A `<noscript>` fallback shows the munged form for non-JS visitors.

## License

MIT
