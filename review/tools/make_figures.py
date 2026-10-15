"""Draw Figures 1–9 (article_v9 numbering) from review/figures/data/*.csv in the
THEIA palette.

Figures 1, 3, 4 and 9 replace v8 tables: each chart carries every cell of
its table (numbers, row labels, qualifiers and headers, verbatim) as labels
or a key, and the table's source note verbatim as its source line.

Outputs review/figures/figN_*.png (2400 px wide, 6.5 in at 369 dpi) and
.svg (text kept as text), plus review/figures/figures.json (title, caption,
alt text, source line, files) used by the v19 build and gate 3, and
review/figures/layout_report.json (every text box, for the overlap and
clipping check).

Layout follows the house chart layout: bold short title naming the measure,
grey subtitle with units and years, the plot, then a grey source line.

Usage: python review/tools/make_figures.py
"""
import csv
import json
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Rectangle  # noqa: E402

REVIEW = Path(__file__).resolve().parents[1]
FIG = REVIEW / "figures"
DATA = FIG / "data"

# THEIA palette
RED = "#A10400"
INK = "#1A1A1A"
GREY = "#8A8A8A"
MUTED = "#555555"
RULE = "#DCDCD8"
GOLD = "#D9AD2B"
PALE = "#F0E2B0"
WHITE = "#FFFFFF"

for f in sorted((Path.home() / ".fonts/theia-static").glob("InstrumentSans-*.ttf")):
    font_manager.fontManager.addfont(str(f))
FONT = "Instrument Sans"
plt.rcParams.update({
    "font.family": FONT,
    "svg.fonttype": "none",
    "text.color": INK,
    "axes.edgecolor": RULE,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.facecolor": WHITE,
    "figure.facecolor": WHITE,
    "savefig.facecolor": WHITE,
    "axes.unicode_minus": True,
    "hatch.color": INK,
    "text.parse_math": False,
})

W_IN = 6.5
DPI = 2400 / W_IN
T_SIZE, S_SIZE, L_SIZE, SRC_SIZE = 10.5, 8.5, 8, 7.5
LEFT_IN = 0.0  # titles align with the figure's left edge


def rows(name):
    with open(DATA / name, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def money(v, sign=False):
    s = f"{abs(v):,.1f}"
    if not sign:
        return f"${s}B"
    return ("+" if v > 0 else "−") + f"${s}B"


def header(fig, title, subtitle, h_in):
    """Title and subtitle at the top-left; returns the y (figure frac) below them."""
    top = 1 - 0.06 / h_in
    fig.text(0.0, top, title, fontsize=T_SIZE, fontweight="bold", color=INK, va="top", ha="left")
    fig.text(0.0, top - 0.24 / h_in, subtitle, fontsize=S_SIZE, color=MUTED, va="top", ha="left")
    return top - 0.46 / h_in


def source(fig, lines, h_in):
    """Source lines at the foot, added top to bottom so they read in order in the SVG."""
    for k, line in enumerate(lines):
        y = (0.04 + 0.15 * (len(lines) - 1 - k)) / h_in
        fig.text(0.0, y, line, fontsize=SRC_SIZE, color=MUTED, va="bottom", ha="left")


def wrap(text, width=118):
    return textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)


def lum(hexc):
    c = [int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def text_on(fill):
    """White only where it clears 4.5:1 on the fill; otherwise ink."""
    return WHITE if contrast(WHITE, fill) >= 4.5 else INK


def table_rows(name):
    """A converted-table CSV: (headers, body rows as lists of cell text, source note)."""
    r = rows(name)
    head = [x["cell_text"] for x in r if x["kind"] == "header"]
    body = {}
    for x in r:
        if x["kind"] == "cell":
            body.setdefault(x["row"], []).append(x["cell_text"])
    note = next(x["cell_text"] for x in r if x["kind"] == "note")
    return head, list(body.values()), note


def num(s):
    return float(s.replace(",", "").replace("$", "").replace("%", ""))


def label(ax, x, y, s, gid=None, **kw):
    kw.setdefault("fontsize", L_SIZE)
    kw.setdefault("color", INK)
    t = ax.text(x, y, s, **kw)
    if gid:
        t.set_gid(gid)
    return t


def clean(ax, grid_axis="x"):
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(False)
    ax.tick_params(length=0, labelsize=L_SIZE, colors=INK)
    if grid_axis:
        ax.grid(axis=grid_axis, color=RULE, linewidth=0.75)
        ax.set_axisbelow(True)


def save(fig, stem):
    fig.savefig(FIG / f"{stem}.png", dpi=DPI)
    fig.savefig(FIG / f"{stem}.svg")
    # layout report: every visible text box in inches
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    boxes = []
    for t in fig.findobj(matplotlib.text.Text):
        if not t.get_visible() or not t.get_text().strip():
            continue
        bb = t.get_window_extent(r)
        boxes.append({"text": t.get_text(), "gid": t.get_gid(), "size": t.get_fontsize(),
                      "x0": bb.x0 / fig.dpi, "y0": bb.y0 / fig.dpi,
                      "x1": bb.x1 / fig.dpi, "y1": bb.y1 / fig.dpi})
    w, h = fig.get_size_inches()
    plt.close(fig)
    return {"width_in": w, "height_in": h, "texts": boxes}


META = []
LAYOUT = {}





def source_note(fig, note, h, extra=()):
    """The table's source note, verbatim, wrapped, as the figure's source line."""
    source(fig, wrap(note) + list(extra), h)


# ---------------------------------------------------------------- Figure 1
def fig1():
    head, body, note = table_rows("fig1_threshold.csv")
    years = [b[0] for b in body]
    vals = [b[1] for b in body]
    lines = wrap(note)
    h = 3.15 + 0.15 * len(lines)
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Threshold in expansion states",
                   f"{head[1]}, by {head[0][0].lower()}{head[0][1:]}", h)
    bottom = (0.62 + 0.15 * len(lines)) / h
    ax = fig.add_axes([0.08, bottom, 0.80, y_top - bottom - 0.02])
    clean(ax, grid_axis="y")
    x = list(range(len(years)))
    # 2027: no fixed value; a band up to 6.0% with the qualifier, verbatim
    q = vals[0]
    cap = num(q.split("at most ")[1])
    ax.add_patch(Rectangle((-0.42, 0), 0.84, cap, facecolor=RULE, edgecolor="none", zorder=1))
    ax.plot([-0.42, 0.42], [cap, cap], color=INK, linewidth=1.2, linestyle=(0, (3, 2)), zorder=3)
    for k, line in enumerate(wrap(q, 15)):
        t = label(ax, 0, cap / 2 + 0.55 - k * 0.55, line, ha="center", va="center", fontsize=7.5, fontweight="bold")
        t.set_gid("qualifier")
    # 2028 on: the step line
    v = [num(t) for t in vals[1:]]
    xs, ys = [], []
    for i, val in enumerate(v, start=1):
        xs += [i - 0.5, i + 0.5]
        ys += [val, val]
    xs[-1] = len(years) - 0.5 + 0.25
    ax.plot(xs, ys, color=INK, linewidth=2, solid_joinstyle="miter", zorder=4)
    for i, (val, txt) in enumerate(zip(v, vals[1:]), start=1):
        label(ax, i, val + 0.18, txt, gid="datalabel", ha="center", va="bottom", fontweight="bold")
    # the 3.5% floor, the chart's one dark-red element
    floor = v[-1]
    ax.plot([0.5, len(years) - 0.25], [floor, floor], color=RED, linewidth=0.9, zorder=2)
    label(ax, len(years) - 0.2, floor, f"{vals[-1]} floor", ha="left", va="center", color=RED, fontweight="bold")
    ax.set_xlim(-0.55, len(years) + 0.35)
    ax.set_ylim(0, 7)
    ax.set_xticks(x, years, fontsize=L_SIZE, fontweight="bold")
    ax.set_yticks(range(0, 8), [f"{k}%" for k in range(0, 8)])
    ax.tick_params(axis="y", labelsize=L_SIZE - 0.5, colors=MUTED)
    ax.set_xlabel(head[0], fontsize=L_SIZE, color=MUTED, labelpad=4)
    ax.set_ylabel(head[1], fontsize=L_SIZE, color=MUTED, labelpad=4)
    source_note(fig, note, h)
    LAYOUT["fig1"] = save(fig, "fig1_threshold")
    steps = "; ".join(f"{y}, {t}" for y, t in zip(years, vals))
    META.append({
        "number": 1, "stem": "fig1_threshold", "csv": "fig1_threshold.csv",
        "title": "Threshold in expansion states",
        "alt": (f"Step chart of the threshold in expansion states by federal fiscal year (begins October 1 of the prior year): "
                f"{steps}. A dark-red reference line, labelled 3.5% floor, marks the 3.5% level that applies from 2032 on. {note}"),
    })


# ---------------------------------------------------------------- Figure 2
def fig2():
    d = {r["item"]: float(r["value"]) for r in rows("fig2_overlap.csv")}
    sdp, alone = d["SDP rule"], d["Provider tax rule, measured alone"]
    ov, add = d["Overlap: already counted in the SDP rule"], d["Provider tax rule, additional cut"]
    comb = d["Both rules combined"]
    h = 2.75
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Provider payment cuts in CMS’s estimates",
                   "Central estimates, billions of 2026 dollars, 2026–2035", h)
    ax = fig.add_axes([0.255, 0.20, 0.70, y_top - 0.21])
    clean(ax)
    bh = 0.42
    ys = {"SDP rule": 2, "Provider tax rule,\nmeasured alone": 1, "Both rules combined": 0}
    gap = 3
    ax.barh(2, sdp, height=bh, color=INK, linewidth=0)
    ax.barh(1, ov, height=bh, color=PALE, edgecolor=GOLD, linewidth=1.2)
    ax.barh(1, add - gap, left=ov + gap, height=bh, color=GREY, linewidth=0)
    ax.barh(0, sdp, height=bh, color=INK, linewidth=0)
    ax.barh(0, add - gap, left=sdp + gap, height=bh, color=GREY, linewidth=0)
    for y, val in ((2, sdp), (1, alone), (0, comb)):
        label(ax, val + 12, y, money(val), gid="datalabel", va="center", ha="left", fontweight="bold")
    label(ax, ov / 2, 1, money(ov), gid="datalabel", va="center", ha="center", fontweight="bold")
    label(ax, ov + add / 2, 1, money(add), gid="datalabel", va="center", ha="center", fontweight="bold")
    label(ax, sdp + add / 2, 0, money(add), gid="datalabel", va="center", ha="center", fontweight="bold")
    label(ax, 2, 1 - bh / 2 - 0.08, "already counted in the SDP rule", va="top", ha="left", fontweight="bold")
    label(ax, ov + gap, 1 + bh / 2 + 0.06, "additional cut", va="bottom", ha="left", color=MUTED)
    label(ax, sdp + gap, 0 + bh / 2 + 0.06, "additional cut", va="bottom", ha="left", color=MUTED)
    ax.set_yticks(list(ys.values()), list(ys.keys()), fontsize=L_SIZE, fontweight="bold")
    ax.set_ylim(-0.6, 2.55)
    ax.set_xlim(0, 1050)
    ax.set_xticks([0, 200, 400, 600, 800, 1000], ["$0", "$200B", "$400B", "$600B", "$800B", "$1,000B"])
    ax.tick_params(axis="x", labelsize=L_SIZE - 0.5, colors=MUTED)
    source(fig, ["Source: SDP rule (CMS-2449-P), Tables 18–20, 91 FR 30451–30452; provider tax rule (CMS-2452-P),",
                 "Table 11, 91 FR 46591, and 91 FR 46592. The combined total is THEIA Services’ arithmetic."], h)
    LAYOUT["fig2"] = save(fig, "fig2_overlap")
    META.append({
        "number": 2, "stem": "fig2_overlap", "csv": "fig2_overlap.csv",
        "title": "Provider payment cuts in CMS’s estimates",
        "alt": ("Horizontal bar chart of CMS’s central estimates, billions of 2026 dollars, 2026–2035: the SDP rule cuts provider "
                "payments by $774.8 billion; the provider tax rule measured alone cuts $384.0 billion, of which $241.9 billion "
                "is already counted in the SDP rule and $142.1 billion is an additional cut; both rules combined cut $916.9 billion "
                "($774.8 billion plus $142.1 billion)."),
    })


# ---------------------------------------------------------------- Figure 3
def fig3():
    head, body, note = table_rows("fig3_reductions.csv")
    labels = [b[0] for b in body]
    fed = [num(b[1]) for b in body]
    st = [num(b[2]) for b in body]
    tot = [num(b[3]) for b in body]
    lines = wrap(note)
    h = 4.05 + 0.15 * len(lines)
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Reduction in Medicaid spending by rule", head[0], h)
    # legend row: Federal, State, Total (the table's column headers)
    ly = y_top - 0.07 / h
    for k, (name, col) in enumerate(((head[1], INK), (head[2], GREY))):
        x0 = 0.0 + k * 0.85 / W_IN
        fig.patches.append(Rectangle((x0, ly - 0.07 / h), 0.13 / W_IN, 0.13 / h, transform=fig.transFigure,
                                     facecolor=col, edgecolor="none"))
        fig.text(x0 + 0.19 / W_IN, ly, name, fontsize=L_SIZE, va="center", ha="left", fontweight="bold")
    fig.text(1.70 / W_IN, ly, f"{head[3]}: at the end of each bar", fontsize=L_SIZE, va="center", ha="left", fontweight="bold")
    ly2 = ly - 0.22 / h
    fig.patches.append(Rectangle((0.0, ly2 - 0.065 / h), 0.13 / W_IN, 0.13 / h, transform=fig.transFigure,
                                 facecolor=PALE, edgecolor=GOLD, linewidth=1.0))
    fig.text(0.19 / W_IN, ly2, "Provider tax rule, measured alone: federal (left) and state (right) segments",
             fontsize=L_SIZE, va="center", ha="left", fontweight="bold")
    bottom = (0.55 + 0.15 * len(lines)) / h
    ax = fig.add_axes([0.335, bottom, 0.60, y_top - bottom - 0.10])
    clean(ax)
    bh = 0.40
    n = len(labels)
    gap = 4
    scale_in = 0.60 * W_IN / 1080  # inches per billion
    for i, (lab, f, s_, t) in enumerate(zip(labels, fed, st, tot)):
        y = n - 1 - i
        alone = "measured alone" in lab
        cf, cs = (PALE, PALE) if alone else (INK, GREY)
        ec, lw = (GOLD, 1.2) if alone else ("none", 0)
        ax.barh(y, f, height=bh, color=cf, edgecolor=ec, linewidth=lw)
        ax.barh(y, s_ - gap, left=f + gap, height=bh, color=cs, edgecolor=ec, linewidth=lw)
        label(ax, t + 12, y, money(t), gid="datalabel", va="center", ha="left", fontweight="bold")
        above_used = False
        for val, x0, col in ((f, 0, cf), (s_, f + gap, cs)):
            txt = money(val)
            w_in = val * scale_in
            if w_in > len(txt) * 0.07 + 0.08:
                label(ax, x0 + val / 2, y, txt, gid="datalabel", va="center", ha="center", fontweight="bold",
                      color=text_on(col))
            elif not above_used:  # too narrow: label above the segment, left-aligned on it
                label(ax, x0, y + bh / 2 + 0.05, txt, gid="datalabel", va="bottom", ha="left", fontweight="bold")
                above_used = True
            else:  # the slot above is taken: below
                label(ax, x0, y - bh / 2 - 0.05, txt, gid="datalabel", va="top", ha="left", fontweight="bold")
        if alone:
            label(ax, 0, y - bh / 2 - 0.05, "Includes the $241.9B overlap; not added to the combined total",
                  va="top", ha="left", fontweight="bold", fontsize=7.5)
    ax.set_yticks([n - 1 - i for i in range(n)], ["\n".join(wrap(l, 34)) for l in labels], fontsize=L_SIZE,
                  fontweight="bold")
    ax.set_ylim(-0.5, n - 0.45)
    ax.set_xlim(0, 1080)
    ax.set_xticks([0, 200, 400, 600, 800, 1000], ["$0", "$200B", "$400B", "$600B", "$800B", "$1,000B"])
    ax.tick_params(axis="x", labelsize=L_SIZE - 0.5, colors=MUTED)
    source_note(fig, note, h)
    LAYOUT["fig3"] = save(fig, "fig3_reductions")
    rows_txt = "; ".join(f"{l}: federal {money(f)}, state {money(s_)}, total {money(t)}"
                         for l, f, s_, t in zip(labels, fed, st, tot))
    META.append({
        "number": 3, "stem": "fig3_reductions", "csv": "fig3_reductions.csv",
        "title": "Reduction in Medicaid spending by rule",
        "alt": (f"Stacked bar chart, {head[0]}, federal and state: {rows_txt}. The provider tax rule measured alone includes "
                f"the $241.9 billion overlap and is not added to the combined total. {note}"),
    })


# ---------------------------------------------------------------- Figure 4
def fig4():
    head, body, note = table_rows("fig4_steps.csv")
    steps = [b[0] for b in body]
    res = [num(b[1]) for b in body]          # 916.9, 753.2, 488.5
    sdp, add = 774.8, 142.1                  # step 1's components, from its own label
    assert "$774.8 billion" in steps[0] and "$142.1 billion" in steps[0]
    cut2 = round(res[0] - res[1], 1)         # 163.7, printed in step 2's label
    cut3 = round(res[1] - res[2], 1)         # 264.7, printed in step 3's label
    assert f"${cut2} billion" in steps[1] and f"${cut3} billion" in steps[2]
    key_lines = [l for st_ in steps for l in wrap(st_, 112)]
    lines = wrap(note)
    key_top_in = 0.04 + 0.15 * len(lines) + 0.14 + 0.15 * len(key_lines)
    axes_bottom_in = key_top_in + 0.48
    h = axes_bottom_in + 2.45 + 0.52
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Loss to providers, central estimate", f"{head[0]} · {head[1]}", h)
    bottom = axes_bottom_in / h
    ax = fig.add_axes([0.10, bottom, 0.62, y_top - bottom - 0.02])
    clean(ax, grid_axis="y")
    bw = 0.72
    ax.bar(0, sdp, width=bw, color=INK, linewidth=0)
    ax.bar(0, add - 4, bottom=sdp + 4, width=bw, color=GREY, linewidth=0)
    ax.bar(1, cut2, bottom=res[1], width=bw, color=GREY, linewidth=0)
    ax.bar(2, res[1], width=bw, color=INK, linewidth=0)
    ax.bar(3, cut3, bottom=res[2], width=bw, facecolor=RULE, edgecolor=GREY, linewidth=1.0, linestyle=(0, (3, 2)))
    ax.bar(4, res[2], width=bw, color=INK, linewidth=0)
    for a, b, yv in ((0, 1, res[0]), (1, 2, res[1]), (2, 3, res[1]), (3, 4, res[2])):
        ax.plot([a + bw / 2, b - bw / 2], [yv, yv], color=GREY, linewidth=0.75)
    label(ax, 0, res[0] + 12, money(res[0]), gid="datalabel", ha="center", va="bottom", fontweight="bold")
    label(ax, 0, sdp / 2, money(sdp), gid="datalabel", ha="center", va="center", fontweight="bold", color=text_on(INK))
    label(ax, 0, sdp + add / 2, money(add), gid="datalabel", ha="center", va="center", fontweight="bold", color=text_on(GREY))
    label(ax, 1, res[1] + cut2 / 2, "−" + money(cut2), gid="datalabel", ha="center", va="center", fontweight="bold",
          color=text_on(GREY), fontsize=7.5)
    label(ax, 2, res[1] + 12, money(res[1]), gid="datalabel", ha="center", va="bottom", fontweight="bold")
    label(ax, 3, res[2] + cut3 / 2, "up to\n−" + money(cut3), gid="datalabel", ha="center", va="center",
          fontweight="bold", fontsize=7.5)
    label(ax, 4, res[2] + 12, money(res[2]), gid="datalabel", ha="center", va="bottom", fontweight="bold")
    # the range bracket: the chart's one dark-red element
    bx = 4.55
    ax.plot([bx, bx], [res[2], res[1]], color=RED, linewidth=1.6, solid_capstyle="butt")
    for yv in (res[2], res[1]):
        ax.plot([bx - 0.08, bx], [yv, yv], color=RED, linewidth=1.6)
    ax.plot([2 + bw / 2, bx - 0.08], [res[1], res[1]], color=RULE, linewidth=0.75, zorder=0)
    label(ax, bx + 0.12, (res[1] + res[2]) / 2, "Range under\nCMS’s central\nestimates:\n$488B–$753B",
          ha="left", va="center", fontweight="bold", clip_on=False)
    ax.set_xticks(range(5), ["Step 1", "Step 2", "After\nstep 2", "Step 3", "After\nstep 3"], fontsize=L_SIZE,
                  fontweight="bold")
    ax.set_xlim(-0.5, 4.75)
    ax.set_ylim(0, 1000)
    ax.set_yticks([0, 200, 400, 600, 800, 1000], ["$0", "$200B", "$400B", "$600B", "$800B", "$1,000B"])
    ax.tick_params(axis="y", labelsize=L_SIZE - 0.5, colors=MUTED)
    # the steps, verbatim, as a key under the chart
    y = key_top_in / h
    for line in key_lines:
        t = fig.text(0.0, y, line, fontsize=SRC_SIZE, color=INK, va="top", ha="left")
        t.set_gid("key")
        y -= 0.15 / h
    source_note(fig, note, h)
    LAYOUT["fig4"] = save(fig, "fig4_steps")
    META.append({
        "number": 4, "stem": "fig4_steps", "csv": "fig4_steps.csv",
        "title": "Loss to providers, central estimate",
        "alt": (f"Waterfall chart, {head[0]}, {head[1]}. {steps[0]}: {res[0]}. {steps[1]}: {res[1]}. {steps[2]}: {res[2]}. "
                f"A bracket marks the range under CMS’s central estimates, about $488 billion to $753 billion. {note}"),
    })


# ---------------------------------------------------------------- Figure 5
def fig5():
    r = rows("fig5_waterfall.csv")
    start, step, end, comp = (float(x["value"]) for x in r)
    h = 3.35
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "The provider tax rule’s net effect on providers",
                   "CMS central estimate, billions of 2026 dollars, 2026–2035", h)
    ax = fig.add_axes([0.10, 0.27, 0.87, y_top - 0.30])
    clean(ax, grid_axis="y")
    bw = 0.5
    ax.bar(0, start, width=bw, color=GREY, linewidth=0)
    ax.bar(1, step, bottom=start, width=bw, color=PALE, edgecolor=GOLD, linewidth=1.2)
    ax.bar(2, end, width=bw, color=INK, linewidth=0)
    ax.axhline(0, color=INK, linewidth=0.8)
    ax.plot([0 + bw / 2, 1 - bw / 2], [start, start], color=GREY, linewidth=0.75)
    ax.plot([1 + bw / 2, 2 - bw / 2], [start + step, start + step], color=GREY, linewidth=0.75)
    label(ax, 0, start - 10, money(start, sign=True), gid="datalabel", ha="center", va="top", fontweight="bold")
    label(ax, 1, start + step / 2, money(step, sign=True), gid="datalabel", ha="center", va="center", fontweight="bold")
    label(ax, 2, end + 10, money(end, sign=True), gid="datalabel", ha="center", va="bottom", fontweight="bold")
    ax.set_xticks([0, 1, 2], ["Measured alone\n(Table 12)", "Overlap already counted\nin the SDP rule",
                              "On top of the SDP rule\n(Table 14)"], fontsize=L_SIZE, fontweight="bold")
    ax.tick_params(axis="x", pad=6)
    ax.set_ylim(-265, 75)
    ax.set_xlim(-0.5, 2.5)
    ax.set_yticks([-250, -200, -150, -100, -50, 0, 50],
                  ["−$250B", "−$200B", "−$150B", "−$100B", "−$50B", "$0", "+$50B"])
    ax.tick_params(axis="y", labelsize=L_SIZE - 0.5, colors=MUTED)
    source(fig, ["Source: provider tax rule (CMS-2452-P), Table 12 (91 FR 46592) and Table 14 (91 FR 46593); 91 FR 46590–46593.",
                 f"Note: the components give +${comp:.1f}B ($163.7B less $142.1B); the difference from CMS’s +${end:.1f}B is",
                 "CMS’s rounding (Appendix E)."], h)
    LAYOUT["fig5"] = save(fig, "fig5_waterfall")
    META.append({
        "number": 5, "stem": "fig5_waterfall", "csv": "fig5_waterfall.csv",
        "title": "The provider tax rule’s net effect on providers",
        "alt": ("Waterfall chart, CMS central estimate, billions of 2026 dollars, 2026–2035: measured alone, the provider tax rule "
                "leaves providers $220.3 billion worse off (CMS Table 12); adding back the $241.9 billion overlap already counted "
                "in the SDP rule gives CMS’s +$21.7 billion on top of the SDP rule (Table 14). The components give +$21.6 billion "
                "($163.7 billion less $142.1 billion); the difference is CMS’s rounding (Appendix E)."),
    })


# ---------------------------------------------------------------- Figure 6
TILES = {
    "AK": (0, 0), "ME": (11, 0),
    "WI": (6, 1), "VT": (10, 1), "NH": (11, 1),
    "WA": (1, 2), "ID": (2, 2), "MT": (3, 2), "ND": (4, 2), "MN": (5, 2), "IL": (6, 2), "MI": (7, 2),
    "NY": (9, 2), "MA": (10, 2),
    "OR": (1, 3), "NV": (2, 3), "WY": (3, 3), "SD": (4, 3), "IA": (5, 3), "IN": (6, 3), "OH": (7, 3),
    "PA": (8, 3), "NJ": (9, 3), "CT": (10, 3), "RI": (11, 3),
    "CA": (1, 4), "UT": (2, 4), "CO": (3, 4), "NE": (4, 4), "MO": (5, 4), "KY": (6, 4), "WV": (7, 4),
    "VA": (8, 4), "MD": (9, 4), "DE": (10, 4),
    "AZ": (2, 5), "NM": (3, 5), "KS": (4, 5), "AR": (5, 5), "TN": (6, 5), "NC": (7, 5), "SC": (8, 5),
    "DC": (9, 5),
    "OK": (4, 6), "LA": (5, 6), "MS": (6, 6), "AL": (7, 6), "GA": (8, 6),
    "HI": (0, 7), "TX": (4, 7), "FL": (9, 7),
}
GROUP_FILL = {"A": RED, "B": GOLD, "C": PALE, "D": GREY, "E": RULE}
# the group names of the sec. 6 table, verbatim
GROUP_NAME = {
    "A": "Both rules",
    "B": "Cap plus lower threshold on non-hospital taxes",
    "C": "Cap only",
    "D": "Non-expansion states with SDPs above the caps",
    "E": "No identified hospital SDPs above the caps",
}


def fig6():
    st = rows("fig6_state_groups.csv")
    assert sorted(TILES) == sorted(r["abbrev"] for r in st), "tile grid must hold exactly the 51 jurisdictions"
    counts = {g: sum(1 for r in st if r["group"] == g) for g in "ABCDE"}
    h = 6.35
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Parts of the two proposed rules that reach each state",
                   "THEIA Services’ state groups A–E, 50 states and DC; groups show where the rules apply, not loss size", h)
    fig.text(0.0, y_top + 0.07 / h, "Legend dollars: each group’s federal hospital SDP spending above the caps in one year (KFF)",
             fontsize=S_SIZE, color=MUTED, va="top", ha="left")
    y_top -= 0.14 / h
    grid_h_in = 3.25
    ax = fig.add_axes([0.0, y_top - (grid_h_in + 0.05) / h, 1.0, grid_h_in / h])
    ax.set_xlim(-0.1, 12.0)
    ax.set_ylim(8.0, -0.1)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    s, gap = 0.92, 0.08
    for r in st:
        c, rr = TILES[r["abbrev"]]
        g = r["group"]
        low = "lower threshold" in r["flag"]
        ax.add_patch(Rectangle((c + gap / 2, rr + gap / 2), s, s, facecolor=GROUP_FILL[g], edgecolor="none"))
        if low:  # heavy ink outline, drawn inside the tile so it never touches a neighbour
            ax.add_patch(Rectangle((c + gap / 2 + 0.05, rr + gap / 2 + 0.05), s - 0.10, s - 0.10,
                                   facecolor="none", edgecolor=INK, linewidth=2.6))
        mark = "*" if (r["abbrev"] == "CO" or "no KFF estimate" in r["flag"]) else ""
        cx, cy = c + gap / 2 + s / 2, rr + gap / 2 + s / 2
        t = ax.text(cx, cy - 0.10, r["abbrev"] + mark, ha="center", va="center", fontsize=8.5,
                    fontweight="bold", color=text_on(GROUP_FILL[g]))
        t.set_gid("tile")
        t2 = ax.text(cx, cy + 0.24, g, ha="center", va="center", fontsize=7, color=text_on(GROUP_FILL[g]))
        t2.set_gid("tileletter")
    leg_top = y_top - (grid_h_in + 0.22) / h
    line_h = 0.235 / h
    for i, g in enumerate("ABCDE"):
        y = leg_top - i * line_h
        fig.patches.append(Rectangle((0.0, y - 0.075 / h), 0.16 / W_IN, 0.16 / h, transform=fig.transFigure,
                                     facecolor=GROUP_FILL[g], edgecolor="none"))
        fig.text(0.08 / W_IN, y + 0.005 / h, g, fontsize=7, color=text_on(GROUP_FILL[g]), ha="center", va="center",
                 fontweight="bold")
        usd = next(r["group_total_above_caps_billion"] for r in st if r["group"] == g)
        usd = f"about ${usd}B" if g != "E" else "$0 (excludes Colorado’s SDP)"
        t = fig.text(0.26 / W_IN, y, f"{g}. {GROUP_NAME[g]} ({counts[g]}): {usd}", fontsize=L_SIZE, color=INK,
                     va="center", ha="left")
        t.set_gid("legend")
    y = leg_top - 5 * line_h
    fig.patches.append(Rectangle((0.0, y - 0.08 / h), 0.16 / W_IN, 0.16 / h, transform=fig.transFigure,
                                 facecolor=RULE, edgecolor="none"))
    fig.patches.append(Rectangle((0.02 / W_IN, y - 0.06 / h), 0.12 / W_IN, 0.12 / h, transform=fig.transFigure,
                                 facecolor="none", edgecolor=INK, linewidth=2.0))
    fig.text(0.26 / W_IN, y, "Heavy dark outline: Group E state whose provider tax the lower threshold reaches "
             "(AR, CO, CT, IN, VT)", fontsize=L_SIZE, color=INK, va="center", ha="left")
    y -= line_h
    fig.text(0.0, y, "* Not in KFF’s dollar figures: Minnesota and Missouri (Group A) have no KFF estimate;",
             fontsize=L_SIZE, color=INK, va="center", ha="left")
    fig.text(0.0, y - 0.17 / h, "   Colorado (Group E) has an SDP above the new limits that KFF’s figures leave out.",
             fontsize=L_SIZE, color=INK, va="center", ha="left")
    source(fig, ["Source: THEIA Services’ grouping from KFF, August 14, 2026 (hospital SDPs above the caps) and August 20, 2026",
                 "(provider taxes above 3.5%), and KFF’s Medicaid expansion tracker; KFF does not use these groups (Appendix H)."], h)
    LAYOUT["fig6"] = save(fig, "fig6_state_map")
    members = {g: ", ".join(sorted(r["abbrev"] for r in st if r["group"] == g)) for g in "ABCDE"}
    usd = {g: next(r["group_total_above_caps_billion"] for r in st if r["group"] == g) for g in "ABCDE"}
    META.append({
        "number": 6, "stem": "fig6_state_map", "csv": "fig6_state_groups.csv",
        "title": "Parts of the two proposed rules that reach each state",
        "alt": ("Tile map of the 50 states and DC in five groups, showing where the rules apply, not where losses are largest; "
                "dollars are each group’s federal hospital SDP spending above the caps in one year (KFF). "
                f"A, both rules, {counts['A']} states, about ${usd['A']} billion: {members['A']}. "
                f"B, cap plus lower threshold on non-hospital taxes, {counts['B']}, about ${usd['B']} billion: {members['B']}. "
                f"C, cap only, {counts['C']}, about ${usd['C']} billion: {members['C']}. "
                f"D, non-expansion states with SDPs above the caps, {counts['D']}, about ${usd['D']} billion: {members['D']}. "
                f"E, no identified hospital SDPs above the caps, {counts['E']}, $0, excluding Colorado’s SDP: {members['E']}; "
                "the lower threshold reaches AR, CO, CT, IN and VT. Minnesota and Missouri have no KFF estimate; Colorado has an "
                "SDP above the new limits that KFF’s figures leave out."),
    })


# ---------------------------------------------------------------- Figure 7
def fig7():
    r = rows("fig7_pediatric.csv")
    ped, adult = (float(x["value"]) for x in r)
    h = 2.25
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Change in hospital inpatient units", "Percent change in the number of units, United States, 2008–2022", h)
    ax = fig.add_axes([0.25, 0.25, 0.70, y_top - 0.29])
    clean(ax)
    bh = 0.42
    ax.barh(1, ped, height=bh, color=RED, linewidth=0)
    ax.barh(0, adult, height=bh, color=GREY, linewidth=0)
    ax.axvline(0, color=INK, linewidth=0.8)
    label(ax, ped - 0.6, 1, f"−{abs(ped):.1f}%", gid="datalabel", ha="right", va="center", fontweight="bold")
    label(ax, adult - 0.6, 0, f"−{abs(adult):.1f}%", gid="datalabel", ha="right", va="center", fontweight="bold")
    ax.set_yticks([1, 0], ["Pediatric inpatient units", "Adult inpatient units"], fontsize=L_SIZE, fontweight="bold")
    ax.set_xlim(-37, 2)
    ax.set_ylim(-0.5, 1.5)
    ax.set_xticks([-35, -30, -25, -20, -15, -10, -5, 0], ["−35%", "−30%", "−25%", "−20%", "−15%", "−10%", "−5%", "0%"])
    ax.tick_params(axis="x", labelsize=L_SIZE - 0.5, colors=MUTED)
    source(fig, ["Source: Michelson et al., December 2024."], h)
    LAYOUT["fig7"] = save(fig, "fig7_pediatric")
    META.append({
        "number": 7, "stem": "fig7_pediatric", "csv": "fig7_pediatric.csv",
        "title": "Change in hospital inpatient units",
        "alt": ("Bar chart from one national study, percent change in the number of units, United States, 2008–2022: pediatric "
                "inpatient units fell 29.9 percent and adult inpatient units fell 4.4 percent. Source: Michelson et al., December 2024."),
    })


# ---------------------------------------------------------------- Figure 8
def fig8():
    r = rows("fig8_psychiatric.csv")
    series = {}
    parts = None
    for x in r:
        if x["item"].startswith("Total: the study"):
            parts = float(x["value"])
            continue
        series.setdefault(x["item"], {})[int(x["year"])] = float(x["value"])
    style = {"Freestanding psychiatric hospitals": INK, "Short-term acute care hospitals": GREY, "Total": RED}
    h = 3.05
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Psychiatric beds per 100,000 people, by hospital type", "United States, 2011 and 2023", h)
    ax = fig.add_axes([0.10, 0.13, 0.40, y_top - 0.21])
    clean(ax, grid_axis=None)
    for name, pts in series.items():
        c = style[name]
        ax.plot([0, 1], [pts[2011], pts[2023]], color=c, linewidth=2, solid_capstyle="round", zorder=3)
        ax.scatter([0, 1], [pts[2011], pts[2023]], s=42, color=c, edgecolor=WHITE, linewidth=1.5, zorder=4)
        label(ax, -0.05, pts[2011], f"{pts[2011]:g}", gid="datalabel", ha="right", va="center", fontweight="bold")
        if name == "Total":
            label(ax, 1.05, pts[2023], f"{pts[2023]:g} (the study’s total; its two parts sum to {parts:g})",
                  gid="datalabel", ha="left", va="center", fontweight="bold", clip_on=False)
            label(ax, 1.05, pts[2023] + 2.3, "Total, both types", ha="left", va="center", fontweight="bold", clip_on=False)
        else:
            label(ax, 1.05, pts[2023], f"{pts[2023]:g}", gid="datalabel", ha="left", va="center", fontweight="bold")
            label(ax, 1.27, pts[2023], name, ha="left", va="center", fontweight="bold", clip_on=False)
    ax.set_xlim(-0.25, 1.25)
    ax.set_ylim(7.5, 32)
    ax.set_xticks([0, 1], ["2011", "2023"], fontsize=L_SIZE, fontweight="bold")
    ax.set_yticks([])
    ax.xaxis.set_ticks_position("top")
    ax.tick_params(axis="x", labeltop=True, labelbottom=False, pad=4)
    for x in (0, 1):
        ax.axvline(x, color=RULE, linewidth=0.75, zorder=1)
    source(fig, ["Source: Lindenfeld et al., PLoS Medicine, July 2025."], h)
    LAYOUT["fig8"] = save(fig, "fig8_psychiatric")
    META.append({
        "number": 8, "stem": "fig8_psychiatric", "csv": "fig8_psychiatric.csv",
        "title": "Psychiatric beds per 100,000 people, by hospital type",
        "alt": ("Slope chart of psychiatric beds per 100,000 people, United States, 2011 and 2023: short-term acute care hospitals "
                "fell from 11.3 to 9.06, freestanding psychiatric hospitals rose from 16.8 to 19.5, and the total, both types, was "
                f"28.1 and 28.4 (the study’s total; its two parts sum to {parts:g}). Source: Lindenfeld et al., PLoS Medicine, July 2025."),
    })


# ---------------------------------------------------------------- Figure 9
def fig9():
    head, body, note = table_rows("fig9_range.csv")
    rowlab = [b[0] for b in body]          # after step 2, step 3 ceiling, after step 3
    est = head[1:]                          # low-savings, central, high-savings
    after2 = [num(x) for x in body[0][1:]]
    ceil = [num(x) for x in body[1][1:]]
    after3 = [num(x) for x in body[2][1:]]
    lines = wrap(note)
    h = 3.0 + 0.15 * len(lines)
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Loss to providers, by estimate", head[0], h)
    bottom = (0.62 + 0.15 * len(lines)) / h
    ax = fig.add_axes([0.20, bottom, 0.76, y_top - bottom - 0.16])
    clean(ax)
    n = len(est)
    for i in range(n):
        y = n - 1 - i
        col = RED if est[i].startswith("Central") else GREY
        ax.plot([after3[i], after2[i]], [y, y], color=col, linewidth=7, solid_capstyle="butt", zorder=3)
        ax.scatter([after3[i], after2[i]], [y, y], s=60, color=col, edgecolor=WHITE, linewidth=1.5, zorder=4)
        label(ax, after3[i] - 18, y, money(after3[i]), gid="datalabel", ha="right", va="center", fontweight="bold")
        label(ax, after2[i] + 18, y, money(after2[i]), gid="datalabel", ha="left", va="center", fontweight="bold")
        label(ax, (after2[i] + after3[i]) / 2, y - 0.22, f"step 3 ceiling {money(ceil[i])}", gid="datalabel",
              ha="center", va="top", fontsize=7.5, color=INK)
    ax.set_yticks([n - 1 - i for i in range(n)], est, fontsize=L_SIZE, fontweight="bold")
    ax.set_ylim(-0.7, n - 0.4)
    ax.set_xlim(0, 1260)
    ax.set_xticks([0, 200, 400, 600, 800, 1000, 1200], ["$0", "$200B", "$400B", "$600B", "$800B", "$1,000B", "$1,200B"])
    ax.tick_params(axis="x", labelsize=L_SIZE - 0.5, colors=MUTED)
    # key: the table's three row labels, verbatim
    ky = y_top + 0.02 / h
    fig.text(0.0, ky, f"Left end: {rowlab[2]}.  Right end: {rowlab[0]}.", fontsize=7.5, va="top", ha="left",
             fontweight="bold")
    fig.text(0.0, ky - 0.15 / h, f"Bar length: {rowlab[1]} (labelled under each bar).", fontsize=7.5, va="top",
             ha="left", fontweight="bold")
    source_note(fig, note, h)
    LAYOUT["fig9"] = save(fig, "fig9_range")
    rows_txt = "; ".join(f"{e}: {rowlab[2]} {money(a3)}, {rowlab[0]} {money(a2)}, {rowlab[1]} {money(c)}"
                         for e, a3, a2, c in zip(est, after3, after2, ceil))
    META.append({
        "number": 9, "stem": "fig9_range", "csv": "fig9_range.csv",
        "title": "Loss to providers, by estimate",
        "alt": f"Range chart, {head[0]}, one row per estimate. {rows_txt}. {note}",
    })


if __name__ == "__main__":
    for f in (fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9):
        f()
    (FIG / "figures.json").write_text(json.dumps(META, indent=2, ensure_ascii=False), encoding="utf-8")
    (FIG / "layout_report.json").write_text(json.dumps(LAYOUT, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", ", ".join(m["stem"] for m in META))
