# Ground-Truth Specification

FUM-MultiLoc may support two complementary forms of spatial ground truth.

## Reference points
Discrete surveyed/defined locations used for fingerprint-style localization.

Expected fields:

```text
reference_point_id,building_id,floor_id,x_m,y_m,z_m,uncertainty_m
```

## Trajectories
Time-aligned ground-truth paths for sequence localization.

Expected fields:

```text
trajectory_id,timestamp_ns,x_m,y_m,z_m,heading_deg,uncertainty_m
```

## Requirements before publication
- Document how truth was obtained.
- Quantify expected error/uncertainty.
- Distinguish measured truth from interpolated truth.
- Document any temporal interpolation.
- Do not silently mix coordinate systems.
