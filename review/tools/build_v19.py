"""Build the Word and PDF versions of the note from a markdown file.

  python review/tools/build_v19.py                     # article_v8.md -> v19 docx + pdf
  python review/tools/build_v19.py --md X.md --out Y.docx [--pdf]

Steps
1. Pre-process the markdown (a copy; article_v8.md is never changed):
   - title, byline and author line -> custom styles Title and Byline;
   - each "*[Figure N] caption*" placeholder -> the figure's PNG, 6.5 in
     wide, as a pandoc figure whose caption reads "Figure N. caption".
2. pandoc with review/tools/theia-reference.docx.
3. Post-process the .docx:
   - every table row cantSplit; header row repeats (tblHeader);
   - tblLook: banded rows on; first column bold only where every body cell
     in it is a short label (6 words or fewer);
   - tight-list paragraphs outside tables -> "Compact List" (Compact is
     the table cell style);
   - a paragraph that is wholly italic and starts "Source:" -> Caption;
   - each image's alt text (docPr descr) from review/figures/figures.json.
4. LibreOffice renders the PDF; fonts are embedded (PDF export default),
   checked by gate5_check.py with pdffonts.
"""
import argparse
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from lxml import etree

TOOLS = Path(__file__).resolve().parent
REVIEW = TOOLS.parent
FIG = REVIEW / "figures"
REF = TOOLS / "theia-reference.docx"
WNS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": WNS,
      "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture"}


def w(tag):
    return f"{{{WNS}}}{tag}"


def preprocess(md, figures):
    lines = md.split("\n")
    # title block: first non-empty lines up to the evidence-tag line
    title_done = False
    out = []
    by_num = {m["number"]: m for m in figures}
    for i, line in enumerate(lines):
        if not title_done and re.fullmatch(r"\*\*(.+)\*\*", line):
            out += ['::: {custom-style="Title"}', line[2:-2], ":::"]
            title_done = True
            continue
        if title_done and i < 8 and re.fullmatch(r"\*(THEIA Services · .+|Prepared by: .+)\*", line):
            out += ['::: {custom-style="Byline"}', line[1:-1], ":::"]
            continue
        m = re.fullmatch(r"\*\[Figure (\d+)\] (.+)\*", line)
        if m:
            n = int(m.group(1))
            f = by_num[n]
            cap = m.group(2).replace("[", r"\[").replace("]", r"\]")
            out.append(f"![Figure {n}. {cap}](figures/{f['stem']}.png){{width=6.5in}}")
            continue
        out.append(line)
    return "\n".join(out)


def words(el):
    return len("".join(t.text or "" for t in el.iter(w("t"))).split())


def postprocess(docx, figures):
    tmp = Path(tempfile.mkdtemp())
    with zipfile.ZipFile(docx) as z:
        z.extractall(tmp)
    doc_path = tmp / "word" / "document.xml"
    tree = etree.parse(str(doc_path))
    root = tree.getroot()

    for tbl in root.iter(w("tbl")):
        rows = tbl.findall(w("tr"))
        for k, tr in enumerate(rows):
            trpr = tr.find(w("trPr"))
            if trpr is None:
                trpr = etree.Element(w("trPr"))
                tr.insert(0, trpr)
            if trpr.find(w("cantSplit")) is None:
                trpr.insert(0, etree.Element(w("cantSplit")))
            if k == 0 and trpr.find(w("tblHeader")) is None:
                trpr.append(etree.Element(w("tblHeader")))
        body_first = [tr.findall(w("tc"))[0] for tr in rows[1:] if tr.findall(w("tc"))]
        short = bool(body_first) and all(words(tc) <= 6 for tc in body_first)
        # direct formatting mirrors the Table style, because LibreOffice does
        # not apply a table style's conditional text colour
        for k, tr in enumerate(rows):
            for c, tc in enumerate(tr.findall(w("tc"))):
                if k > 0:
                    tcpr = tc.find(w("tcPr"))
                    if tcpr is None:
                        tcpr = etree.Element(w("tcPr"))
                        tc.insert(0, tcpr)
                    for old in tcpr.findall(w("shd")):
                        tcpr.remove(old)
                    shd = etree.SubElement(tcpr, w("shd"))
                    shd.set(w("val"), "clear")
                    shd.set(w("color"), "auto")
                    shd.set(w("fill"), "FBEDED" if k % 2 == 1 else "FFFFFF")
                for r in tc.iter(w("r")):
                    rpr = r.find(w("rPr"))
                    if rpr is None:
                        rpr = etree.Element(w("rPr"))
                        r.insert(0, rpr)
                    if k == 0 or (short and c == 0):
                        if rpr.find(w("b")) is None:
                            rpr.append(etree.Element(w("b")))
                    if k == 0:
                        for old in rpr.findall(w("color")):
                            rpr.remove(old)
                        col = etree.SubElement(rpr, w("color"))
                        col.set(w("val"), "C00000")
        tblpr = tbl.find(w("tblPr"))
        look = tblpr.find(w("tblLook"))
        if look is None:
            look = etree.SubElement(tblpr, w("tblLook"))
        for k in list(look.attrib):
            del look.attrib[k]
        look.set(w("firstRow"), "1")
        look.set(w("lastRow"), "0")
        look.set(w("firstColumn"), "1" if short else "0")
        look.set(w("lastColumn"), "0")
        look.set(w("noHBand"), "0")
        look.set(w("noVBand"), "1")
        look.set(w("val"), "04A0" if short else "0420")

    in_table = set()
    for tbl in root.iter(w("tbl")):
        for p in tbl.iter(w("p")):
            in_table.add(p)
    for p in root.iter(w("p")):
        ps = p.find(f"{w('pPr')}/{w('pStyle')}")
        if ps is None:
            continue
        if ps.get(w("val")) == "Compact" and p not in in_table:
            ps.set(w("val"), "CompactList")
    for p in root.iter(w("p")):
        if p in in_table:
            continue
        runs = [r for r in p.findall(w("r")) if "".join(t.text or "" for t in r.iter(w("t"))).strip()]
        text = "".join(t.text or "" for t in p.iter(w("t")))
        if runs and text.startswith("Source:") and all(r.find(f"{w('rPr')}/{w('i')}") is not None for r in runs):
            ppr = p.find(w("pPr"))
            if ppr is None:
                ppr = etree.Element(w("pPr"))
                p.insert(0, ppr)
            ps = ppr.find(w("pStyle"))
            if ps is None:
                ps = etree.Element(w("pStyle"))
                ppr.insert(0, ps)
            ps.set(w("val"), "Caption")

    bylines = [p for p in root.iter(w("p"))
               if (p.find(f"{w('pPr')}/{w('pStyle')}") is not None
                   and p.find(f"{w('pPr')}/{w('pStyle')}").get(w("val")) == "Byline")]
    if bylines:
        ppr = bylines[-1].find(w("pPr"))
        sp = etree.SubElement(ppr, w("spacing"))
        sp.set(w("before"), "0")
        sp.set(w("after"), "240")

    docprs = list(root.iter(f"{{{NS['wp']}}}docPr"))
    assert len(docprs) == len(figures), f"{len(docprs)} images, {len(figures)} figures"
    for dp, f in zip(docprs, figures):
        dp.set("descr", f["alt"])
        dp.set("title", f"Figure {f['number']}")
        dp.set("name", f"Figure {f['number']}")
    tree.write(str(doc_path), xml_declaration=True, encoding="UTF-8", standalone=True)

    out = Path(str(docx) + ".tmp")
    with zipfile.ZipFile(docx) as zin, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = (tmp / item.filename).read_bytes()
            zout.writestr(item, data)
    shutil.move(out, docx)
    shutil.rmtree(tmp)


def render_pdf(docx):
    # lossless images at full resolution; fonts embedded (standard fonts too)
    opts = ('pdf:writer_pdf_Export:{"UseLosslessCompression":{"type":"boolean","value":"true"},'
            '"ReduceImageResolution":{"type":"boolean","value":"false"},'
            '"EmbedStandardFonts":{"type":"boolean","value":"true"}}')
    subprocess.run(["soffice", "--headless", "--convert-to", opts, "--outdir", str(Path(docx).parent), str(docx)],
                   check=True, capture_output=True)
    return Path(docx).with_suffix(".pdf")


def build(md_path, out_docx, pdf=True):
    figures = json.loads((FIG / "figures.json").read_text(encoding="utf-8"))
    md = Path(md_path).read_text(encoding="utf-8")
    pre = preprocess(md, figures)
    used = [m for m in figures if f"figures/{m['stem']}.png" in pre]
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tf:
        tf.write(pre)
    subprocess.run(["pandoc", tf.name, "-f", "markdown-smart+pipe_tables", "-t", "docx",
                    "--reference-doc", str(REF), "--resource-path", str(REVIEW),
                    "-o", str(out_docx)], check=True)
    Path(tf.name).unlink()
    postprocess(out_docx, used)
    print("wrote", out_docx)
    if pdf:
        print("wrote", render_pdf(out_docx))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", default=str(REVIEW / "article_v8.md"))
    ap.add_argument("--out", default=str(REVIEW / "Exposure-Not-Loss-v19-draft.docx"))
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()
    build(a.md, a.out, pdf=not a.no_pdf)
