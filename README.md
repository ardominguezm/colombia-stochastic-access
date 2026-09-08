# Stochastic Accessibility in Colombian Cities

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/00_data_audit_and_pilot.ipynb)

Reproducible pilot for studying stochastic accessibility, first-passage times,
and socioeconomic inequality in the multimodal transport networks of Bogotá
and Medellín.

## Research question

How do conclusions about access to essential services change when route
uncertainty, transfers, and the full first-passage-time distribution are
considered instead of only shortest paths?

This repository starts with a data audit and a small reproducible pilot. It
uses public data only; smart-card records, mobile-phone traces, Waze history,
and institutional agreements are not required.

## Quick start in Google Colab

Open [`notebooks/00_data_audit_and_pilot.ipynb`](notebooks/00_data_audit_and_pilot.ipynb)
in Colab and run the cells in order. The notebook:

1. installs the geospatial dependencies;
2. downloads and validates the current Bogotá GTFS feed;
3. discovers downloadable AMVA origin-destination resources;
4. builds small walking-network pilots from OpenStreetMap;
5. computes first-passage and accessibility-inequality diagnostics;
6. records checksums and a data manifest.

Large source files are written under `data/` and intentionally excluded from
Git. Each run records URLs, timestamps, file sizes, and SHA-256 hashes.

## Repository layout

```text
config/                 Public source registry
data/                   Downloaded data (not versioned)
docs/                   Research design and data notes
notebooks/              Colab notebooks
outputs/                 Generated tables and figures
src/stochastic_access/  Reusable Markov-chain and inequality functions
tests/                   Unit tests
```

## Reproduce locally

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Current scope

The pilot estimates *potential stochastic accessibility*. It does not claim
to reconstruct individual trajectories, real-time congestion, or causal
effects of infrastructure. Those require additional data or a stronger
identification design.

## License

Code is released under the MIT License. Each external dataset retains its own
license and attribution requirements.
