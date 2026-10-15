"""Install the THEIA house fonts as static TrueType instances.

Downloads the variable fonts from the google/fonts GitHub repository and
cuts static Regular / Bold / Italic / Bold Italic instances (plus Instrument
Sans SemiBold) into ~/.fonts/theia-static/, so matplotlib and LibreOffice
get true bold and italic faces rather than synthesized ones.

  Instrument Sans  charts
  EB Garamond      headings and title
  Gelasio          body

Needs: fonttools, skia-pathops. Then run `fc-cache -f`.
Usage: python review/tools/install_fonts.py
"""
import os
import urllib.request
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import OverlapMode, instantiateVariableFont

BASE = "https://raw.githubusercontent.com/google/fonts/main/ofl/"
SRC = Path.home() / ".local/share/vf-src"
OUT = Path.home() / ".fonts/theia-static"
RIBBI = ("Regular", "Bold", "Italic", "Bold Italic")

SPECS = [
    ("instrumentsans/InstrumentSans[wdth,wght].ttf", "Instrument Sans",
     [("Regular", 400, False), ("Bold", 700, False), ("SemiBold", 600, False)], {"wdth": 100}),
    ("instrumentsans/InstrumentSans-Italic[wdth,wght].ttf", "Instrument Sans",
     [("Italic", 400, True), ("Bold Italic", 700, True)], {"wdth": 100}),
    ("ebgaramond/EBGaramond[wght].ttf", "EB Garamond",
     [("Regular", 400, False), ("Bold", 700, False)], {}),
    ("ebgaramond/EBGaramond-Italic[wght].ttf", "EB Garamond",
     [("Italic", 400, True), ("Bold Italic", 700, True)], {}),
    ("gelasio/Gelasio[wght].ttf", "Gelasio", [("Regular", 400, False), ("Bold", 700, False)], {}),
    ("gelasio/Gelasio-Italic[wght].ttf", "Gelasio",
     [("Italic", 400, True), ("Bold Italic", 700, True)], {}),
]


def main():
    SRC.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    for rel, fam, styles, extra in SPECS:
        src = SRC / Path(rel).name
        if not src.exists():
            url = BASE + rel.replace("[", "%5B").replace("]", "%5D")
            urllib.request.urlretrieve(url, src)
        for style, w, ital in styles:
            loc = dict(extra, wght=w)
            inst = instantiateVariableFont(TTFont(src), loc, updateFontNames=False,
                                           overlap=OverlapMode.REMOVE)
            name = inst["name"]
            ribbi = style in RIBBI
            ps = (fam + "-" + style).replace(" ", "")
            for rid in (1, 2, 3, 4, 6, 16, 17, 21, 22, 25):
                name.removeNames(nameID=rid)
            name.setName(fam if ribbi else f"{fam} {style}", 1, 3, 1, 0x409)
            name.setName(style if ribbi else "Regular", 2, 3, 1, 0x409)
            name.setName(ps, 3, 3, 1, 0x409)
            name.setName(f"{fam} {style}", 4, 3, 1, 0x409)
            name.setName(ps, 6, 3, 1, 0x409)
            name.setName(fam, 16, 3, 1, 0x409)
            name.setName(style, 17, 3, 1, 0x409)
            os2 = inst["OS/2"]
            os2.usWeightClass = w
            sel = (1 if ital else 0) | (32 if w >= 700 else 0) | (64 if (not ital and w < 700 and ribbi) else 0)
            os2.fsSelection = (os2.fsSelection & ~0b1100001) | sel
            inst["head"].macStyle = (1 if w >= 700 else 0) | (2 if ital else 0)
            if "STAT" in inst:
                del inst["STAT"]
            inst.save(OUT / f"{ps}.ttf")
            print(OUT / f"{ps}.ttf")


if __name__ == "__main__":
    main()
    os.system("fc-cache -f")
