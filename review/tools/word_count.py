"""Body and appendix word counts for an article_vN.md file.

Method (as in decision_log.md since v4): whitespace tokens that contain a
letter or digit; the body runs from the title through sec. 9 (everything
before "# Appendix"), with table cells, figure captions and evidence tags
counted; the appendix is everything after the "# Appendix" heading.

Usage: python word_count.py review/article_v8.md [...]
"""
import re
import sys

CAP = 6284


def counts(text):
    body, _, appendix = text.partition("\n# Appendix\n")
    n = lambda s: sum(1 for t in s.split() if re.search(r"[A-Za-z0-9]", t))
    return n(body), n(appendix)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        b, a = counts(open(path, encoding="utf-8").read())
        print(f"{path}: body {b:,} ({b - CAP:+,} against the {CAP:,} cap); appendix {a:,}")
