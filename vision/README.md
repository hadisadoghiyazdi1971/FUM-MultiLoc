# Vision Data

This directory contains the processed visual representations and a small sample of raw images used in the indoor localization dataset.

## Directory Structure

```text
vision/
├── embeddings/
│   ├── image_embeddings_train
│   ├── image_embeddings_test
│   ├── image_names_train
│   └── image_names_test
│
└── raw/
    └── image_samples/
        └── 10 sample images
```

## Embeddings

`image_embeddings_train` and `image_embeddings_test` contain the precomputed visual embeddings for the training and test images.

The corresponding image identifiers are stored in:

```text
image_names_train
image_names_test
```

The ordering of the image-name files must remain consistent with the corresponding embedding files.

Conceptually:

```text
image_embeddings_train[i]
        ↕
image_names_train[i]
```

and:

```text
image_embeddings_test[i]
        ↕
image_names_test[i]
```

## Raw Image Samples

The `raw/image_samples/` directory contains 10 representative images from the dataset.

These images are provided only as visual examples of the indoor environment and are not the complete image collection.

The full image dataset may be distributed separately because of its larger storage size.

## Relationship with the Benchmark

The processed visual data in this directory are used by:

```text
benchmarks/vision_only/
```

for vision-based indoor localization experiments.

## Citation

Citation information should be added after the official dataset publication.

