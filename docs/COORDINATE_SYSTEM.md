# Coordinate System

**Do not publish metric labels until this specification is frozen.**

The final release must define:

1. coordinate reference name and version;
2. origin location;
3. positive X, Y, and Z directions;
4. metric units;
5. floor elevation convention;
6. image/floor-plan pixel to metric transformation;
7. transformations between floor-specific and building-wide coordinates;
8. heading convention (zero direction, clockwise/counter-clockwise, degrees/radians);
9. uncertainty/precision of reference points and trajectories.

Recommended public representation:

```text
building_id
floor_id
x_m
y_m
z_m
heading_deg
```

Avoid encoding staff names or other personal information into location identifiers.
