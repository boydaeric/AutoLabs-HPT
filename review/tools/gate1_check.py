"""Gate 1: show that the only differences between article_v7.md and
article_v8.md are the listed edits (make_v8.EDITS, items a–c).

Independent of make_v8.build: diffs v7 against v8 at character level,
then requires every changed hunk to fall inside exactly one listed edit,
and every listed edit to produce at least one hunk.

Usage: python review/tools/gate1_check.py
"""
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_v8 import EDITS  # noqa: E402

REVIEW = Path(__file__).resolve().parents[1]
v7 = (REVIEW / "article_v7.md").read_text(encoding="utf-8")
v8 = (REVIEW / "article_v8.md").read_text(encoding="utf-8")

# Locate each edit's span in v7 and v8.
spans7, spans8 = {}, {}
pos_shift = 0
for eid, part, old, new in EDITS:
    assert v7.count(old) == 1, f"{eid}: not unique in v7"
    spans7[eid] = (v7.index(old), v7.index(old) + len(old))
for eid, part, old, new in EDITS:
    if new:
        # the new string must occur in v8 (once, or locate by context)
        assert v8.count(new) >= 1, f"{eid}: new text missing from v8"

sm = difflib.SequenceMatcher(a=v7, b=v8, autojunk=False)
hunks = [op for op in sm.get_opcodes() if op[0] != "equal"]
fail = False
hit = {eid: 0 for eid, *_ in EDITS}
for tag, i1, i2, j1, j2 in hunks:
    # A hunk may span adjacent edits (e.g. Y4 deletes the text just before
    # Y5's span); it must lie inside one run of contiguous edit spans.
    owners = [eid for eid, (s, e) in spans7.items() if s < max(i2, i1 + 1) and i1 < e]
    lo = min((spans7[o][0] for o in owners), default=None)
    hi = max((spans7[o][1] for o in owners), default=None)
    contiguous = owners and all(
        any(spans7[o][1] == spans7[p][0] for p in owners) or spans7[o][1] == hi
        for o in owners)
    old_s, new_s = v7[i1:i2], v8[j1:j2]
    if not (contiguous and lo <= i1 and i2 <= hi):
        fail = True
        print(f"UNLISTED change at v7[{i1}:{i2}]: {old_s!r} -> {new_s!r}")
    else:
        for o in owners:
            hit[o] += 1
        print(f"{'+'.join(owners)}: {old_s[:70]!r} -> {new_s[:70]!r}")

for eid, n in hit.items():
    if n == 0:
        fail = True
        print(f"Listed edit {eid} produced no change")

# Cross-check: placeholders and tags
ph = lambda s: re.findall(r"\[Figure (\d+)\]", s)
print("v7 figure placeholders:", ph(v7), "| v8:", ph(v8))
assert ph(v8) == ["1", "2", "3", "4", "5"], "v8 placeholders not 1-5 in order"
for tag in ("[E]", "[I]", "[C]", "[DATE]", "[DATE SENT]"):
    print(f"{tag}: v7 {v7.count(tag)}, v8 {v8.count(tag)}")
assert v8.count("[E]") == v7.count("[E]") - 1 and v8.count("[I]") == v7.count("[I]") + 1
assert v8.count("[DATE SENT]") == 0 and v8.count("[proposed title]") == 0
assert v8.count("Prepared by: Eric Boyda") == 1

print("\nGATE 1:", "FAIL" if fail else f"PASS ({len(hunks)} hunks, all inside the {len(EDITS)} listed edits; every listed edit applied)")
sys.exit(1 if fail else 0)
