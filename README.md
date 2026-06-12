# Fundamentals → Data Architect

A four-year, from-zero study plan to top-tier **Data Architect (financial services / fund industry, Luxembourg)** — plus a mobile **Study Tracker** app with per-topic timers and free cross-device sync.

- **[STUDY_PLAN.md](STUDY_PLAN.md)** — the complete plan: Phase 0 (computing foundations, every module with a skip test) → Phase 8 (data products & architect practice). 252 taxonomy topics + 31 gap additions, 1,100 h planned against a 1,152 h budget.
- **[docs/](docs/)** — the tracker app (static PWA, no backend): 169 study items, each a page with its content, a start/stop timer, status, journal, skip-test bank, and hours-vs-budget dashboards.

---

## Run the tracker locally

**Option 1 — local web server (recommended; enables offline cache/PWA):**

```powershell
uv run python -m http.server 8731 --directory docs
```

Then open <http://localhost:8731>. Any static server works; port is arbitrary.

**Option 2 — no server at all:** double-click `docs/index.html`. Everything works except the service worker (offline caching) — fine for desktop use.

**On your phone without deploying:** copy the `docs/` folder to the phone and open `index.html` in the browser — or better, deploy once (below) and install it as an app.

---

## Tracker user guide

**First run**
1. Open the app → home screen shows all 9 phases and the budget bar.
2. Take the **skip tests** (Skip List section of STUDY_PLAN.md) for Phase 0. For every module you pass, open it in the app and set status to **⏭ skipped** — its hours go to your "skip-test bank" (visible on the home screen).

**Daily study loop**
1. Open the current phase → tap the topic you're studying.
2. Tap **▶ Start timer**. Study (the topic's full content — Why / Learn / Resource / Do / Done when — is right there on the page).
3. Tap **⏹ Stop & book** when you finish — the minutes are booked to that topic. Closing the app/phone mid-session is fine: the timer is a timestamp, not a running clock; reopen and stop whenever.
4. Forgot the timer? **＋ minutes** adds (or corrects with a negative number) manually.
5. Write one journal line in the topic's note field: *what I did, what surprised me, open question*.
6. When the topic's **Done when** self-test passes, set status **✅ done**. Status meanings: ○ todo · ◐ doing · ✅ done · ⏭ skipped.

**Dashboards:** home shows % complete (done + skipped estimate vs 1,100 h), total hours logged, and the skip bank; each phase shows its own bar and hours.

**Backup:** ⬇ exports a JSON snapshot (commit it to this repo weekly); ⬆ imports and **merges** it on another device.

**Cross-device sync (free, via a secret GitHub Gist)**
1. GitHub → *Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token*. Tick **only the `gist` scope**.
2. In the app: home → **set up sync** → paste the token → *Save & sync now*. The first sync creates a secret gist and shows its ID.
3. Second device: same screen → paste the same token **and** the Gist ID → *Save & sync now*.
4. From then on it auto-syncs a few seconds after you stop a timer or change a status/note; ⟳ in the top bar forces a sync; ⚠ means the last sync failed (tap *sync settings* for the reason).
5. Merge rules: time sessions from all devices are combined (nothing double-counted or lost); the newest status and journal note win; a *running* timer stays on its own device.

**Install as an app:** once deployed (below), open the URL on your phone → browser menu → **Add to Home Screen** (Android Chrome and iOS Safari). It launches standalone and works offline.

---

## Deploy (free)

**Option A — GitHub Pages (public repo):**

```powershell
gh repo create data-architect-roadmap --public --source . --push
```

Then on github.com: **Settings → Pages → Deploy from a branch → `main` / `docs/`** (or via CLI: `gh api repos/{owner}/data-architect-roadmap/pages -X POST -f "source[branch]=main" -f "source[path]=/docs"`). After ~1 minute the tracker is live at `https://<username>.github.io/data-architect-roadmap/`. Note: the *plan* becomes public; your progress, journal, and token never leave your devices and the secret gist.

**Option B — private repo + Cloudflare Pages:**

```powershell
gh repo create data-architect-roadmap --private --source . --push
```

Then in the Cloudflare dashboard: **Workers & Pages → Create → Pages → Connect to Git** → pick the repo → framework preset *None*, build command *(empty)*, output directory `docs` → Deploy. Free, and the repo stays private.

**Option C — no deploy:** keep using it locally (see *Run locally*); sync still works from localhost or `file://` since it calls the GitHub API directly.

---

## Maintaining / rebuilding

The plan and the app are generated from the same sources: `_worklist.md` (canonical topic/tier/phase list) and `_parts/*.md` (section content). After editing them:

```powershell
uv run _build_appendix_c.py    # regenerate the coverage matrix from the worklist
uv run _assemble_and_qa.py     # assemble STUDY_PLAN.md + run QA assertions (must all PASS)
uv run _build_tracker.py       # regenerate docs/data.js for the tracker
```

Commit and push — Pages redeploys automatically. Tracker progress is keyed by stable item IDs, so regenerating content does not touch your logged time or statuses.

## Tracking discipline

Status changes in the tracker are claims; the evidence lives in your capstone repo. See *Tracking Progress* and *Publishing Your Work* in [STUDY_PLAN.md](STUDY_PLAN.md).
