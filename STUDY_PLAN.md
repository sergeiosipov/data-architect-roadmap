# Study Plan: Fundamentals → Data Architect

**Target:** top-tier Data Architect for financial services / the fund industry (Luxembourg: investment funds, asset management, regulatory data) — **starting from zero**. Nothing is assumed: Phase 0 teaches the computing foundations (Linux, Python, SQL, Git, Docker, networking), and every foundation module has an explicit **skip test** — you decide what you already know, the plan doesn't decide for you.
**Budget:** 6 h/week × 48 weeks × 4 years ≈ **1,152 h**. Full from-zero path: **1,100 h** = 927 h in phases + 173 h Appendix A gap additions (4.5% slack). Every Phase-0 skip test you pass returns its hours to slack; with all of Phase 0 skipped the load is **964 h** (16% slack).
**Tiers:** **T1 Master** — can design, implement, debug, and teach it (48 topics, 19%). **T2 Working** — can use, evaluate, integrate, and make build/buy decisions (109 topics, 43%). **T3 Awareness** — can recognize it, explain tradeoffs, know when to go deeper (90 topics, 36%).
**Tooling policy (dual-track):** every exercise and capstone runs on **FOSS/source-available, free, Docker-composable on a laptop**; each FOSS pick is paired with the **corporate/cloud leader** actually named in EU financial-services job ads and vendor selections (see [Appendix D](#appendix-d)). Primary cloud: **Azure**; AWS/Databricks/Snowflake at evaluation level.
**Coverage guarantee:** all 252 taxonomy subcategories appear exactly once — in a phase (0–8) or [Excluded](#excluded). [Appendix C](#appendix-c) is the authoritative matrix; the [Skip List](#skip-list) is a self-assessment gate, not a coverage bucket.
**Sequencing:** phases are ordered by prerequisite dependency, not taxonomy order; each phase's capstone reuses the previous one's artifacts, ending in one governed, productized fund-data platform.

<a id="how-to-use"></a>
## How to Use This Document

1. **Day one: take each [Phase-0](#phase-0) module's Skip test.** Each module's *Done when* checklist is its Skip test — work through them honestly, on a real machine, not in your head. Mark each module *do* or *skip*. That marked-up list is your personal starting line — revisit it only to downgrade a "skip" you regret.
2. **Work the phases strictly in order.** Each phase's prerequisites and capstone build on the previous one (the dependency chain is checked: 0→1→…→8). Inside a phase, take the T1/T2 entries roughly top to bottom; the T3 table can be sprinkled into spare half-hours anytime within the phase.
3. **Read a topic entry as a contract:** *Why* tells you what the topic buys you in the target role — if it doesn't resonate, reread it after the Do. *Learn* is the checklist of concepts you must be able to explain. *Resource* is ONE primary source — resist collecting alternatives; the alternate is only for when the primary doesn't land. *Tools* is dual-track: **FOSS** = install and use it; **Corp** = evaluation level, meaning you can explain in a meeting what it costs, when it wins, and what locks you in — without ever installing it. *Do* is non-negotiable: the exercise *is* the learning. *Done when* is the exit gate — self-test it before moving on. *Est. hours* is a planning estimate, not a quota: stop when *Done when* is true.
4. **Tier discipline:** **T1** topics get everything — do, redo, and be able to teach them; they are your interview spine. **T2** = complete the entry once, honestly. **T3** = read the one linked source for the listed minutes and move on; depth there is a deliberate non-goal — return only when a real project demands it.
5. **Never skip a capstone.** Capstones are where the 252 topics compose into one platform; they are also your portfolio. Every capstone runs free and local (Docker Compose on a laptop) and lives in one Git repository that grows for four years — by Phase 8 it contains the full C4 set, 24+ ADRs, and a walkthrough you can present in any interview or review board.
6. **Weekly rhythm (6 h):** a workable default is 2 h reading + 3 h hands-on + 1 h notes/review. Keep a short learning journal (one entry per study day: what, surprise, open question) — Phase 1 onward you'll also accumulate ADRs, and the journal is where they start.
7. **Track progress** with the system in [Tracking Progress](#tracking-progress) — the master checklist is [Appendix C](#appendix-c) (all 252 IDs) plus the A.1–A.31 additions in [Appendix A](#appendix-a).
8. **If you fall behind**, spend the slack in this order: defer T3 reads to the next phase → trim T2 *Do* exercises to their minimal version → stretch the phase calendar. Never cut T1 entries or capstones — and never "catch up" by reading without doing.
9. **When a link or tool has moved on** (resources verified June 2026; the data world won't sit still): keep the *topic* and replace the resource with the current equivalent doing the same job — one primary, no hoarding. [Appendix B](#appendix-b) shows which book/chapter serves which phase; [Appendix D](#appendix-d) is the build-vs-buy cheat sheet to reread before any vendor meeting or interview.
10. **Don't reorganize the plan while inside it.** Mid-phase doubts about sequencing are usually fatigue, not insight. Reassess scope only at phase boundaries — the capstone acceptance criteria tell you whether you've actually earned the next phase.

<a id="tracking-progress"></a>
## Tracking Progress

Progress in this plan is **evidence, not hours**. A topic is done when its *Done when* passes and the artifact exists; everything below just makes that visible.

- **The master checklist.** On day one, copy [Appendix C](#appendix-c) plus the A.1–A.31 rows from [Appendix A](#appendix-a) into a `PROGRESS.md` (or spreadsheet) in your capstone repo, adding three columns: `Status` (`todo / doing / done / skipped`), `Date`, `Evidence` (link to the commit, memo, ADR, or journal entry that proves *Done when*). One row per ID — 283 rows total. A row without an evidence link is not done.
- **The skip ledger.** Record every passed Phase-0 skip test in the same file with the hours banked. This is your personal slack budget — when an entry overruns its estimate, charge the overrun against the ledger so you always know where you stand against the 1,152 h envelope.
- **Weekly (15 min, same day each week):** tick rows, log actual hours vs. estimate, and write one journal line per study day — *what I did, what surprised me, one open question*. The open questions become interview answers later; don't skip them.
- **Per phase boundary (the gate review):** (1) run the capstone acceptance criteria as a literal checklist — every unmet criterion blocks the next phase; (2) tag the repo (`phase-1-done`, …); (3) re-test yourself on three *Done when* questions sampled from earlier phases — failed retention means a scheduled 1 h refresher, not a shrug; (4) apply the falling-behind protocol (How to Use, point 8) to anything slipping.
- **Quarterly (30 min):** compare cumulative hours against the phase map, decide defer/trim/stretch explicitly, and write one paragraph: "what can I design today that I couldn't three months ago?" If the answer is thin, the *Do* exercises are being skimmed.
- **The portfolio is the ultimate tracker.** By the end, the repo should show: 9 capstone tags, the C4 set, 24+ ADRs, the DDD context map, the DCAM self-assessment, the obligation→control matrix, and the build-vs-buy memos. If `PROGRESS.md` says "done" but the repo doesn't show it, the repo is right.
- **Mobile tracker app.** This repo ships a companion PWA (`docs/`) generated from the same canonical worklist: every topic is a page with its study content, a **start/stop timer** that books time to that topic (it survives closing the app — elapsed time is computed from the start timestamp), status (todo/doing/done/skipped), per-topic journal notes, the skip-test bank, and hours-vs-budget dashboards. Host it free on GitHub Pages (or open `docs/index.html` directly on the phone). **Cross-device sync** is built in via a secret GitHub Gist: in the app, open *set up sync* and paste a classic GitHub token with only the `gist` scope — devices then merge automatically (time sessions are unioned, newest status/notes win). The ⬇/⬆ JSON export/import remains as the offline backup path.

<a id="publishing"></a>
## Publishing Your Work (GitHub & LinkedIn)

The capstones are designed to be portfolio pieces — publish them; visibility compounds into recognition just like certifications do.

- **Repo strategy:** one evolving repo, `fund-data-platform`, tagged per phase (`phase-1-done` … `phase-8-done`) — its history *is* the four-year story. Additionally, polish 2–3 flagship capstones into standalone repos with their own READMEs (best candidates: the lakehouse (2), the streaming spine (4), the LLM extraction pipeline (7)).
- **README template per published repo:** what problem it solves (fund-data framing, one paragraph) → architecture diagram (C4 container level, exported image) → stack table *with the corporate equivalents column* (that's what makes it read as architect work, not tutorial work) → how to run (`docker compose up`, ≤10 commands) → 3 things I'd do differently. Add a `LICENSE` (MIT) and make sure no real personal data and nothing from an employer ever lands in it — Faker/SDV data only.
- **LinkedIn cadence:** one post per phase boundary (≈ every 5 months) — what you built, the architecture diagram as the image, three concrete lessons, link to the repo. Write it from the *Done when* answers and journal "surprises", not marketing language. Quiet months are fine; eight substantial posts over four years beats weekly noise.
- **What not to publish:** the obligation→control matrix and DCAM assessment reference your thinking about regulated environments — keep them in the private tracking repo; summarize insights in posts without naming any employer's specifics.

<a id="certifications"></a>
## Certification Path (professional recognition)

The plan's content already covers these syllabi — certification is **recognition, not learning**. Each exam needs ~25–40 h of dedicated prep (practice exams, gap drills) **on top of the plan budget**: with the full from-zero path's thin slack, take at most one exam per six months and prefer the Tier-1 three unless your employer funds more. Prices are mid-2026 ballparks — check current ones; many employers (and Microsoft training-day vouchers) cover them.

**Tier 1 — take these; they define recognition for this exact role (Data Architect, EU financial services, Azure):**

| Certification | Take after | Why it's worth it | Ballpark |
|---|---|---|---|
| **CDMP Practitioner** (DAMA) — DMF exam + 2 specialist exams (recommend *Data Modelling* + *Data Governance* or *Metadata*) | Phase 6 | *The* data-management credential in financial services and governance-heavy organizations; CDMP is routinely named in EU fund-industry data-office job ads. The plan's DMBOK/DCAM work in Phase 6 is the prep. | ~$300/exam ×3 |
| **AZ-305 Azure Solutions Architect Expert** (requires AZ-104 first) | Phase 5 | The architect-level Azure badge — strongest cloud-credential signal for architect titles in Microsoft-dominated markets like Luxembourg. Honest caveat: AZ-104 (admin) contains sysadmin material this plan doesn't teach — budget ~30 h extra for it. | ~€170/exam ×2 |
| **TOGAF Enterprise Architecture** Foundation + Practitioner (The Open Group) | Phase 8 | The EA passport in EU institutions and consultancies; pairs with the Phase-8/A.8–A.10 work. Hold it lightly in practice, but the badge opens architecture-board doors. | ~$550 combined |

**Tier 2 — high market currency; add by specialization or employer stack:**

| Certification | Take after | Why | Ballpark |
|---|---|---|---|
| **Databricks Certified Data Engineer Professional** (Associate first if you want a stepping stone) | Phase 4–5 | Strongest lakehouse/Spark signal in the job market; the exam guide is already embedded in this plan's cross-check. | ~$200/exam |
| **DP-700 Fabric Data Engineer Associate** | Phase 5 | The Azure data-platform badge recruiters filter on as Fabric displaces Synapse; free Microsoft practice assessment available. | ~€170 |
| **CCDAK** (Confluent Certified Developer for Apache Kafka) | Phase 4 | Streaming credibility with a compact, fair exam; Phase 4 is direct prep. | ~$150 |

**Early option for the from-zero path:** **DP-900 Azure Data Fundamentals** after Phase 1 — cheap (~€110), gentle, and a real confidence marker that the foundations stuck; skip it if you passed most Phase-0 skip tests.

**Deliberately not recommended for this profile** (know why, in interviews): AWS SAA/SAP (Azure-primary market — keep the free SAP-C02 exam guide as a competency checklist, as Appendix A does), SnowPro Advanced Architect (only if the employer is a Snowflake shop), CKA (only for platform-engineering-heavy roles), ITIL 4 Foundation (cheap HR checkbox in some Lux institutions — take it only if asked; A.13 covers the substance), EDM Council DCAM/CDMC certified training (high signal in fund-industry data offices but member-gated and expensive — employer-funded only).

**Renewal reality:** Microsoft role-based certs renew annually via a free online assessment; Databricks expires after 2 years; CDMP needs continuing-education credits every 3 years; TOGAF doesn't expire. Put renewals in the quarterly review.

<a id="phase-map"></a>
## Phase Map

The phase sequence — months, hours and capstone — now leads **each phase**: every phase heading is followed by a one-line locator (with prev/next navigation), and the same map is the home screen of the [tracker app](#tracking-progress). Budget reconciliation: 927 h of phase work + 173 h [Appendix A](#appendix-a) gap additions = **1,100 h** vs the **1,152 h** budget (4.5% slack; **964 h / 16%** if all of Phase 0 is skip-tested out). Phases run strictly in order, 0 → 8; each phase's capstone reuses the previous one's artifacts, ending in one governed, productized fund-data platform. Jump in: [Phase 0](#phase-0) · [1](#phase-1) · [2](#phase-2) · [3](#phase-3) · [4](#phase-4) · [5](#phase-5) · [6](#phase-6) · [7](#phase-7) · [8](#phase-8).

<a id="skip-list"></a>
## Skip List

Nothing is skipped by assumption. **Each Phase-0 module's *Done when* checklist is also its Skip test** — the criteria, and the hours you bank by passing them cold, live in each module under [Phase 0](#phase-0). Take each honestly: tick every box cold today → skip that module and bank its hours as slack (up to the full **136 h** of Phase 0); any box you can't → do the module. No other phase is skippable. Record what you bank in the skip ledger ([Tracking Progress](#tracking-progress)).


<a id="phase-0"></a>
## Phase 0: Computing & Data Foundations — from zero (months 1–6, 46 h + 90 h Appendix A)

*Phase 0 of 8 · months 1–6 · 136 h total (46 h in-phase + 90 h foundation modules) — every hour skip-testable · capstone: Personal data toolbox.*  start · [Phase 1](#phase-1) →

**Goal:** everything later phases silently stand on, taught from nothing: a Linux working environment, Python, SQL, Git, Docker, how networks and the web work, what data physically is, and the daily toolkit (pandas, notebooks, tests, code review). **Nothing in this plan assumes prior knowledge** — instead, **each module's *Done when* checklist doubles as its Skip test**. If you can tick every box cold today → skip the module and bank its hours as slack (the mechanism is summarized in the [Skip List](#skip-list)). Any box you can't → do the module.
**Entry prerequisites:** none. A computer with admin rights is enough.
**Exit criteria:** you can (1) live in a terminal (navigate, pipe, grep, ssh, write a small script); (2) write a Python program that reads files, calls functions you wrote, and runs under `uv`; (3) answer questions from a multi-table database with joins, aggregation, and a window function; (4) commit, branch, and open a pull request; (5) run a two-service Docker Compose stack; (6) explain what happens between typing a URL and seeing a page.

> Module numbers (0.1–0.12) are referenced from the coverage matrix. Do 0.10 (editor setup) alongside 0.1–0.2, not after 0.9 — it's numbered late only to keep taxonomy grouping tidy.

### Modules

#### 0.1 — A.27 Linux, the command line & shell
- **Why:** The terminal is the substrate of everything later — Docker, Kubernetes, CI, cloud shells, log forensics — and the architect who can't grep a transfer-agency log under pressure delegates the one task that needed their own eyes. Data work without shell fluency is permanent friction: every later phase of this plan assumes you live here.
- **Learn:**
    - your native Ubuntu lab — confirm the release, update packages, and keep all projects under `~` (the home directory) *(Ubuntu CLI tutorial)*
    - cross-platform awareness — colleagues on Windows use WSL2, on macOS use Terminal + Homebrew; the shell skills here transfer unchanged to all three *(Missing Semester lec. 1)*
    - filesystem layout & permissions — /etc vs /home vs /var, rwx bits, sudo, and why a loader script can't write where it wants *(TLCL part 1)*
    - navigation, files, pipes & redirection — composing small tools with `|`, `>`, `>>` instead of opening editors *(Missing Semester lec. 1)*
    - grep/sed/awk at reading level — enough to filter a NAV-feed log and extract a column *(Missing Semester lec. 4)*
    - environment variables & PATH — why "command not found" happens and how shells find programs *(TLCL part 2)*
    - ssh — keys, agents, remote shells; the access pattern for every server and cloud VM later *(Missing Semester lec. 5)*
    - a first bash script — shebang, arguments, exit codes, `set -euo pipefail` from day one *(TLCL part 4)*
    - package managers — apt install/update/remove and where software actually lands *(TLCL part 3)*
- **Resources:**
    - **[The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)** — lectures 1–5 + exercises: shell, shell tools, data wrangling, command-line environment (primary)
    - [The Linux Command Line](https://linuxcommand.org/tlcl.php) (TLCL, Shotts — free book) — permissions, environment, package management and scripting in proper depth (reference)
    - [Ubuntu command-line tutorial](https://ubuntu.com/tutorials/command-line-for-beginners) — your native OS: shell, files and packages on Ubuntu itself (setup)
    - [crontab.guru](https://crontab.guru/) — decode and compose cron schedules for the exercise (reference)
- **Tools:**
    - FOSS (hands-on): [Ubuntu](https://ubuntu.com/) + GNOME Terminal — your native lab for four years (↔ [WSL2](https://learn.microsoft.com/windows/wsl/) on Windows, Terminal + Homebrew on macOS — identical shell skills)
- **Do:**
    1. On your Ubuntu laptop, confirm the release with `lsb_release -a`, run `sudo apt update && sudo apt upgrade`, and create a `~/lab/phase0` directory tree from the terminal only.
    2. Write `fetch_count.sh`: `curl` downloads a public CSV (any ECB series works), `grep -c` counts rows matching a pattern passed as `$1`, and a `date`-stamped line is appended to `run.log` with `>>`.
    3. Harden it: `set -euo pipefail`, a usage message when `$1` is missing, non-zero exit on download failure; prove each path with a deliberate failure.
    4. Schedule it with cron (compose the expression with crontab.guru), let it run a few cycles, and confirm `run.log` grows; note where cron's own output goes.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 12 h)*
    - [ ] Daily file work (move, inspect, search) happens in the terminal without reaching for the file explorer.
    - [ ] Find all `.csv` under a directory tree, count pattern matches through a pipe, fix a permission error, and ssh into a machine — cold.
    - [ ] Explain every field of your crontab line, what `$PATH` does, and read an unfamiliar pipeline (`grep ... | sort | uniq -c`) aloud correctly.
- Est. hours: counted as A.27 (12 h, Appendix A)

#### 0.2 — A.28 Programming from zero: Python
- **Why:** Python is the lingua franca of data engineering and the language of every exercise in this plan — loaders, tests, glue code, and later Spark and Airflow all speak it. An architect who can't read Python can't review the pipelines they design, and in a fund platform that means signing off on transfer-agency logic sight unseen.
- **Learn:**
    - core language — values/types, control flow, functions, modules; small composable functions over script-blobs *(py4e ch. 1–5)*
    - collections — lists, dicts, sets, and which fits a funds-by-ISIN lookup *(py4e ch. 8–10)*
    - files & exceptions — read a CSV line by line and fail loudly on a malformed row *(py4e ch. 7)*
    - environments — `uv init`, `uv add`, `uv run` from day one; lockfiles, and why bare `pip` is banned here; the Astral toolchain (`uv`, `ruff`, `ty`) wired into the editor early *(uv docs: Projects)*
    - type checking — `ty` (Astral's fast Rust-based type checker) catches a wrong type before runtime; type hints on function signatures make `fundcli` self-documenting and reviewable *(ty docs)*
    - tracebacks & debugging — read bottom-up, reproduce minimally, then fix *(Automate: Debugging chapter)*
    - calling an HTTP API — fetch JSON, handle status codes and timeouts *(py4e ch. 12–13)*
    - small CLI scripts — argparse flags, `--help`, exit codes, so scripts behave like real tools *(Python docs: Argparse Tutorial)*
- **Resources:**
    - **[Python for Everybody](https://www.py4e.com/)** (Severance — free full course) — values through files, exceptions and web data; the core path (primary)
    - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (free online) — alternate full course; its Debugging chapter covers tracebacks hands-on (alternate)
    - [uv documentation](https://docs.astral.sh/uv/) — projects, dependencies, `uv run`; the only way Python runs in this plan (reference)
    - [ty documentation](https://docs.astral.sh/ty/) — Astral's fast type checker; the third of the `uv`/`ruff`/`ty` toolchain (reference)
    - [Python docs: Argparse Tutorial](https://docs.python.org/3/howto/argparse.html) — flags, defaults and help text for `fundcli` (reference)
- **Tools:**
    - FOSS (hands-on): [Python](https://docs.python.org/3/) via [uv](https://docs.astral.sh/uv/), [ruff](https://docs.astral.sh/ruff/), [ty](https://docs.astral.sh/ty/), [VS Code](https://code.visualstudio.com/docs) — the daily Astral toolchain for four years
- **Do:**
    1. `uv init fundcli` and commit the empty scaffold; add `ruff` and `ty` (`uv add --dev ruff ty`) and run both on every save from now on.
    2. Build `fundcli`: read a CSV of funds (ISIN, name, currency, domicile), filter by `--currency`/`--domicile` flags via argparse, write a summary JSON (counts per currency and per domicile).
    3. Split it into functions — parse, filter, summarize, write — each with type hints so `uv run ty check` passes clean, and each callable (and, in 0.11, testable) on its own.
    4. Make failure honest: a malformed row raises with its row number; a missing input file exits non-zero with a one-line message, not a raw traceback.
    5. Write `--help` text good enough that someone else can run it without reading the code.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 36 h)*
    - [ ] Write a 100-line script (read a CSV, filter rows via a function you define, write JSON, handle a malformed line) without copying structure from examples.
    - [ ] Verify `uv run fundcli.py --help` behaves like a real tool — flags documented, errors clean, exit codes correct.
    - [ ] Diagnose a planted TypeError from its traceback alone, narrating the read order.
    - [ ] `uv run ty check` passes clean, with type hints on every function signature.
- Est. hours: counted as A.28 (36 h, Appendix A)

#### 0.3 — A.29 SQL from zero
- **Why:** SQL is the single most-used skill of the entire four years; everything from Phase 1 modeling to Phase 8 semantic layers speaks it, and every design review in a fund shop eventually lands on a query. An architect who hesitates at a LEFT JOIN row-count surprise loses the room — and ships NAV reports that silently double rows.
- **Learn:**
    - SELECT/WHERE/ORDER BY — filtering and sorting as the atomic moves *(SQLBolt)*
    - joins — inner vs left, and *why* row counts multiply when the join key isn't unique *(SQLBolt)*
    - GROUP BY/HAVING — aggregation, and which column references are legal after grouping *(PgExercises: Aggregates)*
    - subqueries & CTEs — naming intermediate results instead of nesting blindly *(PostgreSQL Tutorial: CTEs)*
    - NULL semantics — three-valued logic, `NULL = NULL`, and the classic WHERE-clause traps *(PostgreSQL Tutorial)*
    - window functions — ROW_NUMBER, LAG, running sums; "latest NAV per fund" is the canonical use *(PostgreSQL Tutorial: Window Functions)*
    - INSERT/UPDATE/DELETE — modifying data, and what a missing WHERE costs *(PgExercises: Modifying data)*
    - indexes & information_schema at user level — what an index speeds up and how to ask the database about itself *(PostgreSQL docs)*
- **Resources:**
    - **[SQLBolt](https://sqlbolt.com/)** — free interactive lessons: SELECT through joins and aggregation, zero setup (primary)
    - [PgExercises](https://pgexercises.com/) — drills to fluency on a realistic schema: joins, aggregates, modifying data (practice)
    - [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) — alternate track with explicit CTE, NULL and window-function sections (alternate)
    - [PostgreSQL documentation](https://www.postgresql.org/docs/) — indexes, information_schema and exact semantics when the tutorials run out (reference)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL](https://www.postgresql.org/docs/) in Docker (from 0.5), [DBeaver](https://dbeaver.io/) or [psql](https://www.postgresql.org/docs/current/app-psql.html) (↔ [Azure SQL](https://learn.microsoft.com/azure/azure-sql/) — same language)
- **Do:**
    1. Load your 0.2 funds CSV plus a NAV-history table into Postgres (via the 0.5 Compose stack) so you have a two-table funds/nav schema sharing a fund key.
    2. Answer 15 questions of rising difficulty in a committed `.sql` file: filters → joins → GROUP BY → CTEs → "latest NAV per fund via window function".
    3. Break one join on purpose (duplicate a fund row) and document the row-count multiplication before fixing it.
    4. For two of the slower queries, run `EXPLAIN` before and after adding an index and note what changed.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 26 h)*
    - [ ] Demonstrate joins and GROUP BY (with HAVING) as reflexes — no syntax lookups for the core 15 questions.
    - [ ] Explain a LEFT JOIN row-count surprise to someone else, using your duplicated-fund example.
    - [ ] Predict which of three given queries an index would help, and verify with EXPLAIN.
- Est. hours: counted as A.29 (26 h, Appendix A)

#### 0.4 — 9.2.1 Git & GitHub (version control from zero) — T2
- **Why:** Every artifact of the next four years lives in Git; branching and PRs are also how teams (and the capstones) work. In a regulated shop, Git history doubles as the audit trail for "who changed the NAV calculation and when" — an architect who can't reconstruct that stands before compliance empty-handed.
- **Learn:**
    - init/add/commit and the three states — working tree, index, history, and what each command moves *(Pro Git ch. 1–2)*
    - log & diff — interrogating history before trusting it *(Pro Git ch. 2)*
    - branching & merging — cheap branches, fast-forward vs merge commits, resolving a conflict by hand *(Pro Git ch. 3)*
    - remotes — push/pull/fetch, origin conventions, and .gitignore before secrets and data files leak *(Pro Git ch. 2)*
    - GitHub flow — repos, README, opening and merging a pull request *(GitHub: Hello World)*
    - undo recipes — restore vs revert vs reset, and which is safe on shared history *(Oh Shit, Git!?!)*
- **Resources:**
    - **[Pro Git](https://git-scm.com/book/en/v2)** ch. 1–3 (free book) — the three states, history, branching and merging done properly (primary)
    - [GitHub: Hello World quickstart](https://docs.github.com/en/get-started/start-your-journey/hello-world) — the pull-request workflow end to end in 30 minutes (hands-on)
    - [Oh Shit, Git!?!](https://ohshitgit.com/) — the undo recipes you'll actually reach for, indexed by panic (reference)
- **Tools:**
    - FOSS (hands-on): [Git](https://git-scm.com/doc) with [GitHub](https://docs.github.com/) as primary host (↔ GitLab — same model)
    - Corp (evaluate): [Azure Repos](https://learn.microsoft.com/azure/devops/repos/) — same Git underneath; branch policies and PR gates are what fund-industry shops actually configure
- **Do:**
    1. Put `fundcli` (0.2) on GitHub with a README and a .gitignore that excludes `.venv` and data files.
    2. Develop a feature (e.g., a `--format csv|json` flag) on a branch with small commits and real messages; open a PR to yourself and merge it.
    3. Force a merge conflict — edit the same function on two branches — and resolve it by reading the conflict markers, not by clicking "accept theirs".
    4. Practice undo: `git restore` a bad edit, `git revert` a merged commit, `git reset` an unpushed one; write one line each on when it's safe.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 8 h)*
    - [ ] Survive a deliberately broken rebase/merge without fear — you know which undo applies and when `revert` is safer than `reset`.
    - [ ] Explain the three states and trace a file through them with `git status` at each step.
    - [ ] Show a PR with a clean description, small commits and a resolved conflict in its history.
- Est. hours: 8

#### 0.5 — A.30 Docker & containers from zero
- **Why:** The entire lab (Phases 1–8) is Docker-Compose-shaped; containers are also the unit of deployment everywhere you'll architect, from Kafka clusters to Azure container services. Without container fluency you can't reproduce a vendor's "works on our machine" fund-data feed problem — and reproducibility is the architect's first lever in any incident.
- **Learn:**
    - images vs containers — immutable template vs running instance; layers and the build cache *(Docker: Get Started)*
    - running containers — ports, env vars, bind mounts vs named volumes, and what dies on `rm` *(Docker: Get Started)*
    - writing a Dockerfile — FROM/COPY/RUN/CMD for `fundcli`; small images, build context *(Dockerfile reference)*
    - Compose — two services (app + Postgres), depends_on with healthchecks, named volumes for persistence *(Compose docs)*
    - debugging — `docker logs`, `docker exec -it`, and diagnosing a container that exits immediately *(Docker: Get Started)*
    - cleanup hygiene — pruning images and volumes before they eat your disk *(Docker: Get Started)*
- **Resources:**
    - **[Docker: Get Started guide](https://docs.docker.com/get-started/)** — concepts, running, building and first Compose in one official path (primary)
    - [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) — exact instruction semantics when the guide's examples run out (reference)
    - [Docker Compose documentation](https://docs.docker.com/compose/) — service definitions, healthchecks, volumes; the lab's daily file format (reference)
- **Tools:**
    - FOSS (hands-on): [Docker Engine](https://docs.docker.com/engine/install/ubuntu/) installed natively on Ubuntu — every later phase's lab runs on this (↔ Docker Desktop on Windows/macOS)
- **Do:**
    1. Write a Dockerfile for `fundcli` and run it as a one-shot container against a mounted CSV.
    2. Write `compose.yaml`: a Postgres service with a named volume and healthcheck, plus a one-shot loader container that waits for healthy Postgres and ingests your funds CSV.
    3. Prove persistence: `docker compose down && docker compose up` shows the data survived; then `down -v` — explain why it didn't.
    4. Break the loader (wrong env var for the DB password) and diagnose it from `docker logs` alone.
    5. Run a cleanup pass (`docker system df`, then prune) and record what was reclaimed.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 8 h)*
    - [ ] Explain image vs container vs volume to a colleague in plain words, and write a Dockerfile + two-service `docker-compose.yml` (volume + healthcheck) from scratch.
    - [ ] Debug a failing container from its logs without rebuilding blindly.
    - [ ] Start the whole stack with one `docker compose up` from a clean clone.
- Est. hours: counted as A.30 (8 h, Appendix A)

#### 0.6 — A.31 Networking & how the web works
- **Why:** Every integration in this plan (APIs, Kafka, cloud, Private Link in Phase 5) sits on this layer; architects who can't follow a DNS lookup debug by superstition. When the EMT-file transfer to a Luxembourg transfer agent fails at month-end, "which layer?" is the first question — and it's yours.
- **Learn:**
    - IP & ports, TCP vs UDP — addresses, sockets, and why "connection refused" differs from "timeout" *(Cloudflare Learning Center)*
    - DNS resolution end to end — resolver, root, TLD, authoritative; what caching and TTLs change *(Cloudflare Learning Center)*
    - HTTP — methods, status codes, headers; what a REST call actually is on the wire *(MDN: How the web works)*
    - TLS & certificates — what they guarantee (identity, confidentiality) and what they don't, not the math *(Cloudflare Learning Center)*
    - localhost vs LAN vs internet — why a container port "works on my machine" and nowhere else *(MDN: How the web works)*
    - firewalls & proxies — who can silently eat your packets, and how corporate networks differ from home *(Cloudflare Learning Center)*
    - reading `curl -v` — resolution, handshake, request, response, line by line *(everything curl)*
- **Resources:**
    - **[MDN: How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)** — the URL-to-page story with HTTP in context (primary)
    - [Cloudflare Learning Center](https://www.cloudflare.com/learning/) — short free articles on DNS, TLS, firewalls and proxies (reference)
    - [everything curl](https://everything.curl.dev/) — the free curl book; reading verbose output is covered properly (deepening)
- **Tools:**
    - FOSS (hands-on): [curl](https://curl.se/docs/), [dig](https://bind9.readthedocs.io/)/nslookup, [Chrome DevTools](https://developer.chrome.com/docs/devtools/) network tab — the whole diagnostic kit
- **Do:**
    1. Pick one real HTTPS URL (e.g., the ECB Data Portal) and `dig` the name: identify the answer record, its TTL, and who answered.
    2. `curl -v` the URL and annotate every line of the output in a committed text file: resolution, TCP connect, TLS handshake, request headers, response status and headers.
    3. Probe your local 0.5 Postgres port and a firewalled port; classify each failure ("refused" vs "timeout") by layer.
    4. Write a one-page triage table: "slow / blocked / cert error / name not found" → first layer to check → first command to run.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 8 h)*
    - [ ] Map "it's slow / it's blocked / cert error" each to a layer you'd check first, and narrate URL→page (DNS, TCP, TLS, HTTP).
    - [ ] Annotate a fresh `curl -v` of an unseen URL correctly on the first pass.
    - [ ] Explain why DNS can succeed while the connection still times out, with one plausible cause per layer.
- Est. hours: counted as A.31 (8 h, Appendix A)

#### 0.7 — 1.1.1 + 1.1.2 + 1.1.3 What data physically is — T3
- **Why:** Structured/semi-structured/unstructured and their file shapes are the vocabulary of every later storage decision — and of every conversation with fund-data vendors shipping CSV NAV feeds, EMT files and XML messages. An architect who has never debugged an encoding mangle will approve interfaces that corrupt ISINs silently and discover it in reconciliation.
- **Learn:**
    - bytes, text & UTF-8 — code points vs encodings, BOMs, why "Ã©" appears and how to fix it *(Joel on Software: Unicode)*
    - CSV and its dialect traps — separators, quoting, embedded newlines; why CSV has no schema *(Python docs: csv)*
    - JSON & nesting — objects and arrays, plus the types it lacks (dates, decimals — fatal for NAV precision) *(Python docs: json)*
    - XML at reading level — elements, attributes, namespaces; Phase 2's ISO 20022 is XML *(MDN: XML introduction)*
    - what "schema" means — and structured (NAV table) vs semi-structured (EMT file) vs unstructured (prospectus PDF) *(FoDE ch. 1)*
    - spreadsheets vs databases — why Excel is an interchange surface, not a system of record *(FoDE ch. 1)*
- **Resources:**
    - **[Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)** (FoDE, Reis & Housley) ch. 1 — structured/semi-structured/unstructured and what "schema" buys (primary)
    - [Joel on Software: The Absolute Minimum About Unicode](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) — the classic encodings explainer (reference)
    - [Python docs: csv module](https://docs.python.org/3/library/csv.html) — dialects, quoting, sniffing; pair with the [json module](https://docs.python.org/3/library/json.html) for nesting and its missing types (reference)
    - [MDN: XML introduction](https://developer.mozilla.org/en-US/docs/Web/XML/Guides/XML_introduction) — XML at exactly reading level (reference)
- **Tools:**
    - FOSS (hands-on): [Python](https://docs.python.org/3/) (csv/json modules), [pandas](https://pandas.pydata.org/docs/) — the conversion-and-breakage lab
- **Do:**
    1. Take one fund-holdings dataset and produce it three ways: CSV, JSON nested by fund, and pretty-printed XML — same content, three shapes.
    2. Break the CSV twice: inject a stray separator inside a fund name, then re-save a copy in Latin-1 so accented names mangle.
    3. Detect both programmatically — a column-count check per row, and a decode-with-fallback that flags suspect lines — then fix and reload.
    4. Write ten lines: which shape you'd mandate for a vendor NAV feed and why, citing the failure modes you just caused.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 6 h)*
    - [ ] Name the failure modes of CSV from your own scars (and explain UTF-8 mojibake), not a list.
    - [ ] Classify NAV table / EMT file / prospectus PDF as structured / semi-structured / unstructured with one-line justifications.
    - [ ] Demonstrate detecting and repairing an encoding mangle programmatically.
- Est. hours: 6

#### 0.8 — 1.2.1 + 1.3.1 + 1.3.2 Batch processing & OLTP vs OLAP — T2/T3
- **Why:** The transactional-vs-analytical split drives storage choice everywhere; batch is the default processing rhythm of the fund industry (daily NAV). Architects who blur the two end up running month-end analytics on the order-capture database — and explaining to operations why subscriptions slowed at cutoff.
- **Learn:**
    - OLTP workload shape — many small indexed reads/writes, latency-bound; the transfer-agency order book *(FoDE ch. 2–3)*
    - OLAP workload shape — few huge scans and aggregations, throughput-bound; the month-end NAV analysis *(DDIA ch. 3)*
    - why one system rarely serves both well — row vs column layout, and what each makes cheap *(DDIA ch. 3)*
    - batch jobs — schedule → process bounded data → publish; the daily-NAV rhythm *(FoDE ch. 2–3)*
    - idempotent reruns at intuition level — why "run it twice" must be safe; deepened in Phase 1 *(FoDE ch. 2–3)*
    - row store vs column store, first contact — Postgres vs DuckDB on the same query *(DuckDB: Why DuckDB)*
- **Resources:**
    - **[Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)** (FoDE) ch. 2–3 — workloads, batch vs streaming, storage choices (primary)
    - [Designing Data-Intensive Applications](https://dataintensive.net/) (DDIA) ch. 3 — OLTP vs OLAP and column storage, the canonical treatment (deepening)
    - [DuckDB: Why DuckDB](https://duckdb.org/why_duckdb) — what a columnar-vectorized engine optimizes for, in two pages (reference)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL](https://www.postgresql.org/docs/) (row store) + [DuckDB](https://duckdb.org/docs/) (column store) — first contact
    - Corp (evaluate): [Azure SQL](https://learn.microsoft.com/azure/azure-sql/) for OLTP vs [Microsoft Fabric](https://learn.microsoft.com/fabric/) warehousing for OLAP — the same split, priced per side
- **Do:**
    1. Generate ~1M NAV rows (your 0.2 loader, scaled with synthetic funds and dates) and load them into Postgres and into a Parquet file.
    2. Run the same "average NAV per fund per month" query on Postgres and on DuckDB-over-Parquet; record timings, cold and warm.
    3. Run a single-row lookup by fund key on both; record timings again and note the reversal.
    4. Write five sentences on why they differ, arguing from row-vs-column layout — no hand-waving about "DuckDB is fast".
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 4 h)*
    - [ ] Sort ten example workloads into OLTP/OLAP/batch without hesitation, and say why a row store loses to a column store on scans.
    - [ ] Explain your timing results from storage layout, including the case each engine wins.
    - [ ] State where the daily-NAV batch sits on the split and what that implies for where it runs.
- Est. hours: 4

#### 0.9 — 5.4.2 + 14.5.2 pandas & JupyterLab — T2
- **Why:** Notebook-driven wrangling is the data professional's daily bread and your exploration tool for every later phase — profiling a new vendor feed starts in pandas long before it gets a pipeline. An architect who can't poke at the data personally designs from hearsay, and one who doesn't know notebook hidden-state dangers ships "it worked in the notebook" bugs.
- **Learn:**
    - JupyterLab basics — and its dangers: hidden state, out-of-order cells; restart-and-run-all as the only truth *(JupyterLab docs)*
    - loading data — read_csv/read_parquet, dtypes, parse_dates; what pandas guesses wrong *(McKinney ch. 6)*
    - selecting & filtering — loc/iloc, boolean masks, chained-assignment traps *(McKinney ch. 5)*
    - groupby-agg — split-apply-combine for per-fund monthly summaries *(McKinney ch. 10)*
    - joins/merge — pandas joins, with the same row-multiplication trap as SQL *(McKinney ch. 8)*
    - datetime & missing data — parsing dates, resampling to month-end, NaN semantics, dropna vs fillna and when each is honest *(McKinney ch. 7 & 11)*
    - a first chart — matplotlib via pandas, one question per figure *(McKinney ch. 9)*
    - getting data out — to_parquet, and to_sql into Postgres *(pandas user guide: IO)*
- **Resources:**
    - **[Python for Data Analysis, 3rd ed.](https://wesmckinney.com/book/)** (McKinney — free online at the author's site) ch. 1–11 selectively — pandas from its author, with the cleaning chapters that matter (primary)
    - [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html) — IO (Parquet, SQL), merging and groupby reference beyond the book (reference)
    - [JupyterLab documentation](https://jupyterlab.readthedocs.io/) — interface, kernels, and what restart-and-run-all actually resets (reference)
- **Tools:**
    - FOSS (hands-on): [JupyterLab](https://jupyterlab.readthedocs.io/), [pandas](https://pandas.pydata.org/docs/), [matplotlib](https://matplotlib.org/stable/) (↔ Hex/Databricks notebooks later)
- **Do:**
    1. Build a deliberately messy NAV file from your 0.7 data: mixed encodings, duplicate rows, missing dates, one numeric column read as text.
    2. In a notebook, clean it step by step: fix dtypes, drop true duplicates (justify the key), handle missing dates explicitly; document each decision in a markdown cell.
    3. Produce a monthly per-fund summary via groupby/resample and one chart answering a stated question (e.g., "which fund's NAV is most volatile?").
    4. Write the result to both Parquet and Postgres (to_sql against the 0.5 stack); read each back and assert equality.
    5. Restart kernel, Run All — fix whatever breaks, and note which hidden-state assumption bit you.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 10 h)*
    - [ ] Load a messy CSV in JupyterLab, clean it, groupby-aggregate, chart it, and write Parquet — cold.
    - [ ] Explain *why* notebook state burned you at least once, and the restart-and-run-all habit that prevents it.
    - [ ] Reproduce the entire cleaned output from a fresh kernel in one run.
- Est. hours: 10

#### 0.10 — 9.1.1 + 9.1.2 Editor & IDE setup — T3
- **Why:** Tooling friction taxes every hour of the next four years; set it up once, properly. Print-debugging through a reconciliation script costs hours where a breakpoint costs minutes — and the habit gap compounds across every later phase.
- **Learn:**
    - workspace & integrated terminal — VS Code running natively on Ubuntu, so editor and lab share one filesystem *(VS Code docs: Linux)*
    - extensions — Python, ruff, ty, Jupyter, Docker; what each actually adds *(VS Code docs: Python tutorial)*
    - debugging with breakpoints — set, step, inspect variables, watch expressions; stop print-debugging early *(VS Code docs: Python debugging)*
    - keyboard-first habits — command palette, go-to-definition, multi-cursor; a dozen bindings beat a hundred *(VS Code docs: Python tutorial)*
    - JupyterLab vs VS Code notebooks — same kernels, different ergonomics; pick per task *(VS Code docs: Jupyter Notebooks)*
- **Resources:**
    - **[VS Code docs: Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)** — environment, extensions and the run/debug loop end to end (primary)
    - [VS Code on Linux](https://code.visualstudio.com/docs/setup/linux) — installing and running the editor natively on Ubuntu (reference)
    - [VS Code docs: Python debugging](https://code.visualstudio.com/docs/python/debugging) — breakpoints, stepping, launch configurations (reference)
    - [VS Code docs: Jupyter Notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) — notebooks inside the editor, variable explorer included (reference)
- **Tools:**
    - FOSS (hands-on): [VS Code](https://code.visualstudio.com/docs) (↔ JetBrains; choice is taste, fluency is mandatory)
- **Do:**
    1. Install VS Code on Ubuntu with the Python, ruff, ty, Jupyter and Docker extensions; open your `fundcli` repo from your home directory.
    2. Plant a bug in a `fundcli` function (e.g., a filter that drops the wrong currency) on a branch.
    3. Debug it with a breakpoint inside the function: inspect variables, step through the filter, fix it — without a single print.
    4. Drill the bindings for run, breakpoint toggle, command palette and go-to-definition until the mouse is optional.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 2 h)*
    - [ ] Run the edit-run-debug loop frictionlessly, entirely inside the editor + terminal (lint + terminal + notebooks in one window).
    - [ ] Fix a planted bug via breakpoints and variable inspection, no prints.
    - [ ] Open any repo, terminal and debugger without touching the mouse.
- Est. hours: 2

#### 0.11 — 9.4.1 Unit testing from zero (pytest) — T2
- **Why:** Tests are how the capstones (and grown-up data platforms) stay trustworthy; the habit must form before the stakes rise. In a fund platform, an untested parser is a silent NAV-corruption machine — and an architect who never built the habit can't credibly demand it from delivery teams.
- **Learn:**
    - test files & functions — discovery rules, plain `assert`, one behavior per test *(pytest: Get started)*
    - parametrize — one test, many cases; the malformed-row matrix in four lines *(pytest how-to guides)*
    - arranging code to be testable — pure functions, separating parsing from IO so tests need no files *(Real Python: pytest tutorial)*
    - fixtures at basic level — shared setup (a sample funds list, a tmp CSV) without copy-paste *(pytest how-to guides)*
    - the local habit — `uv run pytest` on every change; running in CI comes in Phase 3 *(pytest: Get started)*
- **Resources:**
    - **[pytest documentation: Get started](https://docs.pytest.org/en/stable/getting-started.html)** — install, first tests, assertions, discovery (primary)
    - [pytest how-to guides](https://docs.pytest.org/en/stable/how-to/index.html) — parametrize and fixtures, straight from the source (reference)
    - [Real Python: pytest tutorial](https://realpython.com/pytest-python-testing/) — fixtures, marks and structuring code for testability (deepening)
- **Tools:**
    - FOSS (hands-on): [pytest](https://docs.pytest.org/) via [uv](https://docs.astral.sh/uv/) — `uv add --dev pytest`, then `uv run pytest`
- **Do:**
    1. Refactor `fundcli` so parsing and filtering are pure functions that take rows and return rows — no file IO inside.
    2. Add tests: happy path, empty file, malformed row, wrong currency — the malformed-row cases via `@pytest.mark.parametrize`.
    3. Use a fixture for the sample funds data; keep tests file-free where possible, with one tmp_path test for the file boundary.
    4. Watch one test fail, then fix the code, not the test; commit the failing test and the fix separately to show the habit.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 4 h)*
    - [ ] Write the test first naturally for any new function, including a parametrized edge case.
    - [ ] Show green `uv run pytest` covering happy path, empty file, malformed row and wrong currency.
    - [ ] Explain why the parser is testable without touching the filesystem.
- Est. hours: 4

#### 0.12 — 9.5.1 Code review basics — T3
- **Why:** Review is how engineering teams transfer judgment; doing it well (both directions) is a career-long multiplier. For a future architect it's also the main influence channel — most of your designs get enforced one PR comment at a time, and in regulated fund work the review record is part of the control evidence.
- **Learn:**
    - what reviewers look for — correctness, clarity, scope; design comments before nitpicks *(Google eng-practices: reviewer guide)*
    - writing reviewable PRs — small, well-described, self-reviewed first; one concern per PR *(Google eng-practices: CL author's guide)*
    - giving feedback — on the code, not the person; severity labels make intent unambiguous *(Conventional Comments)*
    - responding to review — without ego; when to push back, and when a comment reveals a documentation gap *(Google eng-practices: CL author's guide)*
- **Resources:**
    - **[Google Engineering Practices: Code Review Developer Guide](https://google.github.io/eng-practices/review/)** — both halves: the reviewer guide and how to get reviewed (primary)
    - [Google eng-practices: The CL author's guide](https://google.github.io/eng-practices/review/developer/) — writing small, reviewable changes and handling comments (reference)
    - [Conventional Comments](https://conventionalcomments.org/) — a labeling format that keeps feedback kind and actionable (reference)
- **Do:**
    1. Take your Capstone 0 PR and self-review it with the guide's checklist: correctness, clarity, naming, tests, docs.
    2. Leave five genuine line comments on your own PR — at least one design-level, not all nitpicks — using Conventional Comments labels.
    3. Fix all five in follow-up commits, replying to each comment as you would to a human reviewer.
    4. Write a three-line personal review checklist you'll apply to every future PR before requesting review.
- **Done when:** *(this checklist is also the module's Skip test — tick every box cold today and skip the module, banking 2 h)*
    - [ ] Submit PRs pre-reviewed by you, with the checklist running in your head; line comments critique code, not people.
    - [ ] Show five genuine self-review comments and their fixes in a real PR.
    - [ ] Distinguish a design-level comment from a nitpick in your own review record.
- Est. hours: 2

### Capstone 0 — Personal data toolbox

- **Goal:** prove the foundations compose: one small, real, reproducible data project touching every module.
- **Stack (100% free):** [Ubuntu](https://ubuntu.com/) (your laptop), [uv](https://docs.astral.sh/uv/)-managed Python, [PostgreSQL](https://www.postgresql.org/docs/) + loader in [Docker Compose](https://docs.docker.com/compose/), [JupyterLab](https://jupyterlab.readthedocs.io/) + [pandas](https://pandas.pydata.org/docs/), [pytest](https://docs.pytest.org/), [Git](https://git-scm.com/doc) + [GitHub](https://docs.github.com/).
- **Build:** (1) pick a public fund/ETF dataset (e.g., an [ECB Data Portal](https://data.ecb.europa.eu/) or [data.europa.eu](https://data.europa.eu/) CSV); (2) `docker compose up` brings Postgres + a Python loader that ingests it idempotently-naively (rerun-safe by truncate-reload — the grown-up version comes in Phase 1); (3) answer 10 SQL questions of rising difficulty in a committed `.sql` file (joins, GROUP BY, at least one window function); (4) a notebook produces one cleaned monthly summary and one chart answering a stated question; (5) pytest covers the loader's parsing — happy path plus malformed input; (6) README explains setup in ≤10 commands; (7) developed on branches with self-reviewed PRs (the 0.12 checklist applied).
- **Architecture deliverables:** none yet — your first C4 diagram and ADR arrive in Phase 1; here the README *is* the architecture document.
- **Acceptance criteria:** a stranger with Docker and uv reproduces everything from the README on a fresh machine; `uv run pytest` green; the chart answers a stated question; the Git history shows ≥3 PRs with self-review comments; rerunning the loader leaves row counts unchanged (truncate-reload verified).
- Est. hours: 10

*Phase 0 total: 46 h in-phase (taxonomy entries 36 h + capstone 10 h) + 90 h via A.27–A.31 = 136 h — every hour of it skippable: each module's *Done when* checklist is its Skip test (mechanism in the [Skip List](#skip-list)).*


<a id="phase-1"></a>
## Phase 1: Distributed Data Systems & Modeling Core (months 7–11, 118 h)

*Phase 1 of 8 · months 7–11 · 118 h · capstone: Fund reference OLTP + reporting mart.*  ← [Phase 0](#phase-0) · [Phase 2](#phase-2) →

**Goal:** rebuild the theoretical foundation an architect reasons from — transaction guarantees, consistency, distribution tradeoffs, database internals — and turn existing modeling intuition into formal, teachable practice (conceptual→logical→physical, dimensional), documented with C4 and ADRs from day one.
**Entry prerequisites:** Phase 0 — or its skip tests passed (Linux/shell, Python, SQL, Git, Docker, networking).
**Exit criteria:** you can (1) explain isolation anomalies and pick an isolation level for a fund-order workload; (2) argue a replication/partitioning choice with PACELC, not folklore; (3) read a Postgres `EXPLAIN ANALYZE` and fix the plan; (4) produce a 3-level model + star schema for a fund domain and defend every key and SCD choice; (5) ship C4 diagrams + ADRs as a matter of habit.

### T1/T2 topics

#### 1.6.1 ACID & isolation levels — T1
- **Why:** Transaction guarantees underpin every regulated-data design review — "is this exactly-once and serializable?" is a question the architect must answer, not delegate. Getting isolation wrong in a fund platform means double-booked orders and unexplainable NAV corrections that auditors will find before you do.
- **Learn:**
    - atomicity and durability mechanics — how the WAL makes a commit survive a crash *(DDIA ch. 7)*
    - isolation anomalies — dirty/non-repeatable/phantom reads and write skew, with a concrete failure story for each *(DDIA ch. 7)*
    - ANSI levels vs snapshot isolation — why READ COMMITTED is the common default and what it silently permits *(Postgres docs: Transaction Isolation)*
    - serializability vs SSI — what `SERIALIZABLE` buys and costs in Postgres *(CMU 15-445 concurrency-control lectures)*
    - vendor defaults — how Postgres, SQL Server (RCSI), and Oracle differ, and why that matters in migrations *(Postgres docs: Transaction Isolation)*
    - idempotent retry vs transactional retry — what the application must do when a serialization failure (SQLSTATE 40001) surfaces *(DDIA ch. 7)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 7 "Transactions" (latest ed.)** — the canonical treatment: anomalies, weak isolation levels, serializability, retry semantics (primary)
    - [PostgreSQL docs: Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — the exact semantics you will demonstrate hands-on, including how Postgres's levels map to ANSI (reference)
    - [CMU 15-445: concurrency-control lectures](https://15445.courses.cs.cmu.edu/) — 2PL, timestamp ordering, MVCC internals behind the levels (deepening)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL](https://www.postgresql.org/docs/) in Docker — two psql sessions are the whole lab (↔ Azure SQL)
    - Corp (evaluate): [Azure SQL](https://learn.microsoft.com/azure/azure-sql/) / [Oracle Database](https://docs.oracle.com/en/database/) — default isolation (RCSI in Azure SQL, statement-level read consistency in Oracle) and TDE-era differences at evaluation level
- **Do:**
    1. Start the Phase-1 Postgres container and open two psql sessions side by side.
    2. At `READ COMMITTED`, reproduce a non-repeatable read, a phantom, and write skew on a two-row "fund cash balance" table; save the exact statement interleavings as scripts.
    3. Re-run the same interleavings at `REPEATABLE READ` and `SERIALIZABLE`; record which anomaly each level prevents and which error (40001) the client receives instead.
    4. Write a half-page note on retry behavior: which isolation level a fund-order workload needs, and how the application must respond to a serialization failure.
- **Done when:**
    - [ ] Reproduce write skew and a phantom on demand and explain why snapshot isolation permits write skew.
    - [ ] Explain to a reviewer a fund-accounting scenario where write skew corrupts data, and name the isolation level that prevents it.
    - [ ] State the default isolation level of Postgres, SQL Server, and Oracle, and one migration consequence of the differences.
- Est. hours: 8

#### 1.6.3 + 1.6.4 + 1.6.5 The consistency spectrum — T2
- **Why:** Replicated platforms — read replicas, geo-DR, caches — silently downgrade consistency, and the architect must name the guarantee actually delivered rather than assume "strong". In a fund platform, an investor seeing a confirmed order vanish on refresh is a read-your-writes violation, not a UI bug, and the fix is architectural.
- **Learn:**
    - eventual vs strong consistency — what "eventually" actually promises and what it never does *(DDIA ch. 5)*
    - read-your-writes and monotonic reads — the session guarantees replica reads break first *(DDIA ch. 5)*
    - causal consistency — preserving "question before answer" ordering across replicas *(DDIA ch. 9)*
    - linearizability vs serializability — single-object recency vs multi-object transaction ordering; they answer different questions *(DDIA ch. 9)*
    - where lag bites in practice — replica reads after writes, cross-region failover and the lost-write window *(DDIA ch. 5)*
    - a worked commercial spectrum — Cosmos DB's five levels as the vocabulary Azure design reviews will use *(Cosmos DB docs: consistency levels)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 5 "Replication" + ch. 9 "Consistency and Consensus" (linearizability sections)** — replication-lag anomalies and the formal guarantees behind them (primary)
    - [Jepsen: Consistency Models](https://jepsen.io/consistency) — the definitive map of guarantee names and how they relate (reference)
    - [Azure Cosmos DB: consistency levels](https://learn.microsoft.com/azure/cosmos-db/consistency-levels) — strong → bounded staleness → session → consistent prefix → eventual, productized (Azure framing)
- **Do:**
    1. List the read paths of a fund platform (order-status API, NAV-history dashboard, transfer-agency register lookup) and the replication topology each would realistically sit on.
    2. For each path, name the minimum guarantee it needs (read-your-writes? monotonic? linearizable?) and the user-visible bug if it is violated.
    3. Write the 1-page memo: which consistency level a fund-order status API needs vs a NAV-history dashboard, and what each choice costs in latency and availability.
- **Done when:**
    - [ ] Give a concrete user-visible bug for each violated guarantee (read-your-writes, monotonic reads, causal).
    - [ ] Defend in one sentence why NAV history tolerates staleness but order status does not.
    - [ ] Map each Cosmos DB consistency level to the textbook guarantee it implements.
- Est. hours: 5

#### 1.7.1 + 1.7.2 CAP & PACELC — T1
- **Why:** Every design review invokes CAP, usually wrongly; the architect corrects the record and uses PACELC's latency half, which is what actually drives cloud database selection. Choosing a fund-data store on "CP vs AP" folklore buys either needless latency or unexplained stale reads in regulated reporting.
- **Learn:**
    - what CAP actually states — the narrow definitions of C (linearizability) and A (every non-failed node answers), and why most systems are neither CP nor AP *(DDIA ch. 9: "The Unhelpfulness of CAP")*
    - partition behavior of common systems — what Postgres, Cassandra, and quorum systems each do when the network splits *(DDIA ch. 9)*
    - PACELC — the Else case: latency vs consistency under normal operation, the tradeoff you pay every day *(Abadi PACELC paper)*
    - classifying real systems — PA/EL vs PC/EC labels for Postgres, Cassandra, Cosmos DB, Spanner-style stores *(Abadi PACELC paper)*
    - how the inventor reframed it — Brewer's own corrections twelve years on *(Brewer: CAP Twelve Years Later)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 9** — including "The Unhelpfulness of CAP" (primary)
    - [Abadi, "Consistency Tradeoffs in Modern Distributed Database System Design"](https://www.cs.umd.edu/~abadi/papers/abadi-pacelc.pdf) — the PACELC paper, IEEE Computer 2012 (source)
    - [Brewer, "CAP Twelve Years Later: How the Rules Have Changed"](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/) — the theorem's author on what people get wrong (reference)
- **Do:**
    1. Re-read the CAP definitions and write one paragraph on why a single-region Azure SQL deployment sits outside CAP's frame entirely.
    2. Build the one-table PACELC classification of the 8 stores you'll meet in this plan (Postgres, Cassandra, Kafka, Cosmos DB, DynamoDB, Spanner, Redis, MongoDB) with a one-line justification per row.
    3. Sanity-check the Cosmos DB row against Microsoft's own consistency documentation and note the nuance (per-level tradeoffs) a single label hides.
- **Done when:**
    - [ ] Explain why "CP vs AP" is the wrong frame for a single-region Azure SQL deployment.
    - [ ] Defend each of the 8 PACELC classifications in one sentence without notes.
    - [ ] State the latency cost of choosing consistency in the Else case, with one concrete example.
- Est. hours: 3

#### 1.8.1 Idempotency — T1
- **Why:** Retry-safety is the single biggest reliability lever in pipelines; non-idempotent loads are how funds double-book trades. An architect who cannot point to where idempotency holds in a design has not finished the design — every regulated rerun, replay, and disaster-recovery story depends on it.
- **Learn:**
    - idempotency keys — client-supplied identifiers that make "did this already apply?" answerable *(DDIA ch. 11)*
    - natural vs synthetic dedup — when a business key (order ref, ISIN+date) suffices and when you must mint one *(DDIA ch. 11)*
    - idempotent writes — MERGE/upsert and `INSERT … ON CONFLICT` as the sink-side mechanism *(Postgres docs: INSERT)*
    - idempotent pipeline runs — the overwrite-partition pattern: a rerun rewrites a deterministic slice, never appends *(DDIA ch. 10–11)*
    - effective exactly-once — at-least-once delivery + idempotent consumer; why true exactly-once delivery is a myth *(DDIA ch. 11)*
    - rerun semantics in managed orchestrators — what actually re-executes on failure recovery *(ADF docs)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 10–11** — fault-tolerance and exactly-once sections; rerunnable batch output; taxonomy concept entry as checklist (primary)
    - [PostgreSQL docs: INSERT … ON CONFLICT](https://www.postgresql.org/docs/current/sql-insert.html) — upsert syntax and conflict-handling semantics for the loader (reference)
    - [Azure Data Factory documentation](https://learn.microsoft.com/azure/data-factory/) — pipeline rerun and retry behavior at evaluation level (Azure framing)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL](https://www.postgresql.org/docs/) upserts — the sink for the provably rerunnable loader (↔ ADF + Azure SQL)
    - Corp (evaluate): [Azure Data Factory](https://learn.microsoft.com/azure/data-factory/) — rerun semantics: what state a re-executed activity sees
- **Do:**
    1. Generate a trades CSV (a few thousand rows with order refs and ISINs) and decide the natural dedup key.
    2. Write a Python loader (via `uv run`) that ingests it into Postgres using `INSERT … ON CONFLICT` (or a staged MERGE) so a second run changes nothing.
    3. Prove it: run twice; compare row counts and a whole-table checksum (e.g. `md5(string_agg(…))`) after each run, and commit the evidence to the repo.
    4. Break it deliberately — kill the loader mid-run — then rerun and show the end state is still identical.
- **Done when:**
    - [ ] List the three places idempotency must hold in a pipeline (source read, transform, sink write) and how to get each.
    - [ ] Show identical row counts and checksums after a double run and after a kill-and-rerun.
    - [ ] Explain why "exactly-once" in practice means at-least-once delivery plus an idempotent consumer.
- Est. hours: 4

#### 1.8.9 Distributed transactions & 2PC — T2
- **Why:** You must recognize when someone proposes a distributed transaction and steer to outbox/saga instead — with reasons, not taste. In a fund platform, a blocked 2PC coordinator between an order service and a position service is an outage that holds locks across the books at the worst possible moment.
- **Learn:**
    - the 2PC protocol — prepare and commit phases, and what each participant promises at "prepared" *(DDIA ch. 9)*
    - the blocking failure mode — in-doubt transactions holding locks while the coordinator is down *(DDIA ch. 9)*
    - XA in practice — why heterogeneous distributed transactions rot in real systems *(DDIA ch. 9)*
    - consensus ≠ 2PC — what Raft solves that 2PC does not (no single blocking point) *(Raft site)*
    - modern alternatives preview — transactional outbox and saga, implemented in Phase 4 *(microservices.io: Outbox / Saga)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 9 "Distributed Transactions and Consensus"** — 2PC, in-doubt transactions, XA, consensus (primary)
    - [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) and [Saga](https://microservices.io/patterns/data/saga.html) — the alternatives your ADR will name (reference)
    - [The Raft consensus algorithm](https://raft.github.io/) — visualization and paper; why consensus is a different problem (deepening)
- **Do:**
    1. Sketch the 2PC message flow for an order-service + position-service write; mark the exact point where coordinator death leaves participants in doubt.
    2. Write down what happens to the participants' locks at that point and who is able to release them.
    3. Write a half-page ADR rejecting 2PC for this hypothetical consistency requirement, naming outbox or saga as the alternative and stating what you give up (atomic visibility) and gain (availability).
- **Done when:**
    - [ ] Explain what happens to locks when a 2PC coordinator dies mid-commit.
    - [ ] Name the alternative pattern in your ADR and the tradeoff it accepts.
    - [ ] Distinguish in two sentences what Raft guarantees that 2PC cannot.
- Est. hours: 5

#### 1.5.1–1.5.4 Storage paradigms — T2
- **Why:** Row vs columnar, shared-nothing vs shared-disk, and storage/compute separation are the axes along which every warehouse/lakehouse vendor differentiates — this is the vocabulary of vendor selection. An architect who cannot derive cost and failure behavior from these decisions ends up reading vendor slides instead of auditing them.
- **Learn:**
    - row vs columnar layouts — why analytical scans love columns and OLTP point-writes love rows *(DDIA ch. 3)*
    - compression and late materialization — why columnar compresses so well and defers row reconstruction *(DDIA ch. 3)*
    - MPP partitioning and data skew — how one hot key turns a 16-node cluster into a 1-node job *(CMU 15-445 storage lectures)*
    - shared-nothing vs shared-disk — which failures stay isolated and which are global *(Snowflake docs: Key Concepts)*
    - separation of storage and compute — the Snowflake/BigQuery model and its cost/elasticity consequences *(Snowflake docs: Key Concepts)*
- **Resources:**
    - **[Designing Data-Intensive Applications](https://dataintensive.net/) ch. 3 "Storage and Retrieval" (column-store sections)** — layout, compression, materialization (primary)
    - [CMU 15-445: storage lectures 3–5](https://15445.courses.cs.cmu.edu/) — page layout, buffer management, the physical substrate (deepening)
    - [Snowflake docs: Key Concepts & Architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts) — the canonical storage/compute-separation design, an explicit hybrid of shared-disk and shared-nothing (reference)
- **Tools:**
    - FOSS (hands-on): [DuckDB](https://duckdb.org/docs/) — columnar engine for the CSV-vs-Parquet experiment (↔ Synapse/Snowflake)
    - Corp (evaluate): [Azure Synapse Analytics](https://learn.microsoft.com/azure/synapse-analytics/) — MPP distribution choices (hash / round-robin / replicated) at evaluation level
- **Do:**
    1. Generate a 10M-row trades table (Faker or DuckDB's range functions) and store it as both CSV and Parquet.
    2. Run the same aggregate (e.g. sum of amount grouped by ISIN) over both files in DuckDB; record timings and bytes scanned.
    3. Explain the timing difference in terms of layout, compression, and I/O — not "Parquet is faster" but why.
    4. Sketch the Snowflake-style three-layer architecture and annotate which cost and failure behaviors follow from each separation decision.
- **Done when:**
    - [ ] Sketch the Snowflake-style architecture and say which failure/cost behaviors follow from each separation decision.
    - [ ] Explain the CSV-vs-Parquet timing gap in terms of columnar layout and I/O, with your measured numbers.
    - [ ] Describe one workload where shared-nothing MPP beats storage/compute separation, and one where it loses.
- Est. hours: 4

#### 3.2.1 Relational internals (the database under everything) — T1
- **Why:** Indexing, query planning, MVCC, and recovery ground every storage decision an architect makes; this is the deepest single investment in the plan. Without it you negotiate with DBAs and vendors on faith — with it you can read any engine's documentation and predict its behavior under fund-platform load.
- **Learn:**
    - pages, heap files, and the buffer pool — why the database manages its own cache instead of trusting the OS *(CMU 15-445 storage lectures)*
    - B+trees vs hash vs GIN/BRIN — which Postgres index answers which predicate shape *(Database Internals Part I)*
    - join algorithms and cardinality estimation — how a misestimate produces a nested-loop disaster *(CMU 15-445 joins/optimization lectures)*
    - MVCC, vacuum, and bloat — why updates copy rows and what unchecked bloat does to NAV-history tables *(Postgres docs: MVCC)*
    - WAL, checkpoints, crash recovery — ARIES-style logging and what fsync actually buys *(CMU 15-445 logging/recovery lectures)*
    - reading `EXPLAIN (ANALYZE, BUFFERS)` — where time and I/O go in a real plan *(Postgres docs: Using EXPLAIN)*
    - connection pooling — why a fund platform fronts Postgres with a pooler, and pooling modes *(PgBouncer docs)*
    - table partitioning — when partition pruning helps and when it just adds planning cost *(Postgres docs: Table Partitioning)*
    - the extension ecosystem — Postgres is a platform: `pgvector` (vectors), PostGIS (geo), TimescaleDB (time-series), Apache AGE (graph), `pgmq` (queues), `pg_cron` (scheduling), `pg_duckdb`/Citus (analytics), DBOS (durable execution) *(Postgres docs: contrib)*
- **Resources:**
    - **[CMU 15-445/645 (latest year)](https://15445.courses.cs.cmu.edu/)** — lectures + notes for storage, buffer pool, indexes, sorting/joins, query optimization, MVCC, logging/recovery (~14 of 26 lectures) (primary)
    - [*Database Internals* (Petrov), Part I](https://www.databass.dev/) — storage-engine and B-tree internals in book form (alternate/deepening)
    - [PostgreSQL docs: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — plus the [MVCC](https://www.postgresql.org/docs/current/mvcc.html) and [Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html) chapters — the exact engine you tune (reference)
    - [PgBouncer docs](https://www.pgbouncer.org/) — session vs transaction pooling and their gotchas (reference)
    - [PostgreSQL docs: Additional Supplied Modules & Extensions](https://www.postgresql.org/docs/current/contrib.html) — the extension surface that turns Postgres into a platform (reference)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL 16](https://www.postgresql.org/docs/) with `EXPLAIN (ANALYZE, BUFFERS)` and [pgbench](https://www.postgresql.org/docs/current/pgbench.html) — the lab engine (↔ Azure SQL)
    - Corp (evaluate): [Azure SQL](https://learn.microsoft.com/azure/azure-sql/) / [Oracle Database](https://docs.oracle.com/en/database/) — planner-hint culture and licensing economics at evaluation level
- 🐘 **Architect's lens — "Postgres until you can't":** one well-run Postgres plus extensions can stand in for a queue (`pgmq`), a cache, a vector DB (`pgvector`), a time-series DB (TimescaleDB), a graph DB (Apache AGE), a scheduler (`pg_cron`), durable execution (DBOS), and a small analytics warehouse (`pg_duckdb`/Citus) — collapsing operational surface and keeping every workload transactional with your data. *Better when* volumes are low-to-moderate and you value one system to run, secure and back up; *worse when* a single workload's scale, latency, or fan-out outgrows one node — then graduate just that workload to a specialist (Kafka, ClickHouse, Neo4j, a warehouse) and keep the rest on Postgres. Knowing the crossover point per extension is the architect's skill.
- **Do:**
    1. Build (or reuse the capstone seed of) a 5-table fund-holdings schema in Postgres and load enough Faker data that scans hurt — millions of rows in holdings and NAV history.
    2. Write a deliberately slow 5-table fund-holdings query; capture its plan with `EXPLAIN (ANALYZE, BUFFERS)`.
    3. Fix it step by step — indexes, statistics targets, rewrites — to a 10× improvement, re-capturing the plan after every change.
    4. Run pgbench before and after to show the throughput effect, and write up the before/after plans narrating where time went.
    5. Demonstrate MVCC bloat on the side: update a large table in a loop, watch the table size grow, VACUUM, and explain what happened.
- **Done when:**
    - [ ] Read an unfamiliar `EXPLAIN ANALYZE` and narrate where time goes and why the planner chose the join order it did.
    - [ ] Show a documented 10× improvement with before/after plans and the reasoning behind each fix.
    - [ ] Explain MVCC bloat and vacuum using your own measured table sizes.
    - [ ] Pick the right index type (B+tree / hash / GIN / BRIN) for four different predicate shapes and justify each.
- Est. hours: 30

#### 8.2.1 + 8.2.2 + 8.2.3 Conceptual → logical → physical modeling — T1
- **Why:** The three-level discipline is the architect's signature artifact chain — business entities to keys/normal forms to engine-specific DDL — and the basis for every review you'll run. Skip a level and you get ISIN-as-primary-key databases that cannot survive a corporate action, or "logical" models silently welded to one engine.
- **Learn:**
    - conceptual entity modeling — naming the business things (fund, share class, investor) and knowing when to stop *(DMBOK ch. 5)*
    - logical keys — candidate vs natural vs surrogate, and why ISIN is an attribute, not a primary key *(DMBOK ch. 5)*
    - normalization 1NF–BCNF — what each form forbids, plus deliberate, documented denormalization *(Hoberman)*
    - physical design — data types, partitioning, and indexes chosen per target engine *(Postgres docs: Table Partitioning)*
    - forward/reverse engineering — round-tripping between model and DDL without drift *(DMBOK ch. 5)*
    - notation fluency — write Crow's Foot, read IDEF1X *(Hoberman)*
- **Resources:**
    - **[DAMA-DMBOK](https://www.dama.org/cpages/body-of-knowledge) ch. 5 "Data Modeling and Design"** — the three-level discipline in the governance framing EU institutions recognize (primary)
    - [Hoberman, *Data Modeling Made Simple* (Technics Publications)](https://technicspublications.com/) — keys, normal forms, and notations in plain language (alternate)
    - [PostgreSQL docs: Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html) — the physical-level mechanics for the NAV-history design (reference)
- **Tools:**
    - FOSS (hands-on): [draw.io](https://www.drawio.com/) / [DBeaver](https://dbeaver.io/) ERD — conceptual/logical diagrams and reverse engineering (↔ erwin)
    - Corp (evaluate): [erwin Data Modeler](https://www.quest.com/erwin/) / [ER/Studio](https://www.idera.com/) / [SqlDBM](https://sqldbm.com/) — what EU banks actually license: model repositories, round-trip engineering, governance hooks
- **Do:**
    1. Model the fund domain conceptually — fund, share class, investor, order, NAV — entities and relationships only, one page.
    2. Derive the logical model: candidate keys per entity, surrogate-key decisions justified in writing, normal form stated and defended per table.
    3. Produce the physical model as Postgres DDL — types, constraints, declarative partitioning for NAV history; reverse-engineer it in DBeaver and diff against your logical model.
    4. Self-review the chain after a week against one test: could a colleague implement from the logical model alone?
- **Done when:**
    - [ ] Hand a colleague the logical model and they can implement it without asking you questions.
    - [ ] State a reason for every surrogate-key choice — including why ISIN is not your PK.
    - [ ] Name the normal form of each table and where you denormalized deliberately, and why.
- Est. hours: 12

#### 8.2.4 Dimensional modeling — T1
- **Why:** Kimball stars remain the dominant analytical model in regulated reporting marts; fund NAV/holdings/fees reporting is textbook dimensional territory. An architect who cannot state a fact table's grain in one sentence cannot review a mart — and ungrained fact tables are where double-counted AUM reports come from.
- **Learn:**
    - fact table grain — declare it first, always; every other decision follows from it *(DWT ch. 1–2)*
    - fact types — transaction, periodic snapshot, accumulating snapshot; NAV is a periodic snapshot *(Kimball techniques: fact tables)*
    - conformed dimensions and the bus matrix — how marts stay joinable across business processes *(DWT ch. 4)*
    - SCD types 1/2/3/6 — security/fund reference data is SCD2 country *(Kimball techniques: SCDs)*
    - junk and degenerate dimensions — where order numbers and flag clusters belong *(Kimball techniques)*
    - star vs snowflake — and why snowflaking is usually a modeling smell in marts *(DWT ch. 1)*
    - financial-services patterns — accounts, heterogeneous products, fee facts *(DWT ch. 19)*
- **Resources:**
    - **[Kimball & Ross, *The Data Warehouse Toolkit* 3rd ed.](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) ch. 1–4 + ch. 19 (financial services)** — grain, fact types, SCDs, bus matrix, finance patterns (primary)
    - [Kimball Group: Dimensional Modeling Techniques](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/) — the full technique catalog, free, for lookup during design (reference)
    - [Corr & Stagnitto, *Agile Data Warehouse Design*](https://books.google.com/books/about/Agile_Data_Warehouse_Design.html?id=TRWFmnv8jP0C) — BEAM workshops for modeling with business stakeholders (alternate)
- **Tools:**
    - FOSS (hands-on): [dbt Core](https://docs.getdbt.com/) + [DuckDB](https://duckdb.org/docs/) — implement the star and SCD2 logic as versioned models (↔ Synapse/Snowflake marts)
    - Corp (evaluate): [Azure Synapse](https://learn.microsoft.com/azure/synapse-analytics/) / [Snowflake](https://docs.snowflake.com/) — the same patterns on licensed mart engines
- **Do:**
    1. Design the bus matrix for a fund administrator — processes: orders, NAV calculation, fee accrual, transfer agency — against conformed dimensions (fund, share class, investor, date).
    2. Declare the grain of each fact table in one written sentence before touching any column list.
    3. Implement the NAV periodic-snapshot star in SQL (dbt + DuckDB) with an SCD2 fund dimension (valid_from / valid_to + current flag).
    4. Write the point-in-time query joining the snapshot fact to the SCD2 dimension as of an arbitrary historical date; test it across at least one attribute change.
- **Done when:**
    - [ ] State the grain of each fact table in one sentence.
    - [ ] Show an SCD2 query returning point-in-time-correct fund attributes for any historical date.
    - [ ] Justify each dimension in the bus matrix as conformed, junk, or degenerate.
- Est. hours: 16

#### 8.5.1 Architecture notations & decision records (C4, ADR) — T1
- **Why:** C4 diagrams and ADRs are the artifacts that define the architect role in practice — they make your reasoning reviewable and your decisions auditable, which is exactly what a regulated fund administrator's IT governance expects. Without them, your designs live in slide decks and hallway memory, and the audit trail for "why is NAV history partitioned this way?" is you.
- **Learn:**
    - C4 levels — context, container, component, code; why most architecture work stops at container *(c4model.com)*
    - diagrams-as-code — text-defined models that diff and review in Git like everything else *(c4model.com)*
    - ADR anatomy — context, decision, consequences; short enough that people actually write them *(adr.github.io)*
    - ADR lifecycle — proposed / accepted / superseded; never rewrite history, supersede it *(adr.github.io: MADR)*
    - lightweight RFC processes — when a decision needs review before an ADR records it *(FoSA: decision chapters)*
    - what reviewers look for — boundaries, data flows, and the decisions you didn't write down *(FoSA: decision chapters)*
- **Resources:**
    - **[c4model.com](https://c4model.com/) (full read)** — levels, notation, diagrams-as-code guidance (primary)
    - [adr.github.io](https://adr.github.io/) — ADR formats including the [MADR template](https://adr.github.io/madr/) and lifecycle conventions (reference)
    - [Richards & Ford, *Fundamentals of Software Architecture*](https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/) — the chapters on diagramming and architecture decisions (alternate/deepening)
- **Tools:**
    - FOSS (hands-on): [Structurizr Lite](https://docs.structurizr.com/lite) (Docker) or [Mermaid C4](https://mermaid.js.org/syntax/c4.html) — diagrams-as-code in the repo (↔ Sparx EA)
    - Corp (evaluate): [Sparx Enterprise Architect](https://sparxsystems.com/) / [Visual Paradigm](https://www.visual-paradigm.com/) — the EA suites EU institutions license: model repositories, traceability, governance
- **Do:**
    1. Pick an existing system you know from work and draw its C4 context diagram: actors, system boundary, external dependencies.
    2. Add the container diagram: deployable units, datastores, and the protocol on every arrow.
    3. Express both as code (Structurizr DSL or Mermaid C4) committed to Git — not a drawing export.
    4. Write 2 retroactive ADRs (MADR format) for that system's key decisions, including one that was later superseded, to model the lifecycle.
    5. Set up the `adr/` directory convention you will reuse in every capstone from here on.
- **Done when:**
    - [ ] Ship C4 + ADRs with every capstone from here on without thinking about it (the capstones enforce this).
    - [ ] Explain when to stop at container level and what would force a component diagram.
    - [ ] Show an ADR pair where one supersedes the other with the status trail intact.
- Est. hours: 8

#### 1.10.1 Modeling notations overview — T2
- **Why:** You need reading fluency across UML/BPMN/DMN/ArchiMate before Phase 4 (BPM) and Phase 8 (ArchiMate practice) go deep. In fund-industry workshops the BA brings BPMN, the vendor brings ArchiMate, and the DBA brings ERDs — the architect is the one who reads all of them without a translator.
- **Learn:**
    - UML class/sequence — system structure and interaction behavior, reading level only *(OMG spec: UML)*
    - BPMN — executable business-process notation (order lifecycle, transfer-agency flows) *(OMG spec: BPMN)*
    - DMN — decision tables and logic, separated from process flow *(OMG spec: DMN)*
    - ArchiMate — business/application/technology layers in one enterprise language *(Open Group: ArchiMate overview)*
    - ERD / IDEF1X — data-modeling notations and where each is still mandated *(DMBOK ch. 5)*
    - C4 — software architecture; which question each notation answers and which it cannot *(c4model.com)*
- **Resources:**
    - **[OMG spec: UML](https://www.omg.org/spec/UML/), [BPMN](https://www.omg.org/spec/BPMN/), [DMN](https://www.omg.org/spec/DMN/)** — read the intro/overview sections of each spec, plus one example diagram each; not the full documents (primary)
    - [The Open Group: ArchiMate overview](https://www.opengroup.org/archimate-forum/archimate-overview) — the enterprise-layer language Phase 8 practices (reference)
    - [c4model.com](https://c4model.com/) — the software-architecture notation already in your toolkit, for contrast (reference)
    - [DAMA-DMBOK](https://www.dama.org/cpages/body-of-knowledge) ch. 5 — ERD/IDEF1X grounding on the data side (reference)
- **Do:**
    1. Collect one example diagram of each notation (from the spec intros and c4model.com) into a reference folder.
    2. Make the one-page "notation chooser" cheat sheet: question → notation → tool, with a fund-industry example question per row (e.g. "how does an order get from EMT file to register?" → BPMN).
    3. Test yourself: take three unfamiliar diagrams, identify each notation, and narrate what the diagram says.
- **Done when:**
    - [ ] Name the notation and read it correctly when shown a diagram cold.
    - [ ] Produce the one-page cheat sheet mapping question → notation → tool.
    - [ ] Give a fund-industry example question for each notation.
- Est. hours: 2

#### 9.1.3 Local data sandboxes — T2
- **Why:** The entire 4-year lab runs on reproducible local stacks; compose fluency is the substrate for every capstone. A stack a stranger cannot bring up identically is a lab you cannot trust — the same discipline that later makes your Azure environments reviewable.
- **Learn:**
    - Compose service graphs — `depends_on`, startup ordering, and what Compose does not guarantee *(Compose docs)*
    - healthchecks — gating dependents on actual readiness (`service_healthy`), not container start *(Compose docs)*
    - volumes and networks — named volumes for state, isolated networks per stack *(Compose docs)*
    - image pinning — exact tags (or digests) so the stack reproduces across machines and months *(Compose docs)*
    - the Testcontainers idea — programmatic throwaway infrastructure for tests *(testcontainers.com)*
    - DuckDB as a zero-infra warehouse — when a file beats a service *(DuckDB docs)*
- **Resources:**
    - **[Docker Compose docs](https://docs.docker.com/compose/)** — top-level concepts, healthchecks, volumes, networks; builds directly on Phase 0's module 0.5 (primary)
    - [Testcontainers](https://testcontainers.com/) — the programmatic throwaway-infra pattern, for awareness (reference)
    - [DuckDB docs](https://duckdb.org/docs/) — the zero-infra analytical engine in the same stack (reference)
- **Tools:**
    - FOSS (hands-on): [Docker Compose](https://docs.docker.com/compose/), [PostgreSQL](https://www.postgresql.org/docs/), [MinIO](https://github.com/minio/minio), [DuckDB](https://duckdb.org/docs/), [Testcontainers](https://testcontainers.com/) — the lab substrate (↔ Azure dev environments)
    - Corp (awareness): [GitHub Codespaces](https://docs.github.com/codespaces) / dev containers — the managed equivalent of the same reproducibility idea
- **Do:**
    1. Write the `docker-compose.yml` you'll grow all four years: Postgres + MinIO + a placeholder service.
    2. Add healthchecks to every service and make dependents wait on `service_healthy`, not just `service_started`.
    3. Put all state on named volumes and pin every image to a specific version tag.
    4. Test from a fresh clone on a clean Docker (prune first): time `docker compose up` until everything reports healthy.
- **Done when:**
    - [ ] Run `docker compose up` on a fresh clone and get a clean, healthy stack in under 2 minutes.
    - [ ] Show every image pinned and every stateful service on a named volume.
    - [ ] Explain the difference between `service_started` and `service_healthy` and why a loader needs the latter.
- Est. hours: 4

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.3.3 | HTAP (workload) | One system serving OLTP + OLAP; niche but recurring vendor pitch | [DDIA ch. 3 (closing section)](https://dataintensive.net/) | 30 |
| 1.6.2 | BASE | Marketing-era label for eventual-consistency systems; know it to translate it in vendor decks | [DDIA ch. 5 intro](https://dataintensive.net/) | 15 |
| 3.2.2 | NoSQL document stores | JSON-document storage (MongoDB); flexible schema, integrity owned by the app | [DDIA ch. 2 (document model)](https://dataintensive.net/) | 45 |
| 3.2.3 | NoSQL key-value | High-throughput KV (Redis/Valkey, DynamoDB); caching + session state | [DDIA ch. 3 (hash indexes)](https://dataintensive.net/) | 30 |
| 3.2.4 | NoSQL wide-column | Sparse-column distributed stores (Cassandra); write-heavy, query-first design | [DDIA ch. 2](https://dataintensive.net/) + [Cassandra docs "data modeling" intro](https://cassandra.apache.org/doc/latest/cassandra/developing/data-modeling/intro.html) | 45 |
| 3.2.10 | HTAP stores | TiDB/SingleStore implementations of 1.3.3 | [TiDB docs](https://docs.pingcap.com/tidb/stable/) + [SingleStore docs](https://docs.singlestore.com/) | 15 |

*T3 subtotal: 3 h*

### Capstone 1 — Fund reference OLTP + reporting mart

- **Goal:** a correct, documented foundation: operational fund reference database + dimensional reporting mart, the seed every later phase builds on.
- **Stack (100% free):** [PostgreSQL 16](https://www.postgresql.org/docs/) (↔ [Azure SQL](https://learn.microsoft.com/azure/azure-sql/) / [Oracle DB](https://docs.oracle.com/en/database/)), [DuckDB](https://duckdb.org/docs/) (↔ [Synapse](https://learn.microsoft.com/azure/synapse-analytics/)/[Snowflake](https://docs.snowflake.com/) mart), [dbt Core](https://docs.getdbt.com/) seed/models for the mart (↔ [dbt Cloud](https://www.getdbt.com/)), [Structurizr Lite](https://docs.structurizr.com/lite) (↔ [Sparx EA](https://sparxsystems.com/)), [Docker Compose](https://docs.docker.com/compose/), Python via [uv](https://docs.astral.sh/uv/), [Faker](https://faker.readthedocs.io/) for sample data (↔ [Tonic.ai](https://www.tonic.ai/)/[Delphix](https://www.delphix.com/)).
- **Build:** (1) implement the Phase-1 physical model in Postgres: funds, share classes, ISIN-keyed securities, investors, orders, NAV history (declaratively partitioned by date, per 8.2.1); (2) load Faker-generated but referentially consistent data with the idempotent loader from 1.8.1, using order refs as the natural dedup key; (3) build the NAV periodic-snapshot star + SCD2 fund dimension in DuckDB as dbt models (per 8.2.4); (4) one deliberately slow query, tuned with the 3.2.1 method, with before/after `EXPLAIN (ANALYZE, BUFFERS)` plans committed to the repo.
- **Architecture deliverables:** C4 context + container diagrams; ADR-001 (surrogate vs natural keys — why ISIN is not your PK), ADR-002 (SCD2 for fund attributes), ADR-003 (partitioning scheme for NAV history).
- **Acceptance criteria:** loader runs twice with identical end state (row counts + checksums committed as evidence); point-in-time query returns correct fund attributes for any historical date, demonstrated across at least one SCD2 attribute change; tuned query ≥10× faster with written plan analysis; a stranger can run `docker compose up && uv run load.py` from the README and get the same numbers — verified on a clean clone before calling it done.
- Est. hours: 14

*Phase 1 total: 118 h (T1/T2 entries 101 h + T3 3 h + capstone 14 h)*


<a id="phase-2"></a>
## Phase 2: Lakehouse & Analytics Engineering (months 12–16, 123 h)

*Phase 2 of 8 · months 12–16 · 123 h · capstone: Fund-document lakehouse.*  ← [Phase 1](#phase-1) · [Phase 3](#phase-3) →

**Goal:** master the open lakehouse stack — object storage, columnar formats, ACID table formats, federated SQL, dbt — and ground the whole plan in the fund-data domain by learning the financial standards the platform will carry (ISO 20022, EMT/EPT, instrument identifiers).
**Entry prerequisites:** Phase 1 (modeling discipline, Postgres internals vocabulary, Docker Compose stack).
**Exit criteria:** you can (1) explain a Parquet footer and an Iceberg snapshot to a skeptic; (2) defend Iceberg vs Delta for a given estate; (3) run a tested, documented dbt project with layered models; (4) design a raw vault for an audit-driven warehouse; (5) read an ISO 20022 message and an EMT file and say where each field lands in your model.

### T1/T2 topics

#### 1.4.3 Medallion architecture — T1
- **Why:** Bronze/silver/gold is the default layering of every lakehouse you will design, and as architect your job is to make the layer contracts explicit standards instead of tribal folklore. In a regulated fund platform, an undocumented layer boundary is where lineage breaks and an auditor's "where did this NAV figure come from?" goes unanswered. Get the contracts wrong and silver becomes a dumping ground that nobody trusts and everybody queries anyway.
- **Learn:**
    - what each layer guarantees — bronze immutable/replayable, silver conformed/deduped/DQ-checked, gold consumption-modeled *(Databricks: Medallion architecture)*
    - the schema-on-read → schema-on-write transition point — where you stop tolerating drift and start enforcing it *(FoDE ch. 8)*
    - reprocessing strategy per layer — what you can rebuild from source vs what is the source of truth *(Databricks: Medallion architecture)*
    - when medallion is cargo cult — three layers is a sensible default, not a law; some estates need two or four *(FoDE ch. 8)*
    - layer ownership and consumer promises — who can break what, and the SLA each layer offers downstream *(Databricks: Medallion architecture)*
- **Resources:**
    - **[Databricks: Medallion architecture](https://www.databricks.com/glossary/medallion-architecture)** — the canonical bronze/silver/gold definition with per-layer responsibilities (primary)
    - [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ch. 8 — transformation patterns and where layering fits the wider lifecycle (reference)
- **Do:**
    1. Write a one-page layer-contract sheet for a fund-data lakehouse with one row per layer: owner, schema policy, DQ gate, retention, consumer promise.
    2. For each layer, state exactly what is rebuildable from the layer below and what is a system of record.
    3. Add a concrete fund example per layer (bronze: raw NAV feed file; silver: conformed NAV per share class; gold: EMT-shaped output).
    4. Mark which layer a late-arriving NAV correction enters and how it propagates upward.
- **Done when:**
    - [ ] You can answer "why not query bronze directly?" with consequences, not dogma.
    - [ ] You can name, for your sheet, which layer owns each DQ rule and why.
    - [ ] You can defend a two-layer or four-layer variant for a specific estate.
- Est. hours: 4

#### 3.1.4 Data lakehouse — T1
- **Why:** The lake-with-ACID-tables-plus-warehouse-SQL pattern is the target architecture for most fund platforms, and you will have to design one and defend it against both "just buy Snowflake" and "just use files on a share." Pick wrong and you either pay warehouse prices for cold regulatory archives or lose the concurrency and security a fund administrator needs at month-end. The architect must articulate which component carries which guarantee.
- **Learn:**
    - lakehouse = object store + open table format + catalog + query engines — the four decoupled layers *(Lakehouse paper, CIDR 2021)*
    - what the warehouse still does better — high concurrency, fine-grained security, ergonomics *(Lakehouse paper, CIDR 2021)*
    - why open formats de-risk vendor lock-in — storage/format/catalog/engine can each be swapped independently *(Lakehouse paper, CIDR 2021)*
    - the warehouse-veteran objections — what Inmon-school practitioners distrust about lakes *(Building the Data Lakehouse)*
    - vendor positioning — Databricks vs Snowflake-with-Iceberg vs Fabric/OneLake at architecture level *(Lakehouse paper, CIDR 2021)*
- **Resources:**
    - **[Lakehouse: A New Generation of Open Platforms (CIDR 2021)](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf)** — Armbrust et al.; the technical core of the lakehouse argument (primary)
    - [Building the Data Lakehouse](https://www.oreilly.com/library/view/building-the-data/9781098117290/) — Inmon et al.; skim for the warehouse-veteran perspective and where lakes earn distrust (reference)
- **Tools:**
    - FOSS (hands-on): [MinIO](https://min.io/docs/minio/linux/index.html) + [Apache Iceberg](https://iceberg.apache.org/docs/latest/) + [Trino](https://trino.io/docs/current/) + [DuckDB](https://duckdb.org/docs/) — the four open layers assembled (↔ a managed lakehouse)
    - Corp (evaluate): [Databricks](https://docs.databricks.com/), [Microsoft Fabric / OneLake](https://learn.microsoft.com/fabric/onelake/), [Snowflake](https://docs.snowflake.com/) — what each bundles and where the lock-in sits
- **Do:**
    1. Write a 2-page build-vs-buy memo: open lakehouse vs Databricks vs Fabric for a 50-person Luxembourg fund administrator.
    2. Score each on cost, in-house skills required, lock-in, and EU compliance/data-residency posture.
    3. For each lakehouse component (storage, format, catalog, engine), state what breaks if you swap that vendor.
    4. Make an explicit recommendation with the one risk that would change it.
- **Done when:**
    - [ ] You can name, for each lakehouse component, what breaks if you swap vendors.
    - [ ] You can rebut both "just use Snowflake" and "just use files" with specific consequences.
    - [ ] You can state which component is the genuine lock-in point in a given vendor's bundle.
- Est. hours: 10

#### 3.1.3 + 3.3.1 Data lake on object storage — T2
- **Why:** Object stores are the physical substrate of everything analytical, and their semantics — no atomic rename, eventually consistent listing, per-request pricing — leak upward into every table format and query engine you design. An architect who treats S3/ADLS like a POSIX filesystem produces designs that corrupt under concurrent writers or cost a fortune in LIST calls. In funds, that is the difference between a lakehouse that survives month-end and one that silently drops a NAV file.
- **Learn:**
    - S3 API object semantics — flat key space, no folders, no atomic rename *(MinIO docs: Core Concepts)*
    - durability vs availability tiers and lifecycle policies — how cold regulatory archives get cheap *(MinIO docs: Object Lifecycle Management)*
    - prefixes, partitioning and request costs — why layout choices are cost choices *(MinIO docs: Core Concepts)*
    - multipart upload mechanics — how large NAV/holdings files land reliably *(MinIO docs: Core Concepts)*
    - ADLS Gen2 hierarchical namespace — why atomic directory rename exists and what it buys *(ADLS Gen2 introduction)*
- **Resources:**
    - **[MinIO documentation](https://min.io/docs/minio/linux/index.html)** — S3-compatible object store: core concepts, lifecycle, multipart upload (primary)
    - [Azure Data Lake Storage Gen2 introduction](https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-introduction) — hierarchical namespace and atomic directory operations on Azure (reference)
- **Tools:**
    - FOSS (hands-on): [MinIO](https://min.io/docs/minio/linux/index.html) — the local S3 substrate for the whole phase (↔ ADLS Gen2 / S3)
    - Corp (evaluate): [ADLS Gen2](https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-introduction) — primary cloud target; [S3](https://docs.aws.amazon.com/s3/) — awareness of the de-facto standard
- **Do:**
    1. Run MinIO in Docker Compose and create a bucket for the fund lakehouse.
    2. With `uv run` + pyarrow, write NAV Parquet files into a `dt=YYYY-MM-DD/` date-partitioned key layout.
    3. Set a lifecycle rule to expire bronze objects after 30 days; verify it appears in the bucket config.
    4. List objects under a prefix and note how many LIST/GET calls a date-range scan would cost.
- **Done when:**
    - [ ] You can explain why "rename a folder" is a problem on S3 but a single atomic operation on ADLS Gen2.
    - [ ] You can predict the request-cost shape of a partitioned scan from the key layout.
    - [ ] You can show a working lifecycle rule expiring bronze objects.
- Est. hours: 4

#### 3.1.1 Cloud data warehouse — T2
- **Why:** Even lakehouse-first shops keep a warehouse for high-concurrency BI and fine-grained security, so you will be asked to compare Snowflake/BigQuery/Synapse credibly during vendor selection. Get the pricing model wrong and a fund administrator's month-end reporting spike turns into a budget incident. The architect must explain to a CFO why costs are workload-shaped, not data-shaped.
- **Learn:**
    - Snowflake's three-layer architecture — separate services, compute (warehouses/credits), storage *(Snowflake: Key Concepts & Architecture)*
    - micro-partitions and clustering vs explicit partitioning — how Snowflake prunes without you partitioning *(Snowflake: Key Concepts & Architecture)*
    - BigQuery's serverless slots model — compute as a fungible pool, not a sized cluster *(BigQuery: Introduction)*
    - Synapse dedicated vs serverless and where Fabric Warehouse lands *(BigQuery: Introduction; Snowflake docs)*
    - how runaway cost happens in each — idle warehouses, full scans, unpartitioned queries *(Snowflake: Key Concepts & Architecture)*
- **Resources:**
    - **[Snowflake: Key Concepts & Architecture](https://docs.snowflake.com/en/user-guide/intro-key-concepts)** — the three-layer model, credits, micro-partitions (primary)
    - [BigQuery: Introduction / overview](https://cloud.google.com/bigquery/docs/introduction) — serverless compute/storage separation and the slots model (reference)
- **Tools:**
    - FOSS (hands-on): [DuckDB](https://duckdb.org/docs/) — a local stand-in for warehouse-style exercises
    - Corp (evaluate): [Snowflake](https://docs.snowflake.com/), [BigQuery](https://cloud.google.com/bigquery/docs/introduction), [Synapse / Fabric Warehouse](https://learn.microsoft.com/fabric/data-warehouse/) — at vendor-selection level
- **Do:**
    1. Build a one-page comparison table covering Snowflake, BigQuery, and Synapse/Fabric.
    2. For each, fill in: architecture, pricing unit, workload isolation mechanism, Iceberg/open-format story, EU-region and compliance posture.
    3. Note for each the single most common way costs run away.
- **Done when:**
    - [ ] You can explain to a CFO why Snowflake costs are workload-shaped, not data-shaped.
    - [ ] You can name each engine's pricing unit and workload-isolation mechanism.
    - [ ] You can state each engine's Iceberg story in one sentence.
- Est. hours: 4

#### 3.4.1 File formats — T1
- **Why:** Parquet internals — row groups, encodings, statistics, predicate pushdown — are where storage cost and query latency are actually decided, and an architect who cannot read a footer argues from vibes. In a fund lakehouse, the difference between a holdings scan that prunes row groups and one that reads every byte is the difference between a sub-second mart and a multi-minute one. This knowledge is vendor-neutral and pays off on every engine.
- **Learn:**
    - Parquet physical structure — file → row groups → column chunks → pages, plus the footer *(Parquet format docs)*
    - encodings and statistics — dictionary/RLE, min/max stats, and how they enable pushdown *(Parquet format docs)*
    - predicate and projection pushdown — how the reader skips row groups and columns *(DuckDB docs: Reading Parquet)*
    - compression tradeoffs — snappy vs zstd, size vs CPU *(Parquet format docs)*
    - Avro as the row-oriented schema-evolution format — where it fits (Kafka, landing) *(Parquet format docs)*
    - Arrow as the in-memory interchange standard and ORC at awareness level *(DuckDB docs: Reading Parquet)*
- **Resources:**
    - **[Apache Parquet format documentation](https://parquet.apache.org/docs/)** — the authoritative description of row groups, encodings, stats (primary)
    - [DuckDB docs: Reading Parquet](https://duckdb.org/docs/data/parquet/overview) — pushdown and projection from the reader's side, used in the lab (reference)
    - [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ch. 6 — file-format context including Avro/ORC tradeoffs (alternate)
- **Tools:**
    - FOSS (hands-on): [pyarrow](https://arrow.apache.org/docs/python/), [DuckDB](https://duckdb.org/docs/), [parquet-tools](https://github.com/apache/parquet-java/tree/master/parquet-tools-deprecated) — write, inspect, and benchmark Parquet
    - Corp (evaluate): same formats everywhere — this knowledge is vendor-neutral by design
- **Do:**
    1. With pyarrow via `uv run`, write the same 10M-row holdings table at three row-group sizes and two compressions (snappy, zstd).
    2. Record file size for each combination.
    3. In DuckDB, run a filtered scan (e.g. one fund, one date range) over each file and measure time.
    4. Inspect the footers (row-group count, min/max stats) and explain the size and time differences from the structure.
- **Done when:**
    - [ ] Given a slow lake query, you check row-group pruning before blaming the engine.
    - [ ] You can read a Parquet footer and state how many row groups a predicate would skip.
    - [ ] You can justify a row-group size and compression choice for a holdings table.
- Est. hours: 8

#### 3.4.2 Table formats (Iceberg, Delta) — T1
- **Why:** The ACID metadata layer is the heart of the lakehouse — snapshots, schema evolution, time travel, and compaction are exactly what you will design, operate, and debug. In a fund platform, time travel is how you reproduce yesterday's NAV report after a correction lands, and a botched compaction is how a table silently triples in size. The Iceberg-vs-Delta decision is an ADR you will own.
- **Learn:**
    - Iceberg metadata tree — metadata file → manifest list → manifests → data files *(Iceberg docs: spec)*
    - snapshots and time travel — how each commit creates an immutable snapshot you can query *(Iceberg docs: spec)*
    - hidden partitioning and partition evolution — changing partitioning without rewriting queries *(Iceberg docs: Partitioning)*
    - copy-on-write vs merge-on-read — the write-vs-read cost tradeoff for UPDATE/DELETE *(Iceberg docs: Configuration)*
    - compaction and maintenance — expiring snapshots, rewriting manifests, file sizing *(Iceberg docs: Maintenance)*
    - schema evolution rules and the Delta log model / UniForm, with Hudi at awareness level *(Apache Iceberg: The Definitive Guide)*
- **Resources:**
    - **[Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/)** — spec, Maintenance, Partitioning, Configuration: the operational core (primary)
    - [Apache Iceberg: The Definitive Guide](https://hello.dremio.com/wp-apache-iceberg-the-definitive-guide-reg.html) — free via Dremio; format-war context, Delta/Hudi comparison, COW vs MOR (alternate)
- **Tools:**
    - FOSS (hands-on): [Iceberg](https://iceberg.apache.org/docs/latest/) on [MinIO](https://min.io/docs/minio/linux/index.html) via [Trino](https://trino.io/docs/current/connector/iceberg.html); Delta via [DuckDB](https://duckdb.org/docs/) / [delta-rs](https://delta-io.github.io/delta-rs/) — exercise both formats
    - Corp (evaluate): [Databricks Delta](https://docs.databricks.com/delta/), [Snowflake managed Iceberg](https://docs.snowflake.com/en/user-guide/tables-iceberg), [Fabric OneLake](https://learn.microsoft.com/fabric/onelake/) — managed forms
- **Do:**
    1. Create an Iceberg NAV table via Trino on MinIO.
    2. Run UPDATE, DELETE, and MERGE statements simulating a NAV correction and a late-arriving holding.
    3. Time-travel to the snapshot before the correction and confirm the prior NAV report reproduces.
    4. Evolve the schema (add a column) and change the partition spec; query still runs unchanged.
    5. Inspect the metadata JSON, manifest list, and manifests on MinIO and narrate the tree out loud.
- **Done when:**
    - [ ] You can debug "why is this table slow/huge" from the manifests alone.
    - [ ] You can write the Iceberg-vs-Delta ADR for a given estate with concrete reasons.
    - [ ] You can reproduce a pre-correction NAV via time travel on demand.
- Est. hours: 12

#### 3.4.3 Table-format catalogs — T2
- **Why:** The catalog is the new lock-in battleground — whoever owns the catalog owns the lakehouse — so this is a vendor-selection conversation you must lead, not delegate. Pick an engine-bundled catalog and you have quietly recreated the lock-in that open formats were supposed to remove. For a Luxembourg fund administrator, the catalog also decides who can vend credentials to regulated data, which is a governance question, not just a technical one.
- **Learn:**
    - what a catalog tracks — namespaces, table pointers, current snapshot per table *(Iceberg REST catalog spec)*
    - the Iceberg REST catalog spec as the decoupling standard — engines talk one API *(Iceberg REST catalog spec)*
    - credential vending — how the catalog brokers scoped storage access *(Apache Polaris docs)*
    - product positioning — Polaris, Unity Catalog OSS, Lakekeeper, Nessie *(Apache Polaris docs)*
    - why engine-bundled catalogs recreate lock-in even with open table formats *(Iceberg REST catalog spec)*
- **Resources:**
    - **[Iceberg REST catalog specification](https://iceberg.apache.org/docs/latest/)** (REST catalog / spec sections) — the open API that decouples engine from catalog (primary)
    - [Apache Polaris documentation](https://polaris.apache.org/) — a reference REST catalog implementation, credential vending, namespaces (reference)
    - [Lakekeeper documentation](https://docs.lakekeeper.io/) — a lightweight Rust REST catalog, easy to run in compose (alternate)
- **Tools:**
    - FOSS (hands-on): [Lakekeeper](https://docs.lakekeeper.io/) or [Apache Polaris](https://polaris.apache.org/) — a REST catalog in Docker Compose (↔ managed catalog)
    - Corp (evaluate): [Unity Catalog](https://docs.databricks.com/data-governance/unity-catalog/), [AWS Glue](https://docs.aws.amazon.com/glue/), [Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/) — what each bundles
- **Do:**
    1. Swap your capstone's catalog from Trino's Hive-style catalog to a Lakekeeper or Polaris REST catalog.
    2. Re-point Trino at the REST catalog and confirm the existing Iceberg tables resolve unchanged.
    3. Document precisely what changed (the catalog endpoint and config) and what did not (the data files, the format).
    4. Note how credentials are vended to the engine through the catalog.
- **Done when:**
    - [ ] You can explain credential vending and why it is the catalog's job.
    - [ ] You can argue why the catalog, not the format, decides openness.
    - [ ] You can swap the catalog without rewriting a single data file.
- Est. hours: 4

#### 4.3.1 MPP/federated SQL engines (Trino) — T2
- **Why:** Trino is the open federation engine (and the heart of Starburst and AWS Athena), and it queries the lakehouse and Postgres in one statement — the practical face of "decoupled compute." For a fund administrator, that means joining live transfer-agency reference data in Postgres to historical Iceberg NAV facts without an ETL hop. But federation done naively produces chatty cross-store joins, and the architect must know when it is an anti-pattern.
- **Learn:**
    - coordinator/worker architecture — how a query is planned and distributed *(Trino docs: Overview)*
    - connectors and pushdown — what predicates/aggregations get pushed to each source *(Trino docs: Iceberg connector)*
    - the memory model and spill — why big joins fail and how spill helps *(Trino docs: Overview)*
    - Iceberg connector specifics — snapshots, time travel, and maintenance from Trino *(Trino docs: Iceberg connector)*
    - cost-based optimizer basics and when federation is an anti-pattern (chatty cross-store joins) *(Trino: The Definitive Guide)*
- **Resources:**
    - **[Trino documentation](https://trino.io/docs/current/)** (Overview + [Iceberg connector](https://trino.io/docs/current/connector/iceberg.html)) — architecture, connectors, pushdown (primary)
    - [Trino: The Definitive Guide](https://www.starburst.io/info/oreilly-trino-guide/) — free via Starburst; CBO, federation patterns and anti-patterns (alternate)
- **Tools:**
    - FOSS (hands-on): [Trino](https://trino.io/docs/current/) — the federation engine over Iceberg + Postgres (↔ Starburst Enterprise, AWS Athena)
    - Corp (evaluate): [Starburst](https://docs.starburst.io/), [AWS Athena](https://docs.aws.amazon.com/athena/), [Synapse serverless](https://learn.microsoft.com/azure/synapse-analytics/sql/on-demand-workspace-overview) — managed Trino-style options
- **Do:**
    1. Add Trino to your Docker Compose stack with Postgres and Iceberg connectors.
    2. Join Postgres fund reference data to Iceberg NAV history in a single query.
    3. Run the same logical join after copying the dimension into Iceberg first; compare timings.
    4. Use EXPLAIN to verify which predicates push down to Postgres vs Iceberg.
- **Done when:**
    - [ ] You can predict which predicates push down to each source and confirm it with EXPLAIN.
    - [ ] You can state when federating beats copying the dimension, and when it does not.
    - [ ] You can read a Trino query plan and spot a chatty cross-store join.
- Est. hours: 5

#### 4.3.3 Embedded analytical engines (DuckDB) — T2
- **Why:** DuckDB is the architect's pocket warehouse — local development, fast testing, and a legitimate production pattern for mid-size workloads — and knowing its limits sharpens every "do we actually need a cluster?" conversation. For a fund administrator running marts that fit comfortably on one node, "no cluster" can be the right, cheapest, most maintainable architecture. The skill is knowing the data-size and concurrency envelope where that holds.
- **Learn:**
    - the in-process model — DuckDB runs inside your process, not as a server *(DuckDB docs: Why DuckDB)*
    - out-of-core execution — querying data larger than RAM by spilling *(DuckDB docs: Why DuckDB)*
    - reading Parquet/Iceberg/Delta directly from object storage *(DuckDB docs: Reading Parquet)*
    - the extension ecosystem and the single-writer constraint *(DuckDB docs: Why DuckDB)*
    - awareness of MotherDuck (managed) and ClickHouse (server-side single-node speed) *(DuckDB docs: Why DuckDB)*
- **Resources:**
    - **[DuckDB docs: Why DuckDB](https://duckdb.org/why_duckdb)** — the design philosophy, in-process model, and intended workloads (primary)
    - [DuckDB documentation (Parquet / extensions)](https://duckdb.org/docs/) — reading lake formats and the extension ecosystem (reference)
- **Tools:**
    - FOSS (hands-on): [DuckDB](https://duckdb.org/docs/) — the embedded engine for marts and benchmarks
    - Corp (evaluate): [MotherDuck](https://motherduck.com/docs/), [ClickHouse Cloud](https://clickhouse.com/docs) — at awareness level
- 🐘 **Postgres-native alternative — [pg_duckdb](https://github.com/duckdb/pg_duckdb) / [Citus](https://www.citusdata.com/) columnar:** *Better when* you want columnar analytics inside the same Postgres that serves OLTP — DuckDB's engine embedded via `pg_duckdb`, or Citus for distributed/columnar tables — so analysts query live data with no separate warehouse to load. *Worse when* you need true lakehouse scale, open table formats, or storage/compute separation: that's Trino/Spark/warehouse territory.
- **Do:**
    1. Benchmark the Phase-1 mart queries two ways: DuckDB over Parquet vs Postgres.
    2. Record query times and resource use for each.
    3. Repeat with a larger-than-RAM holdings table to observe out-of-core behaviour.
    4. Write 5 bullets stating when DuckDB wins and when Postgres (or a cluster) wins.
- **Done when:**
    - [ ] You can articulate the data-size/concurrency envelope where "no cluster" is the right architecture.
    - [ ] You can show DuckDB querying a larger-than-RAM file successfully.
    - [ ] You can name the single-writer constraint and what it rules out.
- Est. hours: 3

#### 5.2.1 + 5.3.1 dbt & the SQL transformation layer — T1
- **Why:** dbt is the modeling-to-production bridge you already started in Phase 1, and mastery — not mere usage — is what lets you set transformation standards for a whole analytics team. In a fund platform, dbt tests are where data-quality contracts become executable and dbt snapshots are how you keep auditable SCD2 history of share-class attributes. Without disciplined materializations and a readable DAG, the warehouse becomes a pile of views nobody can reason about.
- **Learn:**
    - project structure conventions — staging/intermediate/marts mirroring medallion *(dbt best-practice guides)*
    - the ref graph and materializations — view/table/incremental/snapshot and incremental failure modes *(dbt docs: Materializations)*
    - tests — generic, singular, and unit tests as executable DQ contracts *(dbt docs: Tests)*
    - dbt snapshots = SCD2 — keeping auditable history of dimension attributes *(dbt docs: Snapshots)*
    - docs, exposures, and packages (dbt-utils, dbt-expectations) *(dbt best-practice guides)*
    - SQLMesh as the challenger — virtual environments, column-level lineage, at eval level *(SQLMesh docs)*
- **Resources:**
    - **[dbt best-practice guides](https://docs.getdbt.com/best-practices)** — official structure/style/materialization guidance (primary)
    - [dbt documentation](https://docs.getdbt.com/) — materializations, tests, snapshots, exposures reference (reference)
    - [Analytics Engineering with SQL and dbt (Cyr & Dorsey)](https://www.oreilly.com/library/view/analytics-engineering-with/9781098142377/) — end-to-end project narrative (deepening)
    - [SQLMesh documentation](https://sqlmesh.readthedocs.io/) — the challenger's virtual environments and lineage, for evaluation (alternate)
- **Tools:**
    - FOSS (hands-on): [dbt Core](https://docs.getdbt.com/) + [dbt-duckdb](https://github.com/duckdb/dbt-duckdb) / [dbt-trino](https://github.com/starburstdata/dbt-trino); [SQLMesh](https://sqlmesh.readthedocs.io/) (eval) — the transformation layer (↔ dbt Cloud)
    - Corp (evaluate): [dbt Cloud](https://docs.getdbt.com/docs/cloud/about-cloud/dbt-cloud-features), [Coalesce](https://docs.coalesce.io/), [Dataform](https://cloud.google.com/dataform/docs) — managed options
- **Do:**
    1. Rebuild the Phase-1 mart as a layered dbt project on DuckDB: sources with freshness checks, staging → marts.
    2. Implement a snapshot-based SCD2 fund/share-class dimension.
    3. Add tests on every model (generic + at least one singular/unit test on a NAV invariant).
    4. Generate docs and add an exposure for the EMT-shaped output.
    5. Run `dbt build` from scratch and confirm it is green.
- **Done when:**
    - [ ] `dbt build` is green from scratch with tests and docs.
    - [ ] The DAG is readable by a stranger and layered like medallion.
    - [ ] You can explain why each model has the materialization it has.
- Est. hours: 14

#### 5.2.2 Orchestrated ELT (build-vs-buy) — T2
- **Why:** "Fivetran + dbt" is the default managed ingestion pattern, and as architect you must price it against self-hosted connectors for a regulated EU estate where data sovereignty is a hard constraint. Managed ELT wins for long-tail SaaS sources and loses for core banking and mainframe feeds that need to stay inside the perimeter. Getting the crossover point wrong means either an engineer babysitting Airbyte forever or a surprise MAR bill.
- **Learn:**
    - MAR-based pricing mechanics — Monthly Active Rows and how cost scales with change volume *(Fivetran pricing)*
    - connector reliability economics — what you pay an engineer to maintain self-hosted connectors *(Airbyte deployment docs)*
    - when managed ELT wins — long-tail SaaS sources with maintained connectors *(Fivetran pricing)*
    - when it loses — core banking, mainframe, and data-sovereignty constraints *(Airbyte deployment docs)*
- **Resources:**
    - **[Fivetran pricing & architecture](https://www.fivetran.com/pricing)** — the MAR pricing model you must reason about (primary)
    - [Airbyte deployment documentation](https://docs.airbyte.com/) — self-hosting cost and operational profile for comparison (reference)
- **Do:**
    1. Write a half-page build-vs-buy note for a fund admin with 6 internal systems and 4 SaaS sources.
    2. Estimate Fivetran MAR cost for the SaaS sources and engineer-hours for self-hosting the internal ones.
    3. State the crossover point where managed cost beats maintained-Airbyte cost.
    4. Flag which internal sources cannot leave the EU perimeter at all.
- **Done when:**
    - [ ] You can state the crossover point where Fivetran's cost beats an engineer maintaining Airbyte.
    - [ ] You can name which sources are off-limits to managed ELT for sovereignty reasons.
- Est. hours: 2

#### 2.1.1 Batch ELT connectors — T2
- **Why:** Connector platforms are the workhorse of non-streaming ingestion, and hands-on Airbyte makes the managed-vendor conversation concrete instead of theoretical. For a fund administrator, the operating reality is incremental syncs with cursor fields and schema-change handling — exactly where self-hosted connectors quietly break. Running one yourself is how you learn what you are really paying Fivetran to absorb.
- **Learn:**
    - the connector model — source, destination, spec, and state *(Airbyte docs: Core concepts)*
    - incremental sync modes and cursor fields — append vs dedup, and how state advances *(Airbyte docs: Incremental sync)*
    - CDC-flavored connectors vs true log-based CDC — what each guarantees *(Airbyte docs: Core concepts)*
    - schema-change handling — what happens when a source column appears or changes type *(Airbyte docs: Incremental sync)*
    - the operating cost of self-hosting connectors — the hidden maintenance line item *(Airbyte deployment docs)*
- **Resources:**
    - **[Airbyte documentation](https://docs.airbyte.com/)** — core concepts, incremental sync, and self-hosting (primary)
    - [Airbyte: Incremental sync](https://docs.airbyte.com/using-airbyte/core-concepts/sync-modes/incremental-append-deduped) — cursor fields and state semantics in detail (reference)
- **Tools:**
    - FOSS (hands-on): [Airbyte OSS](https://docs.airbyte.com/) — self-hosted connectors in compose (↔ Fivetran, Stitch, ADF copy activity)
    - Corp (evaluate): [Fivetran](https://fivetran.com/docs) — the managed equivalent at build-vs-buy level
- **Do:**
    1. Stand up Airbyte in Docker Compose.
    2. Configure an incremental sync from the Phase-1 Postgres to MinIO Parquet using a cursor field.
    3. Run an initial sync, then an incremental one, and confirm only changed rows move.
    4. Break the cursor on purpose (e.g. reset/alter the cursor column) and repair the sync.
- **Done when:**
    - [ ] You can explain how state is kept and what happens on a re-sync after a schema change.
    - [ ] You can demonstrate an incremental sync moving only changed rows.
    - [ ] You can recover a broken cursor and explain what broke it.
- Est. hours: 4

#### 8.2.5 Data Vault modeling (+ 1.4.7 pattern) — T1
- **Why:** Data Vault is the financial-services-favored EDW pattern — auditability by construction and multi-source integration without re-modeling — and Luxembourg fund shops ask for it by name in job specs. Its hub/link/satellite split is what lets you absorb a second transfer-agency source without rewriting the warehouse, and its insert-only loading is what makes every change explainable to an auditor. Misuse it on a single small source and you have built ceremony with no payoff.
- **Learn:**
    - hubs, links, satellites — business keys, relationships, and history/context separately *(Data Vault 2.0 ch. 1–4)*
    - raw vault vs business vault — where raw integration ends and computed logic begins *(Data Vault 2.0 ch. 5–7)*
    - hash keys and hashdiffs — deterministic keys and cheap change detection *(Data Vault 2.0 ch. 11)*
    - loading patterns — parallel, insert-only, and why that is auditable *(Data Vault 2.0 ch. 11–12)*
    - PIT and bridge tables — restoring query performance over a normalized vault *(Data Vault 2.0 ch. 7)*
    - when Vault is overkill, and Vault-on-lakehouse with dbt/AutomateDV *(AutomateDV docs)*
- **Resources:**
    - **[Building a Scalable Data Warehouse with Data Vault 2.0 (Linstedt & Olschimke)](https://www.oreilly.com/library/view/building-a-scalable/9780128025109/)** ch. 1–7 (modeling) + ch. 11–12 (loading) (primary)
    - [AutomateDV documentation](https://automate-dv.readthedocs.io/) — the dbt package that generates hub/link/sat loads on the lakehouse (reference)
- **Tools:**
    - FOSS (hands-on): [dbt](https://docs.getdbt.com/) + [AutomateDV package](https://automate-dv.readthedocs.io/) — raw vault generated and tested (↔ VaultSpeed)
    - Corp (evaluate): [VaultSpeed](https://docs.vaultspeed.com/), [WhereScape](https://www.wherescape.com/), [Datavault Builder](https://datavault-builder.com/) — automation vendors
- **Do:**
    1. Model fund / share-class / administrator from two conflicting source systems as a raw vault (hubs/links/sats) with AutomateDV.
    2. Choose hub business keys deliberately for messy identifiers (ISIN reuse, internal codes) and justify them.
    3. Build one PIT table over the satellites for query performance.
    4. Land a late-arriving correction insert-only and show the full audit trail from the satellites.
- **Done when:**
    - [ ] You can defend hub key choices for messy real-world identifiers like reused ISINs.
    - [ ] You can explain insert-only loading and the audit trail it produces to an auditor.
    - [ ] You can show a late correction as a new satellite row, not an overwrite.
- Est. hours: 12

#### 1.12.1 ISO 20022 — T1
- **Why:** ISO 20022 is the lingua franca of EU payments and securities messaging, and fund platforms ingest and emit it daily — post-MT migration it is *the* message standard your canonical model must align to. An architect who cannot map a subscription order message onto the warehouse model will design something that drops fields auditors expect to trace. Knowing the message flow is how you reason about what your platform must capture at each hop.
- **Learn:**
    - message taxonomy — pacs/camt/sese/semt/setr business areas, and which matter for funds (setr orders, semt statements, sese settlement) *(iso20022.org: catalogue)*
    - XSD structure, business components, and external code sets *(iso20022.org: catalogue)*
    - the e-Repository and Message Definition Reports as the authoritative source *(iso20022.org: catalogue)*
    - mapping messages to a canonical model — where each business field lands *(iso20022.org: catalogue)*
    - MX-over-SWIFT context — how these messages travel *(SWIFT: standards)*
- **Resources:**
    - **[ISO 20022 message catalogue](https://www.iso20022.org/iso-20022-message-definitions)** — Message Definition Reports incl. setr (investment funds) (primary)
    - [SWIFT: standards](https://www.swift.com/standards) — MX-over-SWIFT context and the broader standards landscape (reference)
- **Do:**
    1. Obtain a sample `setr.010` (subscription order) message and its schema.
    2. Parse it with Python/lxml via `uv run`.
    3. Map every business field onto your Phase-1 model and record the mapping.
    4. Document the gaps — fields your current model cannot hold — and what they would require.
- **Done when:**
    - [ ] You can sketch the message flow (order → status → confirmation → settlement) and name the message type at each hop.
    - [ ] You can map a `setr.010` onto your model and list the unmappable fields.
- Est. hours: 6

#### 1.12.7 EMT / EPT (FinDatEx) — T1
- **Why:** EMT (MiFID target market and costs) and EPT (PRIIPs KID data) are the fund-data dissemination templates of the EU industry — the exact artifacts a Luxembourg fund-data platform produces and consumes every day. Producing a valid EMT is a regulatory data-product deliverable, and the architect must know which upstream attributes block it from completing. Treat these as afterthoughts and distribution stalls because a costs block is half-populated.
- **Learn:**
    - FinDatEx governance and template lifecycle/versioning — how EMT/EPT versions are released *(FinDatEx: templates)*
    - EMT structure — manufacturer target market and costs & charges blocks *(FinDatEx: templates)*
    - EPT structure — PRIIPs KID inputs (SRI, performance scenarios, costs) *(PRIIPs Regulation 1286/2014)*
    - CEPT and delta templates and how distributors consume them *(FinDatEx: templates)*
    - data-quality pain points — versioning, partial files, code lists *(FinDatEx: templates)*
- **Resources:**
    - **[FinDatEx templates](https://findatex.eu/)** — current EMT and EPT specifications, free downloads (primary)
    - [PRIIPs Regulation (EU) No 1286/2014](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014R1286) — the KID regulation behind EPT: SRI, performance scenarios, cost disclosure (reference)
- **Do:**
    1. Download the current EMT spec from FinDatEx and read the target-market and costs blocks.
    2. Build a dbt model set that produces an EMT V4-shaped output from your fund mart.
    3. Validate the output column-by-column against the spec, including code-list values.
    4. List the upstream attributes that, if missing, block EMT completion.
- **Done when:**
    - [ ] You can explain which upstream attributes block EMT completion and why.
    - [ ] You can explain what "regulatory data product" means concretely, using EMT as the example.
    - [ ] Your EMT output validates column-by-column against the FinDatEx spec.
- Est. hours: 5

#### 1.12.2 + 1.12.3 LEI & ISIN (entity and instrument identity) — T2
- **Why:** Identifier discipline is the difference between a fund platform and a data swamp — LEI and ISIN are the join keys of the entire industry. Treat an ISIN as a stable primary key and a corporate action that renames it will silently split one instrument into two in your warehouse. The architect must design a security master that survives identifier lifecycle events without losing history.
- **Learn:**
    - ISIN structure and allocation, and why ISIN ≠ listing (venue-level FIGI/MIC) *(ANNA: standards)*
    - LEI structure and the GLEIF registry *(GLEIF: LEI data)*
    - Level 1 (who-is-who) vs Level 2 (who-owns-whom) data *(GLEIF: Level 2 data)*
    - validation via check digits for both identifiers *(ANNA: standards)*
    - identifier lifecycle events — corporate actions that rename or retire ISINs *(ANNA: standards)*
- **Resources:**
    - **[GLEIF: LEI data](https://www.gleif.org/en/lei-data/gleif-golden-copy)** — golden copy, Level 1/Level 2 data, registry concepts (primary)
    - [ANNA — standards (ISIN ISO 6166)](https://www.anna-web.org/standards/) — ISIN structure, allocation, and check digits (reference)
- **Tools:**
    - FOSS (hands-on): [GLEIF golden copy](https://www.gleif.org/en/lei-data/gleif-golden-copy) — free LEI dataset loaded to lakehouse bronze
- **Do:**
    1. Download the GLEIF golden copy (free) and load it to your lakehouse bronze.
    2. Link your Faker funds to real LEIs of their (fictive) management companies.
    3. Add an internal surrogate key alongside ISIN in your security master.
    4. Sketch a corporate-action scenario where the ISIN changes and show your model keeps continuity via the surrogate.
- **Done when:**
    - [ ] You can explain why a security master needs both ISIN and an internal surrogate, with a concrete corporate-action scenario.
    - [ ] You can validate an ISIN and an LEI check digit.
    - [ ] You can distinguish Level 1 from Level 2 GLEIF data and say what each enables.
- Est. hours: 2

#### 1.12.8 SWIFT MT / MX — T2
- **Why:** Legacy MT messages still flow through fund operations — transfer agency and custody — so architects must read both worlds during the long MX coexistence period. A holdings statement arriving as an MT535 has fields that map lossily onto your richer model, and knowing which is which prevents silent data loss at the boundary. You will be the one who explains which MX message eventually replaces each MT.
- **Learn:**
    - MT message anatomy — blocks and tags for the fund-relevant set (MT502/509/515 orders, MT535/536 statements) *(SWIFT: standards)*
    - MX = ISO 20022 over SWIFT and the translation/coexistence rules *(SWIFT: standards)*
    - the MT-to-MX mapping — which MX message replaces a given MT *(iso20022.org: catalogue)*
    - what SWIFT network membership means operationally *(SWIFT: standards)*
- **Resources:**
    - **[SWIFT: standards](https://www.swift.com/standards)** — MT category 5 (securities) and MX/ISO 20022 standards landing (primary)
    - [ISO 20022 message catalogue](https://www.iso20022.org/iso-20022-message-definitions) — the MX messages that replace MT equivalents (reference)
- **Do:**
    1. Obtain a sample MT535 holdings statement (or a documented field layout from the standard).
    2. Hand-translate it into your model's terms, field by field.
    3. Note the lossy fields — where the MT carries less than your model, or vice versa.
    4. Identify the MX (ISO 20022) message that replaces MT535.
- **Done when:**
    - [ ] You can read an MT message with the spec open and know which MX message replaces it.
    - [ ] You can list the lossy fields in an MT535-to-model translation.
- Est. hours: 2

#### 9.6.2 Data documentation — T2
- **Why:** Generated, always-current documentation is a governance deliverable in its own right, and dbt docs is the gateway drug before the Phase 6 catalogs. In a fund platform a business analyst must be able to trace "where does this EMT field come from?" without interrupting you — that traceability is a regulatory expectation, not a nicety. Docs that drift from the models are worse than none because people trust them.
- **Learn:**
    - dbt docs generation and persistence — `persist_docs` to push descriptions into the warehouse *(dbt docs: documentation)*
    - exposures — declaring downstream consumers like the EMT output *(dbt docs: exposures)*
    - what belongs in model YAML vs the enterprise catalog *(dbt docs: documentation)*
    - docs-as-code review flow — descriptions reviewed in PRs alongside SQL *(dbt docs: documentation)*
- **Resources:**
    - **[dbt docs: documentation](https://docs.getdbt.com/docs/build/documentation)** — generating, persisting, and structuring model docs (primary)
    - [dbt docs: exposures](https://docs.getdbt.com/docs/build/exposures) — declaring downstream consumers in the DAG (reference)
- **Tools:**
    - FOSS (hands-on): [dbt docs](https://docs.getdbt.com/docs/build/documentation) — generated lineage and descriptions (↔ catalog-generated docs in Phase 6)
    - Corp (evaluate): [dbt Cloud docs](https://docs.getdbt.com/docs/collaborate/build-and-view-your-docs) / [Purview](https://learn.microsoft.com/purview/) lineage views
- **Do:**
    1. Fully document the capstone dbt project: every model and column description.
    2. Declare one exposure for the EMT output, naming its consumer.
    3. Run `dbt docs generate` and browse the lineage graph for the EMT field path.
    4. Plan to publish the static docs site from CI later in Phase 3.
- **Done when:**
    - [ ] A business analyst can answer "where does this EMT field come from?" without asking you.
    - [ ] Every model and column in the capstone has a description.
    - [ ] The EMT output is declared as an exposure with its consumer named.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.4.6 | Hub-and-spoke | Centralized integration hub feeding domain marts; the pre-mesh enterprise default architecture | [*Data Management at Scale* ch. 2 (architecture survey)](https://www.oreilly.com/library/view/data-management-at/9781098138851/) | 20 |
| 1.12.4 | CFI (ISO 10962) | 6-character instrument classification code carried in reference data, complementing the ISIN | [ANNA standards (CFI ISO 10962)](https://www.anna-web.org/standards/) | 20 |
| 1.12.5 | FIGI | Bloomberg's open venue-level instrument identifier; the ISIN complement for listing-level identity | [OpenFIGI — about FIGI](https://www.openfigi.com/about/figi) | 20 |
| 1.12.9 | FpML | ISDA's XML standard for OTC derivatives; appears at fund boundaries (hedging share classes) | [FpML official site](https://www.fpml.org/) | 20 |
| 1.12.10 | FIX | Trading-venue messaging protocol; upstream of fund data and rarely modeled directly by you | [FIX Trading Community — standards](https://www.fixtrading.org/standards/) | 20 |
| 1.12.11 | IBAN / SEPA | Payment-account identity standard underpinning EU cash legs of fund subscriptions/redemptions | [ECB — SEPA overview](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html) | 15 |
| 3.1.2 | On-prem MPP warehouses | Teradata/Vertica/Netezza estates you will most often migrate *from* into a lakehouse | [Teradata documentation](https://docs.teradata.com/) | 30 |
| 3.2.11 | Geospatial storage | PostGIS/GeoParquet/H3; ESG and real-asset edge cases in fund and alternatives data | [PostGIS — home](https://postgis.net/) + [GeoParquet spec](https://geoparquet.org/) | 30 |
| 5.3.3 | PRQL / Malloy | Composable, pipelined query-language challengers to SQL with an in-browser tour | [PRQL — language site & playground](https://prql-lang.org/) | 20 |
| 5.4.1 | Interactive data prep | Visual cleanup tools (Alteryx/DataBrew) typically bought and owned by business teams | [Alteryx product overview](https://www.alteryx.com/products/alteryx-designer) | 15 |
| 8.2.6 | Anchor modeling / 6NF | Fully temporal, highly normalized modeling; Data Vault's stricter 6NF cousin | [Anchor Modeling — official site](https://anchormodeling.com/) | 30 |

*T3 subtotal: 4 h*

### Capstone 2 — Fund-document lakehouse

- **Goal:** a working open lakehouse carrying real fund-data shapes (NAV series, holdings, EMT outputs, GLEIF entities) through bronze→silver→gold, with the format/catalog decisions documented like a vendor selection.
- **Stack (100% free):** [MinIO](https://min.io/docs/minio/linux/index.html) (↔ ADLS Gen2), [Apache Iceberg](https://iceberg.apache.org/docs/latest/) (↔ Databricks Delta / Snowflake managed Iceberg), [Lakekeeper](https://docs.lakekeeper.io/) or [Apache Polaris](https://polaris.apache.org/) REST catalog (↔ Unity Catalog / Glue), [Trino](https://trino.io/docs/current/) (↔ Starburst / Athena / Synapse serverless), [DuckDB](https://duckdb.org/docs/) + [dbt Core](https://docs.getdbt.com/) (↔ dbt Cloud on a warehouse), [Airbyte OSS](https://docs.airbyte.com/) (↔ Fivetran / ADF), [AutomateDV](https://automate-dv.readthedocs.io/) raw-vault slice (↔ VaultSpeed), [Docker Compose](https://docs.docker.com/compose/) throughout.
- **Build:** (1) Airbyte lands Phase-1 Postgres + GLEIF golden copy into bronze (Parquet on MinIO); (2) silver Iceberg tables: cleansed NAV/holdings with DQ-checked conformance, raw vault for fund/share-class from two "source systems"; (3) gold: dbt marts incl. the EMT-shaped output and the SCD2 dimensional mart; (4) Trino federates a live Postgres dimension against Iceberg facts; (5) demonstrate time travel + schema evolution + a compaction run. Drive every step from documented commands so the whole stack rebuilds from an empty MinIO.
- **Architecture deliverables:** C4 context/container for the lakehouse; ADR-004 Iceberg vs Delta (estate-specific), ADR-005 REST catalog choice (lock-in analysis), ADR-006 medallion layer contracts (the sheet from 1.4.3 made binding).
- **Acceptance criteria:** end-to-end rebuild from empty MinIO via documented commands; `dbt build` green with tests + docs published; EMT output validates against the FinDatEx column spec; time-travel query reproduces yesterday's NAV report after a correction lands; every stack component annotated with its corporate equivalent in the README; the catalog can be swapped (Hive-style → REST) without rewriting data files.
- Est. hours: 16

*Phase 2 total: 123 h (T1/T2 entries 103 h + T3 4 h + capstone 16 h)*


<a id="phase-3"></a>
## Phase 3: Distributed Compute, Orchestration & Engineering Practice (months 17–21, 118 h)

*Phase 3 of 8 · months 17–21 · 118 h · capstone: Orchestrated Spark NAV pipeline.*  ← [Phase 2](#phase-2) · [Phase 4](#phase-4) →

**Goal:** close the two biggest gaps that block scale — Spark and orchestration — and wrap the platform in software-engineering discipline: CI/CD for data, data versioning with write-audit-publish, integration testing, and managed schema change.
**Entry prerequisites:** Phase 2 (lakehouse running; dbt project to orchestrate).
**Exit criteria:** you can (1) explain a Spark job's stages and fix a skewed join from the UI; (2) defend Airflow vs Dagster vs ADF for a given team; (3) ship a pipeline change through CI with tests, data diff, and an audited publish; (4) run schema change in a regulated estate without downtime (expand–contract).

### T1/T2 topics

#### 4.1.1 Distributed batch compute (Spark) — T1
- **Why:** Spark is the named weak spot and the default heavy-lift engine in every fund-data estate — Databricks, Synapse and Fabric all sell it, so the architect signs off on Spark designs whether or not they chose Spark. An architect who can't read the Spark UI can't review the platform's biggest bills, can't challenge a vendor's "just add nodes" answer, and will rubber-stamp a skewed NAV-calculation job that burns four hours nightly when twenty minutes would do.
- **Learn:**
    - architecture: driver/executors, jobs→stages→tasks — how one action fans out into stages split by shuffles, and why the shuffle is where money goes *(Learning Spark ch. 1–2)*
    - DataFrame API and lazy evaluation — transformations build a plan, actions trigger it; what that means for debugging *(Learning Spark ch. 3–4)*
    - Catalyst optimizer + AQE — how the planner rewrites your query and what adaptive execution fixes at runtime *(Spark docs: SQL Performance Tuning)*
    - partitioning, skew, salting — why one hot ISIN or fund ID stalls a 200-task stage at task 199 *(Spark docs: SQL Performance Tuning)*
    - join strategies — broadcast vs sort-merge, the autoBroadcastJoinThreshold, and when the planner picks wrong *(Learning Spark ch. 7)*
    - caching/persistence levels and the memory model — executor memory regions, spill, and OOM debugging from the error upward *(Spark docs: Tuning)*
    - writing to Iceberg from Spark — catalogs, `MERGE INTO`, and the WAP hooks you'll use in 9.2.2 *(Iceberg docs: Spark)*
    - deployment modes at decision level — local, standalone, K8s, Databricks; what changes operationally between them *(Learning Spark ch. 1)*
- **Resources:**
    - **[Learning Spark, 2nd ed.](https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/) (Damji et al.) ch. 1–7 + 12** — architecture, DataFrame API, Spark SQL, joins, and tuning in one pass (primary)
    - [Spark docs: Tuning](https://spark.apache.org/docs/latest/tuning.html) + [SQL Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — memory model, caching, AQE, skew-join handling — the exact knobs you'll turn in the lab (reference)
    - [Iceberg docs: Spark](https://iceberg.apache.org/docs/latest/) — Spark reads/writes into Iceberg tables, the lakehouse seam this phase exercises (reference)
    - [Spark: The Definitive Guide](https://www.oreilly.com/library/view/spark-the-definitive/9781491912201/) pt. II — alternate treatment of the structured APIs if Learning Spark's pace doesn't suit (alternate)
- **Tools:**
    - FOSS (hands-on): [Apache Spark](https://spark.apache.org/docs/latest/) — local mode + compose cluster is the whole lab (↔ Databricks / Synapse Spark / EMR)
    - Corp (evaluate): [Databricks](https://docs.databricks.com/) — the de-facto enterprise Spark; know Photon, cluster types and pricing well enough to challenge a quote
- **Do:**
    1. Generate a 50M-row holdings/prices dataset (PySpark or DuckDB export) with realistic skew: a handful of mega-funds holding most positions.
    2. Compute per-fund daily NAV and rolling 30-day performance in PySpark against MinIO/Iceberg from the Phase-2 stack; note wall-clock and shuffle volumes from the Spark UI.
    3. Engineer a skewed join (positions × fund reference data keyed on the hot fund IDs); diagnose it in the UI — find the straggler task, its shuffle read size, and the stage timeline.
    4. Fix it twice: once with a broadcast hint, once with salting; compare against AQE's automatic skew-join handling.
    5. Document before/after stage timings with UI screenshots, and finish with a one-paragraph rule of thumb for when DuckDB on one node beats the cluster.
- **Done when:**
    - [ ] Given an unfamiliar slow job, you go UI → stages → shuffle/skew → fix, and can explain each step to a junior.
    - [ ] You can explain why the skewed join stalled (one straggler task, not "Spark is slow") and show the evidence in the UI.
    - [ ] You can state the broadcast threshold trade-off and what AQE does and doesn't rescue.
    - [ ] You can argue when Spark is the *wrong* tool (DuckDB-size data) with numbers from your own runs.
- Est. hours: 36

#### 5.3.2 DataFrame transformation layer (PySpark / Polars / Ibis) — T2
- **Why:** the code half of the transformation layer; choosing SQL vs DataFrames — and which DataFrame runtime — is a standards decision the architect owns and every team inherits. Get it wrong and you end up with NAV logic duplicated in three dialects, pandas row loops melting the cluster, and no answer when an auditor asks where a number was computed.
- **Learn:**
    - PySpark idioms vs pandas habits — no row loops, window specs over groupby-apply, columnar thinking *(PySpark docs)*
    - Polars lazy frames — the query optimizer behind `LazyFrame`, and when Polars on one node replaces Spark below ~100GB *(Polars guide: Lazy API)*
    - Ibis as a portable dataframe API — one expression language compiled to 20+ engines, and what that buys a multi-engine estate *(Ibis docs: Why Ibis)*
    - UDF cost model — Python UDF vs pandas/Arrow UDF vs native expression, and why serialization is the hidden tax *(PySpark docs)*
    - layer ownership as a standard — which transformation types belong in dbt SQL vs DataFrame code, and who enforces it *(Ibis docs: Why Ibis)*
- **Resources:**
    - **[Polars user guide: Lazy API](https://docs.pola.rs/user-guide/lazy/)** — lazy frames, optimization, query plans (primary)
    - [Ibis: Why Ibis](https://ibis-project.org/why) — the portability argument and the backend model (reference)
    - [PySpark documentation](https://spark.apache.org/docs/latest/api/python/) — idioms, window functions, pandas-on-Spark and Arrow/pandas UDFs (reference)
- **Tools:**
    - FOSS (hands-on): [Polars](https://docs.pola.rs/), [Ibis](https://ibis-project.org/), [PySpark](https://spark.apache.org/docs/latest/api/python/) — three runtimes, one transformation, run via uv (↔ Snowpark)
    - Corp (evaluate): [Snowpark](https://docs.snowflake.com/en/developer-guide/snowpark/index) / [Databricks](https://docs.databricks.com/) — the same concepts rebranded; know the lock-in trade-off
- **Do:**
    1. Pick one silver transformation from the Phase-2 lakehouse (e.g. EMT-style share-class enrichment of holdings).
    2. Implement it three ways: PySpark, Polars (lazy), and dbt SQL; verify all three produce identical output on the same input sample.
    3. Time each on the 50M-row dataset and on a 1M-row sample; record where each wins.
    4. Write a half-page standards note: which layer owns which transformation type (set-based joins/aggregations vs procedural enrichment vs ML feature prep) and why, citing your timings.
- **Done when:**
    - [ ] Your standards note survives the question "why not do everything in SQL?"
    - [ ] You can name the dataset size and shape where Polars beats Spark, with your own numbers.
    - [ ] You can explain to a reviewer what a Python UDF costs versus a native expression and how you'd detect the difference in a job profile.
- Est. hours: 8

#### 5.6.1 + 5.6.3 Orchestration (Airflow + Dagster, task- vs asset-oriented) — T1
- **Why:** orchestration is in the explicit mastery bias: the scheduler is the platform's nervous system, and the task-vs-asset paradigm choice shapes team workflow for years. In a fund platform the orchestrator is what guarantees the NAV pipeline ran, in order, exactly once per valuation day — without that discipline, a missed upstream file silently produces yesterday's prices in today's report and the transfer agent finds out from a client.
- **Learn:**
    - Airflow core — DAGs, operators, sensors, and idempotent task design so reruns are safe *(Data Pipelines with Airflow ch. 1–4)*
    - backfills and catchup — how scheduled intervals, `catchup`, and `backfill` interact, and the executors (Local/Celery/K8s) that run it all *(Data Pipelines with Airflow ch. 12)*
    - Airflow datasets / data-aware scheduling — triggering on data readiness instead of clock time *(Airflow docs)*
    - Dagster software-defined assets — assets, partitions, asset checks; why asset-orientation gives lineage and freshness for free *(Dagster docs)*
    - declarative automation — letting the orchestrator derive "what needs to run" from asset state rather than hand-wired triggers *(Dagster docs)*
    - failure handling — retries, SLAs/freshness alerts, and what a sane on-call page contains *(Data Pipelines with Airflow ch. 12)*
    - orchestrator anti-patterns — business logic in DAG files, XCom abuse, non-idempotent tasks *(Airflow docs)*
    - the market map — Prefect/Mage awareness; ADF + Workflow Orchestration Manager (managed Airflow) as the Azure reality *(ADF docs)*
- **Resources:**
    - **[Dagster documentation](https://docs.dagster.io/)** — assets, partitions, asset checks, declarative automation (primary)
    - [Data Pipelines with Apache Airflow, 2nd ed.](https://www.manning.com/books/data-pipelines-with-apache-airflow-second-edition) (Harenslak, de Ruiter et al.) ch. 1–6, 12 — task-oriented orchestration done properly, incl. backfills and operations (reference)
    - [Apache Airflow documentation](https://airflow.apache.org/docs/) — executors, data-aware scheduling, best-practices section on anti-patterns (reference)
    - [Azure Data Factory documentation](https://learn.microsoft.com/azure/data-factory/) — the corp baseline you'll be asked to compare against (evaluation)
- **Tools:**
    - FOSS (hands-on): [Dagster](https://docs.dagster.io/) — primary orchestrator for the capstone (↔ Dagster+ / ADF)
    - FOSS (market fluency): [Apache Airflow](https://airflow.apache.org/docs/) — one comparison DAG; the incumbent in most fund-admin shops (↔ MWAA / Cloud Composer)
    - Corp (evaluate): [Azure Data Factory](https://learn.microsoft.com/azure/data-factory/), [MWAA](https://docs.aws.amazon.com/mwaa/), [Cloud Composer](https://cloud.google.com/composer/docs) — managed offerings at build-vs-buy level: pricing model, upgrade cadence, lock-in
- 🐘 **Postgres-native alternative — [pg_cron](https://github.com/citusdata/pg_cron):** *Better when* the need is just periodic SQL in one database — refresh a materialized view, nightly cleanup, a scheduled `VACUUM` — with zero extra infrastructure. *Worse when* you have cross-system DAGs, inter-task dependencies, backfills, retries, or lineage: pg_cron has no dependency graph or observability, so reach for Dagster/Airflow.
- **Do:**
    1. Orchestrate the Capstone-2 pipeline as Dagster assets with daily partitions; add asset checks for row counts and NAV-total reconciliation.
    2. Wire declarative automation so the gold layer rebuilds when silver assets materialize, not on a cron guess.
    3. Rebuild one branch of the pipeline as an Airflow DAG with a sensor, idempotent tasks, and catchup configured deliberately.
    4. Break a transformation, fix it, then run a 30-day backfill in each tool; record which partitions recomputed and how you proved it.
    5. Write a comparison memo (dev loop, backfills, lineage, ops burden, team skill demands) ending in a recommendation for a 6-person fund-data team on Azure.
- **Done when:**
    - [ ] You can run a clean 30-day backfill after a logic fix and explain exactly which partitions recomputed and why.
    - [ ] You can articulate task- vs asset-oriented orchestration in two minutes with one fund-industry example each.
    - [ ] Your memo defends Dagster vs Airflow vs ADF for a named team profile and survives "but ADF is already included in our Azure agreement".
- Est. hours: 20

#### 9.2.2 Data versioning & write-audit-publish — T2
- **Why:** branch-merge workflows for data are how regulated platforms ship changes without bad data reaching consumers; WAP is the pattern auditors love because the audit step is structural, not a promise. Without it, a corrupted price file lands directly in the gold layer, the NAV goes out wrong, and the remediation is a restatement letter instead of a quietly deleted branch.
- **Learn:**
    - Iceberg branches and tags natively — snapshot lineage, branch retention, and tags as immutable audit markers *(Iceberg docs: Branching and Tagging)*
    - the write-audit-publish flow — write to a staging branch, run checks, fast-forward main only on green *(Iceberg docs: Branching and Tagging)*
    - lakeFS Git-like model — repos, branches, merges over object storage, when you need versioning across many tables at once *(lakeFS docs)*
    - Nessie — catalog-level versioning as an alternative seam for multi-table transactions *(Project Nessie)*
    - DVC — file-oriented versioning for ML-ish artifacts; awareness only *(DVC docs)*
    - choosing the granularity — table-level (Iceberg) vs lake-level (lakeFS/Nessie) versioning, and what each costs operationally *(lakeFS docs)*
- **Resources:**
    - **[Iceberg docs: Branching and Tagging](https://iceberg.apache.org/docs/latest/branching/)** — branch/tag semantics, audit-branch use case, the WAP building blocks (primary)
    - [lakeFS documentation](https://docs.lakefs.io/) — the Git-for-data model, how it works, and the WAP tutorial (reference)
    - [Project Nessie](https://projectnessie.org/) — catalog-level versioning concept (awareness)
    - [DVC documentation](https://dvc.org/doc) — file/artifact versioning for completeness (awareness)
- **Tools:**
    - FOSS (hands-on): [Apache Iceberg](https://iceberg.apache.org/docs/latest/) branches, [lakeFS](https://docs.lakefs.io/) — (↔ no direct corp equivalent — Databricks/Snowflake time travel + clones approximate it)
    - Corp (evaluate): [Snowflake zero-copy cloning](https://docs.snowflake.com/en/user-guide/object-clone) — what clones give you and where they fall short of true branch-merge
- **Do:**
    1. Add a WAP stage to the Dagster pipeline: every load writes to an Iceberg `audit` branch instead of main.
    2. Run the existing DQ asset checks against the branch; on green, fast-forward publish to main; on red, alert and hold the branch for inspection.
    3. Inject a deliberately corrupted load (e.g. prices off by 100x for one ISIN) and walk the failure path end to end.
    4. Tag each published snapshot with the valuation date; demonstrate time-travel back to a prior tag as the audit story.
- **Done when:**
    - [ ] A deliberately corrupted load never becomes visible to the gold consumer, and you can show the audit trail.
    - [ ] You can demonstrate which snapshot a given day's NAV report was computed from, using tags alone.
    - [ ] You can explain to a CAB when table-level branching suffices and when lakeFS-style lake-level versioning is worth the extra moving part.
- Est. hours: 8

#### 9.3.1 CI/CD for data platforms — T2
- **Why:** the deployment pipeline is where engineering standards become enforceable; data teams without CI ship regressions to regulators. The architect defines what "cannot merge" means — without that gate, a broken dbt test rides into production on a Friday and the Monday NAV run is the test environment.
- **Learn:**
    - GitHub Actions core — workflows, jobs, environments, secrets, matrix builds *(GitHub Actions docs)*
    - what to run per PR vs per merge for a data repo — ruff lint, unit tests, dbt build on a prod-like sample, docs publish on merge *(dbt docs: Continuous integration)*
    - deployment gates and approvals — environments with required reviewers as the change-advisory checkpoint *(GitHub Actions docs)*
    - secrets hygiene — OIDC over long-lived keys, least-privilege tokens for the warehouse *(GitHub Actions docs)*
    - GitOps concept — declarative desired state, Argo CD awareness for the later K8s phase *(Argo CD docs)*
- **Resources:**
    - **[GitHub Actions documentation](https://docs.github.com/en/actions)** — workflows, environments, secrets, matrix jobs (primary)
    - [dbt docs: Continuous integration](https://docs.getdbt.com/docs/deploy/continuous-integration) — what a dbt CI job builds and tests, and why only modified assets (reference)
    - [Argo CD documentation](https://argo-cd.readthedocs.io/) — GitOps mechanics at awareness level (deepening)
- **Tools:**
    - FOSS (hands-on): [GitHub Actions](https://docs.github.com/en/actions) + [ruff](https://docs.astral.sh/ruff/) — the CI runner and linter for the capstone repo (↔ Azure DevOps Pipelines, GitLab CI)
    - Corp (evaluate): [Azure DevOps](https://learn.microsoft.com/azure/devops/) — the EU enterprise default; know pipelines, environments and approvals well enough to map your GitHub Actions design across
- **Do:**
    1. Add a PR workflow to the capstone repo: ruff check, `uv run pytest` (unit), then `dbt build --select state:modified+` against a prod-like sample schema.
    2. Add a merge workflow: full dbt build plus dbt docs site publish.
    3. Configure a protected environment with a required reviewer for the publish step, and store warehouse credentials as environment secrets.
    4. Open a PR that deliberately breaks a dbt test; confirm the merge is blocked and the failure is legible in the PR checks.
- **Done when:**
    - [ ] A PR that breaks a dbt test cannot merge, and you can explain every job in the workflow file.
    - [ ] You can justify the PR-vs-merge split (what runs where, and what each minute of CI costs).
    - [ ] You can sketch the equivalent Azure DevOps pipeline on a whiteboard for an enterprise that mandates it.
- Est. hours: 8

#### 9.3.2 Data-aware CI — T2
- **Why:** code-green/data-wrong is the classic data regression; data-aware CI (state deferral, data diff) catches what unit tests can't. A WHERE-clause tweak that passes every schema test can still drop 3% of share classes from the EMT feed — only comparing the data before and after the change catches that.
- **Learn:**
    - dbt slim CI — `state:modified` selection so CI builds only what changed plus downstream *(dbt docs: state method)*
    - defer — resolving unselected refs to prod artifacts instead of rebuilding the world *(dbt docs: Defer)*
    - SQLMesh virtual environments and plans — automatic change categorization (breaking vs non-breaking) and what it decides to backfill *(SQLMesh docs: Plans)*
    - data-diff concept — row/column-level diffs between prod and the PR build, and Datafold as the managed version *(data-diff README)*
    - cost model — when slim CI is enough and when diff-based CI pays for itself in warehouse spend avoided *(SQLMesh docs: Plans)*
- **Resources:**
    - **[SQLMesh docs: Plans](https://sqlmesh.readthedocs.io/en/stable/concepts/plans/)** — plans, virtual environments, breaking vs non-breaking categorization (primary)
    - [dbt docs: state:modified method](https://docs.getdbt.com/reference/node-selection/methods) — state comparison and its sub-selectors (reference)
    - [dbt docs: Defer](https://docs.getdbt.com/reference/node-selection/defer) — the deferral mechanics slim CI depends on (reference)
    - [data-diff README](https://github.com/datafold/data-diff) — the open-source diff tool and the Datafold context around it (reference)
- **Tools:**
    - FOSS (hands-on): [SQLMesh](https://sqlmesh.readthedocs.io/en/stable/) (eval hands-on), [dbt](https://docs.getdbt.com/) slim CI — two philosophies of change safety (↔ Datafold)
    - Corp (evaluate): [Datafold](https://www.datafold.com/) — managed column-level diffs in CI; know its pricing logic for a build-vs-buy memo
- **Do:**
    1. Craft one genuinely breaking change (a filter that silently drops rows) and one non-breaking change (an added column) in the capstone dbt project.
    2. Run both through dbt slim CI (`state:modified+` with `--defer`); record what was built, what passed, and what slipped through.
    3. Mirror the same two changes in a small SQLMesh project; run `sqlmesh plan` and record its categorization and proposed backfill.
    4. Tabulate: change × tool × caught/missed × compute cost; close with a one-paragraph recommendation.
- **Done when:**
    - [ ] You can tell a team when slim CI is enough and when diff-based CI pays for itself.
    - [ ] You can show one concrete change that dbt tests passed but a data diff would have caught.
    - [ ] You can explain SQLMesh's breaking/non-breaking decision for both of your changes.
- Est. hours: 5

#### 9.4.3 Integration testing for pipelines — T2
- **Why:** pipelines fail at the seams (connections, schemas, permissions); throwaway-infra tests are the only honest test of the seams. Mocked unit tests pass forever while the real loader fails on the first NUMERIC overflow from the actual Postgres — in a regulated shop, "it worked against the mock" is not a defence.
- **Learn:**
    - Testcontainers-python — real Postgres/MinIO/Kafka containers per test, lifecycle and port wiring *(Testcontainers docs)*
    - the test pyramid for data — unit SQL → component → end-to-end on a sample, and why the top is thin *(Fowler: Practical Test Pyramid)*
    - golden datasets and snapshot testing — fixture-driven known-good inputs/outputs and asserting end-state invariants *(pytest docs)*
    - idempotency as a testable property — run the loader twice, assert identical end state *(Testcontainers docs)*
    - contract tests preview — Pact's consumer-driven idea, mapped to data contracts coming in Phase 8 *(Pact docs)*
- **Resources:**
    - **[Testcontainers for Python documentation](https://testcontainers-python.readthedocs.io/)** — container fixtures for Postgres, MinIO, Kafka (primary)
    - [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) — the canonical layering argument, adapted here to data *(reference)*
    - [pytest documentation](https://docs.pytest.org/) — fixtures, markers, parametrization for golden-dataset tests (reference)
    - [Pact documentation](https://docs.pact.io/) — contract-testing concept at awareness level (deepening)
- **Tools:**
    - FOSS (hands-on): [Testcontainers](https://testcontainers-python.readthedocs.io/), [pytest](https://docs.pytest.org/) — run via uv against local Docker (↔ same)
    - Corp: same — this layer is tool-agnostic; the discipline, not the vendor, is the deliverable
- **Do:**
    1. Add a `tests/integration` package with pytest fixtures that spin up Postgres and MinIO via Testcontainers.
    2. Load a golden dataset (small holdings file with known NAV totals) and run the idempotent loader once; assert row counts, checksums and the NAV reconciliation.
    3. Run the loader a second time against the same containers; assert the end state is byte-identical (the idempotency proof).
    4. Mark the suite `-m integration`, exclude it from the default run, and wire it into the CI workflow from 9.3.1.
- **Done when:**
    - [ ] `uv run pytest -m integration` passes on a machine with only Docker installed.
    - [ ] Demonstrate the double-run idempotency assertion failing when you deliberately break the loader's upsert.
    - [ ] Explain where the integration layer sits in your test pyramid and what stays in unit tests below it.
- Est. hours: 5

#### 9.7.1 Schema migrations & change management — T2
- **Why:** regulated estates change schemas under change-advisory scrutiny; expand–contract and versioned migrations are how you do it without downtime or drama. A column rename done naively takes the transfer-agency feed down mid-dealing-window; done as parallel change, nobody notices — and the migration history table is the CAB evidence.
- **Learn:**
    - Flyway's model — versioned vs repeatable/declarative migrations, checksums, the schema history table *(Flyway docs)*
    - Alembic — the Python-shop equivalent: autogenerate, review, and the offline SQL mode for DBA sign-off *(Alembic docs)*
    - expand–contract (parallel change) — add-new, migrate-writes, backfill, contract-old as separate deployable steps *(Fowler: Parallel Change)*
    - deployment ordering — DB before code, every migration backward-compatible with the running release *(Fowler: Evolutionary Database Design)*
    - rollback reality — why you roll forward, and what a tested down-path is actually for *(Flyway docs)*
- **Resources:**
    - **[Flyway documentation](https://documentation.red-gate.com/fd)** — concepts, versioned migrations, history table (primary)
    - [Martin Fowler: Parallel Change](https://martinfowler.com/bliki/ParallelChange.html) — the expand–contract pattern itself (reference)
    - [Martin Fowler: Evolutionary Database Design](https://martinfowler.com/articles/evodb.html) — migrations as the unit of database change in a delivery pipeline (deepening)
    - [Alembic documentation](https://alembic.sqlalchemy.org/) — the Python alternative you may standardize on instead (alternate)
- **Tools:**
    - FOSS (hands-on): [Flyway](https://documentation.red-gate.com/fd) or [Alembic](https://alembic.sqlalchemy.org/) — pick one for the lab (↔ Liquibase enterprise, Redgate)
    - Corp (evaluate): [Liquibase](https://docs.liquibase.com/) Pro / Azure DevOps-integrated change flows — what the governed-pipeline tier adds: drift detection, targeted rollback, approvals
- **Do:**
    1. Put the Phase-1 Postgres schema under Flyway (or Alembic) control: baseline migration plus history table.
    2. Plan a column rename on a table the loader writes to, as three migrations: V2 expand (add new column + sync trigger or dual-write), V3 backfill + switch reads, V4 contract (drop old column).
    3. Keep the loader running on a schedule throughout; apply each migration live and watch for failed loads.
    4. Record the migration history and write a five-line CAB-style change record: risk, rollback stance (roll forward), evidence.
- **Done when:**
    - [ ] Zero failed loads during the rename, and the migration history table tells the full story.
    - [ ] Explain why the contract step shipped last and what would break if V2 and V4 were one migration.
    - [ ] Defend "roll forward" to a change board that asks for a rollback script.
- Est. hours: 5

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 4.4.1 | General distributed frameworks | Ray/Dask — Python-native distributed compute beyond Spark; ML-leaning, actor-based scaling | [Ray "Overview" docs page](https://docs.ray.io/en/latest/ray-overview/index.html) | 30 |
| 4.4.2 | Specialized frameworks | Modin etc. — drop-in pandas acceleration on Ray/Dask; niche in practice | [Modin README](https://github.com/modin-project/modin) | 10 |
| 5.1.2 | Code-first ETL (NiFi) | Visual flow-based ingestion engine; common in banks' legacy ingestion estates you may inherit | [NiFi "Overview" doc](https://nifi.apache.org/documentation/) | 25 |
| 9.4.4 | Load/performance testing | k6/Locust/JMeter — throughput and latency testing for data APIs and query engines | [k6 "What is k6" page](https://grafana.com/docs/k6/latest/) | 25 |
| 9.5.2 | Data diff tools | Row-level diffs across model changes (data-diff, Datafold); seen hands-on in 9.3.2 | [Datafold data-diff README](https://github.com/datafold/data-diff) | 20 |
| 9.6.1 | Code documentation | MkDocs/Sphinx static docs sites; you'll publish dbt docs instead | [MkDocs getting started](https://www.mkdocs.org/getting-started/) | 20 |
| 9.9.1 | Notebooks in production | Papermill/Ploomber parameterized notebook jobs; contested practice in regulated shops | [Papermill README](https://github.com/nteract/papermill) | 20 |

*T3 subtotal: 2.5 h*

### Capstone 3 — Orchestrated Spark NAV pipeline

- **Goal:** the lakehouse grows an industrial-strength compute and delivery layer: Spark for scale, Dagster for orchestration, WAP for safety, CI for discipline.
- **Stack (100% free):** [Apache Spark](https://spark.apache.org/docs/latest/) (↔ [Databricks](https://docs.databricks.com/) / [Synapse Spark](https://learn.microsoft.com/azure/synapse-analytics/)), [Dagster OSS](https://docs.dagster.io/) (↔ Dagster+ / [ADF](https://learn.microsoft.com/azure/data-factory/)), [Airflow](https://airflow.apache.org/docs/) (one comparison DAG; ↔ [MWAA](https://docs.aws.amazon.com/mwaa/) / [Composer](https://cloud.google.com/composer/docs)), [Iceberg](https://iceberg.apache.org/docs/latest/branching/) branches for WAP (↔ [Snowflake clones](https://docs.snowflake.com/en/user-guide/object-clone)), [lakeFS](https://docs.lakefs.io/) optional layer (↔ —), [GitHub Actions](https://docs.github.com/en/actions) (↔ [Azure DevOps](https://learn.microsoft.com/azure/devops/)), [Testcontainers](https://testcontainers-python.readthedocs.io/) + [pytest](https://docs.pytest.org/) via [uv](https://docs.astral.sh/uv/), [Flyway](https://documentation.red-gate.com/fd) (↔ [Liquibase Pro](https://docs.liquibase.com/)), all on the Phase-2 compose stack.
- **Build:** (1) Spark job computes daily NAV + rolling performance from 50M-row holdings/prices into silver Iceberg, reusing the skew fixes from 4.1.1; (2) Dagster assets wrap ingestion → Spark → dbt gold with daily partitions and asset checks (row counts + NAV reconciliation); (3) WAP: every load lands on an Iceberg audit branch, publishes to main only on green checks, holds and alerts on red; (4) CI runs lint (ruff), unit, integration (Testcontainers), and slim dbt build (`state:modified+` with defer) per PR; (5) Flyway manages the Postgres source schema, demonstrated with a live expand–contract change under a running loader; (6) 30-day backfill executed and timed, with the recomputed partition set documented.
- **Architecture deliverables:** C4 container diagram updated with compute/orchestration layer; ADR-007 orchestrator selection (Dagster vs Airflow vs ADF), ADR-008 WAP via Iceberg branches, ADR-009 Spark-vs-DuckDB engine threshold (when the cluster is justified).
- **Acceptance criteria:** full pipeline green from `dagster dev` + one CLI command; corrupted-load drill leaves gold untouched with an audit trail (branch held, alert fired, snapshot evidence); skewed-join fix documented with before/after Spark-UI screenshots and stage timings; backfill recomputes exactly the intended partitions and nothing else; CI blocks a breaking PR in under 10 minutes with a legible failure; expand–contract change applied with zero failed loads.
- Est. hours: 20

*Phase 3 total: 118 h (T1/T2 entries 95 h + T3 2.5 h + capstone 20 h ≈ 118)*


<a id="phase-4"></a>
## Phase 4: Streaming & Event-Driven Integration (months 22–27, 119 h)

*Phase 4 of 8 · months 22–27 · 119 h · capstone: Real-time price/flow CDC streaming.*  ← [Phase 3](#phase-3) · [Phase 5](#phase-5) →

**Goal:** close the streaming gap end-to-end: Kafka as the integration backbone, CDC off operational systems, the Beam-model semantics (event time, watermarks, windows), Flink for stateful processing, schema governance on the wire, and the event-driven patterns (outbox, saga, event sourcing) that regulated trade lifecycles are built from.
**Entry prerequisites:** Phases 1–3 (integration-pattern theory from DDIA; lakehouse + orchestrator to land streams into).
**Exit criteria:** you can (1) design a CDC-to-lakehouse flow with stated delivery guarantees and prove them; (2) explain watermarks well enough to debug a wrong window result; (3) own a schema-compatibility policy and show the registry enforcing it; (4) choose among Kafka/Event Hubs/Service Bus/Temporal/Camunda for a given fund workflow and defend it.

### T1/T2 topics

#### 2.4.1 Distributed logs (Kafka) — T1
- **Why:** Kafka is the backbone of modern financial data integration, and as architect you size it, secure it, set its guarantees, and debug it when settlement events go missing. Get partitioning or replication wrong and you silently reorder trade events or lose an entire broker's worth of unflushed orders — the kind of failure auditors trace back to a design decision, not an operator. Knowing the log abstraction cold is what lets you answer capacity, durability, and ordering questions in a design review without hand-waving.
- **Learn:**
    - the log abstraction — topics, partitions, offsets, segments, and retention vs compaction as two different cleanup policies *(Kafka docs: Design)*
    - producer semantics — acks=all, the idempotent producer, and transactions, and what each buys for ordering and duplicates *(Kafka docs: Design — message delivery semantics)*
    - consumer groups — partition assignment, cooperative-sticky rebalancing, and lag as the core health signal *(Kafka docs: Implementation — consumer)*
    - replication internals — ISR, min.insync.replicas, and why unclean leader election trades durability for availability *(Kafka docs: Design — replication)*
    - KRaft mode — the metadata quorum replacing ZooKeeper, and why single-binary clusters are now the norm *(Kafka docs: KRaft)*
    - key design and ordering — ordering is per-partition only, so the partition key is a data-model decision (ISIN here) *(Kafka: Definitive Guide ch. 3–4)*
    - compacted topics as tables — a changelog topic keyed by entity becomes a queryable reference table *(Kafka: Definitive Guide ch. 6)*
    - API-compatible alternatives — Redpanda and the Event Hubs Kafka surface, where compatibility ends *(Kafka: Definitive Guide ch. 1)*
- **Resources:**
    - **[Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/)** ch. 1–7 + 10 (cross-cluster) — the practitioner narrative on producers, consumers, replication, and ops (primary)
    - [Apache Kafka documentation](https://kafka.apache.org/documentation/) — Design, Implementation, and KRaft sections; the authoritative semantics you cite in reviews (reference)
- **Tools:**
    - FOSS (hands-on): [Apache Kafka](https://kafka.apache.org/documentation/) — single-broker KRaft cluster in compose is the whole lab (↔ Confluent Cloud / Event Hubs / MSK)
    - FOSS (hands-on): [Redpanda](https://docs.redpanda.com/) — drop-in Kafka-API broker, lighter to run locally (↔ Confluent Cloud)
    - Corp (evaluate): [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/) — Kafka-compat surface, throughput units, partition limits at build-vs-buy level
- **Do:**
    1. Stand up a single-broker KRaft Kafka (no ZooKeeper) in compose and create a `fund-orders` topic with 3 partitions.
    2. Produce order events keyed by ISIN and prove ordering holds per key but not across partitions.
    3. Run two consumers in one group; trigger a cooperative rebalance and observe which partitions move and how lag behaves.
    4. Create a compacted `fund-reference` topic, write several updates per ISIN, and show only the latest survives compaction — a table served from a log.
- **Done when:**
    - [ ] You can answer "can we lose or duplicate an order event?" for a given producer/consumer config matrix, correctly, every time.
    - [ ] You can state the ordering guarantee for a given key and partition count and justify the partition key choice.
    - [ ] You can explain what min.insync.replicas plus acks=all costs and protects against.
- Est. hours: 14

#### 1.8.2 Delivery semantics (at-most/at-least/exactly-once) — T1
- **Why:** "exactly-once" claims must be audited, not believed, when the payload is a settlement instruction or a NAV correction. As architect you sign off on guarantee diagrams, and a single mislabelled edge — claiming exactly-once where it is really at-least-once into a non-idempotent sink — becomes a duplicated settlement that compliance discovers downstream. The skill is reading any pipeline and marking precisely where the guarantee holds, degrades, and is restored.
- **Learn:**
    - the three guarantees and their cost — at-most-once (may lose), at-least-once (may duplicate), exactly-once (expensive) *(Kafka docs: Design — message delivery semantics)*
    - where duplication enters — producer retries and consumer reprocess after a crash before commit *(Kafka: Definitive Guide ch. 8)*
    - Kafka EOS mechanics — idempotent producer + transactions + read_committed consumers, and that it is within-Kafka only *(Kafka: Definitive Guide ch. 8)*
    - end-to-end exactly-once — at-least-once delivery plus an idempotent or transactional sink, framed as effectively-once *(Streaming Systems ch. 5)*
    - the two-phase-commit sink — how Flink coordinates a transactional sink with checkpoints *(Flink docs: Stateful Stream Processing)*
- **Resources:**
    - **[Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/)** ch. 8 "Exactly-Once Semantics" — the canonical walk-through of idempotent producer and transactions (primary)
    - [Apache Kafka documentation: message delivery semantics](https://kafka.apache.org/documentation/#semantics) — the authoritative definition of each guarantee (reference)
    - [Streaming Systems](https://www.streamingsystems.net/) ch. 5 — effectively-once across the whole pipeline, not just the broker (deepening)
- **Do:**
    1. Build a small consumer that writes each order to a downstream store, in three configurations: auto-commit, manual commit-after-process, and Kafka transactional EOS.
    2. Kill the consumer mid-batch in each configuration and restart it.
    3. Tabulate observed duplicates and losses against your prediction for each configuration.
    4. Mark on a diagram exactly where the guarantee degrades when the downstream store is not idempotent.
- **Done when:**
    - [ ] You can mark, on any pipeline diagram, every point where the guarantee degrades and what restores it.
    - [ ] You can explain why Kafka EOS is within-Kafka and what an end-to-end claim additionally requires.
    - [ ] Your duplicate/loss tabulation matches your prior prediction for all three configs.
- Est. hours: 4

#### 2.3.1 + 1.8.10 Log-based CDC (Debezium) — T1
- **Why:** CDC is how regulated estates go event-driven without touching fragile core systems — it is the highest-leverage integration pattern in the fund back office, turning a transfer-agency database into an event stream nobody had to re-engineer. Get the snapshot, ordering, or restart story wrong and the lakehouse copy silently diverges from the source of record, which is exactly the discrepancy an auditor will surface. The architect must be able to prove completeness and ordering of the whole chain, including after a connector crash.
- **Learn:**
    - logical decoding — how Postgres WAL becomes a stream of row-level change events *(Debezium docs: Postgres connector)*
    - Debezium on Kafka Connect — connectors, tasks, and offset storage as the runtime *(Debezium docs: Architecture)*
    - snapshot modes — initial vs incremental snapshots and when a re-snapshot is forced *(Debezium docs: Postgres connector)*
    - the change envelope — before/after/op/ts_ms fields and tombstones for deletes *(Debezium docs: Architecture)*
    - schema-change events and ordering — per-table ordering and transaction boundaries downstream *(Debezium docs: Postgres connector)*
    - outbox-via-CDC — capturing an application's outbox table as the event source *(Debezium docs: Outbox Event Router)*
    - landing into Iceberg — merge (upsert) vs append-plus-dedupe for the lakehouse copy *(DDIA ch. 11)*
- **Resources:**
    - **[Debezium reference documentation](https://debezium.io/documentation/reference/stable/index.html)** — architecture, the [Postgres connector](https://debezium.io/documentation/reference/stable/connectors/postgresql.html), and the [outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) (primary)
    - [Designing Data-Intensive Applications](https://dataintensive.net/) ch. 11 "Stream Processing" — "keeping systems in sync" reread with practitioner eyes (deepening)
- **Tools:**
    - FOSS (hands-on): [Debezium](https://debezium.io/documentation/reference/stable/index.html) + [Kafka Connect](https://kafka.apache.org/documentation/#connect) — the CDC capture and transport layer (↔ Qlik Replicate / GoldenGate / ADF CDC / Fivetran HVR)
    - Corp (evaluate): [Qlik Replicate](https://www.qlik.com/us/products/qlik-replicate) — an EU-bank incumbent; what to know at build-vs-buy level
    - Corp (evaluate): [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/) — the other incumbent for heterogeneous CDC
- **Do:**
    1. Configure Debezium to capture the Phase-1 Postgres `orders` and `nav` tables into Kafka topics.
    2. Build a merge job that lands those change streams into Iceberg tables on MinIO (upsert on primary key, apply tombstones as deletes).
    3. Mid-stream, restart the Debezium connector and let it resume from its stored offset.
    4. Run a full row-by-row comparison and prove the Iceberg end-state equals the Postgres source after the restart.
- **Done when:**
    - [ ] You can explain to an auditor why the lakehouse copy is complete and ordered, including the restart story.
    - [ ] You can describe what triggers a re-snapshot and how it interacts with already-streamed changes.
    - [ ] Your post-restart comparison shows zero divergence between source and lakehouse.
- Est. hours: 9

#### 2.2.2 Stream connectors (Kafka Connect) — T2
- **Why:** Connect is the operational workhorse around Kafka — connectors, converters, and transforms are where streaming integrations actually live or die, and most CDC and sink plumbing in a fund estate runs on it. Misconfigure a converter or skip the DLQ and a single malformed market-data message stalls an entire connector at 2am. The architect must size Connect clusters and design their failure handling, not just wire up a connector once.
- **Learn:**
    - workers, tasks, and distributed mode — how Connect parallelises and rebalances work *(Kafka docs: Connect)*
    - source vs sink connectors — direction of flow and where offsets are tracked *(Kafka docs: Connect)*
    - converters vs SMTs — serialization (Avro/JSON/Protobuf) versus single-message transforms *(Kafka docs: Connect)*
    - offset management — how Connect stores progress and what an offset reset means *(Kafka docs: Connect)*
    - error handling and DLQ — tolerance settings and dead-letter topics with diagnostic headers *(Kafka: Definitive Guide ch. 9)*
    - connector operations — pause/resume/restart and what each does to in-flight tasks *(Kafka: Definitive Guide ch. 9)*
- **Resources:**
    - **[Apache Kafka documentation: Kafka Connect](https://kafka.apache.org/documentation/#connect)** — concepts, worker config, converters, and transforms (primary)
    - [Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/) ch. 9 — Connect in practice, error handling and DLQ patterns (reference)
- **Tools:**
    - FOSS (hands-on): [Kafka Connect](https://kafka.apache.org/documentation/#connect) — distributed-mode workers running a MinIO sink (↔ Confluent managed connectors, Event Hubs Capture)
    - FOSS (hands-on): [MinIO](https://min.io/docs/minio/linux/index.html) — S3-compatible object store as the sink target (↔ Azure Blob / ADLS)
- **Do:**
    1. Run Connect in distributed mode and configure an S3/MinIO sink connector with a dead-letter topic enabled.
    2. Send a poison message (wrong schema) through the source topic.
    3. Show the bad record parked in the DLQ with headers explaining why it failed.
    4. Size the cluster: estimate workers and tasks for a stated connector load and write down the failure-recovery behaviour.
- **Done when:**
    - [ ] You can size a Connect cluster (workers/tasks) for a given connector load and explain failure recovery.
    - [ ] You can show a poisoned message parked in the DLQ with diagnostic headers.
    - [ ] You can explain what pause/resume/restart each do to running tasks and offsets.
- Est. hours: 4

#### 8.3.1 + 8.3.2 + 1.11.2 Schema registry, schema languages & serialization — T2
- **Why:** the registry is the contract-enforcement point of the streaming estate, and Avro vs Protobuf vs JSON Schema is a recurring standards decision the architect owns. Without a registry, a producer renaming a field silently breaks every downstream consumer and corrupts the NAV pipeline before anyone notices. Knowing the wire format and evolution rules is what lets you make the registry a hard gate rather than a suggestion.
- **Learn:**
    - the registry model — subjects, versions, and per-subject compatibility levels *(Confluent Schema Registry docs)*
    - Avro fundamentals — schemas, logical types (decimal/date), and field-level evolution rules *(Avro spec: Schema Resolution)*
    - Protobuf trade-offs — field numbers, unknown-field preservation, and forward-compat behaviour *(Confluent Schema Registry docs)*
    - JSON Schema's weaker story — why its evolution semantics are looser and riskier *(Confluent Schema Registry docs)*
    - the wire format — magic byte plus schema ID prefixing every payload *(Confluent Schema Registry docs)*
    - subject naming strategies — TopicName vs RecordName vs TopicRecordName and their blast radius *(Confluent Schema Registry docs)*
    - FOSS vs licensed registries — Apicurio vs Confluent SR licensing at build-vs-buy level *(Confluent Schema Registry docs)*
- **Resources:**
    - **[Confluent Schema Registry documentation](https://docs.confluent.io/platform/current/schema-registry/index.html)** — fundamentals, subjects/versions, wire format, and naming strategies (primary)
    - [Apache Avro specification](https://avro.apache.org/docs/1.12.0/specification/) — the Schema Resolution section is the authoritative evolution-rules reference (reference)
- **Tools:**
    - FOSS (hands-on): [Apicurio Registry](https://www.apicur.io/registry/docs/) — open-source registry with Confluent-compatible API (↔ Confluent Cloud SR / Azure Schema Registry / Glue SR)
    - Corp (evaluate): [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html) — Community vs licensed editions and what the managed cloud adds
- **Do:**
    1. Register the fund-order schema in Avro against a subject with `BACKWARD` compatibility.
    2. Attempt three evolutions: add an optional field, rename a field, and change a field's type.
    3. Repeat under `FULL` compatibility and record which evolutions the registry accepts or rejects and the exact error.
    4. Inspect a serialized message and identify the magic byte and schema ID in the wire format.
- **Done when:**
    - [ ] You can write the org's schema-evolution policy and justify each compatibility level per topic class.
    - [ ] You can predict, before submitting, which of the three evolutions the registry will reject under each mode.
    - [ ] You can point to the schema ID inside a raw serialized record.
- Est. hours: 6

#### 1.9.7 Schema evolution compatibility (the policy) — T1
- **Why:** forward/backward compatibility is a governance decision with org-wide blast radius — the architect writes this policy and arbitrates exceptions across Kafka topics, Iceberg tables, and API payloads. Without one mental model, teams upgrade producers and consumers in the wrong order and break the EMT feed or a transfer-agency integration in production. The payoff is being able to rule allow/deny/migrate on any proposed field change in under a minute, with the rule cited.
- **Learn:**
    - the four semantics precisely — backward, forward, full, and the transitive variants across all versions *(Confluent docs: Schema Evolution & Compatibility)*
    - upgrade order — who upgrades first (consumers vs producers) under each compatibility mode *(Confluent docs: Schema Evolution & Compatibility)*
    - default-value discipline — why defaults are what make adding/removing fields safe *(Avro spec: Schema Resolution)*
    - the breaking-change playbook — new subject vs dual-write vs upcaster when a change is genuinely incompatible *(Confluent docs: Schema Evolution & Compatibility)*
    - one model across surfaces — the same rules govern Iceberg table evolution and REST payloads, not just Kafka *(Iceberg docs: Evolution)*
- **Resources:**
    - **[Confluent docs: Schema Evolution & Compatibility Types](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html)** — backward/forward/full/transitive defined precisely, with upgrade-order rules (primary)
    - [Apache Iceberg documentation: Evolution](https://iceberg.apache.org/docs/latest/evolution/) — schema and partition evolution as the table-side of the same policy (reference)
    - [Apache Avro specification](https://avro.apache.org/docs/1.12.0/specification/) — Schema Resolution rules that underpin default-value discipline (reference)
- **Do:**
    1. Write a one-page "Schema Evolution Policy" covering Kafka topics, Iceberg tables, and REST payloads.
    2. State the chosen compatibility level per topic class (reference data vs transactional events) and justify each.
    3. Define the exception process and a breaking-change playbook (new subject / dual-write / upcaster).
    4. Test the policy against five proposed field changes and record the allow/deny/migrate ruling with the rule cited for each.
- **Done when:**
    - [ ] Given any proposed field change, you can rule allow/deny/migrate in under a minute, with the rule cited.
    - [ ] Your policy explicitly covers Kafka, Iceberg, and REST under one model.
    - [ ] You can state the safe upgrade order (producer-first vs consumer-first) for each compatibility level.
- Est. hours: 4

#### 1.9.1 + 1.9.2 + 1.9.4 (with 1.9.3, 1.9.5, 1.9.6) Streaming semantics — the Beam model — T1
- **Why:** event time, watermarks, and windows are the conceptual machinery that make streaming results *correct*, not just fast — and restatement-heavy finance demands event-time rigor. A late trade that arrives after a window closes will quietly understate an intraday fund-flow total unless you have chosen the watermark, lateness, and trigger knobs deliberately. The architect must be able to explain why a count was wrong yesterday and which exact knob fixes it, and what that fix costs in latency.
- **Learn:**
    - event time vs processing time — the central distinction and why event time is the regulated-finance default *(Streaming Systems ch. 1)*
    - the what/where/when/how framing — transformations, windowing, triggers, accumulation as four questions *(Streaming Systems ch. 2)*
    - windowing types — tumbling, sliding, and session windows and when each fits a fund metric *(Streaming Systems ch. 1)*
    - watermarks — perfect vs heuristic, how they propagate, and the latency-vs-completeness tradeoff *(Streaming Systems ch. 3)*
    - triggers and accumulation — early/on-time/late firings and discarding vs accumulating vs retracting *(Streaming Systems ch. 2)*
    - late data handling — allowed lateness, side outputs, and restatements for corrected results *(Streaming Systems ch. 2)*
    - stateful processing preview — keyed state and checkpoints, deepened in the Flink entry below *(Streaming Systems ch. 7)*
- **Resources:**
    - **[Streaming Systems (Akidau, Chernyak, Lax)](https://www.streamingsystems.net/)** — ch. 1–4 plus ch. 7 (state, skim); the canonical, engine-agnostic treatment of the Beam model (primary)
    - [Apache Flink documentation: event-time and watermarks](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) — the same concepts in the engine you will implement them in (reference)
- **Do:**
    1. On paper, draw Beam-model diagrams (event-time axis, watermark line, window bounds) for "intraday fund-flow totals per share class, restated as late orders arrive".
    2. Choose the windowing type, watermark strategy, trigger, and accumulation mode and write one sentence justifying each.
    3. Annotate where a late order lands relative to the watermark and what the trigger does with it.
    4. State the latency cost of your allowed-lateness choice — what you give up to catch stragglers.
- **Done when:**
    - [ ] You can explain to a junior why a count was wrong yesterday and exactly which knob (watermark, lateness, trigger) fixes it — and what that costs.
    - [ ] You can distinguish event time from processing time with a fund example for each.
    - [ ] Your paper design names a concrete windowing/watermark/trigger/accumulation choice ready to implement in Flink.
- Est. hours: 10

#### 4.2.1 Stateful stream processing (Flink) — T1
- **Why:** Flink is the reference stateful engine (and what AWS/Azure managed streaming runs underneath), and real-time NAV estimates and exposure monitoring are Flink-shaped problems. Get checkpointing or state evolution wrong and a job restart produces different numbers than before the crash — unacceptable when those numbers feed a regulated NAV. The architect must be able to narrate the checkpoint-barrier mechanism from memory and reason about state backends, exactly-once sinks, and upgrades.
- **Learn:**
    - the dataflow graph — keyed streams, operators, and parallelism *(Flink docs: Stateful Stream Processing)*
    - state backends — heap vs RocksDB and the size/latency tradeoff *(Flink docs: Stateful Stream Processing)*
    - checkpointing and EOS internals — aligned vs unaligned barriers and how they enable exactly-once *(Flink docs: Stateful Stream Processing)*
    - event-time operators — window and process functions, timers, and watermark strategies in code *(Flink docs: Learn Flink)*
    - Flink SQL and Table API — the declarative path for windowed aggregations *(Flink docs: Learn Flink)*
    - savepoints and upgrades — state evolution and how to redeploy a job without losing state *(Flink docs: Stateful Stream Processing)*
    - Kafka source/sink with EOS — the two-phase-commit sink wiring *(Flink docs: Stateful Stream Processing)*
    - Spark Structured Streaming compared — the micro-batch model and when it is enough *(Spark Structured Streaming guide)*
- **Resources:**
    - **[Apache Flink documentation: Stateful Stream Processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/)** — checkpoints, barriers, state backends, exactly-once internals (primary)
    - [Apache Flink: Learn Flink track](https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/overview/) — guided hands-on for operators, timers, and watermarks (reference)
    - [Spark Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) — the micro-batch alternative for the comparison (alternate)
- **Tools:**
    - FOSS (hands-on): [Apache Flink](https://nightlies.apache.org/flink/flink-docs-stable/) — the stateful engine for the windowed flow-total job (↔ Managed Flink / HDInsight Flink / Confluent Flink / Dataflow)
    - Corp (evaluate): [Azure Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/) — the Azure-native managed streaming option, at build-vs-buy level
- **Do:**
    1. Implement the 1.9 design: a Flink job consuming order events and computing per-share-class windowed flow totals with heuristic watermarks.
    2. Add allowed lateness plus a side output for stragglers; checkpoint state to MinIO.
    3. Write the results exactly-once into Iceberg via the transactional (two-phase-commit) sink.
    4. Kill the job and restore from checkpoint; separately, take a savepoint and perform one upgrade redeploy.
    5. Verify the restored job produces byte-identical results to the pre-crash run.
- **Done when:**
    - [ ] The restored job produces byte-identical results, and you can narrate the checkpoint barrier mechanism from memory.
    - [ ] You can explain aligned vs unaligned checkpoints and when each matters.
    - [ ] You can perform a savepoint-based upgrade without losing state.
- Est. hours: 14

#### 1.8.3 + 1.8.4 Outbox & saga (implemented) — T1
- **Why:** dual-write is the classic event-driven corruption bug and sagas are the bedrock of multi-service trade lifecycles — these two patterns turn theory into production-shaped reflexes. Without the outbox, a service that updates its database and then publishes an event can crash between the two and leave the order booked but never announced. Without a disciplined saga and compensation design, a half-completed subscription leaves cash reserved against units never issued — a reconciliation nightmare the architect must design out.
- **Learn:**
    - the outbox pattern — capture the event in the same transaction as the state change, relay separately *(microservices.io: Transactional Outbox)*
    - the Debezium outbox router — turning the outbox table into clean event topics *(Debezium docs: Outbox Event Router)*
    - idempotent consumers — deduplicating on event ID so replays are safe *(microservices.io: Transactional Outbox)*
    - choreography vs orchestration — distributed vs centrally-directed sagas and their trade-offs *(microservices.io: Saga)*
    - compensation design — semantic undo steps and the dirty-compensation anomaly *(microservices.io: Saga)*
    - timeouts and dead-man handling — what happens when a saga step never replies *(Azure patterns: Saga)*
    - where orchestrators fit — Temporal/Camunda as saga engines (previewing later entries) *(Azure patterns: Saga)*
- **Resources:**
    - **[microservices.io: Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html)** and [Saga](https://microservices.io/patterns/data/saga.html) — the canonical pattern pages with problem, solution, and trade-offs (primary)
    - [Azure Architecture Center: Saga pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) — the cloud-pattern framing and Azure service mapping (reference)
    - [Debezium documentation: Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — the concrete SMT you will wire up (reference)
- **Tools:**
    - FOSS (hands-on): [Debezium Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — relays the outbox table into Kafka topics (↔ application-level outbox relays)
    - FOSS (hands-on): [Apache Kafka](https://kafka.apache.org/documentation/) — the event backbone the saga coordinates over (↔ Event Hubs / Service Bus)
- **Do:**
    1. Add an outbox table to the Phase-1 order service and write events into it inside the same transaction as the order.
    2. Configure Debezium's outbox SMT to route those rows into event topics.
    3. Build a 3-step subscription saga: reserve cash → book units → confirm.
    4. Force a step-2 failure and implement compensation that releases the reserved cash cleanly.
    5. Verify the audit log alone explains the whole failure-and-compensation sequence.
- **Done when:**
    - [ ] The saga's failure path leaves the system consistent and the audit log tells the whole story without manual digging.
    - [ ] You can explain why the outbox eliminates the dual-write race.
    - [ ] Your consumers are idempotent and survive a replayed event without double-effect.
- Est. hours: 7

#### 1.8.5 + 1.8.6 Event sourcing & CQRS — T1/T2
- **Why:** audit-by-construction (1.8.5, T1) is the killer feature for regulated finance — the event log *is* the regulator's evidence, and "what was investor X's position as known on date D?" becomes a replay, not a forensic reconstruction. CQRS (1.8.6, T2) is its usual companion and its main over-application hazard: split read/write models everywhere and you inflict eventual consistency on teams that needed none. The architect must know exactly where event sourcing earns its complexity in a transfer-agency system and where it must not be used.
- **Learn:**
    - state as a fold over events — current state is derived, the event log is the source of truth *(Fowler: Event Sourcing)*
    - commands vs events — intent (may be rejected) vs fact (already happened) *(Designing Event-Driven Systems)*
    - snapshots — materialising state periodically so replay does not start from zero *(Fowler: Event Sourcing)*
    - replay and temporal queries — "position as-known-at date D" from the log *(Fowler: Event Sourcing)*
    - event schema evolution — upcasting old events to new shapes during replay *(Designing Event-Driven Systems)*
    - when ES is wrong — CRUD apps and weak-invariant domains where it adds only cost *(Designing Event-Driven Systems)*
    - CQRS read models — building query-optimised views off the event log, with eventual consistency *(Designing Event-Driven Systems)*
- **Resources:**
    - **[Designing Event-Driven Systems (Ben Stopford, free via Confluent)](https://www.confluent.io/designing-event-driven-systems/)** — the chapters on event sourcing, CQRS, and Kafka-as-event-store (primary)
    - [Martin Fowler: Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) — the foundational essay on fold-over-events, snapshots, and replay (reference)
    - [Azure Architecture Center: Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing) — the cloud-pattern framing and CQRS pairing (reference)
- **Do:**
    1. Event-source the share-register: model order, allocation, and transfer events and fold them to current positions.
    2. Answer "investor X's position as known on date D" purely by replaying events up to D.
    3. Add a snapshot so replay does not always start from the first event.
    4. Write a half-page ADR stating where event sourcing applies in a TA system and where it must not.
- **Done when:**
    - [ ] You can defend the as-known-at vs as-of distinction (bitemporality) with a fund example, and say no to ES somewhere.
    - [ ] You can reconstruct a historical position from the event log alone.
    - [ ] Your ADR names a concrete case where ES would be the wrong choice and why.
- Est. hours: 5

#### 1.8.7 + 1.8.8 Dead-letter queues & backpressure — T2
- **Why:** these two decide whether a bad message or a slow consumer takes down the flow or just a metric. Without a DLQ, one malformed settlement message poison-pills the CDC pipeline and stops every downstream consumer; without backpressure handling, a slow Iceberg sink quietly blows out memory until the job dies. The architect designs the runbook so that a 2am poison pill pages no one and is replayable at 9am with no data loss.
- **Learn:**
    - DLQ design — parking failed messages with diagnostic headers and a defined replay procedure *(Kafka: Definitive Guide ch. 9)*
    - poison-pill detection — distinguishing a one-off bad record from a systemic failure *(Kafka: Definitive Guide ch. 9)*
    - backpressure mechanics — bounded buffers and consumer lag as the early-warning signal *(Flink docs: Stateful Stream Processing)*
    - Flink credit-based flow control — how backpressure propagates upstream without dropping data *(Flink docs: Stateful Stream Processing)*
    - alerting — lag and DLQ-depth thresholds that page the right person at the right time *(Kafka: Definitive Guide ch. 9)*
- **Resources:**
    - **[Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/)** ch. 9 — Connect error handling, DLQ topics, and replay (primary)
    - [Apache Flink documentation: Stateful Stream Processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/) — backpressure and credit-based flow control (reference)
- **Do:**
    1. Define the DLQ-plus-replay runbook for the CDC pipeline: who triages, the replay command, and the idempotency requirement that makes replay safe.
    2. Specify the diagnostic headers a parked message must carry to be triageable cold.
    3. Set lag and DLQ-depth alert thresholds and state who they page.
    4. Dry-run the runbook: park a poison message, then follow your own steps to replay it without loss.
- **Done when:**
    - [ ] A poisoned message at 2am pages no one and is replayable at 9am without data loss.
    - [ ] Your runbook names the triage owner, the replay procedure, and the idempotency precondition.
    - [ ] You can point to backpressure in a running Flink job and explain why it is not dropping data.
- Est. hours: 2.5

#### 2.4.2 Message brokers vs logs — T2
- **Why:** queue semantics (RabbitMQ/Service Bus) and log semantics (Kafka) solve different problems, and picking wrong is expensive in both directions. Use Kafka for request/reply and you fight its consumer-group model; use RabbitMQ for a replayable integration backbone and you lose the replay that auditors and reprocessing depend on. The architect must place each fund-platform messaging need on the right side of this line and defend it.
- **Learn:**
    - competing consumers vs consumer groups — per-message distribution vs partition-bound consumption *(RabbitMQ docs: AMQP Concepts)*
    - ack/redelivery vs offsets — per-message acknowledgment vs replayable offset tracking *(RabbitMQ docs: AMQP Concepts)*
    - routing vs partitioning — exchanges and bindings vs partition keys *(RabbitMQ docs: AMQP Concepts)*
    - when a queue wins — task distribution, request/reply, per-message TTL *(Kafka: Definitive Guide ch. 1)*
    - when a log wins — replay, fan-out, ordering, and long retention *(Kafka: Definitive Guide ch. 1)*
    - AMQP basics and the corp queue — Azure Service Bus as the enterprise queue *(RabbitMQ docs: AMQP Concepts)*
- **Resources:**
    - **[RabbitMQ documentation: AMQP 0-9-1 Concepts](https://www.rabbitmq.com/tutorials/amqp-concepts)** — exchanges, queues, bindings, acks, competing consumers (primary)
    - [Kafka: The Definitive Guide, 2nd ed. (free via Confluent)](https://www.confluent.io/resources/kafka-the-definitive-guide-v2/) ch. 1 — the log model framed against queues (reference)
- **Tools:**
    - FOSS (hands-on): [RabbitMQ](https://www.rabbitmq.com/docs) — short hands-on with exchanges and queues (↔ Azure Service Bus / AWS SQS)
    - Corp (evaluate): [Azure Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/) — the corp-native queue: sessions, dead-lettering, TTL
- 🐘 **Postgres-native alternative — [pgmq](https://github.com/pgmq/pgmq) (SQS-style queues) + `LISTEN`/`NOTIFY` (lightweight pub/sub):** *Better when* you already run Postgres, volumes are low-to-moderate, and you want transactional enqueue — the message and the business row commit in one transaction — with a single system to operate, secure and back up. *Worse when* you need high-throughput fan-out, topic routing/exchanges, very long retention with replay, or a broker protocol ecosystem: reach for RabbitMQ (routing) or Kafka (replayable log).
- **Do:**
    1. Stand up RabbitMQ and run a small competing-consumers task-distribution example.
    2. Contrast it with a Kafka consumer-group example over the same workload.
    3. Build a decision table: 6 fund-platform messaging needs → queue or log, one line of why each.
    4. Identify which of the 6 would be actively harmed by the wrong choice and how.
- **Done when:**
    - [ ] You never propose Kafka for request/reply or RabbitMQ for replayable integration again.
    - [ ] Your decision table covers 6 concrete fund needs with a one-line rationale each.
    - [ ] You can explain ack/redelivery vs offset replay and which an audit-reprocessing use case needs.
- Est. hours: 3

#### 5.6.4 Durable execution (Temporal) — T2
- **Why:** trade lifecycle, KYC, and corporate-actions workflows are long-running, stateful, and retry-heavy — durable execution is the modern saga orchestrator and FS adoption is real. Hand-rolled retry-and-timeout logic across services is where these workflows rot; a worker crash mid-corporate-action leaves the process in an unknown state. Temporal makes the workflow itself durable, and the architect must know when that beats a BPM engine or a plain queue.
- **Learn:**
    - workflow-as-code — deterministic workflow functions plus side-effecting activities *(Temporal docs: Understanding Temporal)*
    - event-history replay — how Temporal reconstructs workflow state after a crash *(Temporal docs: Understanding Temporal)*
    - retries, timeouts, heartbeats — built-in reliability primitives for activities *(Temporal docs: Understanding Temporal)*
    - signals and queries — sending input to and reading state from a running workflow *(Temporal docs: Understanding Temporal)*
    - versioning running workflows — changing code without breaking in-flight executions *(Temporal docs: Understanding Temporal)*
    - placement — Temporal vs BPM vs queue, and Azure Durable Functions as the corp analogue *(Temporal docs: Understanding Temporal)*
- **Resources:**
    - **[Temporal documentation: Understanding Temporal](https://docs.temporal.io/evaluate/understanding-temporal)** — core concepts: workflows, activities, event history, retries (primary)
    - [Temporal documentation root](https://docs.temporal.io/) — the Python SDK tutorial path for the hands-on build (reference)
- **Tools:**
    - FOSS (hands-on): [Temporal](https://docs.temporal.io/) — OSS server in compose running the durable saga (↔ Temporal Cloud / Durable Functions / Step Functions)
    - FOSS (Postgres-native): [DBOS](https://docs.dbos.dev/) — durable execution as a library with workflow/queue state in Postgres (↔ Hatchet, pgflow)
    - Corp (evaluate): [Azure Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/) — the Azure-native durable-execution analogue
- 🐘 **Postgres-native alternative — [DBOS](https://docs.dbos.dev/) (also Hatchet, pgflow):** *Better when* you already run Postgres and want durable workflows without operating a Temporal cluster — workflow and queue state live in your DB, commit transactionally with your business data, far lighter ops and lower latency. *Worse when* you need Temporal's maturity at scale: massive parallel fan-out, very long-lived workflows, rich signals/queries and visibility tooling, or multi-language/multi-region — there a single Postgres becomes the bottleneck and Temporal's ecosystem wins.
- **Do:**
    1. Run Temporal OSS in compose with a worker.
    2. Reimplement the Phase-4 subscription saga as a Temporal workflow with activities for each step.
    3. Add retries and a compensation path for the step-2 failure.
    4. Kill the worker mid-run and watch the workflow resume from event history on restart.
- **Done when:**
    - [ ] You can explain event-history replay and why workflow code must be deterministic.
    - [ ] Your workflow resumes correctly after a mid-run worker kill.
    - [ ] You can state when Temporal beats a BPM engine and when it does not.
- Est. hours: 4

#### 5.6.5 BPM / process orchestration (Camunda, BPMN/DMN) — T2
- **Why:** banks and fund administrators run BPMN engines for settlement, onboarding, and exception handling, so the architect must speak BPMN/DMN and know when model-driven beats code-driven orchestration. A compliance officer can read and sign off a BPMN diagram in a way they never could read Temporal code — that auditability is exactly why these engines persist in regulated shops. The decision the architect owns is BPM vs durable execution vs scheduler, per workflow, with reasons.
- **Learn:**
    - BPMN 2.0 working subset — tasks, gateways, and events (timer/message/error) *(Camunda 8 docs)*
    - pools and lanes — modelling responsibility boundaries across teams/systems *(Camunda 8 docs)*
    - DMN decision tables and FEEL — externalising business rules from process flow *(Camunda 8 docs)*
    - Camunda 7 vs 8/Zeebe — the architecture and licensing shift *(Camunda 8 docs)*
    - human-task workflows — exception queues and manual review steps *(Camunda 8 docs)*
    - the orchestration trichotomy — BPM vs Temporal vs Airflow under one decision framework *(Camunda 8 docs)*
- **Resources:**
    - **[Camunda 8 documentation](https://docs.camunda.io/)** — BPMN and DMN references, Zeebe architecture, human tasks (primary)
    - [bpmn.io](https://bpmn.io/) — the open-source modelling toolkit and tutorials for drawing the diagrams (reference)
- **Tools:**
    - FOSS (hands-on): [Camunda 8 / Zeebe](https://docs.camunda.io/) — runs the BPMN process and DMN table (↔ Camunda Enterprise / Pega / IBM BPM)
    - FOSS (hands-on): [bpmn.io](https://bpmn.io/) — browser-based BPMN/DMN modeller for authoring the diagrams
- **Do:**
    1. Model the subscription-order lifecycle in BPMN with a normal path and an error-handling path to a human task.
    2. Encode the "compliance review required?" rule as a DMN decision table with FEEL expressions.
    3. Deploy and run both in Camunda, triggering the error path at least once.
    4. Write a short comparison of this BPMN solution against the Temporal version of the same saga.
- **Done when:**
    - [ ] You can defend orchestration-tool choice (BPM vs durable execution vs scheduler) for three different fund workflows.
    - [ ] Your BPMN process routes a failure to a human task and resumes correctly.
    - [ ] Your DMN table produces the right review decision for several test inputs.
- Est. hours: 5

#### 1.11.1 + 1.11.3 Data protocols & async API standards — T2
- **Why:** protocol literacy (gRPC vs REST vs Arrow Flight; AsyncAPI/CloudEvents) is the architect's interface-design toolkit across the estate — choosing the transfer mechanism for a BI extract, a microservice call, a market-data feed, or a file drop with numbers, not vibes. Default everything to REST/JDBC and you marshal millions of rows one at a time when Arrow Flight would move columnar batches in a fraction of the time. Async standards (AsyncAPI, CloudEvents) are what make an event estate documentable and interoperable rather than tribal knowledge.
- **Learn:**
    - gRPC over HTTP/2 with Protobuf — contract-first, low-overhead service calls *(AsyncAPI docs)*
    - REST maturity in practice — where REST is the pragmatic default and where it is not *(AsyncAPI docs)*
    - Arrow Flight and ADBC — columnar bulk transfer vs row-marshaling JDBC/ODBC *(Arrow Flight docs)*
    - WebSocket/MQTT/AMQP placement — which transport fits push, IoT-style, and queue use cases *(AsyncAPI docs)*
    - AsyncAPI — OpenAPI-for-events: channels, messages, schemas *(AsyncAPI docs)*
    - CloudEvents — a vendor-neutral event envelope for interop *(CloudEvents spec)*
    - legacy literacy — SOAP/OData you will meet in the existing fund estate *(AsyncAPI docs)*
- **Resources:**
    - **[AsyncAPI documentation](https://www.asyncapi.com/docs)** — concepts, channels, messages; the standard you will author against (primary)
    - [Apache Arrow Flight RPC](https://arrow.apache.org/docs/format/Flight.html) — the columnar bulk-transfer protocol for analytical extracts (reference)
    - [CloudEvents specification](https://cloudevents.io/) — the common event-envelope standard (reference)
- **Tools:**
    - FOSS (hands-on): [AsyncAPI](https://www.asyncapi.com/docs) — author and render the event-API document for your topics
    - FOSS (hands-on): [Apache Arrow Flight](https://arrow.apache.org/docs/format/Flight.html) — columnar transport for the BI-extract comparison (↔ JDBC/ODBC)
- **Do:**
    1. Write the AsyncAPI document for your fund-order Kafka topics: channels, messages, and schema references.
    2. Render its HTML docs from the spec.
    3. Map four transfer needs (BI extract, microservice call, market-data feed, file drop) to a protocol each.
    4. Justify each mapping with a concrete factor (payload size, latency, ordering, schema) — numbers where you have them.
- **Done when:**
    - [ ] You can pick the transfer protocol for: BI extract, microservice call, market-data feed, file drop — with numbers, not vibes.
    - [ ] Your AsyncAPI document renders and accurately describes the order topics.
    - [ ] You can explain why Arrow Flight beats JDBC for a large analytical extract.
- Est. hours: 3

#### 1.4.1 + 1.4.2 Lambda vs Kappa — T2
- **Why:** the batch/speed-layer debate frames every "do we need streaming?" conversation, and medallion-with-streaming is today's synthesis. Reach for Lambda and you pay the dual-codebase tax — maintaining the same NAV-flow logic twice in two systems that must agree — when a replayable log usually makes that second codebase unnecessary. The architect must be able to name which architecture the capstone platform actually is and defend it for fund data.
- **Learn:**
    - the Lambda architecture — batch plus speed layers and the dual-codebase maintenance tax *(Kreps: Questioning the Lambda Architecture)*
    - the Kappa answer — replay the log through one stream framework instead of two systems *(Kreps: Questioning the Lambda Architecture)*
    - retention implications — what Kappa demands of log storage and reprocessing *(Kreps: Questioning the Lambda Architecture)*
    - the modern synthesis — table formats plus streaming ingestion dissolving most of the dichotomy *(Streaming Systems ch. 1)*
- **Resources:**
    - **[Jay Kreps: Questioning the Lambda Architecture](https://www.oreilly.com/radar/questioning-the-lambda-architecture/)** — the essay that defined the Kappa alternative (primary)
    - [Streaming Systems (Akidau, Chernyak, Lax)](https://www.streamingsystems.net/) ch. 1 — the streams-and-tables framing behind the synthesis (reference)
- **Do:**
    1. Write a one-page position note stating which architecture (Lambda, Kappa, or the table-format synthesis) your capstone platform actually is.
    2. Justify why that is the right call for fund data specifically.
    3. State what you would change if regulators demanded sub-minute NAV-error detection.
    4. Name the dual-codebase risk in your design and how you avoid or accept it.
- **Done when:**
    - [ ] You can articulate what you'd change if regulators demanded sub-minute NAV-error detection.
    - [ ] Your note names the platform's actual architecture and defends it for fund data.
    - [ ] You can explain the dual-codebase tax with a concrete fund example.
- Est. hours: 2

#### 1.2.2 + 1.2.3 Micro-batch vs true streaming — T2
- **Why:** Spark Structured Streaming (micro-batch) vs Flink (event-at-a-time) is a real engine decision with latency, state, and ops consequences. Pick micro-batch for a sub-second exposure monitor and you cannot meet the latency floor; pick event-at-a-time for a minute-grained reconciliation and you take on operational complexity you did not need. The architect must place any fund use case in the right latency class and name the engine.
- **Learn:**
    - micro-batch mechanics — the trigger interval and the latency floor it imposes *(Spark Structured Streaming guide)*
    - continuous processing — Spark's lower-latency mode and its limitations *(Spark Structured Streaming guide)*
    - state handling differences — how Spark and Flink each manage and checkpoint state *(Flink docs: Stateful Stream Processing)*
    - ops profile — long-lived Spark cluster reuse vs per-job Flink clusters *(Spark Structured Streaming guide)*
    - the latency-class rubric — minutes vs seconds vs sub-second and which engine each implies *(Flink docs: Stateful Stream Processing)*
- **Resources:**
    - **[Spark Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)** — micro-batch model, triggers, and state (primary)
    - [Apache Flink documentation: Stateful Stream Processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/) — the event-at-a-time contrast (reference)
- **Do:**
    1. Rebuild one Flink aggregation in Spark Structured Streaming on the existing Spark cluster.
    2. Measure end-to-end latency for both implementations.
    3. Compare code volume and operational burden in a half-page note.
    4. Place three fund use cases (intraday flow totals, sub-second exposure alert, nightly reconciliation) in a latency class and name the engine for each.
- **Done when:**
    - [ ] You can place any fund use case in the right latency class and name the engine.
    - [ ] Your note compares measured latency, code, and ops burden for both engines.
    - [ ] You can explain why micro-batch has a latency floor that event-at-a-time does not.
- Est. hours: 3

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.2.4 | Real-time / low-latency paradigm | Sub-second serving paths (in-memory, push); mostly out of fund-admin scope but appears in trading-adjacent systems | [*Streaming Systems* ch. 1 sidebar](https://www.streamingsystems.net/) | 15 |
| 1.3.4 | RT / user-facing analytics workload | High-concurrency, sub-second dashboards served to many external users (Pinot/Druid class) | [StarTree: what is user-facing analytics](https://startree.ai/blog/what-is-user-facing-analytics) | 25 |
| 1.8.12 | Bulkhead | Resource isolation so one slow consumer can't sink the whole flow | [Azure patterns catalog: Bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead) | 15 |
| 1.8.13 | Circuit breaker | Fail-fast wrapper that stops hammering a flaky dependency | [Azure patterns catalog: Circuit Breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) | 15 |
| 2.3.2 | Trigger-based CDC | DB triggers populate change tables; an intrusive legacy approach with write overhead | [Debezium FAQ](https://debezium.io/documentation/faq/) | 15 |
| 2.3.3 | Snapshot-based CDC | Periodic diffing (Fivetran-style); simple but lossy between snapshots | [Fivetran docs: sync modes](https://fivetran.com/docs/core-concepts/sync-modes) | 15 |
| 2.4.3 | Event mesh | Federated brokers routing events across sites/clouds (Solace; big in capital markets) | [Solace: what is an event mesh](https://solace.com/resources/event-mesh/what-is-an-event-mesh) | 25 |
| 4.3.4 | RT analytics engines | Pinot/Druid/ClickHouse serving layer for the 1.3.4 user-facing workloads | [Apache Pinot docs: intro](https://docs.pinot.apache.org/) | 25 |
| 4.3.5 | Streaming databases | Incrementally-maintained materialized views over streams (Materialize/RisingWave) | [RisingWave docs: architecture](https://docs.risingwave.com/get-started/architecture) | 25 |

*T3 subtotal: 3 h*

### Capstone 4 — Real-time fund-flow & price CDC streaming

- **Goal:** the platform gains a streaming spine: operational changes flow as events, stateful aggregations stay correct under late data, and every guarantee is stated and demonstrated.
- **Stack (100% free):** [Kafka KRaft](https://kafka.apache.org/documentation/) or [Redpanda](https://docs.redpanda.com/) (↔ Confluent Cloud / Event Hubs), [Kafka Connect](https://kafka.apache.org/documentation/#connect) + [Debezium](https://debezium.io/documentation/reference/stable/index.html) with [outbox router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) (↔ Qlik Replicate / GoldenGate / ADF), [Apicurio](https://www.apicur.io/registry/docs/) or [Confluent SR](https://docs.confluent.io/platform/current/schema-registry/index.html) with [Avro](https://avro.apache.org/docs/1.12.0/specification/) (↔ Confluent Cloud SR / Azure Schema Registry), [Flink](https://nightlies.apache.org/flink/flink-docs-stable/) (↔ Confluent Flink / Managed Flink / ASA), [Iceberg](https://iceberg.apache.org/docs/latest/) sink on [MinIO](https://min.io/docs/minio/linux/index.html), [Temporal](https://docs.temporal.io/) saga + [Camunda](https://docs.camunda.io/) BPMN process from the entries above, [Dagster](https://docs.dagster.io/) supervising batch reconciliation, all in compose.
- **Build:** (1) Debezium streams orders/NAV + the outbox topic; (2) Flink computes per-share-class windowed flow totals (heuristic watermarks, allowed lateness, late-event side output) exactly-once into Iceberg; (3) nightly Dagster batch reconciles streamed totals against batch recompute and alerts on drift; (4) schema registry enforces the 1.9.7 policy (one rejected evolution kept as evidence); (5) the subscription saga (Temporal) and BPMN process (Camunda) run against the same events; (6) chaos drills: kill broker, connector, Flink job — document recovery and guarantee held. Capture the recovery narrative for each drill as you run it, naming the mechanism that restored correctness.
- **Architecture deliverables:** C4 updated with the streaming spine; ADR-010 log platform choice (Kafka vs Event Hubs vs Redpanda), ADR-011 delivery-guarantee design (where exactly-once is real and where idempotent-at-least-once is the honest answer), ADR-012 orchestration species (BPM vs durable execution vs scheduler, per workflow). Each ADR states the decision, the alternatives weighed, and the EU/fund-industry constraint that drove it.
- **Acceptance criteria:** reconciliation drift = 0 over a 3-day simulated run incl. injected late/duplicate events; each chaos drill has a written recovery narrative naming the mechanism (ISR, checkpoint, offset commit); schema policy violation is blocked by the registry and the evidence archived; saga failure path leaves consistent state with full audit trail.
- Est. hours: 16

*Phase 4 total: 119 h (T1/T2 entries 99.5 h + T3 3 h + capstone 16 h ≈ 119)*


<a id="phase-5"></a>
## Phase 5: Cloud Platform Architecture & Operations — Azure (months 28–33, 108 h + 37 h Appendix A)

*Phase 5 of 8 · months 28–33 · 145 h (108 h + 37 h Appendix A) · capstone: IaC platform on Kubernetes + Well-Architected review.*  ← [Phase 4](#phase-4) · [Phase 6](#phase-6) →

**Goal:** turn the laptop platform into a cloud-shaped one: Azure reference architecture (WAF/CAF), infrastructure as code, Kubernetes as the runtime substrate, the Azure data services at evaluation depth, and the operations disciplines (observability, DR, FinOps) that keep a regulated platform alive and affordable.
**Entry prerequisites:** Phases 2–4 (a real multi-service stack worth provisioning); Appendix A items A.3 (networking), A.4 (Fabric), A.5 (KQL), A.6 (Kubernetes), A.22 (relational HA), A.25 (warehouse performance), A.26 (chaos/resilience testing) are scheduled inside this phase.
**Exit criteria:** you can (1) run a Well-Architected review of your own design and find real findings; (2) provision and tear down the platform from code alone; (3) state RTO/RPO for each platform tier and the topology that delivers it; (4) produce a defensible monthly-cost model for the Azure target architecture; (5) operate the stack on Kubernetes locally and explain what AKS changes.

### T1/T2 topics

#### 8.1.1 Azure reference architecture (WAF + CAF landing zones) — T1
- **Why:** the Well-Architected pillars and CAF landing zones are the daily design language on the primary cloud — reviews, RFPs, and audits are all conducted in it. In a Luxembourg fund-administration estate, the architect who can't map a design to landing-zone boundaries and the five WAF pillars can't get a design through an architecture review board or a CSSF-aligned governance gate. Without this, designs leak across subscription/identity boundaries and you lose the data-residency and segregation arguments before you start.
- **Learn:**
    - WAF's five pillars (reliability, security, cost, operational excellence, performance) and the data-workload lens — what each pillar asks of a data platform specifically *(WAF docs: pillars)*
    - CAF landing zones — management groups → subscriptions-as-units → policy-driven governance via Azure Policy *(CAF docs: What is a landing zone)*
    - hub-spoke vs Virtual WAN network topology — why shared services (identity, connectivity) live in a platform landing zone *(CAF docs: landing zone architecture)*
    - identity baseline — Entra ID, managed identities as the no-secret default for service-to-service auth *(Entra docs: managed identities)*
    - region pairs & availability zones — how to keep EU fund data inside a residency boundary while surviving a zone/region loss *(WAF docs: reliability)*
- **Resources:**
    - **[Microsoft Learn: Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)** — the five pillars, the review/assessment tool, and per-service guidance you'll run your design against (primary)
    - [CAF: What is an Azure landing zone?](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) — management-group hierarchy, platform vs application landing zones, hub-spoke reference (reference)
    - [Entra: managed identities overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview) — the identity baseline that makes the landing zone credential-free (deepening)
- **Tools:**
    - Corp (evaluate): [Azure](https://learn.microsoft.com/azure/) — the primary cloud; landing zones and WAF are how its governance is expressed
    - Corp (evaluate): [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) — the comparison vocabulary so you can read multi-cloud RFPs
- **Do:**
    1. Take your Capstone-4 architecture and run a written WAF review as if it ran on Azure: one finding plus a remediation per pillar (five findings minimum).
    2. Sketch a CSSF-friendly landing zone: management groups → subscriptions → VNets → identities, naming the boundary at each level.
    3. For each pillar finding, name the Azure control that closes it (e.g. Azure Policy for governance, Private Link for security, ZRS for reliability).
    4. Write a one-paragraph data-residency note: which region pair you chose and why it keeps fund data in-boundary.
- **Done when:**
    - [ ] You can sketch the landing zone (mgmt groups → subscriptions → networks → identities) on a whiteboard and justify each boundary.
    - [ ] You can name one concrete finding and remediation per WAF pillar for your own design.
    - [ ] You can state the region-pair and zone topology that meets EU residency without single-region risk.
- Est. hours: 14

#### 9.10.1 Infrastructure as code (OpenTofu/Terraform) — T1
- **Why:** a named weak spot, and the medium in which every platform you design will actually ship; "architecture" that isn't in code is a slide. In a regulated estate, IaC is also the audit trail and the reproducibility guarantee — reviewers want to see the exact resources, policies, and network rules as version-controlled code, not portal screenshots. Without it, environments drift, DR rebuilds are guesswork, and there is no four-eyes review on infrastructure change.
- **Learn:**
    - HCL building blocks — providers, resources, data sources, variables/outputs and how they compose *(OpenTofu docs: language)*
    - state mechanics — remote backends, locking, drift detection, `import` for brownfield estates *(OpenTofu docs: state)*
    - modules and composition — reusable units (a VNet module, a storage module) and workspaces vs directory-per-env *(OpenTofu docs: language)*
    - plan/apply discipline and CI integration — why `plan` is the review artifact and `apply` is gated *(Terraform Up & Running: workflow chapters)*
    - secrets handling in IaC — never in state in clear; reference Key Vault/OpenBao instead *(OpenTofu docs: state, sensitive values)*
    - Terraform↔OpenTofu split (BSL vs MPL) — what the licence fork means for vendor selection *(Terraform Up & Running)*
- **Resources:**
    - **[OpenTofu documentation](https://opentofu.org/docs/)** — language, [state](https://opentofu.org/docs/language/state/), CLI; the FOSS engine you build on (primary)
    - [Terraform: Up & Running, 3rd ed.](https://www.terraformupandrunning.com/) — the concept chapters (state, modules, workflow, testing); commands transfer one-to-one to OpenTofu (reference)
- **Tools:**
    - FOSS (hands-on): [OpenTofu](https://opentofu.org/docs/) — the MPL-licensed engine; drives the compose-era stack and a plan-only azurerm module (↔ Terraform Cloud/Enterprise)
    - Corp (evaluate): [Terraform Enterprise / HCP Terraform](https://developer.hashicorp.com/terraform) — what state backend, policy-as-code (Sentinel), and run governance buy at build-vs-buy level
- **Do:**
    1. Put the entire compose-era platform under OpenTofu using the docker, kubernetes, and helm providers so that one `tofu apply` builds the full local stack.
    2. Factor shared infrastructure (network, storage) into reusable modules; configure a remote state backend with locking.
    3. Write an azurerm module for the target architecture and validate it with `tofu plan` against a free-trial subscription — plan-only, no spend.
    4. Run `tofu destroy && tofu apply` and confirm the platform comes back identically; capture the plan output as the review artifact.
- **Done when:**
    - [ ] Reproduce the platform byte-for-byte with `tofu destroy && tofu apply`.
    - [ ] Explain every line of a teammate's plan output, including what a replace vs in-place update means.
    - [ ] Show that no secret value is stored in clear in state.
- Est. hours: 16

#### 9.10.2 Cloud-native IaC (Bicep) — T2
- **Why:** Microsoft shops mandate Bicep/ARM for Azure-only estates; you must hold a reasoned Bicep-vs-Terraform position in vendor-aligned organizations. Many Luxembourg fund-tech teams are Azure-only and will hand you Bicep, so evaluation fluency is the difference between recommending the right tool and being overruled. Without it, you cannot read the incumbent's deployment code or argue the trade-off credibly.
- **Learn:**
    - Bicep syntax and modules — declarative resource authoring that compiles to ARM JSON *(Bicep docs: file structure)*
    - `what-if` deployments and the ARM deployment model (incremental vs complete) — preview-before-apply on Azure *(Bicep docs: what-if)*
    - when Bicep wins (day-0 Azure features, no state file to manage) vs Terraform (multi-cloud, ecosystem, providers) *(Bicep docs: overview)*
    - Azure Verified Modules (AVM) — the curated module library Microsoft ships for landing zones *(Bicep docs: best practices)*
- **Resources:**
    - **[Microsoft Learn: Bicep documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/)** — fundamentals, file structure, `what-if`, AVM; the free path that covers every Learn bullet (primary)
    - [Fundamentals of Bicep (training path)](https://learn.microsoft.com/en-us/training/paths/fundamentals-bicep/) — hands-on guided modules (reference)
- **Tools:**
    - Corp (evaluate): [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) — Azure-native IaC; no state file, day-0 resource coverage (↔ OpenTofu/Terraform)
- **Do:**
    1. Rewrite one OpenTofu module (storage account + key vault + VNet) in Bicep.
    2. Run `az deployment group what-if` and read the predicted change set.
    3. Write a 10-line comparison: where Bicep was simpler, where Terraform's multi-cloud/state model wins.
- **Done when:**
    - [ ] Recommend Bicep or Terraform for a given org and defend it against the other camp.
    - [ ] Produce a working `what-if` output for your rewritten module.
- Est. hours: 4

#### 2.1.2 + 5.6.2 Azure Data Factory (bulk movement + orchestration) — T2
- **Why:** ADF is the incumbent Azure data-movement and orchestration service you will meet in every Luxembourg estate — evaluation fluency is mandatory even if you'd choose Dagster. The architect is constantly asked "why not just use ADF?" by stakeholders who already pay for it, and needs costed, scenario-specific answers. Without this, you either rubber-stamp ADF where it breaks down or reject it without being able to say why.
- **Learn:**
    - pipelines, activities, triggers — ADF's orchestration primitives and their limits vs code-first DAGs *(ADF docs: introduction)*
    - copy activity & integration runtimes, including self-hosted IR for on-prem transfer-agency systems *(ADF docs: introduction, integration runtime)*
    - mapping data flows — Spark under the hood, and when that is the right or wrong engine *(ADF docs: introduction)*
    - ADF vs Synapse pipelines vs Fabric Data Factory — the lineage and which one a given estate is on *(ADF docs: introduction)*
    - pricing model — DIU-hours, activity runs, IR hours, and where the bill surprises you *(Azure Cost Management docs)*
- **Resources:**
    - **[Azure Data Factory: Introduction](https://learn.microsoft.com/en-us/azure/data-factory/introduction)** — pipelines, activities, copy activity, integration runtimes, CI/CD (primary)
    - [Azure Cost Management overview](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) — the mechanics behind DIU-hour and activity-run pricing (reference)
- **Tools:**
    - Corp (evaluate): [Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/introduction) — incumbent bulk movement + orchestration; self-hosted IR for on-prem (↔ FOSS: Airbyte + Dagster from earlier phases)
    - FOSS (hands-on): [Dagster](https://docs.dagster.io/) — the code-first orchestrator you compare ADF against
- **Do:**
    1. On paper plus the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/), design the ADF implementation of your Airbyte+Dagster ingestion: pipeline sketch, IR placement for an on-prem TA system.
    2. Produce a monthly cost estimate (DIU-hours + activity runs + self-hosted IR).
    3. Identify two places where ADF orchestration breaks down vs a code-first orchestrator and note the workaround or the line you'd draw.
- **Done when:**
    - [ ] Argue ADF-vs-code-first for three scenarios (lift-and-shift shop, product team, hybrid estate) with costs.
    - [ ] Place a self-hosted IR correctly for an on-prem source and explain why.
- Est. hours: 6

#### 4.2.2 Cloud-native streaming (Event Hubs, Stream Analytics) — T2
- **Why:** Event Hubs is what "Kafka on Azure" usually means in practice; knowing its limits against real Kafka is a recurring design question. In a fund platform that streams order/trade events, choosing Event Hubs where you needed log compaction or full transactions corrupts the design quietly. The architect must give a feature-by-feature verdict, not a vibe.
- **Learn:**
    - Event Hubs model — namespaces, throughput/processing units, partitions, Capture to ADLS *(Event Hubs docs: about)*
    - Kafka-protocol surface and its gaps — no log compaction, transaction limits vs open-source Kafka *(Event Hubs docs: Kafka compatibility)*
    - Azure Stream Analytics SQL jobs vs Flink — the SQL-temporal model and where it stops *(Stream Analytics docs: introduction)*
    - Service Bus vs Event Hubs vs Event Grid triage — streaming vs enterprise messaging vs reactive routing *(Event Hubs docs: choosing messaging services)*
- **Resources:**
    - **[Azure Event Hubs: What is Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about)** — model, partitions, Capture, Kafka compatibility, messaging-service triage (primary)
    - [Azure Stream Analytics: Introduction](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction) — SQL streaming jobs, exactly-once semantics, vs Flink (reference)
- **Tools:**
    - Corp (evaluate): [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about) — managed Kafka-protocol streaming (↔ FOSS: Apache Kafka/Redpanda)
    - Corp (evaluate): [Azure Stream Analytics](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-introduction) — managed SQL stream processing (↔ FOSS: Apache Flink)
- **Do:**
    1. List every Kafka feature you used in Capstone-4 (compaction, transactions, consumer groups, retention).
    2. Map each to Event Hubs; flag the ones that don't translate and write the concrete workaround.
    3. Pick one transform and note whether Stream Analytics SQL or Flink fits, with the reason.
- **Done when:**
    - [ ] Answer "can we just use Event Hubs?" with a feature-by-feature verdict.
    - [ ] Name at least one Kafka feature that does not translate and its workaround.
- Est. hours: 3

#### 4.1.2 Serverless compute (Azure Functions) — T2
- **Why:** functions are the glue tier of cloud data platforms (event handlers, light transforms, API shims); the architect decides where glue ends and engines begin. Misplacing that line — running heavy data movement or long stateful jobs in Functions — produces cold-start latency, timeouts, and surprise bills in a fund platform that drops EMT/NAV files on a schedule. Without a clear rule, glue silently grows into an unmaintainable shadow pipeline.
- **Learn:**
    - triggers and bindings — the event-to-code wiring (blob trigger on a file drop, output binding to an event) *(Functions docs: overview)*
    - hosting plans — Flex Consumption/Premium/Dedicated and the cold-start trade-off *(Functions docs: hosting options)*
    - Durable Functions — orchestration for multi-step serverless workflows (ties to 5.6.4) *(Functions docs: overview)*
    - when functions become an anti-pattern — long-running, stateful, heavy data movement *(Functions docs: scenarios)*
- **Resources:**
    - **[Azure Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview)** — triggers/bindings, hosting options, Durable Functions, the cost model (primary)
    - [Azure Functions scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios) — the file-upload, stream-processing, and scheduled-task patterns that show where functions fit and where they don't (reference)
- **Tools:**
    - FOSS (hands-on): [Azure Functions Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) — run and debug functions locally for free (↔ the managed Functions service)
    - Corp (evaluate): [Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview) — the hosted serverless tier; know its cost profile at scale
- **Do:**
    1. Locally run (Core Tools, free) an event-triggered function that validates an incoming EMT file drop and emits an event.
    2. Document its Azure cost profile at 10k files/month (executions + GB-seconds + plan).
    3. Write the rule that separates function-glue from pipeline-engine, with one example on each side.
- **Done when:**
    - [ ] Draw the line between function-glue and pipeline-engine for five workloads.
    - [ ] Produce a working local function that validates a file and emits an event.
- Est. hours: 3

#### 4.3.2 Cloud query services — T2
- **Why:** serverless SQL over the lake (Synapse serverless, Athena) is the cheap-and-cheerful tier of lakehouse consumption; knowing its price/perf envelope completes the engine matrix. With per-TB-scanned pricing, a badly partitioned gold layer turns an ad-hoc query into a four-figure bill — the architect who doesn't understand this signs off file layouts that bankrupt the consumption tier. File layout literally is the cost model here.
- **Learn:**
    - per-TB-scanned pricing mechanics — and the partitioning/pruning economics it forces *(Synapse serverless docs: best practices)*
    - OPENROWSET / external tables — querying Parquet/Delta in place without a running warehouse *(Synapse serverless docs: best practices)*
    - Athena/Trino lineage — the same serverless-SQL-over-object-store pattern across clouds *(Synapse serverless docs: best practices)*
    - when serverless SQL beats a running warehouse vs when it bankrupts you — query frequency × scan size crossover *(Synapse serverless docs: best practices)*
- **Resources:**
    - **[Synapse serverless SQL pool: best practices](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/best-practices-serverless-sql-pool)** — partitioning, Parquet conversion, predicate pushdown, statistics; the cost-model mechanics (primary)
    - [Trino documentation: overview](https://trino.io/docs/current/overview.html) — the open serverless-SQL-over-object-store engine that Athena/Synapse serverless descend from (reference)
- **Tools:**
    - Corp (evaluate): [Synapse serverless SQL](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/best-practices-serverless-sql-pool) — per-TB query over the lake (↔ FOSS: Trino over MinIO from earlier phases)
    - FOSS (hands-on): [Trino](https://trino.io/docs/current/) — the open serverless-SQL engine that makes the pricing trade-off concrete
- **Do:**
    1. Estimate query cost for your gold layer at three partitioning strategies (none, by date, by date+ISIN).
    2. Convert one CSV gold table to partitioned Parquet and re-estimate the scan.
    3. Write one paragraph on the design pressure per-TB pricing creates on file layout.
- **Done when:**
    - [ ] Explain why file layout *is* the cost model in serverless SQL.
    - [ ] Show the cost delta across your three partitioning strategies.
- Est. hours: 2

#### 8.1.2 Vendor reference architectures — T2
- **Why:** Databricks/Snowflake/Fabric blueprints are the shapes vendors will pitch at your employer; you need to read them critically, not learn them reverently. Each blueprint is optimized for the vendor's lock-in, and the architect's job is to translate it into open-component vocabulary and circle the lock-in points live in a meeting. Without this, the org buys the diagram and discovers the exit cost three years later.
- **Learn:**
    - Databricks lakehouse reference — Unity Catalog-centric, medallion layering, DBU-priced compute *(Databricks docs: well-architected lakehouse)*
    - Snowflake data-cloud patterns — secure data sharing, zero-copy clones, listings/exchanges *(Snowflake docs: data sharing)*
    - Fabric end-to-end — OneLake-centric, capacity-based, experiences stitched together *(Fabric docs: end-to-end tutorials)*
    - what each blueprint optimizes for the vendor, and mapping all three onto your open-stack mental model *(Databricks docs: well-architected lakehouse)*
- **Resources:**
    - **[Databricks: well-architected lakehouse](https://docs.databricks.com/aws/en/lakehouse-architecture/)** — the Unity-Catalog/medallion reference and its design principles (primary)
    - [Snowflake: data sharing and collaboration](https://docs.snowflake.com/en/guides-overview-sharing) — shares, listings, zero-copy collaboration patterns (reference)
    - [Microsoft Fabric: end-to-end tutorials](https://learn.microsoft.com/en-us/fabric/get-started/end-to-end-tutorials) — the OneLake-centric, capacity-based blueprint end to end (reference)
- **Do:**
    1. Read one vendor blueprint in a single sitting and annotate it.
    2. Circle every lock-in point (proprietary catalog, proprietary format, capacity SKU, egress trap).
    3. For each lock-in point, write the open-stack equivalent (Iceberg, a catalog, Trino, MinIO).
- **Done when:**
    - [ ] Translate any vendor diagram into open-component vocabulary live in a meeting.
    - [ ] Name the single biggest lock-in point in each of the three blueprints.
- Est. hours: 3

#### 11.8.1 Secrets management — T2
- **Why:** pipelines hold credentials to everything; secrets architecture is a prerequisite to the Phase-6 security work and every audit. A fund platform connecting to transfer-agency systems, market-data feeds, and the warehouse cannot have passwords in env vars or config files — that is an immediate audit finding and a breach waiting to happen. Get this wrong and rotation becomes impossible, so leaked credentials live forever.
- **Learn:**
    - secret stores vs env vars vs files — why a vault with access policies and audit logs is the only acceptable answer *(OpenBao docs: concepts)*
    - rotation — short-lived dynamic secrets and the rotation runbook *(OpenBao docs)*
    - managed identities as the no-secret ideal — eliminate the credential entirely where Azure supports it *(Entra docs: managed identities)*
    - secret injection into K8s (CSI driver) and CI — getting secrets to workloads without writing them to disk *(Azure Key Vault docs: overview)*
    - the Vault→OpenBao licensing fork — what the BSL change means for tool selection *(OpenBao docs: concepts)*
- **Resources:**
    - **[OpenBao documentation](https://openbao.org/docs/)** — concepts, secret engines, dynamic secrets, rotation; the MPL fork of Vault (primary)
    - [Azure Key Vault overview](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) — the corp store, HSM tiers, RBAC, integration with K8s/CI (reference)
    - [Entra: managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview) — the no-secret pattern that beats any store (deepening)
- **Tools:**
    - FOSS (hands-on): [OpenBao](https://openbao.org/docs/) — self-hosted secret store with dynamic secrets (↔ Azure Key Vault, AWS Secrets Manager)
    - Corp (evaluate): [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) — managed store + HSM; pairs with managed identities
- **Do:**
    1. Move every credential in the compose/K8s stack out of files into OpenBao.
    2. Wire one service to fetch its secret at runtime (CSI driver or API), not from disk.
    3. Document the rotation runbook and time a rotation end to end.
- **Done when:**
    - [ ] Confirm `git grep -i password` returns nothing real.
    - [ ] Rotate a credential as a 5-minute documented operation.
    - [ ] Name one service where a managed identity removes the secret entirely.
- Est. hours: 3

#### 12.7.2 Observability stack (OpenTelemetry, Prometheus, Grafana) — T2
- **Why:** logs/metrics/traces with OTel is the CNCF-standard nervous system; data platforms without it are debugged by archaeology. When a NAV pipeline misses its cut-off, the architect must point to a dashboard that shows where lag or failure occurred — not start a forensic dig through logs. Without observability there are no data SLAs, no error budgets, and no honest answer to "is the platform healthy right now?".
- **Learn:**
    - the three pillars and the OTel signals model — traces/metrics/logs, the collector, OTLP *(OpenTelemetry docs: concepts)*
    - instrumenting a Python pipeline with OTel — spans across a Dagster→Spark→Iceberg run *(OpenTelemetry docs: Python)*
    - Prometheus — the scrape model, PromQL basics, alerting rules *(Prometheus docs: overview)*
    - Grafana dashboards and Loki for logs — the visualization and log-aggregation layer *(Grafana docs: contact points)*
    - SLI/SLO/error-budget vocabulary — deepened in Phase 8 for data SLAs *(OpenTelemetry docs: concepts)*
    - Azure Monitor/App Insights as the corp mapping — ties to A.5 KQL *(OpenTelemetry docs: concepts)*
- **Resources:**
    - **[OpenTelemetry documentation](https://opentelemetry.io/docs/concepts/)** — [concepts](https://opentelemetry.io/docs/concepts/) and [Python instrumentation](https://opentelemetry.io/docs/languages/python/); the signals model and how to emit it (primary)
    - [Prometheus: Overview](https://prometheus.io/docs/introduction/overview/) — scrape model, PromQL, alerting (reference)
    - [Grafana: configure contact points](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/) — dashboards and alert routing (reference)
- **Tools:**
    - FOSS (hands-on): [OpenTelemetry](https://opentelemetry.io/docs/) + [Prometheus](https://prometheus.io/docs/) + [Grafana](https://grafana.com/docs/grafana/latest/) + [Loki](https://grafana.com/docs/loki/latest/) — the open observability stack (↔ Azure Monitor, Datadog)
    - Corp (evaluate): [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/) / [Datadog](https://docs.datadoghq.com/) — managed observability; know the build-vs-buy line
- **Do:**
    1. Instrument the Dagster→Spark→Iceberg path with OTel traces and pipeline metrics (rows processed, lag, run duration).
    2. Stand up Prometheus to scrape the metrics and Grafana to visualize them.
    3. Build the platform-health Grafana dashboard with two alert rules: data freshness and consumer lag.
    4. Seed a failure and confirm it shows up on the dashboard with the trace attached.
- **Done when:**
    - [ ] Diagnose a seeded failure from the dashboard alone in under five minutes, traces included.
    - [ ] Show a single trace spanning the full Dagster→Spark→Iceberg run.
    - [ ] Demonstrate both alert rules firing on real conditions.
- Est. hours: 8

#### 12.2.2 Disaster-recovery patterns — T1
- **Why:** RTO/RPO design is a DORA-driven architect deliverable; "what happens if the region dies?" now has regulatory teeth in EU financial services. A fund administrator must be able to recover NAV-relevant data within stated objectives, and the architect owns the topology that delivers them tier by tier. Without an explicit, tested DR design, the org discovers its real RTO during the outage — and explains the gap to a regulator afterwards.
- **Learn:**
    - RTO/RPO/RCO definitions and how to elicit honest numbers from the business *(Azure reliability docs: BC/HA/DR)*
    - topology ladder — backup-restore → pilot light → warm standby → active-active, with cost curves *(Azure reliability docs: BC/HA/DR)*
    - data-layer DR specifics — storage replication (LRS/ZRS/GRS), database geo-replication & failover groups *(Azure reliability docs: BC/HA/DR)*
    - Kafka cross-cluster (MirrorMaker/Geo-DR) and lakehouse DR — re-derivable vs source-of-truth tiers *(Azure reliability docs: BC/HA/DR)*
    - DR testing discipline — game days, failover drills, region pairs & EU residency constraints *(Azure reliability docs: BC/HA/DR)*
- **Resources:**
    - **[Azure reliability: Business continuity, HA & DR](https://learn.microsoft.com/en-us/azure/reliability/concept-business-continuity-high-availability-disaster-recovery)** — RTO/RPO, the topology ladder, failover/failback, residency-bound DR (primary)
    - [PostgreSQL: log-shipping standby servers](https://www.postgresql.org/docs/current/warm-standby.html) — concrete warm-standby/geo-replication mechanics for the database tier (reference)
- **Tools:**
    - Corp (evaluate): [Azure Site Recovery](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview) — orchestrated failover for VM/on-prem tiers
    - FOSS (hands-on): [PostgreSQL streaming replication](https://www.postgresql.org/docs/current/warm-standby.html) — warm-standby you can demonstrate locally
- **Do:**
    1. Tier every store in your platform by RPO/RTO class (e.g. gold marts vs bronze raw).
    2. Choose a topology per tier (backup-restore, pilot light, warm standby, active-active) and justify it.
    3. Cost the delta of each chosen topology vs single-region.
    4. Script and run one tabletop failover drill, recording the achieved RTO/RPO.
- **Done when:**
    - [ ] Defend why gold marts get warm standby but bronze gets backup-restore, with numbers.
    - [ ] State RTO/RPO per tier and the topology that meets it.
    - [ ] Produce a tabletop drill writeup with achieved vs target objectives.
- Est. hours: 7

#### 12.1.1 Backup & recovery (cloud-native) — T2
- **Why:** backups are the bottom rung of the DR ladder and the part auditors actually test; lakehouse-era backup is mostly *not* file copies. A fund platform must answer "when did we last successfully restore?" with a date, and Iceberg snapshots are not a backup when the catalog itself is lost. Without immutable, tested backups, a ransomware event or a bad catalog migration is unrecoverable.
- **Learn:**
    - Azure Backup model — vaults, policies, soft delete, immutability for ransomware *(Azure Backup docs: overview)*
    - database PITR windows — point-in-time restore and its retention limits *(Azure Backup docs: overview)*
    - object-store versioning + lifecycle as backup — and its limits *(Azure Backup docs: overview)*
    - Iceberg snapshot retention vs backup — why snapshots ≠ backups when the catalog dies *(Azure Backup docs: overview)*
- **Resources:**
    - **[Azure Backup: overview](https://learn.microsoft.com/en-us/azure/backup/backup-overview)** — vaults, policies, immutability, blob/database backup, ransomware protection (primary)
    - [Reliability in Azure Backup](https://learn.microsoft.com/en-us/azure/reliability/reliability-backup) — soft delete, immutable vaults, ZRS/GRS for the backups themselves, and the restore-RPO/RTO mechanics (reference)
- **Tools:**
    - Corp (evaluate): [Azure Backup](https://learn.microsoft.com/en-us/azure/backup/backup-overview) — vault-based backup with immutability (↔ FOSS object-store versioning)
    - FOSS (hands-on): [MinIO versioning](https://min.io/docs/minio/linux/administration/object-management/object-versioning.html) — the local stand-in for object-store backup/restore
- **Do:**
    1. Define a backup policy matrix for every store: what, frequency, retention, immutability, restore-test cadence.
    2. Run one real restore from MinIO versioning and time it.
    3. Note for each store whether a snapshot is a backup, and what additional protection the catalog needs.
- **Done when:**
    - [ ] Answer "when did we last *restore* successfully?" with a date, not a shrug.
    - [ ] Produce a complete backup policy matrix for the platform.
- Est. hours: 2

#### 12.3.1 FinOps / cloud cost management — T1
- **Why:** explicit mastery bias: cost models decide architectures, and the architect who can't price a design loses the vendor-selection argument to whoever can. In a fund business, a defensible "€ per daily NAV pipeline run" is what wins or loses the build-vs-buy debate with the CFO. Without a cost model, designs are chosen on aesthetics and the bill is discovered in production.
- **Learn:**
    - FinOps lifecycle (inform/optimize/operate) and unit economics — € per pipeline run, per report, per GB served *(FinOps Foundation framework)*
    - Azure pricing mechanics for data — storage tiers, egress, compute SKUs, reservations/savings plans, spot *(Azure Cost Management docs)*
    - tagging & cost allocation — showback/chargeback so costs land on the right business unit *(Azure Cost Management docs)*
    - the big levers — storage-format efficiency, cluster right-sizing, serverless-vs-provisioned crossover, egress avoidance *(FinOps Foundation framework)*
    - Azure Cost Management + budgets/alerts and the FOCUS billing standard (awareness) *(Azure Cost Management docs)*
- **Resources:**
    - **[FinOps Foundation: Framework](https://www.finops.org/framework/)** — the lifecycle, personas, capabilities, and unit-economics discipline (primary)
    - [Azure Cost Management overview](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) — pricing mechanics, allocation, budgets/alerts (reference)
    - [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) — the lab bench for the cost model (reference)
- **Tools:**
    - Corp (evaluate): [Azure Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) — the primary tool for analysis, budgets, allocation
    - FOSS (hands-on): [OpenCost](https://www.opencost.io/docs/) — Kubernetes cost allocation (awareness; ↔ Vantage/Cloudability)
- **Do:**
    1. Build the full monthly cost model of your target Azure architecture (calculator-based) at 1× data volume.
    2. Re-price the same model at 10× volume and note which lines scale and which step.
    3. Identify the three biggest levers and re-price after pulling them.
- **Done when:**
    - [ ] State € per daily NAV pipeline run and defend every line of the model to a CFO.
    - [ ] Show the 1× vs 10× cost shape and name what drives the difference.
    - [ ] Quantify the saving from your top three levers.
- Est. hours: 9

#### 12.3.2 Data-specific FinOps — T2
- **Why:** warehouse credits and per-query economics behave differently from VM bills; data FinOps is its own discipline with its own levers. A Snowflake or Databricks estate can burn its budget on idle warehouses and oversized clusters that a VM-centric FinOps view never catches. The architect who can spot credit-burn anti-patterns in a usage report is the one who keeps the analytics bill defensible.
- **Learn:**
    - Snowflake credit-burn anatomy — warehouse size × uptime, and auto-suspend discipline *(Snowflake docs: cost)*
    - Databricks DBU model & cluster policies — capping size/idle to control DBU spend *(Databricks docs: compute policies)*
    - BigQuery on-demand vs capacity — per-TB-scanned vs reserved slots *(Databricks docs: pricing)*
    - per-query attribution and the query-cost review as a governance practice *(Snowflake docs: cost)*
- **Resources:**
    - **[Snowflake: understanding overall cost](https://docs.snowflake.com/en/guides-overview-cost)** — credit anatomy, warehouse uptime, auto-suspend, attribution (primary)
    - [Databricks: create and manage compute policies](https://docs.databricks.com/aws/en/admin/clusters/policies) — cluster policies that cap DBU burn (reference)
    - [BigQuery pricing](https://cloud.google.com/bigquery/pricing) — on-demand vs capacity model for the cross-warehouse comparison (reference)
- **Tools:**
    - Corp (evaluate): [Snowflake](https://docs.snowflake.com/) — credit-based warehouse economics
    - Corp (evaluate): [Databricks](https://www.databricks.com/product/pricing) — DBU model and cluster policies
- **Do:**
    1. Write the "cost guardrails" standard for a warehouse estate: auto-suspend, size caps, query tagging, monthly review ritual.
    2. Map each guardrail to the mechanism that enforces it (warehouse setting, cluster policy, tag policy).
    3. List the three classic credit-burn anti-patterns and how the standard prevents each.
- **Done when:**
    - [ ] Spot the three classic credit-burn anti-patterns in a usage report.
    - [ ] Produce a guardrails standard with an enforcement mechanism per rule.
- Est. hours: 3

#### 3.3.4 Caching — T2
- **Why:** caches (Redis/Valkey) sit in front of every serving layer; the architect mostly decides *whether* and *where*, not *how*. For fund NAV data — computed once daily — caching is almost free wins, but for intraday positions a stale cache is a correctness bug. The architect who can't articulate the staleness-vs-load trade-off either over-caches and serves wrong numbers or under-caches and melts the serving layer.
- **Learn:**
    - cache-aside vs read/write-through — who owns the write and when the cache updates *(Azure caching guidance)*
    - invalidation & TTL discipline — the hard part; TTL choice as a correctness decision *(Azure caching guidance)*
    - what to cache in a data platform — API responses, semantic-layer results, feature lookups *(Azure caching guidance)*
    - Valkey/Redis licensing fork and Azure Cache for Redis / Azure Managed Redis *(Azure Cache for Redis docs: overview)*
- **Resources:**
    - **[Azure Architecture Center: Caching guidance](https://learn.microsoft.com/en-us/azure/architecture/best-practices/caching)** — cache-aside, write-through, invalidation, TTL, what to cache (primary)
    - [Azure Cache for Redis: overview](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview) — the managed cache tiers and patterns (reference)
- **Tools:**
    - FOSS (hands-on): [Valkey](https://valkey.io/documentation/) — the open Redis fork for the serving-layer cache (↔ Azure Cache for Redis)
    - Corp (evaluate): [Azure Cache for Redis](https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/cache-overview) — managed cache; note the retirement/Managed Redis migration path
- **Do:**
    1. Decide cache placement for the Phase-8 data API: yes/no, where in the path, and TTL.
    2. Write the 10-line justification anchored to the staleness-vs-load trade-off.
- **Done when:**
    - [ ] Articulate the staleness-vs-load tradeoff for fund NAV data specifically (hint: NAVs are daily — cache hard).
    - [ ] State the TTL you chose and why it is correct for that data's update cadence.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 2.2.1 | Log/metric shippers | Fluent Bit/Vector agents that collect, transform, and route logs/metrics into observability pipelines | [Vector docs "Concepts"](https://vector.dev/docs/introduction/concepts/) | 20 |
| 2.5.1 | iPaaS | Workato/Boomi/Power Automate low-code integration aimed at business users rather than data engineers | [Power Automate overview](https://learn.microsoft.com/en-us/power-automate/getting-started) | 20 |
| 2.5.2 | ESB (legacy) | Central-bus integration era (TIBCO/IBM); the "smart pipes" estate you'll be strangling toward smart-endpoints | [Fowler: Microservices (ESB/SOA retrospective)](https://martinfowler.com/articles/microservices.html) | 20 |
| 3.2.7 | Time-series databases | Prometheus/InfluxDB/kdb+ for timestamp-keyed data (kdb+ = the market-data niche in finance) | [InfluxDB "What is time series data"](https://www.influxdata.com/what-is-time-series-data/) | 20 |
| 3.3.2 | Block storage | VM disks (Azure Managed Disks); the substrate databases and VMs sit on | [Azure Managed Disks overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) | 15 |
| 3.3.3 | File storage | NFS/SMB shares (Azure Files) for legacy app integration and lift-and-shift workloads | [Azure Files introduction](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction) | 15 |
| 5.1.1 | Visual ETL suites | Informatica/SSIS/DataStage — the installed base you'll meet across EU financial services | [Informatica PowerCenter product page](https://www.informatica.com/products/data-integration/powercenter.html) | 25 |
| 9.10.3 | Configuration management | Ansible/Chef VM-era config; mostly displaced by immutable containers but alive in on-prem banks | [Ansible "Getting started"](https://docs.ansible.com/ansible/latest/getting_started/index.html) | 20 |
| 12.1.2 | Enterprise backup suites | Veeam/Commvault/Rubrik estates protecting on-prem bank infrastructure | [Veeam Data Platform overview](https://www.veeam.com/products/veeam-data-platform.html) | 15 |
| 12.2.1 | DR tooling | Azure Site Recovery/Zerto for orchestrated failover of VM and on-prem workloads | [Azure Site Recovery overview](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview) | 20 |
| 12.5.1 | On-call/paging | PagerDuty/Opsgenie rotations & escalation that route incidents to a human | [PagerDuty on-call management](https://www.pagerduty.com/platform/incident-management/on-call-management/) | 15 |
| 12.5.2 | Postmortems | Blameless incident review that fixes systems, not people | [Google SRE: Postmortem Culture](https://sre.google/sre-book/postmortem-culture/) | 30 |
| 12.6.1 | Capacity planning | Forecasting growth against provisioning so the platform neither starves nor wastes | [Google SRE: Software Engineering in SRE (Auxon/capacity planning)](https://sre.google/sre-book/software-engineering-in-sre/) | 20 |
| 12.7.1 | Commercial APM | Datadog/Dynatrace full-stack suites — the build-vs-buy alternative to the OTel stack | [Datadog product overview](https://www.datadoghq.com/product/) | 15 |
| 14.7.3 | Notification tools | Routing data-signal alerts to paging/chat from observability tooling | [Grafana alerting: contact points](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/) | 10 |

*T3 subtotal: 4.5 h*

### Capstone 5 — IaC-provisioned platform on Kubernetes + Well-Architected review

- **Goal:** the platform becomes infrastructure-as-code on a cloud-shaped runtime, with observability, a DR position, and a cost model — everything an architecture review board would demand.
- **Stack (100% free):** [kind](https://kind.sigs.k8s.io/docs/) or [k3d](https://k3d.io/) local Kubernetes (↔ AKS), [Helm](https://helm.sh/docs/) charts for [Kafka](https://kafka.apache.org/documentation/)/[Flink](https://nightlies.apache.org/flink/flink-docs-stable/)/[Trino](https://trino.io/docs/current/)/[Dagster](https://docs.dagster.io/)/[MinIO](https://min.io/docs/minio/kubernetes/upstream/)/[Postgres](https://www.postgresql.org/docs/) (↔ managed PaaS equivalents), [OpenTofu](https://opentofu.org/docs/) with kubernetes/helm/azurerm providers (↔ Terraform Enterprise), [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/) comparison module, [OpenBao](https://openbao.org/docs/) (↔ [Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)), [OTel](https://opentelemetry.io/docs/) + [Prometheus](https://prometheus.io/docs/) + [Grafana](https://grafana.com/docs/grafana/latest/) + [Loki](https://grafana.com/docs/loki/latest/) (↔ [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/)), [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) + free-trial `tofu plan` (no spend).
- **Build:** (1) migrate the compose stack to kind via Helm, OpenTofu-managed end to end; (2) secrets via OpenBao with documented rotation; (3) full observability: traces through one pipeline run, platform dashboard, two alerts (freshness, consumer lag); (4) azurerm module expressing the target Azure architecture (landing-zone slice: VNet/Private Link per A.3, ADLS, AKS, Event Hubs, Key Vault) — validated plan-only; (5) WAF review of the result (one finding per pillar, remediated or accepted in writing); (6) DR design + tabletop drill; (7) monthly cost model at 1×/10×.
- **Architecture deliverables:** C4 deployment diagram (new level for this phase); ADR-013 Kubernetes vs managed-PaaS-per-service, ADR-014 OpenTofu vs Bicep for this estate, ADR-015 DR topology per data tier.
- **Acceptance criteria:** fresh machine → `tofu apply` → healthy platform → one full pipeline run → `tofu destroy`, all documented; seeded failure diagnosed from dashboards in <5 min; WAF review yields ≥5 genuine findings with dispositions; cost model withstands a "what if volumes 10×?" challenge; DR drill writeup names RTO/RPO per tier.
- Est. hours: 18

*Phase 5 total: 107.5 h (T1/T2 entries 85 h + T3 4.5 h + capstone 18 h) + Appendix A items A.3–A.6, A.22, A.25, A.26 (37 h) scheduled in this phase*


<a id="phase-6"></a>
## Phase 6: Governance, Security & Compliance (months 34–39, 120 h + 14 h Appendix A)

*Phase 6 of 8 · months 34–39 · 134 h (120 h + 14 h Appendix A) · capstone: Governed platform — catalog, lineage, DQ, policy, DCAM.*  ← [Phase 5](#phase-5) · [Phase 7](#phase-7) →

**Goal:** build the control plane of a regulated data platform: catalog + lineage as the metadata backbone, data quality as an engineering discipline, MDM/RDM for the entities the fund industry lives on, fine-grained access control and masking, and the regulatory frameworks (GDPR, DORA, DCAM) that decide what "good" means in Luxembourg.
**Entry prerequisites:** Phases 2–5 (a platform worth governing; OTel/observability foundations).
**Exit criteria:** you can (1) stand up a catalog with end-to-end lineage and answer an impact-analysis question from it; (2) design a DQ framework from profiling to alerting with rules tied to the six dimensions; (3) design a security-master MDM with match/merge and survivorship; (4) implement RLS/CLS and policy-as-code on the lakehouse; (5) map your platform to GDPR/DORA obligations and lead a DCAM self-assessment.
**Appendix A items scheduled here:** A.14 data strategy & operating model, A.15 architecture risk management, A.16 data risk & controls, A.17 ethics, A.18 purpose-based sharing, A.19 records management, A.20 organizational change management (14 h).

### T1/T2 topics

#### 10.1.1 Metadata management & active catalogs — T1
- **Why:** in a regulated fund platform the catalog is the control plane an architect designs first — ownership, glossary, lineage, quality, and policy all hang off it, and CSSF/DORA reviewers expect a single answer to "who owns this and what depends on it". Without an active catalog, governance lives in stale spreadsheets, impact analysis becomes guesswork, and a schema change silently breaks an EMT feed nobody knew was downstream.
- **Learn:**
    - metadata kinds — technical vs business vs operational, and active vs passive (metadata that just describes vs metadata that fires actions) *(OpenMetadata docs: Main Concepts)*
    - OpenMetadata architecture — ingestion framework, connectors, and the APIs the platform exposes *(OpenMetadata docs: Ingestion)*
    - the entity model — domains, owners, tiers, and glossary links as the governance skeleton *(OpenMetadata docs: Main Concepts)*
    - automated ingestion — pulling metadata from Postgres, Trino/Iceberg, dbt, and Kafka rather than typing it *(OpenMetadata docs: Connectors)*
    - catalog-driven workflows — announcements, tasks, and approval flows triggered from the catalog *(OpenMetadata docs: Governance)*
    - DataHub as the alternative — event-sourced metadata, also OpenLineage-friendly *(DataHub docs: Architecture)*
    - what makes metadata "active" — policies and alerts firing *from* metadata, not a separate system *(OpenMetadata docs: Main Concepts)*
- **Resources:**
    - **[OpenMetadata documentation](https://docs.open-metadata.org/)** — concepts, entity model, ingestion, and governance workflows; the hands-on backbone for this entry (primary)
    - [DataHub documentation](https://docs.datahub.com/docs/) — the event-sourced alternative; read for its metadata architecture and connector model (alternate)
- **Tools:**
    - FOSS (hands-on): [OpenMetadata](https://docs.open-metadata.org/) — the catalog you deploy and ingest into (↔ Microsoft Purview, Collibra, Alation)
    - Corp (evaluate): [Microsoft Purview](https://learn.microsoft.com/en-us/purview/) — Azure default; know its Data Map and per-asset cost model at build-vs-buy level
    - Corp (evaluate): [Collibra](https://www.collibra.com/) — EU-FS incumbent; know its operating-model/stewardship strengths
- **Do:**
    1. Deploy OpenMetadata via its Docker quickstart and confirm the UI is reachable.
    2. Configure ingestion connectors for Postgres, Trino/Iceberg, dbt, and Kafka; run each pipeline and confirm assets land.
    3. Assign an owner and a tier to every gold asset; link at least one glossary term.
    4. Wire one active workflow: a schema-change announcement that notifies registered consumers of a gold table.
- **Done when:**
    - [ ] Answer "who owns this, who consumes it, what breaks if I change it?" from the catalog in under two minutes.
    - [ ] Show every gold asset carries an owner and a tier.
    - [ ] Trigger the schema-change announcement and confirm a consumer is notified.
- Est. hours: 10

#### 10.3.1 Data lineage (OpenLineage standard) — T1
- **Why:** BCBS-239-grade traceability means every regulatory number must walk back to its sources, and lineage is the architect's impact-analysis weapon when a source column changes. Without it, an auditor's "prove this NAV figure's provenance" becomes a multi-day archaeology dig, and you cannot safely answer "what breaks if I change this column?"
- **Learn:**
    - the OpenLineage object model — runs, jobs, datasets, and facets as the extensible spine *(OpenLineage docs: Spec)*
    - emitters — Dagster, Spark, and dbt integrations that produce events automatically *(OpenLineage docs: Integrations)*
    - Marquez as the reference backend — collecting and visualising lineage events *(Marquez docs: Quickstart)*
    - column-level vs table-level lineage — what SQL parsing (dbt) gives vs what Spark instrumentation gives *(OpenLineage docs: Spec)*
    - lineage into the catalog — feeding OpenMetadata/DataHub from OpenLineage events *(OpenMetadata docs: Lineage)*
    - designing for lineage — naming and job granularity that keep graphs readable *(OpenLineage docs: Integrations)*
    - limits — black-box SaaS steps that emit nothing and how to annotate the gap *(OpenLineage docs: Spec)*
- **Resources:**
    - **[OpenLineage documentation](https://openlineage.io/docs/)** — the spec (runs/jobs/datasets/facets) plus Dagster, Spark, and dbt integrations (primary)
    - [Marquez](https://marquezproject.ai/) — the reference OpenLineage backend; getting-started and the lineage UI you will render from (reference)
    - [OpenMetadata: Lineage](https://docs.open-metadata.org/) — how lineage surfaces inside the catalog you stood up in 10.1.1 (deepening)
- **Tools:**
    - FOSS (hands-on): [OpenLineage](https://openlineage.io/docs/) + [Marquez](https://marquezproject.ai/) — emit and collect lineage, surfaced in OpenMetadata (↔ Purview lineage, Collibra lineage, Manta)
    - Corp (evaluate): [Microsoft Purview](https://learn.microsoft.com/en-us/purview/) / [Collibra](https://www.collibra.com/) lineage — know their depth and connector limits at evaluation level
- **Do:**
    1. Emit OpenLineage events from Dagster and dbt for the full NAV path (Postgres → Debezium → Iceberg → Spark → dbt → EMT output).
    2. Point the emitters at Marquez and confirm runs/jobs/datasets appear.
    3. Render end-to-end lineage for the EMT output and capture column-level detail where dbt SQL parsing allows.
    4. Answer one impact query — "which reports break if `orders.amount` changes?" — directly from the graph.
- **Done when:**
    - [ ] Demonstrate the EMT output's lineage back to source tables to an auditor, column-level where the tooling allows.
    - [ ] Trace the answer to the `orders.amount` impact query from the graph alone.
    - [ ] Identify and annotate any black-box step where lineage stops.
- Est. hours: 7

#### 9.4.2 + 10.4.1 Data quality engineering (Great Expectations / Soda) — T1
- **Why:** in regulated data, DQ rules are how "accuracy, completeness, timeliness" stop being audit prose and become enforced code that blocks a bad publish. Without engineered DQ, a wrong holdings count or a stale FX rate flows into NAV unchecked, and the architect cannot defend which checks run, at what severity, or why.
- **Learn:**
    - the six DQ dimensions — accuracy, completeness, consistency, timeliness, validity, uniqueness — mapped to executable rule types *(Data Quality Fundamentals ch. 1–4)*
    - Great Expectations — suites, checkpoints, and data docs as the rule-and-report layer *(Great Expectations docs)*
    - Soda Core — SodaCL checks and scans wired into orchestration *(Soda docs: Soda Core)*
    - dbt tests vs dedicated DQ frameworks — layering, not either/or *(Soda docs)*
    - severity & circuit-breaking — block-publish vs warn, tied to your WAP gates *(Data Quality Fundamentals ch. 4)*
    - DQ result routing — pushing pass/fail into the catalog and alerts *(Soda docs)*
    - rules from profiling, not imagination — writing checks against observed distributions *(Data Quality Fundamentals ch. 3)*
- **Resources:**
    - **[Data Quality Fundamentals (Moses, Gavish, Vorwerck)](https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/)** ch. 1–4 — the dimensions, rule design, and severity model (primary)
    - [Soda documentation](https://docs.soda.io/) — Soda Core and SodaCL, the check syntax you wire into the WAP gate (reference)
    - [Great Expectations documentation](https://docs.greatexpectations.io/) — suites, checkpoints, and data docs as the alternate framework (alternate)
- **Tools:**
    - FOSS (hands-on): [Soda Core](https://docs.soda.io/) + [Great Expectations](https://docs.greatexpectations.io/) + [dbt tests](https://docs.getdbt.com/docs/build/data-tests) — the layered DQ stack (↔ Informatica DQ, Talend DQ)
    - Corp (evaluate): [Informatica Data Quality](https://docs.informatica.com/) — EU-FS incumbent; evaluate at build-vs-buy level
- **Do:**
    1. Define the DQ rulebook for the NAV pipeline: per dataset, rules across all six dimensions with explicit severities.
    2. Express the rules as SodaCL checks (use Great Expectations for any complex distributional check).
    3. Wire Soda scans into the WAP gate so criticals block publish and warnings page.
    4. Route results to the catalog so each failure links back to the failing expectation.
- **Done when:**
    - [ ] Trigger a seeded completeness failure that blocks publish, appears in the catalog, and pages with a link to the failing expectation.
    - [ ] Justify every rule's dimension and severity in writing.
    - [ ] Show warnings page without blocking while criticals halt the run.
- Est. hours: 10

#### 10.4.3 Data profiling — T2
- **Why:** profiling is the evidence-gathering step before DQ rules — you discover real distributions, cardinalities, and surprises in fund data rather than assuming them. Skip it and your rules encode myths (e.g. assuming an ISIN column is always populated when 2% are vendor placeholders), producing false alarms that erode trust in the DQ gate.
- **Learn:**
    - profiling outputs — distributions, null rates, uniqueness, value patterns, and drift over time *(ydata-profiling docs)*
    - ydata-profiling — one-shot exploratory profile reports from a single line *(ydata-profiling docs)*
    - whylogs — lightweight, mergeable statistical profiles for continuous monitoring *(whylogs docs: Overview)*
    - profiling as DQ-rule generator — turning observed bounds into Soda checks *(ydata-profiling docs)*
    - PII-discovery overlap — profiling surfaces candidate sensitive columns, feeding 11.4.1 *(whylogs docs: Overview)*
- **Resources:**
    - **[ydata-profiling documentation](https://docs.profiling.ydata.ai/)** — one-shot EDA reports: distributions, nulls, correlations, alerts (primary)
    - [whylogs (WhyLabs docs)](https://docs.whylabs.ai/docs/whylogs-overview/) — continuous, mergeable statistical profiles for scheduled drift checks (reference)
- **Tools:**
    - FOSS (hands-on): [ydata-profiling](https://docs.profiling.ydata.ai/) — one-shot profiles (↔ Informatica/Collibra profiling modules)
    - FOSS (hands-on): [whylogs](https://docs.whylabs.ai/docs/whylogs-overview/) — scheduled statistical profiles and diff alerting
- **Do:**
    1. Run ydata-profiling on the silver holdings table and review the alerts section.
    2. Identify the five most surprising findings (unexpected nulls, cardinality, ranges).
    3. Turn each finding into a Soda rule with the right dimension and severity.
    4. Schedule a weekly whylogs profile and configure a diff alert on drift.
- **Done when:**
    - [ ] Show at least three DQ rules that exist *because* profiling falsified an assumption.
    - [ ] Produce a weekly whylogs profile that diffs against the prior week.
- Est. hours: 3

#### 10.4.2 Managed data observability platforms — T2
- **Why:** Monte Carlo-class tools are the buy side of the DQ build-vs-buy decision, and their ML-anomaly pitch needs an architect's informed evaluation, not a sales demo's. Misjudging it means either over-paying for anomaly detection you could rule-encode, or hand-rolling freshness/volume monitoring that a managed tool would catch for less.
- **Learn:**
    - anomaly-detection-on-metadata — flagging freshness/volume/schema drift without hand-written rules *(Monte Carlo docs)*
    - incident workflow & blast radius — lineage-aware incident grouping and downstream impact *(Monte Carlo docs)*
    - pricing models — per-table/per-monitor economics at estate scale *(Monte Carlo docs)*
    - complementarity — where rule-based and anomaly-based DQ each win and lose *(Data Quality Fundamentals ch. on observability)*
- **Resources:**
    - **[Monte Carlo documentation](https://docs.getmontecarlo.com/)** — architecture and the anomaly/incident model (vendor source, read critically) (primary)
    - [Data Quality Fundamentals](https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/) — the observability chapters as the vendor-neutral counterweight (reference)
- **Do:**
    1. Outline your current FOSS stack (Soda + Elementary) coverage by failure class.
    2. Map Monte Carlo's anomaly-detection coverage against the same failure classes.
    3. Write a half-page build-vs-buy comparison for a 200-pipeline estate, including a rough cost sketch.
- **Done when:**
    - [ ] State which failure classes anomaly detection catches that your rules never will, and vice versa.
    - [ ] Recommend build, buy, or hybrid with a one-line justification tied to estate size.
- Est. hours: 2

#### 10.9.1 + 10.9.2 Data observability (pipeline health) — T2
- **Why:** freshness/volume/schema-drift monitoring is the data plane's heartbeat, distinct from infra observability (Phase 5) and from DQ rules — it catches the silent failures that produce a NAV from yesterday's prices. Without it, a stalled Debezium connector or a shrunken load lands quietly and surfaces only when a client queries a wrong number.
- **Learn:**
    - the five data-observability pillars — freshness, volume, schema, distribution, lineage *(Data Quality Fundamentals: observability pillars)*
    - Elementary as dbt-native observability — anomaly tests and the report UI on top of your dbt project *(Elementary docs)*
    - unified alerting — routing data incidents through the same path as infra alerts *(Elementary docs)*
    - the data-incident triage runbook — who is paged, what they check, how it is resolved *(Data Quality Fundamentals: observability pillars)*
- **Resources:**
    - **[Elementary documentation](https://docs.elementary-data.com/)** — dbt-native freshness/volume/schema anomaly tests and the observability report (primary)
    - [Data Quality Fundamentals](https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/) — the observability-pillars framing (reference)
- **Tools:**
    - FOSS (hands-on): [Elementary](https://docs.elementary-data.com/) + [OpenLineage](https://openlineage.io/docs/) events — anomaly tests plus lineage context (↔ Monte Carlo, Databand, Bigeye)
- **Do:**
    1. Add Elementary to the dbt project and run its on-run-end hooks.
    2. Enable volume and freshness anomaly tests on gold models.
    3. Route one synthetic incident (force a stale/shrunken load) through Grafana alerting with a runbook link.
    4. Assign an owner to each detector.
- **Done when:**
    - [ ] Show silent-failure classes (stale, shrunken, schema-drifted) each have a detector and an owner.
    - [ ] Fire the synthetic incident end-to-end into Grafana with a runbook link attached.
- Est. hours: 3

#### 10.5.1 Master data management — T1
- **Why:** the security/fund/counterparty master *is* the fund-industry data problem — every NAV error story ends at reference data, and the architect designs the master even when the tool is bought. Get match/merge or survivorship wrong and two vendor records for the same instrument double-count a position, or a corporate action applies to the wrong golden record and corrupts every downstream report.
- **Learn:**
    - MDM styles — registry, consolidation, coexistence, centralized — and their org costs *(DAMA-DMBOK ch. 10)*
    - match/merge — deterministic vs probabilistic (Fellegi–Sunter intuition), blocking, thresholds *(Splink docs: Fellegi-Sunter)*
    - survivorship & golden-record assembly — which source wins each attribute and why *(DAMA-DMBOK ch. 10)*
    - hierarchy management — fund → sub-fund → share class, and issuer trees *(DAMA-DMBOK ch. 10)*
    - stewardship workflow — review queues for ambiguous matches *(Splink docs)*
    - integration patterns — MDM as a publisher to the platform, not a silo *(DAMA-DMBOK ch. 10)*
    - security-master specifics — identifier cascade (ISIN/FIGI/internal), vendor precedence (Bloomberg vs Refinitiv), corporate-action survivorship *(DAMA-DMBOK ch. 10)*
- **Resources:**
    - **[DAMA-DMBOK (2nd ed.)](https://technicspub.com/dmbok/)** ch. 10 "Reference & Master Data" — MDM styles, survivorship, hierarchy management (primary)
    - [Splink documentation](https://moj-analytical-services.github.io/splink/) — probabilistic linkage, blocking, thresholds, and the Fellegi-Sunter model (MoJ open source) (reference)
- **Tools:**
    - FOSS (hands-on): [Splink](https://moj-analytical-services.github.io/splink/) for match/merge + [PostgreSQL](https://www.postgresql.org/docs/) for the hub (↔ Informatica MDM, Reltio, Semarchy, Tamr)
    - Corp (evaluate): [Informatica MDM](https://docs.informatica.com/) / [Semarchy](https://www.semarchy.com/) — EU-FS shortlist; evaluate at build-vs-buy level
- **Do:**
    1. Ingest two overlapping "vendor" feeds with conflicting attributes into Postgres.
    2. Run Splink match/merge with explicit blocking rules and tuned thresholds.
    3. Express survivorship rules in SQL to assemble the golden record.
    4. Publish the golden record plus a cross-reference table to the lakehouse.
- **Done when:**
    - [ ] Walk a steward through *why* two records merged (match weights) and *why* each golden attribute won (survivorship rule).
    - [ ] Defend registry-vs-centralized for a fund administrator in writing.
    - [ ] Produce a golden record + cross-reference table on the lakehouse.
- Est. hours: 9

#### 10.6.1 Reference data management — T2
- **Why:** code lists (countries, currencies, MICs, fund legal forms, CFI codes) are small data with outsized blast radius — one wrong currency code mis-prices a whole sub-fund. RDM is governance's unglamorous core, and without effective-dated, single-source code lists, the same "country" maps three ways across silver, gold, and the EMT feed.
- **Learn:**
    - internal vs external reference data — what you own vs what ISO/vendors publish *(DAMA-DMBOK ch. 10)*
    - versioning & effective dating — code lists that change without rewriting history *(DAMA-DMBOK ch. 10)*
    - distribution patterns — publish-subscribe from one source of truth *(DAMA-DMBOK ch. 10)*
    - mapping tables — reconciling vendor codes to your canonical codes *(DAMA-DMBOK ch. 10)*
    - ISO maintenance cadence — 4217 (currency), 3166 (country), 10383 (MIC) update rhythms *(DAMA-DMBOK ch. 10)*
    - SCD2 reuse — effective dating is the Phase-1 SCD2 discipline applied to reference data *(dbt docs: snapshots)*
- **Resources:**
    - **[DAMA-DMBOK (2nd ed.)](https://technicspub.com/dmbok/)** ch. 10 (reference-data half) — versioning, distribution, mapping patterns (primary)
    - [Collibra Reference Data Management](https://www.collibra.com/) — the corp pattern to evaluate against your FOSS build (reference)
    - [dbt snapshots](https://docs.getdbt.com/docs/build/snapshots) — SCD2 mechanics reused for effective-dated code lists (deepening)
- **Tools:**
    - FOSS (hands-on): [dbt seeds](https://docs.getdbt.com/docs/build/seeds) + a governed Postgres schema (↔ Collibra RDM, CluedIn)
- **Do:**
    1. Build a governed code-list schema (effective-dated, approved-by, source) for currencies, countries, and MICs.
    2. Load the ISO lists and record their source/version.
    3. Wire one mapping table (vendor country codes → ISO 3166) into the silver layer.
    4. Make a controlled change and confirm history is preserved.
- **Done when:**
    - [ ] Trace any code-list change to who/when/why.
    - [ ] Show the code list is consumed everywhere from one place.
- Est. hours: 3

#### 7.3.1 Business glossary — T2
- **Why:** "NAV", "AUM", and "dealing date" mean different things across teams until the glossary pins them, and glossary-to-asset linkage is what makes the catalog business-readable for compliance and front office alike. Without it, two reports labelled "AUM" disagree and nobody can say which definition is right.
- **Learn:**
    - term lifecycle — draft → approved, with owners and stewards *(OpenMetadata docs: Glossary)*
    - term-to-asset linkage — connecting a glossary term to every column that carries it *(OpenMetadata docs: Glossary)*
    - glossary vs data dictionary vs semantic layer — and the coming convergence *(DAMA-DMBOK ch. 13)*
    - seeding from regulation — AIFMD/PRIIPs definitions as authoritative term sources *(DAMA-DMBOK ch. 13)*
- **Resources:**
    - **[OpenMetadata: Glossary](https://docs.open-metadata.org/)** — term lifecycle, owners, and term-to-asset linkage (primary)
    - [DAMA-DMBOK (2nd ed.)](https://technicspub.com/dmbok/) ch. 13 (metadata/glossary sections) — glossary vs dictionary vs semantic layer (reference)
- **Tools:**
    - FOSS (hands-on): [OpenMetadata glossary](https://docs.open-metadata.org/) — the glossary you build and link (↔ Collibra, Purview glossary)
- **Do:**
    1. Create a 25-term fund glossary (NAV, swing price, AUM, dealing cut-off, …) with definitions.
    2. Assign an owner to each term.
    3. Link every gold table column that carries one of those terms to its glossary entry.
    4. Seed at least three definitions from regulation (AIFMD/PRIIPs).
- **Done when:**
    - [ ] Click "NAV" in the catalog and see its definition, its owner, and every asset that carries it.
    - [ ] Confirm all 25 terms have owners and at least one linked asset where applicable.
- Est. hours: 3

#### 1.12.6 + 3.2.6 FIBO & knowledge graphs / RDF — T2
- **Why:** FIBO is the finance ontology (EDM Council) and RDF/SPARQL is its native stack; semantic master data is a real pattern at EU regulators and large institutions, so the architect must read it fluently and judge where it earns its keep. Without that judgement you either ignore a shared vocabulary that would harmonise entity data, or over-invest in a triple store where a relational hub would do.
- **Learn:**
    - RDF triples and RDFS/OWL basics — the subject-predicate-object model and class/property vocabulary *(Apache Jena: RDF API tutorial)*
    - SPARQL reading fluency — querying a graph for paths and relationships *(Apache Jena: RDF API tutorial)*
    - SHACL validation — shape constraints over RDF, the graph analogue of DQ rules *(Apache Jena: RDF API tutorial)*
    - FIBO structure & pragmatic use — securities/funds/legal-entity domains as a vocabulary source, not a deployment mandate *(FIBO spec site)*
    - property graphs vs RDF — when Cypher/Neo4j beats triples and vice versa *(Apache Jena: RDF API tutorial)*
    - GLEIF Level-2 as a ready-made entity graph — "who owns whom" ownership relationships *(GLEIF: Level 2 data)*
- **Resources:**
    - **[FIBO (spec.edmcouncil.org)](https://spec.edmcouncil.org/fibo/)** — the finance ontology: structure, vocabulary, and the data dictionary (primary)
    - [Apache Jena: RDF API tutorial](https://jena.apache.org/tutorials/rdf_api.html) — RDF/SPARQL basics and the model API for the hands-on lab (reference)
    - [GLEIF Level 2: Who Owns Whom](https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-2-data-who-owns-whom) — the open ownership dataset you load and query (deepening)
- **Tools:**
    - FOSS (hands-on): [Apache Jena / Fuseki](https://jena.apache.org/documentation/fuseki2/) — triple store and SPARQL endpoint (↔ Stardog, Ontotext GraphDB, Neptune)
- **Do:**
    1. Load GLEIF Level-2 ownership for 50 entities into Fuseki.
    2. Write a SPARQL query that walks the ultimate-parent chains.
    3. Map five of your security-master attributes to FIBO terms.
    4. Note one constraint you could express as SHACL.
- **Done when:**
    - [ ] Return ultimate-parent chains for the loaded entities via SPARQL.
    - [ ] Say where FIBO genuinely helps (shared vocabulary, entity relationships) and where it's academic for your estate.
- Est. hours: 4

#### 11.1.2 Fine-grained access control (RLS/CLS on the platform) — T1
- **Why:** "who may see which fund's data at which column grain" is a regulatory requirement you must design *and prove* — Chinese walls between sub-funds and clients are access-control problems, and CSSF/GDPR reviewers will test them. Get RLS/CLS wrong and a TA agent sees another management company's investors, a reportable breach that no after-the-fact apology undoes.
- **Learn:**
    - the RBAC→ABAC→ReBAC ladder — where each authorization model fits data access *(OPA docs: Introduction)*
    - row-level security mechanics — Postgres RLS policies and their performance/leak caveats *(Postgres docs: Row Security Policies)*
    - column-level security & masking interplay — restricting columns vs obscuring values *(SQL Server: Dynamic Data Masking)*
    - lakehouse enforcement reality — engine-level (Trino) vs catalog-level (Unity) vs file-layer enforcement *(Trino docs: Security)*
    - the Unity/Ranger/Lake Formation models — who actually enforces at the file layer *(Unity Catalog: privileges reference)*
    - attribute sources — Entra groups and catalog tags driving ABAC decisions *(Trino docs: Security)*
    - access request/review workflows — recertification, an audit staple *(Postgres docs: Row Security Policies)*
- **Resources:**
    - **[PostgreSQL: Row Security Policies](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)** — RLS policy mechanics and caveats, the first enforcement archetype (primary)
    - [Trino: Security](https://trino.io/docs/current/security.html) — file-based and OPA access control over Iceberg, the engine-level archetype (reference)
    - [Unity Catalog: privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/privileges) — the catalog-level privilege model, the third archetype (deepening)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) + [Trino](https://trino.io/docs/current/security.html) with file-based/OPA rules (↔ Immuta, Privacera, Unity Catalog, Lake Formation)
    - Corp (evaluate): [Immuta](https://documentation.immuta.com/) + [Microsoft Purview](https://learn.microsoft.com/en-us/purview/) policies — evaluate at build-vs-buy level
- **Do:**
    1. Implement "TA agents see only their management company's funds" as Postgres RLS policies.
    2. Implement the same rule as Trino file-based/OPA rules over Iceberg.
    3. Tag PII columns in the catalog and enforce column-level security for a restricted role.
    4. Write the recertification procedure (who reviews access, how often, evidence captured).
- **Done when:**
    - [ ] Demonstrate the same policy at two enforcement layers (Postgres and Trino).
    - [ ] Name where each layer can be bypassed and explain the residual risk in writing.
    - [ ] Show the restricted role sees masked/withheld PII columns.
- Est. hours: 7

#### 11.1.3 Policy-as-code (OPA) — T2
- **Why:** externalized, testable authorization is the modern answer to policy sprawl, and OPA/Rego is its lingua franca across APIs, Kubernetes, and data engines. Without it, the fund-visibility rule lives in three places that drift apart, and changing it becomes three tickets to three admins with no test that the change is correct.
- **Learn:**
    - OPA architecture — PDP/PEP separation (decide vs enforce) *(OPA docs: Philosophy)*
    - Rego basics — rules and data documents as the policy language *(OPA docs: Policy Language)*
    - policy testing — unit tests that prove a policy allows/denies the right cases *(OPA docs: Policy Language)*
    - bundles & distribution — shipping policy to PEPs reproducibly *(OPA docs: Introduction)*
    - Trino-OPA integration — enforcing data access via the OPA plugin *(Trino docs: Security)*
    - Cedar as the typed alternative — when a typed policy language is preferable *(OPA docs: Philosophy)*
    - where policy-as-code wins — consistency, auditability, and CI for policies vs per-system grants *(OPA docs: Philosophy)*
- **Resources:**
    - **[Open Policy Agent documentation](https://www.openpolicyagent.org/docs/)** — Rego, the PDP/PEP philosophy, and policy testing (primary)
    - [Trino: Security](https://trino.io/docs/current/security.html) — the OPA access-control plugin you wire to enforcement (reference)
- **Tools:**
    - FOSS (hands-on): [OPA](https://www.openpolicyagent.org/docs/) — the policy engine and Rego (↔ Immuta policies, Apache Ranger, Cedar/AVP)
- **Do:**
    1. Express the fund-visibility policy from 11.1.2 in Rego.
    2. Write unit tests covering allow and deny cases.
    3. Enforce the policy for Trino via the OPA plugin.
    4. Change the policy in git, run tests, and watch enforcement follow.
- **Done when:**
    - [ ] Make a policy change as a reviewed PR with passing policy tests, not a ticket to three admins.
    - [ ] Show Trino enforcement reflects the latest Rego bundle.
- Est. hours: 3

#### 11.1.1 Identity providers & SSO — T2
- **Why:** every access decision starts with identity, so the architect wires platforms into the IdP and reads OIDC/SAML flows fluently. Get this wrong and group changes don't propagate, leavers keep access, and the audit question "who could see this in March?" has no defensible answer.
- **Learn:**
    - OIDC flows — auth code + PKCE for users, client credentials for services — vs SAML *(OpenID: How Connect Works)*
    - tokens — ID/access/refresh, claims, and audiences *(OpenID: How Connect Works)*
    - groups-to-roles mapping — turning an IdP group claim into in-tool roles *(Keycloak docs)*
    - SCIM provisioning — automated user lifecycle into downstream tools *(Keycloak docs)*
    - managed identities recap — service-to-service auth without secrets *(Keycloak docs)*
    - Keycloak realm/client model — the FOSS IdP's core objects *(Keycloak docs)*
- **Resources:**
    - **[Keycloak documentation](https://www.keycloak.org/documentation)** — realms, clients, OIDC, and group/role mapping for the hands-on lab (primary)
    - [OpenID Connect: How Connect Works](https://openid.net/developers/how-connect-works/) — the OIDC flow and token primer (reference)
- **Tools:**
    - FOSS (hands-on): [Keycloak](https://www.keycloak.org/documentation) — the IdP in front of your tools (↔ Entra ID, Okta)
    - Corp (evaluate): [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/) — the Azure primary IdP
- **Do:**
    1. Stand up Keycloak with a realm and clients for OpenMetadata, Grafana, and Trino (OIDC).
    2. Configure each tool to authenticate via Keycloak.
    3. Create a "data-steward" group and map its claim to in-tool roles.
    4. Add a user to the group and confirm all three tools update.
- **Done when:**
    - [ ] Move one identity's permissions across three tools with one group change.
    - [ ] Narrate the auth-code+PKCE token flow end to end.
- Est. hours: 3

#### 11.2.1 Encryption & key management — T2
- **Why:** "who controls the keys" is the question behind every cloud-data compliance review and the Schrems-flavoured sovereignty debate that EU fund firms must answer. Get key management wrong and either you cannot prove data is protected at rest, or a revoked key bricks a store you didn't realise depended on it.
- **Learn:**
    - envelope encryption — DEKs wrapped by KEKs wrapped by a vault key *(Practical Cloud Security: encryption)*
    - KMS hierarchies — key vault → KEK → DEK and where each lives *(Azure Key Vault docs)*
    - CMK vs platform-managed keys — what customer-managed keys actually buy (revocation, audit) and don't *(Azure Key Vault docs)*
    - TLS everywhere — encryption in transit as table stakes *(Azure Key Vault docs)*
    - key rotation mechanics — automated rotation and its blast radius *(Azure Key Vault docs)*
    - HSM tiers — Managed HSM vs standard vault for higher assurance *(Azure Key Vault docs)*
    - client-side encryption tradeoffs — it breaks query pushdown for analytics *(Azure Key Vault docs)*
- **Resources:**
    - **[Azure Key Vault documentation](https://learn.microsoft.com/en-us/azure/key-vault/)** — keys, secrets, CMK, rotation, and Managed HSM (primary)
    - [Practical Cloud Security, 2nd ed.](https://www.oreilly.com/library/view/practical-cloud-security/9781098148171/) — vendor-neutral envelope encryption, KMS hierarchies, and key-management practice (reference)
- **Do:**
    1. Inventory which Azure stores hold which data classes.
    2. Decide which stores get CMK vs platform-managed keys and justify each.
    3. Specify where keys live, rotation cadence, and the revocation drill.
    4. Document the analytics impact of any client-side encryption choice.
- **Done when:**
    - [ ] Answer "if we revoke the key, what actually happens and how fast?" per store.
    - [ ] Defend each CMK-vs-platform-managed decision in writing.
- Est. hours: 2

#### 11.3.1 + 11.3.2 Data masking & tokenization — T2
- **Why:** masking is how production-shaped fund data becomes usable in lower environments and how analysts see funds without seeing investors — a GDPR minimization requirement. Without referentially-consistent masking, dev runs on real PII (a breach) or on randomised data whose broken joins make every test result meaningless.
- **Learn:**
    - static vs dynamic masking — masking at rest vs masking in the query result *(SQL Server: Dynamic Data Masking)*
    - the technique zoo — redaction, substitution, shuffling, format-preserving encryption, vault tokenization *(Presidio docs)*
    - referential consistency — same investor → same token everywhere so joins survive *(Presidio docs)*
    - warehouse-native dynamic masking — built-in column masking and its inference limits *(SQL Server: Dynamic Data Masking)*
    - masking vs synthesis — when to mask vs generate synthetic data (ties 9.8.1) *(Presidio docs)*
- **Resources:**
    - **[SQL Server: Dynamic Data Masking](https://learn.microsoft.com/en-us/sql/relational-databases/security/dynamic-data-masking)** — warehouse-native dynamic masking, functions, and its inference caveats (primary)
    - [Microsoft Presidio](https://microsoft.github.io/presidio/) — anonymizer operators for deterministic tokenization and the technique zoo (reference)
- **Tools:**
    - FOSS (hands-on): [PostgreSQL](https://www.postgresql.org/docs/) views/functions + [Presidio](https://microsoft.github.io/presidio/) transforms (↔ Delphix, Protegrity, Immuta masking)
- **Do:**
    1. Build a masked replica of the Phase-1 investor tables using deterministic tokenization.
    2. Confirm the same investor maps to the same token across tables.
    3. Prove cross-table joins still resolve on masked data.
    4. Access-control the reversibility (only an authorised role can de-tokenize).
- **Done when:**
    - [ ] Run a full pipeline on masked data and produce correct aggregates with zero real PII downstream.
    - [ ] Demonstrate referential integrity holds and reversibility is access-controlled.
- Est. hours: 3

#### 11.4.1 PII detection & redaction (Presidio) — T2
- **Why:** you can't protect what you haven't found, and automated PII discovery feeds the classification tags that drive masking and access policy. Without it, free-text "client notes" or a new bronze feed lands with un-tagged national IDs and IBANs, and your masking/policy layer never knows to cover them.
- **Learn:**
    - detection approaches — regex/checksums, NER models, and context words *(Presidio docs)*
    - the analyzer/anonymizer pipeline — detect entities, then de-identify them *(Presidio docs)*
    - precision-recall tuning — adjusting recognizers for EU identifiers (IBANs, national IDs) *(Presidio docs)*
    - at-rest vs in-motion scanning — lake scans vs stream interception *(Presidio docs)*
    - classification tags into the catalog — findings flowing to OpenMetadata (ties 10.1.1, A.18) *(OpenMetadata docs: Governance)*
- **Resources:**
    - **[Microsoft Presidio documentation](https://microsoft.github.io/presidio/)** — analyzer/anonymizer, custom recognizers, and tuning (primary)
    - [OpenMetadata: Governance](https://docs.open-metadata.org/) — pushing PII findings as catalog classification tags (reference)
- **Tools:**
    - FOSS (hands-on): [Presidio](https://microsoft.github.io/presidio/) — PII detection and redaction (↔ Macie, GCP DLP, BigID, Purview classifiers)
- **Do:**
    1. Scan bronze plus a synthetic free-text "client notes" set with Presidio.
    2. Push findings as classification tags into the catalog.
    3. Tune one recognizer (Luxembourg phone or IBAN) and measure the precision change.
    4. Confirm tagged columns are picked up by the masking/access layer.
- **Done when:**
    - [ ] Show new PII landing in bronze gets discovered, tagged, and policy-covered without a human noticing it first.
    - [ ] Report the precision change from the tuned recognizer.
- Est. hours: 3

#### 11.6.1 Audit logging & SIEM — T2
- **Why:** "show me who accessed fund X's investor data in March" is a question you must answer from logs designed in advance, not reconstructed in panic during a CSSF inquiry. Without a planned audit taxonomy and tamper-evident retention, the answer is a forensic guess that satisfies no auditor.
- **Learn:**
    - audit-event taxonomy — access, policy change, export, admin events for a data platform *(pgAudit docs)*
    - per-engine query-log capture — Postgres pgAudit and the Trino event listener *(pgAudit docs)*
    - centralization & tamper-evidence — immutability and retention guarantees *(Microsoft Sentinel docs)*
    - the SIEM role — correlation and alerting in Sentinel/Splunk *(Microsoft Sentinel docs)*
    - KQL ties — querying centralized logs (ties A.5) *(Microsoft Sentinel docs)*
    - what auditors actually sample — the access and change events they request *(pgAudit docs)*
- **Resources:**
    - **[pgAudit](https://github.com/pgaudit/pgaudit)** — session and object audit logging for Postgres, the capture layer (primary)
    - [Microsoft Sentinel overview](https://learn.microsoft.com/en-us/azure/sentinel/overview) — the SIEM role: correlation, immutability, and KQL (reference)
- **Tools:**
    - FOSS (hands-on): [pgAudit](https://github.com/pgaudit/pgaudit) + [Trino event listener](https://trino.io/docs/current/develop/event-listener.html) + [Loki](https://grafana.com/docs/loki/latest/) (↔ Splunk, Sentinel, Elastic SIEM)
- **Do:**
    1. Enable pgAudit on Postgres and the event listener on Trino.
    2. Ship both audit streams to Loki with documented retention and immutability notes.
    3. Define the audit-event taxonomy you capture.
    4. Answer one "who touched what when" query end to end.
- **Done when:**
    - [ ] Make the March-access question a five-minute query with a documented chain of custody.
    - [ ] Show audit retention and immutability are configured and recorded.
- Est. hours: 2

#### 11.7.1 Regulatory & compliance frameworks (GDPR, DORA, and the fund stack) — T1
- **Why:** in Luxembourg financial services, regulation shapes architecture more than technology does, and the architect translates legal obligations into platform controls. Miss an obligation — an un-erasable record in Iceberg snapshots, a DORA incident path with no 4-hour reporting hook — and the platform is non-compliant by design, discovered only under examination.
- **Learn:**
    - GDPR for platform builders — lawful basis, minimization, purpose limitation, DSAR/erasure across Iceberg + backups + event logs, RoPA, DPIA triggers, processor chains & SCCs *(gdpr.eu guides)*
    - DORA — ICT risk framework, incident-reporting timelines, resilience testing, the ICT third-party register and exit strategies (cloud concentration) *(EIOPA: DORA)*
    - the fund regulatory stack — UCITS/AIFMD (incl. Annex IV), MiFID II product governance (→ EMT), PRIIPs (→ EPT/KID), SFDR (ESG data) at orientation level *(EIOPA: DORA)*
    - CSSF cloud-outsourcing expectations — notification and audit rights, aligned to EBA/ESMA guidelines (verify current circular at assembly) *(CSSF regulatory framework)*
    - SOC 2 / ISO 27001 — the vendor-evidence vocabulary you read in supplier reviews *(gdpr.eu guides)*
- **Resources:**
    - **[gdpr.eu](https://gdpr.eu/)** — practitioner guides on lawful basis, minimization, DSAR/erasure, and RoPA (primary)
    - [EIOPA: Digital Operational Resilience Act (DORA)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en) — ICT risk, incident reporting, and third-party register (reference)
    - [CSSF regulatory framework](https://www.cssf.lu/en/regulatory-framework/) — cloud-outsourcing circular (verify current circular number at assembly) (deepening)
- **Tools:**
    - Corp (awareness): [OneTrust](https://www.onetrust.com/) / Vanta-class compliance platforms — what they automate (RoPA, DSAR), at awareness level
- **Do:**
    1. List 12 concrete obligations spanning GDPR, DORA, and the fund stack (e.g. "DSAR erasure within 30 days", "DORA major-incident report in 4h", "AIFMD Annex IV quarterly").
    2. Map each obligation to an implemented or planned control on your platform.
    3. Design the erasure path concretely through Iceberg (snapshot expiry/compaction), backups, and Kafka.
    4. Flag gaps honestly where no control exists yet.
- **Done when:**
    - [ ] Brief a compliance officer on how the platform meets each obligation — and where it doesn't yet — without hand-waving.
    - [ ] Show the erasure path through Iceberg + backups + Kafka is concretely designed.
- Est. hours: 9

#### 1.12.12 DCAM (and leading a self-assessment) — T1
- **Why:** DCAM is the financial-services data-management capability model, and architects at fund firms are expected to *lead* assessments and turn scores into roadmaps the board funds. Without the ability to run an evidence-based DCAM assessment, "are we mature?" gets answered by opinion, and the resulting roadmap sequences work by politics rather than dependency.
- **Learn:**
    - DCAM v3 structure — 8 components and the required capabilities, scored on engagement/process/evidence *(EDM Council: DCAM)*
    - how assessments run — evidence-based scoring and stakeholder interviews *(EDM Council: DCAM)*
    - scores to roadmap — sequencing capabilities by dependency *(DAMA-DMBOK ch. 15)*
    - DCAM vs DMBOK — assessment model vs body of knowledge, with CDMC as the cloud profile (ties A.16) *(EDM Council: DCAM)*
    - what "evidence" means — the catalog/lineage/DQ artifacts you actually built in this plan *(DAMA-DMBOK ch. 15)*
- **Resources:**
    - **[EDM Council: DCAM](https://www.edmcouncil.org/frameworks/dcam)** — the v3 framework: components, capabilities, and the engagement/process/evidence scoring model (primary)
    - [DAMA-DMBOK (2nd ed.)](https://technicspub.com/dmbok/) ch. 15 (maturity assessment) — the open companion on running maturity assessments (reference)
- **Do:**
    1. Score your capstone platform across all 8 DCAM components, citing named evidence per capability.
    2. Use engagement/process/evidence dimensions consistently.
    3. Derive the 12-month capability roadmap the scores imply.
    4. Sequence the roadmap by dependency, not by ease.
- **Done when:**
    - [ ] Cite an artifact (catalog, lineage graph, DQ rulebook, ADR…) for every score.
    - [ ] Show the roadmap sequences capabilities by dependency, not vibes.
- Est. hours: 7

#### 9.8.1 Synthetic & test data — T2
- **Why:** privacy-preserving development is a GDPR minimization requirement, and synthetic data is its engineering answer when masking alone isn't enough. Over-fit synthesis leaks via membership inference, and broken referential integrity across synthesized tables makes the dev dataset useless — so the architect must own the fidelity-privacy tradeoff.
- **Learn:**
    - rule-based vs fitted synthesis — Faker fakes vs SDV statistical models (copulas/CTGAN) *(SDV docs)*
    - the fidelity-privacy tradeoff — and membership-inference risk in over-fitted synthesis *(SDV docs)*
    - referential integrity — multi-table synthesis that preserves keys across tables *(SDV docs)*
    - masking vs synthesis — when masking is the safer/simpler choice (ties 11.3) *(SDV docs)*
    - evaluating synthetic quality — fidelity/privacy metrics (SDMetrics) *(SDMetrics docs)*
- **Resources:**
    - **[SDV (Synthetic Data Vault) documentation](https://docs.sdv.dev/sdv/)** — single- and multi-table synthesis, synthesizers, and quality evaluation (primary)
    - [SDMetrics documentation](https://docs.sdv.dev/sdmetrics/) — fidelity and privacy metrics for evaluating synthetic data quality (reference)
- **Tools:**
    - FOSS (hands-on): [SDV](https://docs.sdv.dev/sdv/) + [Faker](https://faker.readthedocs.io/) — fitted synthesis plus rule-based fakes (↔ Mostly AI, Tonic, Gretel)
    - Corp (evaluate): [MOSTLY AI](https://mostly.ai/) — EU synthetic-data vendor; evaluate at build-vs-buy level
- **Do:**
    1. Fit an SDV multi-table synthesizer to the (masked) investor + orders tables.
    2. Generate a synthetic dev dataset preserving referential integrity.
    3. Compare aggregate fidelity against the real data with SDMetrics.
    4. Write the privacy argument (why it's safe to use in dev/test).
- **Done when:**
    - [ ] Run dev/test environments on data with a written justification of why it's safe.
    - [ ] Show referential integrity holds across the synthesized tables.
- Est. hours: 3

#### 10.1.2 Enterprise catalogs (Purview, Collibra) — T2
- **Why:** the buy side of the catalog decision matters because Purview is the Azure default and Collibra the EU-FS incumbent — you'll evaluate or inherit one and must judge it past the demo. Choose on features rather than connector coverage and stewardship workflow, and you buy a catalog that can't see half your estate or that nobody maintains.
- **Learn:**
    - Purview — Data Map scans, classification, glossary, and policy ambitions; M365/Azure integration strengths and lineage/cost gaps *(Microsoft Purview docs)*
    - Collibra — operating-model strength (workflows, stewardship) and implementation weight *(Collibra site)*
    - catalog TCO realities — connector coverage decides everything *(Microsoft Purview docs)*
    - migration/coexistence — open catalog alongside an enterprise catalog *(Collibra site)*
- **Resources:**
    - **[Microsoft Purview documentation](https://learn.microsoft.com/en-us/purview/)** — Data Map, classification, and the governance overview (primary)
    - [Collibra](https://www.collibra.com/) — operating model, stewardship workflows, and architecture overview (reference)
- **Do:**
    1. Build a connector-coverage table for your estate across OpenMetadata, Purview, and Collibra.
    2. Sketch a TCO comparison for a 300-person fund administrator.
    3. Write the vendor-selection memo with a clear recommendation.
- **Done when:**
    - [ ] Name the deciding factor (almost always connector coverage + stewardship workflow, not features).
    - [ ] Produce a memo a sponsor could act on.
- Est. hours: 3

#### 10.7.1 Retention & lifecycle — T2
- **Why:** regulated retention (10-year fund records) and GDPR minimization pull in opposite directions, and lifecycle design is where the architect reconciles them. Without per-class retention that actually deletes across snapshots, backups, and logs, you either keep PII too long (GDPR breach) or expire records a regulator still expects (CSSF breach).
- **Learn:**
    - retention-schedule design by record class — orders vs NAV vs KYC vs logs (ties A.19) *(Azure Blob lifecycle docs)*
    - storage-tier lifecycle — hot → cool → archive economics *(Azure Blob lifecycle docs)*
    - legal hold vs deletion pipelines — suspending deletion when required *(Azure Blob lifecycle docs)*
    - Iceberg snapshot expiry vs business retention — different layers, different controls *(Iceberg docs: expire_snapshots)*
    - deletion that actually deletes — compaction, backups, and logs all cleared *(Iceberg docs: expire_snapshots)*
- **Resources:**
    - **[Azure Blob: lifecycle management](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-overview)** — tiering and deletion policies by rule (primary)
    - [Apache Iceberg: expire_snapshots](https://iceberg.apache.org/docs/latest/spark-procedures/) — snapshot expiry and table maintenance procedures (reference)
- **Tools:**
    - FOSS (hands-on): [MinIO lifecycle](https://min.io/docs/minio/linux/administration/object-management/object-lifecycle-management.html) + [Iceberg maintenance](https://iceberg.apache.org/docs/latest/maintenance/) — tiering and snapshot expiry
- **Do:**
    1. Write the retention schedule for five record classes (orders, NAV, investor KYC, logs, EMT outputs).
    2. Implement it as MinIO lifecycle rules plus Iceberg maintenance jobs (expire_snapshots, remove orphan files).
    3. Account for legal hold and for deletion across backups and logs.
- **Done when:**
    - [ ] Answer "when does this data actually disappear, everywhere?" with a per-class answer you can prove.
    - [ ] Show Iceberg snapshot expiry and storage-tier rules are both configured.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 3.2.5 | Property graph databases | Neo4j/Cypher for relationship-heavy ops use (fraud rings, ownership chains) | [Neo4j: Getting Started](https://neo4j.com/docs/getting-started/current/) | 25 |
| 7.3.2 | Glossary embedded in catalogs | Same discipline as 7.3.1, delivered as a feature of Collibra/Purview | [covered by 10.1.2 reading](https://learn.microsoft.com/en-us/purview/) | 10 |
| 9.8.2 | Test data management | Subset/mask/refresh tooling (Delphix-class) for legacy estates | [Delphix (Perforce) test data management](https://www.perforce.com/products/delphix) | 20 |
| 10.2.1 | AI-native data discovery | LLM-assisted search and Q&A over catalog metadata | [Atlan AI](https://atlan.com/atlan-ai/) | 20 |
| 10.2.2 | Catalog-embedded discovery | Search/browse UX delivered as a catalog feature | [covered by 10.1.1 hands-on](https://docs.open-metadata.org/) | 10 |
| 10.3.2 | Lineage embedded in catalogs | Lineage as a catalog feature vs the open OpenLineage standard | [covered by 10.1.1/10.3.1](https://openlineage.io/docs/) | 10 |
| 10.5.2 | Modern/cloud MDM | ML-first MDM (Tamr) and lighter cloud MDM (Reltio) | [Tamr product overview](https://www.tamr.com/) | 20 |
| 10.6.2 | RDM inside MDM suites | Code-list management bundled into MDM products | [covered by 10.6.1 reading](https://technicspub.com/dmbok/) | 10 |
| 10.7.2 | Enterprise ILM suites | Heavyweight lifecycle tooling (Veritas/IBM) in legacy estates | [Veritas information lifecycle](https://www.veritas.com/) | 15 |
| 11.2.2 | Database encryption / TDE | At-rest encryption inside the engine; table stakes, rarely a decision | [SQL Server: Transparent Data Encryption](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption) | 20 |
| 11.5.1 | Privacy/consent platforms | OneTrust-class consent and DSAR automation | [OneTrust product overview](https://www.onetrust.com/) | 20 |
| 14.7.1 | Anomaly alerting | DQ/observability-triggered alerting; implemented via Elementary above | [covered by 10.9.x hands-on](https://docs.elementary-data.com/) | 10 |

*T3 subtotal: 3 h*

### Capstone 6 — The governed platform (catalog, lineage, DQ, policy, DCAM)

- **Goal:** wrap the entire platform in a working control plane and prove it to an imaginary auditor: every asset owned and classified, every number traceable, every access decision policy-driven, every obligation mapped.
- **Stack (100% free):** [OpenMetadata](https://docs.open-metadata.org/) (↔ Purview/Collibra), [OpenLineage](https://openlineage.io/docs/) + [Marquez](https://marquezproject.ai/) (↔ Purview/Manta lineage), [Soda Core](https://docs.soda.io/) + [Great Expectations](https://docs.greatexpectations.io/) + [Elementary](https://docs.elementary-data.com/) (↔ Informatica DQ / Monte Carlo), [Splink](https://moj-analytical-services.github.io/splink/) + [Postgres](https://www.postgresql.org/docs/) security master (↔ Informatica MDM / Semarchy), [Keycloak](https://www.keycloak.org/documentation) (↔ Entra ID), [OPA](https://www.openpolicyagent.org/docs/) + [Trino rules](https://trino.io/docs/current/security.html) + [Postgres RLS](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) (↔ Immuta/Privacera), [Presidio](https://microsoft.github.io/presidio/) (↔ Macie/Purview classifiers), [pgAudit](https://github.com/pgaudit/pgaudit) + [Loki](https://grafana.com/docs/loki/latest/) (↔ Sentinel/Splunk), [SDV](https://docs.sdv.dev/sdv/) (↔ Mostly AI), [Apache Jena/Fuseki](https://jena.apache.org/documentation/fuseki2/) FIBO/GLEIF slice (↔ Stardog/GraphDB).
- **Build:** (1) catalog ingests every platform component; owners/tiers/classifications complete for gold; (2) end-to-end lineage for the EMT path, demonstrable; (3) DQ rulebook live in the WAP gate + Elementary anomaly watch; (4) security master publishing golden records with steward-explainable merges; (5) fund-visibility policy enforced via RLS + OPA-Trino from one Rego source, identities from Keycloak; (6) PII auto-discovered → tagged → masked replica for dev; (7) audit trail answering the "March access" question; (8) the obligation→control matrix (11.7.1) and the DCAM self-assessment + roadmap (1.12.12) as governing documents.
- **Architecture deliverables:** C4 updated with the control plane; ADR-016 catalog selection (open vs Purview vs Collibra), ADR-017 enforcement architecture (where policy is decided vs enforced, and residual bypass risk), ADR-018 MDM style for the security master (registry vs centralized).
- **Acceptance criteria:** the auditor drill passes: pick any number in the EMT output → lineage to sources, owner, DQ status, access policy, and audit log, each in minutes; a seeded DQ failure blocks publish and reaches the catalog; the same policy change propagates to both enforcement layers via one PR; DCAM scores all cite artifacts; obligation matrix has zero unexamined rows (gaps allowed, but named). Capture each as evidence (screenshots/queries) for the DCAM pack.
- Est. hours: 16

*Phase 6 total: 120 h (T1/T2 entries 101 h + T3 3 h + capstone 16 h) + Appendix A items A.14–A.20 (14 h) scheduled in this phase*


<a id="phase-7"></a>
## Phase 7: AI/ML & LLM Platforms for Fund Data (months 40–43, 74 h + 7 h Appendix A)

*Phase 7 of 8 · months 40–43 · 81 h (74 h + 7 h Appendix A) · capstone: LLM extraction of fund documents.*  ← [Phase 6](#phase-6) · [Phase 8](#phase-8) →

**Goal:** working-level command of the ML/LLM platform stack from the *data architect's* seat: the lifecycle (MLflow), feature serving, vector storage, RAG over fund documents, and — critically for regulated use — evaluation and tracing. Depth is deliberately T2/T3: you architect the platform ML teams run on; you don't compete with them on modeling.
**Entry prerequisites:** Phases 2–6 (lakehouse, orchestration, governance — ML platforms inherit all of it). No ML-theory prerequisite: this phase targets platform-architecture depth, not modeling depth — the entries stay at the intuition level, and each resource is self-contained.
**Exit criteria:** you can (1) design the MLOps lifecycle on your platform with registry, tracking, and promotion gates; (2) choose vector storage and defend hybrid search for RAG; (3) build and *evaluate* an LLM extraction pipeline over fund documents; (4) tell a CIO what LLMOps controls a regulated deployment needs (traces, evals, human gates) and show them running.
**Appendix A items scheduled here:** A.21 LLM agent patterns & prompt engineering, A.23 Model Context Protocol, A.24 LLM application security (7 h).

### T1/T2 topics

#### 6.4.1 MLOps platforms & the ML lifecycle (MLflow) — T2
- **Why:** the registry/tracking/promotion lifecycle is the governance pattern of ML — and the architect owns how it plugs into the data platform, lineage, and audit. Without it, a fund platform ships model changes with no approval trail, and "which model version produced this NAV-impacting forecast?" becomes unanswerable — exactly the question a model-risk validator or CSSF inspector will ask first.
- **Learn:**
    - ML system anatomy — data → features → training → registry → serving → monitoring, and where each stage touches *your* lakehouse, orchestrator, and lineage graph *(DMLS ch. 1–2)*
    - experiment tracking — runs, params, metrics, and artifacts as the audit trail of model development (6.7.1 lives here) *(MLflow docs: Tracking)*
    - model registry & packaging — versions, stages/aliases, pyfunc flavors, and the approval workflow that makes promotion a governed event *(MLflow docs: Model Registry)*
    - drift — data drift vs concept drift, the monitoring signals that detect each, and what triggers retraining *(DMLS ch. 8)*
    - model risk management vocabulary for finance — SR 11-7 / ECB TRIM awareness: model inventory, owners, independent validation; ML models join the same inventory as pricing models *(SR 11-7 letter)*
- **Resources:**
    - **[Designing Machine Learning Systems (Chip Huyen)](https://huyenchip.com/books/) ch. 1–2, 7–9** — system anatomy, deployment, monitoring and drift; skim the deep-modeling middle (primary)
    - [MLflow docs: Tracking](https://mlflow.org/docs/latest/ml/tracking/) — runs, experiments, logging APIs; the hands-on half (reference)
    - [MLflow docs: Model Registry](https://mlflow.org/docs/latest/ml/model-registry/) — versions, aliases/stages, lineage and promotion workflow (reference)
    - [SR 11-7: Guidance on Model Risk Management](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.htm) — the canonical model-risk vocabulary regulators borrow from (deepening)
- **Tools:**
    - FOSS (hands-on): [MLflow](https://mlflow.org/docs/latest/) — tracking server + registry self-hosted on your platform (↔ Azure ML registry, SageMaker, W&B)
    - Corp (evaluate): [Azure ML](https://learn.microsoft.com/en-us/azure/machine-learning/) — evaluated properly in the next entry (6.4.2)
- **Do:**
    1. Stand up MLflow on the platform (`uv run mlflow server` with a Postgres backend store and a local artifact root) and confirm the UI is reachable.
    2. Build a small fund-flow forecasting experiment — an sklearn regressor over monthly subscription/redemption flows — and track 4–6 runs with different params, logging metrics and the model artifact each time.
    3. Compare runs in the UI; register the winning model in the registry with a version and description of its training data window.
    4. Define a written promotion gate from Staging→Production: a metric threshold plus a named human approver; record the approval as registry tags/aliases so it is queryable.
    5. Drill: starting from the Production alias alone, walk back to the exact run, params, data window, and approver — time yourself.
- **Done when:**
    - [ ] Answer "which model version produced this number, trained on what data, approved by whom?" from the registry alone — the model-governance analogue of your lineage drill.
    - [ ] Sketch the six lifecycle stages from memory and name where each touches your lakehouse and orchestrator.
    - [ ] Explain to a risk officer how the MLflow registry maps onto an SR 11-7-style model inventory (model, owner, validation evidence).
- Est. hours: 10

#### 6.4.2 Managed MLOps (Azure ML) — T2
- **Why:** Azure ML is what your employer likely already licenses; you must map open concepts onto it for build-vs-buy and audit conversations. An architect who can't say where Azure ML overlaps with the Dagster+MLflow stack ends up running two orchestrators and two registries — double cost, split audit trail.
- **Learn:**
    - workspaces, compute targets, environments — the resource model, and how Entra RBAC and networking attach to each *(Azure ML docs: concepts)*
    - Azure ML pipelines vs your Dagster — where they overlap, where they fight, and who should orchestrate whom *(Azure ML docs: Build & train models)*
    - model registry + endpoints — online vs batch endpoints, deployments under an endpoint, safe rollout via traffic split *(Azure ML docs: Endpoints)*
    - responsible-AI dashboard positioning — what it offers a regulated buyer and what it doesn't prove *(Azure ML docs: concepts)*
    - cost profile — compute, managed endpoints, and what idles expensively when the team goes home *(Azure ML pricing)*
    - where managed adds value vs constrains — managed endpoints and RBAC integration vs OSS-on-AKS flexibility and portability *(Azure ML docs: Endpoints)*
- **Resources:**
    - **[Azure Machine Learning documentation](https://learn.microsoft.com/en-us/azure/machine-learning/)** — concepts section: workspaces, compute, pipelines, responsible AI (primary)
    - [Azure ML: Endpoints for inference](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints) — online/batch endpoints and deployment model (reference)
    - [Azure ML: Build & train models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-machine-learning-model) — training methods and pipelines, for the Dagster-overlap question (reference)
    - [Azure ML pricing](https://azure.microsoft.com/en-us/pricing/details/machine-learning/) — the cost rows of your build-vs-buy table (reference)
- **Do:**
    1. List every Capstone-7 component (tracking, registry, serving, orchestration, vector store, evals, tracing) down the left of a one-page table.
    2. Map each to its Azure ML (or adjacent Azure service) equivalent, reading the concepts and endpoints docs as you go.
    3. Add a build-vs-buy verdict per row with a one-line justification — cost, RBAC integration, lock-in, or ops burden.
    4. Note the two places Azure ML pipelines and Dagster would fight over orchestration, and state your boundary rule (e.g. Dagster owns data, Azure ML owns training jobs).
- **Done when:**
    - [ ] Brief a platform team on what changes (and what doesn't) if they adopt Azure ML.
    - [ ] Name where Azure ML adds value over OSS-on-AKS (managed endpoints, RBAC) and where it constrains.
    - [ ] State which components you would keep open-source even with an Azure ML licence, and defend each in one sentence.
- Est. hours: 4

#### 6.1.1 Feature stores (Feast) — T2
- **Why:** the online/offline consistency problem is the architecturally interesting part of ML serving — and feature stores are a frequent (often premature) vendor pitch you must evaluate. Get point-in-time correctness wrong and the churn model trains on data it could never have seen at scoring time; buy a feature store for a batch-only fund workload and you've added an online database nobody queries.
- **Learn:**
    - offline vs online stores — training reads months of history from the lakehouse, serving needs millisecond lookups by entity key *(Feast docs: concepts)*
    - point-in-time-correct joins — the training-serving skew killer; your SCD2 instincts apply directly *(Feast docs: Point-in-time joins)*
    - feature definitions as code — entities, feature views, TTLs in versioned Python, reviewable like dbt models *(Feast docs: concepts)*
    - materialization — pushing offline values into the online store on a schedule, and the freshness window that implies *(Feast docs: concepts)*
    - when a feature store is overkill — batch-only scoring (most fund use cases!) needs none of the online machinery *(Tecton/Databricks: What is a feature store)*
- **Resources:**
    - **[Feast documentation](https://docs.feast.dev/)** — concepts: entities, feature views, offline/online stores, materialization (primary)
    - [Feast docs: Point-in-time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) — the exact mechanism you will demonstrate hands-on (reference)
    - [What is a feature store? (Tecton, now Databricks)](https://www.databricks.com/glossary/what-is-a-feature-store) — the vendor framing and components; useful for spotting the buy-side pitch (deepening)
- **Tools:**
    - FOSS (hands-on): [Feast](https://docs.feast.dev/) on [PostgreSQL](https://www.postgresql.org/docs/)/[Redis](https://redis.io/docs/) (↔ Databricks/Tecton/SageMaker feature stores)
    - Corp (evaluate): [Databricks Feature Store](https://docs.databricks.com/) / [SageMaker Feature Store](https://docs.aws.amazon.com/sagemaker/) — what the managed pitch adds: serving SLAs, lineage UI, monitoring
- **Do:**
    1. Define three fund features in Feast over your lakehouse — 30-day flow volatility, investor churn signal, NAV staleness — as entities + feature views with explicit TTLs, committed as code.
    2. Build a training set with `get_historical_features` for a list of (investor, event_timestamp) rows — the point-in-time-correct path.
    3. Build the same training set with a naive latest-value SQL join; diff the two outputs and isolate the rows where the naive join pulled future data past the event timestamp.
    4. Materialize to the online store and fetch the three features for one investor at serving time, noting the freshness lag.
    5. Write a short verdict note: which fund use cases justify an online store, and the conditions under which you'd veto a feature-store purchase.
- **Done when:**
    - [ ] Show concretely how the naive join leaks future data, and state when you'd veto a feature-store purchase.
    - [ ] Explain point-in-time correctness to a data engineer in SCD2 terms (effective-dated lookups, not latest-value).
    - [ ] Name the fund workloads where batch scoring makes the online store unnecessary, and the one that wouldn't.
- Est. hours: 5

#### 1.1.4 + 3.2.9 Vector data & vector storage — T2
- **Why:** embeddings are a new first-class data type in your storage portfolio; the "dedicated vector DB vs pgvector vs search-engine hybrid" decision is today's recurring architecture question. Decide it on vendor slides instead of your own recall/latency numbers and you either buy a cluster Postgres could have replaced, or strand the RAG workload on an index that can't filter by fund family at scale.
- **Learn:**
    - embeddings as learned features — a first-class data type with its own storage, indexing, and lifecycle demands *(Qdrant docs)*
    - ANN indexing — HNSW graph intuition vs IVF lists, and the recall–latency–memory triangle every index trades within *(Qdrant docs: Indexing)*
    - pgvector — HNSW/IVFFlat index types, distance operators, and combining vector search with ordinary WHERE filters *(pgvector README)*
    - dedicated stores vs Postgres vs hybrid engines — the convergence note from the taxonomy: keyword+vector reranked is the RAG default *(Qdrant docs)*
    - metadata filtering at scale — pre- vs post-filtering, and why filterable HNSW is the hard part vendors compete on *(Qdrant docs: Indexing)*
    - vector data lifecycle — re-embedding on model change is a lineage and pipeline problem, not a one-off script *(Qdrant docs)*
- **Resources:**
    - **[pgvector README](https://github.com/pgvector/pgvector)** — index types, distance ops, filtering, tuning; everything for the Postgres half (primary)
    - [Qdrant documentation](https://qdrant.tech/documentation/) — collections, payload filtering, hybrid queries; the dedicated-store half (reference)
    - [Qdrant docs: Indexing](https://qdrant.tech/documentation/concepts/indexing/) — HNSW parameters and filterable-index internals behind your benchmark (deepening)
- **Tools:**
    - FOSS (hands-on): [pgvector](https://github.com/pgvector/pgvector) + [Qdrant](https://qdrant.tech/documentation/) (↔ [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/) vectors, Pinecone)
    - Corp (evaluate): [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) — the managed convergence play, evaluated in 6.6.3
- **Do:**
    1. Embed 1k fund-document chunks with a sentence-transformers model (the 6.6.1/6.6.2 corpus or any public KIDs).
    2. Load the same vectors + metadata (fund family, language, doc type) into Postgres+pgvector and into Qdrant; build an HNSW index in each.
    3. Benchmark filtered top-k ("top-10 within fund family X"): measure latency and recall against an exact-scan baseline; vary one HNSW parameter (`ef_search` or `m`) and record how the recall–latency point moves.
    4. Write the 10-line "when does Postgres suffice" verdict, citing your own numbers and the filtering behaviour you observed.
- **Done when:**
    - [ ] Defend "pgvector until proven otherwise" — or its rejection — with your own numbers.
    - [ ] Explain the recall–latency–memory triangle and what HNSW's parameters trade against each other.
    - [ ] State why an embedding-model change forces a full re-embed and how your pipeline (and lineage) would handle it.
- Est. hours: 7

#### 6.6.1 Embedding models — T2
- **Why:** embedding choice quietly determines retrieval quality, cost, and re-indexing burden — an architect decision dressed as a detail. Pick an English-only API model for a Luxembourg corpus and the French KIDs silently retrieve garbage, while every model upgrade triggers an unbudgeted full re-index through a third-country API.
- **Learn:**
    - local sentence-transformers vs API embeddings — the cost/latency/sovereignty triangle; EU data residency applies to embeddings too! *(Azure OpenAI data privacy)*
    - dimensionality tradeoffs — vector width drives storage and ANN latency; bigger is not reliably better *(sentence-transformers docs)*
    - domain fit for financial text — multilingual reality (French/English) and finance vocabulary beat leaderboard rank *(sentence-transformers docs)*
    - versioning embeddings — model change = full re-index = a pipeline design issue; pin model name+version next to the vectors *(sentence-transformers docs)*
    - MTEB as a (gameable) benchmark — shortlist with it, decide with your own retrieval set *(MTEB leaderboard)*
- **Resources:**
    - **[Sentence-Transformers documentation](https://www.sbert.net/)** — usage, pretrained multilingual models, semantic-search examples (primary)
    - [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) — model shortlisting; read skeptically (reference)
    - [Azure OpenAI: data, privacy, and security](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy) — what API embeddings mean for EU residency and data processing (deepening)
- **Tools:**
    - FOSS (hands-on): [sentence-transformers](https://www.sbert.net/) (↔ OpenAI/Cohere/Voyage embedding APIs, [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/) embeddings)
- **Do:**
    1. Shortlist one local multilingual model (from the sbert pretrained list, MTEB-informed) and one API embedding model; record dimensions, licence, and published price.
    2. Write 20 fund-domain retrieval queries in a French/English mix — Luxembourg reality (NAV, SRI, frais courants, ISIN lookups).
    3. Embed corpus and queries with the local model and measure hit-rate@k; for the API model, tabulate cost-per-million-tokens and residency/processing terms from its documentation.
    4. Tabulate quality/cost/residency side by side; pick a model and write the re-embedding strategy: trigger, batch re-index job, dual-write or cutover window.
- **Done when:**
    - [ ] Your pick comes with a stated re-embedding strategy and a data-residency position.
    - [ ] Explain why MTEB rank alone would have been a bad selection method for this corpus.
    - [ ] Show how the French queries changed (or would change) the model choice versus English-only evaluation.
- Est. hours: 4

#### 6.6.2 RAG frameworks & architecture — T2
- **Why:** RAG is the dominant enterprise LLM pattern and a *data architecture* problem at heart: ingestion, chunking, indexing, retrieval, and freshness are your home turf. Skip the retrieval-quality discipline and the system confidently cites the wrong fund's fee table — in a KID-extraction workflow that's a mis-sold product, not a typo.
- **Learn:**
    - RAG anatomy — load → chunk → embed → index → retrieve (hybrid + rerank) → generate with citations; each stage is a pipeline stage you already know how to govern *(LlamaIndex docs)*
    - chunking strategies and their failure modes — fixed-size vs structure-aware on structured PDFs like KIDs; tables are where naive chunking dies *(LlamaIndex docs)*
    - hybrid retrieval + reranking — BM25 and vectors fused, then reranked; the enterprise default, not an optimization *(Building AI for Production: RAG chapters)*
    - framework positioning — LlamaIndex vs Haystack vs LangChain, and the framework-fatigue caution: thin frameworks, strong pipelines *(Haystack docs)*
    - structured extraction — schema-constrained output (Pydantic-validated) as the capstone pattern *(LlamaIndex docs)*
    - document parsing reality — PDF tables and multi-column layouts; parser choice moves quality more than the LLM does *(Building AI for Production: RAG chapters)*
    - freshness pipeline — document updates → re-chunk → re-index, owned by your orchestrator like any other source *(LlamaIndex docs)*
- **Resources:**
    - **[LlamaIndex documentation](https://docs.llamaindex.ai/)** — RAG concepts, loading/chunking, retrievers, structured extraction (primary)
    - [Building AI for Production (*Building LLMs for Production*, 2nd ed.)](https://towardsai.net/book) — RAG chapters: chunking, hybrid retrieval, production hardening (alternate)
    - [Haystack documentation](https://docs.haystack.deepset.ai/) — a second, pipeline-first framework for the positioning comparison (reference)
- **Tools:**
    - FOSS (hands-on): [LlamaIndex](https://docs.llamaindex.ai/) + [Ollama](https://ollama.com/) for local models (↔ [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/) + [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/), Bedrock KBs)
- **Do:**
    1. Collect 30 public fund KIDs/prospectuses (EN/FR mix); parse with two different PDF parsers and compare how each handles the fee/SRI tables.
    2. Implement two chunking strategies — fixed-size with overlap vs structure-aware sections — and index both variants into your 1.1.4 vector store.
    3. Hand-write 20 questions with known answers (the seed of the 6.8.2 golden set); measure retrieval hit-rate@k per chunking strategy, before any generation.
    4. Add hybrid retrieval (BM25 + vector, fused) with source-span citations; remeasure hit-rate and record the delta.
    5. Write down which single decision (parser, chunking, hybrid) moved retrieval quality most, with numbers.
- **Done when:**
    - [ ] Show retrieval quality numbers (not vibes) and explain which chunking decision moved them most.
    - [ ] Defend why retrieval is measured before generation, to a colleague who wants to "just eval the answers".
    - [ ] Sketch the freshness pipeline (document update → re-chunk → re-index) as a Dagster job over your existing assets.
- Est. hours: 10

#### 6.6.3 Managed RAG platforms — T2
- **Why:** "just use Azure AI Search + OpenAI" is the default corp pitch; you need its real capability/cost envelope versus your open pipeline. Without that envelope you either pay the semantic-ranker meter for a corpus pgvector served fine, or reject the one managed feature (security trimming) your compliance team actually needed.
- **Learn:**
    - the Azure AI Search hybrid stack — vector + keyword in one query, RRF fusion, semantic ranker on top *(Azure AI Search docs: vector search)*
    - integrated vectorization — chunking and embedding inside the indexer pipeline: convenience bought with opacity *(Azure AI Search docs: vector search)*
    - security trimming — ACL-aware retrieval via identity filters; the enterprise killer feature for investor-restricted documents *(Azure AI Search docs: security trimming)*
    - semantic ranker mechanics and pricing — reranking the top-50 with Microsoft's models, billed by usage *(Azure AI Search docs: semantic ranking)*
    - Bedrock KBs / Vertex Search equivalents at a glance — the same managed trade on other clouds *(Amazon Bedrock docs)*
    - what managed buys vs costs — ops and security integration vs lock-in and chunking opacity *(Azure AI Search docs: vector search)*
- **Resources:**
    - **[Azure AI Search: vector search overview](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)** — hybrid scenarios, integrated vectorization, pricing notes (primary)
    - [Azure AI Search: semantic ranking overview](https://learn.microsoft.com/en-us/azure/search/semantic-search-overview) — how the reranker works and what it's billed on (reference)
    - [Azure AI Search: security filter pattern](https://learn.microsoft.com/en-us/azure/search/search-security-trimming-for-azure-search) — the ACL-trimming mechanism your eval must address (reference)
    - [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/) — Knowledge Bases as the AWS counterpart, glance level (deepening)
- **Do:**
    1. Read the three Azure AI Search pages and sketch the managed pipeline (indexer → skillset → index → semantic ranker) side by side with your open 6.6.2 pipeline.
    2. Write the one-page eval: open RAG stack vs Azure AI Search for the fund-document corpus — rows for capability, cost, ops burden, chunking control, lock-in.
    3. Treat the ACL-trimming requirement explicitly: how each side enforces "investor-restricted documents are never retrieved for the wrong user", and what your open stack would have to build.
    4. Conclude with the single requirement that flips the decision either way, stated in one sentence.
- **Done when:**
    - [ ] Name the one requirement (usually security trimming or ops) that flips the decision either way.
    - [ ] Explain what integrated vectorization hides and why that matters when retrieval quality degrades.
    - [ ] State the semantic ranker's pricing model and when it's worth turning on for this corpus.
- Est. hours: 3

#### 6.8.1 LLM tracing & prompt management (Langfuse) — T2
- **Why:** regulated LLM use without traces is unauditable; prompt/version/trace capture is the LLMOps analogue of your lineage work. Without it, "what exactly did the model see when it extracted this SRI value?" has no answer, and an untracked prompt edit can silently change extraction behaviour across the whole corpus.
- **Learn:**
    - the trace model — traces, spans, generations: every LLM call tied to its inputs, outputs, and pipeline context *(Langfuse docs: Tracing)*
    - prompt versioning & rollout — prompts as managed, versioned artifacts fetched at runtime, with labels for staged rollout and rollback *(Langfuse docs: Prompt Management)*
    - cost/latency telemetry — per-call token and cost capture, aggregated for chargeback and SLOs *(Langfuse docs: Tracing)*
    - PII handling in traces — don't log what you masked elsewhere!; masking hooks before persistence *(Langfuse docs: Tracing)*
    - user feedback capture — reviewer scores attached to traces become tomorrow's eval data for 6.8.2 *(Langfuse docs: Tracing)*
- **Resources:**
    - **[Langfuse documentation](https://langfuse.com/docs)** — tracing model, SDK instrumentation, scores/feedback, self-hosting (primary)
    - [Langfuse docs: Prompt Management](https://langfuse.com/docs/prompts) — versioning, labels, runtime fetching (reference)
- **Tools:**
    - FOSS (hands-on): [Langfuse](https://langfuse.com/docs) self-hosted (↔ [LangSmith](https://docs.smith.langchain.com/), [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/) tracing)
- **Do:**
    1. Self-host Langfuse (docker compose) next to the RAG pipeline and create a project + API keys.
    2. Instrument the 6.6.2 pipeline: one trace per question, spans for retrieval and generation, with model name, token counts, and cost metadata on each generation.
    3. Move the extraction prompt into Langfuse prompt management; create a v2 with a deliberate wording change and fetch it by label at runtime.
    4. Run the 20-question set under both prompt versions; compare cost and answer quality per version straight from the traces.
    5. Configure masking so investor names and other PII never reach the stored traces; verify by inspecting raw traces in the UI.
- **Done when:**
    - [ ] "What exactly did the model see and answer for document X last Tuesday?" is a lookup, not a mystery.
    - [ ] Show two prompt versions with a cost/quality comparison derived from traces, not from memory.
    - [ ] Demonstrate that masked fields appear nowhere in the trace store.
- Est. hours: 4

#### 6.8.2 LLM evaluation (Ragas, golden sets) — T2
- **Why:** evaluation is the control that makes LLM extraction defensible in a regulated workflow — without it you have a demo, not a system. No golden set and no CI gate means a prompt tweak can drop ISIN extraction accuracy for weeks before anyone notices, and the discovery will be made by a transfer agent, not by you.
- **Learn:**
    - eval layers — retrieval metrics (precision/recall@k), generation metrics (faithfulness, answer relevancy), and *task* metrics (field-level extraction accuracy vs golden set — the one that matters here) *(Ragas docs: metrics)*
    - LLM-as-judge caveats — bias, drift, cost; align the judge against human labels before trusting it *(Hamel Husain: evals)*
    - building golden datasets — your BA skills, weaponized: sampling, labeling discipline, synthetic testset generation as a bootstrap *(Ragas docs: testset generation)*
    - eval-in-CI — regression gates so a prompt or model change that degrades quality fails the build, like any other test *(DeepEval docs)*
    - human-in-the-loop sampling design — what humans review, at what rate, where the outcome is recorded *(Hamel Husain: evals)*
- **Resources:**
    - **[Ragas documentation](https://docs.ragas.io/en/stable/)** — metrics (faithfulness, relevancy, precision/recall) + testset generation (primary)
    - [DeepEval documentation](https://deepeval.com/docs/getting-started) — pytest-style LLM assertions and CI integration (reference)
    - [Hamel Husain: Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) — the three-level eval system, LLM-as-judge discipline, human review loops (deepening)
- **Tools:**
    - FOSS (hands-on): [Ragas](https://docs.ragas.io/en/stable/)/[DeepEval](https://deepeval.com/docs/getting-started) + [pytest](https://docs.pytest.org/) (↔ [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/) evaluation SDK, [LangSmith](https://docs.smith.langchain.com/) evals)
- **Do:**
    1. Hand-build a 50-field golden set from 10 KIDs — SRI, ongoing costs, ISIN, currency, recommended holding period — stored as versioned YAML/CSV beside the code.
    2. Write a field-accuracy eval (exact or normalized match per field) over the extraction pipeline, plus a Ragas faithfulness eval over the generated answers.
    3. Wire both into CI with pytest/DeepEval and an explicit threshold, so a run below threshold fails the build.
    4. Deliberately degrade the prompt (drop one extraction instruction); confirm CI catches the regression and the failing fields are identifiable.
    5. Write one paragraph per metric on its blind spot — e.g. faithfulness can score high while the extracted field is still wrong.
- **Done when:**
    - [ ] A deliberately degraded prompt is caught by CI before a human would have noticed — and you can explain each metric's blind spot.
    - [ ] Defend field-level accuracy as the primary metric for this workload, over generic generation scores.
    - [ ] State your human-review sampling rate and what triggers escalation to full review.
- Est. hours: 6

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 3.2.8 | Search engines | Inverted-index/BM25 stores (Elasticsearch/OpenSearch); the keyword half of hybrid RAG and of log search | [OpenSearch docs: Intro to OpenSearch](https://docs.opensearch.org/latest/getting-started/intro/) | 30 |
| 6.1.2 | Managed feature stores | Tecton/Databricks/SageMaker FS — buy-side of 6.1.1 (Tecton now part of Databricks) | [Tecton: what is a feature store (now Databricks)](https://www.databricks.com/glossary/what-is-a-feature-store) | 20 |
| 6.2.1 | Training frameworks | PyTorch/sklearn/XGBoost — the ML team's tools; you read, not write | [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) | 25 |
| 6.2.2 | Distributed training | Multi-GPU/node training (DeepSpeed/Ray Train); HPC-adjacent, out of role | [Ray Train overview](https://docs.ray.io/en/latest/train/train.html) | 15 |
| 6.2.3 | Managed training | Azure ML/SageMaker training jobs; covered conceptually in 6.4.2 | [Azure ML: build & train models](https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-machine-learning-model) | 15 |
| 6.3.1 | OS model serving | KServe/BentoML/vLLM serving infra; platform-team territory | [BentoML docs (model serving)](https://docs.bentoml.com/) | 20 |
| 6.3.2 | Managed inference endpoints | Pay-per-call hosted inference; procurement awareness | [Azure ML: endpoints overview](https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints) | 15 |
| 6.7.1 | OS experiment tracking | MLflow tracking — already hands-on in 6.4.1 | [MLflow Tracking (covered in 6.4.1)](https://mlflow.org/docs/latest/ml/tracking/) | 5 |
| 6.7.2 | Managed experiment tracking | W&B/Neptune collaboration features on top of tracking | [W&B product page](https://wandb.ai/site) | 10 |

*T3 subtotal: 2.5 h*

### Capstone 7 — LLM extraction of fund documents (RAG + eval harness)

- **Goal:** a regulated-grade LLM document pipeline: public fund documents in, schema-valid structured data out, with retrieval metrics, field-accuracy evals, full traces, and human gates — feeding the governed lakehouse like any other source.
- **Stack (100% free):** [Ollama](https://ollama.com/) with a local open-weights model (↔ [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)), [LlamaIndex](https://docs.llamaindex.ai/) (↔ [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/) / [Bedrock KBs](https://docs.aws.amazon.com/bedrock/)), [pgvector](https://github.com/pgvector/pgvector) + [Qdrant](https://qdrant.tech/documentation/) comparison (↔ [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/)), [sentence-transformers](https://www.sbert.net/) (↔ Azure OpenAI embeddings), [Langfuse](https://langfuse.com/docs) (↔ [LangSmith](https://docs.smith.langchain.com/)), [Ragas](https://docs.ragas.io/en/stable/)/[DeepEval](https://deepeval.com/docs/getting-started) in CI (↔ Azure AI evals), [MLflow](https://mlflow.org/docs/latest/) registry for prompt+model versions, [Dagster](https://docs.dagster.io/) orchestrating ingest/re-index, outputs into [Iceberg](https://iceberg.apache.org/) with [Soda](https://docs.soda.io/) DQ checks + [OpenLineage](https://openlineage.io/docs/) lineage (the Phase-6 control plane applies unchanged).
- **Build:** (1) corpus: 30+ public KIDs/prospectuses (EN/FR), versioned in object storage; (2) parsing + chunking tuned on tables, with the 6.6.2 parser comparison applied; (3) hybrid retrieval (BM25 + vector) with source-span citations; (4) schema-constrained extraction into an EMT/EPT-shaped record (Pydantic-validated, invalid records rejected not patched); (5) golden-set evals (field accuracy + faithfulness) gating CI per 6.8.2; (6) Langfuse traces end-to-end, PII-safe per 6.8.1; (7) low-confidence extractions routed to a human-review queue (simple [Streamlit](https://docs.streamlit.io/) screen showing field, source span, and confidence); (8) results land in silver with DQ checks; lineage shows document → field.
- **Architecture deliverables:** C4 update (AI subsystem); ADR-019 local vs API models (cost/quality/residency), ADR-020 vector-store choice (with your benchmark), ADR-021 human-in-the-loop design (confidence thresholds, sampling, accountability).
- **Acceptance criteria:** field-level accuracy ≥ target on the held-out golden set with the number stated honestly (no cherry-picked subset); every extracted value traces to a source span (citation) and a trace ID; a degraded prompt fails CI; sub-threshold extractions reach the review queue with full context (field, span, confidence, trace link); reviewer decisions are recorded and queryable; the whole run is reproducible offline (no paid APIs).
- Est. hours: 18

*Phase 7 total: 74 h (T1/T2 entries 53 h + T3 2.5 h + capstone 18 h ≈ 74) + Appendix A items A.21, A.23, A.24 (7 h) scheduled in this phase*


<a id="phase-8"></a>
## Phase 8: Data Products, Semantic Layer & the Architect's Practice (months 44–48, 103 h + 18.5 h Appendix A)

*Phase 8 of 8 · months 44–48 · 121.5 h (103 h + 18.5 h Appendix A) · capstone: Productized fund data product.*  ← [Phase 7](#phase-7) · finish →

**Goal:** convert the governed platform into *products* — contracted, SLA-backed, semantically defined, consumable — and consolidate the formal architect's practice: DDD for boundaries, TOGAF/ArchiMate for the enterprise conversation, regulatory reporting as the domain's flagship deliverable, and the build-vs-buy fluency that Appendix D distills.
**Entry prerequisites:** Phases 1–7 (everything; this phase productizes the accumulated platform).
**Exit criteria:** you can (1) cut data-product boundaries with DDD and defend them; (2) publish a data product with an enforced contract, SLOs, and a semantic layer; (3) design a submission-grade regulatory reporting pipeline; (4) speak TOGAF/ArchiMate fluently in an EA forum; (5) win a build-vs-buy argument in any taxonomy domain with named tools and costs.
**Appendix A items scheduled here:** A.7 architecture styles & trade-off analysis, A.8 business architecture, A.9 EA governance, A.10 roadmapping & migration planning, A.11 agile EA, A.12 OWASP API security, A.13 ITSM/delivery frameworks (18.5 h).

### T1/T2 topics

#### 8.4.1 Domain-driven design — T1
- **Why:** Bounded contexts are how a data architect cuts product and team boundaries that survive reorgs — strategic DDD is the intellectual foundation under data mesh, and the difference between domain-oriented design and folder renaming. Without it, "NAV" means three different things in three systems, integrations rot into a big ball of mud, and every reorg redraws your data landscape along org-chart lines instead of domain lines.
- **Learn:**
    - ubiquitous language — one term, one precise meaning *inside* a context; why "NAV" in fund accounting and "NAV" in client reporting are legitimately different objects *(Learning DDD ch. 2)*
    - bounded contexts — boundaries of language and model consistency, not deployment units; how to spot one in conversation *(Learning DDD ch. 3)*
    - context mapping — partnership, customer–supplier, conformist, anticorruption layer, published language, separate ways, and what each implies for data flows *(Learning DDD ch. 4)*
    - subdomain types — core/supporting/generic and the investment logic that follows: build the core, buy the generic *(Learning DDD ch. 1)*
    - EventStorming — big-picture workshop mechanics (domain events, hotspots, pivotal events): your BA superpower, formalized *(Learning DDD ch. 12)*
    - aggregates at concept level — the consistency-boundary idea you need for design reviews, without the tactical code patterns *(Learning DDD ch. 6)*
    - applying DDD to data — source-aligned vs aggregate vs consumer-aligned data products, and which context owns which *(Data Mesh ch. 2)*
    - the fund-administration domain map — TA, fund accounting, custody, regulatory reporting, client reporting as candidate contexts, with EMT/EPT as published languages *(Learning DDD ch. 4, applied)*
- **Resources:**
    - **[Learning Domain-Driven Design](https://www.oreilly.com/library/view/learning-domain-driven-design/9781098100124/) (Khononov), strategic chapters 1–11 plus ch. 12 on EventStorming** — ubiquitous language, bounded contexts, context mapping, subdomains, aggregates (primary)
    - [Data Mesh](https://www.oreilly.com/library/view/data-mesh/9781492092384/) (Dehghani) ch. 2 — domain ownership and the data-product alignment types (the data application)
    - [Domain Language — Eric Evans](https://www.domainlanguage.com/) — the original DDD source and free DDD Reference for terminology disputes (reference)
- **Tools:**
    - FOSS (hands-on): [EventStorming](https://www.eventstorming.com/) on paper or a [Miro](https://miro.com/) free-tier board — the discovery workshop (↔ no corp equivalent; this is method)
    - FOSS (hands-on): [Context Mapper](https://contextmapper.org/) — a DSL that turns the context map into a versionable, reviewable artifact
- **Do:**
    1. Run a solo big-picture EventStorming of the subscription-order-to-NAV flow: domain events on orange stickies left to right, hotspots flagged, pivotal events (order accepted, trade settled, NAV struck) marked.
    2. Cluster the events into 5–7 candidate bounded contexts for a fund administrator (TA, fund accounting, custody, regulatory reporting, client reporting at minimum) and classify each subdomain as core/supporting/generic.
    3. Draw the context map with an explicit relationship type per edge — e.g. custody-to-fund-accounting as customer–supplier, EMT to distributors as published language, a legacy TA feed behind an ACL.
    4. Encode the map in Context Mapper DSL and commit it alongside your ADR log.
    5. Annotate which contexts own which data products and whether each product is source-aligned, aggregate, or consumer-aligned.
- **Done when:**
    - [ ] Defend the context map against the challenge "why is fund accounting not part of the TA context?" with a domain answer (different language, different invariants), not an org-chart answer.
    - [ ] Name the core subdomain of a fund administrator and justify where you would build rather than buy.
    - [ ] Point to one ACL on the map and explain exactly what model corruption it prevents.
- Est. hours: 10

#### 13.1.1 + 13.1.2 Data contracts (ODCS, enforcement) — T1
- **Why:** Contracts operationalize everything Phase 6 built — they are the mechanism that turns "governed dataset" into "product a consumer can rely on", and what the architect points to when a producer asks "can I rename this column?". The EU fund-data world (EMT files between manufacturers and distributors!) has run on implicit contracts for years; without explicit ones, breaking changes ship silently and surface as failed distributor loads and NAV-report corrections.
- **Learn:**
    - contract anatomy — schema, semantics, quality guarantees, SLAs, ownership, and terms of use as one negotiated document *(Driving Data Quality pt. 1–2)*
    - ODCS structure — the Bitol/Linux Foundation YAML standard: fundamentals, schema, quality, team/roles, and SLA blocks *(ODCS spec)*
    - datacontract-cli workflow — authoring, `lint`, `test` against live data, and breaking-change detection between versions *(Data Contract CLI docs)*
    - enforcement points — producer CI schema diff, schema registry on Kafka, WAP gate in the lakehouse, dbt model contracts in the warehouse *(dbt docs: Model contracts)*
    - contract-first vs contract-extracted adoption — greenfield negotiation vs retro-fitting contracts onto existing feeds, and when each path wins *(Driving Data Quality pt. 3)*
    - versioning & deprecation policy — semver for data, notice periods, migration paths; ties to your 1.9.7 evolution policy — same policy, now productized *(ODCS spec)*
- **Resources:**
    - **[Driving Data Quality with Data Contracts](https://www.oreilly.com/library/view/driving-data-quality/9781837635009/) (Andrew Jones)** — contract anatomy, adoption paths, producer accountability (primary)
    - [Open Data Contract Standard (ODCS)](https://bitol-io.github.io/open-data-contract-standard/) — the specification your contracts are written in (reference)
    - [Data Contract CLI docs](https://cli.datacontract.com/) — authoring, validation, tests against live data, breaking-change detection (hands-on reference)
    - [dbt docs: Model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts) — warehouse-side enforcement of contracted models (reference)
- **Tools:**
    - FOSS (hands-on): [datacontract-cli](https://cli.datacontract.com/) — contract authoring and CI testing (↔ [Gable](https://www.gable.ai/))
    - FOSS (hands-on): [dbt model contracts](https://docs.getdbt.com/docs/collaborate/govern/model-contracts) + [Confluent Schema Registry](https://docs.confluent.io/platform/current/schema-registry/index.html) — enforcement at the model and at the topic (↔ Confluent data contracts)
    - Corp (evaluate): [Gable](https://www.gable.ai/), [DataHub](https://datahubproject.io/) contracts — what commercial contract platforms add (code-level lineage, workflow) at build-vs-buy level
- **Do:**
    1. Write the ODCS contract for your gold NAV mart: schema with per-field semantics (ISIN, NAV-per-share precision), DQ guarantees, freshness SLO, named owner, license terms.
    2. Write the equivalent contract for the EMT output, treating distributors as the consumers and the FinDatEx field semantics as the published language.
    3. Wire `datacontract test` into CI so every merge validates both contracts against the live lakehouse tables.
    4. Add dbt model contracts on the underlying gold models so a type change fails the producer's build, not the consumer's load.
    5. Demonstrate a breaking change (rename a NAV column) being caught pre-merge, and a compatible change (new nullable column) passing with a version bump.
- **Done when:**
    - [ ] Show that a consumer can subscribe to your product knowing exactly what is guaranteed, and a producer cannot break it silently — both demonstrated in CI, not asserted.
    - [ ] Explain where each enforcement point (CI, registry, WAP gate, dbt) catches what the others miss.
    - [ ] Produce the deprecation notice you would send for a breaking change, with version, timeline, and migration path.
- Est. hours: 10

#### 14.4.2 Regulatory reporting — T1
- **Why:** Submission-grade reporting (AIFMD Annex IV, PRIIPs KID/EPT, MiFID/EMT) is the fund-data domain's flagship deliverable — deadline-driven, auditor-reviewed, and the workload your whole platform exists to serve. An architect who cannot design completeness gates and four-eyes approval ships late or wrong filings, and in Luxembourg a wrong Annex IV is a CSSF conversation, not a bug ticket.
- **Learn:**
    - what makes reporting "submission-grade" — completeness gates, plausibility checks, four-eyes approval, resubmission/correction workflow, full lineage to source, immutable filing archive *(ESMA IT guidance, applied)*
    - AIFMD Annex IV concretely — scope, reporting frequency by AUM threshold, the XML format, XSDs, and validation rules *(ESMA IT guidance)*
    - the rest of the EU landscape — PRIIPs KID data via EPT (your Phase-2 work), EMT distribution, SFDR templates and their ESG-data sourcing pain *(FinDatEx)*
    - report calendars & deadline orchestration — filing windows become schedules, sensors, and escalation paths; your Dagster schedules grow teeth *(Dagster docs)*
    - the vendor landscape — what Workiva/AxiomSL (Adenza)/Wolters Kluwer/Vermeg actually sell: forms engines + rule-update subscriptions + filing connectivity; the data stays your problem *(Workiva site)*
    - build-vs-buy economics — rule-maintenance burden is the buy argument; the pipeline feeding the forms engine is never outsourceable *(Workiva site, read critically)*
- **Resources:**
    - **[ESMA: AIFMD reporting IT technical guidance](https://www.esma.europa.eu/document/aifmd-reporting-it-technical-guidance-rev-6-updated)** — Annex IV templates, XSD schemas, validation rules (primary, free)
    - [FinDatEx](https://findatex.eu/) — your Phase-2 EMT/EPT specs (and the SFDR EET), reread as a producer (reference)
    - [Dagster docs](https://docs.dagster.io/) — schedules and sensors for deadline orchestration and the manual approval gate (hands-on reference)
    - [Workiva](https://www.workiva.com/) — one vendor-positioning read for the forms-engine layer (evaluation, not adoption)
- **Tools:**
    - FOSS (hands-on): the platform you built + [Dagster](https://docs.dagster.io/) scheduling and sensors — orchestrates gates, approvals, and deadlines
    - Corp (evaluate): [Workiva](https://www.workiva.com/), [Wolters Kluwer](https://www.wolterskluwer.com/) OneSumX, [Vermeg](https://www.vermeg.com/) — forms engines + rule updates + filing connectivity; know what they do and don't solve
- **Do:**
    1. Design the Annex-IV-shaped pipeline on paper first: gold marts → validation gates → XML rendering → four-eyes approval → immutable filing archive, in one diagram.
    2. Implement the validation gates as hard stops in Dagster: completeness (every required template field populated) and plausibility (AUM within tolerance of last period).
    3. Render the XML against the published ESMA schema and validate it; deliberately corrupt one field and show schema validation failing the run.
    4. Add the four-eyes step: a Dagster sensor that holds the filing until a second identity approves, logging who approved what and when.
    5. Archive each filing immutably (object-lock/WORM-style) with a lineage snapshot pinned to the run, and exercise the resubmission path once.
    6. Write the build-vs-buy memo for the forms-engine layer: rule-maintenance cost, vendor price ballpark, and what stays in-house either way.
- **Done when:**
    - [ ] Demonstrate that a deliberately incomplete dataset cannot reach the filing stage.
    - [ ] Trace a resubmission end-to-end: correction, re-approval, new archive entry linked to the superseded filing.
    - [ ] Defend the memo's honest pricing of the vendor option, including what buying does *not* solve (your data quality).
- Est. hours: 10

#### 8.1.3 Industry frameworks (TOGAF & ArchiMate, working fluency) — T2
- **Why:** TOGAF/ArchiMate is the lingua franca of EA departments in EU financial institutions; the architect who can't speak it gets translated by someone who can. Without working fluency your data architecture never lands in the enterprise repository on its own terms, and your designs lose governance-board arguments to a well-drawn ArchiMate view of a worse idea.
- **Learn:**
    - TOGAF 10 shape — the ADM cycle and what each phase produces, focusing on B/C (data architecture) with E/F covered via A.10 *(TOGAF Standard)*
    - architecture repository & landscape — building blocks, standards, and where your artifacts formally live *(TOGAF Standard)*
    - what to take seriously vs hold lightly — deliverable discipline and governance hooks yes; the full ceremony no *(TOGAF Standard, read critically)*
    - ArchiMate 3.2 core — business/application/technology layers and the core relationship set *(ArchiMate overview)*
    - the data-relevant elements — business object ↔ data object ↔ artifact, and how realization crosses layers *(ArchiMate overview)*
    - modeling in Archi — one model, many views; viewpoints as audience-specific projections *(Archi user guide)*
    - C4 ↔ ArchiMate mapping — which audience needs which notation, and how to translate between them live *(C4 model site)*
- **Resources:**
    - **[The TOGAF Standard](https://www.opengroup.org/togaf)** — Fundamental Content: Introduction & Core Concepts + ADM, free with Open Group registration (primary)
    - [ArchiMate — The Open Group](https://www.opengroup.org/archimate-forum/archimate-overview) — entry point to the 3.2 language specification (reference)
    - [Archi](https://www.archimatetool.com/) — the FOSS modelling tool, its user guide, and "hello ArchiMate" resources (hands-on)
    - [C4 model](https://c4model.com/) — the developer-facing notation you map to and from (deepening)
- **Tools:**
    - FOSS (hands-on): [Archi](https://www.archimatetool.com/) — full ArchiMate 3.2 modelling (↔ [Sparx EA](https://sparxsystems.com/), [BiZZdesign](https://bizzdesign.com/) — the licensed EA suites)
- **Do:**
    1. Read the TOGAF Core Concepts and ADM chapters; write a one-page "what I will actually use" note (phase B/C deliverables, repository discipline, governance hooks).
    2. Model your entire capstone platform in Archi: application layer (services, data products) and technology layer (clusters, storage), with data objects for the products realized by artifacts and linked to business objects (NAV, order, holding).
    3. Produce the COO viewpoint: a business-application view showing which business capabilities each data product serves.
    4. Produce the security viewpoint: a technology view showing zones, the gateway, and where PII-bearing artifacts live.
    5. Translate one ArchiMate application view into a C4 container diagram and record the mapping rules you used.
- **Done when:**
    - [ ] Walk an EA review board through the ArchiMate model and translate any element to/from your C4 diagrams live.
    - [ ] Place any of your existing artifacts (context map, technology standard, roadmap) in the correct ADM phase without looking it up.
    - [ ] State which TOGAF artifacts you would skip on a 10-person programme, and why that is defensible.
- Est. hours: 10

#### 1.4.4 Data mesh (and 13.2.1 enabling platforms) — T2
- **Why:** Mesh is the organizational scaling answer you'll be asked about in every large-firm interview; the architect's job is knowing when its costs are justified — and what "federated computational governance" means after Phase 6. Adopt it too early and you starve the platform team while shattering a small firm's estate into unowned fragments; dismiss it outright and a 3,000-person group keeps its central-team bottleneck forever.
- **Learn:**
    - the four principles — domain ownership, data as a product, self-serve platform, federated computational governance — read against your own build *(Data Mesh pt. I)*
    - what you have already built — principles 2–4 exist single-domain in your platform; what changes when domains multiply *(Data Mesh pt. II)*
    - federated computational governance — global policies executed by the platform (your policy-as-code and catalog work) vs local domain autonomy *(Data Mesh pt. II)*
    - mesh failure modes — mesh-washing, platform-team starvation, premature decentralization *(Data Management at Scale 2e)*
    - enabling platforms — Starburst/Trino federation, Databricks UC domains, your OpenMetadata domains as the technical substrate *(Data Management at Scale 2e)*
    - the sizing test — why a 50-person fund admin should *not* mesh, and the threshold signals that change the answer *(Data Mesh pt. III skim)*
- **Resources:**
    - **[Data Mesh](https://www.oreilly.com/library/view/data-mesh/9781492092384/) (Dehghani), parts I–II, skim III** — the principles and target operating model (primary)
    - [Data Management at Scale, 2nd ed.](https://www.oreilly.com/library/view/data-management-at/9781098138851/) (Strengholt) — the pragmatic counterweight: domains without dogma (alternate)
    - [Data Mesh Principles (martinfowler.com)](https://martinfowler.com/articles/data-mesh-principles.html) — free condensed statement of the four principles (reference)
- **Tools:**
    - FOSS (evaluate): [Trino](https://trino.io/) federation + [OpenMetadata](https://docs.open-metadata.org/) domains — the self-serve substrate you already run
    - Corp (evaluate): [Starburst](https://www.starburst.io/), [Databricks Unity Catalog](https://docs.databricks.com/) domains — what the commercial enabling platforms package
- **Do:**
    1. Re-read your Phase-6/7 platform inventory and mark which mesh principle each component serves; note the gaps (multi-domain ownership, federated policy execution).
    2. Take the DDD context map from 8.4.1 as the candidate domain decomposition for a 300-person fund administrator.
    3. Write the two-page memo: "Should a 300-person fund administrator adopt mesh?" — org sizing, domain map, platform prerequisites, and an honest no/not-yet/yes-partially recommendation with trigger conditions.
    4. Stress-test the memo by writing the strongest one-paragraph counter-argument to your own recommendation, then answer it.
- **Done when:**
    - [ ] Argue both for and against mesh for the same firm, and name the organizational precondition that decides it.
    - [ ] Define federated computational governance in one sentence, with a concrete policy example from your own build.
    - [ ] List three mesh failure modes and the early-warning signal for each.
- Est. hours: 5

#### 7.1.1 + 7.2.1 Semantic & metrics layer (Cube, MetricFlow) — T2
- **Why:** "One definition of AUM" is a governance promise only a semantic layer can keep across BI tools, APIs, and notebooks; headless BI is the architectural pattern behind it. Without it every dashboard and board pack re-derives AUM in its own SQL, the numbers drift, and the architect spends review meetings arbitrating whose figure is right instead of designing.
- **Learn:**
    - semantic-layer anatomy — dimensions, measures, joins, and access control defined once at the semantic level *(Cube docs: data modeling)*
    - Cube specifics — data model files, pre-aggregations, REST and SQL APIs, caching tiers *(Cube docs)*
    - MetricFlow — metric definitions living in the dbt DAG; simple, derived, ratio, and cumulative metric types *(dbt docs: About MetricFlow)*
    - the consistency argument — a metrics layer vs BI-tool-local definitions, and why the latter always drifts *(dbt docs: About MetricFlow)*
    - semantic layer vs glossary — definition *executed* vs definition *documented*, and how to link the two so neither rots *(Cube docs, applied)*
    - when the semantic layer is premature — one consumer, one tool, no contested metrics *(Cube docs: introduction)*
- **Resources:**
    - **[Cube docs](https://docs.cube.dev/)** — data modeling, pre-aggregations, REST/SQL APIs, caching (primary)
    - [dbt docs: About MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow) — metric specification inside the dbt DAG (alternate stack)
    - [Apache Superset](https://superset.apache.org/) — the consuming BI client for the three-client demo (hands-on reference)
- **Tools:**
    - FOSS (hands-on): [Cube](https://docs.cube.dev/) — headless semantic layer (↔ [Looker](https://cloud.google.com/looker)/LookML, [AtScale](https://www.atscale.com/))
    - FOSS (hands-on): [MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow) — dbt-native metrics (↔ [Power BI semantic models](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand) — next entry)
- **Do:**
    1. Define NAV, AUM, and net-flows once in Cube's data model over the gold marts, including the join topology and a management-company access rule at the semantic level.
    2. Mirror the same three metrics as MetricFlow definitions in the dbt project; note where the two specification styles diverge.
    3. Consume the Cube metrics from three clients — a Superset chart, a raw REST call, and a notebook via the SQL API — and show identical numbers.
    4. Link each metric to its glossary term in both directions (glossary entry → semantic-layer reference, metric description → glossary URL).
    5. Change the AUM definition (e.g. exclude side-pocket share classes) in one place and demonstrate all three clients updating, with the change visible in version control.
- **Done when:**
    - [ ] Demonstrate that changing the AUM definition in one place changes it everywhere, with an audit trail.
    - [ ] Explain pre-aggregations: what they cache, when they invalidate, and the freshness trade-off they buy.
    - [ ] State the rule for when a metric belongs in the semantic layer vs a local dashboard calculation.
- Est. hours: 7

#### 7.1.2 Platform semantic layers (Power BI semantic models) — T2
- **Why:** In Azure shops the Power BI semantic model *is* the de-facto semantic layer; you must know when it suffices and when headless wins. Rule wrongly and you either pay for a redundant headless layer nobody queries, or watch certified AUM definitions fork across forty workspace models — the sprawl failure mode that CFOs and auditors both eventually notice.
- **Learn:**
    - storage modes — import vs DirectQuery vs Direct Lake (the Fabric tie to A.4) and their latency/cost/freshness trade-offs *(MS Learn: semantic model modes)*
    - star-schema expectations — why your Kimball work is the prerequisite for a healthy model *(MS Learn: star schema)*
    - RLS in the model — roles, DAX filters, and management-company isolation *(MS Learn: semantic models in the service)*
    - lifecycle management — deployment pipelines and the XMLA endpoint for pro-grade ALM *(MS Learn: semantic models in the service)*
    - sprawl & certified datasets — endorsement, discovery, and the governance that prevents forty AUM definitions *(MS Learn: semantic models in the service)*
    - the decision rubric — Power BI model vs headless layer by org shape, tool mix, and consumer diversity *(MS Learn: semantic model modes, applied)*
- **Resources:**
    - **[Understand star schema and the importance for Power BI](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema)** — the model-design guidance the exercise follows (primary)
    - [Semantic models in the Power BI service](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand) — creation, management, endorsement, and sharing of models (reference)
    - [Semantic model modes in the Power BI service](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand) — import vs DirectQuery vs composite, the Direct Lake context (reference)
- **Tools:**
    - Corp (hands-on, free Desktop): [Power BI](https://learn.microsoft.com/en-us/power-bi/) — Desktop suffices for the exercise (↔ FOSS: [Cube](https://docs.cube.dev/) from the previous entry)
- **Do:**
    1. Build the NAV mart semantic model in Power BI Desktop (free): a star schema with fund/share-class/date dimensions and explicit measures for NAV, AUM, and net-flows.
    2. Implement RLS by management company and verify it with the "view as role" feature.
    3. Compare definitions with your Cube model measure by measure; document every place the two could drift (measure logic, filters, timezone handling).
    4. Write the governance rule preventing drift: which layer is authoritative for which metric, and the review step that enforces it.
    5. Write the one-page rubric ruling "Power BI model vs headless layer" for three org shapes (Azure-only 50-person admin, multi-tool 300-person admin, multi-cloud group).
- **Done when:**
    - [ ] Rule "Power BI model vs headless layer" for three org shapes and defend it.
    - [ ] Demonstrate RLS isolating two management companies inside one model.
    - [ ] Name the semantic-model-sprawl failure mode and the certified-dataset control that contains it.
- Est. hours: 4

#### 12.4.1 Data SLAs & SLO management — T2
- **Why:** The SLO machinery (Phase 5 vocabulary) becomes contractual here: freshness/completeness targets with error budgets are what "productized" means operationally. Without measured SLOs, the contract's "fresh by 08:00 CET" is marketing copy — and the first missed NAV deadline becomes finger-pointing instead of a burn-rate alert with a documented response.
- **Learn:**
    - data SLIs — freshness, completeness, accuracy proxies, and serving-layer availability as measurable indicators *(SRE Workbook ch. 2)*
    - setting SLOs consumers actually need — interview them (BA skills) instead of declaring vanity nines *(SRE Workbook ch. 2)*
    - error budgets for data — when a burned budget freezes risky pipeline changes *(SRE Workbook ch. 2)*
    - burn-rate alerting — multiwindow, multi-burn-rate alerts instead of paging on point failures *(SRE Workbook ch. 5)*
    - SLO surfacing — attainment published on the catalog product page and in the ODCS contract's SLA block *(ODCS spec)*
- **Resources:**
    - **[Google SRE Workbook ch. 2: Implementing SLOs](https://sre.google/workbook/implementing-slos/)** — SLI/SLO/error-budget mechanics, translated to data in your 13.1.1 contract (primary, free online)
    - [Google SRE Workbook ch. 5: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — burn-rate alert design (deepening)
    - [ODCS spec](https://bitol-io.github.io/open-data-contract-standard/) — where the SLA properties live in the contract you already wrote (reference)
- **Do:**
    1. Interview yourself as three consumers (board-pack analyst, distributor ops, regulatory deadline owner) and derive the SLOs each actually needs from the NAV product.
    2. Define the SLOs (e.g., 99% of business days fresh by 08:00 CET; 100% of active share classes present) and encode them in the ODCS contract's SLA block.
    3. Instrument the SLIs from your Phase-5/6 telemetry and store daily attainment.
    4. Add a burn-rate alert (fast + slow window) on the freshness SLO.
    5. Replay one month of synthetic history including one bad week; record attainment, the alert firing, and the error-budget response (a change-freeze note).
- **Done when:**
    - [ ] Show the product page displaying measured SLO attainment, and a simulated bad week visibly consuming error budget with a documented response.
    - [ ] Explain why burn-rate alerting beats alerting on individual late runs.
    - [ ] Justify each SLO target with a named consumer need, not a round number.
- Est. hours: 3

#### 13.3.2 Cross-org data sharing (Delta Sharing) — T2
- **Why:** Fund data is *disseminated* — to distributors, platforms, regulators; open sharing protocols are the modern alternative to the SFTP-and-CSV folklore the industry still runs on. The architect who can't compare sharing protocol vs API vs file-drop ends up rebuilding forty bespoke SFTP feeds, each with its own format drift and no revocation story.
- **Learn:**
    - the Delta Sharing protocol — open, REST-based, format-level access to Delta tables without copying *(Delta Sharing page)*
    - shares, recipients, governance — how access is granted, scoped, audited, and revoked *(delta-sharing GitHub)*
    - the walled gardens — Snowflake secure shares and the Databricks marketplace as in-ecosystem equivalents *(Snowflake docs: Secure Data Sharing)*
    - egress economics — who pays for reads, and why no-copy sharing changes the cost conversation *(Snowflake docs: Secure Data Sharing)*
    - the channel rubric — sharing protocol vs API vs file-drop, scored by volume, latency, and consumer sophistication *(Delta Sharing page, applied)*
    - the contractual overlay — a share is still a product: contract, SLOs, and license terms ride along (ties 13.1.1, A.18) *(delta-sharing GitHub, applied)*
- **Resources:**
    - **[Delta Sharing](https://delta.io/sharing/)** — the open protocol: overview and ecosystem (primary)
    - [delta-sharing on GitHub](https://github.com/delta-io/delta-sharing) — protocol spec, the reference server you will run, client libraries (hands-on)
    - [Snowflake docs: About Secure Data Sharing](https://docs.snowflake.com/en/user-guide/data-sharing-intro) — the walled-garden comparison read (reference)
- **Tools:**
    - FOSS (hands-on): [delta-sharing reference server](https://github.com/delta-io/delta-sharing) — serves a gold Delta table over the open protocol (↔ [Databricks Delta Sharing](https://docs.databricks.com/), [Snowflake shares](https://docs.snowflake.com/en/user-guide/data-sharing-intro), Fabric external sharing)
- **Do:**
    1. Stand up the reference sharing server over a gold Delta table, with a share config exposing one schema to one recipient token.
    2. Consume the share from a separate "distributor" environment with the pandas client; verify the data matches source with no copy pipeline in between.
    3. Rotate and then revoke the recipient credential and show access ending — the revocation story SFTP never had.
    4. Write the rubric: when sharing protocol vs API vs EMT file-drop, scored by volume, latency, consumer sophistication, and audit needs.
- **Done when:**
    - [ ] Design the dissemination architecture for a fund manufacturer with 40 distributor relationships and defend the channel per consumer class.
    - [ ] Explain what the open protocol buys over Snowflake/Databricks-native shares, and what it costs you to run.
    - [ ] Show the revocation demo and name the governance evidence it produces.
- Est. hours: 3

#### 13.4.2 + 2.6.1 Data APIs & gateways (data-as-a-service) — T2
- **Why:** The API is the product surface for operational consumers (websites, partner systems); the gateway is where auth, quotas, and versioning live — an architect's checklist, not a developer's tutorial. Skip the gateway discipline and every consumer hits the database directly: no quotas, no usage attribution for chargeback, and an OWASP-API-Top-10 incident waiting on the NAV endpoint.
- **Learn:**
    - resource modeling for fund data — funds/share-classes/navs as resources, pagination, filtering, consistent error shapes *(Azure AC: Web API design)*
    - versioning policy — URI vs header versioning, deprecation paths; ties to your 1.9.7 evolution policy *(Azure AC: Web API design)*
    - OpenAPI as the contract — the machine-readable spec consumers onboard from, kept in version control *(Azure AC: Web API design)*
    - gateway duties — OIDC token validation (your Keycloak), rate limiting and quotas per consumer tier, usage analytics for chargeback *(Kong Gateway docs)*
    - instant serving — PostgREST (or FastAPI) turning a gold view into a read-only REST API in minutes *(PostgREST docs)*
    - caching policy at the edge — your 3.3.4 decision applied at the gateway tier *(Kong Gateway docs)*
    - API security — the OWASP API Top-10 as the review checklist (A.12) *(OWASP API Security Project)*
    - when GraphQL earns its complexity — many consumers with shape-shifting reads; rarely for fund data (2.6.2 stays T3) *(Azure AC: Web API design)*
- **Resources:**
    - **[Kong Gateway docs](https://developer.konghq.com/gateway/)** — gateway concepts: auth plugins, rate limiting, usage analytics (primary)
    - [PostgREST docs](https://docs.postgrest.org/) — serving Postgres views as REST, roles and JWT integration (hands-on)
    - [Azure Architecture Center: Web API design best practices](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design) — resource modeling, versioning, pagination, filtering (reference)
    - [OWASP API Security Project](https://owasp.org/www-project-api-security/) — the Top-10 checklist you will run against your own API (reference)
- **Tools:**
    - FOSS (hands-on): [PostgREST](https://docs.postgrest.org/) or [FastAPI](https://fastapi.tiangolo.com/) — the serving layer over gold views
    - FOSS (hands-on): [Kong Gateway OSS](https://developer.konghq.com/gateway/) + [Keycloak](https://www.keycloak.org/documentation) — OIDC validation, quotas, usage logs (↔ [Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/), [Apigee](https://cloud.google.com/apigee))
- **Do:**
    1. Expose the NAV product as a read-only REST API: PostgREST over a gold view, with `/funds`, `/share-classes`, `/navs` resources, pagination, and filtering.
    2. Put Kong in front: OIDC plugin validating Keycloak tokens, and two consumer tiers with different rate limits.
    3. Publish the OpenAPI document — generate it, then hand-edit descriptions until a stranger could onboard from it.
    4. Drive traffic past a quota and show enforcement (HTTP 429s) plus per-consumer usage in the gateway logs — the chargeback evidence.
    5. Run the OWASP API Top-10 checklist (A.12) against the API; fix or explicitly risk-accept each finding.
- **Done when:**
    - [ ] Prove an external consumer can onboard from the OpenAPI doc + contract alone, and the gateway proves quota enforcement in logs.
    - [ ] State your API versioning policy and show where a breaking change would surface for consumers.
    - [ ] Present the completed OWASP API Top-10 checklist with each item fixed or risk-accepted.
- Est. hours: 5

#### 14.1.1 + 14.1.3 Business intelligence (Superset hands-on, Power BI fluency) — T2
- **Why:** BI is where your platform meets its judges; the architect doesn't build dashboards for a living but must design the BI tier (tooling, governance, self-service boundaries) and read the vendor market. Get the governance wrong and you inherit the "300 unowned dashboards" estate — contradictory numbers in front of the fund board, with nobody accountable for any of them.
- **Learn:**
    - Superset mechanics — datasets/charts/dashboards, its semantic-ish layer, row-level security, embedding *(Superset docs)*
    - Power BI ecosystem economics — per-user vs capacity/Fabric licensing as the real selection driver in Azure shops *(MS Learn: Power BI licensing)*
    - vendor positioning — Tableau/Looker/Qlik read in one sitting: who sells what, to whom *(Tableau site)*
    - governed self-service — certified datasets, sandbox vs production content, explicit ownership rules *(Superset docs: security)*
    - the sprawl failure mode — how 300 unowned dashboards happen and the certification workflow preventing it *(MS Learn: Power BI licensing, applied)*
    - BI-on-semantic-layer — consume Cube; never re-model metrics inside the BI tool *(Cube docs)*
- **Resources:**
    - **[Apache Superset](https://superset.apache.org/)** — docs: creating charts/dashboards, security and RLS, embedding (primary)
    - [MS Learn: Power BI license types](https://learn.microsoft.com/en-us/power-bi/fundamentals/service-features-license-type) — features by license, the economics read (reference)
    - [Tableau](https://www.tableau.com/) — one vendor-positioning read; skim Looker and Qlik the same way (market scan)
    - [Cube docs](https://docs.cube.dev/) — connecting BI tools to the semantic layer (reference)
- **Tools:**
    - FOSS (hands-on): [Apache Superset](https://superset.apache.org/), [Metabase](https://www.metabase.com/) (↔ [Power BI](https://learn.microsoft.com/en-us/power-bi/) [Azure default], [Tableau](https://www.tableau.com/), [Looker](https://cloud.google.com/looker))
    - Corp (evaluate): [Power BI](https://learn.microsoft.com/en-us/power-bi/) — primary evaluation: licensing tiers, capacity planning, Fabric direction
- **Do:**
    1. Build the fund-board dashboard (NAV trend, net flows, DQ status) in Superset *on top of Cube* — every figure sourced from semantic-layer metrics, zero local SQL definitions.
    2. Apply RLS in Superset by management company and verify with two test users.
    3. Skim Power BI, Tableau, and Looker positioning/pricing pages; write a half-page market map of who wins in which org shape.
    4. Write the BI governance one-pager: certification workflow, ownership, sandbox-vs-production policy, and a decommissioning rule for unowned content.
- **Done when:**
    - [ ] Verify the dashboard consumes only semantic-layer metrics (zero local SQL definitions).
    - [ ] Present the governance pager answering "who may publish what, where" — including the path from sandbox to certified.
    - [ ] Explain Power BI per-user vs capacity licensing well enough to size a 300-user deployment.
- Est. hours: 7

#### 14.6.1 Data app frameworks (Streamlit) — T2
- **Why:** Data apps are the fast path from platform to stakeholder value (review queues, what-if tools); Streamlit is the de-facto standard and your Phase-7 review UI already used it. Without understanding its execution model and scaling limits, the architect green-lights a 200-user Streamlit "application" that reruns the world on every widget click and falls over at the first board demo.
- **Learn:**
    - the execution model — rerun-on-interaction, `st.cache_data`/`st.cache_resource`, session state *(Streamlit docs)*
    - scaling limits — the single-process model and the user-count/interactivity point where it breaks *(Streamlit docs)*
    - the decision line — Streamlit vs Dash vs a real frontend, by interactivity, state complexity, and audience size *(Dash docs, compared)*
    - deployment & auth — running behind your Kong gateway with OIDC instead of public-internet defaults *(Streamlit docs)*
    - the internal-tools landscape — what the Retool class sells: CRUD on governed APIs with RBAC, at a glance *(Retool site)*
- **Resources:**
    - **[Streamlit docs](https://docs.streamlit.io/)** — main concepts, caching, session state, deployment (primary)
    - [Dash docs](https://dash.plotly.com/) — the main FOSS alternative, read for the comparison (alternate)
    - [Retool](https://retool.com/) — the commercial internal-tools class at a glance (market scan)
- **Tools:**
    - FOSS (hands-on): [Streamlit](https://docs.streamlit.io/) — the product console (↔ Snowflake-Streamlit, [Retool](https://retool.com/), [Power Apps](https://learn.microsoft.com/en-us/power-apps/))
- **Do:**
    1. Build the "fund data product console": one screen per product showing SLO status, contract version, latest DQ results, lineage link, and a sample-data preview.
    2. Pull each panel from existing services (SLO telemetry, contract repo, DQ store, OpenMetadata link) — no new data paths.
    3. Cache expensive calls correctly and prove a widget interaction does not refetch the world (log the cache hits).
    4. Serve the console behind Kong with OIDC, so access uses the same identity plane as everything else.
- **Done when:**
    - [ ] Confirm a product owner can answer "is my product healthy and who consumes it?" from the console without touching the platform.
    - [ ] Explain the rerun-on-interaction model and show where caching saved you.
    - [ ] State the user-count/interactivity threshold where you would leave Streamlit, and for what.
- Est. hours: 3

#### 1.8.11 Strangler fig (legacy replacement strategy) — T2
- **Why:** Every Luxembourg estate has a legacy core (TA system, reporting engine) that can only be replaced incrementally; strangler-fig discipline is how migrations avoid big-bang death — and it operationalizes your A.10 roadmapping. Without it, replacement programmes run as multi-year parallel estates with dual-write drift, and the legacy system never dies — it just gains a twin.
- **Learn:**
    - the pattern — incrementally route functionality through a facade until the legacy core is hollow, then switch it off *(Fowler: Strangler Fig Application)*
    - facade placement for data systems — views, CDC-fed parallel runs, routing at the consumption layer *(Azure AC: Strangler Fig pattern)*
    - dual-write avoidance — use your outbox/CDC patterns instead of writing to both systems *(Azure AC: Strangler Fig pattern)*
    - parallel-run reconciliation — your Phase-4 reconciliation pattern reused as the trust-builder before cutover *(Fowler: Strangler Fig Application, applied)*
    - cutover & rollback criteria — measurable gates (drift thresholds, consumer migration counts), not dates *(Azure AC: Strangler Fig pattern)*
    - the anti-pattern — the strangler that never finishes; sunset discipline and funded decommissioning *(Fowler: Strangler Fig Application)*
- **Resources:**
    - **[Strangler Fig Application (Martin Fowler)](https://martinfowler.com/bliki/StranglerFigApplication.html)** — the pattern and its rationale (primary)
    - [Azure Architecture Center: Strangler Fig pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig) — cloud-migration framing, context, and issues to watch (reference)
- **Do:**
    1. Pick the target: a legacy reporting mart to be replaced by your gold layer; inventory its consumers and inbound feeds.
    2. Write the migration ADR: facade design (views/routing), CDC-fed parallel-run period, reconciliation gates, cutover criteria, rollback plan, sunset date.
    3. Define the reconciliation checks concretely (row counts, NAV-per-share tolerance, aggregate AUM) and the drift threshold that blocks cutover.
    4. Add the sunset milestone with a named decommission deliverable — what gets switched off, and who signs.
- **Done when:**
    - [ ] Verify the plan has measurable gates (reconciliation drift thresholds) instead of dates-and-hope.
    - [ ] Explain why dual-write is forbidden in your design and what replaces it.
    - [ ] Name the organizational forces that produce never-finishing stranglers, and your counter for each.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.4.5 | Data fabric | Metadata-driven unified-access vision (vendor-led counterpoint to mesh) | [IBM: What is a data fabric?](https://www.ibm.com/think/topics/data-fabric) — read critically | 20 |
| 2.6.2 | GraphQL data layers | Schema-driven query APIs (Hasura); complexity rarely earned for fund data | [Hasura docs](https://hasura.io/docs/) — "how it works" intro | 20 |
| 2.7.1 | Reverse ETL | Warehouse → SaaS sync (Hightouch/Census); CRM-enrichment use cases | [Hightouch docs](https://hightouch.com/docs) — intro | 20 |
| 13.3.1 | Internal data marketplaces | Catalog-with-checkout UX over data products | [Atlan: Data Marketplace](https://atlan.com/data-marketplace/) | 15 |
| 13.3.3 | Commercial data marketplaces | Buying market/ESG data feeds (Snowflake Marketplace, Datarade) | [About Snowflake Marketplace](https://docs.snowflake.com/collaboration/collaboration-marketplace-about) | 20 |
| 13.4.1 | GraphQL DaaS | Productized GraphQL endpoints; see 2.6.2 | [covered there — Hasura docs](https://hasura.io/docs/) | 5 |
| 14.1.2 | Legacy enterprise BI | BusinessObjects/Cognos/MicroStrategy estates you'll migrate from | [IBM Cognos Analytics](https://www.ibm.com/products/cognos-analytics) — one vendor-positioning overview | 20 |
| 14.2.1 | Visualization libraries | Plotly/Vega/D3 programmatic charting; Storytelling-with-Data principles | [*Storytelling with Data*](https://www.storytellingwithdata.com/) — ch. 1–2 skim | 45 |
| 14.3.1 | Embedded analytics | BI inside products (Superset/Cube embed, Looker embed) | [Cube docs](https://docs.cube.dev/) — embedding pages | 20 |
| 14.4.1 | Operational/paginated reporting | Pixel-perfect statements (Power BI paginated, Jasper) | [Power BI paginated reports overview](https://learn.microsoft.com/en-us/power-bi/paginated-reports/paginated-reports-report-builder-power-bi) | 20 |
| 14.5.1 | Cloud notebooks | Hex/Deepnote collaborative analysis; governance angle (where results live) | [Hex](https://hex.tech/) — product overview | 15 |
| 14.6.2 | Low-code internal tools | Retool/Appsmith CRUD builders on governed APIs | [Appsmith](https://www.appsmith.com/) — overview | 15 |
| 14.7.2 | Reverse-ETL activation | Acting on data signals in operational tools; see 2.7.1 | [covered there — Hightouch docs](https://hightouch.com/docs) | 5 |

*T3 subtotal: 4 h*

### Capstone 8 — The fund data product (end state)

- **Goal:** the four-year arc closes: one fund data product, productized end-to-end — contracted, SLO-backed, semantically defined, multi-channel (BI, API, sharing, EMT file), regulator-ready, and documented like the portfolio piece it is.
- **Stack (100% free):** everything already running, plus [Cube](https://docs.cube.dev/) + [MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow) (↔ [Looker](https://cloud.google.com/looker)/[AtScale](https://www.atscale.com/)/[Power BI semantic models](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-understand)), [datacontract-cli](https://cli.datacontract.com/) + [ODCS](https://bitol-io.github.io/open-data-contract-standard/) (↔ [Gable](https://www.gable.ai/)/[Collibra](https://www.collibra.com/) contracts), [PostgREST](https://docs.postgrest.org/) + [Kong](https://developer.konghq.com/gateway/) (↔ [Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/)), [delta-sharing server](https://github.com/delta-io/delta-sharing) (↔ [Databricks](https://docs.databricks.com/)/[Snowflake](https://docs.snowflake.com/en/user-guide/data-sharing-intro) sharing), [Superset](https://superset.apache.org/) (↔ [Power BI](https://learn.microsoft.com/en-us/power-bi/)), [Streamlit](https://docs.streamlit.io/) console, [Archi](https://www.archimatetool.com/) for the ArchiMate model (↔ [Sparx EA](https://sparxsystems.com/)).
- **Build:** (1) the "Fund NAV & Flows" data product: ODCS contract, SLOs with burn-rate alerting, semantic metrics, owner & glossary links — all visible in the catalog; (2) four consumption channels from one gold source: Superset board dashboard, REST API behind Kong (OIDC + quotas), Delta Share to a "distributor" environment, and EMT/Annex-IV regulatory outputs with validation gates and four-eyes approval; (3) the product console (Streamlit) surfacing health, contract version, and consumers; (4) the architect's portfolio: full C4 set, ArchiMate model + 2 viewpoints, the complete ADR log (001–022+), DDD context map, DCAM assessment + roadmap, build-vs-buy memos, migration (strangler) plan; (5) a 30-minute "architecture walkthrough" deck/script — the artifact you'd present to an interview panel or review board.
- **Architecture deliverables:** ADR-022 product-boundary definition (from the context map), ADR-023 consumption-channel architecture (why four channels, one source), ADR-024 semantic-layer placement (headless vs Power BI, final position).
- **Acceptance criteria:** a cold-start reviewer can: read the contract → consume all four channels → verify an SLO claim from telemetry → trace one EMT figure to source via lineage → find every decision in an ADR; the breaking-change drill fails CI at the contract; the walkthrough survives 10 hard questions you've scripted answers to (CAP misuse, mesh timing, Iceberg-vs-Delta, build-vs-buy × 3, DR cost, GDPR erasure, exactly-once honesty, vendor lock-in).
- Est. hours: 20

*Phase 8 total: 103 h (T1/T2 entries 79 h + T3 4 h + capstone 20 h) + Appendix A items A.7–A.13 (18.5 h) scheduled in this phase*


<a id="excluded"></a>
## Excluded

Taxonomy subcategories deliberately out of scope, each with its reason. Everything else appears in a phase or the Skip List (see [Appendix C](#appendix-c)).

| ID | Subcategory | Reason |
|---|---|---|
| 5.5.1 | Reverse ETL (Processing placement) | Cross-reference pointer in the taxonomy itself ("listed in §2.7"); covered once as 2.7.1 (T3, Phase 8). |
| 6.5.1 | Vector Databases (AI/ML placement) | Cross-reference pointer ("listed in §3.2"); covered once as 3.2.9 (T2, Phase 7). |
| 10.8.1 | Audit & Compliance (Governance placement) | Cross-reference pointer ("see §11"); covered by 11.6.1 and 11.7.1 (Phase 6). |
| 13.5.1 | Standalone CDPs (Segment, mParticle…) | B2C marketing technology — identity resolution and audience activation for consumer brands; no realistic deliverable for a fund-industry data architect. The transferable concepts (entity resolution, golden records) are covered at depth in MDM (10.5.1). |
| 13.5.2 | Composable CDPs (Hightouch/Census audiences) | Same rationale as 13.5.1; the underlying reverse-ETL mechanics are covered as 2.7.1 (T3). |


<a id="appendix-a"></a>
## Appendix A — Gap Additions

Topics that the INPUT-2 cross-check sources treat as significant but that are absent from the taxonomy. Each is scheduled into a phase and counted in the budget (`A.x` IDs). All nine source groups were verified by live web cross-check (June 2026), marked ✓. A.27–A.31 were added on the learner's instruction to assume **zero prior knowledge** — their sources are the verified roadmaps that treat them as foundational.

### Foundations (scheduled in Phase 0; each skippable via its Skip List test)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.27 | Linux, the command line & shell scripting — the substrate beneath Docker, Kubernetes, CI, cloud shells, and log forensics | roadmap.sh postgresql-dba + devops ✓ | T2 | 0 | MIT *The Missing Semester* (free) — https://missing.csail.mit.edu/ | 12 |
| A.28 | Python from zero — control flow, functions, files, environments (uv-first), debugging, a first CLI | roadmap.sh data-engineer ✓ | T2 | 0 | *Python for Everybody* (py4e, free full course); alt: *Automate the Boring Stuff* (free online) | 36 |
| A.29 | SQL from zero — joins, aggregation, NULL semantics, CTEs, window functions | roadmap.sh data-engineer ✓ | T2 | 0 | SQLBolt + PgExercises (free, browser-based) | 26 |
| A.30 | Docker & containers from zero — images, Dockerfiles, Compose, volumes, debugging | roadmap.sh devops ✓ | T2 | 0 | Docker official "Get Started" guide | 8 |
| A.31 | Networking & how the web works — IP/TCP, DNS, HTTP, TLS, proxies/firewalls at literacy level | roadmap.sh devops + system-design ✓ | T2 | 0 | MDN "How the web works" + Cloudflare Learning Center (DNS, TLS) | 8 |

### Platform & cloud (scheduled in Phases 1 and 5)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.1 | Distributed consensus & replication protocols (Raft/Paxos, quorum replication, coordination services) — the layer beneath the taxonomy's consistency/CAP/2PC coverage; what HA/RPO claims of Kafka, Cosmos DB, zone-redundant Azure services rest on | MIT 6.5840 ✓ | T2 | 1 | MIT 6.5840 lectures 4, 6–9, 13 + the extended Raft paper — https://pdos.csail.mit.edu/6.824/schedule.html | 5 |
| A.2 | Byzantine fault tolerance & DLT fundamentals — trust models behind tokenized fund shares, which Luxembourg is actively piloting | MIT 6.5840 ✓ | T3 | 1 | MIT 6.5840 lectures 20–21 (Bitcoin, PBFT) | 1.5 |
| A.3 | Cloud networking & private connectivity (VNets, Private Link, ExpressRoute, NSG/Azure Firewall, private DNS, L4/L7 load balancing) — fund-industry Azure estates are network-isolated by policy; every integration design crosses this layer | roadmap.sh software-architect + system-design ✓ | T2 | 5 | Microsoft Learn AZ-700 path (free) — https://learn.microsoft.com/en-us/training/paths/design-implement-microsoft-azure-networking-solutions-az-700/ | 6 |
| A.4 | Microsoft Fabric / OneLake platform architecture (capacities, domains, shortcuts, Direct Lake, deployment pipelines) — Microsoft's strategic successor to Synapse; the default evaluation target for an Azure-primary architect | DP-700/DP-600 ✓ | T2 | 5 | Microsoft Learn "Get started with Microsoft Fabric" path (free) — https://learn.microsoft.com/en-us/training/paths/get-started-fabric/ | 5 |
| A.5 | KQL & the Kusto engine stack (Eventhouse / Azure Data Explorer / Azure Monitor logs) — pervasive in Azure observability, Sentinel SIEM, and audit-evidence queries; absent from the taxonomy | DP-700/DP-600 ✓ | T2 | 5 | Microsoft Learn "Write your first query with KQL" + KQL path (free) — https://learn.microsoft.com/en-us/training/modules/write-first-query-kusto-query-language/ | 4 |
| A.6 | Kubernetes & container orchestration (pods/services/ingress, Helm, operators, AKS; GitOps with Argo CD; service mesh at awareness) — named weak spot, substrate for Spark/Flink/Airflow executors and every CNCF tool in this plan; the taxonomy assumes it silently | roadmap.sh devops ✓ (GitOps/service-mesh nodes subsumed here) | T2 | 5 | Official Kubernetes tutorials + a local kind/k3d cluster; "Kubernetes: Up & Running" as alternate | 12 |
| A.22 | Relational database administration & HA depth (streaming/logical replication topologies, Patroni-style failover, connection pooling, PITR, vacuum/WAL operations) — complements the internals entry 3.2.1: how the engines behind TA/fund-accounting systems behave under load and failover | roadmap.sh postgresql-dba ✓ | T2 | 5 | *The Internals of PostgreSQL* (Suzuki, free) — https://www.interdb.jp/pg/ — replication/WAL/vacuum chapters | 4 |
| A.25 | Warehouse performance engineering (query-profile analysis, compute sizing, clustering keys & micro-partition pruning, search optimization, materialized views) — a full scored domain in both architect exams; the cost/deadline lever for regulatory reporting windows | SnowPro Adv Architect + AWS SAP-C02 ✓ | T2 | 5 | Snowflake "Exploring and optimizing performance" guide (concepts transfer to any MPP warehouse) — https://docs.snowflake.com/en/guides-overview-performance | 4 |
| A.26 | Resilience testing & chaos engineering (failure injection, game days, DR exercises) — DORA mandates operational-resilience *testing*, not just planning; the hands-on complement to A.15 | AWS SAP-C02 ✓ | T3 | 5 | Principles of Chaos Engineering — https://principlesofchaos.org/ + Azure Chaos Studio docs | 2 |

### Architecture practice (scheduled in Phase 8)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.7 | Architecture styles & trade-off analysis as a discipline (layered/SOA/microservices/event-driven; quantifying trade-offs; presenting and defending decisions) | roadmap.sh software-architect ✓ | T2 | 8 | *Software Architecture: The Hard Parts* (Ford et al.) pt. I–II + Software Architecture Monday lessons — https://www.developertoarchitect.com/lessons/ | 4 |
| A.8 | Business architecture: capability maps, value streams, information mapping — how an architect scopes data domains/products (NAV, TA, regulatory reporting) and ties investment to business outcomes | TOGAF 10 Series Guides ✓ | T2 | 8 | TOGAF Series Guides: Business Capabilities; Value Streams; Information Mapping (free with Open Group registration) — https://www.opengroup.org/togaf/series-guides | 4 |
| A.9 | EA governance & the architecture operating model (architecture boards, architecture contracts, compliance reviews, maturity, roles) — the process through which designs get approved and funded in CSSF-regulated entities | TOGAF 10 ✓ | T2 | 8 | TOGAF 10 Fundamental Content: "EA Capability and Governance" (free with registration) | 3 |
| A.10 | Architecture roadmapping & migration planning (transition architectures, plateaus/gaps, work packages) — how multi-year platform modernizations are sold and steered | TOGAF ADM E–F + ArchiMate 3.2 ch. 12 ✓ | T2 | 8 | ArchiMate 3.2 spec ch. 12 + TOGAF ADM Phases E–F (free with registration) | 3 |
| A.11 | Agile EA practice (intentional vs emergent architecture; architecture runway in sprint-based delivery) | TOGAF Series Guides ✓ | T3 | 8 | TOGAF Series Guide: Enabling Enterprise Agility (free with registration) | 1 |
| A.12 | API/application security basics (OWASP API Top 10: BOLA, injection; PKI/hashing literacy) — data products exposing regulated fund data must survive AppSec review | roadmap.sh software-architect ✓ | T3 | 8 | OWASP API Security Top 10 (2023) — https://owasp.org/API-Security/ | 2 |
| A.13 | ITSM & delivery frameworks (ITIL change/incident/release; SAFe awareness) — change advisory boards are how platform changes ship in Luxembourg institutions, reinforced by DORA | roadmap.sh software-architect ✓ | T3 | 8 | Atlassian ITIL 4 primer — https://www.atlassian.com/itsm/itil | 1.5 |

### Governance, risk & organizational practice (scheduled in Phase 6)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.14 | Data strategy, business case, funding & target operating model (DCAM components 1–4: roles, RACI, stewardship org) — half of DCAM is program-building, not technology | EDM Council DCAM v3 ✓ | T2 | 6 | DCAM v3 overview — https://edmcouncil.org/frameworks/dcam/ + DAMA-DMBOK ch. 1 | 4 |
| A.15 | Architecture-level risk management (TOGAF risk technique, Open FAIR flavor; DORA ICT-risk framing) — designs must be justified in risk language to second-line functions | TOGAF 10 ✓ | T2 | 6 | TOGAF Series Guide: Integrating Risk and Security (free with registration) | 3 |
| A.16 | Data risk & control environment (control inventories, three lines of defense, evidence/attestation; CDMC 14 Key Controls) | DCAM/CDMC ✓ | T3 | 6 | CDMC 14 Key Controls & Automations (free request) — https://edmcouncil.org/frameworks/cdmc/14-key-controls/ | 2 |
| A.17 | Data handling ethics (bias, responsible use; GDPR fairness, EU AI Act expectations) | DAMA-DMBOK2 ch. 2 ✓ | T3 | 6 | DAMA-DMBOK2 Revised, ch. 2 | 1 |
| A.18 | Purpose-based consumption & data sharing agreements (CDMC "Data Consumption Purpose" control) — distributor/TA data sharing needs documented purpose beyond GDPR consent | CDMC ✓ | T3 | 6 | CDMC v1.1, Data Accessibility & Usage component (free download) — https://edmcouncil.org/frameworks/cdmc/ | 1 |
| A.19 | Records & content management as a discipline (retention of prospectuses/KIDs/board minutes under CSSF & MiFID rules; e-discovery) | DAMA-DMBOK2 ch. 9 ✓ | T3 | 6 | DAMA-DMBOK2 Revised, ch. 9 | 1.5 |
| A.20 | Organizational change management for data initiatives (adoption of catalogs/governance; Kotter-style change practice) | DAMA-DMBOK2 ch. 17 ✓ | T3 | 6 | DAMA-DMBOK2 Revised, ch. 17 | 1.5 |

### AI/ML (scheduled in Phase 7)

| ID | Topic | Source | Tier | Phase | Primary resource | Est. h |
|---|---|---|---|---|---|---|
| A.21 | LLM agent patterns & prompt/context-engineering fundamentals (tool use, structured output, ReAct-style agentic workflows, context management) — the taxonomy covers RAG and LLMOps but not agent design, which document-processing platforms increasingly use | roadmap.sh ai-engineer ✓ | T3 | 7 | Anthropic "Building Effective Agents" engineering guide + provider prompt-engineering docs | 2 |
| A.23 | Model Context Protocol (MCP) — the emerging open standard for connecting AI agents to data platforms; Databricks/Snowflake/Microsoft are shipping MCP servers, and "expose governed fund data to AI assistants" will be asked of this architect | roadmap.sh ai-engineer ✓ (dedicated top-level topic) | T2 | 7 | Official MCP documentation (architecture + build-a-server tutorial) — https://modelcontextprotocol.io | 3 |
| A.24 | LLM application security & guardrails (prompt injection, sensitive-data disclosure, excessive agency, adversarial testing) — distinct threat model from A.12; required control vocabulary for GenAI over client/regulatory data under DORA & EU AI Act | roadmap.sh ai-engineer ✓ | T3 | 7 | OWASP Top 10 for LLM & GenAI Applications (2025) — https://genai.owasp.org/llm-top-10/ | 2 |

**Appendix A total: ≈ 173 h** (counted in the budget; of which 90 h are the Phase-0 foundations A.27–A.31, each individually skippable via the Skip List).

### Considered and judged already covered (not gaps)

- **Relational DBMS internals** (CMU 15-445; postgresql-dba roadmap ✓) — the taxonomy names only the databases, but this plan already embeds the internals discipline as the T1 entry 3.2.1; the administration/HA slice that 3.2.1 does *not* cover became A.22.
- **Linux command line & shell craft** (postgresql-dba/devops roadmaps ✓) — initially judged covered by the learner profile; rescheduled as **A.27 in Phase 0** after the learner's instruction to assume nothing.
- **Kafka depth (CCDAK scope ✓: fundamentals, Streams, Connect, testing, observability)** — maps fully onto 2.4.1, 4.2.1, 2.2.2, 9.4.3, 12.7.2 entries; CCDAK adds depth, not breadth. Free prep guide via https://www.confluent.io/certification/.
- **Data-engineer roadmap (✓ via the roadmap content repo) & DE Zoomcamp module list** (Docker/Terraform, orchestration, dbt, Spark, Kafka, warehousing) — maps 1:1 onto Phases 2–5; Zoomcamp repo: https://github.com/DataTalksClub/data-engineering-zoomcamp (GCP-centric; use as pattern reference with Azure equivalents).
- **AWS SAP-C02 scope ✓** (multi-account governance, DR strategy by RTO/RPO, migration) — covered by 8.1.1 (CAF as the Azure analogue), 12.2.2, and A.10; the free exam-guide PDF is a strong professional-architect competency checklist: https://d1.awsstatic.com/training-and-certification/docs-sa-pro/AWS-Certified-Solutions-Architect-Professional_Exam-Guide.pdf.
- **SnowPro Advanced Architect scope ✓** (RBAC/masking/sharing/replication/Iceberg on Snowflake) — covered by 3.1.1, 11.1.2, 11.3.x, 13.3.2 at evaluation level; its performance domain became A.25.
- **GitOps, service mesh, artifact management** (devops roadmap ✓) — subsumed into A.6 (Kubernetes) and 9.3.1 (CI/CD).
- **Azure Cloud Design Patterns catalog** — not a gap (patterns 1.8.x cover the data-relevant set) but adopted as a primary resource in Phase 4: https://learn.microsoft.com/en-us/azure/architecture/patterns/ ✓.
- **DMBOK maturity assessment (ch. 15) / org & roles (ch. 16)** — covered by the DCAM T1 entry (1.12.12) and A.14.
- **Frontend frameworks, enterprise app vendors (SAP/Salesforce), microfrontends** — out of role; excluded.


<a id="appendix-b"></a>
## Appendix B — Reading Order

Consolidated book/course list with chapter→phase mapping. **Primary** = the one resource for its topic entries; **Alternate** = named substitute; **Parallel** = domain reading recommended alongside (commute-grade, drawn from the plan's slack, not the entry budget).

| # | Phase | Resource | What to read | Role |
|---|---|---|---|---|
| 1 | 1 | Kleppmann, *Designing Data-Intensive Applications* (latest ed.) | ch. 2–3 (models, storage), 5 (replication), 7 (transactions), 9 (consistency & consensus) | Primary (1.5.x, 1.6.x, 1.7.x, 1.8.9) |
| 2 | 1 | CMU 15-445 Database Systems (free course) — https://15445.courses.cs.cmu.edu/spring2025/schedule.html | ~14 lectures: storage, buffer pool, indexes, joins, optimization, MVCC, recovery | Primary (3.2.1) |
| 3 | 1 | Petrov, *Database Internals* | Part I | Alternate to #2 |
| 4 | 1 | Kimball & Ross, *The Data Warehouse Toolkit* 3rd ed. | ch. 1–4 + ch. 19 (financial services) | Primary (8.2.4) |
| 5 | 1 | Corr & Stagnitto, *Agile Data Warehouse Design* | BEAM workshop chapters | Alternate to #4 |
| 6 | 1 | DAMA-DMBOK (2nd/Revised ed.) | ch. 5 (modeling) | Primary (8.2.1–8.2.3) |
| 7 | 1 | MIT 6.5840 Distributed Systems (free) — https://pdos.csail.mit.edu/6.824/schedule.html | lectures 4, 6–9, 13 (+ 20–21 for A.2); Raft paper | Primary (A.1, A.2) |
| 8 | 2 | Cyr & Dorsey, *Analytics Engineering with SQL and dbt* | full | Primary (5.2.1/5.3.1) |
| 9 | 2 | Linstedt & Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0* | ch. 1–7 (modeling), 11–12 (loading) | Primary (8.2.5) |
| 10 | 2 | Inmon et al., *Building the Data Lakehouse* | skim, warehouse-veteran perspective | Primary (3.1.4, paired with the CIDR Lakehouse paper) |
| 11 | 2 | *Apache Iceberg: The Definitive Guide* (free via Dremio) | format + maintenance chapters | Alternate (3.4.2) |
| 12 | 2 | *Trino: The Definitive Guide* (free via Starburst) | core + Iceberg connector chapters | Alternate (4.3.1) |
| 13 | 2 | Pozen & Hamacher, *The Fund Industry* | full | Parallel (domain grounding) |
| 14 | 2 | Fowler & David, *The Informed Company* | maturity-stages chapters | Optional (3.1.x context) |
| 15 | 3 | Damji et al., *Learning Spark* 2nd ed. (free PDF, Databricks) | ch. 1–7 + 12 (tuning) | Primary (4.1.1) |
| 16 | 3 | Harenslak & de Ruiter, *Data Pipelines with Apache Airflow* 2nd ed. | ch. 1–6, 12 | Primary (5.6.1, with Dagster docs) |
| 17 | 3 | Forsgren et al., *Accelerate* | part I | Optional (9.3.x culture; DORA-metrics vocabulary) |
| 18 | 4 | Shapira et al., *Kafka: The Definitive Guide* 2nd ed. (free PDF, Confluent) | ch. 1–8 + 10 | Primary (2.4.1, 1.8.2) |
| 19 | 4 | Akidau et al., *Streaming Systems* | ch. 1–4 (+ ch. 7 skim) | Primary (1.9.x) |
| 20 | 4 | Stopford, *Designing Event-Driven Systems* (free PDF, Confluent) | event sourcing/CQRS + Kafka-patterns chapters | Primary (1.8.5/1.8.6) |
| 21 | 4 | Weiss, *After the Trade Is Made* 3rd ed. | settlement/custody chapters | Parallel (domain grounding for streams you model) |
| 22 | 4 | Simmons, *Securities Operations* | trade lifecycle + corporate actions chapters | Alternate to #21 |
| 23 | 5 | Brikman, *Terraform: Up & Running* 3rd ed. | concept chapters (state, modules, testing) | Primary (9.10.1, with OpenTofu docs) |
| 24 | 5 | Dotson, *Practical Cloud Security* 2nd ed. | IAM + network + encryption chapters | Optional (bridges P5→P6 security) |
| 25 | 5 | Google SRE Book / Workbook (free online) | postmortem, capacity, SLO chapters | Primary (12.4.1 in P8; T3 reads in P5) |
| 26 | 6 | Moses et al., *Data Quality Fundamentals* | ch. 1–4 + observability chapters | Primary (9.4.2/10.4.1, 10.9.x) |
| 27 | 6 | DAMA-DMBOK (Revised ed.) | ch. 10 (R&MD), 13 (metadata), 15 (maturity); ch. 1, 2, 9, 17 for A.14/17/19/20 | Primary (10.5.1, 10.6.1; A items) |
| 28 | 6 | Bhajaria, *Data Privacy: A Runbook for Engineers* | PII handling + consent chapters | Alternate (11.3.x–11.5.x) |
| 29 | 6 | Seiner, *Non-Invasive Data Governance* | operating-model chapters | Optional (A.14 counterweight — low-friction governance) |
| 30 | 6 | Loader, *Fund Custody and Administration* | NAV calc + transfer agency chapters | Parallel (domain grounding for MDM/reporting) |
| 31 | 7 | Huyen, *Designing Machine Learning Systems* | ch. 1–2, 7–9 | Primary (6.4.1) |
| 32 | 7 | Bouchard & Peters, *Building LLMs for Production* | RAG + evaluation chapters | Alternate (6.6.2/6.8.2) |
| 33 | 7 | Burkov, *Machine Learning Engineering* | lifecycle chapters | Optional (compact 6.4.x refresher) |
| 34 | 8 | Khononov, *Learning Domain-Driven Design* | ch. 1–11 (strategic) | Primary (8.4.1) |
| 35 | 8 | Jones, *Driving Data Quality with Data Contracts* | full | Primary (13.1.1) |
| 36 | 8 | Dehghani, *Data Mesh* | parts I–II (skim III) | Primary (1.4.4) |
| 37 | 8 | Strengholt, *Data Management at Scale* 2nd ed. | architecture-survey + federated-governance chapters | Primary counterweight to #36 (also 1.4.6 T3 read in P2) |
| 38 | 8 | Ford et al., *Software Architecture: The Hard Parts* | parts I–II | Primary (A.7) |
| 39 | 8 | Ford et al., *Building Evolutionary Architectures* 2nd ed. | fitness-functions chapters | Optional (evolution lens on your ADR/exit-criteria practice) |
| 40 | 8 | TOGAF 10 Fundamental Content + ArchiMate 3.2 spec (free, Open Group registration) | Core Concepts + ADM; ArchiMate ch. on layers + ch. 12 | Primary (8.1.3, A.8–A.11) |
| 41 | 8 | Knaflic, *Storytelling with Data* | ch. 1–2 | T3 read (14.2.1) |

Course-shaped extras already embedded in entries: Microsoft Learn paths (AZ-700 → A.3, Fabric → A.4, KQL → A.5, Bicep → 9.10.2), DataTalksClub DE Zoomcamp as a free hands-on pattern library (Phases 2–5, GCP-centric — substitute Azure equivalents), *The Internals of PostgreSQL* (free, A.22), MIT *Missing Semester* (unscheduled refresher).


<a id="appendix-c"></a>
## Appendix C — Coverage Matrix

All 252 taxonomy subcategory IDs, each exactly once. IDs follow the canonical parse:
subcategory = bold bullet item; concept categories 1.8/1.9 per concept; 1.10 as one
unit; 1.11 as 3 groups; 1.12 per standard; the taxonomy's own cross-reference pointers
(5.5, 6.5, 10.8) carry IDs and are resolved in [Excluded](#excluded). Gap additions
A.1–A.31 are tracked in [Appendix A](#appendix-a). Tier `—` = excluded item. Phase 0
items are taught from zero and individually skippable via the Skip List tests.

| Taxonomy ID | Topic | Tier | Phase |
|---|---|---|---|
| 1.1.1 | Structured data | T3 | Phase 0 |
| 1.1.2 | Semi-structured data | T3 | Phase 0 |
| 1.1.3 | Unstructured data | T3 | Phase 0 |
| 1.1.4 | Vector / embeddings | T2 | Phase 7 |
| 1.2.1 | Batch paradigm | T3 | Phase 0 |
| 1.2.2 | Micro-batch | T2 | Phase 4 |
| 1.2.3 | Streaming paradigm | T2 | Phase 4 |
| 1.2.4 | Real-time / low-latency | T3 | Phase 4 |
| 1.3.1 | OLTP | T2 | Phase 0 |
| 1.3.2 | OLAP | T2 | Phase 0 |
| 1.3.3 | HTAP | T3 | Phase 1 |
| 1.3.4 | RT / user-facing analytics | T3 | Phase 4 |
| 1.4.1 | Lambda architecture | T2 | Phase 4 |
| 1.4.2 | Kappa architecture | T2 | Phase 4 |
| 1.4.3 | Medallion | T1 | Phase 2 |
| 1.4.4 | Data Mesh | T2 | Phase 8 |
| 1.4.5 | Data Fabric | T3 | Phase 8 |
| 1.4.6 | Hub-and-Spoke | T3 | Phase 2 |
| 1.4.7 | Data Vault (pattern) | T2 | Phase 2 |
| 1.5.1 | Row vs columnar | T2 | Phase 1 |
| 1.5.2 | MPP | T2 | Phase 1 |
| 1.5.3 | Shared-nothing vs shared-disk | T2 | Phase 1 |
| 1.5.4 | Storage/compute separation | T2 | Phase 1 |
| 1.6.1 | ACID & isolation levels | T1 | Phase 1 |
| 1.6.2 | BASE | T3 | Phase 1 |
| 1.6.3 | Eventual consistency | T2 | Phase 1 |
| 1.6.4 | Strong consistency | T2 | Phase 1 |
| 1.6.5 | RYW / monotonic / causal | T2 | Phase 1 |
| 1.7.1 | CAP | T1 | Phase 1 |
| 1.7.2 | PACELC | T1 | Phase 1 |
| 1.8.1 | Idempotency | T1 | Phase 1 |
| 1.8.2 | Delivery semantics | T1 | Phase 4 |
| 1.8.3 | Outbox pattern | T1 | Phase 4 |
| 1.8.4 | Saga pattern | T1 | Phase 4 |
| 1.8.5 | Event sourcing | T1 | Phase 4 |
| 1.8.6 | CQRS | T2 | Phase 4 |
| 1.8.7 | Dead-letter queue | T2 | Phase 4 |
| 1.8.8 | Backpressure | T2 | Phase 4 |
| 1.8.9 | Two-phase commit | T2 | Phase 1 |
| 1.8.10 | CDC (pattern) | T1 | Phase 4 |
| 1.8.11 | Strangler fig | T2 | Phase 8 |
| 1.8.12 | Bulkhead | T3 | Phase 4 |
| 1.8.13 | Circuit breaker | T3 | Phase 4 |
| 1.9.1 | Watermarks | T1 | Phase 4 |
| 1.9.2 | Windowing | T1 | Phase 4 |
| 1.9.3 | Late data handling | T2 | Phase 4 |
| 1.9.4 | Event vs processing time | T1 | Phase 4 |
| 1.9.5 | Triggers | T2 | Phase 4 |
| 1.9.6 | Stateful vs stateless | T2 | Phase 4 |
| 1.9.7 | Schema evolution compatibility | T1 | Phase 4 |
| 1.10.1 | Modeling notations (overview) | T2 | Phase 1 |
| 1.11.1 | Data protocols (HTTP…ADBC) | T2 | Phase 4 |
| 1.11.2 | Serialization formats | T2 | Phase 4 |
| 1.11.3 | Async API standards | T2 | Phase 4 |
| 1.12.1 | ISO 20022 | T1 | Phase 2 |
| 1.12.2 | LEI (ISO 17442) | T2 | Phase 2 |
| 1.12.3 | ISIN | T2 | Phase 2 |
| 1.12.4 | CFI | T3 | Phase 2 |
| 1.12.5 | FIGI | T3 | Phase 2 |
| 1.12.6 | FIBO | T2 | Phase 6 |
| 1.12.7 | EMT/EPT (FinDatEx) | T1 | Phase 2 |
| 1.12.8 | SWIFT MT/MX | T2 | Phase 2 |
| 1.12.9 | FpML | T3 | Phase 2 |
| 1.12.10 | FIX | T3 | Phase 2 |
| 1.12.11 | IBAN / SEPA | T3 | Phase 2 |
| 1.12.12 | DCAM | T1 | Phase 6 |
| 2.1.1 | ELT connectors | T2 | Phase 2 |
| 2.1.2 | Bulk load utilities | T2 | Phase 5 |
| 2.2.1 | Log/metric shippers | T3 | Phase 5 |
| 2.2.2 | Stream connectors | T2 | Phase 4 |
| 2.3.1 | Log-based CDC | T1 | Phase 4 |
| 2.3.2 | Trigger-based CDC | T3 | Phase 4 |
| 2.3.3 | Snapshot-based CDC | T3 | Phase 4 |
| 2.4.1 | Distributed logs (Kafka) | T1 | Phase 4 |
| 2.4.2 | Message brokers | T2 | Phase 4 |
| 2.4.3 | Event mesh | T3 | Phase 4 |
| 2.5.1 | iPaaS | T3 | Phase 5 |
| 2.5.2 | ESB (legacy) | T3 | Phase 5 |
| 2.6.1 | API gateways | T2 | Phase 8 |
| 2.6.2 | GraphQL layers | T3 | Phase 8 |
| 2.7.1 | Reverse ETL | T3 | Phase 8 |
| 3.1.1 | Cloud data warehouse | T2 | Phase 2 |
| 3.1.2 | On-prem MPP warehouse | T3 | Phase 2 |
| 3.1.3 | Data lake | T2 | Phase 2 |
| 3.1.4 | Data lakehouse | T1 | Phase 2 |
| 3.2.1 | OLTP / relational internals | T1 | Phase 1 |
| 3.2.2 | NoSQL document | T3 | Phase 1 |
| 3.2.3 | NoSQL key-value | T3 | Phase 1 |
| 3.2.4 | NoSQL wide-column | T3 | Phase 1 |
| 3.2.5 | Property graph | T3 | Phase 6 |
| 3.2.6 | Knowledge graph / RDF | T2 | Phase 6 |
| 3.2.7 | Time-series | T3 | Phase 5 |
| 3.2.8 | Search | T3 | Phase 7 |
| 3.2.9 | Vector storage | T2 | Phase 7 |
| 3.2.10 | HTAP stores | T3 | Phase 1 |
| 3.2.11 | Geospatial | T3 | Phase 2 |
| 3.3.1 | Object storage | T2 | Phase 2 |
| 3.3.2 | Block storage | T3 | Phase 5 |
| 3.3.3 | File storage | T3 | Phase 5 |
| 3.3.4 | Caching | T2 | Phase 5 |
| 3.4.1 | File formats | T1 | Phase 2 |
| 3.4.2 | Table formats | T1 | Phase 2 |
| 3.4.3 | Table-format catalogs | T2 | Phase 2 |
| 4.1.1 | Distributed batch engines | T1 | Phase 3 |
| 4.1.2 | Serverless compute | T2 | Phase 5 |
| 4.2.1 | Stateful stream processing | T1 | Phase 4 |
| 4.2.2 | Cloud-native streaming | T2 | Phase 5 |
| 4.3.1 | MPP SQL engines | T2 | Phase 2 |
| 4.3.2 | Cloud query services | T2 | Phase 5 |
| 4.3.3 | Embedded / single-node | T2 | Phase 2 |
| 4.3.4 | RT/user-facing analytics engines | T3 | Phase 4 |
| 4.3.5 | Streaming databases | T3 | Phase 4 |
| 4.4.1 | General distributed frameworks | T3 | Phase 3 |
| 4.4.2 | Specialized frameworks | T3 | Phase 3 |
| 5.1.1 | Visual ETL | T3 | Phase 5 |
| 5.1.2 | Code-first ETL | T3 | Phase 3 |
| 5.2.1 | In-warehouse SQL ELT (dbt) | T1 | Phase 2 |
| 5.2.2 | ELT orchestrated | T2 | Phase 2 |
| 5.3.1 | SQL transformation layer | T1 | Phase 2 |
| 5.3.2 | Code transformation (DataFrames) | T2 | Phase 3 |
| 5.3.3 | Alternative query languages | T3 | Phase 2 |
| 5.4.1 | Interactive prep | T3 | Phase 2 |
| 5.4.2 | Code-first wrangling | T2 | Phase 0 |
| 5.5.1 | Reverse ETL (pointer) | — | Excluded |
| 5.6.1 | Workflow orchestrators | T1 | Phase 3 |
| 5.6.2 | Cloud-native orchestration | T2 | Phase 5 |
| 5.6.3 | Data-aware orchestration | T2 | Phase 3 |
| 5.6.4 | Durable execution | T2 | Phase 4 |
| 5.6.5 | BPM / process orchestration | T2 | Phase 4 |
| 6.1.1 | OS feature stores | T2 | Phase 7 |
| 6.1.2 | Managed feature stores | T3 | Phase 7 |
| 6.2.1 | Training frameworks | T3 | Phase 7 |
| 6.2.2 | Distributed training | T3 | Phase 7 |
| 6.2.3 | Managed training | T3 | Phase 7 |
| 6.3.1 | OS model serving | T3 | Phase 7 |
| 6.3.2 | Managed endpoints | T3 | Phase 7 |
| 6.4.1 | E2E MLOps platforms | T2 | Phase 7 |
| 6.4.2 | Managed MLOps | T2 | Phase 7 |
| 6.5.1 | Vector DBs (pointer) | — | Excluded |
| 6.6.1 | Embedding models | T2 | Phase 7 |
| 6.6.2 | RAG frameworks | T2 | Phase 7 |
| 6.6.3 | RAG platforms | T2 | Phase 7 |
| 6.7.1 | OS experiment tracking | T3 | Phase 7 |
| 6.7.2 | Managed tracking | T3 | Phase 7 |
| 6.8.1 | Prompt mgmt & tracing | T2 | Phase 7 |
| 6.8.2 | LLM evaluation | T2 | Phase 7 |
| 7.1.1 | OS semantic layer | T2 | Phase 8 |
| 7.1.2 | Platform semantic layers | T2 | Phase 8 |
| 7.2.1 | Metrics layer | T2 | Phase 8 |
| 7.3.1 | Business glossary | T2 | Phase 6 |
| 7.3.2 | Glossary in catalogs | T3 | Phase 6 |
| 8.1.1 | Cloud provider reference arch | T1 | Phase 5 |
| 8.1.2 | Vendor reference arch | T2 | Phase 5 |
| 8.1.3 | Industry reference (TOGAF/DMBOK) | T2 | Phase 8 |
| 8.2.1 | Conceptual modeling | T1 | Phase 1 |
| 8.2.2 | Logical modeling | T1 | Phase 1 |
| 8.2.3 | Physical modeling | T1 | Phase 1 |
| 8.2.4 | Dimensional modeling | T1 | Phase 1 |
| 8.2.5 | Data Vault modeling | T1 | Phase 2 |
| 8.2.6 | Anchor / 6NF | T3 | Phase 2 |
| 8.3.1 | Schema registries | T2 | Phase 4 |
| 8.3.2 | Schema languages | T2 | Phase 4 |
| 8.4.1 | Domain-driven design | T1 | Phase 8 |
| 8.5.1 | Architecture notations & tools | T1 | Phase 1 |
| 9.1.1 | IDEs | T3 | Phase 0 |
| 9.1.2 | Notebooks | T3 | Phase 0 |
| 9.1.3 | Local data sandboxes | T2 | Phase 1 |
| 9.2.1 | Git & hosting | T2 | Phase 0 |
| 9.2.2 | Data versioning | T2 | Phase 3 |
| 9.3.1 | CI/CD pipelines | T2 | Phase 3 |
| 9.3.2 | Data-specific CI | T2 | Phase 3 |
| 9.4.1 | Unit testing | T2 | Phase 0 |
| 9.4.2 | Data quality testing | T1 | Phase 6 |
| 9.4.3 | Integration testing | T2 | Phase 3 |
| 9.4.4 | Load/perf testing | T3 | Phase 3 |
| 9.5.1 | Code review | T3 | Phase 0 |
| 9.5.2 | Data diff | T3 | Phase 3 |
| 9.6.1 | Code docs | T3 | Phase 3 |
| 9.6.2 | Data docs | T2 | Phase 2 |
| 9.7.1 | Schema migrations | T2 | Phase 3 |
| 9.8.1 | Synthetic data | T2 | Phase 6 |
| 9.8.2 | Test data management | T3 | Phase 6 |
| 9.9.1 | Notebooks in production | T3 | Phase 3 |
| 9.10.1 | Cloud-agnostic IaC | T1 | Phase 5 |
| 9.10.2 | Cloud-native IaC | T2 | Phase 5 |
| 9.10.3 | Configuration management | T3 | Phase 5 |
| 10.1.1 | Active metadata platforms | T1 | Phase 6 |
| 10.1.2 | Enterprise catalogs | T2 | Phase 6 |
| 10.2.1 | AI-native discovery | T3 | Phase 6 |
| 10.2.2 | Catalog-embedded discovery | T3 | Phase 6 |
| 10.3.1 | Lineage (standards) | T1 | Phase 6 |
| 10.3.2 | Lineage in catalogs | T3 | Phase 6 |
| 10.4.1 | OS data quality | T1 | Phase 6 |
| 10.4.2 | Managed/enterprise DQ | T2 | Phase 6 |
| 10.4.3 | Data profiling | T2 | Phase 6 |
| 10.5.1 | Master data management | T1 | Phase 6 |
| 10.5.2 | Modern / cloud MDM | T3 | Phase 6 |
| 10.6.1 | Reference data management | T2 | Phase 6 |
| 10.6.2 | RDM inside MDM | T3 | Phase 6 |
| 10.7.1 | Lifecycle / retention (cloud) | T2 | Phase 6 |
| 10.7.2 | Enterprise ILM | T3 | Phase 6 |
| 10.8.1 | Audit & compliance (pointer) | — | Excluded |
| 10.9.1 | Pipeline observability | T2 | Phase 6 |
| 10.9.2 | OS data observability | T2 | Phase 6 |
| 11.1.1 | Identity providers | T2 | Phase 6 |
| 11.1.2 | Fine-grained access control | T1 | Phase 6 |
| 11.1.3 | Policy-as-code | T2 | Phase 6 |
| 11.2.1 | Key management | T2 | Phase 6 |
| 11.2.2 | Database encryption / TDE | T3 | Phase 6 |
| 11.3.1 | Masking / tokenization | T2 | Phase 6 |
| 11.3.2 | Built-in DB masking | T2 | Phase 6 |
| 11.4.1 | PII detection & redaction | T2 | Phase 6 |
| 11.5.1 | Privacy / consent mgmt | T3 | Phase 6 |
| 11.6.1 | Audit logging / SIEM | T2 | Phase 6 |
| 11.7.1 | Regulatory compliance frameworks | T1 | Phase 6 |
| 11.8.1 | Secrets management | T2 | Phase 5 |
| 12.1.1 | Cloud-native backup | T2 | Phase 5 |
| 12.1.2 | Enterprise backup | T3 | Phase 5 |
| 12.2.1 | DR tooling | T3 | Phase 5 |
| 12.2.2 | DR patterns | T1 | Phase 5 |
| 12.3.1 | FinOps / cost mgmt | T1 | Phase 5 |
| 12.3.2 | Data-specific FinOps | T2 | Phase 5 |
| 12.4.1 | SLA/SLO management | T2 | Phase 8 |
| 12.5.1 | On-call / paging | T3 | Phase 5 |
| 12.5.2 | Postmortems | T3 | Phase 5 |
| 12.6.1 | Capacity planning | T3 | Phase 5 |
| 12.7.1 | Commercial APM | T3 | Phase 5 |
| 12.7.2 | OS observability stack | T2 | Phase 5 |
| 13.1.1 | Data contracts (tools) | T1 | Phase 8 |
| 13.1.2 | Data contract standards | T2 | Phase 8 |
| 13.2.1 | Mesh enabling platforms | T2 | Phase 8 |
| 13.3.1 | Internal marketplaces | T3 | Phase 8 |
| 13.3.2 | Cross-org sharing | T2 | Phase 8 |
| 13.3.3 | Commercial data marketplaces | T3 | Phase 8 |
| 13.4.1 | GraphQL data APIs | T3 | Phase 8 |
| 13.4.2 | REST data APIs | T2 | Phase 8 |
| 13.5.1 | Standalone CDPs | — | Excluded |
| 13.5.2 | Composable CDPs | — | Excluded |
| 14.1.1 | Modern cloud BI | T2 | Phase 8 |
| 14.1.2 | On-prem / legacy BI | T3 | Phase 8 |
| 14.1.3 | Open-source BI | T2 | Phase 8 |
| 14.2.1 | Viz libraries | T3 | Phase 8 |
| 14.3.1 | Embedded analytics | T3 | Phase 8 |
| 14.4.1 | Operational reporting | T3 | Phase 8 |
| 14.4.2 | Regulatory reporting | T1 | Phase 8 |
| 14.5.1 | Cloud notebooks | T3 | Phase 8 |
| 14.5.2 | Self-hosted notebooks | T3 | Phase 0 |
| 14.6.1 | Data app frameworks | T2 | Phase 8 |
| 14.6.2 | Internal tool builders | T3 | Phase 8 |
| 14.7.1 | Anomaly alerting | T3 | Phase 6 |
| 14.7.2 | Reverse-ETL activation | T3 | Phase 8 |
| 14.7.3 | Notification tools | T3 | Phase 5 |

**Coverage: 252/252 IDs.** Excluded: 5 · Phase 0: 13 · Phase 1: 26 · Phase 2: 33 · Phase 3: 16 · Phase 4: 40 · Phase 5: 31 · Phase 6: 38 · Phase 7: 19 · Phase 8: 31.


<a id="appendix-d"></a>
## Appendix D — Tool Equivalence Map

Build-vs-buy cheat sheet, one table per taxonomy domain, derived from the taxonomy's `(OS)/(SA)/(C)/(E)` tags and this plan's selections. **FOSS pick** = what you practice on (always free to run); **Corp/cloud leader** = what EU financial-services job ads and vendor selections name; the last column is the honest one-liner for when buying wins.

### 1 Fundamentals
| Category | FOSS pick (hands-on) | Corp/cloud leader (evaluate) | When the corporate option wins |
|---|---|---|---|
| Modeling notations (1.10) | draw.io, Mermaid, Structurizr Lite | Sparx EA, Visual Paradigm | regulated EA repository, multi-user model governance, traceability mandates |
| Financial standards tooling (1.12) | Python/lxml validators + free specs (ISO 20022, FinDatEx) | SWIFT tooling, vendor message libraries | filing connectivity and standard-version maintenance must be vendor-backed |

### 2 Connectivity
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Batch ELT connectors (2.1) | Airbyte OSS | Fivetran; Azure Data Factory | long-tail SaaS connectors with SLAs beat the ops cost of self-hosting |
| Streaming ingestion / shippers (2.2) | Fluent Bit, Vector, Kafka Connect | Datadog agents, Event Hubs Capture | bundled into a licensed observability/streaming estate |
| CDC (2.3) | Debezium | Qlik Replicate, Oracle GoldenGate, Fivetran HVR | exotic legacy sources (mainframe, large Oracle) + vendor accountability |
| Event streaming (2.4) | Apache Kafka / Redpanda | Confluent Cloud, Azure Event Hubs | scarce ops headcount, enterprise SLAs, Azure-native networking/identity |
| Message brokers (2.4) | RabbitMQ | Azure Service Bus | cloud-native sessions/dedup/DLQ features plus zero broker ops |
| Event mesh (2.4) | NATS (lightweight) | Solace PubSub+ | multi-site capital-markets WAN routing with governance |
| iPaaS / ESB (2.5) | n8n (SA) | Power Automate, Boomi, MuleSoft | citizen-integrator demand + certified SaaS connector catalogs |
| API gateways (2.6) | Kong OSS, Tyk | Azure API Management, Apigee | Azure policy/identity integration and enterprise developer portals |
| Reverse ETL (2.7) | custom SQL + API scripts | Hightouch, Census | many SaaS destinations with maintained, monitored connectors |

### 3 Storage
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Cloud DW (3.1) | DuckDB (dev proxy) | Snowflake, BigQuery, Synapse/Fabric | org-scale concurrency, governance, zero-ops elasticity |
| Data lake / object storage (3.1/3.3) | MinIO | ADLS Gen2, S3 | durability SLAs, lifecycle tiers, integrated IAM/audit |
| Lakehouse (3.1/3.4) | Iceberg + Trino on MinIO | Databricks, Snowflake-Iceberg, Fabric OneLake | managed optimization, bundled catalog/governance, vendor support |
| Table-format catalogs (3.4) | Lakekeeper, Apache Polaris, Nessie | Unity Catalog, AWS Glue, Snowflake Open Catalog | credential vending + governance bundled into the licensed estate |
| OLTP relational (3.2) | PostgreSQL | Azure SQL, Oracle, SQL Server | vendor app certification, incumbent DBA estate, HA SLAs |
| NoSQL document/KV/wide-column (3.2) | MongoDB-compatible, Valkey, Cassandra | Cosmos DB, DynamoDB | multi-region guarantees with zero ops |
| Graph / knowledge graph (3.2) | Neo4j CE; Apache Jena/Fuseki | Neo4j Aura, Stardog, Ontotext GraphDB | reasoning at scale, enterprise security, support contracts |
| Time-series (3.2) | Prometheus, TimescaleDB, QuestDB | InfluxDB Cloud; kdb+ | kdb+ remains the tick-data desk standard; managed retention at scale |
| Search (3.2) | OpenSearch, Meilisearch | Elastic Cloud, Algolia | managed relevance + SIEM bundling |
| Vector (3.2) | pgvector, Qdrant | Azure AI Search, Pinecone | ACL-aware retrieval (security trimming) + integrated RAG platform |
| Caching (3.3) | Valkey, Memcached | Azure Cache for Redis, ElastiCache | managed failover + compliance posture |

### 4 Compute
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Batch engines (4.1) | Apache Spark | Databricks, Synapse/Fabric Spark, EMR | Photon-class performance, notebook+governance bundle, support |
| Serverless (4.1) | Functions Core Tools (local) | Azure Functions, AWS Lambda | spiky event-scale pay-per-use with managed triggers |
| Stream processing (4.2) | Apache Flink, Kafka Streams | Confluent Flink, AWS Managed Flink, Azure Stream Analytics | SQL-first teams; managed checkpoints/scaling/upgrades |
| Federated SQL (4.3) | Trino | Starburst, Athena | connector breadth, fine-grained security add-ons, support |
| Embedded OLAP (4.3) | DuckDB | MotherDuck, ClickHouse Cloud | shared state and concurrency beyond one node |
| Real-time analytics (4.3) | ClickHouse, Pinot, Druid | Imply, Tinybird | RT cluster ops complexity at scale |
| Streaming databases (4.3) | RisingWave, Proton | Materialize | managed incremental views with SLAs |
| Distributed frameworks (4.4) | Ray, Dask | Anyscale, Coiled | managed autoscaling GPU fleets |

### 5 Processing
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Visual ETL (5.1) | Apache NiFi | Informatica, Talend, SSIS, ADF data flows | installed base, citizen-ETL mandates, governance integration |
| ELT / transformation (5.2/5.3) | dbt Core, SQLMesh | dbt Cloud, Coalesce, Dataform | bundled scheduler/IDE/semantic layer; faster team onboarding |
| Wrangling (5.4) | pandas, Polars (+ ydata-profiling) | Alteryx, Tableau Prep, Glue DataBrew | analyst self-service mandates |
| Orchestration (5.6) | Airflow, Dagster | ADF, MWAA, Cloud Composer, Dagster+ | managed control plane; hybrid runtimes (self-hosted IR) |
| Durable execution (5.6) | Temporal OSS | Temporal Cloud, Azure Durable Functions, Step Functions | ops burden of self-hosted state clusters |
| BPM (5.6) | Camunda 7 CE, Flowable | Camunda 8 Enterprise, Pega, Appian | human-task UX, audit packs, vendor support for regulated workflows |

### 6 AI/ML
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Feature stores (6.1) | Feast | Databricks FS, Tecton, SageMaker FS | low-latency online serving with SLAs |
| Training & serving (6.2/6.3) | PyTorch, sklearn; vLLM, BentoML | Azure ML, SageMaker, Vertex; Azure OpenAI | managed GPU fleets, RBAC/compliance integration |
| MLOps / registry (6.4/6.7) | MLflow | Azure ML registry, W&B, Databricks | enterprise RBAC, lineage integration, hosted collaboration |
| Embeddings & RAG (6.6) | sentence-transformers + LlamaIndex + Ollama | Azure OpenAI + Azure AI Search, Bedrock KBs | model quality, security trimming, scale, support |
| LLMOps (6.8) | Langfuse + Ragas/DeepEval | LangSmith, Azure AI Foundry | enterprise SSO/compliance and integrated eval suites |

### 7 Semantic
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Semantic / metrics layer (7.1/7.2) | Cube, MetricFlow | Power BI semantic models, Looker/LookML, AtScale | BI-suite gravity — licensing and skills already in-house |
| Business glossary (7.3) | OpenMetadata glossary | Collibra, Purview, Alation | stewardship workflows + attestation auditors recognize |

### 8 Architecture
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Reference frameworks (8.1) | WAF/CAF docs, TOGAF (free w/ registration) | — (frameworks are free; consulting is the product) | — |
| Data modeling tools (8.2) | draw.io, DBeaver ERD, Mermaid | erwin, ER/Studio, SqlDBM, Hackolade | model repository/governance and forward-engineering at enterprise scale |
| Data Vault automation (8.2) | dbt + AutomateDV | VaultSpeed, WhereScape | generated loading code at estate scale with vendor accountability |
| Schema registries (8.3) | Apicurio | Confluent SR, Azure Schema Registry | bundled with the managed Kafka estate |
| EA / process modeling (8.5) | Archi, Structurizr Lite, bpmn.io | Sparx EA, BiZZdesign, Visual Paradigm | multi-user EA repository, TOGAF tooling, audit trails |

### 9 Engineering Practice
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Data versioning (9.2) | lakeFS, Nessie, Iceberg branches | Snowflake clones, Databricks | versioning must live inside the licensed warehouse |
| CI/CD (9.3) | GitHub Actions, GitLab CI | Azure DevOps | org standard + enterprise compliance gates |
| Data-aware CI (9.3) | dbt slim CI, SQLMesh | Datafold, dbt Cloud CI | column-level diffs at scale with support |
| Testing (9.4) | pytest, Testcontainers, k6 | enterprise QA suites | regulated test-evidence management |
| Schema migrations (9.7) | Flyway CE, Alembic | Liquibase Pro, Redgate | policy checks, governance dashboards, DBA workflows |
| Synthetic / test data (9.8) | Faker, SDV | Mostly AI, Tonic, Gretel, Delphix | vendor-attested privacy guarantees; TDM across a legacy estate |
| IaC (9.10) | OpenTofu, Pulumi | Terraform Enterprise; Bicep (Azure-only) | org-scale state/policy management (Sentinel); Azure-mandate shops |
| Documentation (9.6) | MkDocs, dbt docs | Confluence stack | org standard, permissions, non-engineer authoring |

### 10 Governance
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Catalogs / metadata (10.1) | OpenMetadata, DataHub | Microsoft Purview, Collibra, Alation | connector coverage of closed SaaS + stewardship workflows + audit attestation |
| Lineage (10.3) | OpenLineage + Marquez | Purview, Collibra, Manta | parsing lineage out of closed tools (Informatica, SSIS, vendor ETL) |
| Data quality (10.4) | Soda Core, Great Expectations, Elementary | Informatica DQ, Monte Carlo, Soda Cloud | ML anomaly coverage at estate scale + managed incident workflows |
| Profiling (10.4) | ydata-profiling, whylogs | Informatica/Collibra profiling | embedded in the governance suite the org already runs |
| MDM (10.5) | Splink + Postgres hub | Informatica MDM, Semarchy, Reltio, Tamr | stewardship UI, survivorship governance, vendor accountability to regulators |
| Reference data (10.6) | dbt seeds + governed schema | Collibra RDM, CluedIn | approval workflow + audit for code-list changes at org scale |
| Retention / lifecycle (10.7) | MinIO/ADLS lifecycle + Iceberg maintenance | Veritas, Commvault ILM | legal-hold workflows across hybrid legacy estates |
| Data observability (10.9) | Elementary + OpenLineage | Monte Carlo, Acceldata, Databand | rule-free anomaly coverage + on-call integration |

### 11 Security & Compliance
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Identity (11.1) | Keycloak | Microsoft Entra ID, Okta | managed SSO, conditional access, compliance certifications |
| Fine-grained access (11.1) | Postgres RLS, Trino rules, Apache Ranger, OPA | Immuta, Privacera, Unity Catalog, Lake Formation | policy UX for non-engineers + cross-engine enforcement + audit reports |
| Policy-as-code (11.1) | OPA, Cedar | Immuta, PlainID | business-user policy authoring |
| Encryption / KMS (11.2) | OpenBao | Azure Key Vault, AWS KMS | HSM backing + attestations auditors accept |
| Masking / tokenization (11.3) | Postgres functions + Presidio transforms | Delphix, Protegrity, warehouse-native DDM | format-preserving tokenization at estate scale with key governance |
| PII detection (11.4) | Microsoft Presidio | AWS Macie, GCP DLP, BigID, Purview classifiers | coverage of SaaS/closed stores + classification governance |
| Audit / SIEM (11.6) | pgAudit + Loki/Elastic OSS | Microsoft Sentinel, Splunk | SOC integration, correlation content, regulatory reporting |
| Secrets (11.8) | OpenBao, SOPS | Azure Key Vault, AWS Secrets Manager | managed HSM + rotation integrations |
| Compliance automation (11.7) | — (manual evidence binders) | Vanta, Drata, OneTrust | continuous evidence collection once audits become annual rituals |

### 12 Operations
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Backup & DR (12.1/12.2) | pgBackRest, MinIO versioning, Velero | Azure Backup + ASR, Veeam, Rubrik, Zerto | enterprise estates, ransomware vaulting, compliance reporting |
| FinOps (12.3) | OpenCost + calculator-based models | Azure Cost Management, Cloudability, Vantage | multi-cloud chargeback and commitment management |
| SLO management (12.4) | Grafana SLO + Prometheus | Nobl9, Datadog SLOs | SLO governance across dozens of teams |
| Incident management (12.5) | Grafana OnCall | PagerDuty, Opsgenie | enterprise escalation policies + ecosystem integrations |
| Observability (12.6/12.7) | OTel + Prometheus + Grafana + Loki + Tempo | Azure Monitor, Datadog, Dynatrace | single-vendor APM depth and ML insights at enterprise scale |

### 13 Data Products
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| Data contracts (13.1) | ODCS + datacontract-cli + dbt contracts | Gable, Collibra contract features | producer-team UX and enterprise workflow integration |
| Mesh enablement (13.2) | Trino + OpenMetadata domains | Starburst, Databricks UC, Nextdata OS | federation governance and support at organization scale |
| Sharing (13.3) | delta-sharing reference server | Databricks Delta Sharing, Snowflake shares, Fabric sharing | recipient management, marketplace reach, egress engineering |
| Data APIs (13.4) | PostgREST/FastAPI + Kong | Azure APIM + managed backends | enterprise API governance and monetization features |

### 14 Consumption
| Category | FOSS pick | Corp/cloud leader | When the corporate option wins |
|---|---|---|---|
| BI (14.1) | Apache Superset, Metabase, Lightdash | Power BI (Azure default), Tableau, Looker | licensing gravity, self-service maturity, certified-content governance |
| Viz libraries (14.2) | Plotly, Vega-Lite, ECharts | Highcharts (commercial license) | embedding in commercial products with license/legal needs |
| Embedded analytics (14.3) | Cube embed, Superset embedding | Sigma, Looker Embed, Luzmo | multi-tenant security + vendor SLAs |
| Reporting (14.4) | JasperReports, BIRT | Power BI paginated; Workiva, AxiomSL, Wolters Kluwer (regulatory) | regulatory rule maintenance + filing connectivity outweigh build cost |
| Notebooks (14.5) | JupyterHub, Zeppelin | Hex, Deepnote, Databricks notebooks | collaboration + governance for mixed SQL/Python teams |
| Data apps (14.6) | Streamlit, Gradio, Dash | Power Apps, Retool | citizen-developer mandates + enterprise auth out of the box |
| Alerting & activation (14.7) | Grafana alerting | PagerDuty, Monte Carlo alerts, Hightouch | bundled with the observability/DQ/activation suite already licensed |
