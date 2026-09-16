# Stochastic Accessibility in Colombian Cities

[![Data gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/00_data_audit_and_pilot.ipynb)
[![Schema gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/01_bogota_2023_schema_gate.ipynb)
[![Relational OD gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/02_bogota_2023_relational_od_gate.ipynb)
[![Resolution gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/03_bogota_2023_resolution_connectivity_gate.ipynb)
[![Markov/FPT gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/04_bogota_2023_markov_fpt_gate.ipynb)
[![Destination gate](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/05_bogota_2023_purpose_destination_gate.ipynb)
[![Substantive FPT](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/06_bogota_2023_substantive_fpt.ipynb)
[![Group FPT](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/07_bogota_2023_regularized_group_fpt.ipynb)
[![Residence–mobility decomposition](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/08_bogota_2023_residence_mobility_decomposition.ipynb)
[![Decomposition robustness](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/09_bogota_2023_decomposition_robustness.ipynb)
[![Final inference](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/10_bogota_2023_final_inference_and_maps.ipynb)
[![Scope sensitivity](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/11_bogota_region_scope_sensitivity.ipynb)
[![Paired scope inference](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/12_bogota_2023_paired_scope_inference.ipynb)
[![Manuscript outputs](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/13_bogota_2023_manuscript_tables_figures.ipynb)
[![Supplementary material](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/14_bogota_2023_supplementary_material.ipynb)

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
6. **05_bogota_2023_purpose_destination_gate.ipynb** classifies declared
   trip purposes into employment, education, and health; audits duration and
   spatial support; and predefines core and extended destination sets (Gate 6).
7. **06_bogota_2023_substantive_fpt.ipynb** estimates first-passage
   distributions and expected accumulated travel-time rewards toward the
   accepted employment, education, and health destination sets (Gate 7).
8. **07_bogota_2023_regularized_group_fpt.ipynb** estimates regularized
   sex- and stratum-specific transition kernels, checks shrinkage sensitivity,
   and obtains household-cluster bootstrap intervals for group FPT (Gate 8).
9. **08_bogota_2023_residence_mobility_decomposition.ipynb** decomposes group
   FPT gaps into residential composition, mobility-kernel, and interaction
   components using a joint household-cluster bootstrap (Gate 9).
10. **09_bogota_2023_decomposition_robustness.ipynb** tests complete versus
    category-valid references, core versus extended targets, and conditional
    versus unconditional residential starts, with a sex-gap bootstrap (Gate 10).
11. **10_bogota_2023_final_inference_and_maps.ipynb** runs the 500-replicate
    household bootstrap for the primary specification, constructs simultaneous
    intervals, and maps origin-level contributions to the sex gap (Gate 11).
12. **11_bogota_region_scope_sensitivity.ipynb** reconstructs an independent
    Bogotá D.C.-internal kernel and destination sets, compares them with the
    Bogotá–Region estimand, and audits municipality-of-origin influence (Gate 12).
13. **12_bogota_2023_paired_scope_inference.ipynb** applies shared household
    bootstrap multipliers to both territorial scopes and estimates simultaneous
    intervals for regional-minus-district gap amplification (Gate 13).
14. **13_bogota_2023_manuscript_tables_figures.ipynb** freezes the validated
    estimates into publication-ready CSV/LaTeX tables, figures, and a concise
    analytical summary without re-estimating or selecting results (Gate 14).
15. **14_bogota_2023_supplementary_material.ipynb** consolidates regularization,
    specification, support, paired-inference, and stratum diagnostics into a
    standalone supplementary package and runs the final consistency audit (Gate 15).

Large source files are written under data/ and intentionally excluded from Git.
Each run records URLs, timestamps, file sizes, and SHA-256 hashes.

## Manuscript

An initial EPJ Data Science Regular Article draft is available in
[`paper/manuscript.tex`](paper/manuscript.tex), with its verified starter
bibliography and a checklist of remaining submission tasks.

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
