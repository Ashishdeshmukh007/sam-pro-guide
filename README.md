# ServiceNow SAM Pro — Zero to Mastery

A single-file, self-contained visual guide to ServiceNow Software Asset Management
(SAM Pro): how the tool works, how to run it end-to-end, and how Microsoft, Oracle,
and IBM licensing plays out inside it — with case studies and a 140-question interview
bank.

**Live:** https://ashishdeshmukh007.github.io/sam-pro-guide/

## What it is

One `index.html`. No build step, no framework, no runtime dependencies — inline CSS,
vanilla JS, and the two fonts (Inter + Sora) embedded as WOFF2 data URIs. It works
offline, loads in one request (~105 KB gzipped), and `Cmd/Ctrl+F` searches the whole
guide. That self-containment is a feature; keep it.

- 11 parts: fundamentals → platform → architecture → operating the tool → Microsoft /
  Oracle / IBM deep dives → SaaS & audit defense → 8 case studies → interview mastery →
  cheat sheets & 90-day plan.
- Dark/light theme (persisted), scroll-spy TOC, per-section "mark done" progress
  (localStorage), question search + quiz mode.

## Develop

Edit `index.html` directly. Before pushing, run the gate:

```bash
npx --yes html-validate@11.5.6 index.html   # markup validity
python3 check.py                            # duplicate ids, dead anchors, JS syntax
```

CI (`.github/workflows/ci.yml`) runs both on every push and PR. GitHub Pages serves
`main` after CI is green.

## Deploy

```bash
./deploy.sh "content: fix Oracle NUP minimum"
```

Runs the gate, commits, pushes to `main` (which GitHub Pages publishes), and syncs the
local reading copy so the two never drift. See `PRODUCTION.md` for the full hardening
record and runbook.

## Files

| File | Purpose |
|---|---|
| `index.html` | the guide (only thing GitHub Pages needs) |
| `check.py` | structural CI checks |
| `.htmlvalidate.json` | validator config |
| `.github/workflows/ci.yml` | CI gate |
| `deploy.sh` | gated deploy + reading-copy sync |
| `og.png` / `og-card.html` | social share image and the fixture that renders it |
| `sitemap.xml`, `robots.txt` | SEO |
| `PRODUCTION.md` | production-hardening ledger + runbook |

## Content currency

Licensing facts age. Every load-bearing claim carries a verification pass logged in
`PRODUCTION.md`; re-check publisher-specific numbers (VMware/Broadcom minimums, M365
plans, ServiceNow release names) before quoting them in a live setting.
