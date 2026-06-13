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
