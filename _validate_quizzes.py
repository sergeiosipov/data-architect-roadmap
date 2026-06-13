# Validates the Phase-0 quiz files in _quizzes/: exactly 100 Q/A pairs each,
# balanced Q/A, non-empty, code spans balanced. Run: uv run _validate_quizzes.py
import re
import sys
from pathlib import Path

qd = Path(__file__).parent / "_quizzes"
IDS = [f"0.{i}" for i in range(1, 13)] + [
    "1.6.1", "1.6.3", "1.7.1", "1.8.1", "1.8.9", "1.5.1",
    "3.2.1", "8.2.1", "8.2.4", "8.5.1", "1.10.1", "9.1.3"]
fail = False
total = 0

for qid in IDS:
    p = qd / f"{qid}.md"
    if not p.exists():
        print(f"[MISSING] {qid}.md")
        fail = True
        continue
    lines = p.read_text(encoding="utf-8").split("\n")
    qs = [ln for ln in lines if ln.startswith("Q:")]
    as_ = [ln for ln in lines if ln.startswith("A:")]
    # pair them in order, like the build does
    pairs, q = [], None
    for ln in lines:
        if ln.startswith("Q:"):
            q = ln[2:].strip()
        elif ln.startswith("A:") and q is not None:
            pairs.append((q, ln[2:].strip())); q = None
    empty = sum(1 for a, b in pairs if not a or not b)
    badtick = sum(1 for a, b in pairs if (a.count("`") % 2) or (b.count("`") % 2))
    dupes = len(pairs) - len({a for a, _ in pairs})
    total += len(pairs)
    probs = []
    if len(pairs) != 100: probs.append(f"{len(pairs)} pairs (want 100)")
    if len(qs) != len(as_): probs.append(f"Q lines {len(qs)} != A lines {len(as_)}")
    if empty: probs.append(f"{empty} empty Q or A")
    if badtick: probs.append(f"{badtick} unbalanced backticks")
    if dupes: probs.append(f"{dupes} duplicate questions")
    status = "OK  " if not probs else "FAIL"
    if probs: fail = True
    print(f"[{status}] {qid}.md: {len(pairs)} pairs" + ("" if not probs else " — " + "; ".join(probs)))

print(f"TOTAL: {total} questions (want 1200)")
sys.exit(1 if fail else 0)
