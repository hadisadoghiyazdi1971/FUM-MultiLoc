import json
from collections import defaultdict


def build_object_location_map(
    objects_file: str,
    locations_file: str,
    output_file: str
):
    """
    Converts image-based object annotations into
    object-based location lists.

    Args:
        objects_file: path to image -> [objects]
        locations_file: path to image -> [lat, lon]
        output_file: path to save object -> [[lat, lon], ...]
    """

    # Load data
    with open(objects_file, "r", encoding="utf-8") as f:
        image_objects = json.load(f)

    with open(locations_file, "r", encoding="utf-8") as f:
        image_locations = json.load(f)

    object_locations = defaultdict(list)

    for image_name, objects in image_objects.items():
        img_id = image_name.replace('.jpg', '')
        if img_id not in image_locations:
            # Skip images without location info
            continue

        lat_lon = image_locations[img_id]

        for obj in objects:
            object_locations[obj].append(lat_lon)

    # Save result
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(object_locations, f, ensure_ascii=False, indent=2)

    print(f"✅ Saved object-location map to {output_file}")


if __name__ == "__main__":
    build_object_location_map(
        objects_file="../metadata/dataset.json",
        locations_file="../metadata/pic_coords.json",
        output_file="../metadata/object_locations.json"
    )
