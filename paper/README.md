# Manuscript working files

Target journal: **EPJ Data Science**, Regular Article.

Working title: *Metropolitan scope amplifies measured gender disparities in stochastic urban accessibility: Evidence from Bogotá's 2023 mobility survey*.

The current `article` class is intentionally portable. Before submission, migrate the content to the current Springer Nature LaTeX template, retain double spacing and line/page numbering, and compile with pdfLaTeX/Tex Live 2021 compatibility.

## Completed manuscript-package steps

- Three verified publication figures are versioned in `paper/figures/`.
- The closest-literature audit and defensible novelty claim are recorded in
  `paper/novelty_evidence_matrix.md`.
- Notebook 14 builds the standalone supplement and runs the Gate 15 consistency audit.

## Remaining finishing steps

1. Execute notebook 14 and commit its generated LaTeX supplement and tables.
2. Compile and visually inspect the manuscript and supplement with the real figures.
3. Confirm authors, affiliations, funding, acknowledgements, and AI-use disclosure.
4. Make the repository public or create an anonymized review archive as required.
5. Archive the accepted analytical release in Zenodo and insert its DOI in the data/code availability statement.

EPJ Data Science currently requests a 150--250 word abstract, 3--10 keywords, editable source files, sequentially cited tables/figures, and complete declarations.
