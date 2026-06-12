# /// script
# dependencies = ["markdown"]
# ///
# Generates docs/data.js (study-tracker dataset) from _parts/*.md + the Appendix A tables.
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

# --- Appendix A rows (id -> {topic, tier, phase, hours, row_md}) ---
a_items = {}
for line in (parts / "10-appendix-a.md").read_text(encoding="utf-8").splitlines():
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) == 7 and re.fullmatch(r"A\.\d+", cells[0]):
        a_items[cells[0]] = {
            "topic": cells[1], "source": cells[2], "tier": cells[3],
            "phase": int(cells[4]), "hours": float(cells[6]), "resource": cells[5],
        }
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

    # entries: split on #### headings
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
        items.append({"key": key, "title": clean_title, "ids": ids, "tier": tier or "T2",
                      "est": est, "kind": "entry",
                      "html": md2html(body.strip())})

    # T3 table as one item
    t3 = re.search(r"^### T3 awareness topics\n((?:(?!^### ).*\n?)*)", text, re.M)
    if t3:
        sub = re.search(r"\*T3 subtotal: ([\d.]+) h\*", t3.group(1))
        t3_ids = ID_RX.findall(re.sub(r"\(.*?\)", "", t3.group(1)))
        items.append({"key": f"t3-p{n}", "title": "T3 awareness table (quick reads)",
                      "ids": sorted(set(i for i in t3_ids if not i.startswith("A."))),
                      "tier": "T3", "est": float(sub.group(1)), "kind": "t3",
                      "html": md2html(t3.group(1).strip())})

    # capstone as one item
    cap = re.search(r"^### (Capstone \d.*?)$\n((?:(?!^#{2,3} |^\*Phase).*\n?)*)", text, re.M)
    capm = re.search(r"^- Est\. hours: (\d+(?:\.\d+)?)\s*$", cap.group(2), re.M)
    items.append({"key": f"cap-{n}", "title": cap.group(1).strip(), "ids": [],
                  "tier": "CAP", "est": float(capm.group(1)), "kind": "capstone",
                  "html": md2html(cap.group(2).strip())})

    # standalone Appendix-A items for this phase (P0's A.27-31 are embedded in modules)
    if n != 0:
        for aid, a in sorted(a_items.items(), key=lambda kv: int(kv[0][2:])):
            if a["phase"] == n:
                body = (f"**Why it matters:** {a['topic']}\n\n**Source:** {a['source']}"
                        f"\n\n**Primary resource:** {a['resource']}")
                items.append({"key": f"a-{aid}", "title": f"{aid} {a['topic'].split(' — ')[0].split(' (')[0]}",
                              "ids": [aid], "tier": a["tier"], "est": a["hours"],
                              "kind": "gap", "html": md2html(body)})

    ph_est = sum(i["est"] for i in items)
    total_est += ph_est
    phases.append({"n": n, "title": title, "months": months,
                   "estH": round(ph_est, 1), "intro": md2html(intro_md), "items": items})
    print(f"Phase {n}: {len(items)} items, {ph_est:g} h")

print(f"TOTAL: {sum(len(p['items']) for p in phases)} items, {total_est:g} h (expect 1100)")
assert abs(total_est - 1100) < 1, f"hours drifted: {total_est}"

data = {"version": 1, "budgetH": 1152, "fullH": round(total_est, 1), "phases": phases}
js = "window.PLAN = " + json.dumps(data, ensure_ascii=False) + ";"
(out_dir / "data.js").write_text(js, encoding="utf-8")
print(f"wrote docs/data.js ({len(js)//1024} KB)")
