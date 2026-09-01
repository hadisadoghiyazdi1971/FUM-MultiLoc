# Text Modality

This directory contains the textual and semantic representations used in the indoor positioning benchmark.

The text modality is derived from semantic descriptions of indoor images and is organized to support two complementary experimental settings:

1. **Object-level localization**
2. **Image-level semantic localization**

The main distinction is that object-level files represent individual semantic objects independently of a specific image, while image-level text embeddings encode the collection of semantic objects associated with a complete image.

This distinction was introduced to support different localization experiments. In the current experiments, object-level representations produced better localization performance, particularly when uncertainty was estimated separately for each semantic object.

---

# Directory Structure

```text
text/
├── raw/
│   └── image_descriptions.json
│
└── processed/
    ├── embeddings/
    │   ├── object_embeddings.npy
    │   ├── text_object_embeddings.npy
    │   ├── text_embeddings.npy
    │   ├── text_embeddings_train.npy
    │   └── text_embeddings_test.npy
    │
    └── label/
        ├── object_locations.json
        ├── object_names.npy
        ├── test_object_names.npy
        ├── text_embeddings_image_names.npy
        └── text_names_train.npy
```

---

# 1. Raw Data

The `raw/` directory contains the original semantic descriptions generated for the indoor images.

```text
raw/
└── image_descriptions.json
```

The file stores structured semantic information extracted from each image.

Typical information includes:

* location identifiers,
* semantic reference objects,
* object names,
* object types,
* relative object positions,
* detailed natural-language scene descriptions,
* image-related metadata.

The raw file acts as the source from which the processed textual representations are generated.

Conceptually:

```text
Indoor Image
     │
     v
Semantic Description
     │
     v
image_descriptions.json
     │
     ├───────────────┐
     │               │
     v               v
Object-Level     Image-Level
Representation  Representation
```

---

# 2. Processed Data

The `processed/` directory contains representations derived from the raw image descriptions.

It is divided into:

```text
processed/
├── embeddings/
└── label/
```

The `embeddings/` directory contains numerical semantic representations.

The `label/` directory contains names, identifiers, and spatial labels required to associate those embeddings with semantic objects or images.

---

# 3. Object-Level Representation

Object-level representations treat each semantic object as an independent localization observation.

For example, an indoor image may contain:

```text
B3 sign
central counter
wall-mounted display
exit sign
stairs
corridor entrance
```

At the object level, these objects are represented separately.

Conceptually:

```text
Image
 │
 ├── Object 1
 ├── Object 2
 ├── Object 3
 └── Object N
        │
        v
Individual Object Embeddings
```

This representation allows the localization system to reason separately about each visible semantic landmark.

It also makes it possible to estimate uncertainty independently for each object.

---

# 3.1 `object_embeddings`

`object_embeddings` contains embeddings corresponding to individual semantic objects observed in the indoor environment.

Each embedding represents one object rather than the complete semantic content of an image.

Examples of possible semantic objects include:

```text
guide sign
door
stairs
counter
display
corridor entrance
faculty-office sign
laboratory sign
exit sign
```

These representations are intended primarily for object-level localization experiments.

---

# 3.2 `test_object_embeddings`

`text_object_embeddings` is splitted object embedding for test
---

# 3.3 `object_names`

`object_names` contains the semantic names corresponding to the object-level representations.

This file provides the mapping between object embeddings and human-readable semantic object names.

Conceptually:

```text
Embedding Row 0  →  Object Name 0
Embedding Row 1  →  Object Name 1
Embedding Row 2  →  Object Name 2
...
```

The order of entries must therefore remain synchronized with the corresponding object embedding file.

---
### 3.4 `object_locations`

`object_locations` stores the geographic locations associated with semantic identifiers and reference objects in the indoor environment.

Each key corresponds to a semantic token used in the object-level representation, such as:

```text
ID::<identifier>
```

or:

```text
REF::<object_type>::<object_name>
```

The value of each key is a list of one or more geographic coordinates where that semantic object or identifier has been observed or registered.

Example:

```json
{
  "ID::تجهیزات برقی": [
    [
      36.3124148,
      59.5275781
    ]
  ],

  "REF::تابلو::تابلوی برق": [
    [
      36.3124148,
      59.5275781
    ],
    [
      36.3131817,
      59.5262728
    ],
    [
      36.3131791,
      59.5262519
    ],
    [
      36.3121649,
      59.5266714
    ]
  ]
}
```

Each coordinate pair is represented as:

```text
[latitude, longitude]
```

A semantic object may therefore be associated with:

```text
one location
```

or:

```text
multiple locations
```

depending on how frequently and where that object appears in the building.

This is especially important for common semantic objects such as:

```text
electrical panels
doors
stairs
exit signs
corridor signs
office signs
```

which may occur at several different positions.

The object-level representation can therefore be viewed as a semantic landmark-to-location mapping:

```text
Semantic Object
      │
      v
Object Name / Identifier
      │
      v
Object Embedding
      │
      v
Candidate Geographic Locations
```

During localization, an observed semantic object is first represented in the embedding space and matched against the known object database.

Conceptually:

```text
Observed Semantic Object
          │
          v
Object / Text Embedding
          │
          v
Similarity Matching
          │
          v
Matched Semantic Object
          │
          v
One or More Candidate Locations
          │
          v
Uncertainty-Aware Localization
          │
          v
Final Position Estimate
```

When a matched semantic object is associated with multiple locations, the object alone may not uniquely determine the user's position.

For example:

```text
REF::تابلو::تابلوی برق
```

may correspond to several different positions in the building.

In such cases, the localization algorithm must use additional evidence, such as:

* other detected semantic objects,
* similarity scores,
* object-specific uncertainty,
* spatial consistency between candidate landmarks,
* or information from other modalities.

This allows ambiguous objects to contribute useful localization information without treating them as unique location identifiers.

In contrast, highly distinctive identifiers may correspond to only one location and therefore provide stronger localization evidence.

The `object_locations` file should therefore be interpreted as a mapping:

```text
semantic object
        ↓
set of candidate geographic locations
```

rather than a simple one-to-one mapping between each object and a single position.

---

# 3.5 Important Property of Object-Level Data

The object-level files do not simply represent all objects belonging to one particular image.

Instead, they represent the collection of semantic objects available inside the building as independent landmarks.

Therefore:

```text
object_embeddings
object_names
object_locations
```

should be interpreted as a semantic landmark database.

This database can be queried using objects detected or extracted from a new observation.

---

# 4. Image-Level Representation

Image-level representations combine the semantic information associated with all objects appearing in a single image.

For example, if an image contains:

```text
B3 sign
exit sign
central counter
wall display
stairs
```

the image-level text representation encodes the semantic content of the complete observation.

Conceptually:

```text
Image
 │
 ├── Object A
 ├── Object B
 ├── Object C
 └── Object D
       │
       v
Combined Semantic Text
       │
       v
Text Encoder
       │
       v
Image-Level Text Embedding
```

This representation is different from the object-level approach because the semantic information is aggregated before or during encoding.

---

# 4.1 `text_embeddings`

`text_embeddings` contains the image-level textual embeddings.

Each embedding corresponds to the combined semantic information extracted from one image.

Therefore, one row or embedding vector represents one image rather than one individual object.

Conceptually:

```text
Image 1
 ├── Object A
 ├── Object B
 └── Object C
        │
        v
Combined Text
        │
        v
Text Encoder
        │
        v
text_embeddings[0]
```

---

# 4.2 `text_embeddings_train`

`text_embeddings_train` contains the image-level text embeddings assigned to the training split.

These embeddings are generated from the semantic descriptions associated with the benchmark training images.

They are used in experiments where the complete semantic content of an image is treated as a single localization representation.

---

# 4.3 `text_embeddings_test`

`text_embeddings_test` contains the image-level text embeddings assigned to the test split.

The representation format should remain identical to `text_embeddings_train`.

The corresponding image identifiers are stored separately so that each embedding can be associated with the correct benchmark sample.

---

# 4.4 `text_embeddings_image_names`

`text_embeddings_image_names` stores the image identifiers corresponding to the image-level embeddings.

This mapping is necessary because numerical embedding arrays do not directly preserve the original image filename.

Conceptually:

```text
text_embeddings[0]
        │
        └── image_001.jpg

text_embeddings[1]
        │
        └── image_002.jpg
```

The ordering of this file must remain consistent with the corresponding embedding matrix.

---

# 4.5 `text_names_train`

`text_names_train` contains the identifiers or image names corresponding to the training image-level text embeddings.

It acts as the lookup structure for:

```text
text_embeddings_train
```

Conceptually:

```text
text_embeddings_train[i]
          ↕
text_names_train[i]
```

This correspondence must not be changed independently.

---

# 4.6 `test_object_names`

`test_object_names` contains the semantic object names associated with the object-level test configuration.

It is intended to identify the semantic objects involved in evaluation.

The ordering of these entries should remain synchronized with the corresponding test representations used in the experiment.

---

# 5. Object-Level vs. Image-Level Experiments

The text modality intentionally supports two different formulations.

## Object-Level

```text
Individual Object
      │
      v
Object Embedding
      │
      v
Object Matching
      │
      v
Object Location
      │
      v
Position Estimate
```

Advantages include:

* explicit semantic landmarks,
* separate evidence from each object,
* object-specific spatial information,
* independent uncertainty estimation,
* improved interpretability,
* robustness when some objects are unreliable.

---

## Image-Level

```text
All Objects in Image
        │
        v
Combined Text Representation
        │
        v
Image-Level Embedding
        │
        v
Localization
```

Advantages include:

* compact representation,
* direct image-to-location semantic retrieval,
* simpler inference pipeline,
* representation of contextual relationships among multiple objects.

---

# 6. Why Both Representations Are Included

The two representations correspond to different research hypotheses.

In the image-level setting, all semantic information extracted from one observation is encoded into a single representation.

This can be written as:

```text
Image_i
   │
   ├── Object_1
   ├── Object_2
   ├── ...
   └── Object_n
          │
          v
      Text Encoder
          │
          v
       Embedding_i
```

In the object-level setting:

```text
Object_1 → Embedding_1
Object_2 → Embedding_2
...
Object_n → Embedding_n
```

Each object therefore contributes independent localization evidence.

This distinction is particularly important when some objects are much more informative than others.

For example:

```text
generic door
```

may provide weak localization information, while:

```text
B3 guide sign
```

may provide strong localization information.

Treating these observations separately makes it possible to assign different levels of confidence to each semantic landmark.

---

# 7. Object-Level Uncertainty

One motivation for the object-level representation is the ability to estimate uncertainty independently for each semantic object.

Conceptually:

```text
Observed Object
      │
      v
Semantic Similarity
      │
      v
Candidate Landmark
      │
      v
Estimated Location
      │
      v
Uncertainty
```

Different objects may have significantly different localization reliability.

For example:

```text
Object A
Highly distinctive sign
Low uncertainty

Object B
Generic door
High uncertainty
```

This permits uncertainty-aware localization:

```text
Object 1 → Position 1 ± Uncertainty 1
Object 2 → Position 2 ± Uncertainty 2
Object 3 → Position 3 ± Uncertainty 3

                  │
                  v

          Weighted Fusion

                  │
                  v

        Final Position Estimate
```

In the experiments associated with this dataset, the object-level representation provided better performance than representing the complete semantic content of an image with a single text embedding.

For this reason, both representations are preserved so that the two strategies can be compared under the same benchmark.

---

# 8. Relationship Between Files

The main relationships can be summarized as follows.

## Object-Level

```text
object_names
     │
     ├───────────────┐
     │               │
     v               v
object_embeddings  object_locations
```

Each semantic object has:

```text
name
embedding
location
```

---

## Object-Level Text Representation

```text
semantic object text
        │
        v
text_object_embeddings
```

---

## Image-Level

```text
image_descriptions.json
        │
        v
objects belonging to image
        │
        v
combined text representation
        │
        v
text_embeddings
```

and for predefined benchmark splits:

```text
text_embeddings_train
        ↕
text_names_train
```

and:

```text
text_embeddings_test
        ↕
corresponding test image identifiers
```

---

# 9. Relationship with `benchmarks/text_only`

The files in this directory contain the underlying text modality and processed representations.

The benchmark split itself is stored separately in:

```text
benchmarks/text_only/
```

For example:

```text
benchmarks/text_only/
├── text_train.json
├── text_test.json
└── README.md
```

The responsibilities of the two directories are different.

## `text/`

Contains:

```text
raw semantic descriptions
processed embeddings
object-level semantic landmark representations
image-level semantic embeddings
object names
object locations
embedding-to-image mappings
```

## `benchmarks/text_only/`

Contains:

```text
official train/test semantic representations
benchmark split definitions
benchmark usage instructions
```

This separation prevents benchmark definitions from being mixed with the underlying modality data.

---

# 10. Processing Pipeline

The overall processing pipeline can be summarized as:

```text
Indoor Images
      │
      v
Semantic Description Generation
      │
      v
raw/image_descriptions.json
      │
      ├─────────────────────────────┐
      │                             │
      v                             v
Object Extraction              Image-Level Text
      │                             │
      v                             v
Object Names                Combined Description
      │                             │
      v                             v
Text Encoding                Text Encoding
      │                             │
      v                             v
Object Embeddings             Text Embeddings
      │                             │
      v                             v
Object-Level IPS              Image-Level IPS
```

---

# 11. Recommended Loading Strategy

Researchers should always load embeddings together with their corresponding label or identifier files.

For example:

```text
object_embeddings
        +
object_names
        +
object_locations
```

should be treated as one synchronized object-level dataset.

Likewise:

```text
text_embeddings_train
        +
text_names_train
```

should be loaded together.

Do not reorder one file independently of its corresponding mapping file.

---

# 12. Reproducibility

Experiments using the processed embeddings should report at least:

* text encoder architecture,
* exact model version,
* input serialization strategy,
* embedding dimensionality,
* pooling method,
* normalization method,
* similarity metric,
* object matching strategy,
* uncertainty estimation method,
* localization algorithm,
* train/test split,
* benchmark version.

For object-level experiments, researchers should additionally report how evidence from multiple objects is combined.

For example:

```text
Object Encoder: <model>
Embedding Dimension: <dimension>
Similarity Metric: cosine similarity
Object Uncertainty: <method>
Fusion: uncertainty-weighted averaging
```

---

# 13. Important Note on Embedding Reproducibility

Embeddings are derived data rather than raw annotations.

They therefore depend on:

```text
encoder model
model version
tokenization
input formatting
pooling
normalization
software version
```

Whenever possible, the configuration used to generate each embedding file should be stored alongside the embeddings.

A recommended structure is:

```text
processed/
└── embeddings/
    ├── object_embeddings
    ├── object_embeddings_config.json
    │
    ├── text_object_embeddings
    ├── text_object_embeddings_config.json
    │
    ├── text_embeddings
    └── text_embeddings_config.json
```

A configuration file may contain:

```json
{
  "encoder": "MODEL_NAME",
  "model_version": "VERSION",
  "embedding_dimension": 768,
  "pooling": "mean",
  "normalization": "L2",
  "input_type": "semantic object text"
}
```

This is strongly recommended for reproducible benchmark use.

---

# 14. Experimental Interpretation

The processed text modality should be interpreted as containing two semantic scales:

```text
Fine-grained semantic scale
        │
        └── Individual Objects
             ├── object_embeddings
             ├── text_object_embeddings
             ├── object_names
             └── object_locations


Scene-level semantic scale
        │
        └── Entire Image
             ├── text_embeddings
             ├── text_embeddings_train
             ├── text_embeddings_test
             ├── text_embeddings_image_names
             └── text_names_train
```

This design allows direct comparison between:

```text
landmark-based semantic positioning
```

and:

```text
scene-level semantic positioning
```

within the same indoor environment.

---

# 15. Summary

```text
text/
│
├── raw/
│   │
│   └── image_descriptions.json
│       Complete semantic descriptions of images
│
└── processed/
    │
    ├── embeddings/
    │   │
    │   ├── object_embeddings
    │   │     Individual object representations
    │   │
    │   ├── text_object_embeddings
    │   │     Text embeddings of individual objects
    │   │
    │   ├── text_embeddings
    │   │     Image-level semantic embeddings
    │   │
    │   ├── text_embeddings_train
    │   │     Training image-level embeddings
    │   │
    │   └── text_embeddings_test
    │         Test image-level embeddings
    │
    └── label/
        │
        ├── object_locations
        │     Spatial locations of semantic objects
        │
        ├── object_names
        │     Names of semantic landmarks
        │
        ├── test_object_names
        │     Object names used in test experiments
        │
        ├── text_embeddings_image_names
        │     Image IDs corresponding to image-level embeddings
        │
        └── text_names_train
              Image IDs corresponding to training embeddings
```

The object-level representation provides a semantic landmark database, while the image-level representation encodes the complete semantic content associated with each image.

Both are included to support comparison between object-aware and scene-level text-based indoor localization methods.

---

# 16. Citation

Citation information should be added after the official publication of the dataset and assignment of a DOI.

Researchers using the text modality or the object-level semantic localization benchmark should cite the corresponding dataset publication.

---

# 17. License

The data in this directory follows the license specified in the root-level `LICENSE` file.

Any additional restrictions related to semantic descriptions, annotations, or derived embeddings should be documented in the main dataset card.
