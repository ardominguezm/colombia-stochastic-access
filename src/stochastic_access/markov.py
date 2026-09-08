"""Finite-state Markov tools used by the pilot notebooks."""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve


def transition_matrix(
    adjacency: np.ndarray | sparse.spmatrix,
    costs: np.ndarray | sparse.spmatrix | None = None,
    beta: float = 1.0,
) -> sparse.csr_matrix:
    """Build a row-stochastic, cost-biased transition matrix.

    For available edge ``i -> j``, its unnormalised probability is
    ``exp(-beta * cost[i, j])``. Isolated nodes receive a self-loop.
    """
    a = sparse.csr_matrix(adjacency, dtype=float)
    if a.shape[0] != a.shape[1]:
        raise ValueError("adjacency must be square")
    if costs is None:
        weights = a.copy()
    else:
        c = sparse.csr_matrix(costs, dtype=float)
        if c.shape != a.shape:
            raise ValueError("costs and adjacency must have equal shapes")
        rows, cols = a.nonzero()
        weights = sparse.csr_matrix(
            (np.exp(-beta * np.asarray(c[rows, cols]).ravel()), (rows, cols)),
            shape=a.shape,
        )

    row_sums = np.asarray(weights.sum(axis=1)).ravel()
    isolated = np.flatnonzero(row_sums == 0)
    if isolated.size:
        weights = weights + sparse.csr_matrix(
            (np.ones(isolated.size), (isolated, isolated)), shape=a.shape
        )
        row_sums = np.asarray(weights.sum(axis=1)).ravel()
    return sparse.diags(1.0 / row_sums) @ weights


def absorbing_statistics(
    transition: np.ndarray | sparse.spmatrix,
    targets: Iterable[int],
) -> dict[str, np.ndarray]:
    """Return mean and variance of first-passage steps to target states.

    Unreachable transient states are reported as infinity. The variance uses
    the standard absorbing-chain identity ``v=(2N-I)t-t^2``.
    """
    p = sparse.csr_matrix(transition, dtype=float)
    n = p.shape[0]
    if p.shape[1] != n:
        raise ValueError("transition must be square")
    targets = np.unique(np.fromiter(targets, dtype=int))
    if targets.size == 0 or np.any((targets < 0) | (targets >= n)):
        raise ValueError("targets must contain valid node indices")

    transient = np.setdiff1d(np.arange(n), targets)
    result_mean = np.zeros(n, dtype=float)
    result_var = np.zeros(n, dtype=float)
    if transient.size == 0:
        return {"mean": result_mean, "variance": result_var}

    q = p[transient][:, transient]
    system = sparse.eye(transient.size, format="csr") - q
    try:
        mean_t = spsolve(system, np.ones(transient.size))
        second_component = spsolve(system, mean_t)
        var_t = 2.0 * second_component - mean_t - mean_t**2
    except Exception:
        mean_t = np.full(transient.size, np.inf)
        var_t = np.full(transient.size, np.inf)

    invalid = (~np.isfinite(mean_t)) | (mean_t < 0)
    mean_t[invalid] = np.inf
    var_t[invalid] = np.inf
    var_t[~invalid] = np.maximum(var_t[~invalid], 0.0)
    result_mean[transient] = mean_t
    result_var[transient] = var_t
    return {"mean": result_mean, "variance": result_var}

