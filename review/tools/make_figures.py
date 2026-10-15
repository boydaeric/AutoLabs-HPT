"""Draw Figures 1–5 from review/figures/data/*.csv in the THEIA palette.

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
    y = 0.04 / h_in
    for line in reversed(lines):
        fig.text(0.0, y, line, fontsize=SRC_SIZE, color=MUTED, va="bottom", ha="left")
        y += 0.15 / h_in


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


# ---------------------------------------------------------------- Figure 1
def fig1():
    d = {r["item"]: float(r["value"]) for r in rows("fig1_overlap.csv")}
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
    gap = 3  # 2 px surface gap, in data units at this scale
    # SDP rule
    ax.barh(2, sdp, height=bh, color=INK, linewidth=0)
    # Provider tax rule alone: overlap (pale gold, gold outline) + additional cut
    ax.barh(1, ov, height=bh, color=PALE, edgecolor=GOLD, linewidth=1.2)
    ax.barh(1, add - gap, left=ov + gap, height=bh, color=GREY, linewidth=0)
    # Combined: SDP rule + additional cut
    ax.barh(0, sdp, height=bh, color=INK, linewidth=0)
    ax.barh(0, add - gap, left=sdp + gap, height=bh, color=GREY, linewidth=0)
    # tip values
    for y, v in ((2, sdp), (1, alone), (0, comb)):
        label(ax, v + 12, y, money(v), gid="datalabel", va="center", ha="left", fontweight="bold")
    # segment labels
    label(ax, ov / 2, 1, money(ov), gid="datalabel", va="center", ha="center", fontweight="bold")
    label(ax, ov + add / 2, 1, money(add), gid="datalabel", va="center", ha="center", fontweight="bold")
    label(ax, sdp + add / 2, 0, money(add), gid="datalabel", va="center", ha="center", fontweight="bold")
    # annotations for the two provider tax segments
    label(ax, 2, 1 - bh / 2 - 0.08, "already counted in the SDP rule", va="top", ha="left",
          fontweight="bold", fontsize=L_SIZE)
    label(ax, ov + gap, 1 + bh / 2 + 0.06, "additional cut", va="bottom", ha="left", fontsize=L_SIZE,
          color=MUTED)
    label(ax, sdp + gap, 0 + bh / 2 + 0.06, "additional cut", va="bottom", ha="left", fontsize=L_SIZE,
          color=MUTED)
    ax.set_yticks(list(ys.values()), list(ys.keys()), fontsize=L_SIZE, fontweight="bold")
    ax.set_ylim(-0.6, 2.55)
    ax.set_xlim(0, 1050)
    ax.set_xticks([0, 200, 400, 600, 800, 1000], ["$0", "$200B", "$400B", "$600B", "$800B", "$1,000B"])
    ax.tick_params(axis="x", labelsize=L_SIZE - 0.5, colors=MUTED)
    source(fig, ["Source: SDP rule (CMS-2449-P), Tables 18–20, 91 FR 30451–30452; provider tax rule (CMS-2452-P),",
                 "Table 11, 91 FR 46591, and 91 FR 46592. The combined total is THEIA Services’ arithmetic."], h)
    LAYOUT["fig1"] = save(fig, "fig1_overlap")
    META.append({
        "number": 1, "stem": "fig1_overlap", "csv": "fig1_overlap.csv",
        "title": "Provider payment cuts in CMS’s estimates",
        "alt": ("Horizontal bar chart of CMS’s central estimates for 2026–2035: the SDP rule cuts provider payments "
                "by $774.8 billion; the provider tax rule measured alone cuts $384.0 billion, of which $241.9 billion "
                "is already counted in the SDP rule and $142.1 billion is additional; both rules combined cut $916.9 billion."),
    })


# ---------------------------------------------------------------- Figure 2
def fig2():
    r = rows("fig2_waterfall.csv")
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
    # connectors
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
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    ax.tick_params(axis="x", labeltop=False, labelbottom=True)
    source(fig, ["Source: provider tax rule (CMS-2452-P), Table 12 (91 FR 46592) and Table 14 (91 FR 46593); 91 FR 46590–46593.",
                 f"Note: the components give +${comp:.1f}B ($163.7B less $142.1B); the difference from CMS’s +${end:.1f}B is",
                 "CMS’s rounding (Appendix E)."], h)
    LAYOUT["fig2"] = save(fig, "fig2_waterfall")
    META.append({
        "number": 2, "stem": "fig2_waterfall", "csv": "fig2_waterfall.csv",
        "title": "The provider tax rule’s net effect on providers",
        "alt": ("Waterfall chart: measured alone, the provider tax rule leaves providers $220.3 billion worse off (CMS Table 12); "
                "adding back the $241.9 billion overlap already counted in the SDP rule gives CMS’s +$21.7 billion on top of the SDP rule (Table 14)."),
    })


# ---------------------------------------------------------------- Figure 3
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
GROUP_TEXT = {"A": WHITE, "B": INK, "C": INK, "D": WHITE, "E": INK}
# the group names of the sec. 6 table, verbatim
GROUP_NAME = {
    "A": "Both rules",
    "B": "Cap plus lower threshold on non-hospital taxes",
    "C": "Cap only",
    "D": "Non-expansion states with SDPs above the caps",
    "E": "No identified hospital SDPs above the caps",
}


def fig3():
    st = rows("fig3_state_groups.csv")
    assert sorted(TILES) == sorted(r["abbrev"] for r in st), "tile grid must hold exactly the 51 jurisdictions"
    counts = {g: sum(1 for r in st if r["group"] == g) for g in "ABCDE"}
    h = 6.25
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Parts of the two proposed rules that reach each state",
                   "THEIA Services’ state groups A–E, 50 states and DC; groups show where the rules apply, not loss size", h)
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
        ax.add_patch(Rectangle((c + gap / 2, rr + gap / 2), s, s, facecolor=GROUP_FILL[g],
                               edgecolor=RED if low else "none", linewidth=2.0 if low else 0))
        if low:  # inner white ring keeps the red outline distinct from a Group A fill
            ax.add_patch(Rectangle((c + gap / 2 + 0.07, rr + gap / 2 + 0.07), s - 0.14, s - 0.14,
                                   facecolor="none", edgecolor=WHITE, linewidth=0.8))
        mark = "*" if (r["abbrev"] == "CO" or "no KFF estimate" in r["flag"]) else ""
        cx, cy = c + gap / 2 + s / 2, rr + gap / 2 + s / 2
        t = ax.text(cx, cy - 0.10, r["abbrev"] + mark, ha="center", va="center", fontsize=8.5,
                    fontweight="bold", color=GROUP_TEXT[g])
        t.set_gid("tile")
        t2 = ax.text(cx, cy + 0.24, g, ha="center", va="center", fontsize=7, color=GROUP_TEXT[g])
        t2.set_gid("tileletter")
    # legend: swatch with letter, name, count
    leg_top = y_top - (grid_h_in + 0.22) / h
    line_h = 0.235 / h
    for i, g in enumerate("ABCDE"):
        y = leg_top - i * line_h
        fig.patches.append(Rectangle((0.0, y - 0.075 / h), 0.16 / W_IN, 0.16 / h, transform=fig.transFigure,
                                     facecolor=GROUP_FILL[g], edgecolor="none"))
        fig.text(0.08 / W_IN, y + 0.005 / h, g, fontsize=7, color=GROUP_TEXT[g], ha="center", va="center",
                 fontweight="bold")
        fig.text(0.26 / W_IN, y, f"{g}. {GROUP_NAME[g]} ({counts[g]})", fontsize=L_SIZE, color=INK,
                 va="center", ha="left")
    y = leg_top - 5 * line_h
    fig.patches.append(Rectangle((0.01 / W_IN, y - 0.07 / h), 0.14 / W_IN, 0.14 / h, transform=fig.transFigure,
                                 facecolor=RULE, edgecolor=RED, linewidth=1.6))
    fig.text(0.26 / W_IN, y, "Red outline: Group E state whose provider tax the lower threshold reaches "
             "(AR, CO, CT, IN, VT)", fontsize=L_SIZE, color=INK, va="center", ha="left")
    y -= line_h
    fig.text(0.0, y, "* Not in KFF’s dollar figures: Minnesota and Missouri (Group A) have no KFF estimate;",
             fontsize=L_SIZE, color=INK, va="center", ha="left")
    fig.text(0.0, y - 0.17 / h, "   Colorado (Group E) has an SDP above the new limits that KFF’s figures leave out.",
             fontsize=L_SIZE, color=INK, va="center", ha="left")
    source(fig, ["Source: THEIA Services’ grouping from KFF, August 14, 2026 (hospital SDPs above the caps) and August 20, 2026",
                 "(provider taxes above 3.5%), and KFF’s Medicaid expansion tracker; KFF does not use these groups (Appendix H)."], h)
    LAYOUT["fig3"] = save(fig, "fig3_state_map")
    META.append({
        "number": 3, "stem": "fig3_state_map", "csv": "fig3_state_groups.csv",
        "title": "Parts of the two proposed rules that reach each state",
        "alt": ("Tile map of the 50 states and DC sorted into five groups: 24 states where both rules reach (A), 2 where the cap and "
                "a lower threshold on non-hospital taxes reach (B), 3 cap only (C), 8 non-expansion states with SDPs above the caps (D) "
                "and 14 with no identified hospital SDPs above the caps (E), five of which the lower threshold reaches; it shows where "
                "the rules apply, not where losses are largest."),
    })


# ---------------------------------------------------------------- Figure 4
def fig4():
    r = rows("fig4_pediatric.csv")
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
    source(fig, ["Source: Michelson et al., JAMA Pediatrics, December 2024."], h)
    LAYOUT["fig4"] = save(fig, "fig4_pediatric")
    META.append({
        "number": 4, "stem": "fig4_pediatric", "csv": "fig4_pediatric.csv",
        "title": "Change in hospital inpatient units",
        "alt": ("Bar chart from one national study: from 2008 to 2022, pediatric inpatient units fell 29.9 percent and adult "
                "inpatient units fell 4.4 percent."),
    })


# ---------------------------------------------------------------- Figure 5
def fig5():
    r = rows("fig5_psychiatric.csv")
    series = {}
    note = None
    for x in r:
        if x["item"].startswith("Note"):
            note = float(x["value"])
            continue
        series.setdefault(x["item"], {})[int(x["year"])] = float(x["value"])
    style = {"Freestanding psychiatric hospitals": INK, "Short-term acute care hospitals": GREY, "Total": RED}
    h = 3.2
    fig = plt.figure(figsize=(W_IN, h))
    y_top = header(fig, "Psychiatric beds per 100,000 people, by hospital type", "United States, 2011 and 2023", h)
    ax = fig.add_axes([0.10, 0.17, 0.44, y_top - 0.25])
    clean(ax, grid_axis=None)
    for name, pts in series.items():
        c = style[name]
        ax.plot([0, 1], [pts[2011], pts[2023]], color=c, linewidth=2, solid_capstyle="round", zorder=3)
        ax.scatter([0, 1], [pts[2011], pts[2023]], s=42, color=c, edgecolor=WHITE, linewidth=1.5, zorder=4)
        v0 = f"{pts[2011]:g}"
        v1 = f"{pts[2023]:g}"
        label(ax, -0.05, pts[2011], v0, gid="datalabel", ha="right", va="center", fontweight="bold")
        label(ax, 1.05, pts[2023], v1, gid="datalabel", ha="left", va="center", fontweight="bold")
        nm = "Total, both types" if name == "Total" else name
        label(ax, 1.20, pts[2023], nm, ha="left", va="center", fontweight="bold", clip_on=False)
    ax.set_xlim(-0.25, 1.25)
    ax.set_ylim(7.5, 30)
    ax.set_xticks([0, 1], ["2011", "2023"], fontsize=L_SIZE, fontweight="bold")
    ax.set_yticks([])
    ax.xaxis.set_ticks_position("top")
    ax.tick_params(axis="x", labeltop=True, labelbottom=False, pad=4)
    for x in (0, 1):
        ax.axvline(x, color=RULE, linewidth=0.75, zorder=1)
    source(fig, ["Source: Lindenfeld et al., PLoS Medicine, July 2025.",
                 f"Note: the source’s 2023 components sum to {note:g}, not its stated "
                 f"{series['Total'][2023]:g}."], h)
    LAYOUT["fig5"] = save(fig, "fig5_psychiatric")
    META.append({
        "number": 5, "stem": "fig5_psychiatric", "csv": "fig5_psychiatric.csv",
        "title": "Psychiatric beds per 100,000 people, by hospital type",
        "alt": ("Slope chart of psychiatric beds per 100,000 people from 2011 to 2023: short-term acute care hospitals fell from "
                "11.3 to 9.06, freestanding psychiatric hospitals rose from 16.8 to 19.5, and the total was about flat at 28.1 and 28.4."),
    })


if __name__ == "__main__":
    for f in (fig1, fig2, fig3, fig4, fig5):
        f()
    (FIG / "figures.json").write_text(json.dumps(META, indent=2, ensure_ascii=False), encoding="utf-8")
    (FIG / "layout_report.json").write_text(json.dumps(LAYOUT, indent=1, ensure_ascii=False), encoding="utf-8")
    print("wrote", ", ".join(m["stem"] for m in META))
