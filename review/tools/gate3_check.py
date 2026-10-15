"""Gate 3: check the rendered figures.

1. Numbers: each figure's data labels (SVG text in <g id="datalabel">) equal
   its CSV values. For Figures 1, 3, 4 and 9 (converted v8 tables), every
   table cell, header and the source note appear verbatim in the chart text.
   Figure 6's tiles carry each state's CSV group, every tile's text clears
   4.5:1 contrast on its fill, the five lower-threshold states carry heavy
   ink outlines, and dark red fills Group A only.
2. Colours: every colour in every SVG is in the THEIA palette (or white).
3. Separation: each pair of category colours, in greyscale and under
   protan / deutan / tritan simulation (Machado et al. 2009, severity 1),
   differs by OKLab dE x100 >= 8, or the figure carries a secondary
   encoding on every mark of those categories (declared below, then checked).
4. Legibility at 6.5 in: every figure is 6.5 in wide; no text below 7 pt;
   no two text boxes overlap; no text box leaves the figure.

Usage: python review/tools/gate3_check.py
"""
import csv
import itertools
import json
import re
import sys
from pathlib import Path

REVIEW = Path(__file__).resolve().parents[1]
FIG = REVIEW / "figures"
DATA = FIG / "data"
PALETTE = {"#A10400", "#C00000", "#FBEDED", "#1A1A1A", "#8A8A8A", "#555555", "#DCDCD8",
           "#D9AD2B", "#F0E2B0", "#7F0300", "#FFFFFF"}
fails = []


def check(cond, msg):
    print(("ok   " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


def num(s):
    s = s.replace("−", "-").replace("$", "").replace("B", "").replace("%", "").replace(",", "").replace("+", "")
    return float(s)


meta = json.loads((FIG / "figures.json").read_text(encoding="utf-8"))
layout = json.loads((FIG / "layout_report.json").read_text(encoding="utf-8"))

# ---------------------------------------------------------------- 1. numbers
GROUP_FILL = {"A": "#A10400", "B": "#D9AD2B", "C": "#F0E2B0", "D": "#8A8A8A", "E": "#DCDCD8"}
NUM = re.compile(r"\d+(?:,\d{3})*(?:\.\d+)?")


def lum(hexc):
    c = [int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def groups(svg, gid):
    """Text of each <g id=gid> group (lines joined), with the first text's fill colour."""
    out = []
    for body in re.findall(rf'<g id="{gid}">(.*?)</g>', svg, re.S):
        parts = re.findall(r"<text([^>]*)>([^<]*)</text>", body)
        fill = re.search(r"fill: (#[0-9a-fA-F]{6})", parts[0][0]).group(1).upper() if parts else None
        out.append((" ".join(t for _, t in parts), fill))
    return out


def first_num(t):
    """The label's value: its first dollar amount if it has one, else its first number."""
    m = re.search(r"\$(" + NUM.pattern + ")", t) or NUM.search(t)
    return float(m.group(1 if m.re.groups else 0).replace(",", "")) if m else None


squash = lambda t: re.sub(r"\s+", "", t)

for m in meta:
    n = m["number"]
    svg = (FIG / f"{m['stem']}.svg").read_text(encoding="utf-8")
    texts = re.findall(r"<text[^>]*>([^<]*)</text>", svg)
    alltext = " ".join(texts)
    flat = squash("".join(texts))
    rows = list(csv.DictReader(open(DATA / m["csv"], encoding="utf-8")))
    labels = [first_num(t) for t, _ in groups(svg, "datalabel")]
    if "kind" in rows[0]:  # a converted v8 table: every cell, header and the source note, verbatim
        head0 = next(r["cell_text"] for r in rows if r["kind"] == "header")
        miss = [r["cell_text"] for r in rows if squash(r["cell_text"]) not in flat]
        check(not miss, f"fig{n}: all {len(rows)} table cells, headers and the source note appear verbatim" + (f" MISSING {miss}" if miss else ""))
        nums = {float(x.replace(",", "")) for r in rows for x in r["numbers"].split(";") if x}
        values = sorted(float(r["cell_text"].replace(",", "").rstrip("%")) for r in rows if r["kind"] == "cell"
                        and r["column"] != head0 and re.fullmatch(r"[\d.,]+%?", r["cell_text"]))
        got = sorted(abs(v) for v in labels)
        check(all(v in got for v in values) and all(v in nums for v in got),
              f"fig{n}: data labels {got} carry every value cell {values} and only CSV numbers")
        continue
    if n == 6:
        tiles = groups(svg, "tile")
        letters = groups(svg, "tileletter")
        check(len(tiles) == len(letters) == 51, f"fig6: 51 tiles with a group letter ({len(tiles)}, {len(letters)})")
        drawn = {t.rstrip("*"): (g, t.endswith("*")) for (t, _), (g, _) in zip(tiles, letters)}
        bad = [r["abbrev"] for r in rows if drawn.get(r["abbrev"], ("?",))[0] != r["group"]]
        check(not bad, f"fig6: every tile's letter equals its CSV group {bad or ''}")
        starred = sorted(a for a, (_, s_) in drawn.items() if s_)
        check(starred == ["CO", "MN", "MO"], f"fig6: symbol on {starred}")
        low_c = [(t, g, round(contrast(c, GROUP_FILL[g]), 2)) for (t, c), (g, c2) in zip(tiles, letters)
                 for c_ in (c, c2) if contrast(c_, GROUP_FILL[g]) < 4.5]
        worst = min(min(contrast(c, GROUP_FILL[g]), contrast(c2, GROUP_FILL[g])) for (t, c), (g, c2) in zip(tiles, letters))
        check(not low_c, f"fig6: every tile's abbreviation and letter clear 4.5:1 on its fill (lowest {worst:.2f}:1)" + (f" LOW {low_c}" if low_c else ""))
        for g in "ABCDE":
            k = sum(1 for r in rows if r["group"] == g)
            check(re.search(rf"\b{g}\. [^<]*\({k}\)", alltext) is not None, f"fig6: legend count for {g} = {k}")
        legend = [t for t, _ in groups(svg, "legend")]
        for g in "ABCDE":
            v = next(r["group_total_above_caps_billion"] for r in rows if r["group"] == g)
            shown = f"${v}B" if g != "E" else "$0"
            check(any(l.startswith(f"{g}. ") and shown in l for l in legend), f"fig6: legend {g} shows {shown} (CSV {v})")
        low = sorted(r["abbrev"] for r in rows if "lower threshold" in r["flag"])
        check("(" + ", ".join(low) + ")" in alltext, f"fig6: outline legend names {low}")
        heavy = len(re.findall(r"stroke: #1a1a1a; stroke-width: 2\.6", svg))
        red_strokes = svg.count("stroke: #a10400")
        red_fills = svg.count("fill: #a10400")
        check(heavy == len(low) and red_strokes == 0, f"fig6: {heavy} heavy ink outlines (want {len(low)}), {red_strokes} dark-red strokes")
        check(red_fills == 24 + 1, f"fig6: dark red fills only Group A (24 tiles + legend swatch: {red_fills})")
        continue
    plotted = [abs(float(r["value"])) for r in rows if not r["item"].startswith(("Note", "Total: the study"))]
    want = sorted(plotted + ([142.1] if n == 2 else []))  # $142.1B labels two bars in Figure 2
    got = sorted(abs(v) for v in labels)
    check(got == want, f"fig{n}: data labels {got} == CSV {want}")
    for r in rows:
        if r["item"].startswith(("Note", "Total: the study")):
            v = f"{float(r['value']):g}"
            check(v in alltext, f"fig{n}: value {v} printed ({r['role']})")

# ---------------------------------------------------------------- 2. colours
for m in meta:
    svg = (FIG / f"{m['stem']}.svg").read_text(encoding="utf-8")
    hexes = {h.upper() for h in re.findall(r"#[0-9a-fA-F]{6}\b", svg)}
    short = re.findall(r"(?:fill|stroke|color)\s*[:=]\s*\"?(#[0-9a-fA-F]{3})\b", svg)
    named = set(re.findall(r"(?:fill|stroke)\s*:\s*([a-z]+)\b", svg)) - {"none"}
    rgb = re.findall(r"rgba?\(", svg)
    off = sorted(hexes - PALETTE)
    check(not off and not short and not named and not rgb,
          f"{m['stem']}.svg colours {sorted(hexes)} all in palette" + (f" — OFF: {off} {short} {named} {rgb}" if off or short or named or rgb else ""))

# ---------------------------------------------------------------- 3. separation


def srgb_to_lin(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lin_to_oklab(r, g, b):
    l_ = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m_ = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s_ = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    return (0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
            1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
            0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_)


MACHADO = {
    "protan": [[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]],
    "deutan": [[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]],
    "tritan": [[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]],
}


def view(hexc, mode):
    rgb = [srgb_to_lin(int(hexc[i:i + 2], 16)) for i in (1, 3, 5)]
    if mode == "grey":
        y = 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]
        rgb = [y, y, y]
    elif mode != "normal":
        M = MACHADO[mode]
        rgb = [min(1, max(0, sum(M[i][j] * rgb[j] for j in range(3)))) for i in range(3)]
    return lin_to_oklab(*rgb)


def de(a, b, mode):
    pa, pb = view(a, mode), view(b, mode)
    return 100 * sum((x - y) ** 2 for x, y in zip(pa, pb)) ** 0.5


# categories per figure; `secondary` = every mark of every category also
# carries a text label naming it, verified below
CATS = {
    1: {"colours": {"2027 band": "#DCDCD8", "threshold line": "#1A1A1A", "3.5% floor": "#A10400"}, "secondary": "value labels"},
    2: {"colours": {"SDP rule": "#1A1A1A", "additional cut": "#8A8A8A", "overlap": "#F0E2B0"}, "secondary": "row and segment labels"},
    3: {"colours": {"federal": "#1A1A1A", "state": "#8A8A8A", "measured alone": "#F0E2B0"}, "secondary": "segment labels"},
    4: {"colours": {"payments and results": "#1A1A1A", "decreases": "#8A8A8A", "step 3, up to": "#DCDCD8", "range bracket": "#A10400"}, "secondary": "step labels"},
    5: {"colours": {"measured alone": "#8A8A8A", "overlap": "#F0E2B0", "on top of SDP rule": "#1A1A1A"}, "secondary": "axis label under each bar"},
    6: {"colours": {"A": "#A10400", "B": "#D9AD2B", "C": "#F0E2B0", "D": "#8A8A8A", "E": "#DCDCD8"}, "secondary": "group letter on every tile"},
    7: {"colours": {"pediatric": "#A10400", "adult": "#8A8A8A"}, "secondary": "row labels"},
    8: {"colours": {"total": "#A10400", "freestanding": "#1A1A1A", "short-term": "#8A8A8A"}, "secondary": "end labels on every line"},
    9: {"colours": {"central": "#A10400", "low- and high-savings": "#8A8A8A"}, "secondary": "row labels"},
}
for n, spec in CATS.items():
    for (na, a), (nb, b) in itertools.combinations(spec["colours"].items(), 2):
        worst = min((de(a, b, md), md) for md in ("normal", "grey", "protan", "deutan", "tritan"))
        ok = worst[0] >= 8
        note = "" if ok else f" — below 8, relies on secondary encoding: {spec['secondary']}"
        if not ok:
            # only Figure 6 declares a checked secondary encoding (part 1: a letter on all 51 tiles)
            ok = n == 6 and not any("tile's letter" in f for f in fails)
        check(ok, f"fig{n}: {na} vs {nb}: worst dE {worst[0]:.1f} ({worst[1]}){note}")

# ---------------------------------------------------------------- 4. legibility
for key, rep in layout.items():
    check(abs(rep["width_in"] - 6.5) < 1e-6, f"{key}: width {rep['width_in']} in")
    small = [t["text"] for t in rep["texts"] if t["size"] < 7]
    check(not small, f"{key}: no text below 7 pt (min {min(t['size'] for t in rep['texts'])} pt)")
    out = [t["text"][:30] for t in rep["texts"]
           if t["x0"] < -0.005 or t["y0"] < -0.005 or t["x1"] > rep["width_in"] + 0.005 or t["y1"] > rep["height_in"] + 0.005]
    check(not out, f"{key}: no text outside the figure {out or ''}")
    over = []
    for a, b in itertools.combinations(rep["texts"], 2):
        ix = min(a["x1"], b["x1"]) - max(a["x0"], b["x0"])
        iy = min(a["y1"], b["y1"]) - max(a["y0"], b["y0"])
        if ix > 0.01 and iy > 0.01:
            over.append((a["text"][:20], b["text"][:20]))
    check(not over, f"{key}: no overlapping text boxes {over or ''}")

print("\nGATE 3:", "FAIL (%d)" % len(fails) if fails else "PASS")
sys.exit(1 if fails else 0)
