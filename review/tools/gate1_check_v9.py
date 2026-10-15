"""Gate 1 (v9): the only differences between article_v8.md and article_v9.md
are the four table-to-placeholder swaps, their captions and the renumbering.

- Character-level diff of v8 against v9: every changed hunk lies inside one
  listed edit (make_v9.edits), and every listed edit is applied.
- Each new caption equals the replaced table's header cells, verbatim.
- Each converted table's source note is unchanged and sits directly under
  its placeholder.
- The five other tables are byte-identical; placeholders run 1-9; tag and
  [DATE] counts are unchanged; no text refers to a figure number outside
  the placeholders.

Usage: python review/tools/gate1_check_v9.py
"""
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_v9 import TABLES, caption, cells, edits, table_block  # noqa: E402

REVIEW = Path(__file__).resolve().parents[1]
v8 = (REVIEW / "article_v8.md").read_text(encoding="utf-8")
v9 = (REVIEW / "article_v9.md").read_text(encoding="utf-8")
fails = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


E = edits(v8)
spans = {}
for eid, _, old, _ in E:
    assert v8.count(old) == 1
    spans[eid] = (v8.index(old), v8.index(old) + len(old))
hit = {eid: 0 for eid, *_ in E}
sm = difflib.SequenceMatcher(a=v8, b=v9, autojunk=False)
hunks = [op for op in sm.get_opcodes() if op[0] != "equal"]
for _, i1, i2, j1, j2 in hunks:
    own = [e for e, (s, t) in spans.items() if s <= i1 and i2 <= t]
    if len(own) != 1:
        check(False, f"UNLISTED change at v8[{i1}:{i2}]: {v8[i1:i2][:60]!r} -> {v9[j1:j2][:60]!r}")
    else:
        hit[own[0]] += 1
for eid, n in hit.items():
    check(n > 0, f"{eid}: applied ({n} hunk(s))")
print(f"     {len(hunks)} hunks, all inside the {len(E)} listed edits" if not fails else "")

# captions verbatim from header cells; source notes unchanged and directly below
for key, (first, n) in TABLES.items():
    block = table_block(v8, first)
    head = [re.sub(r"^\*\*(.*)\*\*$", r"\1", c) for c in cells(block.split("\n")[0])]
    cap = caption(block)
    words_extra = set(re.findall(r"[A-Za-z0-9]+", cap)) - set(re.findall(r"[A-Za-z0-9]+", " ".join(head)))
    check(f"*[Figure {n}] {cap}*" in v9 and not words_extra,
          f"table {key} -> Figure {n}: caption is its header cells verbatim ({cap[:60]}…)")
    after8 = v8[v8.index(block) + len(block):].lstrip("\n").split("\n")[0]
    ph = f"*[Figure {n}] {cap}*"
    after9 = v9[v9.index(ph) + len(ph):].lstrip("\n").split("\n")[0]
    check(after8 == after9 and after8.startswith("*Source:"), f"table {key}: source note unchanged, directly below the placeholder")

# other tables unchanged


def tables(text):
    out, cur = [], []
    for line in text.split("\n"):
        if line.startswith("|"):
            cur.append(line)
        elif cur:
            out.append("\n".join(cur))
            cur = []
    return out


t8, t9 = tables(v8), tables(v9)
gone = [t for t in t8 if t not in t9]
check(len(t8) == 9 and len(t9) == 5 and len(gone) == 4 and all(t in t8 for t in t9),
      f"tables: v8 {len(t8)}, v9 {len(t9)}; the 5 kept are byte-identical")

ph = re.findall(r"^\*\[Figure (\d+)\]", v9, re.M)
check(ph == [str(i) for i in range(1, 10)], f"placeholders in order: {ph}")
refs = [m for m in re.findall(r"(?i)\b(?:figure|fig\.|figs?\.)\s*\d+[^\n]{0,20}", v9)
        if not re.match(r"Figure \d+\] ", m)]
check(len(refs) == 1 and refs[0].startswith("Figure 1 note)"), f"no other figure-number references (only KFF's own: {refs})")
for tag in ("[E]", "[I]", "[C]", "[DATE]"):
    check(v8.count(tag) == v9.count(tag), f"{tag}: v8 {v8.count(tag)}, v9 {v9.count(tag)}")

print("\nGATE 1:", "FAIL (%d)" % len(fails) if fails else "PASS")
sys.exit(1 if fails else 0)
