# Benchmark Preparation

This directory contains scripts used to construct the official benchmark splits.

## `split_train_test.py`

Creates synchronized training and test subsets across the available modalities.

The script uses the selected test images to generate corresponding splits for:

* image data,
* text embeddings,
* Wi-Fi fingerprints,
* location metadata.

The original source files remain unchanged.

Conceptually:

```text
Selected Test Images
        │
        ├── Vision split
        ├── Text split
        ├── Wi-Fi split
        └── Location metadata
```

A fixed random seed is used where random selection is required to improve reproducibility.

The resulting train/test files are used by the modality-specific benchmark directories:

```text
benchmarks/
├── text_only/
├── vision_only/
└── wifi_only/
```

Researchers evaluating the official benchmark should use the provided splits rather than generating new random splits.
