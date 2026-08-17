# FUM-MultiLoc

**FUM-MultiLoc** is a planned multimodal, map-aware benchmark for indoor positioning and localization in the Faculty of Engineering environment at Ferdowsi University of Mashhad (FUM).

> **Current status — v0.1.0:** repository specification and benchmark skeleton only. No research data are distributed in this release.

The benchmark is being designed around synchronized observations from multiple modalities:

- Wi-Fi radio measurements
- Inertial Measurement Unit (IMU) streams
- Camera / visual observations
- Cellular / BTS-related measurements
- Floor plans and semantic indoor maps
- Spatial ground truth, reference points, and trajectories

The repository is intentionally separated from the large binary dataset. GitHub hosts the benchmark definition, schemas, loaders, evaluation code, documentation, and small examples. Large data releases will be attached later through an archival/data hosting service and referenced by immutable version identifiers.

## Benchmark goals

FUM-MultiLoc is intended to support reproducible research in:

1. floor classification;
2. room / zone recognition;
3. metric indoor localization;
4. inertial trajectory estimation;
5. visual localization;
6. Wi-Fi + IMU fusion;
7. multimodal localization;
8. robustness under missing or degraded modalities;
9. cross-device / cross-session evaluation;
10. map-aware and semantic localization.

## Repository layout

```text
FUM-MultiLoc/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── RELEASE_CHECKLIST.md
├── PUSH_TO_GITHUB.md
├── SECURITY_AND_PRIVACY_NOTICE.md
├── .gitignore
├── .gitattributes
│
├── docs/                  # benchmark and dataset specifications
├── schemas/               # machine-readable format contracts
├── metadata/              # metadata tables; headers only in v0.1.0
├── maps/                  # public/sanitized map products later
├── wifi/                  # Wi-Fi modality documentation and future data references
├── imu/                   # IMU modality documentation and future data references
├── vision/                # visual modality documentation and future data references
├── cellular/              # cellular/BTS modality documentation and future data references
├── ground_truth/          # reference points and trajectory ground truth
├── splits/                # fixed benchmark splits
├── benchmarks/            # task-specific benchmark definitions
├── code/                  # future loader, evaluation, and baselines
├── examples/              # small, non-sensitive examples only
├── assets/                # README figures/logo only; no raw research images
├── releases/              # release manifests/checksums; no large archives
└── .github/               # issue/PR templates and lightweight CI
```

## Data policy

**Do not commit raw research data, large image archives, videos, raw maps, or unreviewed identifiers to Git.**

The default `.gitignore` blocks common large-data formats and raw-data directories. The future public release should use pseudonymized Wi-Fi/cellular identifiers and sanitized visual/map products.

## Intended data architecture

A common sample index will connect all modalities using identifiers and synchronized timestamps. A typical logical record will eventually include:

```text
sample_id
session_id
timestamp_ns
building_id
floor_id
zone_id
room_id
x_m
y_m
z_m
heading_deg
wifi_ref
imu_ref
vision_ref
cellular_ref
split
```

The formal contracts are under [`schemas/`](schemas/).

## Coordinate system

The final benchmark will use an explicit local metric coordinate system. The origin, axis directions, floor transformations, map-to-metric transformation, vertical convention, and ground-truth uncertainty must be fixed before public data release. See [`docs/COORDINATE_SYSTEM.md`](docs/COORDINATE_SYSTEM.md).

## Versioning

Suggested release path:

- `v0.1.0` — repository skeleton and specifications
- `v0.2.0` — finalized modality schemas and metadata dictionary
- `v0.3.0` — sanitized miniature example set
- `v0.5.0` — internal benchmark candidate
- `v0.9.0` — public release candidate
- `v1.0.0` — first stable benchmark release

## Citation

A formal citation and DOI will be added when the first public dataset release is archived. Please do not cite this skeleton as a dataset release.

## License

The repository code/documentation license is provided in `LICENSE`. Dataset licensing may be different and will be specified separately before data publication.

## Contact

Project contact and maintainer information should be added before the first public data release.
