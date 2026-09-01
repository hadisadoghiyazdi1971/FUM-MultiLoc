# Wi-Fi-Only Benchmark

This directory contains the **Wi-Fi-only benchmark split** of the indoor positioning dataset.

The benchmark evaluates indoor localization using only Wi-Fi fingerprint measurements together with the corresponding spatial and device metadata.

The official benchmark is divided into predefined training and test files.

---

## Directory Structure

```text
benchmarks/
└── wifi_only/
    ├── pivot_signal_table_train.csv
    ├── pivot_signal_table_test.csv
    └── README.md
```

Depending on the release format, equivalent JSON or Parquet versions may also be provided.

---

# 1. Benchmark Purpose

The Wi-Fi-only benchmark is designed to evaluate fingerprint-based indoor positioning methods using Received Signal Strength measurements from multiple Wi-Fi access points.

Each row represents one Wi-Fi fingerprint collected at a known spatial position.

Conceptually:

```text
Wi-Fi Access Points
        │
        v
RSS Fingerprint Vector
        │
        v
Localization Model
        │
        v
Predicted Position / Floor / Space
```

The benchmark can be used for:

* indoor coordinate estimation,
* floor classification,
* building classification,
* fingerprint retrieval,
* similarity-based localization,
* cross-device localization,
* machine learning and deep learning-based positioning.

---

# 2. Train and Test Files

The benchmark uses two predefined files:

```text
pivot_signal_table_train.csv
pivot_signal_table_test.csv
```

`pivot_signal_table_train.csv` contains the samples used to train or fit localization models.

`pivot_signal_table_test.csv` contains the samples used for evaluation.

The predefined split should be preserved when reporting official benchmark results.

Researchers should not regenerate a random split if they intend to compare results directly with the benchmark.

---

# 3. Row Structure

Each row contains three main categories of information:

```text
Spatial Metadata
Device / Sensor Metadata
Wi-Fi RSS Fingerprint
```

A simplified representation is:

```text
Sample
 │
 ├── Position
 │    ├── building_id
 │    ├── floor_id
 │    ├── latitude
 │    └── longitude
 │
 ├── Device Metadata
 │    ├── phone
 │    ├── GPS
 │    └── orientation
 │
 └── Wi-Fi Fingerprint
      ├── wifi_ap_0001
      ├── wifi_ap_0002
      ├── ...
      └── wifi_ap_N
```

---

# 4. Spatial Metadata

The spatial fields describe the location associated with each fingerprint.

Typical fields include:

| Field             | Description                                         |
| ----------------- | --------------------------------------------------- |
| `id`              | Unique fingerprint sample identifier                |
| `building_id`     | Building identifier                                 |
| `floor1_id`       | Primary floor identifier                            |
| `floor2_id`       | Secondary or auxiliary floor identifier             |
| `space_id`        | Semantic indoor space identifier, when available    |
| `lat`             | Reference latitude associated with the fingerprint  |
| `lon`             | Reference longitude associated with the fingerprint |
| `timestamp_epoch` | Measurement timestamp in epoch milliseconds         |

The exact interpretation of `floor1_id` and `floor2_id` should remain consistent with the main dataset metadata.

---

# 5. Device and Sensor Metadata

Each fingerprint also contains information recorded by the mobile device.

Typical fields include:

| Field          | Description                                  |
| -------------- | -------------------------------------------- |
| `phone`        | Smartphone model used during data collection |
| `gps_lat`      | GPS latitude reported by the device          |
| `gps_lon`      | GPS longitude reported by the device         |
| `gps_accuracy` | Estimated GPS accuracy                       |
| `ori_x`        | Device orientation component                 |
| `ori_y`        | Device orientation component                 |
| `ori_z`        | Device orientation component                 |

These fields are provided as auxiliary metadata.

For a strict Wi-Fi-only experiment, researchers should clearly state whether they use only the RSS fingerprint or also include any auxiliary metadata.

---

# 6. Wi-Fi Fingerprint Features

The Wi-Fi fingerprint is represented by one column per anonymized access point.

Example:

```text
wifi_ap_0001
wifi_ap_0002
wifi_ap_0003
...
wifi_ap_N
```

Each column contains the Received Signal Strength Indicator (RSSI) measured from that access point.

Typical values are expressed in dBm.

For example:

```text
-45  strong signal
-65  moderate signal
-85  weak signal
-100 access point not detected
```

The value:

```text
-100
```

is used as the missing or not-observed access-point value in the current dataset representation.

---

# 7. Access Point Anonymization

Raw BSSID identifiers are not used in the public benchmark.

Original Wi-Fi access point identifiers are replaced by anonymous identifiers such as:

```text
wifi_ap_0001
wifi_ap_0002
wifi_ap_0003
```

Only the access-point identifier is anonymized.

The original RSSI measurement is preserved.

Conceptually:

```text
Original BSSID
      │
      v
Anonymous AP ID
      │
      v
Same RSSI Value
```

Example:

```text
signal_<raw_bssid> = -64
```

becomes:

```text
wifi_ap_0042 = -64
```

This preserves the fingerprint structure while reducing unnecessary exposure of infrastructure identifiers.

---

# 8. Example Fingerprint

A simplified sample may look like:

```text
id             = 1
building_id    = 1
floor1_id      = 4
lat            = 36.3126330
lon            = 59.5263441
phone          = HONOR/ALI-NX1

wifi_ap_0001   = -100
wifi_ap_0002   = -100
wifi_ap_0003   = -64
wifi_ap_0004   = -87
wifi_ap_0005   = -75
...
```

The full Wi-Fi feature vector can be written as:

```text
x_wifi =
[
  RSS_1,
  RSS_2,
  RSS_3,
  ...
  RSS_N
]
```

---

# 9. Recommended Baselines

Useful baseline methods include:

```text
KNN
WKNN
Random Forest
MLP
Gradient Boosting
Neural Fingerprinting Models
```

For reproducibility, researchers should report:

* preprocessing method,
* missing-value treatment,
* distance metric,
* number of neighbors,
* normalization,
* model hyperparameters,
* use of auxiliary metadata.

---

# 10. RSS Preprocessing

The benchmark preserves the original RSS representation.

Researchers may apply transformations such as:

```text
RSS clipping
normalization
standardization
visibility masking
feature selection
AP filtering
```

However, the exact preprocessing procedure should be reported.

For example:

```text
Missing AP value: -100 dBm
Normalization: min-max
Range: [0, 1]
```

or:

```text
Missing AP value: -100 dBm
Normalization: z-score over training set only
```

Preprocessing parameters should be estimated from the training set and then applied unchanged to the test set.

---

# 11. Missing Access Points

A large portion of the Wi-Fi vector may contain:

```text
-100
```

because many access points are not visible from a given position.

This sparsity is part of the fingerprint structure and should not automatically be treated as corrupted data.

The absence of an access point can itself carry useful localization information.

A binary visibility mask may optionally be derived:

```text
visible = 1  if RSS > -100
visible = 0  if RSS = -100
```

---

# 12. Train/Test Policy

The benchmark files define the official split:

```text
pivot_signal_table_train.csv
pivot_signal_table_test.csv
```

The two subsets should remain disjoint.

Researchers should avoid sample-level random reshuffling when reporting official benchmark scores.

Indoor fingerprint datasets can be especially vulnerable to optimistic results if temporally or spatially adjacent samples appear in both train and test sets.

Whenever possible, future benchmark releases should use splits based on:

```text
physical region
collection session
time
device
trajectory
```

rather than purely random rows.

---

# 13. Cross-Device Evaluation

The dataset contains smartphone metadata, enabling device-robustness experiments.

A possible evaluation protocol is:

```text
Train:
Device A + Device B

Test:
Device C
```

This allows investigation of device heterogeneity in RSS measurements.

Such experiments are useful because different smartphones may report different RSS values even at approximately the same physical location.

---

# 14. Coordinate Representation

The benchmark currently includes geographic coordinates:

```text
latitude
longitude
```

For distance-based evaluation, it may be preferable to convert these coordinates to a local metric reference system.

Conceptually:

```text
Latitude / Longitude
        │
        v
Local Coordinate Transformation
        │
        v
x, y in meters
```

Researchers should document the transformation used if results are reported in meters.

---

# 15. Evaluation Metrics

For coordinate localization, recommended metrics include:

```text
Mean Position Error
Median Position Error
RMSE
75th Percentile Error
90th Percentile Error
95th Percentile Error
```

For a predicted location:

```text
p_hat = (x_hat, y_hat)
```

and ground truth:

```text
p = (x, y)
```

the localization error can be computed as:

```text
e = ||p_hat - p||_2
```

For latitude/longitude coordinates, an appropriate geographic distance function should be used rather than direct Euclidean distance in degrees.

---

# 16. Classification Metrics

For building or floor classification, recommended metrics include:

```text
Accuracy
Macro F1
Precision
Recall
Confusion Matrix
```

For hierarchical positioning, researchers may report both:

```text
Floor Accuracy
Position Error
```

to distinguish between floor-selection errors and within-floor localization errors.

---

# 17. Reproducibility Requirements

When publishing results using this benchmark, researchers should report at least:

* benchmark version,
* Wi-Fi feature preprocessing,
* missing AP treatment,
* normalization method,
* feature-selection method, if used,
* localization model,
* hyperparameters,
* train/test protocol,
* use of device metadata,
* coordinate conversion method,
* evaluation metrics.

For nearest-neighbor methods, also report:

```text
distance metric
number of neighbors
weighting strategy
```

---

# 18. Example Experimental Pipeline

```text
pivot_signal_table_train
          │
          v
Select Wi-Fi Columns
          │
          v
RSS Preprocessing
          │
          v
Train Localization Model
          │
          v
pivot_signal_table_test
          │
          v
Apply Same Preprocessing
          │
          v
Predict Location
          │
          v
Evaluate Position Error
```

---

# 19. Summary

```text
benchmarks/wifi_only/
│
├── pivot_signal_table_train.csv
│      Official Wi-Fi training fingerprints
│
├── pivot_signal_table_test.csv
│      Official Wi-Fi test fingerprints
│
└── README.md
```

Each row represents a Wi-Fi fingerprint associated with a known indoor position.

The benchmark is intended to provide a reproducible evaluation setting for RSS-based indoor positioning while preserving the official train/test split.

---

# 20. Citation

Citation information should be added after the official publication of the dataset and assignment of a DOI.

Researchers using the Wi-Fi-only benchmark should cite the corresponding dataset or benchmark publication.

