# Manuscript working files

Target journal: **EPJ Data Science**, Regular Article.

Working title: *Metropolitan scope amplifies measured gender disparities in stochastic urban accessibility: Evidence from Bogotá's 2023 mobility survey*.

The current `article` class is intentionally portable. Before submission, migrate the content to the current Springer Nature LaTeX template, retain double spacing and line/page numbering, and compile with pdfLaTeX/Tex Live 2021 compatibility.

## Completed manuscript-package steps

- Six verified publication figures are versioned in `paper/figures/`, including the two Gate 16 multiscale figures and the Gate 18 study-area map.
- The closest-literature audit and defensible novelty claim are recorded in
  `paper/novelty_evidence_matrix.md`.
- Notebook 14 builds the standalone supplement and runs the Gate 15 consistency audit.
- Notebook 14 has been executed; the standalone supplement and all eight generated tables are versioned.
- The manuscript and supplement compile successfully and have passed visual layout QA.
- The detailed journal audit and unresolved submission decisions are tracked in
  [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md).

## Current EPJ Data Science extension

Notebook 15 implements Gate 16: a paired multiscale boundary-response analysis over
Bogotá D.C., functional 50%, functional 80%, and the complete Bogotá–Region system.
Gate 16 has been executed and passed all 18 validation checks with 500 shared
household-cluster bootstrap replicates. The manuscript and novelty matrix now include
the supported positive boundary-response slopes and explicitly distinguish them from
strict stepwise monotonicity.

## Final submission audit

Notebook 16 implements Gate 17. It checks frozen numerical claims against Gates 14–16, verifies figures, citations and cross-references, compiles both LaTeX documents, and creates page contact sheets for visual inspection. The prior successful execution predates the study-area map, so Gate 17 must be rerun once more to audit the complete six-figure manuscript.

## Study-area figure

Notebook 17 builds the geographical study-area figure from the official UTAM zoning and the Gate 16 nested scope definitions. Gate 18 has been executed successfully: 140 of 141 survey UTAMs are represented, all four analytical scope classes and all 20 external municipalities are present, geometries are valid, and the publication PNG/PDF were generated. The final PNG is versioned as `paper/figures/figure_study_area_multiscale_scopes.png`.

## Remaining finishing steps

1. Re-run notebook 16 after the map is versioned and inspect the updated manuscript contact sheet.
2. Select the final title and resolve the author-dependent declarations, authorship, and AI-use wording listed in the submission checklist.
3. Make the repository public or create an appropriate review archive, archive the exact release, insert the persistent identifier, and prepare the submission package.

EPJ Data Science currently requests a 150--250 word abstract, 3--10 keywords, editable source files, sequentially cited tables/figures, and complete declarations.
