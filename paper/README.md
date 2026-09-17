# Manuscript working files

Target journal: **EPJ Data Science**, Regular Article.

Working title: *Metropolitan scope amplifies measured gender disparities in stochastic urban accessibility: Evidence from Bogotá's 2023 mobility survey*.

The current `article` class is intentionally portable. Before submission, migrate the content to the current Springer Nature LaTeX template, retain double spacing and line/page numbering, and compile with pdfLaTeX/Tex Live 2021 compatibility.

## Completed manuscript-package steps

- Three verified publication figures are versioned in `paper/figures/`.
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

## Remaining finishing steps

1. Copy the two Gate 16 figures from Drive to `paper/figures/` and run the final Gates 14–16 manuscript consistency audit.
2. Compile and visually inspect the revised manuscript and supplement with the multiscale figures.
3. Resolve the author-dependent declarations, authorship, and AI-use wording listed in the submission checklist.
4. Make the repository public or create an appropriate review archive, then archive the exact release in a DOI-issuing repository.
5. Insert the persistent identifier, prepare the cover letter, and upload the editable source package.

EPJ Data Science currently requests a 150--250 word abstract, 3--10 keywords, editable source files, sequentially cited tables/figures, and complete declarations.
