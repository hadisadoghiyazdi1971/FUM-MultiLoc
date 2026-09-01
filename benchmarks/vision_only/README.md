# Vision-Only Benchmark

This directory contains the **vision-only benchmark** for indoor localization.

The benchmark uses precomputed image embeddings as input and image locations as ground-truth labels.

## Files

```text
vision_only/
├── image_embeddings_train.npy
├── image_embeddings_test.npy
├── labels.json
└── README.md
```

### `image_embeddings_train`

Contains the image embeddings used for training.

Each embedding corresponds to one image in the training split.

### `image_embeddings_test`

Contains the image embeddings used for evaluation.

Each embedding corresponds to one image in the test split.

### `labels`

Contains the mapping between image names and their corresponding locations.

Conceptually:

```text
image_name → latitude, longitude
```

The ordering or identifiers in the label file must remain consistent with the embedding files.

## Benchmark Task

The main task is:

```text
Image Embedding
      ↓
Localization Model
      ↓
Predicted Location
```

The benchmark can be used with methods such as:

* nearest-neighbor retrieval,
* regression models,
* neural networks,
* metric-learning approaches.

## Important Note

The raw images are stored separately in the `vision/` directory.

This folder only contains the processed embeddings and benchmark labels required for the official train/test evaluation.

When reporting results, researchers should preserve the provided train/test split and specify the embedding model and localization method used.

## Citation

Citation information should be added after the official dataset publication and DOI assignment.

