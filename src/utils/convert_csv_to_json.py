import json

import pandas as pd
import os

def convert_csv_to_json(input_path, output_path):
    # Read the CSV file
    data = pd.read_csv(input_path)
    # Convert to JSON format
    data_json = data.to_dict(orient="records")
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    # Save to a JSON file
    with open(output_path, "w") as json_file:
        json.dump(data_json, json_file, indent=4)
    print(f"Converted {len(data_json)} records from {input_path} to {output_path}")

# Paths to your CSV files
melee_weapons_path = "/home/codyjackson/PycharmProjects/RPGs/Archived/Databases/melee_weapons.csv"
ranged_weapons_path = "/home/codyjackson/PycharmProjects/RPGs/Archived/Databases/ranged_weapons.csv"

# Output paths for JSON files
output_melee_json = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/equipment/melee_weapons.json"
output_ranged_json = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/equipment/ranged_weapons.json"

if __name__ == '__main__':
    # Convert the files
    convert_csv_to_json(melee_weapons_path, output_melee_json)
    convert_csv_to_json(ranged_weapons_path, output_ranged_json)
