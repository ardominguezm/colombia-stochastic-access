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
Its results must be executed and audited before any multiscale claim is added to the
manuscript.

## Remaining finishing steps

1. Execute notebook 15, commit Gate 16 outputs, and revise the manuscript only if the multiscale evidence supports the corresponding claim.
2. Resolve the author-dependent declarations, authorship, and AI-use wording listed in the submission checklist.
3. Make the repository public or create an appropriate review archive.
4. Archive the exact analytical release in a DOI-issuing repository and insert the persistent identifier.
5. Prepare the cover letter and upload the editable source package.

EPJ Data Science currently requests a 150--250 word abstract, 3--10 keywords, editable source files, sequentially cited tables/figures, and complete declarations.
