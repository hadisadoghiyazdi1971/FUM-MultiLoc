# Text-Only Benchmark

This directory contains the **text-only benchmark split** of the indoor positioning dataset.

The benchmark evaluates indoor localization using only semantic textual information derived from the image descriptions.

The original and complete semantic descriptions are stored separately in:

```text
text/image_description.json
```

This directory contains only the benchmark-ready training and test splits.

---

## Directory Structure

```text
benchmarks/
└── text_only/
    ├── text_train.json
    ├── text_test.json
    └── README.md
```

The corresponding source semantic descriptions are located in:

```text
text/
└── image_description.json
```

---

# 1. Benchmark Purpose

The goal of the text-only benchmark is to evaluate whether semantic descriptions of indoor scenes can be used for indoor positioning without relying directly on:

* raw images,
* Wi-Fi fingerprints,
* IMU measurements,
* cellular signals.

Each sample is represented by a set of structured semantic tokens extracted from its corresponding image description.

The semantic representation contains two principal types of information:

```text
ID::<location_identifier>

REF::<object_type>::<object_name>
```

These tokens represent location-related identifiers and visible reference objects that may help distinguish indoor positions.

---

# 2. Source Data

The benchmark files are derived from:

```text
text/image_description.json
```

The source file contains richer semantic information for every image, including:

* location identifiers,
* reference objects,
* reference object types,
* relative object positions,
* suitability for distance estimation,
* detailed natural-language descriptions,
* image-related processing metadata.

Only a subset of these fields is used in the current text-only benchmark.

The transformation can be summarized as:

```text
text/image_description.json
        │
        ├── location_identifiers
        │          │
        │          └── ID::<identifier>
        │
        └── reference_objects
                   │
                   └── REF::<object_type>::<object_name>
                            │
                            v
                   benchmark representation
                            │
                     ┌──────┴──────┐
                     │             │
              text_train.json  text_test.json
```

---

# 3. `text_train.json`

`text_train.json` contains the semantic representations assigned to the official training split.

Each JSON key corresponds to an image identifier.

Example:

```json
{
  "1.jpg": [
    "ID::B3",
    "ID::علامت خروج",
    "REF::کانتر::ساختار مرکزی هشت‌ضلعی",
    "REF::تابلو::تابلو راهنمای B3",
    "REF::نمایشگر::نمایشگر دیواری",
    "REF::تابلو::علائم خروج",
    "REF::ورودی::ورودی راهرو فرعی",
    "REF::پله::پله‌ها"
  ]
}
```

The image filename acts as the sample identifier and can be used to associate the textual representation with other modalities in the complete dataset.

---

# 4. `text_test.json`

`text_test.json` has exactly the same representation format as `text_train.json`, but contains samples belonging to the benchmark test split.

General structure:

```json
{
  "<image_id>.jpg": [
    "ID::<identifier>",
    "REF::<object_type>::<object_name>",
    "REF::<object_type>::<object_name>"
  ]
}
```

The official training and test splits should remain fixed when reporting benchmark results.

Researchers should not randomly regenerate these splits if they intend to compare their results with the official benchmark.

---

# 5. Semantic Token Types

Two semantic token types are currently used.

## 5.1 Location Identifier

Format:

```text
ID::<location_identifier>
```

Examples:

```text
ID::B3
ID::علامت خروج
```

These tokens represent semantic entities that may provide direct or indirect information about the physical location.

Possible examples include:

* room identifiers,
* corridor identifiers,
* building signs,
* directional signs,
* office-related identifiers,
* distinctive indoor labels.

---

# 5.2 Reference Object

Format:

```text
REF::<object_type>::<object_name>
```

Example:

```text
REF::تابلو::تابلو راهنمای B3
```

Another example:

```text
REF::پله::پله‌ها
```

Reference objects represent visible landmarks within the indoor environment.

They may not uniquely identify a location individually, but combinations of reference objects can provide strong semantic location cues.

---

# 6. Removed Metadata

The source `image_description.json` contains additional information that is intentionally excluded from the current text-only benchmark representation.

Examples include:

```text
relative_position

suitability_for_distance_estimation

detailed_description

file_path

file_size

processed_at
```

These fields remain available in the source text data for future experiments but are not part of the current official text-only input representation.

This separation provides a controlled benchmark representation and prevents processing-related metadata from influencing localization models.

---

# 7. Intended Tasks

The text-only benchmark can support several indoor positioning and place-recognition tasks.

## Semantic Indoor Localization

```text
semantic tokens
      ↓
localization model
      ↓
predicted location
```

---

## Text Embedding-Based Localization

The semantic tokens may be transformed into textual representations and encoded using a language model.

```text
ID / REF tokens
      ↓
text serialization
      ↓
text encoder
      ↓
embedding
      ↓
localization model
```

---

## Semantic Place Recognition

The semantic representation may be used to determine whether two observations belong to:

* the same location,
* nearby locations,
* the same room,
* the same corridor or indoor region.

---

## Text-to-Location Retrieval

A semantic observation may be used as a query for retrieving the most similar known indoor location.

---

# 8. Recommended Input Serialization

Researchers may use the tokens directly or serialize them into natural-language text.

For example:

```text
ID::B3
ID::علامت خروج
REF::کانتر::ساختار مرکزی هشت‌ضلعی
REF::تابلو::تابلو راهنمای B3
```

may be transformed into:

```text
Location identifiers: B3, exit sign.
Reference objects: central octagonal counter and B3 guide sign.
```

Different serialization strategies are permitted, but they should be explicitly reported when publishing benchmark results.

---

# 10. Data Split Policy

The benchmark uses predefined training and test files:

```text
text_train.json

text_test.json
```

These files define the official split.

Indoor positioning datasets are particularly sensitive to data leakage because nearby images may share:

* the same signs,
* the same objects,
* the same room identifiers,
* similar corridor geometry,
* nearly identical semantic descriptions.

For this reason, random sample-level splitting should be avoided when constructing future versions of the benchmark.

Prefer splits based on:

```text
physical location
trajectory
collection session
spatial region
```

whenever possible.

---

# 12. Benchmark vs. Source Data

It is important to distinguish the source modality data from the benchmark configuration.

## Source Data

```text
text/image_description.json
```

contains the complete semantic information extracted from the images.

## Benchmark Data

```text
benchmarks/text_only/text_train.json
benchmarks/text_only/text_test.json
```

contains the processed and predefined split used for evaluation.

Therefore:

```text
source data
    ↓
semantic preprocessing
    ↓
benchmark representation
    ↓
official train/test split
```

This separation allows future benchmark versions to introduce new representations without modifying the original semantic source data.

---

# 13. Reproducibility Requirements

When reporting results using this benchmark, researchers should specify at least:

* benchmark version,
* text encoder,
* input serialization strategy,
* embedding dimensionality,
* normalization method,
* training method,
* localization target,
* evaluation metrics,
* use of any additional external data.

The official `text_train.json` and `text_test.json` splits should be preserved.

---

# 15. Summary

```text
text/image_description.json
│
│  Complete semantic source data
│
├── location identifiers
├── reference objects
├── relative positions
├── detailed descriptions
└── metadata
        │
        │ semantic preprocessing
        v
benchmarks/text_only/
│
├── text_train.json
│      Official training samples
│
├── text_test.json
│      Official test samples
│
└── README.md
```

The `text_only` benchmark therefore contains only the processed representations and official splits required for text-based indoor localization experiments.

---

# 16. Citation

Citation information should be added after the official dataset publication and DOI assignment.

Researchers using this benchmark should cite the corresponding dataset or benchmark publication.

---

# 17. License

The benchmark follows the license specified in the root-level `LICENSE` file.

Any restrictions related to semantic descriptions, personal identifiers, or derived annotations should also be documented in the main dataset license and dataset card.
