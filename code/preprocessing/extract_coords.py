import json


def transform_json(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Find the table data with "tags_pic" name
    result = {}

    for item in data:
        if item.get("type") == "table" and item.get("name") == "tags_pic":
            table_data = item.get("data", [])

            # Process each record
            for record in table_data:
                try:
                    # Get id, lat, and lon
                    record_id = int(record.get("id"))
                    lat = float(record.get("lat", 0))
                    lon = float(record.get("lon", 0))

                    # Add to result dictionary
                    result[record_id] = [lat, lon]
                except (ValueError, TypeError) as e:
                    print(f"Warning: Could not process record with id {record.get('id')}: {e}")

    # Write the transformed data to output file
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"Transformation complete. Output saved to {output_file}")
    return result


if __name__ == "__main__":
    # Call the function with your file paths
    transform_json("../metadata/tags_pic.json", "../metadata/pic_coords.json")
