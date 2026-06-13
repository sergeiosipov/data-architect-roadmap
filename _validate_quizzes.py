# Validates every quiz file in _quizzes/: exactly 100 Q/A pairs each, balanced Q/A,
# non-empty, balanced code spans, no duplicate questions, single-line Q and A.
# Also reports completeness: which phase-0..8 lessons still lack a quiz file.
# Run: uv run _validate_quizzes.py
import re
import sys
from pathlib import Path

root = Path(__file__).parent
qd = root / "_quizzes"
parts = root / "_parts"
ID_RX = re.compile(r"\b(?:\d+\.\d+(?:\.\d+)?|A\.\d+)\b")


def lesson_ids_for(fname: str) -> list[str]:
    text = (parts / fname).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"^#### (.+?)$\n", text, re.M):
        ids = ID_RX.findall(m.group(1).strip())
        if ids:
            out.append(ids[0])
    return out


PHASE_FILES = {
    0: "00b-phase0.md", 1: "01-phase1.md", 2: "02-phase2.md", 3: "03-phase3.md",
    4: "04-phase4.md", 5: "05-phase5.md", 6: "06-phase6.md", 7: "07-phase7.md",
    8: "08-phase8.md",
}
expected = {n: lesson_ids_for(f) for n, f in PHASE_FILES.items()}
all_expected = [i for ids in expected.values() for i in ids]

# Validate every quiz file that exists, in lesson order then any extras.
present = {p.stem for p in qd.glob("*.md")}
ordered = [i for i in all_expected if i in present]
extras = sorted(present - set(all_expected))
IDS = ordered + extras

fail = False
total = 0
for qid in IDS:
    p = qd / f"{qid}.md"
    lines = p.read_text(encoding="utf-8").split("\n")
    qs = [ln for ln in lines if ln.startswith("Q:")]
    as_ = [ln for ln in lines if ln.startswith("A:")]
    pairs, q = [], None
    for ln in lines:
        if ln.startswith("Q:"):
            q = ln[2:].strip()
        elif ln.startswith("A:") and q is not None:
            pairs.append((q, ln[2:].strip())); q = None
    empty = sum(1 for a, b in pairs if not a or not b)
    badtick = sum(1 for a, b in pairs if (a.count("`") % 2) or (b.count("`") % 2))
    dbl = sum(1 for a, b in pairs if "``" in a or "``" in b)
    dupes = len(pairs) - len({a for a, _ in pairs})
    total += len(pairs)
    probs = []
    if len(pairs) != 100: probs.append(f"{len(pairs)} pairs (want 100)")
    if len(qs) != len(as_): probs.append(f"Q lines {len(qs)} != A lines {len(as_)}")
    if empty: probs.append(f"{empty} empty Q or A")
    if badtick: probs.append(f"{badtick} unbalanced backticks")
    if dbl: probs.append(f"{dbl} double-backtick spans")
    if dupes: probs.append(f"{dupes} duplicate questions")
    status = "OK  " if not probs else "FAIL"
    if probs: fail = True
    print(f"[{status}] {qid}.md: {len(pairs)} pairs" + ("" if not probs else " — " + "; ".join(probs)))

print(f"TOTAL: {total} questions across {len(IDS)} quiz files")

# Completeness report (informational unless --strict): phases 1-8 lessons missing a quiz.
strict = "--strict" in sys.argv
for n in range(1, 9):
    missing = [i for i in expected[n] if i not in present]
    if missing:
        print(f"[INCOMPLETE] Phase {n}: {len(expected[n]) - len(missing)}/{len(expected[n])} lessons have quizzes; missing: {missing}")
        if strict:
            fail = True

sys.exit(1 if fail else 0)
