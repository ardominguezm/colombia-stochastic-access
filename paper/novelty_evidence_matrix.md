# Novelty and evidence matrix

## Claim defended by the paper

The paper does **not** claim that random walks, first-passage times, gendered mobility, or boundary sensitivity are individually new. Its defensible contribution is their combination in a single estimand and inferential design:

> How does the female–male gap in purpose-specific stochastic accessibility respond as an observed metropolitan mobility system expands from Bogotá D.C. through nested functional scopes to the complete region, and which algebraic component—residential starting distributions or mobility kernels—accounts for that response?

## Closest literature

| Study | Data/network | Main outcome | Relation to this paper | Remaining distinction |
|---|---|---|---|---|
| Guzman, Oviedo & Rivera (2017) | Bogotá city-region; conventional transport accessibility | Income- and mode-related equity in access to work and study | Establishes the Bogotá accessibility-equity context | Does not use subgroup-specific OD Markov kernels, FPT, paired scope inference, or residence–kernel decomposition |
| Macedo et al. (2022) | Official surveys from Bogotá, Medellín and São Paulo | Gender and socioeconomic differences in mobility diversity | Establishes gendered mobility differences in Colombia | Does not estimate purpose-target FPT accessibility or boundary-induced attenuation |
| Sousa & Nicosia (2022) | Census adjacency graphs in US/UK metropolitan areas | Random-walk class coverage time for ethnic segregation | Closest random-walk urban inequality precedent | Walk occurs on geographic adjacency and targets demographic classes, not survey-weighted mobility transitions and opportunities |
| Neira et al. (2024) | Multilayer transport networks; Cuenca | Random-walk segregation/encounter index | Shows transport-constrained stochastic segregation | Focuses on encounter segregation and network layers, not gender accessibility gaps or administrative truncation |
| Pintér & Lengyel (2025) | GPS mobility network | Effects of administrative/physical barriers on mobility communities | Establishes that boundaries can structure mobility | Does not estimate how a boundary changes a subgroup-specific accessibility gap with paired design |
| Yang et al. (2026) | Mobile-phone mobility and transport modes in Beijing | Mode-specific mixing and multimodal uniformity | Very recent EPJ Data Science comparator | Studies SES mixing across transport layers, not territorial-scope sensitivity of purpose-specific accessibility |
| Present study | Bogotá 2023 household mobility survey; four nested weighted OD Markov networks | Female–male FPT gaps to employment, education and health targets | Integrates stochastic accessibility, gender and functional territorial scope | Shared household bootstrap estimates a boundary-response curve and residence–kernel decomposition across nested scopes |

## Evidence produced by the pipeline

| Result | Status | Primary evidence |
|---|---|---|
| Regional female–male FPT gaps are positive for all three purposes | Produced | Gate 13/14 estimates and simultaneous intervals |
| District restriction attenuates the gaps by 52.0%, 51.8% and 65.9% | Produced | Paired scope contrasts |
| Regional-minus-district contrasts remain positive after simultaneous correction | Produced | Joint Poisson household bootstrap |
| Total-gap slopes over interface-flow coverage are positive for employment, education, and health after simultaneous correction | Produced | Gate 16 four-scope shared household bootstrap |
| Strict stepwise monotonicity holds for every purpose | **Not supported** | Point estimates and bootstrap monotonicity probabilities; education and health are non-monotone at intermediate scopes |
| Amplification is concentrated in the mobility-kernel component | Produced | Symmetric residence–kernel decomposition and Gate 16 slope intervals |
| Facatativá and Soacha contribute strongly for selected purposes | Produced, descriptive attribution | Origin/municipality kernel contributions |
| Administrative borders causally generate the gender gaps | **Not supported** | The design is cross-sectional and descriptive |
| Removing or integrating a municipality would reproduce the attribution values | **Not supported** | Contributions are not intervention effects |

## Positioning sentence

We estimate a multiscale boundary response of a gender accessibility gap rather than merely comparing accessibility levels across two maps: the same household bootstrap perturbation is propagated through four nested OD kernels, and both endpoint contrasts and response slopes are decomposed into residential and mobility-kernel components.

## Remaining checks before submission

1. Copy the two Gate 16 PNG files to `paper/figures/` and compile the manuscript with the new multiscale graphic.
2. Add the Gate 16 scope and slope tables to the standalone supplement.
3. Run a final machine-readable consistency audit across Gates 14–16, manuscript numbers, tables, and figure captions.
4. Archive the accepted repository release and insert its DOI in Data availability.
5. Confirm funding, authorship, acknowledgements, and the journal's current AI-disclosure wording.
