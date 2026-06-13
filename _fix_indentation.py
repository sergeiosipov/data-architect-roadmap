# Converts 2-space nested-list indentation to 4-space in the phase files, so nested
# lists render correctly in python-markdown (the app) as well as on GitHub.
# Idempotent: only matches lines whose marker sits exactly at column 2.
# Run: uv run _fix_indentation.py
import re
from pathlib import Path

parts = Path(__file__).parent / "_parts"
FILES = ["00b-phase0.md", "01-phase1.md", "02-phase2.md", "03-phase3.md", "04-phase4.md",
         "05-phase5.md", "06-phase6.md", "07-phase7.md", "08-phase8.md"]

# 2 leading spaces immediately followed by a list marker: "- ", "* ", "+ ", "N. ", "- [ ]"
NESTED = re.compile(r"^  (?=(?:[-*+] |\d+\. ))")

total = 0
for fname in FILES:
    p = parts / fname
    lines = p.read_text(encoding="utf-8").split("\n")
    changed = 0
    for i, line in enumerate(lines):
        if NESTED.match(line):
            lines[i] = "  " + line  # 2 -> 4
            changed += 1
    p.write_text("\n".join(lines), encoding="utf-8")
    total += changed
    print(f"{fname}: {changed} nested-list lines re-indented to 4 spaces")
print(f"TOTAL: {total} lines (expected ~2099)")
