#!/usr/bin/env python3
"""Show the source context for evidence-ledger rows so a reviewer can verify them.

usage: verify_ledger_context.py ROW [ROW ...] [--render DIR]

For each ledger row (the `ledger_row` column; 1-based data-row index in older ledgers): locates the page of the source PDF whose text layer
contains the excerpt (falls back to the figure itself), prints ~700 characters of
surrounding text, and with --render writes a PNG of that page for visual checking
(needed for rows whose text exists only in OCR output).
"""
import csv
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path

LEDGER = Path("output/evidence_ledger_delta.csv")


def norm(s):
    return re.sub(r"[^a-z0-9$%.]+", " ", s.lower()).strip()


@lru_cache(maxsize=None)
def pdf_pages(path):
    out = subprocess.run(["pdftotext", path, "-"], capture_output=True, text=True, timeout=300).stdout
    pages = out.split("\f")
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout).group(1))
    return (pages + [""] * n)[:n]


@lru_cache(maxsize=None)
def ocr_page(path, page):
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-r", "200", "-f", str(page), "-l", str(page), "-png", "-singlefile", path, f"{td}/p"],
                       capture_output=True)
        r = subprocess.run(["tesseract", f"{td}/p.png", "stdout"], capture_output=True, timeout=300)
    return r.stdout.decode("utf-8", "replace")


def docx_text(path):
    import docx
    d = docx.Document(path)
    return "\n".join([p.text for p in d.paragraphs] + [c.text for t in d.tables for row in t.rows for c in row.cells])


def find(text_pages, claim, fig):
    words = norm(claim.strip("“”…")).split()
    keys = [" ".join(words[i:i + 6]) for i in range(0, max(1, len(words) - 5), 3)]
    nf = norm(fig)
    # prefer the page holding both an excerpt shingle and the figure: short generic shingles
    # ("the excess burden of taxation by") can also occur on earlier pages
    for need_fig in (True, False):
        for pi, t in enumerate(text_pages, 1):
            nt = norm(t)
            if need_fig and nf not in nt:
                continue
            for k in keys:
                if k and k in nt:
                    return pi, t, "excerpt"
    for pi, t in enumerate(text_pages, 1):
        if nf and nf in norm(t):
            return pi, t, "figure only"
    return None, "", "not found"


def context(t, fig, claim):
    flat = re.sub(r"\s+", " ", t)
    i = flat.find(fig)
    if i < 0:
        w = norm(claim.strip("“”…")).split()[:4]
        i = norm(flat).find(" ".join(w))
    i = max(i, 0)
    return flat[max(0, i - 450):i + 350]


def main():
    args = sys.argv[1:]
    render = None
    if "--render" in args:
        render = args[args.index("--render") + 1]
        args = args[:args.index("--render")]
    rows = list(csv.DictReader(LEDGER.open(newline="", encoding="utf-8")))
    by_row = {int(r["ledger_row"]): r for r in rows} if "ledger_row" in rows[0] else dict(enumerate(rows, 1))
    for a in args:
        n = int(a.lstrip("r"))
        x = by_row[n]
        src = x["file"].split(" (")[0]
        print(f"\n=== r{n} {x['comment ID']} | {x['commenter']} | fig={x['figure']} | {x['file_basis']}")
        print(f"    claim: {x['claim']}")
        if src.endswith(".pdf"):
            pages = pdf_pages(src)
            page, t, how = find(pages, x["claim"], x["figure"])
            if page is None or "OCR" in x["file_basis"] or "not re-located" in x["file_basis"]:
                # search OCR text page by page
                for p in range(1, len(pages) + 1):
                    ot = ocr_page(src, p)
                    pg, tt, hw = find([ot], x["claim"], x["figure"])
                    if pg:
                        page, t, how = p, tt, "OCR " + hw
                        break
            print(f"    file: {src} | page {page} of {len(pages)} | located by {how}")
            nxt = pages[page] if page and page < len(pages) and "OCR" not in how else ""
            print(f"    context: …{context(t + ' ' + nxt[:600], x['figure'], x['claim'])}…")
            if render and page:
                Path(render).mkdir(parents=True, exist_ok=True)
                outp = f"{render}/r{n}_p{page}"
                subprocess.run(["pdftoppm", "-r", "110", "-f", str(page), "-l", str(page), "-png", "-singlefile", src, outp])
                print(f"    rendered: {outp}.png")
        elif src.endswith(".docx"):
            t = docx_text(src)
            print(f"    file: {src} | docx (no fixed pages)")
            print(f"    context: …{context(t, x['figure'], x['claim'])}…")
        else:
            import json
            rec = json.loads(Path(src).read_text())
            print(f"    file: {src} (comment field)")
            print(f"    context: …{context(re.sub('<[^>]+>', ' ', rec.get('comment') or ''), x['figure'], x['claim'])}…")


if __name__ == "__main__":
    main()
