# Assembles STUDY_PLAN.md from _parts/ and runs the step-8 QA assertions.
# Run: uv run _assemble_and_qa.py
import re
import sys
from pathlib import Path

root = Path(__file__).parent
parts_dir = root / "_parts"
ORDER = [
    "00-header.md", "00b-phase0.md", "01-phase1.md", "02-phase2.md", "03-phase3.md",
    "04-phase4.md", "05-phase5.md", "06-phase6.md", "07-phase7.md", "08-phase8.md",
    "09-excluded.md", "10-appendix-a.md", "11-appendix-b.md", "12-appendix-c.md",
    "13-appendix-d.md",
]

texts = [(name, (parts_dir / name).read_text(encoding="utf-8")) for name in ORDER]
doc = "\n\n".join(t for _, t in texts)
(root / "STUDY_PLAN.md").write_text(doc, encoding="utf-8")
print(f"ASSEMBLED STUDY_PLAN.md: {len(doc.splitlines())} lines, {len(doc)} chars\n")

results: list[tuple[str, bool, str]] = []

# (a) every taxonomy ID exactly once in plan (Appendix C) or Excluded; excluded IDs consistent
wl_rows = re.findall(r"^\| (\d+\.\d+\.\d+) \| .+? \| (.+?) \| (.+?) \|",
                     (root / "_worklist.md").read_text(encoding="utf-8"), re.M)
wl_ids = [r[0] for r in wl_rows]
mat_section = doc.split('<a id="appendix-c"></a>')[1].split('<a id="appendix-d"></a>')[0]
mat_ids = re.findall(r"^\| (\d+\.\d+\.\d+) \|", mat_section, re.M)
exc_section = doc.split('<a id="excluded"></a>')[1].split('<a id="appendix-a"></a>')[0]
exc_ids = set(re.findall(r"^\| (\d+\.\d+\.\d+) \|", exc_section, re.M))
wl_exc = {i for i, t, p in wl_rows if p.strip() == "Excluded"}
ok_a = (
    len(wl_ids) == 252 and len(set(wl_ids)) == 252
    and sorted(mat_ids) == sorted(wl_ids) and len(mat_ids) == len(set(mat_ids))
    and exc_ids == wl_exc
)
results.append(("(a) 252 IDs exactly once; Excluded table == worklist Excluded set",
                ok_a, f"worklist={len(wl_ids)} matrix={len(mat_ids)} unique={len(set(mat_ids))} excluded={sorted(exc_ids)}"))

# (b) intra-document anchors resolve
targets = set(re.findall(r'<a id="([^"]+)"></a>', doc))
links = set(re.findall(r"\]\(#([^)\s]+)\)", doc))
missing = links - targets
results.append(("(b) all intra-document anchors resolve", not missing,
                f"links={len(links)} targets={len(targets)} missing={sorted(missing) or 'none'}"))

# (c) no two entries use the identical primary resource
resources = [re.sub(r"\s*\*Alternate.*$", "", r).rstrip(" .")
             for r in re.findall(r"^- \*\*Resource:\*\* (.+)$", doc, re.M)]
norm = {}
for r in resources:
    norm.setdefault(r.strip().lower(), 0)
    norm[r.strip().lower()] += 1
dupes = {k: v for k, v in norm.items() if v > 1}
results.append(("(c) no duplicate primary resources doing the same job", not dupes,
                f"{len(resources)} primary resources; duplicates: {dupes or 'none'}"))

# (d) phase prerequisites form a DAG (each phase only references earlier phases)
ok_d, detail_d = True, []
for m in re.finditer(r'<a id="phase-(\d)"></a>(.*?)(?=<a id="phase-|\Z)', doc, re.S):
    n = int(m.group(1))
    prereq_m = re.search(r"\*\*Entry prerequisites:\*\* (.+)", m.group(2))
    refs = [int(x) for x in re.findall(r"Phases? (\d)", prereq_m.group(1))] if prereq_m else []
    refs += [int(x) for x in re.findall(r"(\d)[–-](\d)", prereq_m.group(1)) for x in x] if prereq_m else []
    bad = [r for r in refs if r >= n]
    if bad:
        ok_d = False
    detail_d.append(f"P{n}<-{sorted(set(refs)) or '[]'}")
results.append(("(d) phase prerequisites form a DAG (only earlier phases referenced)",
                ok_d, "; ".join(detail_d)))

# Budget check
phase_hours = {}
for m in re.finditer(r'<a id="phase-(\d)"></a>(.*?)(?=<a id="phase-|<a id="excluded")', doc, re.S):
    n, body = int(m.group(1)), m.group(2)
    entries = [float(x) for x in re.findall(r"^- Est\. hours: ([\d.]+)", body, re.M)]
    t3 = [float(x) for x in re.findall(r"\*T3 subtotal: ([\d.]+) h\*", body)]
    phase_hours[n] = (sum(entries), sum(t3))
a_section = doc.split('<a id="appendix-a"></a>')[1].split('<a id="appendix-b"></a>')[0]
a_hours, a_p0 = 0.0, 0.0
for line in a_section.splitlines():
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) == 7 and re.fullmatch(r"A\.\d+", cells[0]):
        a_hours += float(cells[6])
        if cells[4] == "0":
            a_p0 += float(cells[6])
total = sum(e + t for e, t in phase_hours.values()) + a_hours
p0_inphase = sum(phase_hours.get(0, (0.0, 0.0)))
skip_total = total - p0_inphase - a_p0
budget = 6 * 48 * 4
slack_full = (budget - total) / budget
slack_skip = (budget - skip_total) / budget
print("BUDGET:")
for n, (e, t) in sorted(phase_hours.items()):
    print(f"  Phase {n}: entries+capstone {e:g} h + T3 {t:g} h = {e + t:g} h")
print(f"  Appendix A: {a_hours:g} h (of which Phase-0 foundations: {a_p0:g} h)")
print(f"  FULL FROM-ZERO PATH: {total:g} h vs budget {budget} h -> slack {slack_full:.1%}")
print(f"  ALL-P0-SKIPPED PATH: {skip_total:g} h -> slack {slack_skip:.1%}")
results.append(("budget: from-zero path fits budget; skipped path keeps ~15% slack",
                total <= budget and slack_full >= 0 and slack_skip >= 0.13,
                f"full={total:g}h skip={skip_total:g}h budget={budget}h slack {slack_full:.1%}/{slack_skip:.1%}"))

print("\nQA ASSERTIONS:")
all_ok = True
for name, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}\n         {detail}")
    all_ok = all_ok and ok
sys.exit(0 if all_ok else 1)
