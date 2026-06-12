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
