# Consolidated EPJ Data Science review candidate

This directory is the single review snapshot following Gate 23. The manuscript is
`manuscript.tex` (compiled as `manuscript.pdf`); Additional file 1 is
`supplementary_material.tex` (compiled as `supplementary_material.pdf`). The
main text contains seven numbered figures in `figures/`. The supplement has
13 numbered tables, S1–S13, and no figures. The new Figure 7 is generated with
`python scripts/plot_gate23_validation.py` using the frozen values in
`figure_data/gate23_figure_data.csv`. The primary Figure 7 intervals are the
Gate 13 simultaneous intervals; Gate 23 provides the comparator estimates,
home-origin estimates, and exploratory target-selection intervals. The panels
use different estimands, units, and bootstrap definitions.

Compile from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error supplementary_material.tex
```

The compiled snapshot was visually checked with all seven embedded figure files;
the supplement was checked with Tables S1–S13. Both compilation logs have no
undefined references, float-size warnings, or overfull boxes. These PDFs are
review candidates and must not be represented as submitted or accepted.

Before journal submission, the author needs to confirm the author list and
affiliations, funding, acknowledgments, and the AI-use disclosure; replace
the provisional data/code availability statement with a public persistent
archive DOI; prepare the cover letter and any required journal declarations;
and confirm the current Springer Nature template and submission instructions.
The private GitHub repository alone is not a public data/code availability
archive. Survey microdata should remain referenced by their official source.
