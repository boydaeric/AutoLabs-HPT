"""Gate 5 (v20: Stage 4 gate): check Exposure-Not-Loss-v20-draft.docx and .pdf
against article_v9.md. Paths and the expected figure count are set below; for
v19 they were article_v8.md, v19 and 5 figures.

1. Text: the docx body's words, in order, equal article_v8.md's words
   (markdown syntax ignored; the placeholder "[Figure N]" reads
   "Figure N." in the caption; images carry no text).
2. Counts: headings (by level), tables, [E], [I], [C], [DATE] and figure
   placeholders match.
3. Images: five, in order, each 6.5 in wide with alt text from
   figures.json and its caption directly below.
4. PDF: every font embedded; no "Confidential"; no table row split across
   pages; a table that runs onto another page repeats its header row there;
   no heading stranded at a page foot (the heading's page also holds the
   start of the next paragraph or table).

Usage: python review/tools/gate5_check.py
"""
import difflib
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

from lxml import etree

REVIEW = Path(__file__).resolve().parents[1]
MD = REVIEW / "article_v9.md"
DOCX = REVIEW / "Exposure-Not-Loss-v20-draft.docx"
PDF = REVIEW / "Exposure-Not-Loss-v20-draft.pdf"
N_FIG, N_TABLES = 9, 5
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
WP = "{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}"
fails = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


# ---------------------------------------------------------------- markdown side
md = MD.read_text(encoding="utf-8")
ast = json.loads(subprocess.run(["pandoc", str(MD), "-f", "markdown-smart", "-t", "json"],
                                capture_output=True, text=True, check=True).stdout)


def inline_text(x):
    out = []

    def walk(n):
        if isinstance(n, dict):
            t = n.get("t")
            if t == "Str":
                out.append(n["c"])
            elif t in ("Para", "Plain", "Header"):
                walk(n.get("c"))
                out.append(" ")
            elif t in ("Space", "SoftBreak", "LineBreak"):
                out.append(" ")
            elif t == "Image":
                return
            else:
                walk(n.get("c"))
        elif isinstance(n, list):
            for m in n:
                walk(m)
    walk(x)
    return "".join(out)


md_text = inline_text(ast["blocks"])
md_text = re.sub(r"\[Figure (\d+)\]", r"Figure \1.", md_text)
md_words = md_text.split()

md_tables = sum(1 for b in ast["blocks"] if b["t"] == "Table")
md_h = {1: len(re.findall(r"^# ", md, re.M)), 2: len(re.findall(r"^## ", md, re.M)),
        3: len(re.findall(r"^### ", md, re.M))}

# ---------------------------------------------------------------- docx side
with zipfile.ZipFile(DOCX) as z:
    root = etree.fromstring(z.read("word/document.xml"))
body = root.find(f"{W}body")


def ptext(p):
    return "".join(t.text or "" for t in p.iter(f"{W}t"))


def style(p):
    s = p.find(f"{W}pPr/{W}pStyle")
    return s.get(f"{W}val") if s is not None else ""


doc_text = " ".join(ptext(p) for p in body.iter(f"{W}p"))
doc_words = doc_text.split()
sm = difflib.SequenceMatcher(a=md_words, b=doc_words, autojunk=False)
diffs = [op for op in sm.get_opcodes() if op[0] != "equal"]
for tag, i1, i2, j1, j2 in diffs[:10]:
    print(f"     {tag}: md {' '.join(md_words[max(0, i1 - 3):i2 + 3])!r} | docx {' '.join(doc_words[max(0, j1 - 3):j2 + 3])!r}")
check(not diffs, f"text: docx words equal {MD.name} words ({len(md_words)} md, {len(doc_words)} docx, {len(diffs)} differences)")

paras = list(body.iter(f"{W}p"))
d_h = {k: sum(1 for p in paras if style(p) == f"Heading{k}") for k in (1, 2, 3)}
check(d_h == md_h, f"headings by level: docx {d_h}, md {md_h}")
d_tables = len(body.findall(f".//{W}tbl"))
check(d_tables == md_tables == N_TABLES, f"tables: docx {d_tables}, md {md_tables} (want {N_TABLES})")
for tag in ("[E]", "[I]", "[C]", "[DATE]"):
    check(doc_text.count(tag) == md_text.count(tag), f"{tag}: docx {doc_text.count(tag)}, md {md_text.count(tag)}")
md_ph = re.findall(r"^\*\[Figure (\d+)\]", md, re.M)
caps = [ptext(p) for p in paras if style(p) == "ImageCaption"]
check([c.split(".")[0] for c in caps] == [f"Figure {n}" for n in md_ph] == [f"Figure {n}" for n in range(1, N_FIG + 1)],
      f"figure placeholders: md {md_ph}, docx captions {[c.split('.')[0] for c in caps]}")

# ---------------------------------------------------------------- images
meta = json.loads((REVIEW / "figures" / "figures.json").read_text(encoding="utf-8"))
docprs = list(body.iter(f"{WP}docPr"))
extents = [e for e in body.iter(f"{WP}extent")]
check(len(docprs) == N_FIG, f"images: {len(docprs)} (want {N_FIG})")
for dp, ext, m in zip(docprs, extents, meta):
    check(dp.get("descr") == m["alt"] and m["alt"].strip() and dp.get("title") == f"Figure {m['number']}",
          f"image {m['number']}: alt text set ({len(m['alt'].split())} words)")
    check(abs(int(ext.get("cx")) - 5943600) < 1000, f"image {m['number']}: width {int(ext.get('cx')) / 914400:.2f} in")
for i, p in enumerate(paras):
    if p.find(f".//{WP}docPr") is not None:
        nxt = paras[i + 1]
        check(style(nxt) == "ImageCaption", f"caption directly below image: {ptext(nxt)[:40]!r}")

# ---------------------------------------------------------------- PDF
info = subprocess.run(["pdfinfo", str(PDF)], capture_output=True, text=True).stdout
npages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
pages = [subprocess.run(["pdftotext", "-f", str(k), "-l", str(k), str(PDF), "-"], capture_output=True, text=True).stdout
         for k in range(1, npages + 1)]
# pdftotext drops a hyphen where a word wraps at it ("non-" + "hospital"), so
# matching ignores whitespace, hyphens and soft hyphens on both sides
flat = [re.sub(r"[\s\-­]+", "", p) for p in pages]
fonts = subprocess.run(["pdffonts", str(PDF)], capture_output=True, text=True).stdout.splitlines()[2:]
not_emb = [l.split()[0] for l in fonts if " no " in f" {l} ".replace("  ", " ") and l.split()[-5] == "no"]
check(fonts and not not_emb, f"PDF fonts embedded: {sorted({l.split()[0].split('+')[-1] for l in fonts})}")
check(not any("Confidential" in p for p in pages), "PDF: no 'Confidential'")
n_alt = len(re.findall(rb"/Alt\s*[(<]", PDF.read_bytes()))
check("Tagged:          yes" in info and n_alt == N_FIG, f"PDF: tagged, {n_alt} images with alt text")
check(re.search(r"Title:\s+The Missing Total", info) is not None and re.search(r"Author:\s+Eric Boyda", info) is not None,
      "PDF: title and author metadata set")


def key(s):
    return re.sub(r"[\s\-­]+", "", s)


def pages_with(s):
    k = key(s)
    return [i for i, f in enumerate(flat) if k and k in f]


split_rows, broken_tables = [], []
for ti, tbl in enumerate(body.iter(f"{W}tbl")):
    rows = tbl.findall(f"{W}tr")
    header = [ptext(tc) for tc in rows[0].findall(f"{W}tc")]
    span, last = set(), 0
    for r in rows:
        cells = [" ".join(ptext(p) for p in tc.iter(f"{W}p")) for tc in r.findall(f"{W}tc")]
        # a row is whole on a page when its cells, in order, occur there together
        home = [pg for pg in pages_with("".join(cells)) if pg >= last]
        if not home:
            # multi-line cells (e.g. bottom-aligned headers) are read line by
            # line across columns: then each cell must be whole on one common page
            homes = [set(pages_with(c)) for c in cells if key(c)]
            home = sorted(pg for pg in (set.intersection(*homes) if homes else set()) if pg >= last)
        if not home:
            split_rows.append((ti + 1, cells[0][:40]))
            continue
        last = home[0]
        span.add(home[0])
    if len(span) > 1:
        for pg in sorted(span):
            if not all(key(h) in flat[pg] for h in header if key(h)):
                broken_tables.append((ti + 1, pg + 1))
check(not split_rows, f"PDF: no table row split across pages {split_rows or ''}")
check(not broken_tables, f"PDF: tables that cross a page repeat their header {broken_tables or ''}")

stranded = []
blocks = [el for el in body if el.tag in (f"{W}p", f"{W}tbl")]
for i, el in enumerate(blocks):
    if el.tag == f"{W}p" and style(el).startswith("Heading"):
        h = ptext(el)
        nxt = blocks[i + 1]
        nt = ptext(nxt) if nxt.tag == f"{W}p" else " ".join(ptext(p) for p in nxt.iter(f"{W}p"))
        start = " ".join(nt.split()[:5])
        hp, np_ = set(pages_with(h)), set(pages_with(start))
        if not (hp & np_):
            stranded.append(h[:40])
check(not stranded, f"PDF: no heading stranded at a page foot {stranded or ''}")

print(f"\n{PDF.stem}: {npages} pages")
print("GATE 5:", "FAIL (%d)" % len(fails) if fails else "PASS")
sys.exit(1 if fails else 0)
