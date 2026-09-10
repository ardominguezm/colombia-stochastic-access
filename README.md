# Stochastic Accessibility in Colombian Cities

[![Data gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/00_data_audit_and_pilot.ipynb)
[![Schema gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/01_bogota_2023_schema_gate.ipynb)
[![Relational OD gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/02_bogota_2023_relational_od_gate.ipynb)
[![Resolution gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/03_bogota_2023_resolution_connectivity_gate.ipynb)
[![Markov/FPT gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/04_bogota_2023_markov_fpt_gate.ipynb)

Reproducible project for studying stochastic accessibility, first-passage
times, and socioeconomic inequality in Colombian multimodal transport networks.

## Research question

How do conclusions about access to essential services change when route
uncertainty, transfers, and the full first-passage-time distribution are
considered instead of only shortest paths?

## Study design

Bogotá is the primary inferential case because its 2023 Mobility Survey
publishes row-level household, person, trip, stage, weight, and zoning data.
Medellín is retained as an external validation case using recent EOD 2025
macrozone results, current network information, and 2017 microdata only for
clearly labeled auxiliary analyses.

The project uses public data only; smart-card records, mobile-phone traces,
Waze history, and institutional agreements are not required for the core paper.

## Notebooks

1. **00_data_audit_and_pilot.ipynb** validates the initial public sources,
   builds two small OSM networks, and tests the first-passage machinery.
2. **01_bogota_2023_schema_gate.ipynb** downloads the Bogotá 2023 processed
   survey and zoning packages, inventories their contents, confirms the
   published relational keys, and evaluates analytical Gate 2.
3. **02_bogota_2023_relational_od_gate.ipynb** measures full-table key
   cardinalities and join/spatial coverage, then builds weighted ZAT-level OD
   matrices for the study region and Bogotá-internal trips (Gate 3).
4. **03_bogota_2023_resolution_connectivity_gate.ipynb** compares ZAT and
   UTAM transition networks using connectivity, effective edge support,
   bootstrap stability, and subgroup feasibility to select the primary
   inferential resolution (Gate 4).
5. **04_bogota_2023_markov_fpt_gate.ipynb** builds the accepted UTAM
   Markov kernel, verifies ergodicity and spectral diagnostics, solves technical
   first-passage problems, and validates them against Monte Carlo simulation
   before attaching substantive service destinations (Gate 5).

Large source files are written under data/ and intentionally excluded from Git.
Each run records URLs, timestamps, file sizes, and SHA-256 hashes.

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

The project estimates *potential stochastic accessibility*. It does not claim
to reconstruct individual trajectories, real-time congestion, or causal
infrastructure effects.

## License

Code is released under the MIT License. Each external dataset retains its own
license and attribution requirements.
