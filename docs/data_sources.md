# Data sources and caveats

| Source | Role | Access | Main caveat |
|---|---|---|---|
| SIMUR Bogotá GTFS | Scheduled transit network | Direct public ZIP | Large uncompressed feed; schedule is not realised travel time |
| AMVA EOD 2017 | Trips, people, households | Public catalog resources | Older cross-sectional survey |
| Metro Medellín GTFS | Metro, tram, cable topology/schedule | Public ArcGIS item | Verify latest service dates |
| OpenStreetMap | Walking network and POIs | Overpass/OSMnx | Completeness varies by feature and neighborhood |
| DANE/municipal zones | Population and socioeconomic aggregation | Public | Harmonisation between city geographies |
| Air-quality networks | Optional exposure extension | Public | Sparse stations require interpolation and uncertainty |

Every downloaded file must be accompanied by a manifest entry containing its
source URL, UTC retrieval time, size, and SHA-256 checksum. Raw data must not be
committed to Git.

