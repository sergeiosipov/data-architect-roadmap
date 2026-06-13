# Validates the expanded lesson format in _parts/0*-phase*.md.
# Run: uv run _validate_expansion.py
import re
import sys
from pathlib import Path

parts = Path(__file__).parent / "_parts"
FILES = ["00b-phase0.md", "01-phase1.md", "02-phase2.md", "03-phase3.md", "04-phase4.md",
         "05-phase5.md", "06-phase6.md", "07-phase7.md", "08-phase8.md"]
LINK = re.compile(r"\[[^\]]+\]\(https?://[^)]+\)")
hard_fail = False

for fname in FILES:
    text = (parts / fname).read_text(encoding="utf-8")
    probs = []
    entries = list(re.finditer(r"^#### (.+?)$\n((?:(?!^#{3,4} ).*\n?)*)", text, re.M))
    n_cov = n_learn = 0
    for m in entries:
        head, body = m.group(1).strip(), m.group(2)
        if not re.search(r"^- \*\*Why:\*\*", body, re.M):
            probs.append(f"no Why: {head[:50]}")
        learn = re.search(r"^- \*\*Learn:\*\*\s*\n((?:[ \t]+-.*\n?)+)", body, re.M)
        if not learn:
            probs.append(f"Learn not a sub-list: {head[:50]}")
        else:
            bullets = re.findall(r"^[ \t]+- ", learn.group(1), re.M)
            if len(bullets) < 3:
                probs.append(f"Learn <3 bullets: {head[:50]}")
            n_learn += len(bullets)
            n_cov += len(re.findall(r"\*\([^)]+\)\*", learn.group(1)))
        res = re.search(r"^- \*\*Resources:\*\*\s*\n((?:[ \t]+-.*\n?)+)", body, re.M)
        if not res:
            probs.append(f"no Resources list: {head[:50]}")
        elif len(LINK.findall(res.group(1))) < 2:
            probs.append(f"Resources <2 links: {head[:50]}")
        tools = re.search(r"^- \*\*Tools:\*\*\s*\n?((?:[ \t]+-.*\n?)*)", body, re.M)
        if tools and tools.group(1) and not LINK.search(tools.group(1)):
            probs.append(f"Tools list without links: {head[:50]}")
        if not re.search(r"^- \*\*Do:\*\*", body, re.M):
            probs.append(f"no Do: {head[:50]}")
        if not re.search(r"^- \*\*Done when:\*\*", body, re.M):
            probs.append(f"no Done when: {head[:50]}")
        if not re.search(r"^- Est\. hours: (\d|counted as A\.)", body, re.M):
            probs.append(f"no Est. hours: {head[:50]}")
    # T3 table rows should link in the Read column
    t3 = re.search(r"^### T3 awareness topics\n((?:(?!^### ).*\n?)*)", text, re.M)
    t3_rows = t3_linked = 0
    if t3:
        for row in re.findall(r"^\| \d+\.\d+\.\d+ \|.*\|$", t3.group(1), re.M):
            t3_rows += 1
            if LINK.search(row):
                t3_linked += 1
    cov_pct = round(100 * n_cov / n_learn) if n_learn else 0
    status = "OK " if not probs else "FAIL"
    if probs:
        hard_fail = True
    print(f"[{status}] {fname}: {len(entries)} entries, learn-coverage tags {cov_pct}% "
          f"({n_cov}/{n_learn}), T3 links {t3_linked}/{t3_rows}"
          + ("" if not probs else "\n        " + "\n        ".join(probs[:12])))
    if cov_pct < 70 and n_learn:
        hard_fail = True
        print(f"        coverage below 70% threshold")

sys.exit(1 if hard_fail else 0)
