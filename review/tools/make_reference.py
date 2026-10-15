"""Build review/tools/theia-reference.docx, the pandoc reference document
for THEIA Services' house design.

Starts from pandoc's own default reference.docx (so every part pandoc
expects is present), then replaces:
  word/styles.xml       every style pandoc uses, defined in the palette
  word/theme/theme1.xml theme colours and fonts mapped to the palette
  word/document.xml     a short style sample plus the section properties
                        (US Letter, 1-inch margins, header and footer)
and adds word/header1.xml and word/footer1.xml.

THEIA palette: A10400 dark red; C00000 table header text; FBEDED banding;
1A1A1A ink; 8A8A8A mid grey; 555555 muted grey; DCDCD8 rule grey;
D9AD2B gold; F0E2B0 pale gold; 7F0300 deep red; FFFFFF white.

Usage: python review/tools/make_reference.py
"""
import re
import subprocess
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
OUT = TOOLS / "theia-reference.docx"

RED, HEAD_RED, PINK, INK = "A10400", "C00000", "FBEDED", "1A1A1A"
MID, MUTED, RULE, GOLD, PALE, DEEP = "8A8A8A", "555555", "DCDCD8", "D9AD2B", "F0E2B0", "7F0300"
HEAD_FONT, BODY_FONT = "EB Garamond", "Gelasio"

W = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
     'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')


def fonts(f):
    return f'<w:rFonts w:ascii="{f}" w:hAnsi="{f}" w:eastAsia="{f}" w:cs="{f}"/>'


def pstyle(sid, name, based=None, nxt=None, ppr="", rpr="", q=True, custom=False):
    b = f'<w:basedOn w:val="{based}"/>' if based else ""
    n = f'<w:next w:val="{nxt}"/>' if nxt else ""
    c = ' w:customStyle="1"' if custom else ""
    return (f'<w:style w:type="paragraph" w:styleId="{sid}"{c}><w:name w:val="{name}"/>{b}{n}'
            f'{"<w:qFormat/>" if q else ""}<w:pPr>{ppr}</w:pPr><w:rPr>{rpr}</w:rPr></w:style>')


def cstyle(sid, name, rpr, based="DefaultParagraphFont", custom=False):
    c = ' w:customStyle="1"' if custom else ""
    return (f'<w:style w:type="character" w:styleId="{sid}"{c}><w:name w:val="{name}"/>'
            f'<w:basedOn w:val="{based}"/><w:rPr>{rpr}</w:rPr></w:style>')


def heading(level, size_half, before, after):
    return pstyle(f"Heading{level}", f"heading {level}", "Normal", "BodyText",
                  f'<w:keepNext/><w:keepLines/><w:spacing w:before="{before}" w:after="{after}" w:line="240" w:lineRule="auto"/>'
                  f'<w:jc w:val="center"/><w:outlineLvl w:val="{level - 1}"/>',
                  f'{fonts(HEAD_FONT)}<w:b w:val="0"/><w:color w:val="{RED}"/><w:sz w:val="{size_half}"/><w:szCs w:val="{size_half}"/>')


CAPTION_RPR = f'<w:i/><w:color w:val="{MUTED}"/><w:sz w:val="18"/><w:szCs w:val="18"/>'
BYLINE_RPR = f'<w:color w:val="{MUTED}"/><w:sz w:val="20"/><w:szCs w:val="20"/>'

STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles {W}>
<w:docDefaults>
 <w:rPrDefault><w:rPr>{fonts(BODY_FONT)}<w:color w:val="{INK}"/><w:sz w:val="21"/><w:szCs w:val="21"/><w:lang w:val="en-US"/></w:rPr></w:rPrDefault>
 <w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault>
</w:docDefaults>
{pstyle("Normal", "Normal", ppr='<w:spacing w:after="120" w:line="276" w:lineRule="auto"/>', rpr=f'{fonts(BODY_FONT)}<w:color w:val="{INK}"/><w:sz w:val="21"/><w:szCs w:val="21"/>').replace('<w:style w:type="paragraph" w:styleId="Normal">', '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">')}
{pstyle("BodyText", "Body Text", "Normal", ppr='<w:spacing w:before="0" w:after="120"/>')}
{pstyle("FirstParagraph", "First Paragraph", "BodyText", "BodyText")}
{pstyle("Compact", "Compact", "BodyText", ppr='<w:spacing w:before="0" w:after="0" w:line="252" w:lineRule="auto"/>', rpr='<w:sz w:val="19"/><w:szCs w:val="19"/>')}
{pstyle("CompactList", "Compact List", "BodyText", ppr='<w:spacing w:before="0" w:after="60"/>', custom=True)}
{pstyle("Title", "Title", "Normal", "Byline", f'<w:keepNext/><w:keepLines/><w:spacing w:before="120" w:after="120" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>', f'{fonts(HEAD_FONT)}<w:color w:val="{RED}"/><w:sz w:val="44"/><w:szCs w:val="44"/>')}
{pstyle("Subtitle", "Subtitle", "Title", "Byline", '<w:spacing w:before="0" w:after="120"/>', f'<w:color w:val="{INK}"/><w:sz w:val="30"/><w:szCs w:val="30"/>')}
{pstyle("Byline", "Byline", "Normal", "BodyText", '<w:keepNext/><w:spacing w:before="0" w:after="20" w:line="252" w:lineRule="auto"/><w:jc w:val="center"/>', BYLINE_RPR, custom=True)}
{pstyle("Author", "Author", "Byline", "BodyText")}
{pstyle("Date", "Date", "Byline", "BodyText")}
{pstyle("AbstractTitle", "Abstract Title", "Normal", "Abstract", '<w:keepNext/><w:spacing w:before="240" w:after="60"/><w:jc w:val="center"/>', f'<w:b/><w:color w:val="{RED}"/>', custom=True)}
{pstyle("Abstract", "Abstract", "Normal", "BodyText", '<w:spacing w:before="120" w:after="120"/>', '<w:sz w:val="20"/><w:szCs w:val="20"/>', custom=True)}
{pstyle("Bibliography", "Bibliography", "Normal")}
{heading(1, 34, 360, 120)}
{heading(2, 27, 240, 80)}
{heading(3, 24, 200, 60)}
{heading(4, 22, 160, 40)}
{heading(5, 22, 160, 40)}
{heading(6, 22, 160, 40)}
{heading(7, 22, 160, 40)}
{heading(8, 22, 160, 40)}
{heading(9, 22, 160, 40)}
{pstyle("BlockText", "Block Text", "BodyText", "BodyText", '<w:spacing w:before="60" w:after="120"/><w:ind w:left="480" w:right="480"/>', f'<w:color w:val="{INK}"/>')}
{pstyle("FootnoteText", "footnote text", "Normal", ppr='<w:spacing w:after="40"/>', rpr='<w:sz w:val="18"/><w:szCs w:val="18"/>')}
{pstyle("DefinitionTerm", "Definition Term", "Normal", "Definition", '<w:keepNext/><w:spacing w:before="0" w:after="0"/>', '<w:b/>', custom=True)}
{pstyle("Definition", "Definition", "Normal", ppr='<w:ind w:left="360"/>', custom=True)}
{pstyle("Caption", "caption", "Normal", ppr='<w:spacing w:before="40" w:after="200"/>', rpr=CAPTION_RPR)}
{pstyle("TableCaption", "Table Caption", "Caption", ppr='<w:keepNext/>', custom=True)}
{pstyle("ImageCaption", "Image Caption", "Caption", custom=True)}
{pstyle("Figure", "Figure", "Normal", ppr='<w:keepNext/><w:spacing w:before="120" w:after="0"/><w:jc w:val="center"/>', custom=True)}
{pstyle("CaptionedFigure", "Captioned Figure", "Figure", ppr='<w:keepNext/>', custom=True)}
{pstyle("TOCHeading", "TOC Heading", "Heading1", "BodyText", q=False)}
<w:style w:type="character" w:default="1" w:styleId="DefaultParagraphFont"><w:name w:val="Default Paragraph Font"/><w:uiPriority w:val="1"/><w:semiHidden/><w:unhideWhenUsed/></w:style>
{cstyle("BodyTextChar", "Body Text Char", "", custom=True)}
{cstyle("VerbatimChar", "Verbatim Char", '<w:rFonts w:ascii="Liberation Mono" w:hAnsi="Liberation Mono"/><w:sz w:val="19"/>', custom=True)}
{cstyle("SectionNumber", "Section Number", "", custom=True)}
{cstyle("FootnoteReference", "footnote reference", '<w:vertAlign w:val="superscript"/>')}
{cstyle("Hyperlink", "Hyperlink", f'<w:color w:val="{RED}"/>')}
<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/><w:uiPriority w:val="99"/><w:semiHidden/><w:unhideWhenUsed/><w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
<w:style w:type="table" w:customStyle="1" w:styleId="Table"><w:name w:val="Table"/><w:basedOn w:val="TableNormal"/><w:qFormat/>
 <w:pPr><w:spacing w:before="0" w:after="0" w:line="252" w:lineRule="auto"/></w:pPr>
 <w:rPr><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr>
 <w:tblPr><w:tblBorders><w:top w:val="nil"/><w:left w:val="nil"/><w:bottom w:val="nil"/><w:right w:val="nil"/><w:insideH w:val="nil"/><w:insideV w:val="nil"/></w:tblBorders>
  <w:tblCellMar><w:top w:w="72" w:type="dxa"/><w:left w:w="115" w:type="dxa"/><w:bottom w:w="72" w:type="dxa"/><w:right w:w="115" w:type="dxa"/></w:tblCellMar></w:tblPr>
 <w:trPr><w:cantSplit/></w:trPr>
 <w:tblStylePr w:type="firstRow"><w:pPr><w:keepNext/></w:pPr><w:rPr><w:b/><w:bCs/><w:color w:val="{HEAD_RED}"/></w:rPr><w:tblPr/><w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>
  <w:tcPr><w:tcBorders><w:bottom w:val="single" w:sz="8" w:space="0" w:color="{RED}"/></w:tcBorders><w:shd w:val="clear" w:color="auto" w:fill="FFFFFF"/><w:vAlign w:val="bottom"/></w:tcPr></w:tblStylePr>
 <w:tblStylePr w:type="band1Horz"><w:tblPr/><w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="{PINK}"/></w:tcPr></w:tblStylePr>
 <w:tblStylePr w:type="band2Horz"><w:tblPr/><w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="FFFFFF"/></w:tcPr></w:tblStylePr>
 <w:tblStylePr w:type="firstCol"><w:rPr><w:b/><w:bCs/></w:rPr></w:tblStylePr>
</w:style>
</w:styles>
"""

HEADER = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:hdr {W}><w:p><w:pPr><w:pStyle w:val="Header"/><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="{RED}"/></w:pBdr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/></w:pPr>
<w:r><w:rPr>{fonts(HEAD_FONT)}<w:b/><w:color w:val="{RED}"/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr><w:t>THEIA</w:t></w:r>
<w:r><w:rPr>{fonts(HEAD_FONT)}<w:color w:val="{RED}"/><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr><w:t xml:space="preserve"> Services</w:t></w:r></w:p></w:hdr>
"""


def fld(instr):
    rpr = f'<w:rPr><w:i/><w:color w:val="{MUTED}"/><w:sz w:val="17"/><w:szCs w:val="17"/></w:rPr>'
    return (f'<w:r>{rpr}<w:fldChar w:fldCharType="begin"/></w:r><w:r>{rpr}<w:instrText xml:space="preserve"> {instr} </w:instrText></w:r>'
            f'<w:r>{rpr}<w:fldChar w:fldCharType="separate"/></w:r><w:r>{rpr}<w:t>1</w:t></w:r><w:r>{rpr}<w:fldChar w:fldCharType="end"/></w:r>')


FRPR = f'<w:rPr><w:i/><w:color w:val="{MUTED}"/><w:sz w:val="17"/><w:szCs w:val="17"/></w:rPr>'
FOOTER = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:ftr {W}><w:p><w:pPr><w:pStyle w:val="Footer"/><w:pBdr><w:top w:val="single" w:sz="4" w:space="6" w:color="{RULE}"/></w:pBdr><w:spacing w:before="0" w:after="0"/><w:jc w:val="center"/></w:pPr>
<w:r>{FRPR}<w:t xml:space="preserve">Public note · Page </w:t></w:r>{fld("PAGE")}<w:r>{FRPR}<w:t xml:space="preserve"> of </w:t></w:r>{fld("NUMPAGES")}</w:p></w:ftr>
"""

HF_STYLES = (pstyle("Header", "header", "Normal", q=False, ppr='<w:tabs><w:tab w:val="center" w:pos="4680"/><w:tab w:val="right" w:pos="9360"/></w:tabs><w:spacing w:after="0"/>')
             + pstyle("Footer", "footer", "Normal", q=False, ppr='<w:tabs><w:tab w:val="center" w:pos="4680"/><w:tab w:val="right" w:pos="9360"/></w:tabs><w:spacing w:after="0"/>'))
STYLES = STYLES.replace("</w:styles>", HF_STYLES + "\n</w:styles>")

SECTPR = ('<w:sectPr><w:headerReference w:type="default" r:id="rIdTheiaHeader"/>'
          '<w:footerReference w:type="default" r:id="rIdTheiaFooter"/>'
          '<w:pgSz w:w="12240" w:h="15840"/>'
          '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="576" w:gutter="0"/>'
          '<w:cols w:space="720"/></w:sectPr>')


def para(style, text):
    return f'<w:p><w:pPr><w:pStyle w:val="{style}"/></w:pPr><w:r><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'


DOCUMENT = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document {W}><w:body>
{para("Title", "Title")}{para("Byline", "Byline")}{para("Author", "Author")}{para("Heading1", "Heading 1")}
{para("Heading2", "Heading 2")}{para("FirstParagraph", "First Paragraph")}{para("BodyText", "Body Text")}
{para("Compact", "Compact")}{para("ImageCaption", "Image Caption")}{para("TableCaption", "Table Caption")}
{SECTPR}</w:body></w:document>
"""


def theme(xml):
    """Map the theme's colours and fonts to the palette."""
    slots = {"dk1": INK, "lt1": "FFFFFF", "dk2": MUTED, "lt2": RULE, "accent1": RED, "accent2": GOLD,
             "accent3": MID, "accent4": DEEP, "accent5": PALE, "accent6": HEAD_RED, "hlink": RED, "folHlink": DEEP}
    for slot, val in slots.items():
        xml = re.sub(rf"<a:{slot}>.*?</a:{slot}>", f'<a:{slot}><a:srgbClr val="{val}"/></a:{slot}>', xml, flags=re.S)
    xml = re.sub(r'<a:srgbClr val="000000"', f'<a:srgbClr val="{INK}"', xml)
    xml = re.sub(r'(<a:majorFont>\s*<a:latin typeface=")[^"]*"', rf'\1{HEAD_FONT}"', xml)
    xml = re.sub(r'(<a:minorFont>\s*<a:latin typeface=")[^"]*"', rf'\1{BODY_FONT}"', xml)
    return xml


def main():
    base = TOOLS / "_pandoc-default-reference.docx"
    subprocess.run(["pandoc", "-o", str(base), "--print-default-data-file", "reference.docx"], check=True)
    with zipfile.ZipFile(base) as zin, zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/styles.xml":
                data = STYLES.encode()
            elif item.filename == "word/document.xml":
                data = DOCUMENT.encode()
            elif item.filename == "word/theme/theme1.xml":
                data = theme(data.decode()).encode()
            elif item.filename == "word/comments.xml":
                continue
            elif item.filename == "word/_rels/document.xml.rels":
                s = data.decode()
                s = re.sub(r'<Relationship [^>]*Target="comments.xml" />', "", s)
                s = re.sub(r'<Relationship [^>]*TargetMode="External" />', "", s)
                s = s.replace("</Relationships>",
                              '<Relationship Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Id="rIdTheiaHeader" Target="header1.xml"/>'
                              '<Relationship Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Id="rIdTheiaFooter" Target="footer1.xml"/>'
                              "</Relationships>")
                data = s.encode()
            elif item.filename == "[Content_Types].xml":
                s = data.decode()
                s = s.replace('<Override PartName="/word/comments.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml" />', "")
                s = s.replace("</Types>",
                              '<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
                              '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
                              "</Types>")
                data = s.encode()
            zout.writestr(item, data)
        zout.writestr("word/header1.xml", HEADER)
        zout.writestr("word/footer1.xml", FOOTER)
    base.unlink()
    print("wrote", OUT)


if __name__ == "__main__":
    main()
