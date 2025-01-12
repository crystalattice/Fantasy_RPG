from dataclasses import dataclass, asdict
from typing import List, Tuple, Union, Dict
from enum import IntEnum
import json


@dataclass
class StrengthAbility:
    to_hit: int
    damage: int
    weight: int
    open_stuck_doors: float
    open_locked_doors: float
    bend_bars_lift_gates: int


class StrengthModifier(IntEnum):
    """
    Enum for indexing the various ability modifiers related to strength.
    """
    TO_HIT = 0
    DAMAGE = 1
    WEIGHT = 2
    OPEN_STUCK_DOORS = 3
    OPEN_LOCKED_DOORS = 4
    BEND_BARS_LIFT_GATES = 5


# Define abilities corresponding to strength ranges and exceptional values
strength_abilities: Dict[Union[int, str], StrengthAbility] = {
    1: StrengthAbility(-5, -2, -55, 0.0, 0.0, 0),
    2: StrengthAbility(-4, -2, -45, 0.0, 0.0, 0),
    3: StrengthAbility(-3, -1, -35, 0.17, 0.0, 0),
    4: StrengthAbility(-2, -1, -25, 0.17, 0.0, 0),
    5: StrengthAbility(-2, -1, -25, 0.17, 0.0, 0),
    6: StrengthAbility(-1, 0, -15, 0.17, 0.0, 0),
    7: StrengthAbility(-1, 0, -15, 0.17, 0.0, 0),
    8: StrengthAbility(0, 0, 0, 0.33, 0.0, 1),
    9: StrengthAbility(0, 0, 0, 0.33, 0.0, 1),
    10: StrengthAbility(0, 0, 0, 0.33, 0.0, 2),
    11: StrengthAbility(0, 0, 0, 0.33, 0.0, 2),
    12: StrengthAbility(0, 0, 10, 0.33, 0.0, 4),
    13: StrengthAbility(0, 0, 10, 0.33, 0.0, 4),
    14: StrengthAbility(0, 0, 20, 0.33, 0.0, 7),
    15: StrengthAbility(0, 0, 20, 0.33, 0.0, 7),
    16: StrengthAbility(0, 1, 35, 0.5, 0.0, 10),
    17: StrengthAbility(1, 1, 50, 0.5, 0.0, 13),
    18: StrengthAbility(1, 2, 75, 0.5, 0.0, 16),
    "18/01-50": StrengthAbility(1, 3, 100, 0.5, 0.0, 20),
    "18/51-75": StrengthAbility(2, 3, 125, 0.67, 0.0, 25),
    "18/76-90": StrengthAbility(2, 4, 150, 0.67, 0.0, 30),
    "18/91-99": StrengthAbility(2, 5, 200, 0.67, 0.17, 35),
    "18/00": StrengthAbility(3, 6, 300, 0.83, 0.33, 40),
    19: StrengthAbility(3, 7, 450, 0.875, 0.5, 50),
    20: StrengthAbility(3, 8, 500, 0.875, 0.5, 60),
    21: StrengthAbility(4, 9, 600, 0.9, 0.67, 70),
    22: StrengthAbility(4, 10, 750, 0.9, 0.67, 80),
    23: StrengthAbility(5, 11, 900, 0.917, 0.83, 90),
    24: StrengthAbility(6, 12, 1200, 0.917, 0.875, 100),
    25: StrengthAbility(7, 14, 1500, 0.958, 0.9, 100),
}


def get_strength_ability(str_val: Union[int, str], ability: StrengthModifier) -> Union[int, float]:
    """
    Retrieve the specific ability modifier for a given strength score.

    Args:
        str_val (int | str): The strength score, either integer (1-25) or exceptional (e.g., "18/01-50").
        ability (StrengthModifier): The specific ability modifier to retrieve.

    Returns:
        int | float: The value of the requested ability modifier for the given strength score.
    """
    if str_val in strength_abilities:
        return getattr(strength_abilities[str_val], ability.name.lower())
    raise ValueError(f"Invalid strength value: {str_val}")


def serialize_strength_abilities_to_json(output_file: str):
    """
    Serialize strength abilities to JSON format.

    Args:
        output_file (str): Path to save the JSON file.
    """
    abilities_json = {
        str(key): asdict(value) for key, value in strength_abilities.items()
    }

    # Save to JSON file
    with open(output_file, "w") as file:
        json.dump(abilities_json, file, indent=4)
    print(f"Serialized strength abilities to {output_file}")


# Example Usage
if __name__ == "__main__":
    # Retrieve a specific strength ability
    strength_value = "18/51-75"
    modifier_type = StrengthModifier.WEIGHT
    result = get_strength_ability(str_val=strength_value, ability=modifier_type)
    print(f"Strength {strength_value}: {modifier_type.name} = {result}")

    # Serialize abilities to JSON
    output_file = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/character_creation/strength_abilities.json"
    serialize_strength_abilities_to_json(output_file)
