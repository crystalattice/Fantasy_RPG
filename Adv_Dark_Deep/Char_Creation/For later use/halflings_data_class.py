from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class Halfling:
    """Class representing the Halfling race with its characteristics."""
    subrace: str
    ability_scores: Dict[str, Dict[str, Tuple[int, int]]]
    saving_throw_bonus: Dict[int, int] = field(default_factory=dict)
    movement_ability: str = ""
    giant_fighting_bonus: int = -4
    languages: List[str] = field(default_factory=list)
    additional_languages_limit: Dict[int, int] = field(default_factory=dict)
    age_ranges: Dict[str, Tuple[int, int]] = field(default_factory=dict)
    height_table: List[Tuple[int, int, int]] = field(default_factory=list)
    weight_table: List[Tuple[int, int, int]] = field(default_factory=list)
    level_limits: Dict[str, Dict[int, int]] = field(default_factory=dict)
    special_abilities: List[str] = field(default_factory=list)

# Data for Halflings
halfling = Halfling(
    subrace="Halfling",
    ability_scores={
        "Male": {
            "Strength": (6, 17),
            "Intelligence": (6, 18),
            "Wisdom": (3, 17),
            "Dexterity": (8, 18),
            "Constitution": (10, 19),
            "Charisma": (3, 18),
        },
        "Female": {
            "Strength": (6, 14),
            "Intelligence": (6, 18),
            "Wisdom": (3, 17),
            "Dexterity": (8, 18),
            "Constitution": (10, 19),
            "Charisma": (3, 18),
        }
    },
    saving_throw_bonus={
        4: 1,
        7: 2,
        11: 3,
        14: 4,
        18: 5
    },
    movement_ability="Move quietly with -2 penalty to enemy surprise rolls if only with other halflings or elves and not wearing metal armor.",
    languages=["Common", "Dwarven", "Elvish", "Gnome", "Goblin", "Halfling", "Orcish"],
    additional_languages_limit={17: 1, 18: 2},
    age_ranges={
        "Young Adult": (22, 33),
        "Mature": (34, 68),
        "Middle Age": (69, 101),
        "Old": (102, 144),
        "Very Old": (145, 199),
    },
    height_table=[
        (1, 34, 36 - 1),  # 36 - 1d3
        (35, 56, 36),
        (57, 90, 36 + 1),  # 36 + 1d3
        (91, 100, 36 + 6),  # 36 + 1d6
    ],
    weight_table=[
        (1, 10, 60 - 8),  # 60 - 2d8
        (11, 22, 60 - 1),  # 60 - 1d4
        (23, 38, 60),
        (39, 50, 60 + 1),  # 60 + 1d4
        (51, 100, 60 + 12),  # 60 + 2d6
    ],
    level_limits={
        "Bard": {14: 5, 16: 6, 19: 7},
        "Cleric": {14: 4, 18: 6, 19: 8},
        "Fighter": {14: 4, 17: 5, 18: 5, 19: 8},
        "Mountebank": {14: 6, 16: 7, 19: 9},
    },
    special_abilities=[
        "Natural resistance to magic and poison",
        "Giant-type creatures receive a -4 penalty 'to hit'",
        "Halflings can move quietly with penalties to enemy surprise rolls"
    ]
)

if __name__ == "__main__":
    # Example code to test the logic
    print("Halfling:", halfling)
