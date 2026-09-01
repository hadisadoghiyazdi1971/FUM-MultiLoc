import json


def extract_object_names(input_file: str, output_file: str):
    """
    استخراج object_name با تمایز صریح بین
    location_identifiers و reference_objects
    """

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = {}

    for image_name, image_data in data.items():
        object_names = []

        pos = image_data.get("position_analysis", {})

        # ---------- Location Identifiers ----------
        for obj in pos.get("location_identifiers", []):
            # مثال: ID::AB-413
            object_names.append(f"ID::{obj}")

        # ---------- Reference Objects ----------
        for obj in pos.get("reference_objects", []):
            if (
                obj.get("suitability_for_distance_estimation") == "بله"
                and "object_name" in obj
            ):
                obj_type = obj.get("object_type", "UNKNOWN")
                obj_name = obj["object_name"]

                # مثال: REF::wall::دیوار
                object_names.append(f"REF::{obj_type}::{obj_name}")

        result[image_name] = object_names

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ داده‌ها در {output_file} ذخیره شد")
    return result


input_filename = "../metadata/image_descriptions.json"
output_filename = "../metadata/dataset.json"
output = extract_object_names(input_filename, output_filename)

