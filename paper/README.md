# Bogotá stochastic urban accessibility paper

The current submission candidate is aimed at *Computers, Environment and Urban Systems*. Read [`REVIEW_RELEASE.md`](REVIEW_RELEASE.md) for the source and figure manifest, and [`SUBMISSION_CHECKLIST.md`](SUBMISSION_CHECKLIST.md) for author decisions.

The main source and compiled review copy are `manuscript.tex` and `manuscript.pdf`. The standalone supplement is `supplementary_material.tex` and `supplementary_material.pdf`; its fourteen tables are in `supplementary/tables/`. All eight figures appear in the main text. Figure 7 uses `scripts/plot_gate23_validation.py` and `figure_data/gate23_figure_data.csv`; Figure 8 uses `scripts/plot_gate24_boundary_mechanism.py` and `figure_data/gate24_boundary_mechanism_intervals.csv`. The latter CSV retains four decimal places; the publication-format notebook instead loads the full-precision Gate 24 output from Drive.

Run `notebooks/24_bogota_publication_figures_all_formats.ipynb` in Colab to produce a manifest and ZIP with all eight main-text figures in PNG, PDF and EPS. The first six PDFs/EPS embed the archived PNG pixels; Figures 7 and 8 are drawn as vector graphics.
