# Mobility networks, territorial boundaries, and sex-based gaps in stochastic urban accessibility: evidence from Bogotá

[![Status: submitted](https://img.shields.io/badge/status-submitted-blue)](#publication-status)
[![Journal: CEUS](https://img.shields.io/badge/journal-Computers%2C%20Environment%20and%20Urban%20Systems-4c78a8)](#publication-status)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)

Reproducibility repository for a study of territorial boundaries and sex-disaggregated stochastic accessibility in Bogotá and its surrounding municipalities.

## Publication status

**Submitted to _Computers, Environment and Urban Systems_ on 28 September 2026.**

This repository accompanies the manuscript:

> Andy Rafael Domínguez-Monterroza. “Mobility networks, territorial boundaries, and sex-based gaps in stochastic urban accessibility: evidence from Bogotá.”

The manuscript is under peer review. Results and documentation may be updated in response to editorial or reviewer comments. A versioned archival DOI will be added after the public release is deposited.

## Study overview

The analysis uses the public **2023 Bogotá–Region Household Mobility Survey** to estimate survey-weighted mobility transition kernels at the UTAM level. First-passage times to employment, education, and health destination sets measure the expected number of aggregate mobility transitions required to reach relevant opportunities.

The workflow compares Bogotá D.C. with the complete Bogotá–Region system and with two intermediate functional scopes. It includes:

- effective-sample-size regularization of sex-specific transition rows;
- female-minus-male stochastic-accessibility gaps;
- a residence–kernel decomposition within each territorial scope;
- paired household-cluster bootstrap inference;
- multiscale territorial-boundary sensitivity;
- municipality-omission and target-definition diagnostics;
- time-threshold and home-origin sensitivity checks; and
- ordered accounting of network, destination, and resident-population changes.

First-passage transitions are dimensionless movements in an aggregate fitted flow system. They are not minutes of travel or observed individual itineraries. All comparisons are descriptive and do not identify causal effects of administrative boundaries.

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
| Primary estimation | 06–12 | Purpose-specific FPT, regularized group kernels, decomposition, robustness, final inference, and paired district–region comparison |
| Reporting and spatial analysis | 13–17 | Publication tables, supplementary outputs, multiscale response, consistency audit, and study-area map |
| Extended sensitivity analyses | 18–23 | Relative gaps, shrinkage sensitivity, specification grid, municipal influence, decisive validation, and ordered territorial accounting |
| Figure export | 24 | Publication figures in PNG, PDF, and EPS formats |

Open any notebook directly in Google Colab from the [`notebooks/`](notebooks/) directory. Notebooks 01 and 02 allow manual upload of the official survey archive when the source server blocks automated downloads.

## Repository layout

```text
config/                 Public source registry
data/                   Downloaded data and caches (not versioned)
docs/                   Data and methodological documentation
notebooks/              Executable Colab workflow, numbered 00–24
outputs/figures/         Versioned publication figures
src/stochastic_access/  Reusable Markov-chain and accessibility functions
tests/                   Unit tests
```

## Local installation

```bash
git clone https://github.com/ardominguezm/colombia-stochastic-access.git
cd colombia-stochastic-access
python -m pip install -r requirements.txt
python -m pytest -q
```

The principal workflow was executed in Google Colab. Local execution may require manually downloading the official survey files into the paths documented by the notebooks.

## Reproducibility notes

- Household identifiers define the resampling clusters.
- Shared Poisson(1) household multipliers preserve paired territorial comparisons.
- Network components, reference kernels, and target sets are held fixed where specified by each inferential procedure.
- Generated numerical results are frozen before manuscript-table and figure construction.
- The repository intentionally excludes the manuscript source while the article is under review.

## Citation

Until an archival DOI is available, cite the software repository using [`CITATION.cff`](CITATION.cff). After publication, the article citation and archival DOI will replace this provisional reference.

## License

Code is released under the [MIT License](LICENSE). External datasets retain their original licenses and attribution requirements.
