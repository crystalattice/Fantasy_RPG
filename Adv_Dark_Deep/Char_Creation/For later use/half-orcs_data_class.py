from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class HalfOrc:
    """Class representing the Half-Orc race with its characteristics."""
    subrace: str
    ability_scores: Dict[str, Dict[str, Tuple[int, int]]]
    infravision_range: int = 60
    languages: List[str] = field(default_factory=list)
    additional_languages_limit: int = 2
    height_table: List[Tuple[int, int, int]] = field(default_factory=list)
    weight_table: List[Tuple[int, int, int]] = field(default_factory=list)
    age_ranges: Dict[str, Tuple[int, int]] = field(default_factory=dict)
    level_limits: Dict[str, Dict[int, int]] = field(default_factory=dict)
    special_abilities: List[str] = field(default_factory=list)

# Data for Half-Orcs
half_orc = HalfOrc(
    subrace="Half-Orc",
    ability_scores={
        "Male": {
            "Strength": (6, 18),
            "Intelligence": (3, 17),
            "Wisdom": (3, 14),
            "Dexterity": (3, 17),
            "Constitution": (13, 19),
            "Charisma": (3, 12),
        },
        "Female": {
            "Strength": (6, 18),
            "Intelligence": (3, 17),
            "Wisdom": (3, 14),
            "Dexterity": (3, 17),
            "Constitution": (13, 19),
            "Charisma": (3, 12),
        }
    },
    languages=["Common", "Orcish"],
    height_table=[
        (1, 45, 66 - 1),  # 66 - 1d4
        (46, 55, 66 - 1),  # 66 - 1d4
        (56, 65, 66),
        (66, 75, 66 + 1),  # 66 + 1d4
        (76, 100, 66 + 4),  # 66 + 1d8
    ],
    weight_table=[
        (1, 30, 150 - 8),  # 150 - 2d8
        (31, 38, 150 - 1),  # 150 - 1d8
        (39, 47, 150),
        (48, 55, 150 + 1),  # 150 + 1d8
        (56, 100, 150 + 40),  # 150 + 4d10
    ],
    age_ranges={
        "Young Adult": (12, 15),
        "Mature": (16, 30),
        "Middle Age": (31, 45),
        "Old": (46, 60),
        "Very Old": (61, 80),
    },
    level_limits={
        "Cleric": {14: 4, 15: 5, 16: 6, 17: 7, 18: 7, 19: 7, 21: 7},
        "Fighter": {14: 10, 18: 10, 19: 12, 21: 17},
        "Thief": {14: 8, 16: 10, 17: 11},
        "Mountebank": {14: 4, 16: 6, 18: 7},
    },
    special_abilities=[
        "Infravision up to 60 feet",
        "Penalties of -2 to Charisma, +1 to Strength, and +1 to Constitution",
        "Can learn up to 2 additional languages if intelligence score allows"
    ]
)

if __name__ == "__main__":
    # Example code to test the logic
    print("Half-Orc:", half_orc)
