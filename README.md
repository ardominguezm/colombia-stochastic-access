# Stochastic urban accessibility across territorial boundaries: Sex-based gaps in Bogotá

[![Status: submitted](https://img.shields.io/badge/status-submitted-blue)](#publication-status)
[![Journal: EPJ Data Science](https://img.shields.io/badge/journal-EPJ%20Data%20Science-4c78a8)](#publication-status)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)

Reproducibility repository for a study of territorial boundaries and sex-based stochastic accessibility in Bogotá and its surrounding municipalities.

## Publication status

**Submitted to _EPJ Data Science_ in October 2026.**

This repository accompanies the manuscript:

> Andy Rafael Domínguez-Monterroza. “Stochastic urban accessibility across territorial boundaries: Sex-based gaps in Bogotá.”

The manuscript is under peer review. Results and documentation may be updated in response to editorial or reviewer comments.

## Study overview

The analysis uses the public **2023 Bogotá–Region Household Mobility Survey** to estimate survey-weighted mobility transition kernels at the UTAM level. First-passage times to employment, education, and health destination sets measure the expected number of aggregate mobility transitions required to reach relevant opportunities.

The workflow compares the Bogotá D.C.-internal system with the complete Bogotá–Region system and two intermediate functional scopes. It includes:

- effective-sample-size regularization of sex-specific transition rows;
- female-minus-male stochastic-accessibility gaps;
- a residential-distribution--mobility-kernel decomposition within each territorial scope;
- paired household-cluster bootstrap inference;
- multiscale territorial-boundary sensitivity;
- municipality-omission and target-definition diagnostics;
- time-threshold and home-origin sensitivity checks;
- ordered accounting of network, destination, and resident-population changes; and
- origin-specific accessibility-gap maps for employment, education, and health.

First-passage transitions are dimensionless movements in an aggregate fitted flow system. They are not minutes of travel or observed individual itineraries. All comparisons are descriptive and do not identify causal effects of territorial boundaries.

## Data

The source microdata and zoning files are publicly available from the Bogotá Mobility Observatory. They are not redistributed in this repository. Large downloaded files and restricted intermediate data remain excluded from version control.

See:

- [Data sources](docs/data_sources.md)
- [Data dictionary](docs/data_dictionary.md)
- [Research design](docs/research_design.md)
- [Source registry](config/data_sources.yml)

## Reproducible workflow

The notebooks are numbered in dependency order.

| Stage | Notebooks | Purpose |
|---|---|---|
| Data and network validation | 00–05 | Source audit, relational joins, spatial resolution, connectivity, Markov/FPT validation, and destination construction |
| Primary estimation | 06–12 | Purpose-specific FPT, regularized group kernels, decomposition, robustness, final inference, and paired district--region comparison |
| Reporting and spatial analysis | 13–17 | Publication tables, supplementary outputs, multiscale response, consistency audit, and study-area map |
| Extended sensitivity analyses | 18–23 | Relative gaps, shrinkage sensitivity, specification grid, municipal influence, validation diagnostics, and ordered territorial accounting |
| Figure export | 24 | Publication figures in PNG, PDF, and EPS formats |
| Spatial interpretation | 25 | Origin-specific female-minus-male FPT maps for employment, education, and health |

Open any notebook directly in Google Colab from the [`notebooks/`](notebooks/) directory. Notebooks 01 and 02 allow manual upload of the official survey archive when the source server blocks automated downloads.

The origin-specific accessibility-gap map can be reproduced and customised directly in Colab:

[![Open notebook 25 in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ardominguezm/colombia-stochastic-access/blob/main/notebooks/25_bogota_origin_specific_sex_gap_map.ipynb)

Notebook 25 reads the frozen Gate 11 CSV and zoning archive from Drive. If Drive cannot be mounted, it requests both files together through Colab's upload dialog and automatically downloads the completed figure bundle.

## Repository layout

```text
config/                  Public source registry
data/                    Downloaded data and caches (not versioned)
docs/                    Data and methodological documentation
notebooks/               Executable Colab workflow, numbered 00–25
outputs/figures/         Versioned publication figures
src/stochastic_access/   Reusable Markov-chain and accessibility functions
tests/                   Unit tests
