# Renumbers phase month ranges after inserting Phase 0 and points Phase 1's
# prerequisites at Phase 0. Run: uv run _patch_months.py
from pathlib import Path

parts = Path(__file__).parent / "_parts"
EDITS = {
    "01-phase1.md": [
        ("## Phase 1: Distributed Data Systems & Modeling Core (months 1–6, 118 h)",
         "## Phase 1: Distributed Data Systems & Modeling Core (months 7–11, 118 h)"),
        ("**Entry prerequisites:** none beyond the profile (Python, SQL, Git, Docker basics).",
         "**Entry prerequisites:** Phase 0 — or its skip tests passed (Linux/shell, Python, SQL, Git, Docker, networking)."),
    ],
    "02-phase2.md": [
        ("## Phase 2: Lakehouse & Analytics Engineering (months 7–12, 123 h)",
         "## Phase 2: Lakehouse & Analytics Engineering (months 12–16, 123 h)"),
    ],
    "03-phase3.md": [
        ("## Phase 3: Distributed Compute, Orchestration & Engineering Practice (months 13–18, 118 h)",
         "## Phase 3: Distributed Compute, Orchestration & Engineering Practice (months 17–21, 118 h)"),
    ],
    "04-phase4.md": [
        ("## Phase 4: Streaming & Event-Driven Integration (months 19–24, 119 h)",
         "## Phase 4: Streaming & Event-Driven Integration (months 22–27, 119 h)"),
    ],
    "05-phase5.md": [
        ("## Phase 5: Cloud Platform Architecture & Operations — Azure (months 25–30, 108 h + 27 h Appendix A)",
         "## Phase 5: Cloud Platform Architecture & Operations — Azure (months 28–33, 108 h + 27 h Appendix A)"),
    ],
    "06-phase6.md": [
        ("## Phase 6: Governance, Security & Compliance (months 31–36, 120 h + 14 h Appendix A)",
         "## Phase 6: Governance, Security & Compliance (months 34–39, 120 h + 14 h Appendix A)"),
    ],
    "07-phase7.md": [
        ("## Phase 7: AI/ML & LLM Platforms for Fund Data (months 37–42, 74 h + 2 h Appendix A)",
         "## Phase 7: AI/ML & LLM Platforms for Fund Data (months 40–43, 74 h + 2 h Appendix A)"),
    ],
    "08-phase8.md": [
        ("## Phase 8: Data Products, Semantic Layer & the Architect's Practice (months 43–48, 103 h + 18.5 h Appendix A)",
         "## Phase 8: Data Products, Semantic Layer & the Architect's Practice (months 44–48, 103 h + 18.5 h Appendix A)"),
    ],
}
for fname, edits in EDITS.items():
    p = parts / fname
    t = p.read_text(encoding="utf-8")
    for old, new in edits:
        assert old in t, f"{fname}: not found: {old[:60]}…"
        t = t.replace(old, new)
    p.write_text(t, encoding="utf-8")
    print(f"patched {fname} ({len(edits)} edit(s))")
print("months renumbered OK")
