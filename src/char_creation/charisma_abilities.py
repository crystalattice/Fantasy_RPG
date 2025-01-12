from dataclasses import dataclass, asdict
from typing import List, Tuple
import json


@dataclass
class CharismaAbility:
    max_henchmen: int
    morale_adj: int
    react_adj: int


# Define abilities corresponding to charisma ranges
charisma_abilities: List[Tuple[range, CharismaAbility]] = [
    (range(1, 2), CharismaAbility(0, -8, -35)),  # Charisma 1
    (range(2, 3), CharismaAbility(0, -7, -30)),  # Charisma 2
    (range(3, 4), CharismaAbility(1, -6, -25)),  # Charisma 3
    (range(4, 5), CharismaAbility(1, -5, -20)),  # Charisma 4
    (range(5, 6), CharismaAbility(2, -4, -15)),  # Charisma 5
    (range(6, 7), CharismaAbility(2, -3, -10)),  # Charisma 6
    (range(7, 9), CharismaAbility(3, -2, -5)),   # Charisma 7-8
    (range(9, 12), CharismaAbility(4, 0, 0)),    # Charisma 9-11
    (range(12, 13), CharismaAbility(5, 0, 0)),   # Charisma 12
    (range(13, 14), CharismaAbility(5, 0, 5)),   # Charisma 13
    (range(14, 15), CharismaAbility(6, 1, 10)),  # Charisma 14
    (range(15, 16), CharismaAbility(7, 3, 15)),  # Charisma 15
    (range(16, 17), CharismaAbility(8, 4, 25)),  # Charisma 16
    (range(17, 18), CharismaAbility(10, 6, 30)), # Charisma 17
    (range(18, 19), CharismaAbility(15, 8, 35)), # Charisma 18
    (range(19, 20), CharismaAbility(20, 10, 40)),# Charisma 19
    (range(20, 21), CharismaAbility(25, 12, 45)),# Charisma 20
    (range(21, 22), CharismaAbility(30, 14, 50)),# Charisma 21
    (range(22, 23), CharismaAbility(35, 16, 55)),# Charisma 22
    (range(23, 24), CharismaAbility(40, 18, 60)),# Charisma 23
    (range(24, 25), CharismaAbility(45, 20, 65)),# Charisma 24
    (range(25, 26), CharismaAbility(50, 20, 70)),# Charisma 25
]


def get_charisma_ability(char_val: int, ability: str) -> int:
    """
    Get the appropriate ability for a given charisma value.

    Args:
        char_val (int): The charisma value (1-25).
        ability (str): The ability to retrieve (e.g., 'morale_adj').

    Returns:
        int: The ability value.
    """
    for char_range, char_ability in charisma_abilities:
        if char_val in char_range:
            return getattr(char_ability, ability)
    raise ValueError(f"Invalid charisma value: {char_val}")


def serialize_charisma_abilities_to_json(output_file: str):
    """
    Serialize charisma abilities to JSON format.

    Args:
        output_file (str): Path to save the JSON file.
    """
    # Convert ranges to lists for JSON serialization
    abilities_json = [
        {"range": list(char_range), **asdict(char_ability)}
        for char_range, char_ability in charisma_abilities
    ]

    # Save to JSON file
    with open(output_file, "w") as file:
        json.dump(abilities_json, file, indent=4)
    print(f"Serialized charisma abilities to {output_file}")


# Example Usage
if __name__ == "__main__":
    # Retrieve a specific charisma ability
    char_val = 16
    ability = "morale_adj"
    value = get_charisma_ability(char_val, ability)
    print(f"Charisma {char_val} - {ability}: {value}")

    # Serialize abilities to JSON
    output_file = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/character_creation/charisma_abilities.json"
    serialize_charisma_abilities_to_json(output_file)
