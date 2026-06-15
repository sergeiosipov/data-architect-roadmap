# Deterministic audit of the _quizzes/*.md bank: cross-lesson duplicate questions,
# within-lesson near-duplicates, thin answers, and aggregate stats. No agent tokens.
# Run: uv run _audit_questions.py
# ponytail: normalized-string match, not semantic. Ceiling: catches lexical dupes /
# trivially-reworded ones, not paraphrases; upgrade path is an embedding pass if needed.
import re
from collections import Counter, defaultdict
from pathlib import Path

qd = Path(__file__).parent / "_quizzes"


def parse(p):
    pairs, q = [], None
    for ln in p.read_text(encoding="utf-8").split("\n"):
        if ln.startswith("Q:"):
            q = ln[2:].strip()
        elif ln.startswith("A:") and q is not None:
            pairs.append((q, ln[2:].strip())); q = None
    return pairs


def norm(s):
    s = s.lower().replace("`", "")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


files = sorted(qd.glob("*.md"))
by_norm = defaultdict(list)      # normalized Q -> [(lesson, idx, rawQ)]
ans_lens, q_lens = [], []
thin, within_dupe = [], defaultdict(int)
total = 0
for f in files:
    lid = f.stem
    seen = set()
    for i, (q, a) in enumerate(parse(f), 1):
        total += 1
        n = norm(q)
        by_norm[n].append((lid, i, q))
        if n in seen:
            within_dupe[lid] += 1
        seen.add(n)
        ans_lens.append(len(a)); q_lens.append(len(q))
        if len(a) < 160:
            thin.append((lid, i, len(a), q[:60]))

cross = {n: v for n, v in by_norm.items() if len({x[0] for x in v}) > 1}
print(f"== Question bank audit: {total} questions across {len(files)} lessons ==\n")

print(f"CROSS-LESSON duplicate questions (same normalized text in >1 lesson): {len(cross)} clusters")
for n, v in sorted(cross.items(), key=lambda kv: -len(kv[1]))[:20]:
    lessons = ", ".join(sorted({x[0] for x in v}))
    print(f"  [{len(v)}x] \"{v[0][2][:70]}\"  in: {lessons}")

wd = {k: v for k, v in within_dupe.items() if v}
print(f"\nWITHIN-LESSON near-duplicate questions (normalized): {sum(wd.values())} in {len(wd)} lessons")
for lid, c in sorted(wd.items(), key=lambda kv: -kv[1])[:15]:
    print(f"  {lid}: {c}")

print(f"\nANSWER length: min={min(ans_lens)} median~{sorted(ans_lens)[len(ans_lens)//2]} max={max(ans_lens)} mean={sum(ans_lens)//len(ans_lens)}")
print(f"THIN answers (<160 chars): {len(thin)} ({100*len(thin)//total}%)")
for lid, i, ln, q in thin[:12]:
    print(f"  {lid}#{i} ({ln}c): {q}")

# formulaic openings
openers = Counter(norm(q).split(" ")[0] + " " + (norm(q).split(" ")[1] if len(norm(q).split(" "))>1 else "") for v in by_norm.values() for _,_,q in v)
print("\nMost common question openers (monotony check):")
for w, c in openers.most_common(12):
    print(f"  {c:5d}  {w}…")
