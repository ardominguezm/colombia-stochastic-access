# Pilot research design

## Primary estimand

For each origin zone and service class, estimate the distribution of the
first-passage time on a multimodal network. Compare this distribution with
shortest-path accessibility and quantify between-zone inequality.

## Minimal publishable analysis

1. Build comparable walking and public-transit networks for Bogotá and Medellín.
2. Define transition probabilities from generalized cost (time, transfers,
   fare, and optional slope).
3. Calibrate or bound parameters with public origin-destination surveys.
4. Estimate mean, variance, and tail probabilities of first-passage times.
5. Aggregate results with population weights and socioeconomic strata.
6. Compare real networks against spatial and degree-preserving null models.
7. Evaluate targeted edge removal/addition counterfactuals, including cable systems.

## Claims intentionally excluded from the pilot

- Reconstructed individual trajectories.
- Real-time crowding or vehicle occupancy.
- Causal infrastructure effects.
- Personal pollution dose.

## Decision gates

- **Gate 1:** required datasets download and contain stable spatial identifiers.
- **Gate 2:** GTFS and street layers can be joined without excessive unmatched stops.
- **Gate 3:** survey modal shares and trip-time distributions can calibrate the model.
- **Gate 4:** stochastic metrics add information beyond shortest paths.
- **Gate 5:** results remain stable under transition-rule and spatial-scale sensitivity.

