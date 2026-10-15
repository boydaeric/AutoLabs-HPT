"""Build review/article_v8.md from review/article_v7.md.

Every edit is an exact (old, new) string pair. Each old string is asserted
to occur exactly once in v7 before it is replaced. EDITS is also imported by
gate1_check.py, which proves these are the only differences.

Usage: python review/tools/make_v8.py
"""
from pathlib import Path

REVIEW = Path(__file__).resolve().parents[1]

# (id, part of the instruction, old, new)
EDITS = [
    # a. Eric's text edits (Exposure-Not-Loss-v18-draft.docx, his copy)
    ("Y1", "a",
     "Under Two Proposed Rules [proposed title]**",
     "Under Two Proposed Rules**"),
    ("Y2", "a",
     "request for confirmation, sent [DATE SENT], as of [DATE].",
     "request for confirmation, sent September 28, 2026, as of [DATE]."),
    # b. Figure plan
    ("Y3", "b",
     "*THEIA Services · Public note · September 6, 2026; revised [DATE]*\n",
     "*THEIA Services · Public note · September 6, 2026; revised [DATE]*\n\n"
     "*Prepared by: Eric Boyda*\n"),
    ("Y4", "b",
     "*[Figure 2] The provider tax rule’s net effect on providers: −$220.3 billion "
     "measured alone, +$21.7 billion after counting the SDP rule’s cuts first.*\n\n",
     ""),
    ("Y5", "b", "*[Figure 3] From −$220.3 billion", "*[Figure 2] From −$220.3 billion"),
    ("Y6", "b", "*[Figure 6] Which parts", "*[Figure 3] Which parts"),
    ("Y7", "b", "*[Figure 7] Pediatric inpatient", "*[Figure 4] Pediatric inpatient"),
    ("Y8", "b", "*[Figure 8] Psychiatric beds", "*[Figure 5] Psychiatric beds"),
    # c. Appendix I, comment counts: tag only
    ("Y9", "c",
     "CMS-2452-P (docket CMS-2026-2476), 214 as filed / 213 corrected "
     "(188 / 187 distinct texts). [E]",
     "CMS-2452-P (docket CMS-2026-2476), 214 as filed / 213 corrected "
     "(188 / 187 distinct texts). [I]"),
]


def build(text):
    for eid, _, old, new in EDITS:
        n = text.count(old)
        assert n == 1, f"{eid}: old string occurs {n} times"
        text = text.replace(old, new)
    return text


if __name__ == "__main__":
    v7 = (REVIEW / "article_v7.md").read_text(encoding="utf-8")
    (REVIEW / "article_v8.md").write_text(build(v7), encoding="utf-8")
    print(f"article_v8.md written; {len(EDITS)} edits applied")
