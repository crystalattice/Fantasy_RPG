from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class Human:
    """Class representing the Human race with its characteristics."""
    subrace: str = "Human"
    ability_scores: Dict[str, Tuple[int, int]] = field(default_factory=dict)
    height_table: List[Tuple[int, int, int]] = field(default_factory=list)
    weight_table: List[Tuple[int, int, int]] = field(default_factory=list)
    age_ranges: Dict[str, Tuple[int, int]] = field(default_factory=dict)
    special_abilities: List[str] = field(default_factory=list)

# Data for Humans
human = Human(
    ability_scores={
        "Strength": (3, 18),
        "Intelligence": (3, 18),
        "Wisdom": (3, 18),
        "Dexterity": (3, 18),
        "Constitution": (3, 18),
        "Charisma": (3, 18),
    },
    height_table=[
        (1, 20, 72 - 12),  # 72 - 1d12
        (21, 40, 72 - 1),  # 72 - 1d4
        (41, 60, 72),
        (61, 80, 72 + 1),  # 72 + 1d4
        (81, 100, 72 + 12),  # 72 + 1d12
    ],
    weight_table=[
        (1, 25, 175 - 36),  # 175 - 3d12
        (26, 40, 175 - 1),  # 175 - 1d8
        (41, 60, 175),
        (61, 75, 175 + 1),  # 175 + 1d8
        (76, 100, 175 + 60),  # 175 + 5d12
    ],
    age_ranges={
        "Young Adult": (14, 20),
        "Mature": (21, 40),
        "Middle Age": (41, 60),
        "Old": (61, 90),
        "Very Old": (91, 120),
    },
    special_abilities=[
        "Humans have no bonuses or penalties to their ability scores.",
        "Humans do not receive any special racial powers or skills.",
        "Humans can rise to any level in any character class.",
        "Humans cannot multi-class but can change class once in their career."
    ]
)

if __name__ == "__main__":
    # Example code to test the logic
    print("Human:", human)
