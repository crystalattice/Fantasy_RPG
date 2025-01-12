from dataclasses import dataclass, asdict
from typing import List, Tuple
import json


@dataclass
class ConstitutionAbility:
    HP_Bonus: int
    Fighter_HP_Bonus: int
    Reroll_HD: str
    System_Shock: int
    Resurrection: int


# Define abilities corresponding to constitution ranges
constitution_abilities: List[Tuple[range, ConstitutionAbility]] = [
    (range(1, 2), ConstitutionAbility(-4, 0, "5, 6, 7, 8, 9, 10", 25, 30)),
    (range(2, 3), ConstitutionAbility(-3, 0, "6, 7, 8, 9, 10", 30, 35)),
    (range(3, 4), ConstitutionAbility(-2, 0, "", 35, 40)),
    (range(4, 7), ConstitutionAbility(-1, 0, "", 40, 55)),  # Constitution 4-6
    (range(7, 15), ConstitutionAbility(0, 0, "", 55, 85)),  # Constitution 7-14
    (range(15, 16), ConstitutionAbility(1, 1, "", 88, 92)),
    (range(16, 17), ConstitutionAbility(2, 2, "", 91, 94)),
    (range(17, 18), ConstitutionAbility(2, 3, "", 97, 98)),
    (range(18, 19), ConstitutionAbility(2, 4, "", 99, 100)),
    (range(19, 20), ConstitutionAbility(2, 5, "1", 99, 100)),
    (range(20, 21), ConstitutionAbility(2, 6, "1, 2", 99, 100)),
    (range(21, 23), ConstitutionAbility(2, 6, "1, 2, 3", 99, 100)),  # Constitution 21-22
    (range(23, 26), ConstitutionAbility(2, 7, "1, 2, 3", 99, 100)),  # Constitution 23-25
]


def get_constitution_ability(con_val: int, ability: str) -> int:
    """
    Get the appropriate ability for a given constitution value.

    Args:
        con_val (int): The constitution value (1-25).
        ability (str): The ability to retrieve (e.g., 'HP_Bonus').

    Returns:
        int: The ability value.
    """
    for con_range, con_ability in constitution_abilities:
        if con_val in con_range:
            return getattr(con_ability, ability)
    raise ValueError(f"Invalid constitution value: {con_val}")


def serialize_constitution_abilities_to_json(output_file: str):
    """
    Serialize constitution abilities to JSON format.

    Args:
        output_file (str): Path to save the JSON file.
    """
    # Convert ranges to lists for JSON serialization
    abilities_json = [
        {"range": list(con_range), **asdict(con_ability)}
        for con_range, con_ability in constitution_abilities
    ]

    # Save to JSON file
    with open(output_file, "w") as file:
        json.dump(abilities_json, file, indent=4)
    print(f"Serialized constitution abilities to {output_file}")


# Example Usage
if __name__ == "__main__":
    # Retrieve a specific constitution ability
    con_val = 16
    ability = "System_Shock"
    value = get_constitution_ability(con_val, ability)
    print(f"Constitution {con_val} - {ability}: {value}")

    # Serialize abilities to JSON
    output_file = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/character_creation/constitution_abilities.json"
    serialize_constitution_abilities_to_json(output_file)
