# Visual Mapping Strategy — Phase 0

> **Status: built.** All of it ships in `index.html`, +14 KB (3%), no new dependencies,
> `html-validate` + `check.py` green, zero console errors.
>
> | Item | Outcome |
> |---|---|
> | 3.2 architecture | Built — traced data paths, hover or pin a chain |
> | 3.10 order of operations | Built — reused `.flow`, added scroll-drawn spine |
> | 6.5 Oracle partitioning | Built — 3-beat rack, 2 → 32 cores, 1 → 16 licenses |
> | 7.2 IBM sub-capacity | Built — ILMT-lapse snap-back to a full-capacity bill |
> | 8.2 + 11.5 timelines | Built — `.tl.drawn`, phase bars fill on scroll |
> | 5.2 / 6.2 / 7.1 figures | **Not needed** — `.calc` and `.rack` figures already existed and already reveal on scroll. Manufacturing new ones would have been churn. |
>
> Two mechanisms came out of it, both reusable: `.drawn` (opt-in scroll-drawn progress on
> `.flow` and `.tl`) and `.rk` beat racks (one visual, several scenarios, driven purely by
> a `data-beat` attribute). Each is opt-in, so the 16 other flows and 3 other timelines are
> untouched.


Zero Content Loss: nothing below deletes prose. Every visual either sits *above* the
text it introduces or *wraps* text that is reproduced verbatim inside it.

## Constraints this repo imposes on the playbook

Two conflicts with the PDF, both worth resolving before Phase 1:

1. **No CDN.** `index.html` is one self-contained file — inline CSS, vanilla JS, fonts
   as WOFF2 data URIs, zero external requests, works offline (README: "That
   self-containment is a feature; keep it"). Phase 1 says install GSAP/Tailwind/
   framer-motion from CDN. That breaks the invariant, adds ~120 KB of network, and is
   redundant: the file already runs 18 `@keyframes`, 6 `IntersectionObserver`s, 4
   CSS `animation-timeline` scroll-driven animations, and 8 `prefers-reduced-motion`
   guards. **Skip Phase 1.** Everything below is buildable on what's already there.
2. **No hosted video.** A real MP4 can't be data-URI'd into a 460 KB single file. Where
   the playbook says "explainer video", this plan substitutes a scripted, scroll-scrubbed
   SVG/CSS sequence — same pedagogy, no external asset, no bitrot.

Also note the mock's design language (indigo glow, glass panels, blob blur) is not this
site's. Recent commits established an editorial *ledger* aesthetic. Visuals below should
inherit existing `.pipeline` / `.arch` / `.flow` / `.node` styling, not replace it.

## 1. Three sections → scroll-triggered infographics

| # | Section | Why it fits | Text preservation |
|---|---|---|---|
| 1 | **3.10 Under the hood: reconciliation's order of operations** | Strictly ordered steps; readers currently have to hold the sequence in their head. Vertical timeline with a fill-on-scroll spine, one node per operation. | Each node's headline is the exact step wording; the full original paragraph sits directly beneath its node — no accordion, no summarizing. |
| 2 | **8.2 Implementation methodology (how engagements actually run)** | Phase-by-phase engagement arc — the canonical timeline shape. | Phase label + first two sentences in the node; remainder of the exact paragraph renders below the node in the same card. |
| 3 | **11.5 Your first 90 days on a SAM Pro project** | Already a 30/60/90 structure; a horizontal scrub timeline makes the pacing legible at a glance. | Every bullet preserved verbatim as node content. Nothing dropped. |

Runner-up if a fourth is wanted: **4.1 The operating rhythm** as a looping cadence dial
feeding into walkthroughs 4.2–4.8.

## 2. Two topics → animated explainers (in-page SVG sequence, not video)

**A. 6.5 Virtualization: hard vs soft partitioning (the VMware problem)**
Script: a 2-host vSphere cluster, 4 VMs, one running Oracle DB. Beat 1 — user sees 2
licensed cores. Beat 2 — vMotion arrow moves the VM; the licensable boundary expands to
the whole cluster; the counter runs up. Beat 3 — the same estate under hard partitioning
(LDOM/Solaris zones) with the boundary staying put. Closing frame: the two totals
side by side. This is the single most expensive misunderstanding in the guide; watching
the number climb teaches it faster than the paragraph does.
Placement: above §6.5's existing text, which stays intact underneath.

**B. 7.2 Full capacity vs sub-capacity: the money concept**
Script: a 16-core box, one WebSphere instance pinned to 4 cores. Beat 1 — full-capacity
PVU math bills all 16. Beat 2 — ILMT is installed and reporting; the billable region
shrinks to 4. Beat 3 — ILMT lapses past the 30-day window and the box snaps back to 16.
The snap-back is the lesson.
Placement: above §7.2, ahead of 7.3's ILMT discussion; original text untouched.

## 3. High-res architecture diagrams

Vector, inline, theme-aware — not photos. Screenshots of a ServiceNow instance would
bloat the file and go stale within a release cycle.

- **3.2 Full architecture on one screen** — the existing `.arch` column grid becomes an
  annotated SVG with hover-revealed connectors between data sources → normalization →
  entitlement → reconciliation → outputs. Highest-value single diagram in the guide.
- **5.2 Windows Server: core licensing, visually** — a physical-core grid that fills to
  show the 8-per-proc / 16-per-server minimums and where the pack math lands.
- **6.2 Processor licensing: cores × core factor** — socket → core → core-factor →
  licence-count chain as one left-to-right figure.
- **7.1 PVU, visually** — processor class → PVU-per-core table rendered as a scaled bar
  so relative weight is visible, not looked up.
- **3.1 five-stage pipeline** — already visual (`.pipeline`); upgrade only, scroll-scrub
  the arrows rather than rebuild.

## 4. Keep exactly as text — do not visualize

These are reference surfaces. Their value is `Cmd+F`, scanability, and copy-paste; a
visual layer would actively degrade them.

- **All of Part 10** (71 KB, 120 Q&A) — already has search + quiz mode. Leave it.
- **11.6 Glossary** and **1.3 Vocabulary** — definition lists, scanned not read.
- **The three calculation cookbooks** (5.10, 6.11, 7.10) — worked arithmetic; the
  step-by-step text *is* the artifact.
- **11.2 / 11.3 crib cards and publisher pocket guides** — dense-by-design lookup tables.
- **Part 9 case studies** — narrative; the story is the mechanism.
- **8.4 audit-defense playbook** — sequenced prose whose caveats don't survive
  compression into nodes.
- **5.9 / 6.10 / 7.9 agreement deep dives** — contractual nuance; diagrams would imply
  a precision the terms don't have.

## Suggested build order

3.2 architecture SVG → 3.10 infographic → 6.5 explainer → 7.2 explainer → 11.5 →
8.2 → the three publisher figures. Each is independently shippable; run
`npx html-validate index.html && python3 check.py` after every one.
