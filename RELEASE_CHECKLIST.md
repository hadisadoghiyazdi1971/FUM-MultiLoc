# Release Checklist

## Repository
- [ ] Version number updated.
- [ ] Changelog updated.
- [ ] README status updated.
- [ ] No raw/private data are in Git history.
- [ ] All schema files validate.

## Data inventory
- [ ] File counts recorded.
- [ ] Byte sizes recorded.
- [ ] Sessions/devices/days/floors inventoried.
- [ ] Missing/corrupt records documented.

## Ground truth
- [ ] Coordinate origin and axes frozen.
- [ ] Units documented.
- [ ] Map transforms validated.
- [ ] Ground-truth uncertainty reported.

## Synchronization
- [ ] Sensor clock domains documented.
- [ ] Timestamp units documented.
- [ ] Offset/drift correction documented.
- [ ] Cross-modal synchronization validated.

## Privacy/security
- [ ] Faces and sensitive visual regions reviewed.
- [ ] Personal room labels removed or generalized.
- [ ] Wi-Fi identifiers pseudonymized where required.
- [ ] Cellular/BTS identifiers reviewed and minimized.
- [ ] Raw maps reviewed for sensitive information.

## Benchmark
- [ ] Splits frozen.
- [ ] Leakage checks completed.
- [ ] Evaluation metrics frozen.
- [ ] Baselines reproduced.
- [ ] Test-set policy documented.

## Publication
- [ ] Dataset license finalized.
- [ ] Data-use/ethics statement finalized.
- [ ] Archive/hosting selected.
- [ ] Checksums generated.
- [ ] DOI/citation added.
