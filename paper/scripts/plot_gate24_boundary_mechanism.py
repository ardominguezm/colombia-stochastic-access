"""Plot the ordered Gate 24 accounting identity at publication resolution.

Uses exact Gate 24 CSV if specified via GATE24_INTERVALS, otherwise the
four-decimal publication coordinates checked into figure_data. Intervals are
max-t simultaneous across purposes within each term, not across all terms.
"""
from __future__ import annotations

import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(os.environ.get("GATE24_INTERVALS", ROOT / "figure_data/gate24_boundary_mechanism_intervals.csv"))
DEST = Path(os.environ.get("FIGURE_OUTPUT", ROOT / "figures"))
DEST.mkdir(parents=True, exist_ok=True)
frame = pd.read_csv(SOURCE).rename(columns={
    "purpose_group": "purpose", "point_estimate": "point",
    "simultaneous_ci_lower": "ci_lower", "simultaneous_ci_upper": "ci_upper",
})
terms = {
    "network_fixed_targets_residents": "Network with city residents and targets",
    "target_set_change": "Target set with city residents",
    "added_residents": "Adding regional residents",
    "total_region_minus_district": "Total regional minus district",
}
if set(frame.term).issubset(terms):
    frame["term"] = frame.term.map(terms)
frame.purpose = frame.purpose.str.title()
purposes = ["Employment", "Education", "Health"]
assert len(frame) == 12
assert set(frame.term) == set(terms.values())
assert set(frame.purpose) == set(purposes)
assert frame.groupby(["purpose", "term"]).size().eq(1).all()
assert ((frame.ci_lower <= frame.point) & (frame.point <= frame.ci_upper)).all()
for p in purposes:
    f = frame.set_index(["purpose", "term"]).loc[p]
    assert abs(f.loc[terms["total_region_minus_district"], "point"] -
               sum(f.loc[terms[k], "point"] for k in list(terms)[:3])) < 2e-4

palette = ["#32528b", "#c9763d", "#25827b", "#263642"]
offsets = [-.28, -.09, .10, .29]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9,
                     "pdf.fonttype": 42, "ps.fonttype": 42})
fig, ax = plt.subplots(figsize=(7.2, 4.7))
for j, label in enumerate(terms.values()):
    sub = frame[frame.term.eq(label)].set_index("purpose").loc[purposes]
    val = sub.point.to_numpy(float)
    low = sub.ci_lower.to_numpy(float)
    high = sub.ci_upper.to_numpy(float)
    assert np.isfinite([*val, *low, *high]).all()
    ax.errorbar(val, np.arange(3) + offsets[j], xerr=[val-low, high-val],
                fmt="D" if j == 3 else "o", markersize=5,
                capsize=3, elinewidth=1.4, linewidth=1,
                color=palette[j], label=label, zorder=3)
ax.axvline(0, lw=1, ls="--", color="#64737f", zorder=1)
ax.set_yticks(np.arange(3), purposes)
ax.set_ylim(2.55, -.55)
ax.set_xlim(-.28, 1.04)
ax.set_xlabel("Contribution to regional minus district gap (FPT transitions)")
ax.grid(axis="x", color="#e9eef0", linewidth=.7)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(.5, -.25),
          ncol=2, fontsize=8, columnspacing=1.5)
fig.subplots_adjust(left=.15, right=.98, top=.95, bottom=.30)
base = DEST / "figure_boundary_mechanism"
for extension, opts in [("png", {"dpi": 300}), ("pdf", {}), ("eps", {})]:
    fig.savefig(base.with_suffix("." + extension), facecolor="white", **opts)
plt.close(fig)
print("Boundary-mechanism figure:", base, "from", SOURCE)
