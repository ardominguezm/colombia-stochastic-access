import numpy as np

from stochastic_access.markov import absorbing_statistics, transition_matrix
from stochastic_access.metrics import weighted_atkinson, weighted_gini


def test_first_passage_on_directed_chain():
    adjacency = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 1]], dtype=float)
    p = transition_matrix(adjacency)
    result = absorbing_statistics(p, targets=[2])
    np.testing.assert_allclose(result["mean"], [2, 1, 0])
    np.testing.assert_allclose(result["variance"], [0, 0, 0])


def test_cost_bias_prefers_cheaper_edge():
    adjacency = np.array([[0, 1, 1], [0, 1, 0], [0, 0, 1]], dtype=float)
    costs = np.array([[0, 1, 3], [0, 0, 0], [0, 0, 0]], dtype=float)
    p = transition_matrix(adjacency, costs, beta=1.0).toarray()
    assert p[0, 1] > p[0, 2]
    np.testing.assert_allclose(p.sum(axis=1), 1.0)


def test_inequality_metrics():
    assert weighted_gini([1, 1, 1]) == 0
    assert weighted_gini([0, 0, 1]) > 0
    assert weighted_atkinson([1, 1, 1], epsilon=0.5) == 0

