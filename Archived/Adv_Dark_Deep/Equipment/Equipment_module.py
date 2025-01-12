import json
from typing import List, Dict, Optional

# Example JSON schema for equipment
EQUIPMENT_DATA = {
    "weapons": [
        {
            "name": "Longsword",
            "type": "melee",
            "cost": 15,
            "weight": 4,
            "damage": "1d8",
            "speed": 5
        },
        {
            "name": "Shortbow",
            "type": "ranged",
            "cost": 25,
            "weight": 2,
            "damage": "1d6",
            "speed": 7
        }
    ],
    "armor": [
        {
            "name": "Chainmail",
            "type": "medium",
            "cost": 75,
            "weight": 40,
            "AC_bonus": 5
        }
    ]
}

# Equipment module functionality
def list_items(category: str) -> List[Dict]:
    """
    List items from a specific category (e.g., weapons, armor).

    Args:
        category (str): The category of items to list (e.g., "weapons", "armor").

    Returns:
        List[Dict]: A list of items in the specified category.
    """
    return EQUIPMENT_DATA.get(category, [])

def find_item_by_name(category: str, name: str) -> Optional[Dict]:
    """
    Find an item by name within a specific category.

    Args:
        category (str): The category to search within.
        name (str): The name of the item to find.

    Returns:
        Optional[Dict]: The item if found, else None.
    """
    items = EQUIPMENT_DATA.get(category, [])
    for item in items:
        if item["name"].lower() == name.lower():
            return item
    return None

def add_item(category: str, item: Dict) -> None:
    """
    Add a new item to a specific category. Ensures no duplicate entries based on name.

    Args:
        category (str): The category to add the item to (e.g., "weapons").
        item (Dict): The item data to add.
    """
    if category in EQUIPMENT_DATA:
        existing_items = [i["name"].lower() for i in EQUIPMENT_DATA[category]]
        if item["name"].lower() not in existing_items:
            EQUIPMENT_DATA[category].append(item)
        else:
            print(f"Item '{item['name']}' already exists in category '{category}'.")
    else:
        EQUIPMENT_DATA[category] = [item]

def calculate_encumbrance(inventory: List[Dict]) -> int:
    """
    Calculate the total weight of items in an inventory.

    Args:
        inventory (List[Dict]): A list of items in the inventory.

    Returns:
        int: The total weight of the inventory.
    """
    return sum(item.get("weight", 0) for item in inventory)

# Example usage
if __name__ == "__main__":
    # List all weapons
    weapons = list_items("weapons")
    print("Weapons:", weapons)

    # Find a specific item
    longsword = find_item_by_name("weapons", "Longsword")
    print("Found item:", longsword)

    # Add a new item
    new_weapon = {
        "name": "Warhammer",
        "type": "melee",
        "cost": 20,
        "weight": 6,
        "damage": "1d8",
        "speed": 7
    }
    add_item("weapons", new_weapon)
    print("Updated weapons:", list_items("weapons"))

    # Attempt to add a duplicate item
    duplicate_weapon = {
        "name": "Longsword",
        "type": "melee",
        "cost": 15,
        "weight": 4,
        "damage": "1d8",
        "speed": 5
    }
    add_item("weapons", duplicate_weapon)

    # Calculate encumbrance
    inventory = [
        {"name": "Longsword", "weight": 4},
        {"name": "Chainmail", "weight": 40}
    ]
    total_weight = calculate_encumbrance(inventory)
    print("Total Encumbrance:", total_weight)
