import json
from typing import List, Dict

def load_spells(file_path: str) -> List[Dict]:
    """
    Load spells from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict]: A list of spells.
    """
    with open(file_path, "r") as file:
        return json.load(file)

# Example usage
cleric_spells = load_spells("data/adventures_dark_deep/rules/spells/cleric_spells.json")
print("Cleric Spells:", cleric_spells)
