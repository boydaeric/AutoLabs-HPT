"""Gate 3: check the rendered figures.

1. Numbers: each figure's data labels (SVG text in <g id="datalabel">) equal
   its CSV values; note values appear in the figure's text; Figure 3's
   tiles carry each state's CSV group and the legend carries the counts.
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
for m in meta:
    svg = (FIG / f"{m['stem']}.svg").read_text(encoding="utf-8")
    texts = re.findall(r"<text[^>]*>([^<]*)</text>", svg)
    alltext = " ".join(texts)
    rows = list(csv.DictReader(open(DATA / m["csv"], encoding="utf-8")))
    if m["number"] == 3:
        tiles = re.findall(r'<g id="tile">\s*<text[^>]*>([^<]*)</text>', svg)
        letters = re.findall(r'<g id="tileletter">\s*<text[^>]*>([^<]*)</text>', svg)
        check(len(tiles) == len(letters) == 51, f"fig3: 51 tiles with a group letter ({len(tiles)}, {len(letters)})")
        drawn = {t.rstrip("*"): (g, t.endswith("*")) for t, g in zip(tiles, letters)}
        bad = [r["abbrev"] for r in rows if drawn.get(r["abbrev"], ("?",))[0] != r["group"]]
        check(not bad, f"fig3: every tile's letter equals its CSV group {bad or ''}")
        starred = sorted(a for a, (_, s) in drawn.items() if s)
        check(starred == ["CO", "MN", "MO"], f"fig3: symbol on {starred}")
        for g in "ABCDE":
            n = sum(1 for r in rows if r["group"] == g)
            check(f"({n})" in alltext and re.search(rf"\b{g}\. [^<]*\({n}\)", alltext) is not None,
                  f"fig3: legend count for {g} = {n}")
        low = sorted(r["abbrev"] for r in rows if "lower threshold" in r["flag"])
        check("(" + ", ".join(low) + ")" in alltext, f"fig3: outline legend names {low}")
        n_outline = svg.count("stroke: #a10400")
        check(n_outline >= len(low), f"fig3: {n_outline} red outlines drawn (>= {len(low)})")
        continue
    labels = [num(t) for t in re.findall(r'<g id="datalabel">\s*<text[^>]*>([^<]*)</text>', svg)]
    plotted = [float(r["value"]) for r in rows if not r["item"].startswith("Note")]
    want = sorted(plotted)
    got = sorted(labels)
    if m["number"] == 1:  # $142.1B labels both the provider tax bar and the combined bar
        want = sorted(plotted + [142.1])
    check(got == want, f"fig{m['number']}: data labels {got} == CSV {want}")
    for r in rows:
        if r["item"].startswith("Note"):
            v = f"{float(r['value']):g}"
            check(v in alltext, f"fig{m['number']}: note value {v} printed")

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
    1: {"colours": {"SDP rule": "#1A1A1A", "additional cut": "#8A8A8A", "overlap": "#F0E2B0"}, "secondary": "row and segment labels"},
    2: {"colours": {"measured alone": "#8A8A8A", "overlap": "#F0E2B0", "on top of SDP rule": "#1A1A1A"}, "secondary": "axis label under each bar"},
    3: {"colours": {"A": "#A10400", "B": "#D9AD2B", "C": "#F0E2B0", "D": "#8A8A8A", "E": "#DCDCD8"}, "secondary": "group letter on every tile"},
    4: {"colours": {"pediatric": "#A10400", "adult": "#8A8A8A"}, "secondary": "row labels"},
    5: {"colours": {"total": "#A10400", "freestanding": "#1A1A1A", "short-term": "#8A8A8A"}, "secondary": "end labels on every line"},
}
for n, spec in CATS.items():
    for (na, a), (nb, b) in itertools.combinations(spec["colours"].items(), 2):
        worst = min((de(a, b, md), md) for md in ("normal", "grey", "protan", "deutan", "tritan"))
        ok = worst[0] >= 8
        note = "" if ok else f" — below 8, relies on secondary encoding: {spec['secondary']}"
        if not ok:
            # only Figure 3 declares a checked secondary encoding (part 1: a letter on all 51 tiles)
            ok = n == 3 and not any("tile's letter" in f for f in fails)
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
