# Bogotá manuscript and supplement: publication candidate

The manuscript is `manuscript.tex` (`manuscript.pdf`); Additional file 1 is `supplementary_material.tex` (`supplementary_material.pdf`). The main text has eight numbered figures in `figures/`. The supplement contains fourteen tables, S1–S14, and no figures. The primary paired bootstrap and the independent 500-replicate ordered mechanism bootstrap have distinct interval families; Figure 8 and Table S14 report the latter.

To regenerate the last two figures:

```bash
python scripts/plot_gate23_validation.py
python scripts/plot_gate24_boundary_mechanism.py
```

The archived Figure 8 coordinates are rounded to four decimals. The Colab notebook `../notebooks/24_bogota_publication_figures_all_formats.ipynb` regenerates it from the exact Gate 24 intervals CSV on Drive and exports all eight images in three formats. Figures 1–6 remain raster based in PDF/EPS; their source generation notebooks are the route to truly vector output if a journal requires it.

Compile in `paper/`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error supplementary_material.tex
```

This is a manuscript candidate, not a submitted paper. Author identification, licensing, public reproducibility archive, declarations, and journal formatting require final author review.
