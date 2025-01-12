from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class Bard:
    """
    The Bard class represents a character with a unique blend of musical, magical, and
    thieving abilities. Bards are skilled in influencing others, gathering lore, and casting
    spells through their songs.

    Attributes:
        level (int): The current level of the bard.
        experience_points (int): The total experience points accumulated by the bard.
        hit_points (int): The current hit points of the bard.
        spells (Dict[int, List[str]]): A dictionary mapping spell levels to lists of spells available at each level.
        verbal_patter (Dict[int, Dict[str, int]]): A dictionary mapping bard level to verbal patter abilities.
        spell_slots (Dict[int, Dict[int, int]]): A dictionary mapping bard level to available spell slots.
        lore (Dict[int, int]): A dictionary mapping bard level to the lore ability percentage.
        hide_in_shadows (Dict[int, int]): A dictionary mapping bard level to hide in shadows ability percentage.
        listen_at_doors (Dict[int, int]): A dictionary mapping bard level to listen at doors ability percentage.
        read_languages (Dict[int, int]): A dictionary mapping bard level to read languages ability percentage.
        sleight_of_hand (Dict[int, int]): A dictionary mapping bard level to sleight of hand ability percentage.
        dexterity_adjustment (Dict[int, Dict[str, int]]): A dictionary mapping dexterity scores to adjustments for bard abilities.
        racial_adjustment (Dict[str, Dict[str, int]]): A dictionary mapping races to adjustments for bard abilities.
        armor_modifiers (Dict[str, Dict[str, int]]): A dictionary mapping armor types to adjustments for bard abilities.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = 0
    spells: Dict[int, List[str]] = field(default_factory=lambda: {
        1: ["Alter Animal", "Bless", "Cure Animal Wounds", "Sleep"],
        2: ["Calmness", "Disgust", "False Trail", "Friends"],
        3: ["Haunting Dream", "Message", "Perception", "Resist Cold"],
        4: ["Sharp Note", "Ready Spell", "Ventriloquism", "Wizard Lock"]
    })
    verbal_patter: Dict[int, Dict[str, int]] = field(default_factory=lambda: {
        1: {"Attend": 40, "Inspire": 30, "Entertain": 20, "Distract": 10},
        2: {"Attend": 45, "Inspire": 35, "Entertain": 25, "Distract": 15},
        3: {"Attend": 50, "Inspire": 40, "Entertain": 30, "Distract": 20},
        4: {"Attend": 55, "Inspire": 45, "Entertain": 35, "Distract": 25},
        5: {"Attend": 60, "Inspire": 50, "Entertain": 40, "Distract": 30},
        6: {"Attend": 65, "Inspire": 55, "Entertain": 45, "Distract": 35},
        7: {"Attend": 70, "Inspire": 60, "Entertain": 50, "Distract": 40},
        8: {"Attend": 75, "Inspire": 65, "Entertain": 55, "Distract": 45},
        9: {"Attend": 80, "Inspire": 70, "Entertain": 60, "Distract": 50},
        10: {"Attend": 85, "Inspire": 75, "Entertain": 65, "Distract": 55},
        11: {"Attend": 90, "Inspire": 80, "Entertain": 70, "Distract": 60},
        12: {"Attend": 95, "Inspire": 85, "Entertain": 75, "Distract": 65},
    })
    spell_slots: Dict[int, Dict[int, int]] = field(default_factory=lambda: {
        1: {1: 1},
        2: {1: 2},
        3: {1: 2, 2: 1},
        4: {1: 3, 2: 2},
        5: {1: 4, 2: 2, 3: 1},
        6: {1: 4, 2: 2, 3: 2},
        7: {1: 4, 2: 3, 3: 2, 4: 1},
        8: {1: 4, 2: 3, 3: 3, 4: 2},
        9: {1: 4, 2: 3, 3: 3, 4: 2, 5: 1},
        10: {1: 4, 2: 4, 3: 3, 4: 2, 5: 2},
        11: {1: 4, 2: 4, 3: 4, 4: 3, 5: 3, 6: 1},
        12: {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 1},
        13: {1: 5, 2: 5, 3: 5, 4: 4, 5: 4, 6: 2, 7: 1},
        14: {1: 5, 2: 5, 3: 5, 4: 4, 5: 4, 6: 2, 7: 2},
        15: {1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 3, 7: 3},
    })
    lore: Dict[int, int] = field(default_factory=lambda: {
        1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45,
        10: 50, 11: 55, 12: 60, 13: 65, 14: 70, 15: 75, 16: 80, 17: 85, 18: 90
    })
    hide_in_shadows: Dict[int, int] = field(default_factory=lambda: {
        1: 0, 2: 0, 3: 10, 4: 15, 5: 20, 6: 25, 7: 31, 8: 37, 9: 43,
        10: 49, 11: 56, 12: 63, 13: 70, 14: 77, 15: 85, 16: 93, 17: 99, 18: 99
    })
    listen_at_doors: Dict[int, int] = field(default_factory=lambda: {
        1: 10, 2: 10, 3: 15, 4: 15, 5: 20, 6: 20, 7: 25, 8: 25, 9: 30,
        10: 30, 11: 35, 12: 35, 13: 40, 14: 40, 15: 50, 16: 50, 17: 55, 18: 60
    })
    read_languages: Dict[int, int] = field(default_factory=lambda: {
        1: 20, 2: 25, 3: 30, 4: 35, 5: 40, 6: 45, 7: 50, 8: 55, 9: 60,
        10: 65, 11: 70, 12: 75, 13: 80, 14: 85, 15: 90, 16: 90, 17: 90, 18: 90
    })
    sleight_of_hand: Dict[int, int] = field(default_factory=lambda: {
        1: 35, 2: 40, 3: 45, 4: 50, 5: 55, 6: 60, 7: 65, 8: 70, 9: 75,
        10: 80, 11: 85, 12: 90, 13: 95, 14: 100, 15: 105, 16: 110, 17: 115, 18: 115
    })
    dexterity_adjustment: Dict[int, Dict[str, int]] = field(default_factory=lambda: {
        9: {"Hide in Shadows": -10, "Sleight of Hand": -10},
        10: {"Hide in Shadows": -5, "Sleight of Hand": -5},
        16: {"Hide in Shadows": 0, "Sleight of Hand": 5},
        17: {"Hide in Shadows": 5, "Sleight of Hand": 10},
        18: {"Hide in Shadows": 10, "Sleight of Hand": 15},
        19: {"Hide in Shadows": 12, "Sleight of Hand": 20},
        20: {"Hide in Shadows": 15, "Sleight of Hand": 23},
        21: {"Hide in Shadows": 18, "Sleight of Hand": 26},
        22: {"Hide in Shadows": 20, "Sleight of Hand": 29},
        23: {"Hide in Shadows": 23, "Sleight of Hand": 32},
        24: {"Hide in Shadows": 25, "Sleight of Hand": 35},
        25: {"Hide in Shadows": 30, "Sleight of Hand": 38}
    })
    racial_adjustment: Dict[str, Dict[str, int]] = field(default_factory=lambda: {
        "Elf": {"Hide in Shadows": 10, "Listen at Doors": 5, "Sleight of Hand": 5},
        "Gnome": {"Hide in Shadows": 5, "Listen at Doors": 10, "Sleight of Hand": 5},
        "Half-Elf": {"Hide in Shadows": 5, "Sleight of Hand": 5},
        "Halfling": {"Hide in Shadows": 15, "Read Languages": -5}
    })
    armor_modifiers: Dict[str, Dict[str, int]] = field(default_factory=lambda: {
        "None": {"Hide in Shadows": 5, "Listen at Doors": 0, "Sleight of Hand": 5},
        "Leather Cuirass or Lamellar": {"Hide in Shadows": 0, "Listen at Doors": 0, "Sleight of Hand": 0},
        "Elven Mail": {"Hide in Shadows": -10, "Listen at Doors": -5, "Sleight of Hand": -20},
        "Brigandine or Lamellar": {"Hide in Shadows": -20, "Listen at Doors": -10, "Sleight of Hand": -30},
        "Mail": {"Hide in Shadows": -30, "Listen at Doors": -15, "Sleight of Hand": -40}
    })

    def level_up(self):
        """
        Level up the bard, increasing hit points, available spells, and improving abilities.

        Increases the bard's level by one, updates the hit points based on the bard's hit dice (d6),
        and increases abilities like lore, hide in shadows, and others according to the bard's level progression.
        """
        self.level += 1
        self.hit_points += self._roll_hit_dice()

        # Improve abilities according to the bard's level progression
        self._update_abilities()

    def _roll_hit_dice(self) -> int:
        """
        Roll the hit dice for the bard to determine additional hit points upon leveling up.

        Returns:
            int: The rolled hit points based on a 6-sided die.
        """
        from random import randint
        return randint(1, 6)

    def _update_abilities(self):
        """
        Update the bard's abilities based on the new level.

        This method updates all relevant abilities such as lore, hide in shadows,
        and others based on the bard's current level.
        """
        # Example of updating abilities
        self.lore[self.level] = self.lore.get(self.level, 0)
        self.hide_in_shadows[self.level] = self.hide_in_shadows.get(self.level, 0)
        self.listen_at_doors[self.level] = self.listen_at_doors.get(self.level, 0)
        self.read_languages[self.level] = self.read_languages.get(self.level, 0)
        self.sleight_of_hand[self.level] = self.sleight_of_hand.get(self.level, 0)

    def add_experience(self, points: int):
        """
        Add experience points to the bard and handle level-ups if necessary.

        Args:
            points (int): The amount of experience points to add.
        """
        self.experience_points += points
        self._check_for_level_up()

    def _check_for_level_up(self):
        """
        Check if the bard has enough experience points to level up and do so if possible.
        """
        level_thresholds = [0, 2500, 5000, 12500, 25000, 50000, 100000, 200000, 400000, 650000, 900000]
        if self.level < len(level_thresholds) and self.experience_points >= level_thresholds[self.level]:
            self.level_up()
