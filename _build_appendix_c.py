# Generates _parts/12-appendix-c.md from _worklist.md (run: uv run _build_appendix_c.py)
import re
from pathlib import Path

root = Path(__file__).parent
rows = []
for line in (root / "_worklist.md").read_text(encoding="utf-8").splitlines():
    m = re.match(r"^\| (\d+\.\d+\.\d+) \| (.+?) \| (.+?) \| (.+?) \|", line)
    if m:
        rows.append(tuple(s.strip() for s in m.groups()))

assert len(rows) == 252, f"expected 252 rows, got {len(rows)}"
assert len({r[0] for r in rows}) == 252, "duplicate IDs"

PHASE = {f"P{i}": f"Phase {i}" for i in range(0, 9)} | {"Excluded": "Excluded"}

out = [
    '<a id="appendix-c"></a>',
    "## Appendix C — Coverage Matrix",
    "",
    "All 252 taxonomy subcategory IDs, each exactly once. IDs follow the canonical parse:",
    "subcategory = bold bullet item; concept categories 1.8/1.9 per concept; 1.10 as one",
    "unit; 1.11 as 3 groups; 1.12 per standard; the taxonomy's own cross-reference pointers",
    "(5.5, 6.5, 10.8) carry IDs and are resolved in [Excluded](#excluded). Gap additions",
    "A.1–A.31 are tracked in [Appendix A](#appendix-a). Tier `—` = excluded item. Phase 0",
    "items are taught from zero and individually skippable via the Skip List tests.",
    "",
    "| Taxonomy ID | Topic | Tier | Phase |",
    "|---|---|---|---|",
]
counts = {}
for id_, topic, tier, phase in rows:
    ph = PHASE[phase]
    counts[ph] = counts.get(ph, 0) + 1
    out.append(f"| {id_} | {topic} | {tier} | {ph} |")

out.append("")
total = sum(counts.values())
dist = " · ".join(f"{k}: {v}" for k, v in sorted(counts.items()))
out.append(f"**Coverage: {total}/252 IDs.** {dist}.")
out.append("")

(root / "_parts" / "12-appendix-c.md").write_text("\n".join(out), encoding="utf-8")
print(f"rows={total}  unique=252  dist: {dist}")
