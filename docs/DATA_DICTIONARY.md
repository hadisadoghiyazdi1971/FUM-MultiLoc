# Data Dictionary

This file provides human-readable meanings for canonical fields. Machine-readable schemas are under `schemas/`.

## Common identifiers

| Field | Meaning |
|---|---|
| `sample_id` | Globally unique benchmark sample identifier |
| `session_id` | Acquisition session identifier |
| `device_id` | Pseudonymous acquisition device identifier |
| `timestamp_ns` | Canonical synchronized timestamp in nanoseconds |
| `building_id` | Public building identifier |
| `floor_id` | Public floor identifier |
| `zone_id` | Optional semantic/spatial zone identifier |
| `room_id` | Public anonymous room identifier |

## Pose

| Field | Meaning |
|---|---|
| `x_m`,`y_m`,`z_m` | Local metric coordinates |
| `heading_deg` | Heading according to `COORDINATE_SYSTEM.md` |
| `uncertainty_m` | Ground-truth positional uncertainty if known |

The detailed modality fields will be finalized in v0.2.0.
