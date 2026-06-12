# Prompt for Claude Code — generate `STUDY_PLAN.md` (Fundamentals → Data Architect)

Copy everything below the line into Claude Code, run from the folder containing
`data-architecture-learning-guide-v2.md`. Edit the `PARAMETERS` block first if needed.

---

## TASK

Create `STUDY_PLAN.md`: a complete, self-contained study plan that takes me from my
current level to a top-tier **Data Architect (financial services / fund industry)**.
If I learn everything in this plan to the prescribed depth, there should be no
material gap left in my knowledge for that role.

## PARAMETERS

- TAXONOMY_FILE: `./data-architecture-learning-guide-v2.md`
- HOURS_PER_WEEK: 6
- HORIZON_YEARS: 4  (total budget ≈ 6 × 48 × 4 ≈ 1,150 study hours — the plan MUST fit)
- PRIMARY_CLOUD: Azure (secondary awareness: AWS, Databricks, Snowflake)
- DOMAIN_FOCUS: investment funds / asset management / regulatory data (Luxembourg)
- TOOLING_POLICY: dual-track — **hands-on with leading FOSS** (free to run locally,
  used for all exercises/capstones) + **decision-level knowledge of the corporate
  market leaders** actually deployed in EU financial services (what job ads and
  vendor-selection meetings name).

## LEARNER PROFILE (calibrate starting level — do NOT teach these from scratch)

- 9+ years as Business Analyst & Data Engineer in fintech (wealth aggregation, fund data).
- Solid: Python, SQL (incl. window functions, CTEs), Git, Docker basics, Linux basics,
  data modeling fundamentals, requirements/BA work, Jira/Confluence.
- Currently learning/using: dbt, uv/ruff, JupyterLab, dimensional modeling vocabulary.
- Weak/missing: distributed systems theory, streaming, Spark, cloud architecture at scale,
  Kubernetes, IaC, governance frameworks, formal architecture practice (ADRs, TOGAF/ArchiMate),
  security/compliance architecture, MLOps/LLMOps.
- MSc in Mathematics & Computer Science — comfortable with theory; do not oversimplify.

## INPUT 1 — CANONICAL TAXONOMY (source of truth for WHAT to cover)

Read TAXONOMY_FILE in full. It contains:
- 14 domains → categories → ~243 subcategories (Fundamentals, Connectivity, Storage,
  Compute, Processing, AI/ML, Semantic, Architecture, Engineering Practice, Governance,
  Security & Compliance, Operations, Data Products, Consumption);
- reference lists: Concepts & Patterns, Standards & Protocols, Financial Services
  Standards & Protocols, Books (incl. fund-data books), Tools & Vendors.

The Tools & Vendors list tags every tool `(OS)` open-source, `(SA)` source-available,
`(C)` cloud-managed, `(E)` enterprise. Use these tags to drive TOOLING_POLICY: per
category select 1–2 `(OS)`/`(SA)` tools for hands-on work and 1–2 `(C)`/`(E)` market
leaders for evaluation-level knowledge. Selection criteria: adoption in EU financial
services, job-ad frequency, maturity — name the winner, not five alternatives.

This taxonomy defines the scope. Every subcategory must end up in exactly one of:
(a) the study plan, or (b) an explicit `## Excluded` section with a one-line reason.

## INPUT 2 — EXTERNAL CROSS-CHECK SOURCES (for gaps and resource selection only)

Use web access if available; otherwise use built-in knowledge and tag items `[unverified]`.
Never invent URLs.

- roadmap.sh: `data-engineer`, `software-architect`, `system-design`; selectively
  `ai-engineer`, `devops`, `postgresql-dba`.
- DAMA-DMBOK2 (Revised Edition) table of contents + CDMP exam outline (dama.org).
- TOGAF Standard 10th Edition structure + ArchiMate 3.2 (The Open Group).
- EDM Council: DCAM and CDMC capability frameworks (financial-services data management).
- Cert syllabi (use as free topic checklists, certs themselves optional):
  Microsoft DP-700/DP-600, Databricks Data Engineer Professional, SnowPro Advanced
  Architect, AWS Solutions Architect Professional, Confluent CCDAK.
- Courses: CMU 15-445 Database Systems, MIT 6.824 Distributed Systems,
  DataTalksClub Data Engineering Zoomcamp.
- Books: prefer the ones already in the taxonomy's Books reference list (DDIA latest
  edition, Fundamentals of Data Engineering, Kimball Toolkit, Data Vault 2.0, Data Mesh,
  Streaming Systems, Database Internals, Software Architecture: The Hard Parts,
  Building Evolutionary Architectures, DAMA-DMBOK).

Topics found in these sources but missing from the taxonomy go to an
`## Appendix A — Gap Additions` section (do not silently merge into the tree).

## PROCESS (execute in order; verify each step before the next)

1. **Parse** TAXONOMY_FILE → extract the full domain/category/subcategory tree into a
   working list with stable IDs (e.g., `3.2.1`).
2. **Cross-check** the tree against INPUT 2; record genuine gaps for Appendix A.
3. **Tier every subcategory** by target depth for a financial-services Data Architect:
   - **T1 Master** — can design, implement, debug, and teach it. (~15–20% of topics)
   - **T2 Working** — can use, evaluate, integrate, and make build/buy decisions. (~40%)
   - **T3 Awareness** — can recognize it, explain tradeoffs, know when to go deeper. (~40%)
   One-line justification per T1 item. Tiering rationale: architects are defined by
   calibrated depth, not uniform depth. Bias T1 toward: data modeling, distributed
   systems fundamentals, storage/lakehouse architecture, integration patterns,
   orchestration, governance & lineage, security/compliance for regulated finance,
   architecture practice (ADRs, C4, tradeoff analysis), cost/FinOps.
4. **Sequence** topics into 6–8 phases ordered by prerequisite dependency, not by
   taxonomy order. Each phase = theme + duration + entry prerequisites + exit criteria.
   Phase 1 must respect the learner profile (skip Python/SQL/Git basics).
5. **Write topic entries.** For every T1 and T2 topic:
   - `Why` (1 line, role-relevant),
   - `Learn` (key concepts checklist, 3–8 bullets),
   - `Resource` (ONE primary: book + chapters, or official doc, or course unit;
     optionally one alternate),
   - `Tools` (dual-track per TOOLING_POLICY: `FOSS:` tool(s) to practice with ·
     `Corp:` enterprise/cloud leader(s) to know at build-vs-buy level; omit the line
     for purely conceptual topics),
   - `Do` (one concrete exercise — code, design doc, or comparison memo),
   - `Done when` (self-test: a question I must answer or artifact I must produce),
   - `Est. hours`.
   T3 topics: grouped tables per category with `Topic | What it is (1 line) |
   Read (1 link/chapter) | Est. min`.
6. **Capstone projects** — one per phase, cumulative, themed on fund/financial data
   (e.g., fund-document ingestion → lakehouse → dbt → orchestration → governance/lineage
   → LLM extraction → data product with SLAs). Capstone stacks must be **100% free to
   run** (FOSS/source-available or genuinely free tiers, Docker-composable on a laptop);
   annotate every component with its corporate equivalent ("MinIO ↔ ADLS Gen2",
   "OpenMetadata ↔ Collibra/Purview"). Each capstone lists: goal, stack,
   architecture deliverables (C4 diagram + 2–3 ADRs), and acceptance criteria.
7. **Budget check** — sum all `Est. hours` + capstones; must be ≤ total budget with
   ~15% slack. If over, demote T2→T3 (state which) rather than cutting coverage.
8. **QA pass** — assert: (a) every taxonomy ID appears exactly once in plan or Excluded;
   (b) all intra-document anchors resolve; (c) no duplicate resources doing the same job;
   (d) phase prerequisites form a DAG. Print the assertion results at the end of the run
   (not in the document).

## OUTPUT FORMAT — single file `STUDY_PLAN.md`

1. `# Study Plan: Fundamentals → Data Architect` — 10-line overview: tier definitions,
   total hours, phase map table (`Phase | Theme | Months | Hours | Capstone`).
2. `## Skip List` — what the profile already covers, one line each.
3. `## Phase 1..N` — each: goal, exit criteria, topic entries (T1/T2 full format,
   T3 tables), capstone spec.
4. `## Excluded` — taxonomy subcategories deliberately out of scope + reason.
5. `## Appendix A — Gap Additions` — external topics absent from the taxonomy.
6. `## Appendix B — Reading Order` — consolidated book list with chapter→phase mapping.
7. `## Appendix C — Coverage Matrix` — table `Taxonomy ID | Topic | Tier | Phase`.
8. `## Appendix D — Tool Equivalence Map` — one table per taxonomy domain:
   `Category | FOSS pick (hands-on) | Corp/cloud leader (evaluate) | When the corporate
   option wins (1 line)`. This is the build-vs-buy cheat sheet for interviews and
   vendor selection; derive it from the taxonomy's `(OS)/(SA)/(C)/(E)` tags.

## STYLE CONSTRAINTS

- No motivational filler, no generic career advice, no tool marketing.
- Markdown only; tables where specified; anchors for all phases and appendices.
- Be specific: "DDIA ch. 5–6" not "read about replication".
- Where the taxonomy already names books/tools for a subcategory, prefer those.
