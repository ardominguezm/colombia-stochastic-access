"""Weighted inequality metrics for accessibility outcomes."""

from __future__ import annotations

import numpy as np


def _validated(values, weights):
    x = np.asarray(values, dtype=float)
    w = np.ones_like(x) if weights is None else np.asarray(weights, dtype=float)
    mask = np.isfinite(x) & np.isfinite(w) & (w > 0)
    x, w = x[mask], w[mask]
    if x.size == 0 or np.any(x < 0):
        raise ValueError("values must contain finite non-negative observations")
    return x, w


def weighted_gini(values, weights=None) -> float:
    """Compute a weighted Gini coefficient for non-negative values."""
    x, w = _validated(values, weights)
    if np.allclose(x, 0):
        return 0.0
    order = np.argsort(x)
    x, w = x[order], w[order]
    cumw = np.cumsum(w)
    cumxw = np.cumsum(x * w)
    lorenz_area = np.trapezoid(
        np.r_[0.0, cumxw / cumxw[-1]], np.r_[0.0, cumw / cumw[-1]]
    )
    return float(1.0 - 2.0 * lorenz_area)


def weighted_atkinson(values, weights=None, epsilon: float = 0.5) -> float:
    """Compute the weighted Atkinson index (epsilon > 0, epsilon != 1)."""
    if epsilon <= 0 or np.isclose(epsilon, 1.0):
        raise ValueError("epsilon must be positive and different from one")
    x, w = _validated(values, weights)
    mean = np.average(x, weights=w)
    if np.isclose(mean, 0):
        return 0.0
    equally_distributed = np.average(x ** (1.0 - epsilon), weights=w) ** (
        1.0 / (1.0 - epsilon)
    )
    return float(1.0 - equally_distributed / mean)

