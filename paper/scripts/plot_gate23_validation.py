"""Render the manuscript's Gate 23 validation figure from frozen checked values.

Panel A's primary simultaneous intervals are Gate 13's published 500-household
max-t intervals. The home-origin point estimates are Gate 23. Panel B uses the
conditional 500-household percentile intervals from Gate 23. Panel C uses its
reduced 150-household exploratory percentile intervals. These intervals have
different definitions and are never pooled or compared as if exchangeable.
"""
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "figure_data" / "gate23_figure_data.csv"
OUTPUT = ROOT / "figures"
OUTPUT.mkdir(exist_ok=True)
rows = list(csv.DictReader(SOURCE.open(encoding="utf-8", newline="")))
assert [r["purpose"] for r in rows] == ["Employment", "Education", "Health"]
for row in rows:
    for key, value in row.items():
        if key != "purpose":
            row[key] = float(value)

ink = "#233642"
blue = "#2D4E8F"
orange = "#D47A37"
green = "#227C78"
gray = "#6A7780"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9,
    "axes.labelsize": 9, "axes.titlesize": 10, "axes.labelcolor": ink,
    "text.color": ink, "axes.edgecolor": "#BFC9CE",
    "xtick.color": ink, "ytick.color": ink,
    "pdf.fonttype": 42, "ps.fonttype": 42,
})
fig, axs = plt.subplots(3, 1, figsize=(7.2, 8.55), constrained_layout=False)
fig.subplots_adjust(left=.20, right=.965, top=.965, bottom=.065, hspace=.62)
y = np.arange(3)
labels = [r["purpose"] for r in rows]

def style(ax, xlabel, xlim, xticks=None):
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_ylim(2.6, -1.15)
    ax.set_xlim(*xlim)
    if xticks is not None:
        ax.set_xticks(xticks)
    ax.axvline(0, color=gray, lw=1, ls="--", zorder=0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=8)
    ax.grid(axis="x", color="#E6ECEF", lw=.7, zorder=0)
    ax.set_axisbelow(True)
    ax.set_xlabel(xlabel, labelpad=7)

def errorbars(ax, values, lows, highs, offset, color, marker, label):
    v = np.asarray(values, float)
    lo = np.asarray(lows, float)
    hi = np.asarray(highs, float)
    ax.errorbar(v, y + offset, xerr=np.vstack((v-lo, hi-v)), fmt=marker,
                color=color, ecolor=color, elinewidth=1.65, capsize=3.4,
                markersize=6, markeredgecolor="white", markeredgewidth=.5,
                label=label, zorder=3)

# A: pairwise FPT gaps, the primary confirmatory result beside a point check.
ax = axs[0]
errorbars(ax, [r["primary_fpt"] for r in rows],
          [r["primary_lo"] for r in rows], [r["primary_hi"] for r in rows],
          -.13, blue, "o", "Primary FPT; simultaneous 95% CI")
ax.scatter([r["home_fpt"] for r in rows], y+.13, marker="D", s=36,
           color=orange, edgecolor="white", linewidth=.5, zorder=4,
           label="Home-origin kernel; point estimate")
style(ax, "Regional minus district female−male FPT gap (transitions)", (-.08, 1.08),
      [0, .2, .4, .6, .8, 1.0])
ax.set_title("A   Gender gap in stochastic access", loc="left", weight="semibold", pad=9)
ax.legend(frameon=False, loc="upper right", fontsize=8, handlelength=2.1,
          borderaxespad=.1)

# B: distinct percentage-point scale and conditional, unadjusted intervals.
ax = axs[1]
for cutoff, off, color, marker in [(45, -.12, green, "o"), (60, .12, orange, "s")]:
    key = f"time{cutoff}"
    errorbars(ax, [100*r[key] for r in rows],
              [100*r[key+"_lo"] for r in rows],
              [100*r[key+"_hi"] for r in rows], off, color, marker,
              f"{cutoff} min; percentile 95% CI")
style(ax, "Regional minus district male−female reachable-share gap (percentage points)",
      (-.67, .35), [-.6, -.4, -.2, 0, .2])
ax.set_title("B   Time-threshold opportunity proxy", loc="left", weight="semibold", pad=9)
ax.legend(frameon=False, loc="upper right", fontsize=8, handlelength=2.1,
          borderaxespad=.1)

# C: matched 150-replicate sensitivity only, without inventing new point fits.
ax = axs[2]
for key, off, color, marker, label in [
    ("fixed", -.12, blue, "o", "Fixed targets; percentile 95% CI"),
    ("reselected", .12, orange, "s", "Reselected targets; percentile 95% CI")
]:
    for k, row in enumerate(rows):
        lo, hi = row[key+"_lo"], row[key+"_hi"]
        ax.plot([lo, hi], [y[k]+off]*2, color=color, lw=2.0, zorder=3)
        ax.plot([lo, hi], [y[k]+off]*2, linestyle="none", marker="|",
                markersize=10, color=color, zorder=4)
    ax.plot([], [], marker=marker, lw=2, color=color, label=label)
style(ax, "Regional minus district female−male FPT gap (transitions)", (-.08, 1.08),
      [0, .2, .4, .6, .8, 1.0])
ax.set_title("C   Target-selection sensitivity", loc="left", weight="semibold", pad=9)
ax.legend(frameon=False, loc="upper right", fontsize=8, handlelength=2.1,
          borderaxespad=.1)

path = OUTPUT / "figure_7_validation_diagnostics"
fig.savefig(path.with_suffix(".png"), dpi=300, facecolor="white")
fig.savefig(path.with_suffix(".pdf"), facecolor="white")
plt.close(fig)
print(path.with_suffix(".png"))
