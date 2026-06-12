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
