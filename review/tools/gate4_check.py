"""Gate 4: check the reference document and a two-page sample built with it.

1. Colour scan of every XML part of theia-reference.docx: each colour
   value (w:color, w:fill, w:val of w:color/w:shd/w:highlight, a:srgbClr,
   a:sysClr lastClr, VML colours) is in the THEIA palette; no blue; no
   highlight; hyperlink style in #A10400.
2. Every style pandoc uses is defined, plus Byline, Compact List, Header,
   Footer and the Table style's header, banding and first-column parts.
3. The sample (review/tools/sample_gate4.md) built by build_v19.py renders
   to two US Letter pages with the running header and the footer
   "Public note · Page X of Y" on each page, never "Confidential", and with
   the house fonts embedded. Page images go to the scratch folder given as
   argument, beside the layout reference's pages, for the side-by-side look.

Usage: python review/tools/gate4_check.py SCRATCH_DIR
"""
import re
import subprocess
import sys
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import build_v19  # noqa: E402

PALETTE = {"A10400", "C00000", "FBEDED", "1A1A1A", "8A8A8A", "555555", "DCDCD8",
           "D9AD2B", "F0E2B0", "7F0300", "FFFFFF"}
fails = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


def colours(xml):
    found = []
    found += re.findall(r'w:(?:color|fill)="([0-9A-Fa-f]{6})"', xml)
    found += re.findall(r'<w:(?:color|shd|highlight)\b[^>]*\bw:val="([0-9A-Fa-f]{6})"', xml)
    found += re.findall(r'<a:srgbClr val="([0-9A-Fa-f]{6})"', xml)
    found += re.findall(r'lastClr="([0-9A-Fa-f]{6})"', xml)
    found += re.findall(r'(?:fillcolor|strokecolor|color2?)="#?([0-9A-Fa-f]{6})"', xml)
    return {c.upper() for c in found}


def is_blue(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) for i in (0, 2, 4))
    return b > r + 20 and b > g


ref = TOOLS / "theia-reference.docx"
allc = set()
with zipfile.ZipFile(ref) as z:
    for n in z.namelist():
        if n.endswith(".xml") or n.endswith(".rels"):
            xml = z.read(n).decode("utf-8", "ignore")
            c = colours(xml)
            allc |= c
            off = sorted(c - PALETTE)
            check(not off, f"{n}: colours {sorted(c) or '-'}" + (f" OFF-PALETTE {off}" if off else ""))
            check("w:highlight" not in xml, f"{n}: no highlighting")
            check(not re.search(r'w:val="(?:blue|darkBlue|cyan)"', xml), f"{n}: no named blue")
    styles = z.read("word/styles.xml").decode()
    header = z.read("word/header1.xml").decode()
    footer = z.read("word/footer1.xml").decode()
    document = z.read("word/document.xml").decode()
check(not any(is_blue(c) for c in allc), f"no blue anywhere ({sorted(allc)})")

need = ["Normal", "BodyText", "FirstParagraph", "Compact", "CompactList", "Title", "Subtitle", "Byline", "Author",
        "Date", "Abstract", "AbstractTitle", "Bibliography", "Heading1", "Heading2", "Heading3", "BlockText",
        "FootnoteText", "Caption", "TableCaption", "ImageCaption", "Figure", "CaptionedFigure", "DefinitionTerm",
        "Definition", "TOCHeading", "Header", "Footer", "DefaultParagraphFont", "BodyTextChar", "VerbatimChar",
        "SectionNumber", "FootnoteReference", "Hyperlink", "TableNormal", "Table"]
ids = set(re.findall(r'w:styleId="([^"]+)"', styles))
check(not (set(need) - ids), f"styles defined: missing {sorted(set(need) - ids) or 'none'}")
hl = re.search(r'w:styleId="Hyperlink".*?</w:style>', styles, re.S).group(0)
check('w:val="A10400"' in hl, "Hyperlink style is #A10400")
tbl = re.search(r'w:styleId="Table">.*?</w:style>', styles, re.S).group(0)
check('w:type="firstRow"' in tbl and 'w:val="C00000"' in tbl and 'w:color="A10400"' in tbl and "<w:tblHeader/>" in tbl,
      "Table style: header row bold #C00000, #A10400 rule, repeats")
check('w:type="band1Horz"' in tbl and 'w:fill="FBEDED"' in tbl, "Table style: #FBEDED banding")
check("<w:cantSplit/>" in tbl and 'w:insideV w:val="nil"' in tbl, "Table style: rows do not split; no vertical borders")
for h, size in (("Heading1", "34"), ("Heading2", "27")):
    blk = re.search(rf'w:styleId="{h}">.*?</w:style>', styles, re.S).group(0)
    check(all(x in blk for x in ('w:val="A10400"', "<w:keepNext/>", 'w:jc w:val="center"', f'w:sz w:val="{size}"', "EB Garamond")),
          f"{h}: EB Garamond {int(size) / 2} pt, #A10400, centred, keep with next")
check('w:ascii="Gelasio"' in styles and 'w:sz w:val="21"' in styles and 'w:line="276"' in styles,
      "body: Gelasio 10.5 pt, line 1.15")
check(">THEIA<" in header and "> Services<" in header and "<w:b/>" in header and 'w:color="A10400"' in header,
      "header: THEIA bold + Services, #A10400, rule beneath")
check("PAGE" in footer and "NUMPAGES" in footer and "Public note · Page" in footer and 'w:color="DCDCD8"' in footer
      and "<w:i/>" in footer and "Confidential" not in footer, "footer: Public note · Page X of Y, italic, rule above")
check('w:w="12240" w:h="15840"' in document and all(f'w:{s}="1440"' for s in ("top", "bottom", "left", "right"))
      and 'w:left="1440"' in document, "page: US Letter, 1-inch margins")

# sample
scratch = Path(sys.argv[1]) if len(sys.argv) > 1 else TOOLS
docx = scratch / "sample_gate4.docx"
build_v19.build(TOOLS / "sample_gate4.md", docx)
pdf = docx.with_suffix(".pdf")
info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
check(pages == 2, f"sample renders to {pages} pages")
check("612 x 792" in info, "sample page size US Letter (612 x 792 pt)")
for p in range(1, pages + 1):
    t = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    check(lines[0].startswith("THEIA Services"), f"sample p.{p}: running header first")
    check(lines[-1] == f"Public note · Page {p} of {pages}", f"sample p.{p}: footer '{lines[-1]}'")
    check("Confidential" not in t, f"sample p.{p}: no 'Confidential'")
fonts = subprocess.run(["pdffonts", str(pdf)], capture_output=True, text=True).stdout
for f in ("Gelasio-Regular", "EBGaramond-Regular", "Gelasio-Bold", "Gelasio-Italic"):
    check(re.search(rf"\+{f}\s.*\byes\b", fonts) is not None, f"sample: {f} embedded")
subprocess.run(["pdftoppm", "-r", "80", "-png", str(pdf), str(scratch / "sample")], check=True)
print(f"page images for the side-by-side comparison: {scratch}/sample-*.png")

print("\nGATE 4:", "FAIL (%d)" % len(fails) if fails else "PASS")
sys.exit(1 if fails else 0)
