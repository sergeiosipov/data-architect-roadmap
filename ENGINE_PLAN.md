# Learning Engine — master build plan & status (branch `feature/learning-engine`)

Goal: implement all 30 learning-methodology features, fully + verifiably populated, then deploy ONCE (merge to `main` + Pages). Work stays on this branch until the final deploy so the live study site is undisturbed. No fabrication: every citation / lab golden-output / scenario answer must be source-verified, not invented.

## Architecture principles
- The app (`docs/`) is a no-backend vanilla-JS PWA. State `S` in `localStorage["spt-v1"]`; optional Gist sync merges `S.items` by `u` timestamp. ANY new `S.<sub>` object must (a) be added to the sync payload in `syncNow`, (b) get a merge branch in a `merge*()` helper, (c) be covered by export/import — otherwise it won't sync.
- Content lives in markdown sources (`_parts/*.md`, `_quizzes/<id>.md`, new `_pins/`, `_labs/`, `_scenarios/`); Python `uv` build scripts compile to `docs/*.js`. Keep that split.
- Every build stays green: `uv run _assemble_and_qa.py` (5 asserts), `uv run _validate_quizzes.py`, plus new validators must pass before any commit. Bump `docs/sw.js` cache on each shippable change.
- Lesson id = `it.ids[0]` (e.g. `1.6.1`); quiz/pin/lab/scenario files are keyed by that id. App `INDEX` is keyed by `it.key` (e.g. `e-1.6.1`).

## Data-model additions (localStorage `S`)
- `S.srs[cardId] = {due, ivl, ease, reps, lapses, last, conf}` — spaced-repetition ledger. cardId = `"<lessonId>#<NN>"` (zero-padded) for quiz cards, `"<lessonId>#c<NN>"` for clozes, `"<lessonId>#s<NN>"` for scenarios. Merge: newer `last` wins per card.
- `S.items[key].dw = [bool,...]` — Done-when checkbox state, length-aligned OR-merge.
- `S.items[key].dump`, `.dump2`, `.teach`, `.adr` — free-recall / teach-back / ADR text (newest `u` wins, already carried by item merge once added).
- `S.reg[cellId] = {rating, u}` — regulatory crosswalk self-ratings.
- `S.exams[]`, `S.errata[]` — append-only logs (union-merge by stable id).

## Build-output additions (`docs/`)
- `quizzes.js` → `window.QUIZ = {"1.6.1":[{i,q,a}],...}` (stable-ID quiz data; replaces baked HTML, shrinks data.js).
- `data.js` topic objects gain: `doneWhen:[{text,pin?}]`, `pins:[{b,src,loc,url,quote,archived,audited,status,domain}]`, `verifiers:[{tok,expectHash}]`, `scenarios:<id>`, `worked/faded`, `explain:[...]`.
- `graph.js` → `window.GRAPH` prerequisite DAG edge list.
- `clozes.js`, `scenarios.js` → card pools that join `S.srs`.

## Design constraints (per user steering, 2026-06-14)
NO gamification — maximize learning ROI, not engagement. DROPPED: confidence/"guess" taps, calibration scoring, streaks, forecast/finish-date dashboards, badges, notifications (#5 and #29 removed). Apply ponytail "lazy senior dev": minimal code, no unrequested abstractions, no new deps, deletion over addition, fewest files, mark shortcuts `ponytail:` with ceiling+upgrade path, leave ONE runnable self-check for non-trivial logic; not lazy on validation/security/accessibility. Question over-scope. Priorities, in order: learning PATH & topic/material INTERCONNECTION · material PRECISION + FRESHNESS · methodological CORRECTNESS · control-check questions · scientifically-based spaced-repetition + practice.

## Feature sequence (re-prioritized) & STATUS
Legend: [ ] todo · [~] in progress · [x] done+verified · [×] dropped

### Phase 1 — Spaced-repetition schedule over the control questions  ✅ DONE+VERIFIED
- [x] #1  Stable quiz IDs + grade ledger — build emits `quizzes.js` (126 lessons/12,600 cards); `S.srs` (SM-2-lite); mergeSrs sync; export/import. data.js 7.5MB→684KB.
- [x] #2  Grade-on-reveal (Again/Hard/Good/Easy) on each lesson's self-test → schedules the card.
- [x] #3  `#/review` due-now cross-lesson queue (due first, top-up with new, interleaved) + sober home "due now" tile.
- [×] #5  confidence/calibration — DROPPED (gamification). [×] #29 forecast/streak dashboard — DROPPED.

### Phase 2 — Learning materials: precision · interconnection · freshness  ← user's top ask, NEXT
- [ ] #12 `_sources.yaml` edition/version registry (lock DDIA 2e, Postgres 16, consolidated regs) — kills "ch.7 silently moved".
- [ ] #9  `_pins/<id>.md`: per Learn-bullet exact `§`/`p.`/`@mm:ss` deep anchor; build parses → `pins[]`; render text-fragment / `&t=` links inline on the bullet.
- [ ] #10 Freshness: `_check_links.py` (uv + httpx HEAD; stdlib `urllib` if httpx avoidable — ponytail) → `status` + `last-checked`; offline verbatim quote per pin so a 404 never blocks; Wayback fallback URL.
- [ ] #13 `_validate_pins.py` — coverage % gate + per-pin `audited` date with TTL (methodological correctness; fails build below threshold).
- [ ] #11 Regulatory bullets pinned to PRIMARY source only (EUR-Lex/ISO/SWIFT/FinDatEx article/field) — stricter agent, never a blog.
- [ ] #15 Done-when ⟶ the exact pin + quote that proves it (interconnect check ↔ source).
- [ ] POPULATE (VERIFIED agentic pass, long pole): seed from each bullet's existing parenthetical → resolver agent returns smallest span + verbatim quote, MUST verify against the real source (web/PDF); accept/reject gate; ship only verified pins; Wayback-snapshot on accept. No fabrication.

### Phase 3 — Learning path & interconnection
- [ ] #17 Prerequisite DAG (`_build_graph.py` from coverage-matrix `ids` + cross-refs + `_graph_overrides.md`) → `graph.js`.
- [ ] #18 Per-lesson "requires X (not yet done)" soft note + a single "next best topic" suggestion (topologically eligible). No adaptive-magic over-engineering.
- [ ] #19 Quiz lapses (from `S.srs`) rolled up onto the DAG → "weak cluster: vector indexing; its prereq distance-metrics is shaky."
- [ ] #20 (optional) fund-domain goal → back-chained topic path. Build only if #17/#18 prove useful.

### Phase 4 — Mastery gating & control checks (functional, not points)
- [ ] #14 Stateful mastery-gating Done-when (parse `[ ]` → `S.items.dw`; can't mark `done` until ticked + lesson cards above a retention bar). Criterion-referenced, not a score.
- [ ] #4  Interleave the review queue across topics (desirable difficulty) — small selection tweak, no new file unless needed.
- [ ] #30 Generalize Phase-0 skip-tests to all phases (pass cold → bank hours) + spaced re-assessment drops mastery back if retention checks fail.
- [ ] #8  (optional) self-test exam mode (N questions, answers withheld to end). Functional control check; build if wanted.

### Phase 5 — Practice (verified)
- [ ] #21 `_labs/<key>/` seed fund fixtures + `verify.sh` golden-output checks for hands-on "Do" steps; pass-token hash in build. Start with the few procedural lessons that have machine-checkable outputs.
- [ ] #22 Worked-example → faded-practice for the ~10 hardest procedures.

### Phase 6 — Domain depth (authored + verified, where it earns its place)
- [ ] #26 Regulatory crosswalk (GDPR/DORA/UCITS/AIFMD → lessons) — a table page; cheap, high value.
- [ ] #25 Fund-admin scenario questions for the ~30 fund lessons (application, not recall).
- [ ] #27/#28 explain-to-auditor prompts + ADR/spine project — only if they pull weight.

### Phase 7 — Integration & deploy (single deploy)
- [ ] All validators + assemble green; preview-verify every view; sync of new state tested; bump sw.js cache; README update; merge to `main`; push; confirm live.

DROPPED outright (gamification / low-ROI): #5, #29, #7 heatmap-dashboard, #6 cloze (build only if recall data shows a gap), #16/#23/#24 (extra recall ceremonies — skip unless asked).

## Verification discipline
Every shippable increment: run validators/build, then drive `docs/` in the browser preview (load, exercise the new view, console clean) before committing. Never push to `main` until Phase 7.
