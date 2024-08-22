from collections import namedtuple
from typing import Type, Dict
from enum import IntEnum

# Define the namedtuple for strength attributes
Strength: Type[namedtuple] = namedtuple("Strength",
                                        ["to_hit", "damage", "weight", "open_stuck_doors", "open_locked_doors",
                                         "bend_bars_lift_gates"])


class StrengthModifier(IntEnum):
    """
    Enum for indexing the various ability modifiers related to strength.

    Attributes:
        TO_HIT: Index for the "to hit" modifier.
        DAMAGE: Index for the damage modifier.
        WEIGHT: Index for the weight allowance.
        OPEN_STUCK_DOORS: Index for the ability to open stuck doors.
        OPEN_LOCKED_DOORS: Index for the ability to open locked doors.
        BEND_BARS_LIFT_GATES: Index for the ability to bend bars or lift gates.
    """
    TO_HIT = 0
    DAMAGE = 1
    WEIGHT = 2
    OPEN_STUCK_DOORS = 3
    OPEN_LOCKED_DOORS = 4
    BEND_BARS_LIFT_GATES = 5


# Define the strength scores using namedtuple
strength_abilities: Dict[int | str, Strength] = {
    1: Strength(-5, -2, -55, 0.0, 0.0, 0),
    2: Strength(-4, -2, -45, 0.0, 0.0, 0),
    3: Strength(-3, -1, -35, 0.17, 0.0, 0),
    4: Strength(-2, -1, -25, 0.17, 0.0, 0),
    5: Strength(-2, -1, -25, 0.17, 0.0, 0),
    6: Strength(-1, 0, -15, 0.17, 0.0, 0),
    7: Strength(-1, 0, -15, 0.17, 0.0, 0),
    8: Strength(0, 0, 0, 0.33, 0.0, 1),
    9: Strength(0, 0, 0, 0.33, 0.0, 1),
    10: Strength(0, 0, 0, 0.33, 0.0, 2),
    11: Strength(0, 0, 0, 0.33, 0.0, 2),
    12: Strength(0, 0, 10, 0.33, 0.0, 4),
    13: Strength(0, 0, 10, 0.33, 0.0, 4),
    14: Strength(0, 0, 20, 0.33, 0.0, 7),
    15: Strength(0, 0, 20, 0.33, 0.0, 7),
    16: Strength(0, 1, 35, 0.5, 0.0, 10),
    17: Strength(1, 1, 50, 0.5, 0.0, 13),
    18: Strength(1, 2, 75, 0.5, 0.0, 16),
    "18/01-50": Strength(1, 3, 100, 0.5, 0.0, 20),
    "18/51-75": Strength(2, 3, 125, 0.67, 0.0, 25),
    "18/76-90": Strength(2, 4, 150, 0.67, 0.0, 30),
    "18/91-99": Strength(2, 5, 200, 0.67, 0.17, 35),
    "18/00": Strength(3, 6, 300, 0.83, 0.33, 40),
    19: Strength(3, 7, 450, 0.875, 0.5, 50),
    20: Strength(3, 8, 500, 0.875, 0.5, 60),
    21: Strength(4, 9, 600, 0.9, 0.67, 70),
    22: Strength(4, 10, 750, 0.9, 0.67, 80),
    23: Strength(5, 11, 900, 0.917, 0.83, 90),
    24: Strength(6, 12, 1200, 0.917, 0.875, 100),
    25: Strength(7, 14, 1500, 0.958, 0.9, 100),
}


def get_strength_ability(str_val: int | str, ability: StrengthModifier) -> int | float:
    """
    Retrieve the specific ability modifier for a given strength score.

    Args:
        str_val (int | str): The strength score of the character, which can be an integer (1-25)
                             or a string (e.g., "18/01-50") for exceptional strength values.
        ability (StrengthModifier): The specific ability modifier to retrieve (e.g., TO_HIT, DAMAGE).

    Returns:
        int | float: The value of the requested ability modifier for the given strength score.

    Raises:
        ValueError: If the provided strength value is not valid.

    Example:
        >>> get_strength_ability(18, StrengthModifier.DAMAGE)
        2
        >>> get_strength_ability("18/01-50", StrengthModifier.WEIGHT)
        100
    """
    if isinstance(str_val, int) and 1 <= str_val <= 25:
        return strength_abilities[str_val][ability]
    elif isinstance(str_val, str) and str_val in strength_abilities:
        return strength_abilities[str_val][ability]
    else:
        raise ValueError(f"Invalid strength value: {str_val}")


# Example usage
if __name__ == "__main__":
    strength_value = 18
    modifier_type = StrengthModifier.DAMAGE
    result = get_strength_ability(str_val=strength_value, ability=modifier_type)
    print(f"Strength {strength_value}: {modifier_type.name} = {result}")
