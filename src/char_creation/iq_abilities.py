from dataclasses import dataclass, asdict
from typing import List, Tuple
import json


@dataclass
class IQAbility:
    Max_Additional_Languages: int
    Immune_to_Illusion: int
    Max_Mage_Spell_Level: int


# Define abilities corresponding to IQ ranges
iq_abilities: List[Tuple[range, IQAbility]] = [
    (range(1, 8), IQAbility(0, 0, 0)),  # IQ 1-7
    (range(8, 9), IQAbility(1, 0, 0)),  # IQ 8
    (range(9, 10), IQAbility(1, 0, 4)), # IQ 9
    (range(10, 12), IQAbility(2, 0, 5)), # IQ 10-11
    (range(12, 14), IQAbility(3, 0, 6)), # IQ 12-13
    (range(14, 16), IQAbility(4, 0, 7)), # IQ 14-15
    (range(16, 17), IQAbility(5, 0, 8)), # IQ 16
    (range(17, 18), IQAbility(6, 0, 8)), # IQ 17
    (range(18, 19), IQAbility(7, 0, 9)), # IQ 18
    (range(19, 20), IQAbility(7, 1, 9)), # IQ 19
    (range(20, 21), IQAbility(7, 2, 9)), # IQ 20
    (range(21, 22), IQAbility(7, 3, 9)), # IQ 21
    (range(22, 23), IQAbility(7, 4, 9)), # IQ 22
    (range(23, 24), IQAbility(7, 5, 9)), # IQ 23
    (range(24, 25), IQAbility(7, 6, 9)), # IQ 24
    (range(25, 26), IQAbility(7, 7, 9)), # IQ 25
]


def get_iq_ability(iq_val: int, ability: str) -> int:
    """
    Get the appropriate ability for a given IQ value.

    Args:
        iq_val (int): The IQ value (1-25).
        ability (str): The ability to retrieve (e.g., 'Max_Additional_Languages').

    Returns:
        int: The ability value.
    """
    for iq_range, iq_ability in iq_abilities:
        if iq_val in iq_range:
            return getattr(iq_ability, ability)
    raise ValueError(f"Invalid IQ value: {iq_val}")


def serialize_iq_abilities_to_json(output_file: str):
    """
    Serialize IQ abilities to JSON format.

    Args:
        output_file (str): Path to save the JSON file.
    """
    # Convert ranges to lists for JSON serialization
    abilities_json = [
        {"range": list(iq_range), **asdict(iq_ability)}
        for iq_range, iq_ability in iq_abilities
    ]

    # Save to JSON file
    with open(output_file, "w") as file:
        json.dump(abilities_json, file, indent=4)
    print(f"Serialized IQ abilities to {output_file}")


# Example Usage
if __name__ == "__main__":
    # Retrieve a specific IQ ability
    iq_val = 16
    ability = "Max_Mage_Spell_Level"
    value = get_iq_ability(iq_val, ability)
    print(f"IQ {iq_val} - {ability}: {value}")

    # Serialize abilities to JSON
    output_file = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/character_creation/iq_abilities.json"
    serialize_iq_abilities_to_json(output_file)
