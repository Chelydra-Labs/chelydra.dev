---
title: Silt
tagline: Capture the flow. Map the connections. Let your thoughts settle.
description: >
  Silt is a lightweight, super-fast note-taking app for capturing
  stream-of-consciousness thoughts and mapping them to one another.
  Built with Go + Wails + Svelte 5 — no Electron, idle RAM under 65MB.
  Plaintext Markdown is the source of truth; a native SQLite cache projects
  your notes into Agenda, Calendar, and Kanban views.
repo: Chelydra-Labs/Silt
homepage: https://github.com/Chelydra-Labs/Silt
docs: https://github.com/Chelydra-Labs/Silt#documentation
license: MIT
language: Go
order: 1
featured: true
accent: '#5B8DEF'
published: 2025-01-01
---

## What it is

Silt bridges the gap between structured namespace notebooks and chronological
block-based daily streams. Notes are organized **Notebook > Section > Page**,
and each Page is a single Markdown file on disk whose blocks carry their own
dates. Your data never gets locked inside a proprietary database.

## Highlights

- **Notebook > Section > Page hierarchy** — folders on disk; each Page is a single `.md` file.
- **Smart Graph** — hierarchical slash tags (`#work/project/milestone`), global block references (`((uuid))`), and live embeds.
- **Themeable** — driven by a single JSON theme file. Five themes ship built-in; drop your own in `<vault>/.system/themes/`.
- **Plugin SDK** — Agenda, Calendar, and Kanban are built on the same SDK available to third-party plugins.
- **No file lock-in** — flat directories of basic Markdown.
- **Zero-bloat performance** — no Electron. Sub-16ms input rendering.
- **Fail-safe design** — atomic staging protocol prevents file corruption.

## Platform support

Windows and Linux are first-class. macOS is not blocked but is not specifically built or tested against.
