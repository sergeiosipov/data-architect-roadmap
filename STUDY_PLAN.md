# Study Plan: Fundamentals → Data Architect

**Target:** top-tier Data Architect for financial services / the fund industry (Luxembourg: investment funds, asset management, regulatory data) — **starting from zero**. Nothing is assumed: Phase 0 teaches the computing foundations (Linux, Python, SQL, Git, Docker, networking), and every foundation module has an explicit **skip test** — you decide what you already know, the plan doesn't decide for you.
**Budget:** 6 h/week × 48 weeks × 4 years ≈ **1,152 h**. Full from-zero path: **1,100 h** = 927 h in phases + 173 h Appendix A gap additions (4.5% slack). Every Phase-0 skip test you pass returns its hours to slack; with all of Phase 0 skipped the load is **964 h** (16% slack).
**Tiers:** **T1 Master** — can design, implement, debug, and teach it (48 topics, 19%). **T2 Working** — can use, evaluate, integrate, and make build/buy decisions (109 topics, 43%). **T3 Awareness** — can recognize it, explain tradeoffs, know when to go deeper (90 topics, 36%).
**Tooling policy (dual-track):** every exercise and capstone runs on **FOSS/source-available, free, Docker-composable on a laptop**; each FOSS pick is paired with the **corporate/cloud leader** actually named in EU financial-services job ads and vendor selections (see [Appendix D](#appendix-d)). Primary cloud: **Azure**; AWS/Databricks/Snowflake at evaluation level.
**Coverage guarantee:** all 252 taxonomy subcategories appear exactly once — in a phase (0–8) or [Excluded](#excluded). [Appendix C](#appendix-c) is the authoritative matrix; the [Skip List](#skip-list) is a self-assessment gate, not a coverage bucket.
**Sequencing:** phases are ordered by prerequisite dependency, not taxonomy order; each phase's capstone reuses the previous one's artifacts, ending in one governed, productized fund-data platform.

<a id="how-to-use"></a>
## How to Use This Document

1. **Day one: take the [Skip List](#skip-list) tests.** Work through each Phase-0 skip test honestly, on a real machine, not in your head. Mark each module *do* or *skip*. That marked-up table is your personal starting line — revisit it only to downgrade a "skip" you regret.
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
- **Mobile tracker app.** This repo ships a companion PWA (`docs/`) generated from the same canonical worklist: every topic is a page with its study content, a **start/stop timer** that books time to that topic (it survives closing the app — elapsed time is computed from the start timestamp), status (todo/doing/done/skipped), per-topic journal notes, the skip-test bank, and hours-vs-budget dashboards. Host it free on GitHub Pages (or open `docs/index.html` directly on the phone). Progress lives in the browser's localStorage — use the ⬇ export button weekly and commit the JSON to the repo as your backup; ⬆ imports it on a new device.

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

| Phase | Theme | Months | Hours | Capstone |
|---|---|---|---|---|
| [0](#phase-0) | Computing & data foundations — from zero (skippable per module) | 1–6 | 46 | Personal data toolbox (Python + SQL + Docker + Git, reproducible) |
| [1](#phase-1) | Distributed data systems & modeling core | 7–11 | 118 | Fund reference OLTP + reporting mart (PostgreSQL, C4, ADRs) |
| [2](#phase-2) | Lakehouse & analytics engineering | 12–16 | 123 | Fund-document lakehouse (MinIO + Iceberg + dbt/DuckDB/Trino medallion) |
| [3](#phase-3) | Distributed compute, orchestration & engineering practice | 17–21 | 118 | Orchestrated Spark NAV pipeline (Dagster/Airflow, CI, lakeFS) |
| [4](#phase-4) | Streaming & event-driven integration | 22–27 | 119 | Real-time price/flow CDC streaming (Kafka + Debezium + Flink) |
| [5](#phase-5) | Cloud platform architecture & operations (Azure) | 28–33 | 108 | IaC-provisioned platform on Kubernetes + Azure Well-Architected review |
| [6](#phase-6) | Governance, security & compliance | 34–39 | 120 | Governed platform: catalog + lineage + DQ + policy + DCAM self-assessment |
| [7](#phase-7) | AI/ML & LLM platforms for fund data | 40–43 | 74 | LLM extraction of fund documents (RAG + evaluation harness) |
| [8](#phase-8) | Data products, semantic layer & the architect's practice | 44–48 | 103 | Productized fund data product: contracts, SLAs, semantic layer, regulatory report |
| [A](#appendix-a) | Gap additions (scheduled within phases 0, 1, 5, 6, 7, 8 above) | — | 173 | of which 90 h are the Phase-0 foundations A.27–A.31 |
| | **Total** | **48** | **1,100** | **vs 1,152 h budget → 4.5% slack (964 h / 16% with Phase 0 skipped)** |

<a id="skip-list"></a>
## Skip List

Nothing is skipped by assumption. Each [Phase 0](#phase-0) module has a **skip test** below — take it honestly; pass = skip the module and bank the hours, any doubt = do the module. (No other phase is skippable.)

| Module | Covers | Hours banked | Skip if you can do this cold, today |
|---|---|---|---|
| 0.1 Linux & shell | A.27 | 12 | In a terminal: find all `.csv` under a directory, count lines matching a pattern with a pipe, fix a permission error, ssh into a machine, and explain what `$PATH` does. |
| 0.2 Python | A.28 | 36 | Write (without a template) a CLI script that reads a CSV, filters rows via a function you define, writes JSON, handles a malformed line gracefully — and run it with `uv run`. |
| 0.3 SQL | A.29 | 26 | Against two joined tables: explain why a LEFT JOIN changed the row count, write a GROUP BY with HAVING, and return the latest row per group with a window function. |
| 0.4 Git & GitHub | 9.2.1 | 8 | Branch, commit, push, open a PR, resolve a merge conflict, and name when `revert` is safer than `reset`. |
| 0.5 Docker | A.30 | 8 | Write a Dockerfile from scratch and a two-service `docker-compose.yml` with a volume and a healthcheck; debug a failing container from its logs. |
| 0.6 Networking & web | A.31 | 8 | Narrate everything between typing a URL and the page rendering (DNS, TCP, TLS, HTTP), and read `curl -v` output line by line. |
| 0.7 Data basics | 1.1.1–1.1.3 | 6 | Explain UTF-8 mojibake, name three ways CSV files break, and classify five datasets as structured/semi-structured/unstructured. |
| 0.8 Workloads & batch | 1.2.1, 1.3.1, 1.3.2 | 4 | Sort ten workloads into OLTP/OLAP/batch and say why a row store loses to a column store on scans. |
| 0.9 pandas & notebooks | 5.4.2, 14.5.2 | 10 | Load a messy CSV in JupyterLab, clean it, groupby-aggregate, chart it, write Parquet — and explain the hidden-state danger of notebooks. |
| 0.10 Editor & IDE | 9.1.1, 9.1.2 | 2 | Debug with a breakpoint (no prints), and your editor runs lint + terminal + notebooks in one window. |
| 0.11 Unit testing | 9.4.1 | 4 | Write pytest cases incl. a parametrized edge case, and structure code so it's testable (pure functions). |
| 0.12 Code review | 9.5.1 | 2 | Self-review a PR with a checklist and write line comments that critique code, not people. |
| Capstone 0 | — | 10 | Skip only if every test above passed — the capstone exists to prove they compose. |


<a id="phase-0"></a>
## Phase 0: Computing & Data Foundations — from zero (months 1–6, 46 h + 90 h Appendix A)

**Goal:** everything later phases silently stand on, taught from nothing: a Linux working environment, Python, SQL, Git, Docker, how networks and the web work, what data physically is, and the daily toolkit (pandas, notebooks, tests, code review). **Nothing in this plan assumes prior knowledge** — instead, every module below has a **skip test** (collected in the [Skip List](#skip-list)). Pass the test honestly → skip the module and bank its hours as slack. Fail any part → do the module.
**Entry prerequisites:** none. A computer with admin rights is enough.
**Exit criteria:** you can (1) live in a terminal (navigate, pipe, grep, ssh, write a small script); (2) write a Python program that reads files, calls functions you wrote, and runs under `uv`; (3) answer questions from a multi-table database with joins, aggregation, and a window function; (4) commit, branch, and open a pull request; (5) run a two-service Docker Compose stack; (6) explain what happens between typing a URL and seeing a page.

> Module numbers (0.1–0.12) are referenced from the coverage matrix. Do 0.10 (editor setup) alongside 0.1–0.2, not after 0.9 — it's numbered late only to keep taxonomy grouping tidy.

### Modules

#### 0.1 — A.27 Linux, the command line & shell
- **Why:** the terminal is the substrate of everything later — Docker, Kubernetes, CI, cloud shells, log forensics; data work without shell fluency is permanent friction.
- **Learn:** install WSL2 + Ubuntu (your lab for four years); filesystem & permissions; navigation, files, pipes & redirection; grep/sed/awk at reading level; environment variables & PATH; ssh; a first bash script; package managers (apt).
- **Resource:** MIT, *The Missing Semester of Your CS Education* (free) — https://missing.csail.mit.edu/ — lectures 1–5 + exercises.
- **Tools:** FOSS: WSL2 + Ubuntu, Windows Terminal (↔ macOS/cloud shells — same skills).
- **Do:** write a shell script that downloads a CSV, counts rows matching a pattern, and appends a timestamped log line; schedule it with cron.
- **Done when:** you stop reaching for the file explorer; the skip test in the Skip List passes cold.
- Est. hours: counted as A.27 (12 h, Appendix A)

#### 0.2 — A.28 Programming from zero: Python
- **Why:** Python is the lingua franca of data engineering and the language of every exercise in this plan.
- **Learn:** values/types, control flow, functions, modules; lists/dicts/sets; files & exceptions; virtual environments — `uv` from day one (`uv init`, `uv add`, `uv run`); reading tracebacks and debugging; calling an HTTP API; writing a small CLI script; code style (ruff) early.
- **Resource:** *Python for Everybody* (py4e, Charles Severance — free full course). *Alternate:* *Automate the Boring Stuff with Python* (free online).
- **Tools:** FOSS: Python via uv, ruff, VS Code.
- **Do:** build `fundcli`: a CLI that reads a CSV of funds, filters by currency/domicile flags, and writes a summary JSON — typed args, functions, tests come in 0.11.
- **Done when:** you write a 100-line script without copying structure from examples, and `uv run fundcli.py --help` behaves like a real tool.
- Est. hours: counted as A.28 (36 h, Appendix A)

#### 0.3 — A.29 SQL from zero
- **Why:** SQL is the single most-used skill of the entire four years; everything from Phase 1 modeling to Phase 8 semantic layers speaks it.
- **Learn:** SELECT/WHERE/ORDER; joins (inner/left, and *why* rows multiply); GROUP BY/HAVING; subqueries & CTEs; NULL semantics (the classic traps); window functions (ROW_NUMBER, LAG, running sums); INSERT/UPDATE/DELETE; what an index does (user view); information schema.
- **Resource:** SQLBolt (free, interactive) for the core, then PgExercises (free) to fluency. *Alternate:* postgresqltutorial.com.
- **Tools:** FOSS: PostgreSQL in Docker (from 0.5), DBeaver or psql (↔ Azure SQL — same language).
- **Do:** against a two-table funds/nav schema (provided by your own 0.2 loader), answer 15 questions of rising difficulty, ending with "latest NAV per fund via window function".
- **Done when:** joins and GROUP BY are reflexes and you can explain a LEFT JOIN row-count surprise to someone else.
- Est. hours: counted as A.29 (26 h, Appendix A)

#### 0.4 — 9.2.1 Git & GitHub (version control from zero) — T2
- **Why:** every artifact of the next four years lives in Git; branching and PRs are also how teams (and the capstones) work.
- **Learn:** init/add/commit and the three states; log/diff; branching & merging, resolving a conflict; remotes, push/pull; .gitignore; GitHub: repos, README, pull requests; undo recipes (restore, revert, reset — when each is safe).
- **Resource:** *Pro Git* (free book) ch. 1–3 + GitHub "Hello World" quickstart.
- **Tools:** FOSS: Git (↔ GitHub primary; GitLab/Azure Repos same model).
- **Do:** put `fundcli` (0.2) on GitHub; develop a feature on a branch; open a PR to yourself; force a merge conflict and resolve it.
- **Done when:** a deliberately broken rebase/merge doesn't scare you — you know which undo applies.
- Est. hours: 8

#### 0.5 — A.30 Docker & containers from zero
- **Why:** the entire lab (Phases 1–8) is Docker-Compose-shaped; containers are also the unit of deployment everywhere you'll architect.
- **Learn:** images vs containers; pulling & running (ports, env vars, volumes); writing a Dockerfile for `fundcli`; Compose: two services (app + Postgres), healthchecks, named volumes; logs & exec for debugging; cleanup hygiene.
- **Resource:** Docker official "Get Started" guide (free).
- **Tools:** FOSS: Docker Desktop or Docker Engine in WSL2.
- **Do:** `docker compose up` starts Postgres + a one-shot loader container that ingests your funds CSV; data survives a restart via a volume.
- **Done when:** you can explain image vs container vs volume to a colleague and debug a failing container from its logs.
- Est. hours: counted as A.30 (8 h, Appendix A)

#### 0.6 — A.31 Networking & how the web works
- **Why:** every integration in this plan (APIs, Kafka, cloud, Private Link in Phase 5) sits on this layer; architects who can't follow a DNS lookup debug by superstition.
- **Learn:** IP/ports, TCP vs UDP (intuition level); DNS resolution end to end; HTTP: methods, status codes, headers, what a REST call actually is; TLS/certificates (what they guarantee, not the math); localhost vs LAN vs internet; what a firewall and a proxy do; reading `curl -v` output.
- **Resource:** MDN "How the web works" series + Cloudflare Learning Center (DNS and TLS articles) — both free.
- **Tools:** FOSS: curl, dig/nslookup, your browser's dev tools.
- **Do:** trace one request by hand: `dig` the name, `curl -v` the URL, annotate every line of the output (resolution, handshake, request, response headers).
- **Done when:** "it's slow / it's blocked / cert error" each map to a layer you'd check first.
- Est. hours: counted as A.31 (8 h, Appendix A)

#### 0.7 — 1.1.1 + 1.1.2 + 1.1.3 What data physically is — T3
- **Why:** structured/semi-structured/unstructured and their file shapes are the vocabulary of every later storage decision.
- **Learn:** bytes, text and UTF-8 (why encodings corrupt); CSV and its dialect traps; JSON & nesting; XML at reading level (Phase 2's ISO 20022 is XML); what "schema" means; structured vs semi-structured vs unstructured with concrete fund examples (NAV table / EMT file / prospectus PDF); spreadsheets vs databases.
- **Resource:** *Fundamentals of Data Engineering* (Reis & Housley) ch. 1 + hands-on conversions below.
- **Tools:** FOSS: Python (csv/json modules), pandas.
- **Do:** take one fund-holdings dataset and produce it as CSV, JSON (nested by fund), and pretty-printed XML; break the CSV with a stray separator and an encoding mangle, then detect and fix both programmatically.
- **Done when:** you can name the failure modes of CSV from your own scars, not a list.
- Est. hours: 6

#### 0.8 — 1.2.1 + 1.3.1 + 1.3.2 Batch processing & OLTP vs OLAP — T2/T3
- **Why:** the transactional-vs-analytical split drives storage choice everywhere; batch is the default processing rhythm of the fund industry (daily NAV).
- **Learn:** what a transaction-processing workload looks like (many small reads/writes) vs analytical (few huge scans); why one system rarely serves both well; batch jobs: schedule → process bounded data → publish; idempotent reruns at intuition level (deepened in Phase 1).
- **Resource:** *Fundamentals of Data Engineering* ch. 2–3 (workload & storage sections).
- **Tools:** FOSS: PostgreSQL (row store) + DuckDB (column store) — first contact.
- **Do:** run the same "average NAV per fund per month" query on Postgres and on DuckDB-over-Parquet at 1M rows; record timings; write five sentences on why they differ.
- **Done when:** you can sort ten example workloads into OLTP/OLAP/batch without hesitation.
- Est. hours: 4

#### 0.9 — 5.4.2 + 14.5.2 pandas & JupyterLab — T2
- **Why:** notebook-driven wrangling is the data professional's daily bread and your exploration tool for every later phase.
- **Learn:** JupyterLab basics (and its dangers: hidden state, out-of-order cells); pandas: read_csv/parquet, select/filter, groupby-agg, joins/merge, datetime handling, missing data; a first chart; getting data out (to Parquet, to Postgres).
- **Resource:** Wes McKinney, *Python for Data Analysis* 3rd ed. (free online at the author's site), ch. 1–10 selectively.
- **Tools:** FOSS: JupyterLab, pandas, matplotlib (↔ Hex/Databricks notebooks later).
- **Do:** clean a deliberately messy NAV file (mixed encodings, duplicate rows, missing dates), produce a monthly per-fund summary and a chart, and write the result to both Parquet and Postgres.
- **Done when:** the skip test passes and you also know *why* notebook state burned you at least once.
- Est. hours: 10

#### 0.10 — 9.1.1 + 9.1.2 Editor & IDE setup — T3
- **Why:** tooling friction taxes every hour of the next four years; set it up once, properly.
- **Learn:** VS Code: workspace, integrated terminal (WSL), extensions (Python, ruff, Jupyter, Docker); debugging with breakpoints (stop print-debugging early); keyboard-first habits; JupyterLab vs VS Code notebooks.
- **Resource:** VS Code official docs (Python tutorial section).
- **Tools:** FOSS: VS Code (↔ JetBrains; choice is taste, fluency is mandatory).
- **Do:** debug your 0.2 CLI with a breakpoint inside a function: inspect variables, step, fix a planted bug without a single print.
- **Done when:** edit-run-debug loop feels frictionless and lives entirely inside the editor + terminal.
- Est. hours: 2

#### 0.11 — 9.4.1 Unit testing from zero (pytest) — T2
- **Why:** tests are how the capstones (and grown-up data platforms) stay trustworthy; the habit must form before the stakes rise.
- **Learn:** pytest: test files/functions, assertions, parametrize; arranging code to be testable (pure functions); fixtures at basic level; running in CI comes in Phase 3 — here it's the local habit.
- **Resource:** pytest official "Get started" + how-to guides (free).
- **Tools:** FOSS: pytest via uv.
- **Do:** add tests to `fundcli`: happy path, empty file, malformed row, wrong currency — watch one fail, fix the code, not the test.
- **Done when:** writing the test first feels natural for any new function.
- Est. hours: 4

#### 0.12 — 9.5.1 Code review basics — T3
- **Why:** review is how engineering teams transfer judgment; doing it well (both directions) is a career-long multiplier.
- **Learn:** what reviewers look for (correctness, clarity, scope); writing reviewable PRs (small, described, self-reviewed first); giving feedback on the code, not the person; responding to review without ego.
- **Resource:** Google Engineering Practices code-review guide (free, google.github.io/eng-practices).
- **Do:** self-review your capstone PR with the guide's checklist; leave five genuine line comments and fix them.
- **Done when:** your PRs come pre-reviewed by you, and the checklist runs in your head.
- Est. hours: 2

### Capstone 0 — Personal data toolbox

- **Goal:** prove the foundations compose: one small, real, reproducible data project touching every module.
- **Stack (100% free):** WSL2 + Ubuntu, uv-managed Python, PostgreSQL + loader in Docker Compose, JupyterLab + pandas, pytest, Git + GitHub.
- **Build:** (1) pick a public fund/ETF dataset (e.g., an ECB or data.europa.eu CSV); (2) `docker compose up` brings Postgres + a Python loader that ingests it idempotently-naively (rerun-safe by truncate-reload — the grown-up version comes in Phase 1); (3) answer 10 SQL questions of rising difficulty in a committed `.sql` file; (4) a notebook produces one cleaned monthly summary and one chart; (5) pytest covers the loader's parsing; (6) README explains setup in ≤10 commands; (7) developed on branches with self-reviewed PRs.
- **Architecture deliverables:** none yet — your first C4 diagram and ADR arrive in Phase 1; here the README *is* the architecture document.
- **Acceptance criteria:** a stranger with Docker and uv reproduces everything from the README on a fresh machine; `uv run pytest` green; the chart answers a stated question; the Git history shows ≥3 PRs with self-review comments.
- Est. hours: 10

*Phase 0 total: 46 h in-phase (taxonomy entries 36 h + capstone 10 h) + 90 h via A.27–A.31 = 136 h — every hour of it skippable via the [Skip List](#skip-list) tests.*


<a id="phase-1"></a>
## Phase 1: Distributed Data Systems & Modeling Core (months 7–11, 118 h)

**Goal:** rebuild the theoretical foundation an architect reasons from — transaction guarantees, consistency, distribution tradeoffs, database internals — and turn existing modeling intuition into formal, teachable practice (conceptual→logical→physical, dimensional), documented with C4 and ADRs from day one.
**Entry prerequisites:** Phase 0 — or its skip tests passed (Linux/shell, Python, SQL, Git, Docker, networking).
**Exit criteria:** you can (1) explain isolation anomalies and pick an isolation level for a fund-order workload; (2) argue a replication/partitioning choice with PACELC, not folklore; (3) read a Postgres `EXPLAIN ANALYZE` and fix the plan; (4) produce a 3-level model + star schema for a fund domain and defend every key and SCD choice; (5) ship C4 diagrams + ADRs as a matter of habit.

### T1/T2 topics

#### 1.6.1 ACID & isolation levels — T1
- **Why:** transaction guarantees underpin every regulated-data design review; "is this exactly-once and serializable?" is a question you must answer, not delegate.
- **Learn:** atomicity vs durability mechanics (WAL); isolation anomalies (dirty/non-repeatable/phantom reads, write skew); ANSI levels vs snapshot isolation; serializability vs SSI; how Postgres, SQL Server, and Oracle differ in defaults; idempotent retry vs transactional retry.
- **Resource:** DDIA ch. 7 "Transactions" (latest ed.). *Alternate:* CMU 15-445 concurrency-control lectures.
- **Tools:** FOSS: PostgreSQL (in Docker) · Corp: Azure SQL / Oracle DB (defaults + TDE-era differences at evaluation level).
- **Do:** reproduce write skew and a phantom in Postgres with two psql sessions at `READ COMMITTED`, then fix both with `REPEATABLE READ`/`SERIALIZABLE`; note retry behavior.
- **Done when:** you can explain to a reviewer why snapshot isolation permits write skew and name a fund-accounting scenario where that corrupts data.
- Est. hours: 8

#### 1.6.3 + 1.6.4 + 1.6.5 The consistency spectrum — T2
- **Why:** replicated platforms (read replicas, geo-DR, caches) silently downgrade consistency; the architect must name the guarantee actually delivered.
- **Learn:** eventual vs strong; read-your-writes, monotonic reads, causal consistency; linearizability vs serializability (they answer different questions); where lag bites: replica reads after writes, cross-region failover.
- **Resource:** DDIA ch. 5 "Replication" + ch. 9 "Consistency and Consensus" (linearizability sections).
- **Do:** write a 1-page memo: which consistency level a fund-order status API needs vs a NAV-history dashboard, and what each costs.
- **Done when:** you can give a concrete user-visible bug for each violated guarantee.
- Est. hours: 5

#### 1.7.1 + 1.7.2 CAP & PACELC — T1
- **Why:** every design review invokes CAP, usually wrongly; the architect corrects the record and uses PACELC's latency half, which is what actually drives cloud database selection.
- **Learn:** what CAP actually states (and what it doesn't — A and C definitions are narrow); partition behavior of common systems; PACELC: latency–consistency tradeoff under normal operation; classify Postgres, Cassandra, Cosmos DB, Spanner-style systems.
- **Resource:** DDIA ch. 9 (incl. "The Unhelpfulness of CAP") + Abadi's PACELC paper (IEEE Computer 2012).
- **Do:** build a one-table PACELC classification of 8 stores you'll meet in this plan (Postgres, Cassandra, Kafka, Cosmos DB, DynamoDB, Spanner, Redis, MongoDB) with one-line justifications.
- **Done when:** you can explain why "CP vs AP" is the wrong frame for a single-region Azure SQL deployment.
- Est. hours: 3

#### 1.8.1 Idempotency — T1
- **Why:** retry-safety is the single biggest reliability lever in pipelines; non-idempotent loads are how funds double-book trades.
- **Learn:** idempotency keys; natural vs synthetic dedup; idempotent writes (MERGE/upsert, INSERT … ON CONFLICT); idempotent pipeline runs (overwrite-partition pattern); at-least-once delivery + idempotent consumer = effective exactly-once.
- **Resource:** DDIA ch. 11 (fault-tolerance/exactly-once sections); taxonomy concept entry as checklist.
- **Tools:** FOSS: PostgreSQL upserts · Corp: ADF rerun semantics (evaluation level).
- **Do:** write a Python loader (via `uv run`) that ingests a trades CSV into Postgres and is provably safe to run twice — demonstrate with row counts and checksums.
- **Done when:** you can list the three places idempotency must hold in a pipeline (source read, transform, sink write) and how to get each.
- Est. hours: 4

#### 1.8.9 Distributed transactions & 2PC — T2
- **Why:** you must recognize when someone proposes a distributed transaction and steer to outbox/saga instead — with reasons, not taste.
- **Learn:** 2PC protocol and its blocking failure mode; coordinator failure; XA in practice; why consensus (Raft) ≠ 2PC; modern alternatives preview (outbox, saga — implemented in Phase 4).
- **Resource:** DDIA ch. 9 ("Distributed Transactions and Consensus").
- **Do:** write a half-page ADR rejecting 2PC for a hypothetical order-service + position-service consistency requirement, naming the alternative.
- **Done when:** you can explain what happens to locks when a 2PC coordinator dies mid-commit.
- Est. hours: 5

#### 1.5.1–1.5.4 Storage paradigms — T2
- **Why:** row vs columnar, shared-nothing vs shared-disk, and storage/compute separation are the axes along which every warehouse/lakehouse vendor differentiates — this is the vocabulary of vendor selection.
- **Learn:** row vs columnar layouts and why scans love columns; compression + late materialization; MPP partitioning and data skew; shared-nothing vs shared-disk; separation of storage and compute (Snowflake/BigQuery model) and its cost/elasticity consequences.
- **Resource:** DDIA ch. 3 "Storage and Retrieval" (column-store sections) + CMU 15-445 storage lectures 3–5.
- **Do:** in DuckDB, run the same aggregate over a 10M-row table stored as CSV vs Parquet; explain the timing difference in terms of layout and I/O.
- **Done when:** you can sketch the Snowflake-style architecture and say which failure/cost behaviors follow from each separation decision.
- Est. hours: 4

#### 3.2.1 Relational internals (the database under everything) — T1
- **Why:** indexing, query planning, MVCC, and recovery ground every storage decision an architect makes; this is the deepest single investment in the plan.
- **Learn:** pages/heap files and buffer pool; B+trees vs hash vs GIN/BRIN; query planner: cardinality estimation, join algorithms (nested-loop/hash/merge); MVCC and vacuum; WAL, checkpoints, crash recovery; connection pooling; partitioning and when it helps.
- **Resource:** CMU 15-445 (latest year) — lectures + notes for: storage, buffer pool, indexes, sorting/joins, query optimization, MVCC, logging/recovery (~14 of 26 lectures). *Alternate:* *Database Internals* (Petrov) Part I.
- **Tools:** FOSS: PostgreSQL 16 + `EXPLAIN (ANALYZE, BUFFERS)`, pgbench · Corp: Azure SQL / Oracle (planner-hint culture, licensing economics — evaluation level).
- **Do:** take a deliberately slow 5-table fund-holdings query; capture the plan, fix it with indexes/statistics/rewrites to a 10× improvement; write up before/after plans.
- **Done when:** you can read an unfamiliar `EXPLAIN ANALYZE` and narrate where time goes and why the planner chose the join order it did.
- Est. hours: 30

#### 8.2.1 + 8.2.2 + 8.2.3 Conceptual → logical → physical modeling — T1
- **Why:** the three-level discipline is the architect's signature artifact chain — business entities to keys/normal forms to engine-specific DDL — and the basis for every review you'll run.
- **Learn:** conceptual entity modeling (and when to stop); logical: candidate/natural/surrogate keys, 1NF–BCNF and deliberate denormalization; physical: data types, partitioning, indexes per target engine; forward/reverse engineering; notation fluency (Crow's Foot; read IDEF1X).
- **Resource:** DAMA-DMBOK ch. 5 "Data Modeling and Design". *Alternate:* Hoberman, *Data Modeling Made Simple*.
- **Tools:** FOSS: draw.io / DBeaver ERD · Corp: erwin / ER/Studio / SqlDBM (what EU banks actually license — evaluation level).
- **Do:** model the fund domain three ways: conceptual (fund, share class, investor, order, NAV), logical (keys + normal forms justified), physical (Postgres DDL with partitioning for NAV history).
- **Done when:** a colleague can implement your logical model without asking you questions; every surrogate-key choice has a stated reason.
- Est. hours: 12

#### 8.2.4 Dimensional modeling — T1
- **Why:** Kimball stars remain the dominant analytical model in regulated reporting marts; fund NAV/holdings/fees reporting is textbook dimensional territory.
- **Learn:** fact table grain (declare it first, always); fact types (transaction, periodic snapshot, accumulating snapshot — NAV is a periodic snapshot); conformed dimensions and the bus matrix; SCD types 1/2/3/6 (security/fund reference data is SCD2 country); junk/degenerate dimensions; star vs snowflake.
- **Resource:** Kimball & Ross, *The Data Warehouse Toolkit* 3rd ed., ch. 1–4 + ch. 19 (financial services). *Alternate:* Corr & Stagnitto, *Agile Data Warehouse Design* (BEAM workshops).
- **Tools:** FOSS: dbt + DuckDB for implementation · Corp: same patterns in Synapse/Snowflake marts.
- **Do:** design the bus matrix for a fund administrator (processes: orders, NAV calculation, fee accrual, transfer agency); implement the NAV periodic-snapshot star with an SCD2 fund dimension in SQL.
- **Done when:** you can state the grain of each fact table in one sentence and show an SCD2 query returning point-in-time-correct fund attributes for any historical date.
- Est. hours: 16

#### 8.5.1 Architecture notations & decision records (C4, ADR) — T1
- **Why:** C4 diagrams and ADRs are the artifacts that define the architect role in practice — they make your reasoning reviewable and your decisions auditable.
- **Learn:** C4 levels (context, container, component, code — and when to stop at container); diagrams-as-code; ADR anatomy (context, decision, consequences) and lifecycle (proposed/accepted/superseded); lightweight RFC processes; what reviewers actually look for.
- **Resource:** c4model.com (full read) + adr.github.io (MADR template). *Alternate:* Richards & Ford, *Fundamentals of Software Architecture* ch. on diagramming & decisions.
- **Tools:** FOSS: Structurizr Lite (Docker) or Mermaid C4 · Corp: Sparx Enterprise Architect / Visual Paradigm (the EA suites EU institutions license).
- **Do:** document an existing system you know from work as C4 context + container diagrams, plus 2 retroactive ADRs for its key decisions.
- **Done when:** every capstone from here on ships C4 + ADRs without you thinking about it (the capstones enforce this).
- Est. hours: 8

#### 1.10.1 Modeling notations overview — T2
- **Why:** you need reading fluency across UML/BPMN/DMN/ArchiMate before Phase 4 (BPM) and Phase 8 (ArchiMate practice) go deep.
- **Learn:** which notation answers which question — UML class/sequence (system structure/behavior), BPMN (executable process), DMN (decision logic), ArchiMate (enterprise layers), ERD/IDEF1X (data), C4 (software) — and reading-level literacy in each.
- **Resource:** taxonomy's standards reference list entries + one example diagram of each from the linked OMG/Open Group spec intros.
- **Do:** make a one-page "notation chooser" cheat sheet: question → notation → tool.
- **Done when:** shown a diagram cold, you can name the notation and read it correctly.
- Est. hours: 2

#### 9.1.3 Local data sandboxes — T2
- **Why:** the entire 4-year lab runs on reproducible local stacks; compose fluency is the substrate for every capstone.
- **Learn:** Docker Compose service graphs, healthchecks, volumes/networks; Testcontainers idea (programmatic throwaway infra); DuckDB as a zero-infra warehouse; pinning images for reproducibility.
- **Resource:** Docker Compose official docs (top-level concepts + healthchecks) — builds directly on Phase 0's module 0.5.
- **Tools:** FOSS: Docker Compose, DuckDB, Testcontainers · Corp: dev-container/codespace equivalents (awareness).
- **Do:** write the `docker-compose.yml` you'll grow all four years: Postgres + MinIO + a placeholder service, with healthchecks and named volumes.
- **Done when:** `docker compose up` gives a clean, healthy stack on a fresh clone in under 2 minutes.
- Est. hours: 4

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.3.3 | HTAP (workload) | One system serving OLTP + OLAP; niche but recurring vendor pitch | DDIA ch. 3 (closing section) | 30 |
| 1.6.2 | BASE | Marketing-era label for eventual-consistency systems; know it to translate it | DDIA ch. 5 intro | 15 |
| 3.2.2 | NoSQL document stores | JSON-document storage (MongoDB); flexible schema, app-owned integrity | DDIA ch. 2 (document model) | 45 |
| 3.2.3 | NoSQL key-value | High-throughput KV (Redis/Valkey, DynamoDB); caching + session state | DDIA ch. 3 (hash indexes) | 30 |
| 3.2.4 | NoSQL wide-column | Sparse-column distributed stores (Cassandra); write-heavy, query-first design | DDIA ch. 2 + Cassandra docs "data modeling" intro | 45 |
| 3.2.10 | HTAP stores | TiDB/SingleStore implementations of 1.3.3 | vendor architecture pages | 15 |

*T3 subtotal: 3 h*

### Capstone 1 — Fund reference OLTP + reporting mart

- **Goal:** a correct, documented foundation: operational fund reference database + dimensional reporting mart, the seed every later phase builds on.
- **Stack (100% free):** PostgreSQL 16 (↔ Azure SQL / Oracle), DuckDB (↔ Synapse/Snowflake mart), dbt Core seed/models for the mart (↔ dbt Cloud), Structurizr Lite (↔ Sparx EA), Docker Compose, Python via uv, Faker for sample data (↔ Tonic.ai/Delphix).
- **Build:** (1) implement the Phase-1 physical model in Postgres: funds, share classes, ISIN-keyed securities, investors, orders, NAV history (partitioned); (2) load Faker-generated but referentially consistent data with the idempotent loader from 1.8.1; (3) build the NAV periodic-snapshot star + SCD2 fund dimension in DuckDB; (4) one deliberately slow query, tuned, with before/after plans.
- **Architecture deliverables:** C4 context + container diagrams; ADR-001 (surrogate vs natural keys — why ISIN is not your PK), ADR-002 (SCD2 for fund attributes), ADR-003 (partitioning scheme for NAV history).
- **Acceptance criteria:** loader runs twice with identical end state; point-in-time query returns correct fund attributes for any historical date; tuned query ≥10× faster with written plan analysis; a stranger can run `docker compose up && uv run load.py` from the README and get the same numbers.
- Est. hours: 14

*Phase 1 total: 118 h (T1/T2 entries 101 h + T3 3 h + capstone 14 h)*


<a id="phase-2"></a>
## Phase 2: Lakehouse & Analytics Engineering (months 12–16, 123 h)

**Goal:** master the open lakehouse stack — object storage, columnar formats, ACID table formats, federated SQL, dbt — and ground the whole plan in the fund-data domain by learning the financial standards the platform will carry (ISO 20022, EMT/EPT, instrument identifiers).
**Entry prerequisites:** Phase 1 (modeling discipline, Postgres internals vocabulary, Docker Compose stack).
**Exit criteria:** you can (1) explain a Parquet footer and an Iceberg snapshot to a skeptic; (2) defend Iceberg vs Delta for a given estate; (3) run a tested, documented dbt project with layered models; (4) design a raw vault for an audit-driven warehouse; (5) read an ISO 20022 message and an EMT file and say where each field lands in your model.

### T1/T2 topics

#### 1.4.3 Medallion architecture — T1
- **Why:** bronze/silver/gold is the default layering of every lakehouse you'll design; the architect's job is making the layer contracts explicit instead of folklore.
- **Learn:** what each layer guarantees (immutability/replayability in bronze; conformance, dedup, DQ-checked in silver; consumption-modeled gold); schema-on-read→write transition point; when medallion is cargo cult (3 layers is a default, not a law); reprocessing strategy per layer.
- **Resource:** Databricks medallion architecture docs + *Fundamentals of Data Engineering* ch. 8 (transformation patterns).
- **Do:** write the layer contract sheet for a fund-data lakehouse: per layer — owner, schema policy, DQ gate, retention, consumer promise.
- **Done when:** you can answer "why not query bronze directly?" with consequences, not dogma.
- Est. hours: 4

#### 3.1.4 Data lakehouse — T1
- **Why:** the lake-with-ACID-tables-plus-warehouse-SQL pattern is the target architecture for fund platforms; you must design one and defend it against both "just use Snowflake" and "just use files."
- **Learn:** lakehouse = object store + open table format + catalog + query engines; what the warehouse still does better (concurrency, fine-grained security, ergonomics); decoupling storage/format/catalog/engine and why open formats de-risk vendor lock-in; Databricks vs Snowflake-with-Iceberg vs Fabric positioning.
- **Resource:** Inmon et al., *Building the Data Lakehouse* (skim for the warehouse-veteran perspective) + the CIDR 2021 "Lakehouse" paper (Armbrust et al.) as the technical core.
- **Tools:** FOSS: MinIO + Iceberg + Trino + DuckDB · Corp: Databricks, Microsoft Fabric/OneLake, Snowflake (evaluation level).
- **Do:** write a 2-page build-vs-buy memo: open lakehouse vs Databricks vs Fabric for a 50-person Luxembourg fund administrator — cost, skills, lock-in, compliance.
- **Done when:** you can name, for each lakehouse component, what breaks if you swap vendors.
- Est. hours: 10

#### 3.1.3 + 3.3.1 Data lake on object storage — T2
- **Why:** object stores are the physical substrate of everything analytical; their semantics (no rename, eventual listing, request pricing) leak into every design above.
- **Learn:** S3 API semantics; durability vs availability tiers; prefixes/partitioning and request costs; multipart upload; lifecycle policies; ADLS Gen2's hierarchical namespace and why it exists.
- **Resource:** MinIO docs (core concepts) + ADLS Gen2 introduction (Microsoft Learn).
- **Tools:** FOSS: MinIO (↔ ADLS Gen2 / S3) · Corp: ADLS Gen2 (primary), S3 (awareness).
- **Do:** run MinIO in compose; write NAV Parquet files into a date-partitioned layout via `uv run` + pyarrow; set a lifecycle rule to expire bronze after 30 days.
- **Done when:** you can explain why "rename a folder" is a problem on S3 but not ADLS Gen2.
- Est. hours: 4

#### 3.1.1 Cloud data warehouse — T2
- **Why:** even lakehouse-first shops keep a warehouse; you'll be asked to compare Snowflake/BigQuery/Synapse credibly in vendor selection.
- **Learn:** Snowflake's three-layer architecture (services/compute/storage), credits and warehouses; BigQuery's serverless slots model; Synapse dedicated vs serverless; micro-partitions and clustering vs partitioning; what each prices and how runaway cost happens.
- **Resource:** Snowflake "Key Concepts & Architecture" docs + BigQuery "Under the hood" architecture docs.
- **Tools:** FOSS: DuckDB as a stand-in for exercises · Corp: Snowflake, BigQuery, Synapse/Fabric Warehouse (evaluation level).
- **Do:** one-page comparison table (architecture, pricing unit, workload isolation, Iceberg story, EU-region/compliance posture) for the three.
- **Done when:** you can explain to a CFO why Snowflake costs are workload-shaped, not data-shaped.
- Est. hours: 4

#### 3.4.1 File formats — T1
- **Why:** Parquet internals (row groups, encodings, statistics, pushdown) are where storage cost and query latency are actually decided; architects who can't read a footer argue from vibes.
- **Learn:** Parquet structure: row groups, column chunks, pages, dictionary/RLE encodings, min/max stats, predicate & projection pushdown; compression tradeoffs (snappy/zstd); Avro as row-oriented schema-evolution format and where it fits (Kafka, landing); Arrow as the in-memory interchange standard; ORC awareness.
- **Resource:** Parquet official format docs + DuckDB blog posts on Parquet internals. *Alternate:* *Fundamentals of Data Engineering* ch. 6.
- **Tools:** FOSS: pyarrow, DuckDB, `parquet-tools` · Corp: same formats everywhere (this knowledge is vendor-neutral by design).
- **Do:** with pyarrow via `uv run`, write the same 10M-row holdings table at three row-group sizes and two compressions; measure file size and a filtered-scan time in DuckDB; inspect footers and explain results.
- **Done when:** given a slow lake query, you check row-group pruning before blaming the engine.
- Est. hours: 8

#### 3.4.2 Table formats (Iceberg, Delta) — T1
- **Why:** the ACID metadata layer is the heart of the lakehouse — snapshots, schema evolution, time travel, and compaction are what you'll design, operate, and debug.
- **Learn:** Iceberg metadata tree (metadata file → manifest list → manifests → data files); snapshots & time travel; hidden partitioning and partition evolution; copy-on-write vs merge-on-read; compaction/maintenance; schema evolution rules; Delta log model and UniForm; Hudi at awareness level; format-war state of play.
- **Resource:** Iceberg official docs (spec + "Maintenance") + Tabular/Iceberg blog series. *Alternate:* *Apache Iceberg: The Definitive Guide* (O'Reilly, free via Dremio).
- **Tools:** FOSS: Iceberg on MinIO via Trino; Delta via DuckDB/`delta-rs` · Corp: Databricks Delta, Snowflake managed Iceberg, Fabric OneLake (evaluation level).
- **Do:** create an Iceberg NAV table via Trino; run UPDATE/DELETE/MERGE; time-travel to pre-update; evolve schema (add column, change partition spec); inspect the metadata JSON/manifests on MinIO and narrate the tree.
- **Done when:** you can debug "why is this table slow/huge" from manifests alone, and write the Iceberg-vs-Delta ADR for a given estate.
- Est. hours: 12

#### 3.4.3 Table-format catalogs — T2
- **Why:** the catalog is the new lock-in battleground; whoever owns the catalog owns the lakehouse — a vendor-selection conversation you must lead.
- **Learn:** what a catalog tracks (namespaces, table pointers, snapshots); Iceberg REST catalog spec as the decoupling standard; Polaris, Unity Catalog OSS, Lakekeeper, Nessie positioning; credential vending; why engine-bundled catalogs recreate lock-in.
- **Resource:** Iceberg REST catalog spec + Apache Polaris docs (overview).
- **Tools:** FOSS: Lakekeeper or Polaris in compose · Corp: Unity Catalog (Databricks), AWS Glue, Snowflake Open Catalog (evaluation level).
- **Do:** swap your capstone's catalog (e.g., Trino's Hive-style catalog → Lakekeeper REST) and document what changed and what didn't.
- **Done when:** you can explain credential vending and why the catalog, not the format, decides openness.
- Est. hours: 4

#### 4.3.1 MPP/federated SQL engines (Trino) — T2
- **Why:** Trino is the open federation engine (and the heart of Starburst/Athena); it queries the lakehouse and Postgres in one statement — the practical face of "decoupled compute."
- **Learn:** coordinator/worker architecture; connectors and pushdown; memory model and spill; Iceberg connector specifics; cost-based optimizer basics; when federation is an anti-pattern (chatty joins across stores).
- **Resource:** Trino official docs ("Overview" + "Iceberg connector") . *Alternate:* *Trino: The Definitive Guide* (free via Starburst).
- **Tools:** FOSS: Trino (↔ Starburst Enterprise, AWS Athena) · Corp: Starburst, Athena, Synapse serverless (evaluation level).
- **Do:** add Trino to compose; join Postgres fund reference data to Iceberg NAV history in one query; compare with copying the dimension into Iceberg first.
- **Done when:** you can predict which predicates push down to each source and verify with EXPLAIN.
- Est. hours: 5

#### 4.3.3 Embedded analytical engines (DuckDB) — T2
- **Why:** DuckDB is the architect's pocket warehouse — local development, testing, and a legitimate production pattern for mid-size workloads; knowing its limits sharpens every "do we need a cluster?" conversation.
- **Learn:** in-process model; out-of-core execution; reading Parquet/Iceberg/Delta directly; extension ecosystem; single-writer constraint; MotherDuck awareness; ClickHouse as the server-side single-node speed king (awareness).
- **Resource:** DuckDB official docs ("Why DuckDB" + Parquet/extensions pages).
- **Tools:** FOSS: DuckDB · Corp: MotherDuck, ClickHouse Cloud (awareness).
- **Do:** benchmark the Phase-1 mart queries: DuckDB-over-Parquet vs Postgres; write 5 bullets on when each wins.
- **Done when:** you can articulate the data size/concurrency envelope where "no cluster" is the right architecture.
- Est. hours: 3

#### 5.2.1 + 5.3.1 dbt & the SQL transformation layer — T1
- **Why:** dbt is the modeling-to-production bridge you already started; mastery (not usage) is what lets you set standards for a whole analytics team.
- **Learn:** project structure conventions (staging/intermediate/marts mirroring medallion); ref graph & materializations (view/table/incremental/snapshot — incremental strategies and their failure modes); tests (generic, singular, unit tests); dbt snapshots = SCD2; docs & exposures; packages (dbt-utils, dbt-expectations); semantic conventions; SQLMesh as the challenger (virtual environments, column-level lineage) at evaluation level.
- **Resource:** Cyr & Dorsey, *Analytics Engineering with SQL and dbt* (full) + official dbt best-practice guides.
- **Tools:** FOSS: dbt Core + dbt-duckdb/dbt-trino; SQLMesh (eval) · Corp: dbt Cloud, Coalesce, Dataform (evaluation level).
- **Do:** rebuild the Phase-1 mart as a layered dbt project on DuckDB: sources with freshness checks, staging→marts, snapshot-based SCD2 fund dimension, tests on every model, generated docs.
- **Done when:** `dbt build` is green from scratch, the DAG is readable by a stranger, and you can explain why each model has its materialization.
- Est. hours: 14

#### 5.2.2 Orchestrated ELT (build-vs-buy) — T2
- **Why:** "Fivetran + dbt" is the default managed pattern; you must price it against self-hosted connectors for a regulated EU estate.
- **Learn:** MAR-based pricing mechanics; connector reliability economics; when managed ELT wins (long-tail SaaS sources) vs loses (core banking, mainframe, data sovereignty).
- **Resource:** Fivetran pricing/architecture docs + Airbyte deployment docs (comparison read).
- **Do:** half-page build-vs-buy note for a fund admin with 6 internal systems and 4 SaaS sources.
- **Done when:** you can state the crossover point where Fivetran's cost beats an engineer maintaining Airbyte.
- Est. hours: 2

#### 2.1.1 Batch ELT connectors — T2
- **Why:** connector platforms are the workhorse of non-streaming ingestion; hands-on Airbyte makes the managed-vendor conversation concrete.
- **Learn:** connector model (source/destination/spec/state); incremental sync modes and cursor fields; CDC-flavored connectors vs true CDC; schema-change handling; operating cost of self-hosted connectors.
- **Resource:** Airbyte docs (core concepts + incremental sync).
- **Tools:** FOSS: Airbyte OSS (↔ Fivetran, Stitch, ADF copy activity) · Corp: Fivetran (evaluation level).
- **Do:** stand up Airbyte in compose; sync the Phase-1 Postgres to MinIO Parquet incrementally; break the cursor on purpose and repair it.
- **Done when:** you can explain how state is kept and what happens on a re-sync after schema change.
- Est. hours: 4

#### 8.2.5 Data Vault modeling (+ 1.4.7 pattern) — T1
- **Why:** Data Vault is the financial-services-favored EDW pattern — auditability by construction, multi-source integration without re-modeling — and Luxembourg shops ask for it by name.
- **Learn:** hubs (business keys), links (relationships), satellites (history & context); raw vault vs business vault; hash keys & hashdiffs; loading patterns (parallel, insert-only); PIT and bridge tables for query performance; when Vault is overkill (single-source, small team); Vault-on-lakehouse with dbt (AutomateDV).
- **Resource:** Linstedt & Olschimke, *Building a Scalable Data Warehouse with Data Vault 2.0*, ch. 1–7 (modeling) + ch. 11–12 (loading).
- **Tools:** FOSS: dbt + AutomateDV package · Corp: VaultSpeed, WhereScape, Datavault Builder (evaluation level).
- **Do:** model fund/share-class/administrator from two conflicting source systems as a raw vault (hubs/links/sats) with AutomateDV; build one PIT table; show that a late-arriving correction is fully auditable.
- **Done when:** you can defend hub key choices for messy real-world identifiers (ISIN reuse, internal codes) and explain insert-only loading to an auditor.
- Est. hours: 12

#### 1.12.1 ISO 20022 — T1
- **Why:** the lingua franca of EU payments and securities messaging — fund platforms ingest and emit it; post-MT migration it is *the* message standard your models must align to.
- **Learn:** message taxonomy (pacs/camt/sese/semt/setr business areas — which matter for funds: setr orders, semt statements, sese settlement); XSD structure, business components, external code sets; the e-Repository and Message Definition Reports; mapping messages to canonical models; MX-over-SWIFT context.
- **Resource:** iso20022.org — Message Definition Report for setr (investment funds) + the "ISO 20022 for Dummies" SWIFT booklet (free PDF).
- **Do:** parse a sample `setr.010` (subscription order) with Python/lxml via `uv run`; map every business field onto your Phase-1 model; document gaps your model can't hold.
- **Done when:** you can sketch the message flow (order → status → confirmation → settlement) for a fund subscription and name the message types at each hop.
- Est. hours: 6

#### 1.12.7 EMT / EPT (FinDatEx) — T1
- **Why:** EMT (MiFID target market/costs) and EPT (PRIIPs KID data) are the fund-data dissemination templates of the EU industry — the exact artifacts a Luxembourg fund-data platform produces and consumes daily.
- **Learn:** FinDatEx governance and template lifecycle/versioning; EMT structure (manufacturer target market, costs & charges blocks); EPT structure (KID inputs: SRI, performance scenarios, costs); CEPT/delta templates; how distributors consume them; data-quality pain points (versioning, partial files, code lists).
- **Resource:** findatex.eu — current EMT and EPT template specifications (free downloads).
- **Do:** build a dbt model set that produces a valid EMT V4-shaped output from your fund mart; validate column-by-column against the spec.
- **Done when:** you can explain to a product manager which upstream attributes block EMT completion and what "regulatory data product" means concretely.
- Est. hours: 5

#### 1.12.2 + 1.12.3 LEI & ISIN (entity and instrument identity) — T2
- **Why:** identifier discipline is the difference between a fund platform and a data swamp; LEI and ISIN are the join keys of the industry.
- **Learn:** ISIN structure/allocation (and why ISIN ≠ listing — venue-level FIGI/MIC); LEI structure, GLEIF registry, Level 1/Level 2 (who-owns-whom) data; validation (check digits); identifier lifecycle events (corporate actions renaming ISINs).
- **Resource:** GLEIF site (LEI intro + Level 2 data docs) + ANNA ISIN guidelines.
- **Do:** download the GLEIF golden copy (free), load it to your lakehouse bronze, and link your Faker funds to real LEIs of their (fictive) management companies.
- **Done when:** you can explain why a security master needs both ISIN and an internal surrogate, with a concrete corporate-action scenario.
- Est. hours: 2

#### 1.12.8 SWIFT MT / MX — T2
- **Why:** legacy MT messages still flow through fund operations (TA, custody); architects must read both worlds during the long MX coexistence.
- **Learn:** MT message anatomy (blocks, tags) for the fund-relevant set (MT502/509/515 orders, MT535/536 statements); MX = ISO 20022 over SWIFT; translation/coexistence rules; what SWIFT network membership means operationally.
- **Resource:** SWIFT standards documentation (MT category 5 overview) — free with registration.
- **Do:** hand-translate an MT535 holdings statement into your model's terms; note the lossy fields.
- **Done when:** you can read an MT message with the spec open and know which MX message replaces it.
- Est. hours: 2

#### 9.6.2 Data documentation — T2
- **Why:** generated, always-current documentation is a governance deliverable; dbt docs is the gateway drug before Phase 6 catalogs.
- **Learn:** dbt docs generation/persistence (`persist_docs`); exposures to declare downstream consumers; what belongs in model YAML vs the catalog; docs-as-code review flow.
- **Resource:** dbt docs documentation + "exposures" guide.
- **Tools:** FOSS: dbt docs (↔ catalog-generated docs in Phase 6) · Corp: dbt Cloud docs / Purview-generated lineage views.
- **Do:** fully document the capstone dbt project (every model + column description, one exposure for the EMT output) and publish the static site from CI later in Phase 3.
- **Done when:** a business analyst can answer "where does this EMT field come from?" without asking you.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.4.6 | Hub-and-spoke | Centralized hub feeding domain marts; the pre-mesh enterprise default | *Data Management at Scale* ch. 2 (architecture survey) | 20 |
| 1.12.4 | CFI (ISO 10962) | 6-char instrument classification code carried in reference data | ANNA CFI overview page | 20 |
| 1.12.5 | FIGI | Bloomberg's open venue-level instrument identifier; ISIN complement | openfigi.com overview | 20 |
| 1.12.9 | FpML | ISDA XML for OTC derivatives; appears at fund boundaries (hedging) | fpml.org "What is FpML" | 20 |
| 1.12.10 | FIX | Trading-venue messaging protocol; upstream of fund data, rarely modeled by you | fixtrading.org online spec intro | 20 |
| 1.12.11 | IBAN / SEPA | Payment-account identity standard underpinning EU cash legs | ECB SEPA overview | 15 |
| 3.1.2 | On-prem MPP warehouses | Teradata/Vertica/Netezza estates you'll migrate *from* | Teradata architecture overview | 30 |
| 3.2.11 | Geospatial storage | PostGIS/GeoParquet/H3; ESG & real-asset edge cases in funds | PostGIS "What is" + GeoParquet README | 30 |
| 5.3.3 | PRQL / Malloy | Composable query-language challengers to SQL | prql-lang.org tour | 20 |
| 5.4.1 | Interactive data prep | Visual cleanup tools (Alteryx/DataBrew) bought by business teams | Alteryx product overview | 15 |
| 8.2.6 | Anchor modeling / 6NF | Fully temporal modeling; Data Vault's stricter cousin | anchormodeling.com intro | 30 |

*T3 subtotal: 4 h*

### Capstone 2 — Fund-document lakehouse

- **Goal:** a working open lakehouse carrying real fund-data shapes (NAV series, holdings, EMT outputs, GLEIF entities) through bronze→silver→gold, with the format/catalog decisions documented like a vendor selection.
- **Stack (100% free):** MinIO (↔ ADLS Gen2), Apache Iceberg (↔ Databricks Delta / Snowflake managed Iceberg), Lakekeeper or Polaris REST catalog (↔ Unity Catalog / Glue), Trino (↔ Starburst / Athena / Synapse serverless), DuckDB + dbt Core (↔ dbt Cloud on a warehouse), Airbyte OSS (↔ Fivetran / ADF), AutomateDV raw-vault slice (↔ VaultSpeed), Docker Compose throughout.
- **Build:** (1) Airbyte lands Phase-1 Postgres + GLEIF golden copy into bronze (Parquet on MinIO); (2) silver Iceberg tables: cleansed NAV/holdings with DQ-checked conformance, raw vault for fund/share-class from two "source systems"; (3) gold: dbt marts incl. the EMT-shaped output and the SCD2 dimensional mart; (4) Trino federates a live Postgres dimension against Iceberg facts; (5) demonstrate time travel + schema evolution + a compaction run.
- **Architecture deliverables:** C4 context/container for the lakehouse; ADR-004 Iceberg vs Delta (estate-specific), ADR-005 REST catalog choice (lock-in analysis), ADR-006 medallion layer contracts (the sheet from 1.4.3 made binding).
- **Acceptance criteria:** end-to-end rebuild from empty MinIO via documented commands; `dbt build` green with tests + docs published; EMT output validates against the FinDatEx column spec; time-travel query reproduces yesterday's NAV report after a correction lands; every stack component annotated with its corporate equivalent in the README.
- Est. hours: 16

*Phase 2 total: 123 h (T1/T2 entries 103 h + T3 4 h + capstone 16 h)*


<a id="phase-3"></a>
## Phase 3: Distributed Compute, Orchestration & Engineering Practice (months 17–21, 118 h)

**Goal:** close the two biggest gaps that block scale — Spark and orchestration — and wrap the platform in software-engineering discipline: CI/CD for data, data versioning with write-audit-publish, integration testing, and managed schema change.
**Entry prerequisites:** Phase 2 (lakehouse running; dbt project to orchestrate).
**Exit criteria:** you can (1) explain a Spark job's stages and fix a skewed join from the UI; (2) defend Airflow vs Dagster vs ADF for a given team; (3) ship a pipeline change through CI with tests, data diff, and an audited publish; (4) run schema change in a regulated estate without downtime (expand–contract).

### T1/T2 topics

#### 4.1.1 Distributed batch compute (Spark) — T1
- **Why:** Spark is the named weak spot and the default heavy-lift engine in every fund-data estate (Databricks, Synapse, Fabric all sell it); architects who can't read the Spark UI can't review the platform's biggest bills.
- **Learn:** architecture: driver/executors, jobs→stages→tasks, the shuffle; DataFrame API and lazy evaluation; Catalyst optimizer + AQE; partitioning, skew, salting; join strategies (broadcast vs sort-merge) and when the planner picks wrong; caching/persistence levels; memory model and OOM debugging; writing to Iceberg; deployment modes (local, standalone, K8s, Databricks) at decision level.
- **Resource:** *Learning Spark, 2nd ed.* (Damji et al., free PDF from Databricks) ch. 1–7 + 12 (tuning) + official "Tuning" and "SQL Performance" docs. *Alternate:* *Spark: The Definitive Guide* pt. II.
- **Tools:** FOSS: Apache Spark (local + compose, ↔ Databricks / Synapse Spark / EMR) · Corp: Databricks (the de-facto enterprise Spark; evaluation level incl. Photon, cluster pricing).
- **Do:** generate a 50M-row holdings/prices dataset; compute per-fund daily NAV and rolling performance in PySpark against MinIO/Iceberg; engineer a skewed join, diagnose it in the Spark UI, fix it with broadcast + salting; document before/after stage timings.
- **Done when:** given an unfamiliar slow job, you go UI → stages → shuffle/skew → fix, and can explain each step to a junior; you can also argue when Spark is the *wrong* tool (DuckDB-size data).
- Est. hours: 36

#### 5.3.2 DataFrame transformation layer (PySpark / Polars / Ibis) — T2
- **Why:** the code half of the transformation layer; choosing SQL vs DataFrames (and which DataFrame runtime) is a standards decision you'll own.
- **Learn:** PySpark idioms vs pandas habits (no row loops, window specs); Polars lazy frames and when it replaces Spark below ~100GB; Ibis as portable dataframe API over 20+ engines; UDF cost model (Python UDF vs pandas UDF vs native).
- **Resource:** Polars user guide (lazy API) + Ibis "Why Ibis" docs.
- **Tools:** FOSS: Polars, Ibis, PySpark · Corp: Snowpark, Databricks (same concepts rebranded).
- **Do:** implement one silver transformation three ways (PySpark, Polars, dbt SQL); write a half-page standards note: which layer owns which transformation type and why.
- **Done when:** your standards note survives the question "why not do everything in SQL?"
- Est. hours: 8

#### 5.6.1 + 5.6.3 Orchestration (Airflow + Dagster, task- vs asset-oriented) — T1
- **Why:** orchestration is in the explicit mastery bias: the scheduler is the platform's nervous system, and the task-vs-asset paradigm choice shapes team workflow for years.
- **Learn:** Airflow: DAGs, operators, sensors, idempotent task design, backfills/catchup, executors (Local/Celery/K8s), datasets; Dagster: software-defined assets, partitions, asset checks, declarative automation — and why asset-orientation gives lineage for free; failure handling: retries, SLAs, alerting; orchestrator anti-patterns (business logic in DAG files, XCom abuse); Prefect/Mage awareness; ADF + Managed Airflow as the Azure reality.
- **Resource:** Dagster docs "Concepts" (assets, partitions) + *Data Pipelines with Apache Airflow* 2nd ed. (Harenslak & de Ruiter) ch. 1–6, 12.
- **Tools:** FOSS: Dagster (primary hands-on), Airflow (market fluency) · Corp: Azure Data Factory / MWAA / Cloud Composer (evaluation level).
- **Do:** orchestrate the Capstone-2 pipeline as Dagster assets with daily partitions and asset checks; rebuild one branch of it as an Airflow DAG; write a comparison memo (dev loop, backfills, lineage, ops burden).
- **Done when:** you can run a clean 30-day backfill after a logic fix and explain exactly which partitions recomputed and why.
- Est. hours: 20

#### 9.2.2 Data versioning & write-audit-publish — T2
- **Why:** branch-merge workflows for data are how regulated platforms ship changes without bad data reaching consumers; WAP is the pattern auditors love.
- **Learn:** Iceberg branching/tagging natively; write-audit-publish flow; lakeFS Git-like model (repos, branches, merges over object storage); Nessie catalog-level versioning; DVC for ML-ish file versioning (awareness); choosing between table-level and lake-level versioning.
- **Resource:** Iceberg branching docs + lakeFS docs ("How it works" + WAP tutorial).
- **Tools:** FOSS: Iceberg branches, lakeFS (↔ no direct corp equivalent — Databricks/Snowflake time travel + clones) · Corp: Snowflake zero-copy clones (evaluation level).
- **Do:** implement WAP in the Dagster pipeline: write to an Iceberg branch, run DQ checks, fast-forward publish on green, alert-and-hold on red.
- **Done when:** a deliberately corrupted load never becomes visible to the gold consumer, and you can show the audit trail.
- Est. hours: 8

#### 9.3.1 CI/CD for data platforms — T2
- **Why:** the deployment pipeline is where engineering standards become enforceable; data teams without CI ship regressions to regulators.
- **Learn:** GitHub Actions: workflows, environments, secrets, matrix jobs; what to run per PR vs per merge for a data repo (lint/ruff, unit tests, dbt build on prod-like sample, docs publish); deployment gates and approvals; GitOps concept (Argo CD awareness for later K8s phase).
- **Resource:** GitHub Actions official docs (core concepts) + dbt "CI in practice" guide.
- **Tools:** FOSS: GitHub Actions (↔ Azure DevOps Pipelines, GitLab CI) · Corp: Azure DevOps (EU enterprise default; evaluation level).
- **Do:** add CI to the capstone repo: ruff + pytest + `dbt build --select state:modified+` on PR, docs site publish on merge.
- **Done when:** a PR that breaks a dbt test cannot merge, and you can explain every job in the workflow file.
- Est. hours: 8

#### 9.3.2 Data-aware CI — T2
- **Why:** code-green/data-wrong is the classic data regression; data-aware CI (state deferral, data diff) catches what unit tests can't.
- **Learn:** dbt slim CI (state:modified, defer); SQLMesh virtual environments and automatic change categorization (breaking vs non-breaking); data-diff concept (row/column-level diffs between prod and PR build); Datafold as the managed version.
- **Resource:** SQLMesh docs ("Plans" + virtual environments) + dbt slim CI guide.
- **Tools:** FOSS: SQLMesh (eval hands-on), dbt slim CI · Corp: Datafold (evaluation level).
- **Do:** run the same breaking change through dbt slim CI and SQLMesh plan; record which caught what, and at what compute cost.
- **Done when:** you can tell a team when slim CI is enough and when diff-based CI pays for itself.
- Est. hours: 5

#### 9.4.3 Integration testing for pipelines — T2
- **Why:** pipelines fail at the seams (connections, schemas, permissions); throwaway-infra tests are the only honest test of the seams.
- **Learn:** Testcontainers-python (Postgres/MinIO/Kafka containers per test); test pyramid for data (unit SQL → component → end-to-end on sample); golden datasets and snapshot testing; contract tests preview (Pact concept; full data contracts in Phase 8).
- **Resource:** Testcontainers-python docs + one well-known reference blog on data pipeline testing pyramids (verify link at assembly).
- **Tools:** FOSS: Testcontainers, pytest · Corp: same (this layer is tool-agnostic).
- **Do:** write an integration test that spins Postgres + MinIO, runs the idempotent loader twice, and asserts end-state invariants.
- **Done when:** `uv run pytest -m integration` passes on a machine with only Docker installed.
- Est. hours: 5

#### 9.7.1 Schema migrations & change management — T2
- **Why:** regulated estates change schemas under change-advisory scrutiny; expand–contract and versioned migrations are how you do it without downtime or drama.
- **Learn:** Flyway/Liquibase models (versioned vs declarative); Alembic for Python shops; expand–contract (parallel change) pattern; backward-compatible deployment ordering (DB before code); migration review and rollback reality (roll forward).
- **Resource:** Flyway docs (concepts) + Martin Fowler "Parallel Change" / "Evolutionary Database Design" articles.
- **Tools:** FOSS: Flyway or Alembic (↔ Liquibase enterprise, Redgate) · Corp: Liquibase Pro / Azure DevOps-integrated change flows (evaluation level).
- **Do:** rename a column on the live Phase-1 Postgres via expand–contract across three migration versions, with the loader running throughout.
- **Done when:** zero failed loads during the rename, and the migration history table tells the full story.
- Est. hours: 5

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 4.4.1 | General distributed frameworks | Ray/Dask — Python-native distributed compute beyond Spark (ML-leaning) | Ray "Overview" docs page | 30 |
| 4.4.2 | Specialized frameworks | Modin etc. — drop-in pandas acceleration; niche | Modin README | 10 |
| 5.1.2 | Code-first ETL (NiFi) | Visual flow-based ingestion engine; common in banks' legacy ingestion | NiFi "Overview" doc | 25 |
| 9.4.4 | Load/performance testing | k6/Locust/JMeter — throughput testing for data APIs and engines | k6 "What is k6" page | 25 |
| 9.5.2 | Data diff tools | Row-level diffs across model changes (data-diff, Datafold) | Datafold data-diff README | 20 |
| 9.6.1 | Code documentation | MkDocs/Sphinx static docs; you'll publish dbt docs instead | MkDocs getting started | 20 |
| 9.9.1 | Notebooks in production | Papermill/Ploomber parameterized notebook jobs; contested practice | Papermill README | 20 |

*T3 subtotal: 2.5 h*

### Capstone 3 — Orchestrated Spark NAV pipeline

- **Goal:** the lakehouse grows an industrial-strength compute and delivery layer: Spark for scale, Dagster for orchestration, WAP for safety, CI for discipline.
- **Stack (100% free):** Apache Spark (↔ Databricks / Synapse Spark), Dagster OSS (↔ Dagster+ / ADF), Airflow (one comparison DAG; ↔ MWAA / Composer), Iceberg branches for WAP (↔ Snowflake clones), lakeFS optional layer (↔ —), GitHub Actions (↔ Azure DevOps), Testcontainers + pytest via uv, Flyway (↔ Liquibase Pro), all on the Phase-2 compose stack.
- **Build:** (1) Spark job computes daily NAV + rolling performance from 50M-row holdings/prices into silver Iceberg; (2) Dagster assets wrap ingestion → Spark → dbt gold with daily partitions and asset checks; (3) WAP: every load lands on a branch, publishes only on green checks; (4) CI runs lint, unit, integration (Testcontainers), and slim dbt build per PR; (5) Flyway manages the Postgres source schema, demonstrated with a live expand–contract change; (6) 30-day backfill executed and timed.
- **Architecture deliverables:** C4 container diagram updated with compute/orchestration layer; ADR-007 orchestrator selection (Dagster vs Airflow vs ADF), ADR-008 WAP via Iceberg branches, ADR-009 Spark-vs-DuckDB engine threshold (when the cluster is justified).
- **Acceptance criteria:** full pipeline green from `dagster dev` + one CLI command; corrupted-load drill leaves gold untouched with an audit trail; skewed-join fix documented with UI screenshots; backfill recomputes exactly the intended partitions; CI blocks a breaking PR in under 10 minutes.
- Est. hours: 20

*Phase 3 total: 118 h (T1/T2 entries 95 h + T3 2.5 h + capstone 20 h ≈ 118)*


<a id="phase-4"></a>
## Phase 4: Streaming & Event-Driven Integration (months 22–27, 119 h)

**Goal:** close the streaming gap end-to-end: Kafka as the integration backbone, CDC off operational systems, the Beam-model semantics (event time, watermarks, windows), Flink for stateful processing, schema governance on the wire, and the event-driven patterns (outbox, saga, event sourcing) that regulated trade lifecycles are built from.
**Entry prerequisites:** Phases 1–3 (integration-pattern theory from DDIA; lakehouse + orchestrator to land streams into).
**Exit criteria:** you can (1) design a CDC-to-lakehouse flow with stated delivery guarantees and prove them; (2) explain watermarks well enough to debug a wrong window result; (3) own a schema-compatibility policy and show the registry enforcing it; (4) choose among Kafka/Event Hubs/Service Bus/Temporal/Camunda for a given fund workflow and defend it.

### T1/T2 topics

#### 2.4.1 Distributed logs (Kafka) — T1
- **Why:** Kafka is the backbone of modern financial data integration; the architect sizes it, secures it, sets its guarantees, and debugs it when settlement events go missing.
- **Learn:** log abstraction: topics, partitions, offsets, segments, retention/compaction; producers: acks, idempotent producer, transactions; consumers: groups, rebalancing (cooperative), lag; replication: ISR, min.insync.replicas, unclean elections; KRaft (no more ZooKeeper); partitioning/key design and ordering guarantees; compacted topics as changelog tables; Kafka-API-compatible alternatives (Redpanda) and Azure Event Hubs Kafka surface.
- **Resource:** *Kafka: The Definitive Guide* 2nd ed. (free PDF via Confluent), ch. 1–7 + 10 (cross-cluster) — skim ops chapters.
- **Tools:** FOSS: Apache Kafka or Redpanda in compose (↔ Confluent Cloud, Azure Event Hubs, AWS MSK) · Corp: Confluent Cloud & Event Hubs (evaluation level: pricing units, quotas, Kafka-compat limits).
- **Do:** stand up single-broker KRaft Kafka; produce fund-order events keyed by ISIN; demonstrate ordering per key, consumer-group rebalance behavior, and a compacted `fund-reference` topic serving as a table.
- **Done when:** you can answer "can we lose or duplicate an order event?" for a given producer/consumer config matrix, correctly, every time.
- Est. hours: 14

#### 1.8.2 Delivery semantics (at-most/at-least/exactly-once) — T1
- **Why:** "exactly-once" claims must be audited, not believed, when the payload is a settlement instruction or a NAV correction.
- **Learn:** what each guarantee costs; where duplication enters (producer retry, consumer reprocess); Kafka EOS: idempotent producer + transactions + read_committed — and its boundaries (within-Kafka, not end-to-end); end-to-end exactly-once = at-least-once + idempotent/transactional sink; the Flink two-phase-commit sink connection.
- **Resource:** *Kafka: The Definitive Guide* ch. 8 (exactly-once semantics) + Confluent EOS blog series (verify link at assembly).
- **Do:** kill your consumer mid-batch in three configurations (auto-commit, manual commit-after-process, transactional) and tabulate observed duplicates/losses against prediction.
- **Done when:** you can mark, on any pipeline diagram, every point where the guarantee degrades and what restores it.
- Est. hours: 4

#### 2.3.1 + 1.8.10 Log-based CDC (Debezium) — T1
- **Why:** CDC is how regulated estates go event-driven without touching fragile core systems — the highest-leverage integration pattern in the fund back office.
- **Learn:** logical decoding (Postgres WAL → events); Debezium architecture on Kafka Connect; snapshot modes and re-snapshotting; event envelope (before/after/op/ts, tombstones); schema-change events; ordering & transaction boundaries downstream; outbox-via-CDC; delivery guarantees of the whole chain; landing CDC into Iceberg (merge vs append+dedupe).
- **Resource:** Debezium official documentation (architecture + Postgres connector + outbox event router). *Alternate:* DDIA ch. 11 (rereading "keeping systems in sync" with practitioner eyes).
- **Tools:** FOSS: Debezium + Kafka Connect (↔ Qlik Replicate, GoldenGate, ADF CDC, Fivetran HVR) · Corp: Qlik Replicate / GoldenGate (the EU bank incumbents; evaluation level).
- **Do:** stream the Phase-1 Postgres `orders` and `nav` tables through Debezium into Kafka, land them in Iceberg via a merge job, and prove end-state equality after a mid-stream connector restart.
- **Done when:** you can explain to an auditor why the lakehouse copy is complete and ordered, including the restart story.
- Est. hours: 9

#### 2.2.2 Stream connectors (Kafka Connect) — T2
- **Why:** Connect is the operational workhorse around Kafka — connectors, converters, and transforms are where streaming integrations actually live or die.
- **Learn:** workers/tasks/distributed mode; source vs sink connectors; converters (Avro/JSON/Protobuf) vs SMTs; offset management; error handling + DLQ topics; connector operations (pause/resume/restart).
- **Resource:** Kafka Connect official documentation (concepts + worker config).
- **Tools:** FOSS: Kafka Connect (↔ Confluent managed connectors, Event Hubs Capture).
- **Do:** configure an S3/MinIO sink connector with DLQ; poison one message and show it parked with headers explaining why.
- **Done when:** you can size a Connect cluster (workers/tasks) for a given connector load and explain failure recovery.
- Est. hours: 4

#### 8.3.1 + 8.3.2 + 1.11.2 Schema registry, schema languages & serialization — T2
- **Why:** the registry is the contract-enforcement point of the streaming estate; Avro vs Protobuf vs JSON Schema is a recurring standards decision the architect owns.
- **Learn:** registry model (subjects, versions, compatibility levels); Avro: schemas, logical types, evolution rules; Protobuf: field numbers, unknown fields; JSON Schema's weaker evolution story; wire format (magic byte + schema ID); subject naming strategies; Apicurio vs Confluent SR licensing.
- **Resource:** Confluent Schema Registry docs (fundamentals + compatibility) + Avro spec (evolution section).
- **Tools:** FOSS: Apicurio or Confluent SR Community (↔ Confluent Cloud SR, Azure Schema Registry, AWS Glue SR).
- **Do:** register the fund-order schema in Avro; evolve it three ways (add optional, rename, type change) under `BACKWARD` and `FULL` modes; record what the registry rejects and why.
- **Done when:** you can write the org's schema-evolution policy and justify each compatibility level per topic class.
- Est. hours: 6

#### 1.9.7 Schema evolution compatibility (the policy) — T1
- **Why:** forward/backward compatibility is a governance decision with org-wide blast radius — the architect writes this policy and arbitrates exceptions.
- **Learn:** backward/forward/full/transitive semantics precisely; who upgrades first (consumers vs producers) under each; default-value discipline; breaking-change playbook (new subject vs dual-write vs upcaster); how the same policy applies to Iceberg table schemas and API payloads — one mental model across batch, stream, and API.
- **Resource:** Confluent compatibility docs + Iceberg schema-evolution docs (read as one policy domain).
- **Do:** write a one-page "Schema Evolution Policy" covering Kafka topics, Iceberg tables, and REST payloads: levels, exception process, breaking-change playbook.
- **Done when:** given any proposed field change, you can rule allow/deny/migrate in under a minute, with the rule cited.
- Est. hours: 4

#### 1.9.1 + 1.9.2 + 1.9.4 (with 1.9.3, 1.9.5, 1.9.6) Streaming semantics — the Beam model — T1
- **Why:** event time, watermarks, and windows are the conceptual machinery that make streaming results *correct*, not just fast — and restatement-heavy finance demands event-time rigor.
- **Learn:** event time vs processing time; the what/where/when/how framing; windowing (tumbling/sliding/session); watermarks: perfect vs heuristic, propagation, and why they're a tradeoff between latency and completeness; triggers & accumulation modes; late data: allowed lateness, side outputs, restatements; stateful processing: keyed state, checkpoints (T2 depth, deepened in Flink below).
- **Resource:** Akidau et al., *Streaming Systems*, ch. 1–4 (+ ch. 7 state, skim) — the canonical text, per the taxonomy.
- **Do:** on paper (Beam-model diagrams), design the windowing/watermark/trigger strategy for "intraday fund-flow totals per share class, restated as late orders arrive" — then implement it in Flink in the next entry.
- **Done when:** you can explain to a junior why a count was wrong yesterday and exactly which knob (watermark, lateness, trigger) fixes it — and what that costs.
- Est. hours: 10

#### 4.2.1 Stateful stream processing (Flink) — T1
- **Why:** Flink is the reference stateful engine (and what AWS/Azure managed streaming runs underneath); real-time NAV estimates and exposure monitoring are Flink-shaped problems.
- **Learn:** dataflow graph, keyed streams, state backends (RocksDB); checkpointing & exactly-once internals (aligned barriers, unaligned); event-time operators: window/process functions, timers; watermark strategies in code; Flink SQL & Table API; savepoints, upgrades, state evolution; Kafka source/sink with EOS; Spark Structured Streaming compared (micro-batch model, when it's enough).
- **Resource:** Flink official docs ("Learn Flink" track + "Stateful Stream Processing" concepts) — current and free; book alternatives are dated.
- **Tools:** FOSS: Apache Flink (↔ AWS Managed Flink, Azure HDInsight/Flink, Confluent Flink, GCP Dataflow) · Corp: Confluent Flink SQL / Azure Stream Analytics (evaluation level).
- **Do:** implement the 1.9 design: Flink job consuming order events, computing per-share-class windowed flow totals with heuristic watermarks, allowed lateness + side output for stragglers, checkpointed to MinIO, EOS into Iceberg; kill/restore from checkpoint and savepoint-upgrade once.
- **Done when:** the restored job produces byte-identical results, and you can narrate the checkpoint barrier mechanism from memory.
- Est. hours: 14

#### 1.8.3 + 1.8.4 Outbox & saga (implemented) — T1
- **Why:** dual-write is the classic event-driven corruption bug and sagas are the bedrock of multi-service trade lifecycles — these two patterns turn theory into production-shaped reflexes.
- **Learn:** outbox: same-transaction event capture, Debezium outbox router, idempotent consumers; saga: choreography vs orchestration, compensation design, isolation anomalies (dirty compensations), timeout/dead-man handling; where Temporal/Camunda fit as saga orchestrators; Azure Cloud Design Patterns catalog entries for both.
- **Resource:** microservices.io pattern pages (Outbox, Saga) + Azure Architecture Center pattern catalog (Saga) — https://learn.microsoft.com/en-us/azure/architecture/patterns/.
- **Do:** add an outbox table to the Phase-1 order service; route it through Debezium's outbox SMT; build a 3-step subscription saga (reserve cash → book units → confirm) with a deliberate step-2 failure compensating cleanly.
- **Done when:** the saga's failure path leaves the system consistent and the audit log tells the whole story without manual digging.
- Est. hours: 7

#### 1.8.5 + 1.8.6 Event sourcing & CQRS — T1/T2
- **Why:** audit-by-construction (1.8.5, T1) is the killer feature for regulated finance — the event log *is* the regulator's evidence; CQRS (1.8.6, T2) is its usual companion and over-application hazard.
- **Learn:** state as fold over events; commands vs events; snapshots; replay & temporal queries ("position as-known-at"); schema evolution of events (upcasting); when ES is wrong (CRUD apps, weak invariants); CQRS read models from the event log; eventual consistency between write/read sides; the Kafka-as-event-store debate (and its caveats).
- **Resource:** Stopford, *Designing Event-Driven Systems* (free Confluent PDF), ch. on event sourcing/CQRS + Fowler's Event Sourcing essay.
- **Do:** event-source the share-register: order/allocation/transfer events → fold to positions; answer "investor X's position as known on date D" from replay; write a half-page ADR on where ES applies in a TA system and where it must not.
- **Done when:** you can defend the as-known-at vs as-of distinction (bitemporality) with a fund example, and say no to ES somewhere.
- Est. hours: 5

#### 1.8.7 + 1.8.8 Dead-letter queues & backpressure — T2
- **Why:** these two decide whether a bad message or a slow consumer takes down the flow or just a metric.
- **Learn:** DLQ design: park with diagnostic headers, replay procedure, poison-pill detection; backpressure: bounded buffers, consumer lag as signal, Flink's credit-based flow control; alerting on lag/DLQ depth.
- **Resource:** Confluent error-handling blog/docs + Flink network-stack docs section (backpressure monitoring).
- **Do:** define the DLQ + replay runbook for the CDC pipeline (who triages, how to replay safely, idempotency requirement).
- **Done when:** a poisoned message at 2am pages no one and is replayable at 9am without data loss.
- Est. hours: 2.5

#### 2.4.2 Message brokers vs logs — T2
- **Why:** queue semantics (RabbitMQ/Service Bus) and log semantics (Kafka) solve different problems; picking wrong is expensive in both directions.
- **Learn:** competing consumers vs consumer groups; per-message ack/redelivery vs offsets; routing (exchanges) vs partitioning; when a queue wins (task distribution, request/reply, per-message TTL) vs a log (replay, fan-out, ordering, retention); AMQP basics; Azure Service Bus as the corp queue.
- **Resource:** RabbitMQ "Concepts" docs + a queue-vs-log comparison from the Kafka guide ch. 1.
- **Tools:** FOSS: RabbitMQ (↔ Azure Service Bus, AWS SQS) — short hands-on only.
- **Do:** decision table: 6 fund-platform messaging needs → queue or log, one line of why each.
- **Done when:** you never propose Kafka for request/reply or RabbitMQ for replayable integration again.
- Est. hours: 3

#### 5.6.4 Durable execution (Temporal) — T2
- **Why:** trade lifecycle, KYC, and corporate-actions workflows are long-running, stateful, and retry-heavy — durable execution is the modern saga orchestrator and FS adoption is real.
- **Learn:** workflow-as-code model: deterministic workflow code, activities, event-history replay; retries/timeouts/heartbeats; signals & queries; versioning running workflows; where Temporal vs a BPM engine vs a queue fits; Azure Durable Functions as the corp-native analogue.
- **Resource:** Temporal docs ("Core concepts" + Python SDK tutorial).
- **Tools:** FOSS: Temporal OSS in compose (↔ Temporal Cloud, Azure Durable Functions, AWS Step Functions).
- **Do:** reimplement the Phase-4 saga as a Temporal workflow with retries and a compensation path; kill the worker mid-run and watch it resume.
- **Done when:** you can explain event-history replay and why workflow code must be deterministic.
- Est. hours: 4

#### 5.6.5 BPM / process orchestration (Camunda, BPMN/DMN) — T2
- **Why:** banks and fund administrators run BPMN engines for settlement, onboarding, and exception handling; the architect must speak BPMN/DMN and know when model-driven beats code-driven orchestration.
- **Learn:** BPMN 2.0 working subset: tasks, gateways, events (timer/message/error), pools/lanes; DMN decision tables + FEEL; Camunda 7 vs 8/Zeebe architecture & licensing; human-task workflows and exception queues; BPM vs Temporal vs Airflow — three orchestration species, one decision framework.
- **Resource:** Camunda 8 docs (BPMN + DMN references) + bpmn.io tutorials.
- **Tools:** FOSS: Camunda (Zeebe) or Flowable (↔ Camunda Enterprise, Pega, IBM BPM).
- **Do:** model the subscription-order lifecycle in BPMN with an error-handling path to a human task; encode the "compliance review required?" rule as a DMN table; run both in Camunda.
- **Done when:** you can defend orchestration-tool choice (BPM vs durable execution vs scheduler) for three different fund workflows.
- Est. hours: 5

#### 1.11.1 + 1.11.3 Data protocols & async API standards — T2
- **Why:** protocol literacy (gRPC vs REST vs Arrow Flight; AsyncAPI/CloudEvents) is the architect's interface-design toolkit across the estate.
- **Learn:** gRPC/HTTP2 + Protobuf contract-first; REST maturity in practice; Arrow Flight/ADBC for bulk analytical transfer (vs JDBC/ODBC row-marshaling); WebSocket/MQTT/AMQP placement; AsyncAPI as OpenAPI-for-events; CloudEvents envelope; SOAP/OData literacy for the legacy estate you'll meet.
- **Resource:** AsyncAPI docs (concepts) + Arrow Flight introduction + CloudEvents spec overview.
- **Do:** write the AsyncAPI document for your fund-order Kafka topics (channels, messages, schemas) and render its docs.
- **Done when:** you can pick the transfer protocol for: BI extract, microservice call, market-data feed, file drop — with numbers, not vibes.
- Est. hours: 3

#### 1.4.1 + 1.4.2 Lambda vs Kappa — T2
- **Why:** the batch/speed-layer debate frames every "do we need streaming?" conversation; medallion-with-streaming is today's synthesis.
- **Learn:** Lambda's dual-codebase tax; Kappa's replay-the-log answer and its storage/retention implications; how table formats + streaming ingestion (your Phase-2/4 stack) dissolve most of the dichotomy.
- **Resource:** Kreps' "Questioning the Lambda Architecture" (O'Reilly radar essay) + *Streaming Systems* ch. 1 framing.
- **Do:** one-page position note: which architecture your capstone platform actually is, and why that's the right call for fund data.
- **Done when:** you can articulate what you'd change if regulators demanded sub-minute NAV-error detection.
- Est. hours: 2

#### 1.2.2 + 1.2.3 Micro-batch vs true streaming — T2
- **Why:** Spark Structured Streaming (micro-batch) vs Flink (event-at-a-time) is a real engine decision with latency, state, and ops consequences.
- **Learn:** micro-batch mechanics & latency floor; continuous processing; state handling differences; ops profile (Spark cluster reuse vs Flink job clusters); decision rubric by latency class (minutes/seconds/sub-second).
- **Resource:** Spark Structured Streaming programming guide (overview) read against Flink's "Stateful Stream Processing" concepts page.
- **Do:** rebuild one Flink aggregation in Spark Structured Streaming on the existing cluster; compare latency, code, and ops burden in a half-page note.
- **Done when:** you can place any fund use case in the right latency class and name the engine.
- Est. hours: 3

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.2.4 | Real-time / low-latency paradigm | Sub-second serving paths; mostly out of fund-admin scope | *Streaming Systems* ch. 1 sidebar | 15 |
| 1.3.4 | RT / user-facing analytics workload | High-concurrency sub-second dashboards (Pinot/Druid class) | StarTree "what is user-facing analytics" blog | 25 |
| 1.8.12 | Bulkhead | Resource isolation so one consumer can't sink the ship | Azure patterns catalog: Bulkhead | 15 |
| 1.8.13 | Circuit breaker | Fail-fast wrapper for flaky dependencies | Azure patterns catalog: Circuit Breaker | 15 |
| 2.3.2 | Trigger-based CDC | DB triggers populate change tables; intrusive legacy approach | Debezium FAQ comparison section | 15 |
| 2.3.3 | Snapshot-based CDC | Periodic diffing (Fivetran-style); simple, lossy between snapshots | Fivetran docs: sync modes | 15 |
| 2.4.3 | Event mesh | Federated brokers across sites/clouds (Solace; big in capital markets) | Solace "what is an event mesh" page | 25 |
| 4.3.4 | RT analytics engines | Pinot/Druid/ClickHouse serving layer for 1.3.4 workloads | Pinot docs intro | 25 |
| 4.3.5 | Streaming databases | Incrementally-maintained materialized views (Materialize/RisingWave) | RisingWave "why" docs page | 25 |

*T3 subtotal: 3 h*

### Capstone 4 — Real-time fund-flow & price CDC streaming

- **Goal:** the platform gains a streaming spine: operational changes flow as events, stateful aggregations stay correct under late data, and every guarantee is stated and demonstrated.
- **Stack (100% free):** Kafka KRaft or Redpanda (↔ Confluent Cloud / Event Hubs), Kafka Connect + Debezium with outbox router (↔ Qlik Replicate / GoldenGate / ADF), Apicurio or Confluent SR with Avro (↔ Confluent Cloud SR / Azure Schema Registry), Flink (↔ Confluent Flink / Managed Flink / ASA), Iceberg sink on MinIO, Temporal saga + Camunda BPMN process from the entries above, Dagster supervising batch reconciliation, all in compose.
- **Build:** (1) Debezium streams orders/NAV + the outbox topic; (2) Flink computes per-share-class windowed flow totals (heuristic watermarks, allowed lateness, late-event side output) exactly-once into Iceberg; (3) nightly Dagster batch reconciles streamed totals against batch recompute and alerts on drift; (4) schema registry enforces the 1.9.7 policy (one rejected evolution kept as evidence); (5) the subscription saga (Temporal) and BPMN process (Camunda) run against the same events; (6) chaos drills: kill broker, connector, Flink job — document recovery and guarantee held.
- **Architecture deliverables:** C4 updated with the streaming spine; ADR-010 log platform choice (Kafka vs Event Hubs vs Redpanda), ADR-011 delivery-guarantee design (where exactly-once is real and where idempotent-at-least-once is the honest answer), ADR-012 orchestration species (BPM vs durable execution vs scheduler, per workflow).
- **Acceptance criteria:** reconciliation drift = 0 over a 3-day simulated run incl. injected late/duplicate events; each chaos drill has a written recovery narrative naming the mechanism (ISR, checkpoint, offset commit); schema policy violation is blocked by the registry and the evidence archived; saga failure path leaves consistent state with full audit trail.
- Est. hours: 16

*Phase 4 total: 119 h (T1/T2 entries 99.5 h + T3 3 h + capstone 16 h ≈ 119)*


<a id="phase-5"></a>
## Phase 5: Cloud Platform Architecture & Operations — Azure (months 28–33, 108 h + 37 h Appendix A)

**Goal:** turn the laptop platform into a cloud-shaped one: Azure reference architecture (WAF/CAF), infrastructure as code, Kubernetes as the runtime substrate, the Azure data services at evaluation depth, and the operations disciplines (observability, DR, FinOps) that keep a regulated platform alive and affordable.
**Entry prerequisites:** Phases 2–4 (a real multi-service stack worth provisioning); Appendix A items A.3 (networking), A.4 (Fabric), A.5 (KQL), A.6 (Kubernetes), A.22 (relational HA), A.25 (warehouse performance), A.26 (chaos/resilience testing) are scheduled inside this phase.
**Exit criteria:** you can (1) run a Well-Architected review of your own design and find real findings; (2) provision and tear down the platform from code alone; (3) state RTO/RPO for each platform tier and the topology that delivers it; (4) produce a defensible monthly-cost model for the Azure target architecture; (5) operate the stack on Kubernetes locally and explain what AKS changes.

### T1/T2 topics

#### 8.1.1 Azure reference architecture (WAF + CAF landing zones) — T1
- **Why:** the Well-Architected pillars and CAF landing zones are the daily design language on the primary cloud — reviews, RFPs, and audits are all conducted in it.
- **Learn:** WAF's five pillars and the data-platform-specific lenses; CAF landing zones: management groups, subscriptions-as-units, policy-driven governance (Azure Policy), hub-spoke network topology; identity baseline (Entra ID, managed identities); Azure analytics reference architectures (Synapse/Fabric/Databricks patterns in the Architecture Center); region pairs & availability zones for EU data residency.
- **Resource:** Microsoft Learn: Well-Architected Framework (data workload guidance) + CAF "Ready" methodology / enterprise-scale landing zone docs.
- **Tools:** FOSS: — (conceptual; exercised via IaC below) · Corp: Azure (primary), AWS Well-Architected as the comparison vocabulary.
- **Do:** run a written WAF review of your Capstone-4 architecture as if it ran on Azure: one finding + remediation per pillar.
- **Done when:** you can sketch a CSSF-friendly landing zone (mgmt groups → subscriptions → networks → identities) on a whiteboard and justify each boundary.
- Est. hours: 14

#### 9.10.1 Infrastructure as code (OpenTofu/Terraform) — T1
- **Why:** a named weak spot, and the medium in which every platform you design will actually ship; "architecture" that isn't in code is a slide.
- **Learn:** HCL: providers, resources, data sources, variables/outputs; state: backends, locking, drift, import; modules and composition; plan/apply discipline and CI integration; workspaces vs directory-per-env; secrets handling in IaC; Terraform↔OpenTofu split (BSL vs MPL) and what it means for vendor selection; azurerm provider patterns.
- **Resource:** OpenTofu docs (language + state) + *Terraform: Up & Running* 3rd ed. (concept chapters; commands transfer).
- **Tools:** FOSS: OpenTofu (↔ Terraform Cloud/Enterprise, Azure-native Bicep below) · Corp: Terraform Enterprise (evaluation level).
- **Do:** put the entire compose-era platform under OpenTofu using the docker, kubernetes, and helm providers: one `tofu apply` builds the full local stack; plus an azurerm module for the target architecture validated with `tofu plan` against a free-trial subscription (plan-only — no spend).
- **Done when:** `tofu destroy && tofu apply` reproduces the platform byte-for-byte, and you can explain every line of a teammate's plan output.
- Est. hours: 16

#### 9.10.2 Cloud-native IaC (Bicep) — T2
- **Why:** Microsoft shops mandate Bicep/ARM for Azure-only estates; you must hold a reasoned Bicep-vs-Terraform position in vendor-aligned organizations.
- **Learn:** Bicep syntax, modules, what-if deployments; ARM deployment model (incremental/complete); when Bicep wins (day-0 Azure features, no state file) vs Terraform (multi-cloud, ecosystem); AVM (Azure Verified Modules).
- **Resource:** Microsoft Learn Bicep fundamentals path (free).
- **Do:** rewrite one OpenTofu module (storage account + key vault + VNet) in Bicep; run `what-if`; write the 10-line comparison.
- **Done when:** you can recommend Bicep or Terraform for a given org and defend it against the other camp.
- Est. hours: 4

#### 2.1.2 + 5.6.2 Azure Data Factory (bulk movement + orchestration) — T2
- **Why:** ADF is the incumbent Azure data-movement and orchestration service you will meet in every Luxembourg estate — evaluation fluency is mandatory even if you'd choose Dagster.
- **Learn:** pipelines, activities, triggers; copy activity & integration runtimes (incl. self-hosted IR for on-prem); mapping data flows (Spark under the hood); ADF vs Synapse pipelines vs Fabric Data Factory lineage; pricing model (DIU-hours, activity runs); CI/CD for ADF (ARM/Git mode); where ADF orchestration breaks down vs code-first orchestrators.
- **Resource:** ADF official docs (concepts + copy activity + self-hosted IR).
- **Tools:** Corp: ADF/Fabric DF (↔ FOSS: Airbyte + Dagster from earlier phases).
- **Do:** design (on paper + pricing calculator) the ADF implementation of your Airbyte+Dagster ingestion: pipeline sketch, IR placement for an on-prem TA system, monthly cost estimate.
- **Done when:** you can argue ADF-vs-code-first for three scenarios (lift-and-shift shop, product team, hybrid estate) with costs.
- Est. hours: 6

#### 4.2.2 Cloud-native streaming (Event Hubs, Stream Analytics) — T2
- **Why:** Event Hubs is what "Kafka on Azure" usually means in practice; knowing its limits against real Kafka is a recurring design question.
- **Learn:** Event Hubs model: namespaces, throughput units/processing units, partitions, capture; Kafka-protocol surface and its gaps (no compaction, transactions limits); Azure Stream Analytics SQL jobs vs Flink; Service Bus vs Event Hubs vs Event Grid triage.
- **Resource:** Event Hubs docs (features + Kafka compatibility page).
- **Do:** map every Capstone-4 Kafka feature you used to Event Hubs; flag the ones that don't translate and their workarounds.
- **Done when:** you can answer "can we just use Event Hubs?" with a feature-by-feature verdict.
- Est. hours: 3

#### 4.1.2 Serverless compute (Azure Functions) — T2
- **Why:** functions are the glue tier of cloud data platforms (event handlers, light transforms, API shims); the architect decides where glue ends and engines begin.
- **Learn:** triggers/bindings, hosting plans (consumption/premium), cold starts; Durable Functions (ties to 5.6.4); when functions become an anti-pattern (long-running, stateful, heavy data movement).
- **Resource:** Azure Functions docs (concepts + hosting options).
- **Do:** local-run (Functions Core Tools, free) an event-triggered function that validates an incoming EMT file drop and emits an event; document its Azure cost profile at 10k files/month.
- **Done when:** you can draw the line between function-glue and pipeline-engine for five workloads.
- Est. hours: 3

#### 4.3.2 Cloud query services — T2
- **Why:** serverless SQL over the lake (Synapse serverless, Athena) is the cheap-and-cheerful tier of lakehouse consumption; knowing its price/perf envelope completes the engine matrix.
- **Learn:** per-TB-scanned pricing mechanics and the partitioning/pruning economics it creates; OPENROWSET/external tables; Athena/Trino lineage; when serverless SQL beats a running warehouse and when it bankrupts you.
- **Resource:** Synapse serverless SQL docs (best practices page).
- **Do:** estimate query cost for your gold layer at three partitioning strategies; one paragraph on the design pressure per-TB pricing creates.
- **Done when:** you can explain why file layout *is* the cost model in serverless SQL.
- Est. hours: 2

#### 8.1.2 Vendor reference architectures — T2
- **Why:** Databricks/Snowflake/Fabric blueprints are the shapes vendors will pitch at your employer; you need to read them critically, not learn them reverently.
- **Learn:** Databricks lakehouse reference (Unity Catalog-centric, medallion); Snowflake data cloud patterns (shares, zero-copy); Fabric end-to-end (OneLake-centric, capacity-based); what each blueprint optimizes for the *vendor*; mapping all three onto your open-stack mental model.
- **Resource:** each vendor's official reference-architecture page (one sitting each).
- **Do:** annotate one vendor blueprint: circle every lock-in point and every place your open stack has an equivalent.
- **Done when:** you can translate any vendor diagram into open-component vocabulary live in a meeting.
- Est. hours: 3

#### 11.8.1 Secrets management — T2
- **Why:** pipelines hold credentials to everything; secrets architecture is a prerequisite to the Phase-6 security work and every audit.
- **Learn:** secret stores (Key Vault, OpenBao/Vault) vs env vars vs files; rotation; managed identities as the no-secret ideal; secret injection into K8s (CSI driver) and CI; the Vault→OpenBao licensing fork.
- **Resource:** OpenBao docs (concepts) + Azure Key Vault + managed identities overview.
- **Tools:** FOSS: OpenBao (↔ Azure Key Vault, AWS Secrets Manager) · Corp: Key Vault (primary).
- **Do:** move every credential in the compose/K8s stack out of files into OpenBao; document the rotation runbook.
- **Done when:** `git grep -i password` returns nothing real, and rotation is a 5-minute documented operation.
- Est. hours: 3

#### 12.7.2 Observability stack (OpenTelemetry, Prometheus, Grafana) — T2
- **Why:** logs/metrics/traces with OTel is the CNCF-standard nervous system; data platforms without it are debugged by archaeology.
- **Learn:** three pillars + OTel signals model (traces/metrics/logs, collector, OTLP); Prometheus: scrape model, PromQL basics, alerting rules; Grafana dashboards; Loki for logs; instrumenting a Python pipeline with OTel; SLI/SLO/error-budget vocabulary (deepened in Phase 8 for data SLAs); Azure Monitor/App Insights as the corp mapping (ties to A.5 KQL).
- **Resource:** OpenTelemetry docs (concepts + Python) + Prometheus "Overview"/PromQL basics.
- **Tools:** FOSS: OTel + Prometheus + Grafana + Loki (↔ Azure Monitor, Datadog) · Corp: Datadog/Azure Monitor (evaluation level).
- **Do:** instrument the Dagster→Spark→Iceberg path with OTel traces and pipeline metrics (rows, lag, duration); build the platform-health Grafana dashboard with two alert rules (freshness, consumer lag).
- **Done when:** a seeded failure is diagnosable from the dashboard alone in under five minutes, traces included.
- Est. hours: 8

#### 12.2.2 Disaster-recovery patterns — T1
- **Why:** RTO/RPO design is a DORA-driven architect deliverable; "what happens if the region dies?" now has regulatory teeth in EU financial services.
- **Learn:** RTO/RPO/RCO definitions and how to elicit honest numbers from the business; topology ladder: backup-restore → pilot light → warm standby → active-active, with cost curves; data-layer DR specifics: storage replication (LRS/ZRS/GRS), database geo-replication & failover groups, Kafka cross-cluster (MirrorMaker/Geo-DR), lakehouse DR (re-derivable vs source-of-truth tiers); DR testing discipline (game days, failover drills); region pairs & EU residency constraints.
- **Resource:** Azure Architecture Center DR guidance + WAF reliability pillar (data workload sections).
- **Do:** write the DR design for your platform: tier every store by RPO/RTO class, choose a topology per tier, cost the delta vs single-region, and script one tabletop failover drill.
- **Done when:** you can defend why gold marts get warm standby but bronze gets backup-restore, with numbers.
- Est. hours: 7

#### 12.1.1 Backup & recovery (cloud-native) — T2
- **Why:** backups are the bottom rung of the DR ladder and the part auditors actually test; lakehouse-era backup is mostly *not* file copies.
- **Learn:** Azure Backup model (vaults, policies, soft delete, immutability for ransomware); database PITR windows; object-store versioning + lifecycle as backup; Iceberg snapshot retention vs backup (and why snapshots ≠ backups when the catalog dies); restore testing.
- **Resource:** Azure Backup docs (overview + blob/database sections).
- **Do:** define the backup policy matrix for every store in the platform (what, frequency, retention, immutability, restore test cadence); run one real restore from MinIO versioning.
- **Done when:** you can answer "when did we last *restore* successfully?" with a date, not a shrug.
- Est. hours: 2

#### 12.3.1 FinOps / cloud cost management — T1
- **Why:** explicit mastery bias: cost models decide architectures, and the architect who can't price a design loses the vendor-selection argument to whoever can.
- **Learn:** FinOps lifecycle (inform/optimize/operate) and unit economics (€ per pipeline run, per report, per GB served); Azure pricing mechanics for data: storage tiers, egress, compute SKUs, reservations/savings plans, spot; tagging & cost allocation (showback/chargeback); the big levers: storage-format efficiency, cluster right-sizing, serverless-vs-provisioned crossover, egress avoidance; Azure Cost Management + budgets/alerts; FOCUS billing-data standard (awareness).
- **Resource:** FinOps Foundation framework docs (free) + Azure Cost Management docs; Azure pricing calculator as the lab bench.
- **Tools:** FOSS: OpenCost (K8s cost, awareness) · Corp: Azure Cost Management (primary), Vantage/Cloudability (awareness).
- **Do:** build the full monthly cost model of your target Azure architecture (calculator-based) at 1× and 10× data volume; identify the three biggest levers and re-price after pulling them.
- **Done when:** you can state € per daily NAV pipeline run and defend every line of the model to a CFO.
- Est. hours: 9

#### 12.3.2 Data-specific FinOps — T2
- **Why:** warehouse credits and per-query economics behave differently from VM bills; data FinOps is its own discipline with its own levers.
- **Learn:** Snowflake credit burn anatomy (warehouse size × uptime; auto-suspend discipline); Databricks DBU model & cluster policies; BigQuery on-demand vs capacity; per-query attribution; the query-cost review as a governance practice.
- **Resource:** Snowflake cost-management docs + Databricks cluster-policy docs (read as patterns).
- **Do:** write the "cost guardrails" standard for a warehouse estate: auto-suspend, size caps, query tagging, monthly review ritual.
- **Done when:** you can spot the three classic credit-burn anti-patterns in a usage report.
- Est. hours: 3

#### 3.3.4 Caching — T2
- **Why:** caches (Redis/Valkey) sit in front of every serving layer; the architect mostly decides *whether* and *where*, not *how*.
- **Learn:** cache-aside vs read/write-through; invalidation & TTL discipline; what to cache in a data platform (API responses, semantic-layer results, feature lookups); Valkey/Redis licensing fork; Azure Cache for Redis.
- **Resource:** Azure Architecture Center caching guidance page.
- **Do:** decide cache placement for the Phase-8 data API (yes/no, where, TTL) and write the 10-line justification.
- **Done when:** you can articulate the staleness-vs-load tradeoff for fund NAV data specifically (hint: NAVs are daily — cache hard).
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 2.2.1 | Log/metric shippers | Fluent Bit/Vector agents feeding observability pipelines | Vector docs "concepts" | 20 |
| 2.5.1 | iPaaS | Workato/Boomi/Power Automate business-user integration | Power Automate overview | 20 |
| 2.5.2 | ESB (legacy) | Central-bus integration era (TIBCO/IBM); what you'll be strangling | one architecture-blog ESB retrospective | 20 |
| 3.2.7 | Time-series databases | Prometheus/InfluxDB/kdb+ (kdb+ = market-data niche) | InfluxDB "what is time series" page | 20 |
| 3.3.2 | Block storage | VM disks (Azure Managed Disks); database substrate | Azure Disks overview | 15 |
| 3.3.3 | File storage | NFS/SMB shares (Azure Files); legacy app integration | Azure Files overview | 15 |
| 5.1.1 | Visual ETL suites | Informatica/SSIS/DataStage — the installed base in EU FS | Informatica PowerCenter product page | 25 |
| 9.10.3 | Configuration management | Ansible/Chef VM-era config; mostly displaced by containers | Ansible "how it works" | 20 |
| 12.1.2 | Enterprise backup suites | Veeam/Commvault/Rubrik estates in on-prem banks | Veeam product overview | 15 |
| 12.2.1 | DR tooling | Azure Site Recovery/Zerto orchestrated failover | ASR overview | 20 |
| 12.5.1 | On-call/paging | PagerDuty/Opsgenie rotations & escalation | PagerDuty "what is on-call" | 15 |
| 12.5.2 | Postmortems | Blameless incident review practice | Google SRE book postmortem chapter (free online) | 30 |
| 12.6.1 | Capacity planning | Forecasting growth vs provisioning | Google SRE book capacity chapter intro | 20 |
| 12.7.1 | Commercial APM | Datadog/Dynatrace full-stack suites | Datadog product tour | 15 |
| 14.7.3 | Notification tools | Paging/chat alert routing from data signals | Grafana alerting → contact points docs | 10 |

*T3 subtotal: 4.5 h*

### Capstone 5 — IaC-provisioned platform on Kubernetes + Well-Architected review

- **Goal:** the platform becomes infrastructure-as-code on a cloud-shaped runtime, with observability, a DR position, and a cost model — everything an architecture review board would demand.
- **Stack (100% free):** kind or k3d local Kubernetes (↔ AKS), Helm charts for Kafka/Flink/Trino/Dagster/MinIO/Postgres (↔ managed PaaS equivalents), OpenTofu with kubernetes/helm/azurerm providers (↔ Terraform Enterprise), Bicep comparison module, OpenBao (↔ Key Vault), OTel + Prometheus + Grafana + Loki (↔ Azure Monitor), Azure pricing calculator + free-trial `tofu plan` (no spend).
- **Build:** (1) migrate the compose stack to kind via Helm, OpenTofu-managed end to end; (2) secrets via OpenBao with documented rotation; (3) full observability: traces through one pipeline run, platform dashboard, two alerts; (4) azurerm module expressing the target Azure architecture (landing-zone slice: VNet/Private Link per A.3, ADLS, AKS, Event Hubs, Key Vault) — validated plan-only; (5) WAF review of the result (one finding per pillar, remediated or accepted in writing); (6) DR design + tabletop drill; (7) monthly cost model at 1×/10×.
- **Architecture deliverables:** C4 deployment diagram (new level for this phase); ADR-013 Kubernetes vs managed-PaaS-per-service, ADR-014 OpenTofu vs Bicep for this estate, ADR-015 DR topology per data tier.
- **Acceptance criteria:** fresh machine → `tofu apply` → healthy platform → one full pipeline run → `tofu destroy`, all documented; seeded failure diagnosed from dashboards in <5 min; WAF review yields ≥5 genuine findings with dispositions; cost model withstands a "what if volumes 10×?" challenge; DR drill writeup names RTO/RPO per tier.
- Est. hours: 18

*Phase 5 total: 107.5 h (T1/T2 entries 85 h + T3 4.5 h + capstone 18 h) + Appendix A items A.3–A.6, A.22, A.25, A.26 (37 h) scheduled in this phase*


<a id="phase-6"></a>
## Phase 6: Governance, Security & Compliance (months 34–39, 120 h + 14 h Appendix A)

**Goal:** build the control plane of a regulated data platform: catalog + lineage as the metadata backbone, data quality as an engineering discipline, MDM/RDM for the entities the fund industry lives on, fine-grained access control and masking, and the regulatory frameworks (GDPR, DORA, DCAM) that decide what "good" means in Luxembourg.
**Entry prerequisites:** Phases 2–5 (a platform worth governing; OTel/observability foundations).
**Exit criteria:** you can (1) stand up a catalog with end-to-end lineage and answer an impact-analysis question from it; (2) design a DQ framework from profiling to alerting with rules tied to the six dimensions; (3) design a security-master MDM with match/merge and survivorship; (4) implement RLS/CLS and policy-as-code on the lakehouse; (5) map your platform to GDPR/DORA obligations and lead a DCAM self-assessment.
**Appendix A items scheduled here:** A.14 data strategy & operating model, A.15 architecture risk management, A.16 data risk & controls, A.17 ethics, A.18 purpose-based sharing, A.19 records management, A.20 organizational change management (14 h).

### T1/T2 topics

#### 10.1.1 Metadata management & active catalogs — T1
- **Why:** governance-and-lineage is an explicit mastery bias: the catalog is the control plane — ownership, glossary, lineage, quality, and policy all hang off it.
- **Learn:** metadata kinds (technical/business/operational) and active vs passive metadata; OpenMetadata architecture (ingestion framework, connectors, APIs); entity model: domains, owners, tiers, glossary links; automated ingestion from Postgres/Trino/dbt/Kafka/Dagster; catalog-driven workflows (announcements, tasks, approval flows); DataHub as the alternative (event-sourced metadata, also OpenLineage-friendly); what makes metadata "active" (policies and alerts firing *from* metadata).
- **Resource:** OpenMetadata official docs (concepts + ingestion) . *Alternate:* DataHub docs (architecture).
- **Tools:** FOSS: OpenMetadata (↔ Microsoft Purview, Collibra, Alation) · Corp: Purview (Azure default) + Collibra (EU FS incumbent) at evaluation level.
- **Do:** deploy OpenMetadata; ingest Postgres, Trino/Iceberg, dbt, and Kafka metadata; assign owners/tiers to every gold asset; wire one active workflow (schema-change announcement to consumers).
- **Done when:** "who owns this, who consumes it, what breaks if I change it?" is answerable from the catalog in under two minutes.
- Est. hours: 10

#### 10.3.1 Data lineage (OpenLineage standard) — T1
- **Why:** BCBS-239-grade traceability — every regulatory number must walk back to its sources; lineage is also the architect's impact-analysis weapon.
- **Learn:** OpenLineage spec: runs/jobs/datasets, facets; emitters: Dagster, Spark, dbt integrations; Marquez as reference backend; column-level vs table-level lineage (what dbt/SQL parsing gives vs what Spark gives); lineage into the catalog (OpenMetadata/DataHub ingestion); designing for lineage (naming, job granularity); limits — lineage of black-box SaaS steps.
- **Resource:** OpenLineage docs (spec + integrations) + Marquez getting-started.
- **Tools:** FOSS: OpenLineage + Marquez, surfaced in OpenMetadata (↔ Purview lineage, Collibra lineage, Manta) · Corp: Purview/Collibra lineage (evaluation level).
- **Do:** emit OpenLineage events from Dagster and dbt for the full NAV path (Postgres → Debezium → Iceberg → Spark → dbt → EMT output); render end-to-end lineage and answer one impact query ("which reports break if `orders.amount` changes?") from it.
- **Done when:** the EMT output's lineage back to source tables is demonstrable to an auditor, column-level where the tooling allows.
- Est. hours: 7

#### 9.4.2 + 10.4.1 Data quality engineering (Great Expectations / Soda) — T1
- **Why:** non-negotiable in regulated data: DQ rules are how "accuracy, completeness, timeliness" stop being audit prose and start being code.
- **Learn:** the six DQ dimensions mapped to executable rule types; Great Expectations: suites, checkpoints, data docs; Soda Core: SodaCL checks, scan integration in orchestration; dbt tests vs dedicated DQ frameworks (layering, not either/or); severity & circuit-breaking (block publish vs warn — ties to your WAP gates); DQ result routing to catalog/alerts; writing rules from profiling output, not imagination.
- **Resource:** *Data Quality Fundamentals* (Moses et al.) ch. 1–4 + Soda Core docs (SodaCL).
- **Tools:** FOSS: Soda Core + Great Expectations + dbt tests (↔ Informatica DQ, Talend DQ) · Corp: Informatica DQ (EU FS incumbent; evaluation level).
- **Do:** define the DQ rulebook for the NAV pipeline: per dataset, rules across all six dimensions with severities; wire Soda scans into the WAP gate so criticals block publish and warnings page the catalog.
- **Done when:** a seeded completeness failure blocks publish, appears in the catalog, and pages with a link to the failing expectation — and you can justify every rule's dimension and severity.
- Est. hours: 10

#### 10.4.3 Data profiling — T2
- **Why:** profiling is the evidence-gathering step before DQ rules — discover distributions, cardinalities, and surprises rather than assuming them.
- **Learn:** profiling outputs (distributions, nulls, uniqueness, patterns, drift over time); ydata-profiling for one-shot EDA; whylogs for continuous statistical profiles; profiling as DQ-rule generator; PII discovery overlap (ties to 11.4.1).
- **Resource:** ydata-profiling docs + whylogs concepts page.
- **Tools:** FOSS: ydata-profiling, whylogs (↔ Informatica/Collibra profiling modules).
- **Do:** profile the silver holdings table; turn the five most surprising findings into Soda rules; schedule a weekly whylogs profile and diff alert.
- **Done when:** at least three of your DQ rules exist *because* profiling falsified an assumption.
- Est. hours: 3

#### 10.4.2 Managed data observability platforms — T2
- **Why:** Monte Carlo-class tools are the buy side of the DQ build-vs-buy; their ML-anomaly pitch needs informed evaluation.
- **Learn:** anomaly-detection-on-metadata model (freshness/volume/schema drift without rules); incident workflow & lineage-aware blast radius; pricing models; where rule-based and anomaly-based DQ complement each other.
- **Resource:** Monte Carlo docs/architecture overview (vendor source, read critically).
- **Do:** half-page build-vs-buy: your Soda+Elementary stack vs Monte Carlo for a 200-pipeline estate.
- **Done when:** you can state which failure classes anomaly detection catches that your rules never will, and vice versa.
- Est. hours: 2

#### 10.9.1 + 10.9.2 Data observability (pipeline health) — T2
- **Why:** freshness/volume/schema-drift monitoring is the data plane's heartbeat — distinct from infra observability (Phase 5) and from DQ rules (above).
- **Learn:** the five data-observability pillars (freshness, volume, schema, distribution, lineage); Elementary as dbt-native observability (anomaly tests, report UI); wiring data incidents into the same alerting path as infra; data incident triage runbook.
- **Resource:** Elementary docs + *Data Quality Fundamentals* ch. on observability pillars.
- **Tools:** FOSS: Elementary + OpenLineage events (↔ Monte Carlo, Databand, Bigeye).
- **Do:** add Elementary to the dbt project; enable volume/freshness anomaly tests on gold; route one synthetic incident through Grafana alerting with a runbook link.
- **Done when:** silent-failure classes (stale, shrunken, schema-drifted) each have a detector and an owner.
- Est. hours: 3

#### 10.5.1 Master data management — T1
- **Why:** the security/fund/counterparty master *is* the fund-industry data problem — every NAV error story ends at reference data; the architect designs the master, even when the tool is bought.
- **Learn:** MDM styles (registry, consolidation, coexistence, centralized) and their org costs; match/merge: deterministic vs probabilistic (Fellegi–Sunter intuition), blocking, thresholds; survivorship rules and golden-record assembly; hierarchy management (fund → sub-fund → share class; issuer trees); stewardship workflow (review queues); integration patterns (MDM as publisher to the platform); security-master specifics: identifier cascade (ISIN/FIGI/internal), vendor-feed precedence (Bloomberg vs Refinitiv), corporate-action survivorship.
- **Resource:** DAMA-DMBOK ch. 10 (Reference & Master Data) + Splink documentation (probabilistic linkage, MoJ open source).
- **Tools:** FOSS: Splink for match/merge + Postgres for the hub (↔ Informatica MDM, Reltio, Semarchy, Tamr) · Corp: Informatica MDM / Semarchy (EU FS shortlist; evaluation level).
- **Do:** build a mini security master: ingest two overlapping "vendor" feeds with conflicting attributes; Splink match/merge with explicit blocking + thresholds; survivorship rules in SQL; publish the golden record + cross-reference table to the lakehouse.
- **Done when:** you can walk a steward through *why* two records merged (match weights) and *why* each golden attribute won (survivorship rule), and defend registry-vs-centralized for a fund administrator.
- Est. hours: 9

#### 10.6.1 Reference data management — T2
- **Why:** code lists (countries, currencies, MICs, fund legal forms, CFI codes) are small data with outsized blast radius; RDM is governance's unglamorous core.
- **Learn:** internal vs external reference data; versioning & effective dating of code lists; distribution patterns (publish-subscribe from one source of truth); mapping tables between vendor codes; ISO list maintenance cadence (4217, 3166, 10383 MIC); ties back to SCD2 discipline from Phase 1.
- **Resource:** DAMA-DMBOK ch. 10 (reference-data half) + Collibra RDM product docs (as the corp pattern).
- **Tools:** FOSS: dbt seeds + a governed Postgres schema (↔ Collibra RDM, CluedIn).
- **Do:** build the governed code-list schema (effective-dated, approved-by, source) for currencies/countries/MICs; wire one mapping table (vendor country codes → ISO) into the silver layer.
- **Done when:** a code-list change is traceable (who/when/why) and consumed everywhere from one place.
- Est. hours: 3

#### 7.3.1 Business glossary — T2
- **Why:** "NAV", "AUM", "dealing date" mean different things across teams until the glossary pins them; glossary-to-asset linkage is what makes catalogs business-readable.
- **Learn:** term lifecycle (draft → approved, owners, stewards); term-to-asset linkage; glossary vs data dictionary vs semantic layer (and the coming convergence); seeding from regulation (AIFMD/PRIIPs definitions) vs from analytics.
- **Resource:** OpenMetadata glossary docs + DAMA-DMBOK ch. 13 (metadata, glossary sections).
- **Tools:** FOSS: OpenMetadata glossary (↔ Collibra, Purview glossary).
- **Do:** create a 25-term fund glossary (NAV, swing price, AUM, dealing cut-off, …) with owners; link every gold table column that carries one of those terms.
- **Done when:** clicking "NAV" in the catalog shows its definition, its owner, and every asset that carries it.
- Est. hours: 3

#### 1.12.6 + 3.2.6 FIBO & knowledge graphs / RDF — T2
- **Why:** FIBO is the finance ontology (EDM Council) and RDF/SPARQL is its native stack; semantic master data is a real pattern in EU regulators and large institutions.
- **Learn:** RDF triples, RDFS/OWL basics, SPARQL reading fluency; SHACL validation idea; FIBO's structure (domains: securities, funds, legal entities) and pragmatic use (vocabulary + relationships source, not a deployment mandate); property graphs vs RDF (when each); GLEIF Level-2 as a ready-made entity graph.
- **Resource:** FIBO primer at spec.edmcouncil.org + Apache Jena tutorial (RDF/SPARQL basics).
- **Tools:** FOSS: Apache Jena/Fuseki (↔ Stardog, Ontotext GraphDB, Neptune).
- **Do:** load GLEIF Level-2 ownership for 50 entities into Fuseki; SPARQL the ultimate-parent chains; map five of your security-master attributes to FIBO terms.
- **Done when:** you can say where FIBO genuinely helps (shared vocabulary, entity relationships) and where it's academic for your estate.
- Est. hours: 4

#### 11.1.2 Fine-grained access control (RLS/CLS on the platform) — T1
- **Why:** "who may see which fund's data at which column grain" is a regulatory requirement you must design *and prove* — Chinese walls between sub-funds and clients are access-control problems.
- **Learn:** RBAC→ABAC→ReBAC ladder and where each fits data; row-level security mechanics (Postgres RLS policies; warehouse equivalents) and their performance/leak caveats; column-level security & masking interplay; lakehouse access control reality (Trino/engine-level vs catalog-level enforcement; Ranger/Lake Formation/Unity models — who actually enforces at the file layer); attribute sources (Entra groups, catalog tags); access request/review workflows (recertification — an audit staple).
- **Resource:** Postgres RLS docs + Trino security docs + Unity Catalog privilege model docs (read as three enforcement archetypes).
- **Tools:** FOSS: Postgres RLS + Trino with file-based/OPA rules (↔ Immuta, Privacera, Unity Catalog, Lake Formation) · Corp: Immuta + Purview policies (evaluation level).
- **Do:** implement "TA agents see only their management company's funds" as Postgres RLS *and* as Trino rules over Iceberg; tag PII columns in the catalog and enforce CLS for a restricted role; write the recertification procedure.
- **Done when:** you can demonstrate the same policy at two enforcement layers, name where each can be bypassed, and explain the residual risk in writing.
- Est. hours: 7

#### 11.1.3 Policy-as-code (OPA) — T2
- **Why:** externalized, testable authorization is the modern answer to policy sprawl; OPA/Rego is its lingua franca and shows up across the platform (APIs, K8s, data).
- **Learn:** OPA architecture (PDP/PEP separation); Rego basics (rules, data documents); policy testing; bundles & distribution; Trino-OPA integration; Cedar as the typed alternative; where policy-as-code beats per-system grants (consistency, auditability, CI for policies).
- **Resource:** OPA docs ("Policy language" + "Philosophy") .
- **Tools:** FOSS: OPA (↔ Immuta policies, Apache Ranger, Cedar/AVP).
- **Do:** express the fund-visibility policy from 11.1.2 in Rego with unit tests; enforce it for Trino via the OPA plugin; change the policy in git and watch enforcement follow.
- **Done when:** a policy change is a reviewed PR with passing policy tests — not a ticket to three different admins.
- Est. hours: 3

#### 11.1.1 Identity providers & SSO — T2
- **Why:** every access decision starts with identity; the architect wires platforms into the IdP and reads OIDC/SAML flows fluently.
- **Learn:** OIDC flows (auth code + PKCE, client credentials for services) vs SAML; tokens (ID/access/refresh, claims, audiences); groups-to-roles mapping into data tools; SCIM provisioning; managed identities recap; Keycloak realm/client model.
- **Resource:** Keycloak docs (getting started + OIDC) + OIDC spec overview (openid.net primer).
- **Tools:** FOSS: Keycloak (↔ Entra ID, Okta) · Corp: Entra ID (primary).
- **Do:** put Keycloak in front of OpenMetadata, Grafana, and Trino (OIDC); map a "data-steward" group claim to in-tool roles.
- **Done when:** one identity, one group change, three tools' permissions move together — and you can narrate the token flow.
- Est. hours: 3

#### 11.2.1 Encryption & key management — T2
- **Why:** "who controls the keys" is the question behind every cloud-data compliance review (and the Schrems-flavored sovereignty debate).
- **Learn:** envelope encryption; KMS hierarchies (key vault → KEK → DEK); customer-managed keys (CMK) vs platform-managed — what CMK actually buys (revocation, audit) and doesn't; TLS everywhere as table stakes; key rotation mechanics; HSM tiers; client-side encryption tradeoffs for analytics (it breaks pushdown).
- **Resource:** Azure Key Vault + storage-encryption docs (CMK sections) .
- **Do:** write the key-management design for the Azure target: which stores get CMK, where keys live, rotation cadence, revocation drill.
- **Done when:** you can answer "if we revoke the key, what actually happens and how fast?" per store.
- Est. hours: 2

#### 11.3.1 + 11.3.2 Data masking & tokenization — T2
- **Why:** masking is how production-shaped data becomes usable in lower environments and how analysts see funds without seeing investors.
- **Learn:** static vs dynamic masking; technique zoo (redaction, substitution, shuffling, format-preserving encryption, tokenization with vault); referential consistency under masking (same investor → same token everywhere); warehouse-native dynamic masking; masking vs synthesis decision (ties to 9.8.1).
- **Resource:** Microsoft dynamic-data-masking docs + a tokenization-pattern overview (Skyflow/Protegrity whitepaper class — read critically).
- **Tools:** FOSS: Postgres views/functions + Presidio transforms (↔ Delphix, Protegrity, Immuta masking).
- **Do:** build the masked replica of the Phase-1 investor tables (deterministic tokenization preserving joins); prove referential integrity holds and reversibility is access-controlled.
- **Done when:** a full pipeline run on masked data produces correct aggregates with zero real PII downstream.
- Est. hours: 3

#### 11.4.1 PII detection & redaction (Presidio) — T2
- **Why:** you can't protect what you haven't found; automated PII discovery feeds classification tags that drive masking and access policy.
- **Learn:** detection approaches (regex/checksums, NER models, context words); Presidio analyzer/anonymizer pipeline; precision-recall tuning for EU identifiers (IBANs, national IDs); scanning at rest (lake) vs in motion; classification tags flowing into the catalog (ties to 10.1.1, A.18).
- **Resource:** Microsoft Presidio docs.
- **Tools:** FOSS: Presidio (↔ Macie, GCP DLP, BigID, Purview classifiers).
- **Do:** scan bronze + a synthetic free-text "client notes" set with Presidio; push findings as catalog tags; tune one recognizer (Luxembourg phone/IBAN) and measure precision change.
- **Done when:** new PII landing in bronze gets discovered, tagged, and policy-covered without a human noticing it first.
- Est. hours: 3

#### 11.6.1 Audit logging & SIEM — T2
- **Why:** "show me who accessed fund X's investor data in March" is a question you must answer from logs designed in advance, not reconstructed in panic.
- **Learn:** audit-event taxonomy for data platforms (access, policy change, export, admin); query-log capture per engine (Postgres pgAudit, Trino event listener); centralization & tamper-evidence (immutability, retention); SIEM role (correlation/alerting — Sentinel/Splunk); KQL ties (A.5); what auditors actually sample.
- **Resource:** pgAudit docs + Microsoft Sentinel overview (architecture page).
- **Tools:** FOSS: pgAudit + Trino event listener + Loki (↔ Splunk, Sentinel, Elastic SIEM).
- **Do:** enable audit capture on Postgres and Trino; ship to Loki with retention + immutability notes; answer one "who touched what when" query end-to-end.
- **Done when:** the March-access question is a five-minute query with a documented chain of custody.
- Est. hours: 2

#### 11.7.1 Regulatory & compliance frameworks (GDPR, DORA, and the fund stack) — T1
- **Why:** in Luxembourg financial services, regulation shapes architecture more than technology does — the architect translates legal obligations into platform controls.
- **Learn:** GDPR for platform builders: lawful basis, minimization, purpose limitation, DSAR/erasure in a lakehouse (delete in Iceberg, backups, event logs!), records of processing, DPIA triggers, processor chains & SCCs; DORA: ICT risk framework, incident reporting timelines, resilience testing, the register of ICT third parties and exit strategies (cloud concentration!); the fund regulatory stack at orientation level: UCITS/AIFMD (incl. Annex IV reporting), MiFID II product governance (→ EMT), PRIIPs (→ EPT/KID), SFDR (ESG data demands); CSSF expectations for cloud outsourcing (notification, audit rights — aligned to EBA/ESMA guidelines); SOC 2 / ISO 27001 as vendor-evidence vocabulary.
- **Resource:** gdpr.eu practitioner guides + the DORA regulation summary on EIOPA/ESMA sites + CSSF cloud-outsourcing circular page (orientation read; verify current circular number at assembly).
- **Tools:** Corp context: OneTrust/Vanta-class compliance platforms (awareness).
- **Do:** build the obligation→control matrix for your platform: 12 concrete obligations (e.g., "DSAR erasure within 30 days", "DORA major-incident report in 4h", "AIFMD Annex IV quarterly") each mapped to an implemented or planned control, with gaps flagged honestly.
- **Done when:** you can brief a compliance officer on how the platform meets each obligation — and where it doesn't yet — without hand-waving; the erasure path through Iceberg + backups + Kafka is concretely designed.
- Est. hours: 9

#### 1.12.12 DCAM (and leading a self-assessment) — T1
- **Why:** DCAM is the financial-services data-management capability model; architects at fund firms are expected to *lead* assessments and turn scores into roadmaps.
- **Learn:** DCAM v3 structure: 8 components, 34 capabilities, scoring on engagement/process/evidence; how assessments run (evidence-based scoring, stakeholder interviews); from scores to a sequenced capability roadmap; DCAM vs DMBOK (assessment model vs body of knowledge) and CDMC as the cloud profile (ties to A.16); what "evidence" means per capability — artifacts you've actually built in this plan.
- **Resource:** EDM Council DCAM v3 overview (framework page) + DAMA-DMBOK ch. 15 (maturity assessment) as the open companion; full DCAM is member-gated — note this in client conversations.
- **Do:** run a DCAM-style self-assessment of your capstone platform across all 8 components: score each with named evidence, then write the 12-month capability roadmap the scores imply.
- **Done when:** every score cites an artifact (catalog, lineage graph, DQ rulebook, ADR…) and the roadmap sequences capabilities by dependency, not vibes.
- Est. hours: 7

#### 9.8.1 Synthetic & test data — T2
- **Why:** privacy-preserving development is a compliance requirement (GDPR minimization) and synthetic data is its engineering answer.
- **Learn:** rule-based fakes (Faker) vs statistically-fitted synthesis (SDV: copulas/CTGAN); fidelity-privacy tradeoff (and membership-inference risk in over-fitted synthesis); referential integrity across synthesized tables; when masking beats synthesis (ties 11.3); evaluating synthetic quality (SDMetrics).
- **Resource:** SDV docs (single + multi-table synthesis).
- **Tools:** FOSS: SDV + Faker (↔ Mostly AI, Tonic, Gretel) · Corp: Mostly AI (EU; evaluation level).
- **Do:** fit SDV to the (masked) investor+orders tables; generate a synthetic dev dataset; compare aggregate fidelity vs the real data and document the privacy argument.
- **Done when:** dev/test environments run on data with a written justification of why it's safe.
- Est. hours: 3

#### 10.1.2 Enterprise catalogs (Purview, Collibra) — T2
- **Why:** the buy side of the catalog decision; Purview is the Azure default and Collibra the EU-FS incumbent — you'll evaluate or inherit one.
- **Learn:** Purview: Data Map scans, classification, glossary, policy ambitions — strengths (M365/Azure integration) and gaps (lineage depth, cost model per scanned asset); Collibra: operating-model strength (workflows, stewardship), implementation weight; catalog TCO realities (connector coverage decides everything); migration/coexistence patterns (open catalog + enterprise catalog).
- **Resource:** Purview docs (Data Map + governance overview) + Collibra resource library (architecture overview).
- **Do:** write the catalog vendor-selection memo: OpenMetadata vs Purview vs Collibra for a 300-person fund administrator — connector coverage table, TCO sketch, recommendation.
- **Done when:** the memo names the deciding factor (it's almost always connector coverage + stewardship workflow, not features).
- Est. hours: 3

#### 10.7.1 Retention & lifecycle — T2
- **Why:** regulated retention (10-year fund records) and GDPR minimization pull opposite directions; lifecycle design is where they reconcile.
- **Learn:** retention-schedule design by record class (ties A.19); storage-tier lifecycle (hot→cool→archive economics); legal hold vs deletion pipelines; Iceberg snapshot expiry vs business retention (different layers!); deletion that actually deletes (compaction, backups, logs).
- **Resource:** Azure Blob lifecycle-management docs + Iceberg `expire_snapshots` docs.
- **Do:** write the retention schedule for five record classes (orders, NAV, investor KYC, logs, EMT outputs) and implement it as MinIO lifecycle + Iceberg maintenance jobs.
- **Done when:** "when does this data actually disappear, everywhere?" has a per-class answer you can prove.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 3.2.5 | Property graph databases | Neo4j/Cypher for relationship-heavy ops use (fraud, ownership) | Neo4j "what is a graph DB" page | 25 |
| 7.3.2 | Glossary embedded in catalogs | Same discipline as 7.3.1, as a feature of Collibra/Purview | covered by 10.1.2 reading | 10 |
| 9.8.2 | Test data management | Subset/mask/refresh tooling (Delphix-class) for legacy estates | Delphix TDM overview | 20 |
| 10.2.1 | AI-native data discovery | LLM-assisted search/Q&A over catalog metadata | Atlan AI or DataHub smart-search blog | 20 |
| 10.2.2 | Catalog-embedded discovery | Search/browse UX as a catalog feature | covered by 10.1.1 hands-on | 10 |
| 10.3.2 | Lineage embedded in catalogs | Lineage as a catalog feature vs the open standard | covered by 10.1.1/10.3.1 | 10 |
| 10.5.2 | Modern/cloud MDM | ML-first MDM (Tamr) and lighter cloud MDM (Reltio) | Tamr product overview | 20 |
| 10.6.2 | RDM inside MDM suites | Code-list management bundled in MDM products | covered by 10.6.1 reading | 10 |
| 10.7.2 | Enterprise ILM suites | Heavyweight lifecycle tooling (Veritas/IBM) in legacy estates | Veritas ILM overview | 15 |
| 11.2.2 | Database encryption / TDE | At-rest encryption inside engines; table stakes, rarely a decision | SQL Server TDE docs intro | 20 |
| 11.5.1 | Privacy/consent platforms | OneTrust-class consent, DSAR automation | OneTrust product overview | 20 |
| 14.7.1 | Anomaly alerting | DQ/observability-triggered alerting; implemented via Elementary above | covered by 10.9.x hands-on | 10 |

*T3 subtotal: 3 h*

### Capstone 6 — The governed platform (catalog, lineage, DQ, policy, DCAM)

- **Goal:** wrap the entire platform in a working control plane and prove it to an imaginary auditor: every asset owned and classified, every number traceable, every access decision policy-driven, every obligation mapped.
- **Stack (100% free):** OpenMetadata (↔ Purview/Collibra), OpenLineage + Marquez (↔ Purview/Manta lineage), Soda Core + Great Expectations + Elementary (↔ Informatica DQ / Monte Carlo), Splink + Postgres security master (↔ Informatica MDM / Semarchy), Keycloak (↔ Entra ID), OPA + Trino rules + Postgres RLS (↔ Immuta/Privacera), Presidio (↔ Macie/Purview classifiers), pgAudit + Loki (↔ Sentinel/Splunk), SDV (↔ Mostly AI), Apache Jena/Fuseki FIBO/GLEIF slice (↔ Stardog/GraphDB).
- **Build:** (1) catalog ingests every platform component; owners/tiers/classifications complete for gold; (2) end-to-end lineage for the EMT path, demonstrable; (3) DQ rulebook live in the WAP gate + Elementary anomaly watch; (4) security master publishing golden records with steward-explainable merges; (5) fund-visibility policy enforced via RLS + OPA-Trino from one Rego source, identities from Keycloak; (6) PII auto-discovered → tagged → masked replica for dev; (7) audit trail answering the "March access" question; (8) the obligation→control matrix (11.7.1) and the DCAM self-assessment + roadmap (1.12.12) as governing documents.
- **Architecture deliverables:** C4 updated with the control plane; ADR-016 catalog selection (open vs Purview vs Collibra), ADR-017 enforcement architecture (where policy is decided vs enforced, and residual bypass risk), ADR-018 MDM style for the security master (registry vs centralized).
- **Acceptance criteria:** the auditor drill passes: pick any number in the EMT output → lineage to sources, owner, DQ status, access policy, and audit log, each in minutes; a seeded DQ failure blocks publish and reaches the catalog; the same policy change propagates to both enforcement layers via one PR; DCAM scores all cite artifacts; obligation matrix has zero unexamined rows (gaps allowed, but named).
- Est. hours: 16

*Phase 6 total: 120 h (T1/T2 entries 101 h + T3 3 h + capstone 16 h) + Appendix A items A.14–A.20 (14 h) scheduled in this phase*


<a id="phase-7"></a>
## Phase 7: AI/ML & LLM Platforms for Fund Data (months 40–43, 74 h + 7 h Appendix A)

**Goal:** working-level command of the ML/LLM platform stack from the *data architect's* seat: the lifecycle (MLflow), feature serving, vector storage, RAG over fund documents, and — critically for regulated use — evaluation and tracing. Depth is deliberately T2/T3: you architect the platform ML teams run on; you don't compete with them on modeling.
**Entry prerequisites:** Phases 2–6 (lakehouse, orchestration, governance — ML platforms inherit all of it). No ML-theory prerequisite: this phase targets platform-architecture depth, not modeling depth — the entries stay at the intuition level, and each resource is self-contained.
**Exit criteria:** you can (1) design the MLOps lifecycle on your platform with registry, tracking, and promotion gates; (2) choose vector storage and defend hybrid search for RAG; (3) build and *evaluate* an LLM extraction pipeline over fund documents; (4) tell a CIO what LLMOps controls a regulated deployment needs (traces, evals, human gates) and show them running.
**Appendix A items scheduled here:** A.21 LLM agent patterns & prompt engineering, A.23 Model Context Protocol, A.24 LLM application security (7 h).

### T1/T2 topics

#### 6.4.1 MLOps platforms & the ML lifecycle (MLflow) — T2
- **Why:** the registry/tracking/promotion lifecycle is the governance pattern of ML — and the architect owns how it plugs into the data platform, lineage, and audit.
- **Learn:** ML system anatomy (Huyen's framing): data → features → training → registry → serving → monitoring, and where each touches *your* platform; MLflow: tracking (runs/params/metrics), model registry (stages/aliases, approvals), packaging; experiment tracking as audit trail (6.7.1 lives here); drift concepts (data/concept) and retraining triggers; model risk management vocabulary for finance (SR 11-7/ECB TRIM awareness — models need inventories and owners too).
- **Resource:** Chip Huyen, *Designing Machine Learning Systems* ch. 1–2, 7–9 (skim the deep-modeling middle) + MLflow docs (tracking + registry).
- **Tools:** FOSS: MLflow (↔ Azure ML registry, SageMaker, W&B) · Corp: Azure ML (evaluation level, next entry).
- **Do:** stand up MLflow on the platform; track a small fund-flow forecasting experiment (sklearn, a few runs); register the winner and define a written promotion gate (eval threshold + human approval) from Staging→Production.
- **Done when:** "which model version produced this number, trained on what data, approved by whom?" is answerable from the registry — the model-governance analogue of your lineage drill.
- Est. hours: 10

#### 6.4.2 Managed MLOps (Azure ML) — T2
- **Why:** Azure ML is what your employer likely already licenses; you must map open concepts onto it for build-vs-buy and audit conversations.
- **Learn:** workspaces, compute targets, environments; pipelines vs your Dagster (overlap and friction); model registry + endpoints; responsible-AI dashboard positioning; cost profile; where Azure ML adds value over OSS-on-AKS (managed endpoints, RBAC integration) and where it constrains.
- **Resource:** Azure ML documentation (concepts section).
- **Do:** map every Capstone-7 component to its Azure ML equivalent in a one-page table with a build-vs-buy verdict per row.
- **Done when:** you can brief a platform team on what changes (and what doesn't) if they adopt Azure ML.
- Est. hours: 4

#### 6.1.1 Feature stores (Feast) — T2
- **Why:** the online/offline consistency problem is the architecturally interesting part of ML serving — and feature stores are a frequent (often premature) vendor pitch you must evaluate.
- **Learn:** offline vs online stores; point-in-time-correct joins (the training-serving skew killer — your SCD2 instincts apply directly); feature definitions as code; materialization; when a feature store is overkill (batch-only scoring — most fund use cases!).
- **Resource:** Feast docs (concepts + point-in-time joins).
- **Tools:** FOSS: Feast on Postgres/Redis (↔ Databricks/Tecton/SageMaker feature stores).
- **Do:** define three fund features (30-day flow volatility, investor churn signal, NAV staleness) in Feast over your lakehouse; demonstrate a point-in-time-correct training set vs a naive (leaky) join.
- **Done when:** you can show concretely how the naive join leaks future data, and state when you'd veto a feature-store purchase.
- Est. hours: 5

#### 1.1.4 + 3.2.9 Vector data & vector storage — T2
- **Why:** embeddings are a new first-class data type in your storage portfolio; the "dedicated vector DB vs pgvector vs search-engine hybrid" decision is today's recurring architecture question.
- **Learn:** embeddings as learned features; ANN indexing (HNSW intuition, IVF; recall-latency-memory triangle); pgvector (indexes, filtering) vs dedicated stores (Qdrant/Milvus) vs hybrid engines (the convergence note from the taxonomy: keyword+vector reranked is the RAG default); metadata filtering at scale; vector data lifecycle (re-embedding on model change — a lineage problem!).
- **Resource:** pgvector README + Qdrant docs (concepts: indexing, filtering, hybrid).
- **Tools:** FOSS: pgvector + Qdrant (↔ Azure AI Search vectors, Pinecone) .
- **Do:** embed 1k fund-document chunks; benchmark pgvector vs Qdrant on filtered top-k (latency/recall vs exact); write the 10-line "when does Postgres suffice" verdict.
- **Done when:** you can defend "pgvector until proven otherwise" — or its rejection — with your own numbers.
- Est. hours: 7

#### 6.6.1 Embedding models — T2
- **Why:** embedding choice quietly determines retrieval quality, cost, and re-indexing burden — an architect decision dressed as a detail.
- **Learn:** sentence-transformers locally vs API embeddings (cost/latency/sovereignty — EU data residency applies to embeddings too!); dimensionality tradeoffs; domain fit for financial text; versioning embeddings (model change = full re-index = pipeline design issue); MTEB as a (gameable) benchmark.
- **Resource:** sentence-transformers docs (+ MTEB leaderboard, read skeptically).
- **Tools:** FOSS: sentence-transformers (↔ OpenAI/Cohere/Voyage embedding APIs, Azure OpenAI embeddings).
- **Do:** compare a local multilingual model vs one API model on 20 fund-domain retrieval queries (French/English mix — Luxembourg reality); tabulate quality/cost/residency.
- **Done when:** your pick comes with a stated re-embedding strategy and a data-residency position.
- Est. hours: 4

#### 6.6.2 RAG frameworks & architecture — T2
- **Why:** RAG is the dominant enterprise LLM pattern and a *data architecture* problem at heart: ingestion, chunking, indexing, retrieval, and freshness are your home turf.
- **Learn:** RAG anatomy: load → chunk (strategies and their failure modes on structured PDFs like KIDs) → embed → index → retrieve (hybrid + rerank) → generate with citations; LlamaIndex vs Haystack vs LangChain positioning (and framework-fatigue caution — thin frameworks, strong pipelines); structured extraction with schema-constrained output (the capstone pattern); document parsing reality (tables in PDFs are where RAG dies); freshness pipeline (document updates → re-index, via your orchestrator).
- **Resource:** LlamaIndex docs (RAG concepts + structured extraction). *Alternate:* *Building LLMs for Production* (RAG chapters).
- **Tools:** FOSS: LlamaIndex + Ollama for local models (↔ Azure OpenAI + AI Search, Bedrock KBs).
- **Do:** build retrieval over 30 public fund KIDs/prospectuses (PDF parsing, chunking experiments, hybrid retrieval with citations); measure retrieval hit-rate on 20 hand-written questions before any generation.
- **Done when:** you can show retrieval quality numbers (not vibes) and explain which chunking decision moved them most.
- Est. hours: 10

#### 6.6.3 Managed RAG platforms — T2
- **Why:** "just use Azure AI Search + OpenAI" is the default corp pitch; you need its real capability/cost envelope versus your open pipeline.
- **Learn:** Azure AI Search: hybrid + semantic ranker, integrated vectorization, security trimming (ACL-aware retrieval — the enterprise killer feature); pricing tiers; Bedrock KB / Vertex Search equivalents at a glance; what managed buys (ops, security integration) vs costs (lock-in, chunking opacity).
- **Resource:** Azure AI Search docs (vector + semantic ranking overview).
- **Do:** one-page eval: your open RAG stack vs Azure AI Search for the fund-document corpus, including the ACL-trimming requirement.
- **Done when:** you can name the one requirement (usually security trimming or ops) that flips the decision either way.
- Est. hours: 3

#### 6.8.1 LLM tracing & prompt management (Langfuse) — T2
- **Why:** regulated LLM use without traces is unauditable; prompt/version/trace capture is the LLMOps analogue of your lineage work.
- **Learn:** trace model (traces/spans/generations); prompt versioning & rollout; cost/latency telemetry per call; PII handling in traces (don't log what you masked elsewhere!); user feedback capture as eval input.
- **Resource:** Langfuse docs (tracing + prompt management).
- **Tools:** FOSS: Langfuse self-hosted (↔ LangSmith, Azure AI Foundry tracing).
- **Do:** instrument the RAG pipeline with Langfuse; version one prompt change and compare cost/quality across versions from the traces.
- **Done when:** "what exactly did the model see and answer for document X last Tuesday?" is a lookup, not a mystery.
- Est. hours: 4

#### 6.8.2 LLM evaluation (Ragas, golden sets) — T2
- **Why:** evaluation is the control that makes LLM extraction defensible in a regulated workflow — without it you have a demo, not a system.
- **Learn:** eval layers: retrieval metrics (precision/recall@k), generation metrics (faithfulness, answer relevancy — Ragas), and *task* metrics (field-level extraction accuracy vs golden set — the one that matters here); LLM-as-judge caveats (bias, drift, cost); building golden datasets (your BA skills, weaponized); eval-in-CI: regression gates for prompt/model changes; human-in-the-loop sampling design.
- **Resource:** Ragas docs (metrics + testset) + DeepEval docs (CI integration page).
- **Tools:** FOSS: Ragas/DeepEval + pytest (↔ Azure AI evaluation SDK, LangSmith evals).
- **Do:** hand-build a 50-field golden set from 10 KIDs (SRI, costs, ISIN…); wire field-accuracy + faithfulness evals into CI so a prompt change that drops accuracy below threshold fails the build.
- **Done when:** a deliberately degraded prompt is caught by CI before a human would have noticed — and you can explain each metric's blind spot.
- Est. hours: 6

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 3.2.8 | Search engines | Inverted-index/BM25 stores (Elasticsearch/OpenSearch); the keyword half of hybrid RAG | OpenSearch "intro to search" docs | 30 |
| 6.1.2 | Managed feature stores | Tecton/Databricks/SageMaker FS — buy-side of 6.1.1 | Tecton "what is a feature store" page | 20 |
| 6.2.1 | Training frameworks | PyTorch/sklearn/XGBoost — the ML team's tools; you read, not write | sklearn user-guide landing page | 25 |
| 6.2.2 | Distributed training | Multi-GPU/node training (DeepSpeed/Ray Train); HPC-adjacent, out of role | Ray Train overview | 15 |
| 6.2.3 | Managed training | Azure ML/SageMaker training jobs; covered conceptually in 6.4.2 | Azure ML training docs intro | 15 |
| 6.3.1 | OS model serving | KServe/BentoML/vLLM serving infra; platform-team territory | BentoML "what is model serving" | 20 |
| 6.3.2 | Managed inference endpoints | Pay-per-call hosted inference; procurement awareness | Azure ML endpoints overview | 15 |
| 6.7.1 | OS experiment tracking | MLflow tracking — already hands-on in 6.4.1 | covered there | 5 |
| 6.7.2 | Managed experiment tracking | W&B/Neptune collaboration features | W&B product page | 10 |

*T3 subtotal: 2.5 h*

### Capstone 7 — LLM extraction of fund documents (RAG + eval harness)

- **Goal:** a regulated-grade LLM document pipeline: public fund documents in, schema-valid structured data out, with retrieval metrics, field-accuracy evals, full traces, and human gates — feeding the governed lakehouse like any other source.
- **Stack (100% free):** Ollama with a local open-weights model (↔ Azure OpenAI), LlamaIndex (↔ Azure AI Foundry / Bedrock KBs), pgvector + Qdrant comparison (↔ Azure AI Search), sentence-transformers (↔ Azure OpenAI embeddings), Langfuse (↔ LangSmith), Ragas/DeepEval in CI (↔ Azure AI evals), MLflow registry for prompt+model versions, Dagster orchestrating ingest/re-index, outputs into Iceberg with Soda DQ checks + OpenLineage lineage (the Phase-6 control plane applies unchanged).
- **Build:** (1) corpus: 30+ public KIDs/prospectuses (EN/FR); (2) parsing + chunking tuned on tables; (3) hybrid retrieval with citations; (4) schema-constrained extraction into an EMT/EPT-shaped record (Pydantic-validated); (5) golden-set evals (field accuracy + faithfulness) gating CI; (6) Langfuse traces end-to-end, PII-safe; (7) low-confidence extractions routed to a human-review queue (simple Streamlit screen); (8) results land in silver with DQ checks; lineage shows document → field.
- **Architecture deliverables:** C4 update (AI subsystem); ADR-019 local vs API models (cost/quality/residency), ADR-020 vector-store choice (with your benchmark), ADR-021 human-in-the-loop design (confidence thresholds, sampling, accountability).
- **Acceptance criteria:** field-level accuracy ≥ target on the held-out golden set with the number stated honestly; every extracted value traces to a source span (citation) and a trace ID; a degraded prompt fails CI; sub-threshold extractions reach the review queue with full context; the whole run is reproducible offline (no paid APIs).
- Est. hours: 18

*Phase 7 total: 74 h (T1/T2 entries 53 h + T3 2.5 h + capstone 18 h ≈ 74) + Appendix A items A.21, A.23, A.24 (7 h) scheduled in this phase*


<a id="phase-8"></a>
## Phase 8: Data Products, Semantic Layer & the Architect's Practice (months 44–48, 103 h + 18.5 h Appendix A)

**Goal:** convert the governed platform into *products* — contracted, SLA-backed, semantically defined, consumable — and consolidate the formal architect's practice: DDD for boundaries, TOGAF/ArchiMate for the enterprise conversation, regulatory reporting as the domain's flagship deliverable, and the build-vs-buy fluency that Appendix D distills.
**Entry prerequisites:** Phases 1–7 (everything; this phase productizes the accumulated platform).
**Exit criteria:** you can (1) cut data-product boundaries with DDD and defend them; (2) publish a data product with an enforced contract, SLOs, and a semantic layer; (3) design a submission-grade regulatory reporting pipeline; (4) speak TOGAF/ArchiMate fluently in an EA forum; (5) win a build-vs-buy argument in any taxonomy domain with named tools and costs.
**Appendix A items scheduled here:** A.7 architecture styles & trade-off analysis, A.8 business architecture, A.9 EA governance, A.10 roadmapping & migration planning, A.11 agile EA, A.12 OWASP API security, A.13 ITSM/delivery frameworks (18.5 h).

### T1/T2 topics

#### 8.4.1 Domain-driven design — T1
- **Why:** bounded contexts are how you cut data-product and team boundaries that survive reorgs; DDD's strategic patterns are the intellectual foundation under data mesh — and the difference between domain-oriented design and folder renaming.
- **Learn:** strategic DDD only, deeply: ubiquitous language; bounded contexts & context mapping (partnership, customer-supplier, conformist, ACL, published language); subdomain types (core/supporting/generic) and investment logic; EventStorming as the discovery workshop (your BA superpower, formalized); aggregates at concept level; applying it to data: source-aligned vs aggregate vs consumer-aligned products; the fund-administration domain map (TA, fund accounting, custody, regulatory reporting, client reporting).
- **Resource:** Vlad Khononov, *Learning Domain-Driven Design* (strategic chapters 1–11) . *Alternate:* Evans for reference; *Data Mesh* ch. 2 for the data application.
- **Tools:** FOSS: EventStorming (paper/Miro-free-tier) + Context Mapper DSL (↔ — no corp equivalent; this is method).
- **Do:** run a solo EventStorming of the subscription-order-to-NAV flow; derive the context map for a fund administrator (5–7 contexts with relationship types); mark which contexts own which data products.
- **Done when:** your context map survives the challenge "why is fund accounting not part of the TA context?" with a domain answer, not an org-chart answer.
- Est. hours: 10

#### 13.1.1 + 13.1.2 Data contracts (ODCS, enforcement) — T1
- **Why:** contracts operationalize everything Phase 6 built — they are the mechanism that turns "governed dataset" into "product a consumer can rely on," and the EU fund-data world (EMT files between manufacturers and distributors!) has run on implicit contracts for years.
- **Learn:** contract anatomy: schema, semantics, quality guarantees, SLAs, ownership, terms of use; ODCS (Bitol/Linux Foundation) structure and the Data Contract Specification; datacontract-cli: authoring, validation, breaking-change detection, tests against live data; enforcement points: producer CI (schema diff), registry (Kafka), WAP gate (lakehouse), dbt model contracts; contract-first vs contract-extracted adoption paths; versioning & deprecation policy (ties to your 1.9.7 evolution policy — same policy, now productized).
- **Resource:** Andrew Jones, *Driving Data Quality with Data Contracts* + ODCS spec (bitol-io.github.io) + datacontract-cli docs.
- **Tools:** FOSS: datacontract-cli + dbt model contracts + Confluent SR (↔ Gable, DataHub contracts, Confluent data contracts).
- **Do:** write the ODCS contract for your gold NAV mart and the EMT output (schema + DQ guarantees + freshness SLO + owner + license terms); wire `datacontract test` into CI against the live lakehouse; demonstrate a breaking change being caught pre-merge.
- **Done when:** a consumer can subscribe to your product knowing exactly what is guaranteed, and a producer cannot break it silently — both demonstrated, not asserted.
- Est. hours: 10

#### 14.4.2 Regulatory reporting — T1
- **Why:** submission-grade reporting (AIFMD Annex IV, PRIIPs KID/EPT, MiFID/EMT) is the fund-data domain's flagship deliverable — deadline-driven, auditor-reviewed, and the workload your whole platform exists to serve.
- **Learn:** what makes reporting "submission-grade": completeness gates, plausibility checks, four-eyes approval, resubmission/correction workflow, full lineage to source, immutable filing archive; the EU fund reporting landscape concretely: AIFMD Annex IV (scope, frequency, XML), PRIIPs KID data (EPT — your Phase-2 work), EMT distribution, SFDR templates (ESG data sourcing pain); report calendars & deadline orchestration (your Dagster schedules grow teeth); the vendor landscape: Workiva/AxiomSL(Adenza)/Wolters Kluwer/Vermeg — what they actually sell (forms engines + rule updates + filing connectivity) and what stays your problem (the data); build-vs-buy economics (rule-maintenance burden is the buy argument).
- **Resource:** ESMA AIFMD reporting guidelines page (IT technical guidance + Annex IV templates, free) + your Phase-2 FinDatEx specs, reread as a producer.
- **Tools:** FOSS: the platform you built + Dagster scheduling (↔ Workiva, AxiomSL, Wolters Kluwer OneSumX — evaluation level).
- **Do:** design and implement the Annex-IV-shaped pipeline: gold marts → validation gates (completeness/plausibility) → XML rendering against the published schema → four-eyes approval step (Dagster sensor + manual gate) → immutable filing archive with lineage snapshot; write the build-vs-buy memo for the forms-engine layer.
- **Done when:** a deliberately incomplete dataset cannot reach the filing stage; a resubmission is traceable end-to-end; and your memo prices the vendor option honestly.
- Est. hours: 10

#### 8.1.3 Industry frameworks (TOGAF & ArchiMate, working fluency) — T2
- **Why:** TOGAF/ArchiMate is the lingua franca of EA departments in EU financial institutions; the architect who can't speak it gets translated by someone who can.
- **Learn:** TOGAF 10 shape: ADM cycle (what each phase produces — focus on B/C data architecture, E/F via A.10), architecture repository/landscape, building blocks; what to take seriously (deliverable discipline, governance hooks) vs hold lightly (the full ceremony); ArchiMate 3.2: core layers (business/application/technology), the data-relevant elements (business object ↔ data object ↔ artifact), viewpoints; modeling your platform in Archi; mapping C4 ↔ ArchiMate (when each audience needs which).
- **Resource:** TOGAF 10 Fundamental Content: Introduction & Core Concepts + ADM (free with Open Group registration) + Archi tool + its "hello ArchiMate" tutorial.
- **Tools:** FOSS: Archi (↔ Sparx EA, BiZZdesign — the licensed EA suites).
- **Do:** model your entire capstone platform in ArchiMate (application + technology layers, data objects for the products) and produce two viewpoints: one for the COO (business-application), one for security (technology).
- **Done when:** you can walk an EA review board through the ArchiMate model and translate any element to/from your C4 diagrams live.
- Est. hours: 10

#### 1.4.4 Data mesh (and 13.2.1 enabling platforms) — T2
- **Why:** mesh is the organizational scaling answer you'll be asked about in every large-firm interview; the architect's job is knowing when its costs are justified — and what "federated computational governance" means after Phase 6.
- **Learn:** the four principles (domain ownership, data as product, self-serve platform, federated computational governance) read against your build: you have already built principles 2–4 single-domain; what changes multi-domain; mesh failure modes (mesh-washing, platform-team starvation, premature decentralization); enabling platforms: Starburst/Trino federation, Databricks UC domains, your OpenMetadata domains; sizing test: when a 50-person fund admin should *not* mesh.
- **Resource:** Dehghani, *Data Mesh* (part I–II; skim III) + *Data Management at Scale* 2nd ed. (Strengholt's pragmatic counterweight).
- **Do:** write the two-page memo: "Should a 300-person fund administrator adopt mesh?" — org sizing, domain map (from your DDD work), platform prerequisites, and an honest no/not-yet/yes-partially recommendation.
- **Done when:** you can argue both for and against mesh for the same firm, and name the organizational precondition that decides it.
- Est. hours: 5

#### 7.1.1 + 7.2.1 Semantic & metrics layer (Cube, MetricFlow) — T2
- **Why:** "one definition of AUM" is a governance promise only a semantic layer can keep across BI tools, APIs, and notebooks; headless BI is the architectural pattern behind it.
- **Learn:** semantic-layer anatomy: dimensions, measures, joins, access control at the semantic level; Cube: data models, pre-aggregations, REST/SQL APIs, caching; MetricFlow/dbt Semantic Layer: metric definitions in the dbt DAG; metrics layer vs BI-tool-local definitions (the consistency argument); semantic layer vs glossary (definition *executed* vs definition *documented* — link them); when the semantic layer is premature.
- **Resource:** Cube docs (data modeling section) + dbt Semantic Layer/MetricFlow docs.
- **Tools:** FOSS: Cube + MetricFlow (↔ Looker/LookML, AtScale, Power BI semantic models).
- **Do:** define NAV, AUM, and net-flows once in Cube over the gold marts; consume them from three clients (Superset, a REST call, a notebook) and show identical numbers; link each metric to its glossary term.
- **Done when:** changing the AUM definition in one place changes it everywhere, with an audit trail.
- Est. hours: 7

#### 7.1.2 Platform semantic layers (Power BI semantic models) — T2
- **Why:** in Azure shops the Power BI semantic model *is* the de-facto semantic layer; you must know when it suffices and when headless wins.
- **Learn:** Power BI semantic models: import vs DirectQuery vs Direct Lake (Fabric tie to A.4); star-schema expectations (your Kimball work pays off); RLS in the model; deployment pipelines & XMLA endpoint; the "semantic model sprawl" failure mode and certified-dataset governance; Power BI vs headless decision rubric.
- **Resource:** Microsoft Learn: Power BI semantic model guidance (star schema + model management pages).
- **Tools:** Corp: Power BI (primary; free Desktop suffices for the exercise) (↔ FOSS: Cube from previous entry).
- **Do:** build the NAV mart semantic model in Power BI Desktop (free) with RLS by management company; document where its definitions and your Cube definitions could drift and the governance rule preventing it.
- **Done when:** you can rule "Power BI model vs headless layer" for three org shapes and defend it.
- Est. hours: 4

#### 12.4.1 Data SLAs & SLO management — T2
- **Why:** the SLO machinery (Phase 5 vocabulary) becomes contractual here: freshness/completeness targets with error budgets are what "productized" means operationally.
- **Learn:** data SLIs (freshness, completeness, accuracy proxy, availability of the serving layer); setting SLOs consumers actually need (interview them — BA skills) vs vanity nines; error budgets for data (when to freeze risky pipeline changes); SLO surfacing in catalog + contract; alerting on burn rate, not point failures.
- **Resource:** Google SRE Workbook SLO chapters (free online), translated to data in your contract from 13.1.1.
- **Do:** define SLOs for the NAV product (e.g., 99% of business days fresh by 08:00 CET), instrument them from the Phase-5/6 telemetry, and add a burn-rate alert; record one month of synthetic compliance.
- **Done when:** the product page shows measured SLO attainment, and a simulated bad week visibly consumes error budget with a documented response.
- Est. hours: 3

#### 13.3.2 Cross-org data sharing (Delta Sharing) — T2
- **Why:** fund data is *disseminated* — to distributors, platforms, regulators; open sharing protocols are the modern alternative to the SFTP-and-CSV folklore the industry still runs on.
- **Learn:** Delta Sharing protocol (open, REST-based, format-level); shares/recipients/governance; Snowflake shares & Databricks marketplace as the walled-garden equivalents; egress economics; sharing vs API vs file-drop decision rubric (volume, latency, consumer sophistication); contractual overlay (ties 13.1.1, A.18).
- **Resource:** Delta Sharing docs (open protocol) + Snowflake secure-sharing docs (comparison read).
- **Tools:** FOSS: delta-sharing reference server (↔ Databricks Delta Sharing, Snowflake shares, Fabric external sharing).
- **Do:** stand up the reference sharing server over a gold Delta table; consume it from a separate "distributor" environment with pandas; write the rubric: when sharing protocol vs API vs EMT file-drop.
- **Done when:** you can design the dissemination architecture for a fund manufacturer with 40 distributor relationships and defend the channel per consumer class.
- Est. hours: 3

#### 13.4.2 + 2.6.1 Data APIs & gateways (data-as-a-service) — T2
- **Why:** the API is the product surface for operational consumers (websites, partner systems); the gateway is where auth, quotas, and versioning live — an architect's checklist, not a developer's tutorial.
- **Learn:** productized data API design: resource modeling for fund data (funds/share-classes/navs), pagination, filtering, versioning policy (ties 1.9.7), OpenAPI as the contract; gateway duties: OIDC token validation (your Keycloak), rate limiting/quotas per consumer tier, usage analytics for chargeback; PostgREST/FastAPI as instant serving over gold views; caching policy (your 3.3.4 decision); when GraphQL earns its complexity (2.6.2 stays T3).
- **Resource:** Kong OSS docs (gateway concepts) + PostgREST docs.
- **Tools:** FOSS: PostgREST or FastAPI + Kong OSS (↔ Azure API Management, Apigee).
- **Do:** expose the NAV product as a read-only REST API (PostgREST over a gold view) behind Kong with OIDC + rate limits; publish its OpenAPI document; run the OWASP API Top-10 checklist (A.12) against it.
- **Done when:** an external consumer can onboard from the OpenAPI doc + contract alone, and the gateway proves quota enforcement in logs.
- Est. hours: 5

#### 14.1.1 + 14.1.3 Business intelligence (Superset hands-on, Power BI fluency) — T2
- **Why:** BI is where your platform meets its judges; the architect doesn't build dashboards for a living but must design the BI tier (tooling, governance, self-service boundaries) and read the vendor market.
- **Learn:** Superset: datasets/charts/dashboards, semantic-ish layer, RLS, embedding; Power BI ecosystem economics (per-user vs capacity/Fabric licensing — the real selection driver in Azure shops); Tableau/Looker/Qlik positioning in one sitting; governed self-service: certified datasets, sandbox vs production content, the "300 unowned dashboards" failure mode; BI-on-semantic-layer (consume Cube, don't re-model).
- **Resource:** Superset docs (creating charts/dashboards + security) + Power BI licensing/deployment guidance page.
- **Tools:** FOSS: Apache Superset, Metabase (↔ Power BI [Azure default], Tableau, Looker) · Corp: Power BI (primary evaluation).
- **Do:** build the fund-board dashboard (NAV trend, flows, DQ status) in Superset *on top of Cube*; write the BI governance one-pager (certification workflow, ownership, sandbox policy).
- **Done when:** the dashboard consumes only semantic-layer metrics (zero local SQL definitions), and your governance pager answers "who may publish what, where".
- Est. hours: 7

#### 14.6.1 Data app frameworks (Streamlit) — T2
- **Why:** data apps are the fast path from platform to stakeholder value (review queues, what-if tools); Streamlit is the de-facto standard and your Phase-7 review UI already used it.
- **Learn:** Streamlit execution model (rerun-on-interaction, caching, session state) and its scaling limits; when Streamlit vs Dash vs a real frontend; deployment & auth patterns behind the gateway; the internal-tools landscape (Retool-class) at a glance.
- **Resource:** Streamlit docs (main concepts + caching).
- **Tools:** FOSS: Streamlit (↔ Snowflake-Streamlit, Retool, Power Apps).
- **Do:** build the "fund data product console": SLO status, contract version, DQ results, lineage link, sample data preview — one screen per product, served behind Kong.
- **Done when:** a product owner can answer "is my product healthy and who consumes it?" from the console without touching the platform.
- Est. hours: 3

#### 1.8.11 Strangler fig (legacy replacement strategy) — T2
- **Why:** every Luxembourg estate has a legacy core (TA system, reporting engine) that can only be replaced incrementally; strangler-fig discipline is how migrations avoid big-bang death — and it operationalizes your A.10 roadmapping.
- **Learn:** facade/routing layer placement for data systems (views, CDC-fed parallel run, dual-write avoidance — use your outbox/CDC instead); parallel-run reconciliation as the trust-builder (your Phase-4 reconciliation pattern, reused); cutover & rollback criteria; anti-pattern: strangler that never finishes (sunset discipline).
- **Resource:** Fowler's Strangler Fig article + Azure Architecture Center strangler-fig pattern page.
- **Do:** write the migration ADR for replacing a legacy reporting mart with your gold layer: facade, parallel-run period, reconciliation gates, cutover criteria, rollback plan, sunset date.
- **Done when:** the plan has measurable gates (reconciliation drift thresholds) instead of dates-and-hope.
- Est. hours: 2

### T3 awareness topics

| ID | Topic | What it is | Read | Est. min |
|---|---|---|---|---|
| 1.4.5 | Data fabric | Metadata-driven unified-access vision (vendor-led counterpoint to mesh) | Gartner-adjacent vendor explainer, read critically | 20 |
| 2.6.2 | GraphQL data layers | Schema-driven query APIs (Hasura); complexity rarely earned for fund data | Hasura "how it works" page | 20 |
| 2.7.1 | Reverse ETL | Warehouse → SaaS sync (Hightouch/Census); CRM-enrichment use cases | Hightouch docs intro | 20 |
| 13.3.1 | Internal data marketplaces | Catalog-with-checkout UX over data products | Atlan/DataHub marketplace blog | 15 |
| 13.3.3 | Commercial data marketplaces | Buying market/ESG data feeds (Snowflake Marketplace, Datarade) | Snowflake Marketplace overview | 20 |
| 13.4.1 | GraphQL DaaS | Productized GraphQL endpoints; see 2.6.2 | covered there | 5 |
| 14.1.2 | Legacy enterprise BI | BusinessObjects/Cognos/MicroStrategy estates you'll migrate from | one vendor-positioning overview | 20 |
| 14.2.1 | Visualization libraries | Plotly/Vega/D3 programmatic charting; Storytelling-with-Data principles | *Storytelling with Data* ch. 1–2 skim | 45 |
| 14.3.1 | Embedded analytics | BI inside products (Superset/Cube embed, Looker embed) | Cube embedding docs page | 20 |
| 14.4.1 | Operational/paginated reporting | Pixel-perfect statements (Power BI paginated, Jasper) | Power BI paginated reports overview | 20 |
| 14.5.1 | Cloud notebooks | Hex/Deepnote collaborative analysis; governance angle (where results live) | Hex product overview | 15 |
| 14.6.2 | Low-code internal tools | Retool/Appsmith CRUD builders on governed APIs | Appsmith overview | 15 |
| 14.7.2 | Reverse-ETL activation | Acting on data signals in operational tools; see 2.7.1 | covered there | 5 |

*T3 subtotal: 4 h*

### Capstone 8 — The fund data product (end state)

- **Goal:** the four-year arc closes: one fund data product, productized end-to-end — contracted, SLO-backed, semantically defined, multi-channel (BI, API, sharing, EMT file), regulator-ready, and documented like the portfolio piece it is.
- **Stack (100% free):** everything already running, plus Cube + MetricFlow (↔ Looker/AtScale/Power BI semantic models), datacontract-cli + ODCS (↔ Gable/Collibra contracts), PostgREST + Kong (↔ Azure API Management), delta-sharing server (↔ Databricks/Snowflake sharing), Superset (↔ Power BI), Streamlit console, Archi for the ArchiMate model (↔ Sparx EA).
- **Build:** (1) the "Fund NAV & Flows" data product: ODCS contract, SLOs with burn-rate alerting, semantic metrics, owner & glossary links — all visible in the catalog; (2) four consumption channels from one gold source: Superset board dashboard, REST API behind Kong, Delta Share to a "distributor", EMT/Annex-IV regulatory outputs with validation gates and four-eyes approval; (3) the product console (Streamlit); (4) the architect's portfolio: full C4 set, ArchiMate model + 2 viewpoints, the complete ADR log (001–022+), DDD context map, DCAM assessment + roadmap, build-vs-buy memos, migration (strangler) plan; (5) a 30-minute "architecture walkthrough" deck/script — the artifact you'd present to an interview panel or review board.
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
