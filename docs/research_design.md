# Research design

## Study architecture

Bogotá is the primary inferential city. The 2023 Mobility Survey supplies
row-level household, person, trip, stage, weighting, and zoning information.
Medellín is an external-transferability case: the 2025 EOD viewer supplies
recent macrozone aggregates, while the public 2017 microdata are retained only
for auxiliary historical analyses.

This asymmetric design avoids treating datasets with different years and
granularities as if they were directly exchangeable.

## Primary estimand

For each origin zone and service class, estimate the distribution of the
first-passage time on a multimodal network. Compare this distribution with
shortest-path accessibility and quantify socioeconomic and spatial inequality.

## Minimal publishable analysis

1. Audit and join Bogotá 2023 households, persons, trips, stages, and ZAT/UTAM.
2. Construct a weighted observed origin-destination matrix.
3. Build Bogotá walking and public-transit layers from OSM and dated GTFS.
4. Define transition probabilities from generalized cost, observed attraction,
   transfers, and route uncertainty.
5. Estimate mean, variance, quantiles, and tail probabilities of first-passage times.
6. Compare stochastic metrics against deterministic shortest-path accessibility.
7. Aggregate with survey weights and estimate inequality by socioeconomic group.
8. Evaluate robustness under transition rules, spatial scales, and network perturbations.
9. Test spatial transferability using Medellín 2025 macrozone aggregates without
   claiming individual-level inference for that city.

## Claims intentionally excluded

- Reconstructed individual trajectories.
- Real-time crowding or vehicle occupancy.
- Direct Bogotá-Medellín comparisons of unstandardized values.
- Causal infrastructure effects.
- Personal pollution dose.

## Decision gates

- **Gate 1 — availability:** required sources download and are readable.
- **Gate 2 — analytical integrity:** Bogotá household, person, trip, and zoning
  tables expose stable join keys, origin/destination fields, and survey weights.
- **Gate 3 — relational validity:** joins satisfy expected cardinalities and yield
  a geographically valid weighted OD matrix.
- **Gate 4 — network integration:** survey zones, GTFS stops, OSM nodes, and
  essential-service destinations can be spatially linked with acceptable coverage.
- **Gate 5 — calibration:** observed modal shares and trip-time distributions
  identify or meaningfully bound the transition model.
- **Gate 6 — added information:** stochastic metrics explain heterogeneity not
  captured by shortest paths and remain stable under sensitivity analyses.
