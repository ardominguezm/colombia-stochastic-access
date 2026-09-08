# Data dictionary: planned harmonised tables

## zones

| Field | Meaning |
|---|---|
| city | Bogota or Medellin |
| zone_id | Stable source zone identifier |
| population | Expansion-weighted population |
| socioeconomic_group | Comparable within-city group |
| geometry | Zone polygon in a projected CRS |

## od_flows

| Field | Meaning |
|---|---|
| origin_id | Origin zone |
| destination_id | Destination zone |
| mode | Harmonised primary mode |
| departure_period | Harmonised time interval |
| expansion_weight | Survey expansion factor |

## network_edges

| Field | Meaning |
|---|---|
| source_node | Directed origin node |
| target_node | Directed destination node |
| layer | walk, bus, BRT, metro, tram, cable, bicycle |
| travel_time_s | Scheduled or modelled travel time |
| transfer_penalty_s | Generalised transfer penalty |
| source_snapshot | Source and retrieval identifier |

## accessibility

| Field | Meaning |
|---|---|
| origin_id | Origin zone or network node |
| service_class | Health, education, employment, food |
| mean_fpt | Mean first-passage time |
| variance_fpt | First-passage-time variance |
| p_reach_30 | Probability of reaching within 30 minutes |
| model_specification | Transition model and parameter set |

