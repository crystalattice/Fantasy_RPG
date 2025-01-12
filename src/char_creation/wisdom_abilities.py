from dataclasses import dataclass, asdict
from typing import List, Tuple
import json


@dataclass
class WisdomAbility:
    Magical_Attack_Adjustment: int
    Cleric_Bonus: str
    Spell_Failure: int
    Immune_to_Charm: int


# Define abilities corresponding to wisdom values
wisdom_abilities: List[Tuple[range, WisdomAbility]] = [
    (range(1, 9), WisdomAbility(-1, "0", 100, 0)),  # Wisdom 1-8
    (range(9, 10), WisdomAbility(0, "0", 20, 0)),  # Wisdom 9
    (range(10, 13), WisdomAbility(0, "0", 15, 0)),  # Wisdom 10-12
    (range(13, 14), WisdomAbility(0, "1x1", 0, 0)),  # Wisdom 13
    (range(14, 15), WisdomAbility(0, "2x1", 0, 0)),  # Wisdom 14
    (range(15, 16), WisdomAbility(1, "2x1, 1x2", 0, 0)),  # Wisdom 15
    (range(16, 17), WisdomAbility(2, "2x1, 2x2", 0, 0)),  # Wisdom 16
    (range(17, 18), WisdomAbility(3, "2x1, 2x2, 1x3", 0, 0)),  # Wisdom 17
    (range(18, 19), WisdomAbility(4, "2x1, 2x2, 1x3, 1x4", 0, 0)),  # Wisdom 18
    (range(19, 20), WisdomAbility(4, "3x1, 2x2, 1x3, 2x4", 0, 1)),  # Wisdom 19
    (range(20, 21), WisdomAbility(4, "3x1, 3x2, 1x3, 3x4", 0, 2)),  # Wisdom 20
    (range(21, 22), WisdomAbility(4, "3x1, 3x2, 2x3, 3x4, 1x5", 0, 3)),  # Wisdom 21
    (range(22, 23), WisdomAbility(4, "3x1, 3x2, 2x3, 4x4, 2x5", 0, 4)),  # Wisdom 22
    (range(23, 24), WisdomAbility(4, "3x1, 3x2, 2x3, 4x4, 4x5", 0, 5)),  # Wisdom 23
    (range(24, 25), WisdomAbility(4, "3x1, 3x2, 2x3, 4x4, 4x5, 2x6", 0, 6)),  # Wisdom 24
    (range(25, 26), WisdomAbility(4, "3x1, 3x2, 2x3, 4x4, 4x5, 3x6, 1x7", 0, 7)),  # Wisdom 25
]


def get_wisdom_ability(wis_val: int, ability: str) -> int:
    """
    Get the appropriate ability for a given wisdom value.

    Args:
        wis_val (int): The wisdom value (1-25).
        ability (str): The ability to retrieve (e.g., 'Magical_Attack_Adjustment').

    Returns:
        int: The ability value.
    """
    for wis_range, wis_ability in wisdom_abilities:
        if wis_val in wis_range:
            return getattr(wis_ability, ability)
    raise ValueError(f"Invalid wisdom value: {wis_val}")


def serialize_wisdom_abilities_to_json(output_file: str):
    """
    Serialize wisdom abilities to JSON format.

    Args:
        output_file (str): Path to save the JSON file.
    """
    # Convert ranges to lists for JSON serialization
    abilities_json = [
        {"range": list(wis_range), **asdict(wis_ability)}
        for wis_range, wis_ability in wisdom_abilities
    ]

    # Save to JSON file
    with open(output_file, "w") as file:
        json.dump(abilities_json, file, indent=4)
    print(f"Serialized wisdom abilities to {output_file}")


# Example Usage
if __name__ == "__main__":
    # Retrieve a specific wisdom ability
    wis_val = 16
    ability = "Magical_Attack_Adjustment"
    value = get_wisdom_ability(wis_val, ability)
    print(f"Wisdom {wis_val} - {ability}: {value}")

    # Serialize abilities to JSON
    output_file = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/character_creation/wisdom_abilities.json"
    serialize_wisdom_abilities_to_json(output_file)
