# Moves the 13 former Skip-List IDs into Phase 0 (with tier upgrades where teaching
# from zero merits T2) and updates the worklist footer. Run: uv run _patch_worklist_p0.py
from pathlib import Path

p = Path(__file__).parent / "_worklist.md"
t = p.read_text(encoding="utf-8")

ROWS = {
    "| 1.1.1 | Structured data | T3 | Skip | profile: 9y DE |":
        "| 1.1.1 | Structured data | T3 | P0 | taught from zero (0.7) |",
    "| 1.1.2 | Semi-structured data | T3 | Skip | profile |":
        "| 1.1.2 | Semi-structured data | T3 | P0 | taught from zero (0.7) |",
    "| 1.1.3 | Unstructured data | T3 | Skip | profile |":
        "| 1.1.3 | Unstructured data | T3 | P0 | taught from zero (0.7) |",
    "| 1.2.1 | Batch paradigm | T3 | Skip | profile: daily work |":
        "| 1.2.1 | Batch paradigm | T3 | P0 | taught from zero (0.8) |",
    "| 1.3.1 | OLTP | T3 | Skip | profile |":
        "| 1.3.1 | OLTP | T2 | P0 | taught from zero (0.8) |",
    "| 1.3.2 | OLAP | T3 | Skip | profile |":
        "| 1.3.2 | OLAP | T2 | P0 | taught from zero (0.8) |",
    "| 5.4.2 | Code-first wrangling | T3 | Skip | pandas: profile |":
        "| 5.4.2 | Code-first wrangling | T2 | P0 | pandas from zero (0.9) |",
    "| 9.1.1 | IDEs | T3 | Skip | profile |":
        "| 9.1.1 | IDEs | T3 | P0 | taught from zero (0.10) |",
    "| 9.1.2 | Notebooks | T3 | Skip | profile |":
        "| 9.1.2 | Notebooks | T3 | P0 | taught from zero (0.10) |",
    "| 9.2.1 | Git hosting | T3 | Skip | profile |":
        "| 9.2.1 | Git & hosting | T2 | P0 | taught from zero (0.4) |",
    "| 9.4.1 | Unit testing | T3 | Skip | pytest: profile |":
        "| 9.4.1 | Unit testing | T2 | P0 | taught from zero (0.11) |",
    "| 9.5.1 | Code review | T3 | Skip | profile |":
        "| 9.5.1 | Code review | T3 | P0 | taught from zero (0.12) |",
    "| 14.5.2 | Self-hosted notebooks | T3 | Skip | JupyterLab: profile |":
        "| 14.5.2 | Self-hosted notebooks | T3 | P0 | taught from zero (0.9) |",
}
for old, new in ROWS.items():
    assert old in t, f"row not found: {old}"
    t = t.replace(old, new)

OLD_FOOT = """Tier counts (script-verified): T1=48 (19.0%) · T2=104 (41.3%) · T3=95 (37.7%, of which 13 Skip) · Excluded=5 · Total=252 · 0 duplicate IDs.
Per-phase T1 (script-verified): P1=10 · P2=9 · P3=2 · P4=12 · P5=4 · P6=8 · P7=0 · P8=3.
Phase rows: P1=26 · P2=33 · P3=16 · P4=40 · P5=31 · P6=38 · P7=19 · P8=31 · Skip=13 · Excluded=5."""
NEW_FOOT = """Tier counts (script-verified): T1=48 (19.0%) · T2=109 (43.3%) · T3=90 (35.7%) · Excluded=5 · Total=252 · 0 duplicate IDs.
Per-phase T1 (script-verified): P0=0 · P1=10 · P2=9 · P3=2 · P4=12 · P5=4 · P6=8 · P7=0 · P8=3.
Phase rows: P0=13 · P1=26 · P2=33 · P3=16 · P4=40 · P5=31 · P6=38 · P7=19 · P8=31 · Excluded=5.
Phase 0 added on user instruction (2026-06-12): no profile-based skipping; each P0 module
carries a skip test. Non-taxonomy basics live in Appendix A as A.27-A.31."""
assert OLD_FOOT in t
t = t.replace(OLD_FOOT, NEW_FOOT)

p.write_text(t, encoding="utf-8")

# verify
import re
rows = [tuple(s.strip() for s in m.groups()) for m in re.finditer(
    r"^\| (\d+\.\d+\.\d+) \| (.+?) \| (.+?) \| (.+?) \|", t, re.M)]
tiers, phases = {}, {}
for _, _, tier, ph in rows:
    tiers[tier] = tiers.get(tier, 0) + 1
    phases[ph] = phases.get(ph, 0) + 1
print(f"rows={len(rows)} unique={len({r[0] for r in rows})}")
print("tiers:", dict(sorted(tiers.items())))
print("phases:", dict(sorted(phases.items())))
assert len(rows) == 252 and "Skip" not in phases and phases.get("P0") == 13
print("worklist patched OK")
