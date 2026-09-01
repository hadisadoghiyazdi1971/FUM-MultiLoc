"""
Automated script to generate train/test indices without modifying source files.
This script:
1. Randomly selects test images from across the entire dataset (by index)
2. Keeps dataset.json and pivot_signal_table.json unchanged
3. Computes train/test indices for image/text/RSS selection
4. Saves test_set_info.json for use in run.py
"""

import copy
import json
import random
import os
from pathlib import Path

import numpy as np

# ============================================================================
# FILE PATHS CONFIGURATION
# ============================================================================

# Input file paths
PATHS = {
    # Input files
    'pic_coords': '../metadata/pic_coords.json',
    'image_names': '../metadata/image_names.npy',
    'test_set_info': '../metadata/test_set_info.json',
    'dataset': '../metadata/dataset.json',
    'pivot_table': '../metadata/pivot_signal_table.json',
    'text_embeddings': '../metadata/text_embeddings.npy',
    'text_embeddings_image_names': '../metadata/text_embeddings_image_names.npy',

    # Output files
    'dataset_train': '../metadata/dataset_train.json',
    'dataset_test': '../metadata/dataset_test.json',
    'pivot_table_train': '../metadata/pivot_signal_table_train.json',
    'pivot_table_test': '../metadata/pivot_signal_table_test.json',
    'text_embeddings_train': '../metadata/text_embeddings_train.npy',
    'text_embeddings_test': '../metadata/text_embeddings_test.npy',
    'text_names_train': '../metadata/text_names_train.npy',
    'test_set_info_output': '../test_set_info.json',
}

# ============================================================================
# CONFIGURATION
# ============================================================================

# Random seed for reproducibility
RANDOM_SEED = 42

# Number of test images (set to None to use all from test_set_info.json)
# If you want to randomly select a specific number, set TEST_IMAGES_COUNT = 200
# If you want to use all images from test_set_info.json, set TEST_IMAGES_COUNT = None
TEST_IMAGES_COUNT = None  # Uses all images from test_set_info.json

# ============================================================================


def execute_train_test_split():
    """Main function to execute train/test split."""

    print("="*80)
    print("EXECUTING RANDOM TRAIN/TEST SPLIT")
    print("="*80)

    # Change to script directory
    os.chdir(Path(__file__).parent)

    # Step 1: Load image coordinates
    print("\n[1/7] Loading image metadata...")
    with open(PATHS['pic_coords'], 'r', encoding='utf-8') as f:
        pic_coords = json.load(f)

    # Load image embeddings to get full set of available images
    image_names = np.load(PATHS['image_names'], allow_pickle=True)
    available_images = list(str(name) for name in image_names)

    # Map images to their coordinates
    image_to_coord = {}
    for img_name in available_images:
        coord = pic_coords.get(img_name)
        if coord is not None:
            coord_key = (float(coord[0]), float(coord[1]))
            image_to_coord[img_name] = coord_key

    print(f"  ✓ Found {len(image_to_coord)} images with valid coordinates")

    # Step 2: Load or create test set
    print("\n[2/7] Preparing test set...")
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)

    # Load existing test_set_info.json
    with open(PATHS['test_set_info'], 'r', encoding='utf-8') as f:
        test_set_info = json.load(f)

    # Determine test image names
    if TEST_IMAGES_COUNT is not None:
        # Randomly select TEST_IMAGES_COUNT images
        all_image_names = list(image_to_coord.keys())
        if len(all_image_names) < TEST_IMAGES_COUNT:
            print(f"  ⚠ Warning: Only {len(all_image_names)} images available, using all of them")
            test_image_names = all_image_names
        else:
            test_image_names = random.sample(all_image_names, TEST_IMAGES_COUNT)
        print(f"  ✓ Randomly selected {len(test_image_names)} test images from dataset")
    else:
        # Use images from test_set_info.json
        test_image_names = test_set_info["test_images"]
        print(f"  ✓ Using {len(test_image_names)} test images from test_set_info.json")

    test_image_names_with_ext = {f"{name}" if name.endswith('.jpg') else f"{name}.jpg"
                                 for name in test_image_names}

    # Step 3: Filter dataset.json
    print("\n[3/7] Filtering dataset.json...")
    with open(PATHS['dataset'], 'r', encoding='utf-8') as f:
        dataset = json.load(f)

    original_count = len(dataset)

    # Extract test images and save to test.json (match with .jpg extension)
    dataset_test = {k: v for k, v in dataset.items() if k in test_image_names_with_ext}
    dataset_train = {k: v for k, v in dataset.items() if k not in test_image_names_with_ext}

    # Save test images to metadata/test.json
    with open(PATHS['dataset_test'], 'w', encoding='utf-8') as f:
        json.dump(dataset_test, f, ensure_ascii=False, indent=2)

    # Save filtered dataset (train only)
    with open(PATHS['dataset_train'], 'w', encoding='utf-8') as f:
        json.dump(dataset_train, f, ensure_ascii=False, indent=2)

    print(f"  ✓ Original: {original_count} images")
    print(f"  ✓ Test images: {len(dataset_test)} → {PATHS['dataset_test']}")
    print(f"  ✓ Train: {len(dataset_train)} images → {PATHS['dataset_train']}")

    # Step 4: Build test coordinates set
    print("\n[4/7] Building test coordinates set...")
    test_coords = set()
    for img_name in test_image_names:
        img_name_clean = img_name.split('.jpg')[0] if img_name.endswith('.jpg') else img_name
        if img_name_clean in image_to_coord:
            test_coords.add(image_to_coord[img_name_clean])
        elif img_name in image_to_coord:
            test_coords.add(image_to_coord[img_name])

    print(f"  ✓ Test images map to {len(test_coords)} unique locations")

    # Step 5: Split pivot_signal_table.json
    print("\n[5/7] Splitting pivot_signal_table.json...")
    with open(PATHS['pivot_table'], 'r', encoding='utf-8') as f:
        pivot_data = json.load(f)

    # Extract table data
    rows = []
    table_index = None
    for idx, item in enumerate(pivot_data):
        if isinstance(item, dict) and item.get('type') == 'table' and item.get('name') == 'pivot_signal_table':
            rows = item.get('data', [])
            table_index = idx
            break

    if table_index is None or not rows:
        print("  ✗ Could not find pivot_signal_table!")
        return False

    # Split rows
    train_rows = []
    test_rows = []

    for row in rows:
        lat = float(row.get('lat', 0))
        lon = float(row.get('lon', 0))
        coord = (lat, lon)

        if coord in test_coords:
            test_rows.append(row)
        else:
            train_rows.append(row)

    # Create train pivot table (keep original structure)
    train_pivot = copy.deepcopy(pivot_data)
    train_pivot[table_index]['data'] = train_rows

    # Create test pivot table
    test_pivot = copy.deepcopy(pivot_data)
    test_pivot[table_index]['data'] = test_rows

    # Save both
    with open(PATHS['pivot_table_train'], 'w', encoding='utf-8') as f:
        json.dump(train_pivot, f, ensure_ascii=False, indent=2)

    with open(PATHS['pivot_table_test'], 'w', encoding='utf-8') as f:
        json.dump(test_pivot, f, ensure_ascii=False, indent=2)

    print(f"  ✓ Train rows: {len(train_rows)} → {PATHS['pivot_table_train']}")
    print(f"  ✓ Test rows: {len(test_rows)} → {PATHS['pivot_table_test']}")

    # Step 6: Split text embeddings
    print("\n[6/7] Splitting text embeddings...")
    text_embedding = np.load(PATHS['text_embeddings'])
    text_embedding_image_names = np.load(PATHS['text_embeddings_image_names'])

    # Clean test image names for comparison (remove .jpg if present)
    test_image_names_set = set()
    for name in test_image_names:
        clean_name = name.split('.jpg')[0] if name.endswith('.jpg') else name
        test_image_names_set.add(clean_name)

    text_embedding_test = []
    text_embedding_train = []
    image_names_train = []

    for idx, image_name in enumerate(text_embedding_image_names):
        # Clean image name for comparison
        clean_image_name = image_name.split('.jpg')[0] if isinstance(image_name, str) and image_name.endswith('.jpg') else image_name

        if clean_image_name in test_image_names_set:
            text_embedding_test.append(text_embedding[idx])
        else:
            text_embedding_train.append(text_embedding[idx])
            image_names_train.append(image_name)

    # Convert to numpy arrays
    text_embedding_train = np.array(text_embedding_train)
    text_embedding_test = np.array(text_embedding_test)
    image_names_train = np.array(image_names_train)

    # Save
    np.save(PATHS['text_embeddings_train'], text_embedding_train)
    np.save(PATHS['text_embeddings_test'], text_embedding_test)
    np.save(PATHS['text_names_train'], image_names_train)

    print(f"  ✓ Train text embeddings: {len(text_embedding_train)} → {PATHS['text_embeddings_train']}")
    print(f"  ✓ Test text embeddings: {len(text_embedding_test)} → {PATHS['text_embeddings_test']}")
    print(f"  ✓ Train image names: {len(image_names_train)} → {PATHS['text_names_train']}")

    # Step 7: Update test_set_info.json with locations
    print("\n[7/7] Updating test_set_info.json with locations...")

    # Fill in test_locations from test_images
    test_locations = []
    for image_name in test_image_names:
        # Clean image name
        clean_name = image_name.split('.jpg')[0] if image_name.endswith('.jpg') else image_name

        # Look up in pic_coords
        if clean_name in pic_coords:
            test_locations.append(pic_coords[clean_name])
        elif image_name in pic_coords:
            test_locations.append(pic_coords[image_name])
        else:
            print(f"  ⚠ Warning: Image ID {image_name} not found in pic_coords.json")

    # Save test set info with all information
    test_set_info = {
        'test_images': sorted(test_image_names),
        'test_count': len(test_image_names),
        'test_locations': sorted(test_locations),
        'location_count': len(test_coords),
        'pivot_train_count': len(train_rows),
        'pivot_test_count': len(test_rows),
        'dataset_train_count': len(dataset_train),
        'dataset_test_count': len(dataset_test),
        'text_train_count': len(text_embedding_train),
        'text_test_count': len(text_embedding_test)
    }

    with open(PATHS['test_set_info_output'], 'w', encoding='utf-8') as f:
        json.dump(test_set_info, f, indent=2, ensure_ascii=False)

    print(f"  ✓ Successfully filled in {len(test_locations)} test locations")
    print(f"  ✓ Saved: {PATHS['test_set_info_output']}")

    print("\n" + "="*80)
    print("✓ RANDOM TRAIN/TEST SPLIT COMPLETE")
    print("="*80)
    print(f"\nSummary:")
    print(f"  • Test images: {len(test_image_names)} across {len(test_coords)} unique locations")
    print(f"  • Dataset: {original_count} → train={len(dataset_train)}, test={len(dataset_test)}")
    print(f"  • Pivot table: train={len(train_rows)}, test={len(test_rows)}")
    print(f"  • Text embeddings: train={len(text_embedding_train)}, test={len(text_embedding_test)}")
    print(f"\nFiles created/modified:")
    for key, path in PATHS.items():
        if 'output' in key or 'train' in key or 'test' in key:
            print(f"  • {path}")
    print(f"\nNext: Run main.py to evaluate all localization methods")

    return True


if __name__ == "__main__":
    success = execute_train_test_split()
    exit(0 if success else 1)