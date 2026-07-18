# Production Status — SAM Pro Zero-to-Mastery Guide

Tier: A-static (confirmed 2026-07-18 — public free content site, no accounts/payments/user data; human answered scope batch)
Current phase: 1 — Correctness net (CI)
Next task: CI workflow with HTML validation + anchor/dup-ID checks; prove red→green gate

## Inventory
- **App:** single-file static HTML learning guide (`index.html`, 3,003 lines, 339KB raw / 105KB gzipped). Inline CSS + vanilla JS. No build step, no framework, no JS deps.
- **External deps:** Google Fonts only (Sora 3 weights + Inter 4 weights, `display=swap`).
- **State:** localStorage (theme + per-section "mark done" progress). No backend, no data store.
- **Deploy:** GitHub Pages, legacy build, repo `Ashishdeshmukh007/sam-pro-guide` (public), live at https://ashishdeshmukh007.github.io/sam-pro-guide/
- **Source-of-truth problem:** master copy also at `/Users/Ashish/Learnings/ServiceNow SAM Pro Training/SAM-Pro-Zero-to-Mastery-Guide.html` — currently byte-identical (sha b82eabee…) but synced by hand; no local clone existed until this audit (cloned to `~/Projects/sam-pro-guide`).
- **Content:** 11 parts, ~30k words, 140 Q&A accordions, 4,294 DOM elements. Built 2026-07-11 from training PDFs + web research of that date. No source citations or "last verified" dates in the document.

## Red flags
- **None (security):** no secrets, no eval, no inline event handlers, no forms, no user input beyond search box (client-side filter only).
- **No CI:** nothing validates HTML/links/JS before a push goes live.
- **No sync mechanism** between Learnings master and repo — divergence is one edit away.
- **SEO/meta:** no meta description (Lighthouse fail), no OG/Twitter cards, no canonical URL.
- **A11y (Lighthouse 98):** heading-order violations (h3 after h1 in hero; h5 in case studies), comparison tables use `<td>` for row headers instead of `<th scope="row">`.
- **Supply chain/privacy:** Google Fonts = 3rd-party request on every load (fails closed OK — `display=swap` + system font fallbacks present).
- **Content drift risk:** licensing facts (VMware/Broadcom minimums, M365/Copilot, ServiceNow release names, SAM Pro AI features) age quickly; guide is a point-in-time snapshot with no verification trail.

## Verified good (evidence this session, 2026-07-18)
- Local master ↔ deployed: byte-identical (shasum b82eabee230be54fcaf1aaf36a3e7a039d5e76e7 both).
- Lighthouse (desktop, live URL): **A11y 98, Best Practices 100, SEO 90, Agentic 100**. 3 fails: heading-order, td-has-header, meta-description.
- Transfer: 105,465 bytes gzipped, total load 63ms. Perf is a non-issue.
- **No-JS resilience:** `.pre` (opacity:0 reveal) is added BY JS — with JS off/failed, full content renders. Verified in source (line 2923).
- Reduced-motion media query present; focus-visible styles present; print stylesheet present; light/dark themes with pre-paint theme script.

## Gap report (static-site adaptation of phases)
- Phase 1 (correctness): NO CI. Required: HTML validation + internal-anchor link check + JS smoke test on push.
- Phase 2 (security): clean. Remaining: self-host fonts (removes only 3rd-party dep), meta CSP optional (GitHub Pages can't set headers).
- Phase 3 (failure design): PASS already (no-JS safe, font fallback safe, no external calls at runtime).
- Phase 4 (data safety): git history = backup. localStorage progress is expendable. N/A beyond that.
- Phase 5 (observability): N/A at Tier A static (GitHub Pages status page suffices). Logged as decision.
- Phase 6 (deploy discipline): THE gap. Required: repo = canonical source, one-command deploy that also syncs Learnings copy, CI gate before Pages deploy.
- Phase 7 (UX floor): a11y fixes above; mobile TOC is a static block pushed above content (<980px) — check usability; otherwise good.
- Phase 8 (perf): PASS (105KB gz). Optional: font subsetting when self-hosting.
- Content (the real "correctness" for a content product): needs fact-check + currency pass with sources — this is the deep-research work.

## Decisions
- 2026-07-18 — Cloned repo to ~/Projects/sam-pro-guide; this becomes the working copy. — agent (deploy discipline prerequisite)
- 2026-07-18 — Repo will be canonical source; Learnings copy becomes a synced artifact of deploy. — agent (single source of truth; user's reading habit preserved by sync-back)
- 2026-07-18 — ⚑ Content scope: **verify + update + expand** (fact-check all load-bearing claims, correct in place, add 2026-current gaps), sources logged. — human
- 2026-07-18 — ⚑ Structure: **stays single-file** — self-containment is the product feature; all UI/a11y work in-place. — human
- 2026-07-18 — Tier A-static: Phase 4 = git history (sufficient), Phase 5 = skipped (GitHub Pages status page; no runtime to observe). — agent per playbook tier matching

## Runbook
Deploy: (to be defined Phase 6)   Rollback: git revert + push (to be proven Phase 6)

## Backlog
- README.md for the repo (has none).
- Consider font subsetting (Sora+Inter, latin subset) when self-hosting.

## Incidents
- none
