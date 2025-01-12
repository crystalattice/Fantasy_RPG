from dataclasses import dataclass, asdict
from typing import List, Tuple
import json


@dataclass
class DexterityAbility:
    Init_Adj: int
    Missile_Attack: int
    AC_Adj: int


# Define abilities corresponding to dexterity ranges
dex_abilities: List[Tuple[range, DexterityAbility]] = [
    (range(1, 2), DexterityAbility(5, -5, 6)),    # Dex 1
    (range(2, 3), DexterityAbility(4, -4, 5)),    # Dex 2
    (range(3, 4), DexterityAbility(3, -3, 4)),    # Dex 3
    (range(4, 5), DexterityAbility(2, -2, 3)),    # Dex 4
    (range(5, 6), DexterityAbility(1, -1, 2)),    # Dex 5
    (range(6, 7), DexterityAbility(0, 0, 1)),     # Dex 6
    (range(7, 15), DexterityAbility(0, 0, 0)),    # Dex 7-14
    (range(15, 16), DexterityAbility(0, 0, -1)),  # Dex 15
    (range(16, 17), DexterityAbility(-1, 1, -2)), # Dex 16
    (range(17, 18), DexterityAbility(-2, 2, -3)), # Dex 17
    (range(18, 21), DexterityAbility(-3, 3, -4)), # Dex 18-20
    (range(21, 24), DexterityAbility(-4, 4, -5)), # Dex 21-23
    (range(24, 26), DexterityAbility(-5, 5, -6)), # Dex 24-25
]


def get_dex_ability(dex_value: int, ability: str) -> int:
    """
    Get the appropriate ability for a given dexterity value.

    Args:
        dex_value (int): The dexterity value (1-25).
        ability (str): The ability to retrieve (e.g., 'Init_Adj').

    Returns:
        int: The ability value.
    """
    for dex_range, dex_ability in dex_abilities:
        if dex_value in dex_range:
            return getattr(dex_ability, ability)
    raise ValueError(f"Invalid dexterity value: {dex_value}")


def serialize_dex_abilities_to_json(output_file: str):
    """
    Serialize dexterity abilities to JSON format.

    Args:
        output_file (str): Path to save the JSON file.
    """
    # Convert ranges to lists for JSON serialization
    abilities_json = [
        {"range": list(dex_range), **asdict(dex_ability)}
        for dex_range, dex_ability in dex_abilities
    ]

    # Save to JSON file
    with open(output_file, "w") as file:
        json.dump(abilities_json, file, indent=4)
    print(f"Serialized dexterity abilities to {output_file}")


# Example Usage
if __name__ == "__main__":
    # Retrieve a specific dexterity ability
    dex_value = 16
    ability = "AC_Adj"
    value = get_dex_ability(dex_value, ability)
    print(f"Dexterity {dex_value} - {ability}: {value}")

    # Serialize abilities to JSON
    output_file = "/data/adventures_dark_deep/character_creation/dex_abilities.json"
    serialize_dex_abilities_to_json(output_file)
