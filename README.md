# FUM-MultiLoc
FUM-MultiLoc: A Multimodal, Map-Aware Benchmark for Indoor Positioning at Ferdowsi University of Mashhad


# FUM-MultiLoc

**FUM-MultiLoc: A Multimodal, Map-Aware Benchmark for Indoor Positioning at Ferdowsi University of Mashhad**

[![Status](https://img.shields.io/badge/status-specification%20%2F%20data%20preparation-orange)](#project-status)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Benchmark](https://img.shields.io/badge/type-indoor%20positioning%20benchmark-blue)](#benchmark-tasks)
[![Modalities](https://img.shields.io/badge/modalities-Wi--Fi%20%7C%20IMU%20%7C%20Vision%20%7C%20Cellular-green)](#modalities)

---

## Overview

**FUM-MultiLoc** is an indoor positioning benchmark under development for the Faculty of Engineering environment at **Ferdowsi University of Mashhad (FUM), Mashhad, Iran**.

The benchmark is designed around synchronized and complementary sensing modalities rather than a single positioning signal. Its planned public release combines:

- **Wi-Fi fingerprints**
- **Inertial measurements (IMU)**
- **Camera / visual observations**
- **Cellular / BTS measurements**
- **Metric indoor maps**
- **Floor, zone, and room-level semantic information**
- **Reference-point and trajectory ground truth**
- **Predefined benchmark splits and evaluation protocols**

The goal is to support reproducible evaluation of indoor localization methods ranging from classical fingerprinting to multimodal sensor fusion and robust positioning under missing or degraded modalities.

> **Current state:** the repository currently contains the benchmark specification, schemas, documentation, repository organization, and release framework. Large raw data files are intentionally not stored in Git history. Dataset files will be added through dedicated versioned data releases.

---

## Why FUM-MultiLoc?

Many indoor-positioning datasets focus on a single sensing modality, a single localization task, or a limited evaluation protocol. FUM-MultiLoc is being organized as a **benchmark rather than a data dump**, with explicit support for:

1. **single-modality localization;**
2. **multimodal fusion;**
3. **metric and semantic localization;**
4. **trajectory estimation;**
5. **cross-session and cross-device evaluation;**
6. **robustness to missing modalities;**
7. **reproducible train/validation/test protocols;**
8. **future benchmark extensions without breaking earlier versions.**

The benchmark is intended to make it possible to compare methods under the same spatial definitions, sensor conventions, data splits, and evaluation metrics.

---

## Modalities

| Modality | Planned Content | Typical Use |
|---|---|---|
| **Wi-Fi** | AP observations, RSSI, frequency/channel information, timestamps | Fingerprinting, floor/room classification, metric localization |
| **IMU** | Accelerometer, gyroscope, and available inertial streams | PDR, trajectory estimation, motion modeling |
| **Vision** | Indoor camera frames or image sequences with synchronized references | Visual place recognition, visual localization, multimodal fusion |
| **Cellular / BTS** | Cellular signal observations and radio measurements | Cellular localization, complementary radio sensing |
| **Maps** | Floor plans, metric coordinate definitions, semantic regions | Map-aware localization, constraints, visualization |
| **Ground Truth** | Reference points, poses, trajectories, floor/room labels | Training, validation, and benchmark evaluation |

Exact fields, units, sampling characteristics, anonymization rules, and synchronization conventions are defined in the corresponding schema and documentation files.

---

## Benchmark Tasks

FUM-MultiLoc is designed to support a family of related indoor-positioning tasks.

### T1 — Floor Classification

Predict the floor of a sample or observation sequence.

**Input examples:** Wi-Fi, cellular, vision, or multimodal observations  
**Output:** `floor_id`

---

### T2 — Room / Zone Recognition

Predict the semantic room or indoor zone associated with a sample.

**Output examples:**

```text
building_id
floor_id
zone_id
room_id
room_type
```

---

### T3 — Metric Indoor Localization

Estimate a metric position in the benchmark coordinate system.

\[
\hat{\mathbf{p}} = (\hat{x},\hat{y})
\]

or, when height information is available,

\[
\hat{\mathbf{p}} = (\hat{x},\hat{y},\hat{z})
\]

Typical evaluation will include localization error statistics such as mean, median, RMSE, and percentile errors.

---

### T4 — IMU Trajectory Estimation

Estimate a pedestrian trajectory from inertial measurements.

Potential evaluation includes:

- trajectory error,
- position drift,
- absolute trajectory error,
- relative trajectory error.

---

### T5 — Visual Localization

Estimate location and, where supported, orientation from indoor visual observations.

Potential outputs include:

```text
x
y
z
heading
floor_id
room_id
```

---

### T6 — Wi-Fi + IMU Fusion

Evaluate fusion methods that combine radio fingerprints with pedestrian motion estimates.

This task is intended for classical filters as well as learned fusion approaches.

---

### T7 — Full Multimodal Localization

Combine several available modalities:

\[
\{\text{Wi-Fi},\text{IMU},\text{Vision},\text{Cellular},\text{Map}\}
\rightarrow
\{\text{Floor},\text{Room},\text{Position},\text{Trajectory}\}.
\]

---

### T8 — Missing-Modality Robustness

Evaluate localization when one or more modalities are unavailable or degraded.

Example conditions may include:

- no camera,
- no Wi-Fi,
- weak cellular measurements,
- partial IMU availability,
- delayed or missing observations.

This task is intended to measure robustness in realistic operational conditions.

---

## Benchmark Philosophy

FUM-MultiLoc follows five main principles.

### 1. Reproducibility

Benchmark splits, coordinate conventions, evaluation metrics, and data schemas are versioned.

### 2. Modality Independence

Researchers should be able to use only the modalities needed for a given experiment without downloading unrelated data.

### 3. Explicit Ground Truth

Ground-truth definitions and their expected precision are documented separately from sensor measurements.

### 4. No Hidden Spatial Ambiguity

Floor, room, zone, and metric coordinates are represented by explicit identifiers and coordinate-system documentation.

### 5. Stable Benchmark Versions

Published benchmark versions should remain reproducible even as new sessions, devices, floors, or modalities are added later.

---

## Repository Structure

```text
FUM-MultiLoc/
│
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── RELEASE_CHECKLIST.md
├── SECURITY_AND_PRIVACY_NOTICE.md
│
├── docs/
│   ├── DATASET_CARD.md
│   ├── BENCHMARK_PROTOCOL.md
│   ├── COLLECTION_PROTOCOL.md
│   ├── COORDINATE_SYSTEM.md
│   ├── DATA_DICTIONARY.md
│   ├── GROUND_TRUTH_SPEC.md
│   ├── PRIVACY_AND_ANONYMIZATION.md
│   ├── SPLIT_POLICY.md
│   ├── TIMESTAMP_AND_SYNC.md
│   └── DATA_HOSTING_AND_VERSIONING.md
│
├── schemas/
│   ├── sample.schema.json
│   ├── wifi.schema.json
│   ├── imu.schema.json
│   ├── vision.schema.json
│   ├── cellular.schema.json
│   └── ground_truth.schema.json
│
├── metadata/
│   ├── sessions.csv
│   ├── devices.csv
│   ├── sensors.csv
│   └── locations.csv
│
├── maps/
├── wifi/
├── imu/
├── vision/
├── cellular/
│
├── ground_truth/
│   ├── reference_points/
│   └── trajectories/
│
├── splits/
│   └── benchmark_v1/
│
├── benchmarks/
│   ├── wifi_only/
│   ├── imu_only/
│   ├── vision_only/
│   ├── wifi_imu/
│   └── multimodal/
│
├── code/
│   ├── loader/
│   ├── evaluation/
│   └── baselines/
│
├── examples/
├── assets/
└── releases/
```

Each top-level dataset component has its own README describing the expected content and release policy.

---

## Core Metadata Model

A synchronized benchmark sample is expected to be represented by a common identifier and a shared timestamp/reference structure.

Conceptually:

```text
sample_id
session_id
timestamp

building_id
floor_id
zone_id
room_id

x
y
z
heading

wifi_ref
imu_ref
vision_ref
cellular_ref

device_id
trajectory_id
split
```

The exact public schema is versioned under [`schemas/`](schemas/).

---

## Spatial Organization

Indoor space is represented hierarchically:

```text
Building
└── Floor
    └── Zone
        └── Room
            └── Room Type
```

Example:

```text
ENG
└── F2
    └── WEST
        └── R215
            └── faculty_office
```

Personally identifying room labels are not required for benchmark tasks. Public releases are intended to use stable research identifiers and semantic room categories.

---

## Coordinate System

Metric localization requires one benchmark-wide coordinate convention.

The final public release will specify:

- coordinate-system origin,
- axis direction,
- units,
- floor elevation,
- transformation between floor-plan pixels and metric coordinates,
- valid spatial regions,
- reference-point precision,
- pose and heading conventions.

See [`docs/COORDINATE_SYSTEM.md`](docs/COORDINATE_SYSTEM.md).

---

## Time Synchronization

Multimodal benchmarking depends on reliable temporal alignment.

The synchronization specification defines how timestamps from:

- Wi-Fi scans,
- IMU samples,
- images,
- cellular measurements,
- ground-truth observations

are associated with the same sample or trajectory.

See [`docs/TIMESTAMP_AND_SYNC.md`](docs/TIMESTAMP_AND_SYNC.md).

---

## Planned Benchmark Splits

The benchmark will avoid naive random splitting of highly correlated consecutive samples.

Candidate evaluation protocols include:

| Split | Purpose |
|---|---|
| **Session-independent** | Generalization to unseen acquisition sessions |
| **Trajectory-independent** | Prevent leakage between neighboring trajectory samples |
| **Device-independent** | Evaluate device heterogeneity |
| **User-independent** | Evaluate user-independent performance where applicable |
| **Day-independent** | Evaluate temporal generalization |
| **Cross-floor** | Evaluate transfer across spatial regions |
| **Environment-change** | Evaluate robustness to temporal/environmental changes |

The authoritative split definitions will be versioned under [`splits/`](splits/).

---

## Evaluation Metrics

Depending on the task, benchmark reports may include:

### Metric localization

- Mean Position Error
- Median Position Error
- RMSE
- 75th percentile error
- 90th percentile error
- 95th percentile error

### Floor / room recognition

- Accuracy
- Macro F1
- Per-class recall
- Confusion matrix

### Trajectory estimation

- Absolute Trajectory Error (ATE)
- Relative Pose / Trajectory Error
- Drift statistics

### Robust multimodal localization

- performance with all modalities,
- performance after removing each modality,
- degradation relative to full-modality performance.

The versioned scoring protocol is maintained in [`docs/BENCHMARK_PROTOCOL.md`](docs/BENCHMARK_PROTOCOL.md).

---

## Data Organization Strategy

Large sensor data are intentionally separated from source-code version control.

The repository itself is intended to contain:

- documentation,
- schemas,
- metadata definitions,
- benchmark splits,
- evaluation code,
- baseline code,
- small examples,
- release manifests.

Large dataset artifacts, especially camera data, will be distributed through dedicated versioned dataset releases rather than committed directly to Git history.

Planned data packages may include:

```text
FUM-MultiLoc-Core
FUM-MultiLoc-WiFi
FUM-MultiLoc-IMU
FUM-MultiLoc-Vision
FUM-MultiLoc-Cellular
FUM-MultiLoc-Full
```

This organization allows users to download only the modalities needed for their experiments.

---

## Data Release Tiers

The benchmark is planned around multiple access tiers.

### Tier 0 — Metadata / Specification

Small files needed to understand the benchmark:

- schemas,
- data dictionary,
- sample indices,
- benchmark protocol,
- map metadata.

### Tier 1 — Benchmark Core

A practical package containing the principal benchmark measurements and labels.

### Tier 2 — Full Multimodal Release

The complete multimodal dataset, including large visual data where publication and privacy requirements permit.

---

## Privacy and Anonymization

Before public release, potentially sensitive information must be reviewed.

This includes:

### Vision

Possible sensitive content:

- faces,
- personal documents,
- monitor content,
- whiteboards,
- office name plates,
- personal identifiers.

### Wi-Fi

Network identifiers may require pseudonymization.

### Cellular / BTS

Infrastructure identifiers may require transformation or selective publication.

### Maps and rooms

Public semantic identifiers should avoid unnecessary disclosure of personally identifying or operationally sensitive information.

The benchmark privacy policy is documented in:

[`docs/PRIVACY_AND_ANONYMIZATION.md`](docs/PRIVACY_AND_ANONYMIZATION.md)

and

[`SECURITY_AND_PRIVACY_NOTICE.md`](SECURITY_AND_PRIVACY_NOTICE.md).

---

## Baselines

The benchmark will include reference implementations where appropriate.

Planned baseline families include:

### Wi-Fi

- KNN
- Weighted KNN
- Random Forest
- simple neural fingerprinting baseline

### IMU

- pedestrian dead reckoning baseline

### Vision

- image retrieval / visual place-recognition baseline

### Wi-Fi + IMU

- filtering or learned sensor-fusion baseline

### Multimodal

- reference multimodal fusion model

Baselines are not intended to define the state of the art. Their purpose is to verify the benchmark pipeline and provide reproducible reference scores.

---

## Reproducibility

A benchmark release is considered reproducible only when it provides:

- immutable version identifier,
- data manifest,
- cryptographic checksums,
- schema version,
- split version,
- evaluation version,
- baseline configuration,
- documented preprocessing,
- release notes.

Release-related files are stored under [`releases/`](releases/).

---

## Project Status

**Current repository stage: `v0.1.x — Specification and Repository Preparation`**

Current work focuses on:

- repository organization,
- modality schemas,
- metadata contracts,
- privacy review,
- coordinate-system specification,
- synchronization policy,
- benchmark task definition,
- data inventory preparation.

### Planned development stages

```text
v0.1.x  Repository and benchmark specification
v0.2.x  Data inventory and finalized schemas
v0.3.x  Small public example / loader validation
v0.5.x  Internal benchmark candidate
v0.9.x  Public release candidate
v1.0.0  First stable benchmark release
```

No benchmark score should be reported as an official FUM-MultiLoc result before the corresponding public benchmark version is frozen.

---

## Data Availability

**The full dataset is not yet publicly released.**

This repository currently serves as the canonical specification and software location for FUM-MultiLoc.

Official dataset download links, persistent identifiers, checksums, and version information will be added here when the first data release is ready.

---

## Documentation

Important documents:

- [Dataset Card](docs/DATASET_CARD.md)
- [Benchmark Protocol](docs/BENCHMARK_PROTOCOL.md)
- [Collection Protocol](docs/COLLECTION_PROTOCOL.md)
- [Coordinate System](docs/COORDINATE_SYSTEM.md)
- [Ground Truth Specification](docs/GROUND_TRUTH_SPEC.md)
- [Timestamp and Synchronization](docs/TIMESTAMP_AND_SYNC.md)
- [Data Dictionary](docs/DATA_DICTIONARY.md)
- [Split Policy](docs/SPLIT_POLICY.md)
- [Privacy and Anonymization](docs/PRIVACY_AND_ANONYMIZATION.md)
- [Data Hosting and Versioning](docs/DATA_HOSTING_AND_VERSIONING.md)

---

## Using the Benchmark

The final benchmark workflow is intended to follow this pattern:

```text
Download selected modalities
        ↓
Verify release manifest/checksums
        ↓
Load metadata and synchronized sample index
        ↓
Use official train/validation/test split
        ↓
Train / run localization method
        ↓
Export predictions in benchmark format
        ↓
Run official evaluator
        ↓
Report benchmark version + task + metrics
```

Example usage code will be added under [`examples/`](examples/) as loaders become stable.

---

## Result Reporting

Scientific publications using FUM-MultiLoc should report at least:

```text
Dataset version
Benchmark task
Split version
Modalities used
Preprocessing
Evaluation version
Primary metric
Secondary metrics
Random seed / number of runs where applicable
```

A result without the benchmark version and split identifier may not be directly comparable with results from another release.

---

## Citation

A formal citation and persistent dataset identifier will be provided with the first stable public data release.

Until then, please refer to the repository as:

> **FUM-MultiLoc: A Multimodal, Map-Aware Benchmark for Indoor Positioning at Ferdowsi University of Mashhad.**

A machine-readable citation file will be maintained in `CITATION.cff`.

---

## Contributing

Contributions related to:

- loaders,
- benchmark validation,
- evaluation tools,
- documentation,
- baseline implementations,
- schema checks,
- reproducibility utilities

are welcome.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

Dataset-content changes and benchmark-protocol changes require additional review because they can affect comparability across versions.

---

## Issues

Use GitHub Issues for:

- documentation problems,
- loader bugs,
- evaluator bugs,
- schema inconsistencies,
- reproducibility problems,
- benchmark questions.

Do not post private, personally identifying, restricted, or security-sensitive dataset content in public issues.

---

## License

Repository code and documentation are currently distributed under the terms stated in [LICENSE](LICENSE).

The final dataset release may require a separate dataset-specific license or data-use notice. If so, the applicable terms will be published with each data release.

---

## Maintainers

**FUM-MultiLoc Project**  
Ferdowsi University of Mashhad  
Faculty of Engineering  
Mashhad, Iran

Repository:

`https://github.com/hadisadoghiyazdi1971/FUM-MultiLoc`

---

## Acknowledgment

FUM-MultiLoc is being developed as a reproducible research resource for indoor positioning, multimodal localization, and sensor-fusion studies.

Details of contributors, data-collection support, institutional acknowledgments, and related publications will be added as the benchmark release matures.

---

## Quick Links

- [Dataset Card](docs/DATASET_CARD.md)
- [Benchmark Protocol](docs/BENCHMARK_PROTOCOL.md)
- [Data Schemas](schemas/)
- [Ground Truth](ground_truth/)
- [Benchmark Splits](splits/)
- [Baselines](code/baselines/)
- [Evaluation](code/evaluation/)
- [Roadmap](ROADMAP.md)
- [Contributing](CONTRIBUTING.md)
- [License](LICENSE)
