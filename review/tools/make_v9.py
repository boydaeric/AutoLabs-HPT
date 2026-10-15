"""Build review/article_v9.md from review/article_v8.md.

Four tables become figure placeholders (sec. 1 threshold schedule, sec. 3
reductions, sec. 4 steps, App. D range). Each caption is the table's header
cells, verbatim and in order: the first cell, ": ", the other cells joined
by "; ", and a full stop. The source note under each table stays as it is,
directly below the placeholder. Figures are renumbered 1-9 in order of
appearance. Every old string is asserted to occur exactly once.

EDITS and TABLES are imported by gate1_check_v9.py and build_figure_data.py.

Usage: python review/tools/make_v9.py
"""
import re
from pathlib import Path

REVIEW = Path(__file__).resolve().parents[1]

# first header cell of each converted table -> new figure number
TABLES = {
    "a": ("**Federal fiscal year (begins October 1 of the prior year)**", 1),
    "b": ("**Reduction in Medicaid spending, central estimate, 2026–2035, billions of 2026 dollars**", 3),
    "c": ("**Central estimate, 2026–2035**", 4),
    "d": ("**Loss to providers, billions of 2026 dollars, 2026–2035**", 9),
}
# existing placeholders: old number -> new number (order of appearance)
RENUMBER = {1: 2, 2: 5, 3: 6, 4: 7, 5: 8}


def table_block(text, first_cell):
    """Return the exact markdown table (consecutive '|' lines) whose header starts with first_cell."""
    lines = text.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith("| " + first_cell)]
    assert len(starts) == 1, (first_cell, starts)
    i = j = starts[0]
    while j < len(lines) and lines[j].startswith("|"):
        j += 1
    return "\n".join(lines[i:j])


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def caption(block):
    head = [re.sub(r"^\*\*(.*)\*\*$", r"\1", c) for c in cells(block.split("\n")[0])]
    return head[0] + ": " + "; ".join(head[1:]) + "."


def edits(v8):
    out = []
    for key, (first, n) in TABLES.items():
        block = table_block(v8, first)
        out.append((f"Z-{key}", "swap", block, f"*[Figure {n}] {caption(block)}*"))
    for old, new in RENUMBER.items():
        line = next(l for l in v8.split("\n") if l.startswith(f"*[Figure {old}] "))
        out.append((f"Z-r{old}", "renumber", line, line.replace(f"[Figure {old}]", f"[Figure {new}]", 1)))
    return out


def build(v8):
    text = v8
    for eid, _, old, new in edits(v8):
        assert text.count(old) == 1, f"{eid}: old string occurs {text.count(old)} times"
        text = text.replace(old, new)
    return text


if __name__ == "__main__":
    v8 = (REVIEW / "article_v8.md").read_text(encoding="utf-8")
    v9 = build(v8)
    (REVIEW / "article_v9.md").write_text(v9, encoding="utf-8")
    for eid, kind, old, new in edits(v8):
        print(eid, kind, "->", new[:110])
