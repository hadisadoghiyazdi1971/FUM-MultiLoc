# Preprocessing Scripts

This directory contains scripts used to generate and preprocess the semantic and spatial data used by the benchmark.

## Files

### `gemini.py`

Analyzes indoor images using Gemini and generates structured semantic descriptions containing:

* location identifiers,
* reference objects,
* object types,
* relative positions,
* short scene descriptions.

The generated descriptions are used as the source for the text modality.

### `extract_objects.py`

Extracts semantic objects from the generated image descriptions.

It converts:

```text
location identifiers
```

into:

```text
ID::<identifier>
```

and suitable reference objects into:

```text
REF::<object_type>::<object_name>
```

### `extract_coords.py`

Extracts image coordinates from the original `tags_pic` data and creates a simplified mapping:

```text
image_id → [latitude, longitude]
```

### `object_location_map.py`

Combines semantic object annotations with image coordinates to generate:

```text
semantic object → candidate locations
```

A semantic object may therefore be associated with one or multiple geographic locations.

## Processing Pipeline

```text
Images
   ↓
gemini.py
   ↓
image_descriptions.json
   ↓
extract_objects.py
   ↓
semantic objects
   │
   ├── extract_coords.py → image coordinates
   │
   └── object_location_map.py
             ↓
       object_locations.json
```

These scripts generate derived data and are not required when using the already processed benchmark files.
