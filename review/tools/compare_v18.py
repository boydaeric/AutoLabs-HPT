"""Compare two .docx files paragraph by paragraph (text only).

Usage: python compare_v18.py REPO_DOCX ERIC_DOCX

Prints every paragraph (body paragraphs and table cells, in document order)
whose text differs, with a word-level diff. Formatting is ignored.
"""
import difflib
import sys

from docx import Document
from docx.oxml.ns import qn


def paragraphs(path):
    doc = Document(path)
    out = []
    for block in doc.element.body.iter():
        if block.tag == qn("w:p"):
            text = "".join(t.text or "" for t in block.iter(qn("w:t")))
            out.append(text)
    return out


def main(a_path, b_path):
    a, b = paragraphs(a_path), paragraphs(b_path)
    print(f"repo paragraphs: {len(a)}; Eric paragraphs: {len(b)}")
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    n = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        n += 1
        print(f"\n=== change {n}: {op} repo[{i1}:{i2}] Eric[{j1}:{j2}]")
        old = " ".join(a[i1:i2]).split(" ")
        new = " ".join(b[j1:j2]).split(" ")
        wsm = difflib.SequenceMatcher(a=old, b=new, autojunk=False)
        for wop, x1, x2, y1, y2 in wsm.get_opcodes():
            if wop != "equal":
                ctx = " ".join(old[max(0, x1 - 6):x1])
                print(f"  {wop}: …{ctx} [{' '.join(old[x1:x2])}] -> [{' '.join(new[y1:y2])}]")
    print(f"\n{n} changed paragraph block(s)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
