import json
import sys

def append_to_json(key, value):
    file_path = "gateway.json"
    try:
        # Load existing JSON data or initialize an empty dictionary
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        # Append or update the value for the given key
        data[key] = value

        # Write the updated data back to the JSON file
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Appended {key}: {value} to {file_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python append_to_json.py <file_path> <key> <value>")
        sys.exit(1)

    key = sys.argv[1]
    value = sys.argv[2]

    append_to_json(key, value)
