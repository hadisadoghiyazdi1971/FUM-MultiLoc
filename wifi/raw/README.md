# FUM-MultiLoc Dataset

## Wi-Fi Fingerprint Database for Indoor Positioning System

## 1. Overview

This dataset is a Wi-Fi fingerprint collection developed for indoor positioning research at the Faculty of Engineering, Ferdowsi University of Mashhad.

The dataset contains synchronized Wi-Fi Received Signal Strength (RSS) measurements together with spatial and device-related metadata. It is designed to support research on fingerprint-based Indoor Positioning Systems (IPS), including localization, fingerprint matching, machine learning-based positioning, and multimodal sensor fusion.

The dataset is part of the larger **FUM-MultiLoc benchmark**, which aims to provide a multimodal indoor localization platform using Wi-Fi, IMU, camera, cellular signals, and semantic indoor maps.

---

# 2. Dataset Contents

This release contains two equivalent representations of the Wi-Fi fingerprint database:

```
pivot_signal_table.csv
pivot_signal_table.json
```

## CSV Format

`pivot_signal_table.csv` is the main machine-learning-ready format.

Each row represents one Wi-Fi fingerprint measurement collected at a specific physical location.

The dataset contains:

* 3943 fingerprint samples
* 119 total attributes
* 104 Wi-Fi signal features
* Multiple smartphone devices
* Multiple indoor floors

---

# 3. Data Organization

Each sample contains three main groups of information:

## 3.1 Spatial and Collection Metadata

| Field           | Description                                       |
| --------------- | ------------------------------------------------- |
| id              | Unique sample identifier                          |
| building_id     | Building identifier                               |
| floor1_id       | Primary floor identifier                          |
| floor2_id       | Secondary floor identifier                        |
| space_id        | Indoor semantic space identifier (when available) |
| lat             | Latitude of collection point                      |
| lon             | Longitude of collection point                     |
| timestamp_epoch | Measurement timestamp in milliseconds             |

---

## 3.2 Device and Sensor Information

| Field        | Description                           |
| ------------ | ------------------------------------- |
| phone        | Smartphone model used for measurement |
| gps_lat      | GPS latitude recorded by device       |
| gps_lon      | GPS longitude recorded by device      |
| gps_accuracy | GPS reported accuracy in meters       |
| ori_x        | Device orientation angle X            |
| ori_y        | Device orientation angle Y            |
| ori_z        | Device orientation angle Z            |

The orientation values can be used for studying the effect of user/device heading on Wi-Fi fingerprints.

---

# 3.3 Wi-Fi RSS Fingerprints

Wi-Fi measurements are stored using BSSID-based feature names.

Example:

```
signal_46d9e70ba363
signal_b28ba98d7dff
signal_fae2c614d290
```

Each feature represents the RSS value received from one Access Point (AP).

The values are expressed in dBm.

Example:

```
-52  : strong received signal
-75  : medium received signal
-100 : AP not detected
```

The value `-100 dBm` is used as the missing AP representation.

---

# 4. Example Record

A single fingerprint sample contains:

```
Sample ID:
1

Building:
1

Floor:
4

Device:
HONOR/ALI-NX1

Timestamp:
1765436417007

Position:
Latitude: 36.3126330
Longitude: 59.5263441

Wi-Fi fingerprint:

AP_1 : -64 dBm
AP_2 : -87 dBm
AP_3 : -100 dBm
...
```

# 6. Missing Values

Unavailable Wi-Fi access points are represented as:

```
RSS = -100 dBm
```

Users should not remove these values without considering the effect of missing AP visibility on indoor localization performance.

Recommended preprocessing:

* Keep the original RSS matrix
* Normalize RSS values
* Optionally add AP visibility masks

---

# 7. Coordinate Information

The dataset currently provides geographic coordinates:

```
latitude
longitude
```

For metric indoor localization experiments, conversion to a local coordinate system is recommended:

```
Latitude/Longitude
        |
        v
Local Cartesian Coordinate
        |
        v
(x,y) position in meters
```

---

# 8. Device Diversity

Measurements were collected using multiple smartphones.

Available devices include:

* HONOR/ALI-NX1
* Redmi/24117RN76G
* Redmi/2303CRA44A
* Samsung/SM-N975F

Device information is provided to enable:

* Cross-device evaluation
* Device adaptation studies
* Domain shift analysis

---

# 9. Recommended Dataset Split

For fair evaluation, random splitting of adjacent samples is discouraged.

Recommended benchmark protocols:

## Session-independent split

Train and test samples are collected in different sessions.

## Device-independent split

Train and test contain different smartphone models.

## Location-independent split

Test locations are unseen during training.

## Temporal split

Training and testing are performed on different collection dates.

---

# 10. File Description

```
.
├── pivot_signal_table.csv
│   Main Wi-Fi fingerprint matrix
│
└── pivot_signal_table.json
    JSON representation exported from database
```

---

# 11. Citation

If you use this dataset in academic research, please cite:

```
FUM-MultiLoc:
A Multimodal Indoor Localization Benchmark Based on Wi-Fi,
IMU, Vision and Cellular Signals.

Faculty of Engineering,
Ferdowsi University of Mashhad.
```

---

# 12. License and Privacy

Before public release, sensitive information should be reviewed.

Recommended actions:

* Replace raw BSSID identifiers with anonymous AP identifiers.
* Remove personally identifiable information.
* Release semantic room information using anonymous room IDs.
* Review all camera data separately according to privacy regulations.


