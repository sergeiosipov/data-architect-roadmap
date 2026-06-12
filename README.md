# Fundamentals → Data Architect

A four-year, from-zero study plan to top-tier **Data Architect (financial services / fund industry, Luxembourg)** — plus a mobile tracker app with per-topic timers.

## Contents

- **[STUDY_PLAN.md](STUDY_PLAN.md)** — the complete plan: Phase 0 (computing foundations, every module with a skip test) through Phase 8 (data products & architect practice), 252 taxonomy topics + 31 gap additions, 1,100 h planned against a 1,152 h budget. Read it directly in the GitHub mobile app.
- **[docs/](docs/)** — the **Study Tracker PWA**: each of the 169 study items is a page with its content, a start/stop **timer** that books time to that topic (survives closing the app), status tracking, skip-test bank, journal notes, and hours-vs-budget dashboards. Host on GitHub Pages (`Settings → Pages → main /docs`) or open `docs/index.html` locally. Progress lives in browser localStorage — **export (⬇) weekly** and commit the JSON here as backup.
- **Build scripts** (run with [uv](https://docs.astral.sh/uv/)):
  - `uv run _assemble_and_qa.py` — assembles STUDY_PLAN.md from `_parts/` and runs the QA assertions (coverage, anchors, resources, DAG, budget).
  - `uv run _build_appendix_c.py` — regenerates the coverage matrix from `_worklist.md`.
  - `uv run _build_tracker.py` — regenerates `docs/data.js` for the tracker from the same sources.
- **`_worklist.md`** — the canonical topic/tier/phase list both the document and the app are generated from. Edit here first, then rebuild.

## Tracking discipline

Status changes in the tracker are claims; the evidence lives in the capstone repo (see *Tracking Progress* and *Publishing Your Work* in the plan).
