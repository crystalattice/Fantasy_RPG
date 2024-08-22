from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class Gnome:
    """Class representing the gnome race with its different subraces."""
    subrace: str
    ability_scores: Dict[str, Dict[str, Tuple[int, int]]]
    infravision_range: int = 60
    saving_throw_bonus: Dict[int, int] = field(default_factory=dict)
    hit_bonus: Dict[str, int] = field(default_factory=dict)
    hit_penalty: Dict[str, int] = field(default_factory=dict)
    languages: List[str] = field(default_factory=list)
    additional_languages_limit: int = 2
    age_ranges: Dict[str, Tuple[int, int]] = field(default_factory=dict)
    height_table: List[Tuple[int, int, int]] = field(default_factory=list)
    weight_table: List[Tuple[int, int, int]] = field(default_factory=list)
    level_limits: Dict[str, Dict[int, int]] = field(default_factory=dict)
    mining_abilities: Dict[str, int] = field(default_factory=dict)
    additional_abilities: Dict[str, str] = field(default_factory=dict)
    special_abilities: List[str] = field(default_factory=list)


# Data for Hill Gnomes
hill_gnome = Gnome(
    subrace="Hill Gnome",
    ability_scores={
        "Male": {
            "Strength": (6, 18),
            "Intelligence": (7, 18),
            "Wisdom": (3, 18),
            "Dexterity": (3, 18),
            "Constitution": (8, 18),
            "Charisma": (3, 18),
        },
        "Female": {
            "Strength": (6, 15),
            "Intelligence": (7, 18),
            "Wisdom": (3, 18),
            "Dexterity": (3, 18),
            "Constitution": (8, 18),
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
    hit_bonus={
        "Kobolds": 1,
        "Goblins": 1,
    },
    hit_penalty={
        "Gnolls": -4,
        "Bugbears": -4,
        "Ogres": -4,
        "Trolls": -4,
        "Ogre Magi": -4,
        "Giants": -4,
        "Titans": -4,
    },
    languages=["Common", "Dwarvish", "Gnomish", "Halfling", "Goblin", "Kobold"],
    age_ranges={
        "Young Adult": (59, 90),
        "Mature": (91, 300),
        "Middle Age": (301, 450),
        "Old": (451, 600),
        "Very Old": (601, 750),
    },
    height_table=[
        (1, 40, 39 - 1),  # 39 - 1d3
        (41, 65, 39),
        (66, 100, 39 + 1),  # 39 + 1d3
    ],
    weight_table=[
        (1, 20, 80 - 4),  # 80 - 2d4
        (21, 37, 80 - 1),  # 80 - 1d4
        (38, 58, 80),
        (59, 75, 80 + 1),  # 80 + 1d4
        (76, 100, 80 + 12),  # 80 + 2d6
    ],
    level_limits={
        "Bard": {14: 5, 16: 6, 19: 6},
        "Cleric": {14: 7, 16: 8, 19: 12},
        "Fighter": {14: 5, 16: 6, 19: 9},
        "Illusionist": {14: 6, 16: 7, 19: 8},
        "Mountebank": {14: 8, 16: 9, 19: 11},
    },
    mining_abilities={
        "Detect Slopes": 80,
        "Detect Unsafe Areas": 70,
        "Sense Depth": 60,
        "Sense Direction Underground": 50
    },
    additional_abilities={
        "Speak with Burrowing Mammals": "Ability to communicate with burrowing mammals like badgers, moles, etc."
    },
    special_abilities=[
        "Infravision 60 feet",
        "Saving throw bonuses based on constitution",
        "Hit bonuses against kobolds and goblins",
        "Hit penalties for attacking gnolls, bugbears, ogres, trolls, ogre magi, giants, titans",
    ]
)

# Data for Forest Gnomes
forest_gnome = Gnome(
    subrace="Forest Gnome",
    ability_scores={
        "Male": {
            "Strength": (6, 18),
            "Intelligence": (7, 18),
            "Wisdom": (3, 18),
            "Dexterity": (3, 18),
            "Constitution": (8, 18),
            "Charisma": (3, 18),
        },
        "Female": {
            "Strength": (6, 15),
            "Intelligence": (7, 18),
            "Wisdom": (3, 18),
            "Dexterity": (3, 18),
            "Constitution": (8, 18),
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
    hit_bonus={
        "Kobolds": 1,
        "Goblins": 1,
    },
    hit_penalty={
        "Gnolls": -4,
        "Bugbears": -4,
        "Ogres": -4,
        "Trolls": -4,
        "Ogre Magi": -4,
        "Giants": -4,
        "Titans": -4,
    },
    languages=["Common", "Dwarvish", "Gnomish", "Halfling", "Goblin", "Kobold"],
    age_ranges={
        "Young Adult": (59, 90),
        "Mature": (91, 300),
        "Middle Age": (301, 450),
        "Old": (451, 600),
        "Very Old": (601, 750),
    },
    height_table=[
        (1, 40, 39 - 1),  # 39 - 1d3
        (41, 65, 39),
        (66, 100, 39 + 1),  # 39 + 1d3
    ],
    weight_table=[
        (1, 20, 82 - 4),  # 82 - 2d4
        (21, 37, 82 - 1),  # 82 - 1d4
        (38, 58, 82),
        (59, 75, 82 + 1),  # 82 + 1d4
        (76, 100, 82 + 12),  # 82 + 2d6
    ],
    level_limits={
        "Bard": {14: 5, 16: 6, 19: 6},
        "Druid": {14: 7, 16: 7, 19: 7},
        "Fighter": {14: 5, 16: 5, 19: 9},
        "Savant": {14: 7, 16: 7, 19: 14},
        "Mountebank": {14: 8, 16: 9, 19: 11},
    },
    mining_abilities={
        "Detect Slopes": 80,
        "Detect Unsafe Areas": 70,
        "Sense Depth": 60,
        "Sense Direction Underground": 50
    },
    additional_abilities={
        "Speak with Small Woodland Creatures": "Ability to communicate with small woodland creatures like foxes, squirrels, etc."
    },
    special_abilities=[
        "Infravision 60 feet",
        "Saving throw bonuses based on constitution",
        "Hit bonuses against kobolds and goblins",
        "Hit penalties for attacking gnolls, bugbears, ogres, trolls, ogre magi, giants, titans",
        "Blend with surroundings in wooded terrain with underbrush 65% of the time"
    ]
)

# Data for Deep Gnomes
deep_gnome = Gnome(
    subrace="Deep Gnome",
    ability_scores={
        "Male": {
            "Strength": (6, 18),
            "Intelligence": (7, 18),
            "Wisdom": (3, 18),
            "Dexterity": (3, 18),
            "Constitution": (8, 18),
            "Charisma": (3, 18),
        },
        "Female": {
            "Strength": (6, 15),
            "Intelligence": (7, 18),
            "Wisdom": (3, 18),
            "Dexterity": (3, 18),
            "Constitution": (8, 18),
            "Charisma": (3, 18),
        }
    },
    infravision_range=120,
    saving_throw_bonus={
        4: 1,
        7: 2,
        11: 3,
        14: 4,
        18: 5
    },
    hit_bonus={
        "Kobolds": 1,
        "Goblins": 1,
        "Dark Elves (Drow)": 1,
        "Fish Men": 1,
    },
    hit_penalty={
        "Gnolls": -4,
        "Bugbears": -4,
        "Ogres": -4,
        "Trolls": -4,
        "Ogre Magi": -4,
        "Giants": -4,
        "Titans": -4,
    },
    languages=["Common", "Dwarvish", "Gnomish", "Halfling", "Goblin", "Kobold"],
    age_ranges={
        "Young Adult": (50, 82),
        "Mature": (83, 270),
        "Middle Age": (271, 405),
        "Old": (406, 540),
        "Very Old": (541, 675),
    },
    height_table=[
        (1, 40, 39 - 1),  # 39 - 1d3
        (41, 65, 39),
        (66, 100, 39 + 1),  # 39 + 1d3
    ],
    weight_table=[
        (1, 20, 80 - 4),  # 80 - 2d4
        (21, 37, 80 - 1),  # 80 - 1d4
        (38, 58, 80),
        (59, 75, 80 + 1),  # 80 + 1d4
        (76, 100, 80 + 12),  # 80 + 2d6
    ],
    level_limits={
        "Bard": {14: 5, 16: 6, 19: 6},
        "Cleric": {14: 7, 16: 8, 19: 12},
        "Fighter": {14: 5, 16: 6, 19: 9},
        "Illusionist": {14: 6, 16: 7, 19: 8},
        "Mountebank": {14: 8, 16: 9, 19: 11},
    },
    mining_abilities={
        "Detect Slopes": 80,
        "Detect Unsafe Areas": 70,
        "Sense Depth": 60,
        "Sense Direction Underground": 50
    },
    additional_abilities={
        "Elemental Summons": "Ability to summon an earth elemental or xorn at 6th level, once per day",
        "Camouflage": "Ability to camouflage themselves around natural stonework with a 60% chance of success"
    },
    special_abilities=[
        "Infravision 120 feet",
        "Ultravision 30 feet",
        "Saving throw bonuses: +2 vs poison, +3 vs all other attacks",
        "Immunity to illusions",
        "Hit bonuses against kobolds, goblins, dark elves (drow), and fish men",
        "Hit penalties for attacking gnolls, bugbears, ogres, trolls, ogre magi, giants, titans",
        "Summon an earth elemental once per day",
        "Non-detection ability as a constant effect"
    ]
)

if __name__ == "__main__":
    # Example code to test the logic
    print("Hill Gnome:", hill_gnome)
    print("Forest Gnome:", forest_gnome)
    print("Deep Gnome:", deep_gnome)
