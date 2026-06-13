# /// script
# dependencies = ["markdown"]
# ///
# Generates docs/data.js (study-tracker dataset) from _parts/*.md + Appendix A tables.
# Also: builds a resource/tool link map from the taxonomy reference lists and auto-links
# names in the rendered content; renders the full plan (guide/appendices) as in-app pages.
# Run: uv run _build_tracker.py
import json
import re
from pathlib import Path

import markdown

root = Path(__file__).parent
parts = root / "_parts"
out_dir = root / "docs"
out_dir.mkdir(exist_ok=True)

MD = markdown.Markdown(extensions=["tables"])


def md2html(text: str) -> str:
    MD.reset()
    return MD.convert(text)


ID_RX = re.compile(r"\b(?:\d+\.\d+(?:\.\d+)?|A\.\d+)\b")

# ---------------------------------------------------------------- link map
TAXO = (root / "data-architecture-learning-guide-v2.md").read_text(encoding="utf-8")
LINKS: dict[str, str] = {}


def add(name: str, url: str):
    name = name.strip()
    if len(name) >= 3 and name not in LINKS:
        LINKS[name] = url


def aliases_for(name: str):
    out = [name]
    no_paren = re.sub(r"\s*\([^)]*\)", "", name).strip()
    if no_paren != name:
        out.append(no_paren)
        for inner in re.findall(r"\(([^)]+)\)", name):
            for piece in re.split(r"\s*/\s*", inner):
                if not re.search(r"\d|ed\.|formerly|now", piece):
                    out.append(piece.strip())
    for piece in re.split(r"\s*/\s*", no_paren):
        out.append(piece.strip())
    for pref in ("Apache ", "HashiCorp "):
        if no_paren.startswith(pref):
            out.append(no_paren[len(pref):])
    return out


URL_RX = r"🔗 (https?://\S+)"
# tools: **Name** — *(tags)* — description 🔗 url
for m in re.finditer(r'<a id="t-[^"]+"></a>\n\*\*(.+?)\*\* — .*?' + URL_RX, TAXO):
    url = m.group(2).rstrip(".,·)")
    for a in aliases_for(m.group(1)):
        add(a, url)
# books + standards + domain books: ### Title ... 🔗 url (first link in block)
for m in re.finditer(r"^### (.+?)\n((?:(?!^#{1,3} ).*\n?)*)", TAXO, re.M):
    title, block = m.group(1).strip(), m.group(2)
    u = re.search(URL_RX, block)
    if not u:
        continue
    url = u.group(1).rstrip(".,·)")
    for a in aliases_for(title):
        add(a, url)
    if ":" in title:
        add(title.split(":")[0].strip(), url)

MANUAL = {
    "DDIA": "https://dataintensive.net/",
    "Kimball": "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/",
    "Data Warehouse Toolkit": LINKS.get("Kimball", "https://www.kimballgroup.com/"),
    "Data Vault 2.0": "https://www.elsevier.com/books/building-a-scalable-data-warehouse-with-data-vault-2-0/linstedt/978-0-12-802510-9",
    "Postgres": "https://www.postgresql.org/docs/",
    "Power BI": "https://learn.microsoft.com/power-bi/",
    "Entra ID": "https://learn.microsoft.com/entra/",
    "Event Hubs": "https://learn.microsoft.com/azure/event-hubs/",
    "ADF": "https://learn.microsoft.com/azure/data-factory/",
    "ADLS Gen2": "https://learn.microsoft.com/azure/storage/blobs/data-lake-storage-introduction",
    "Synapse": "https://learn.microsoft.com/azure/synapse-analytics/",
    "LEI": "https://www.gleif.org/",
    "EMT/EPT": "https://findatex.eu/",
    "FinDatEx": "https://findatex.eu/",
    "Kubernetes": "https://kubernetes.io/docs/tutorials/",
    "AKS": "https://learn.microsoft.com/azure/aks/",
    "kind": "https://kind.sigs.k8s.io/",
    "Helm": "https://helm.sh/docs/",
    "Argo CD": "https://argo-cd.readthedocs.io/",
    "Microsoft Fabric": "https://learn.microsoft.com/fabric/",
    "OneLake": "https://learn.microsoft.com/fabric/onelake/",
    "KQL": "https://learn.microsoft.com/training/modules/write-first-query-kusto-query-language/",
    "Azure Well-Architected": "https://learn.microsoft.com/azure/well-architected/",
    "Well-Architected Framework": "https://learn.microsoft.com/azure/well-architected/",
    "CAF": "https://learn.microsoft.com/azure/cloud-adoption-framework/",
    "Azure Policy": "https://learn.microsoft.com/azure/governance/policy/",
    "Bicep": "https://learn.microsoft.com/training/paths/fundamentals-bicep/",
    "Azure Cost Management": "https://learn.microsoft.com/azure/cost-management-billing/",
    "Azure Chaos Studio": "https://learn.microsoft.com/azure/chaos-studio/",
    "Microsoft Sentinel": "https://learn.microsoft.com/azure/sentinel/",
    "CMU 15-445": "https://15445.courses.cs.cmu.edu/",
    "MIT 6.5840": "https://pdos.csail.mit.edu/6.824/",
    "MIT 6.824": "https://pdos.csail.mit.edu/6.824/",
    "SQLBolt": "https://sqlbolt.com/",
    "PgExercises": "https://pgexercises.com/",
    "Pro Git": "https://git-scm.com/book",
    "Python for Everybody": "https://www.py4e.com/",
    "py4e": "https://www.py4e.com/",
    "Automate the Boring Stuff": "https://automatetheboringstuff.com/",
    "The Missing Semester": "https://missing.csail.mit.edu/",
    "Missing Semester": "https://missing.csail.mit.edu/",
    "Docker Compose": "https://docs.docker.com/compose/",
    "Dockerfile": "https://docs.docker.com/get-started/",
    "Docker": "https://docs.docker.com/get-started/",
    "MDN": "https://developer.mozilla.org/en-US/docs/Learn",
    "Cloudflare Learning Center": "https://www.cloudflare.com/learning/",
    "Python for Data Analysis": "https://wesmckinney.com/book/",
    "Google Engineering Practices": "https://google.github.io/eng-practices/",
    "Google SRE Book": "https://sre.google/books/",
    "Google SRE Workbook": "https://sre.google/books/",
    "SRE Workbook": "https://sre.google/books/",
    "Terraform: Up & Running": "https://www.terraformupandrunning.com/",
    "Data Pipelines with Apache Airflow": "https://www.manning.com/books/data-pipelines-with-apache-airflow",
    "microservices.io": "https://microservices.io/patterns/",
    "Azure Architecture Center": "https://learn.microsoft.com/azure/architecture/",
    "adr.github.io": "https://adr.github.io/",
    "MADR": "https://adr.github.io/madr/",
    "AutomateDV": "https://automate-dv.readthedocs.io/",
    "Splink": "https://moj-analytical-services.github.io/splink/",
    "OpenBao": "https://openbao.org/",
    "Ollama": "https://ollama.com/",
    "FinOps Foundation": "https://www.finops.org/framework/",
    "pgAudit": "https://www.pgaudit.org/",
    "pyarrow": "https://arrow.apache.org/docs/python/",
    "Strangler Fig": "https://martinfowler.com/bliki/StranglerFigApplication.html",
    "Parallel Change": "https://martinfowler.com/bliki/ParallelChange.html",
    "Event Sourcing essay": "https://martinfowler.com/eaaDev/EventSourcing.html",
    "Iceberg REST": "https://iceberg.apache.org/spec/",
    "GLEIF": "https://www.gleif.org/",
    "roadmap.sh": "https://roadmap.sh/",
    "DCAM": "https://edmcouncil.org/frameworks/dcam/",
    "CDMC": "https://edmcouncil.org/frameworks/cdmc/",
    "VS Code": "https://code.visualstudio.com/docs",
    "JupyterLab": "https://docs.jupyter.org/",
    "uv": "https://docs.astral.sh/uv/",
    "ruff": "https://docs.astral.sh/ruff/",
    "Anthropic “Building Effective Agents”": "https://www.anthropic.com/engineering/building-effective-agents",
}
for k, v in MANUAL.items():
    LINKS[k] = v

STOP = {"None", "REST", "JSON", "XML", "YAML", "CSV", "SQL", "Mage", "Hop", "Aim", "SDL"}
for s in STOP:
    LINKS.pop(s, None)
NAMES = sorted(LINKS.keys(), key=len, reverse=True)
NAME_RX = {n: re.compile(r"(?<![\w/.-])" + re.escape(n) + r"(?![\w/-])") for n in NAMES}
print(f"link map: {len(LINKS)} names")

TAG_RX = re.compile(r"(<[^>]+>)")


def autolink(html: str) -> str:
    segs = TAG_RX.split(html)
    in_a = 0
    linked: set[str] = set()
    for i, seg in enumerate(segs):
        if seg.startswith("<"):
            low = seg[:3].lower()
            if low.startswith("<a ") or seg.lower().startswith("<a>"):
                in_a += 1
            elif low.startswith("</a"):
                in_a = max(0, in_a - 1)
            continue
        if in_a or not seg.strip():
            continue
        spans = []  # (start, end, name)
        for name in NAMES:
            if name in linked or name not in seg:
                continue
            m = NAME_RX[name].search(seg)
            if m and not any(m.start() < e and m.end() > s for s, e, _ in spans):
                spans.append((m.start(), m.end(), name))
                linked.add(name)
        if spans:
            spans.sort()
            out, pos = [], 0
            for s, e, name in spans:
                out.append(seg[pos:s])
                out.append(f'<a href="{LINKS[name]}">{seg[s:e]}</a>')
                pos = e
            out.append(seg[pos:])
            segs[i] = "".join(out)
    return "".join(segs)


ANCHOR_MAP = {
    "how-to-use": "#/doc/guide", "phase-map": "#/",
    "tracking-progress": "#/doc/tracking", "certifications": "#/doc/tracking",
    "publishing": "#/doc/tracking", "skip-list": "#/p/0",
    "excluded": "#/doc/excluded", "appendix-a": "#/doc/appa",
    "appendix-b": "#/doc/appb", "appendix-c": "#/doc/appc", "appendix-d": "#/doc/appd",
}
for i in range(9):
    ANCHOR_MAP[f"phase-{i}"] = f"#/p/{i}"


def finalize(html: str, link_names: bool = True) -> str:
    if link_names:
        html = autolink(html)
    html = re.sub(r'href="#([\w-]+)"',
                  lambda m: f'href="{ANCHOR_MAP.get(m.group(1), "#" + m.group(1))}"', html)
    html = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', html)
    return html


# ---------------------------------------------------------------- Phase-0 quizzes
QUIZ_DIR = root / "_quizzes"
QUIZ_IDS = [f"0.{i}" for i in range(1, 13)]


def _inline_code(s: str) -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def parse_quiz(path: Path):
    pairs, q = [], None
    for line in path.read_text(encoding="utf-8").split("\n"):
        if line.startswith("Q:"):
            q = line[2:].strip()
        elif line.startswith("A:") and q is not None:
            pairs.append((q, line[2:].strip()))
            q = None
    return pairs


def quiz_html(pairs) -> str:
    inner = "".join(
        f'<details class="q"><summary><b>{i}.</b> {_inline_code(q)}</summary>'
        f'<div class="a">{_inline_code(a)}</div></details>'
        for i, (q, a) in enumerate(pairs, 1))
    return ('<details class="quiz"><summary>\U0001F4DD Self-test — '
            f'{len(pairs)} questions (tap one to reveal its answer)</summary>{inner}</details>')


# ---------------------------------------------------------------- Appendix A rows
a_items = {}
for line in (parts / "10-appendix-a.md").read_text(encoding="utf-8").splitlines():
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) == 7 and re.fullmatch(r"A\.\d+", cells[0]):
        a_items[cells[0]] = {"topic": cells[1], "source": cells[2], "tier": cells[3],
                             "phase": int(cells[4]), "hours": float(cells[6]), "resource": cells[5]}
assert len(a_items) == 31, f"expected 31 A-items, got {len(a_items)}"

PHASE_FILES = ["00b-phase0.md", "01-phase1.md", "02-phase2.md", "03-phase3.md",
               "04-phase4.md", "05-phase5.md", "06-phase6.md", "07-phase7.md",
               "08-phase8.md"]

phases = []
total_est = 0.0

for fname in PHASE_FILES:
    text = (parts / fname).read_text(encoding="utf-8")
    hm = re.search(r"^## Phase (\d): (.+?) (?:—.+?)?\(months ([\d–-]+)", text, re.M)
    n, title, months = int(hm.group(1)), hm.group(2).strip().rstrip(" —"), hm.group(3)
    intro = text.split("###")[0]
    intro_md = re.sub(r'^<a id="phase-\d"></a>\s*\n## .+$', "", intro, flags=re.M).strip()
    items = []

    for m in re.finditer(r"^#### (.+?)$\n((?:(?!^#{3,4} ).*\n?)*)", text, re.M):
        heading, body = m.group(1).strip(), m.group(2)
        ids = ID_RX.findall(heading)
        tm = re.search(r"—\s*(T[123](?:/T[123])?)\s*$", heading)
        tier = tm.group(1) if tm else ""
        a_ref = re.search(r"- Est\. hours: counted as (A\.\d+) \((\d+(?:\.\d+)?) h", body)
        em = re.search(r"^- Est\. hours: (\d+(?:\.\d+)?)\s*$", body, re.M)
        if a_ref:
            est = float(a_ref.group(2))
            tier = tier or a_items[a_ref.group(1)]["tier"]
        elif em:
            est = float(em.group(1))
        else:
            raise SystemExit(f"{fname}: no hours in entry '{heading}'")
        key = "e-" + (ids[0] if ids else re.sub(r"\W+", "-", heading.lower())[:24])
        clean_title = re.sub(r"—\s*T[123](?:/T[123])?\s*$", "", heading).strip(" —")
        body_html = finalize(md2html(body.strip()))
        nq = 0
        if n == 0 and ids:
            qp = QUIZ_DIR / f"{ids[0]}.md"
            if qp.exists():
                qpairs = parse_quiz(qp)
                if qpairs:
                    body_html += quiz_html(qpairs)
                    nq = len(qpairs)
        items.append({"key": key, "title": clean_title, "ids": ids, "tier": tier or "T2",
                      "est": est, "kind": "entry", "quiz": nq, "html": body_html})

    t3 = re.search(r"^### T3 awareness topics\n((?:(?!^### ).*\n?)*)", text, re.M)
    if t3:
        sub = re.search(r"\*T3 subtotal: ([\d.]+) h\*", t3.group(1))
        t3_ids = ID_RX.findall(re.sub(r"\(.*?\)", "", t3.group(1)))
        items.append({"key": f"t3-p{n}", "title": "T3 awareness table (quick reads)",
                      "ids": sorted(set(i for i in t3_ids if not i.startswith("A."))),
                      "tier": "T3", "est": float(sub.group(1)), "kind": "t3",
                      "html": finalize(md2html(t3.group(1).strip()))})

    cap = re.search(r"^### (Capstone \d.*?)$\n((?:(?!^#{2,3} |^\*Phase).*\n?)*)", text, re.M)
    capm = re.search(r"^- Est\. hours: (\d+(?:\.\d+)?)\s*$", cap.group(2), re.M)
    items.append({"key": f"cap-{n}", "title": cap.group(1).strip(), "ids": [],
                  "tier": "CAP", "est": float(capm.group(1)), "kind": "capstone",
                  "html": finalize(md2html(cap.group(2).strip()))})

    if n != 0:
        for aid, a in sorted(a_items.items(), key=lambda kv: int(kv[0][2:])):
            if a["phase"] == n:
                body = (f"**Why it matters:** {a['topic']}\n\n**Source:** {a['source']}"
                        f"\n\n**Primary resource:** {a['resource']}")
                items.append({"key": f"a-{aid}",
                              "title": f"{aid} {a['topic'].split(' — ')[0].split(' (')[0]}",
                              "ids": [aid], "tier": a["tier"], "est": a["hours"],
                              "kind": "gap", "html": finalize(md2html(body))})

    ph_est = sum(i["est"] for i in items)
    total_est += ph_est
    phases.append({"n": n, "title": title, "months": months, "estH": round(ph_est, 1),
                   "intro": finalize(md2html(intro_md)), "items": items})
    print(f"Phase {n}: {len(items)} items, {ph_est:g} h")

print(f"TOTAL: {sum(len(p['items']) for p in phases)} items, {total_est:g} h (expect 1100)")
assert abs(total_est - 1100) < 1, f"hours drifted: {total_est}"

# ---------------------------------------------------------------- plan pages
header = (parts / "00-header.md").read_text(encoding="utf-8")
g_end = header.index('<a id="tracking-progress"></a>')
t_end = header.index('<a id="phase-map"></a>')
# Phase map -> the home screen; skip tests -> each Phase-0 module's Done-when.
# So the trailing "Phase Map / Skip List" pointer block (header[t_end:]) is not a standalone page.
pages = [
    {"key": "guide", "title": "Overview & how to use", "md": header[:g_end]},
    {"key": "tracking", "title": "Tracking, certifications & publishing", "md": header[g_end:t_end]},
    {"key": "excluded", "title": "Excluded topics", "md": (parts / "09-excluded.md").read_text(encoding="utf-8")},
    {"key": "appa", "title": "Appendix A — Gap additions", "md": (parts / "10-appendix-a.md").read_text(encoding="utf-8")},
    {"key": "appb", "title": "Appendix B — Reading order", "md": (parts / "11-appendix-b.md").read_text(encoding="utf-8")},
    {"key": "appc", "title": "Appendix C — Coverage matrix", "md": (parts / "12-appendix-c.md").read_text(encoding="utf-8")},
    {"key": "appd", "title": "Appendix D — Tool equivalence map", "md": (parts / "13-appendix-d.md").read_text(encoding="utf-8")},
]
out_pages = []
for pg in pages:
    md_txt = re.sub(r'<a id="[\w-]+"></a>\n?', "", pg["md"])
    md_txt = re.sub(r"^## .+$", "", md_txt, count=1, flags=re.M).strip()
    link_names = pg["key"] in {"appb", "appd", "appa", "tracking"}  # link-rich pages
    out_pages.append({"key": pg["key"], "title": pg["title"],
                      "html": finalize(md2html(md_txt), link_names=link_names)})
    print(f"page {pg['key']}: {len(out_pages[-1]['html']) // 1024} KB")

data = {"version": 2, "budgetH": 1152, "fullH": round(total_est, 1),
        "phases": phases, "pages": out_pages}
js = "window.PLAN = " + json.dumps(data, ensure_ascii=False) + ";"
(out_dir / "data.js").write_text(js, encoding="utf-8")
print(f"wrote docs/data.js ({len(js) // 1024} KB)")

# ---------------------------------------------------------------- QUIZZES.md (GitHub-readable)
qz = ["# Phase 0 — Self-test Question Banks\n",
      "100 questions per foundation lesson. Click a question to reveal its answer. "
      "These also appear inside each lesson in the [tracker app](https://sergeiosipov.github.io/data-architect-roadmap/).\n"]
qtotal = 0
for qid in QUIZ_IDS:
    p = QUIZ_DIR / f"{qid}.md"
    if not p.exists():
        continue
    lines = p.read_text(encoding="utf-8").split("\n")
    title = next((ln.lstrip("# ").strip() for ln in lines if ln.startswith("#")), f"Phase 0 · {qid}")
    pairs = parse_quiz(p)
    qtotal += len(pairs)
    qz.append(f"\n## {title}\n")
    for i, (q, a) in enumerate(pairs, 1):
        qz.append(f"<details><summary><b>{i}.</b> {q}</summary>\n\n{a}\n\n</details>\n")
(root / "QUIZZES.md").write_text("\n".join(qz), encoding="utf-8")
print(f"wrote QUIZZES.md ({qtotal} questions across "
      f"{sum(1 for q in QUIZ_IDS if (QUIZ_DIR / f'{q}.md').exists())} lessons)")
