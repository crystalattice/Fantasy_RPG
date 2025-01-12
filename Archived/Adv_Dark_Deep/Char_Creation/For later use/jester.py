from dataclasses import dataclass, field
from typing import Dict, Tuple


@dataclass
class Jester:
    """
    The Jester class represents a character of the Jester subclass in the game.

    Attributes:
    -----------
    hit_dice : int
        Number of hit dice used to determine hit points.
    primary_attributes : Tuple[str, str, str]
        Tuple of primary attributes required for the Jester class.
    required_alignment : str
        Required alignment for the Jester class.
    allowed_races : Tuple[str, str, str]
        Tuple of races allowed to become a Jester.
    armor : Tuple[str, str, str, str, str, str]
        Tuple of allowed armor types for the Jester class.
    weapons : Tuple[str, ...]
        Tuple of allowed weapons for the Jester class.
    abilities : Tuple[str, ...]
        Tuple of special abilities Jesters possess.
    experience_table : Dict[int, Tuple[int, int]]
        Dictionary mapping experience points to level and hit points.
    spell_slots : Dict[int, Dict[int, int]]
        Dictionary mapping Jester levels to available spell slots.
    verbal_patter : Dict[int, Dict[str, int]]
        Dictionary mapping Jester levels to verbal patter effectiveness percentages.
    charisma_adjustment : Dict[int, Dict[str, int]]
        Dictionary mapping Charisma scores to adjustments in verbal patter effectiveness.
    tumbling_and_performing : Dict[int, Dict[str, Tuple[int, int]]]
        Dictionary mapping Jester levels to tumbling and performing abilities.
    dexterity_adjustment : Dict[int, Dict[str, int]]
        Dictionary mapping Dexterity scores to adjustments in tumbling and performing abilities.
    racial_adjustment : Dict[str, Dict[str, int]]
        Dictionary mapping race to adjustments in tumbling and performing abilities.
    armor_modifiers : Dict[str, Dict[str, int]]
        Dictionary mapping armor types to modifiers in tumbling and performing abilities.
    """

    hit_dice: int = 6
    primary_attributes: Tuple[str, str, str] = ("Intelligence", "Dexterity", "Charisma")
    required_alignment: str = "Non-Lawful"
    allowed_races: Tuple[str, str, str] = ("Human", "Halfling", "Gnome")
    armor: Tuple[str, str, str, str, str, str] = (
    "Leather Cuirass", "Furs", "Gambeson", "Leather Lamellar", "Brigandine", "Leather Scale")
    weapons: Tuple[str, ...] = (
    "Club", "Dagger", "Dart", "Knife", "Short Sword", "Long Sword", "Broad Sword", "Sling", "Hand Axe", "Slapstick",
    "Javelin", "Caltrops")
    abilities: Tuple[str, ...] = ("Verbal Patter", "Tumbling", "Pranks", "Spell Use", "Attract a Troupe at 10th level")
    experience_table: Dict[int, Tuple[int, int]] = field(default_factory=lambda: {
        1: (0, 1),
        2: (2250, 2),
        3: (4500, 3),
        4: (10000, 4),
        5: (20000, 5),
        6: (40000, 6),
        7: (70000, 7),
        8: (110000, 8),
        9: (200000, 9),
        10: (350000, 10),
        11: (600000, 11),
        12: (850000, 12)
    })
    spell_slots: Dict[int, Dict[int, int]] = field(default_factory=lambda: {
        3: {1: 1},
        4: {1: 2},
        5: {1: 2, 2: 1},
        6: {1: 2, 2: 2},
        7: {1: 2, 2: 2, 3: 1},
        8: {1: 3, 2: 2, 3: 1},
        9: {1: 3, 2: 2, 3: 2, 4: 1},
        10: {1: 3, 2: 3, 3: 2, 4: 1},
        11: {1: 3, 2: 3, 3: 2, 4: 2},
        12: {1: 3, 2: 3, 3: 3, 4: 2}
    })
    verbal_patter: Dict[int, Dict[str, int]] = field(default_factory=lambda: {
        1: {"Assure, Demean, Attend, Question": 40, "Entertain, Distract, Distrust, Second Look": 20,
            "Befuddle, Trust, Value": 10, "Enrage": -10},
        2: {"Assure, Demean, Attend, Question": 45, "Entertain, Distract, Distrust, Second Look": 25,
            "Befuddle, Trust, Value": 15, "Enrage": -5},
        3: {"Assure, Demean, Attend, Question": 50, "Entertain, Distract, Distrust, Second Look": 30,
            "Befuddle, Trust, Value": 20, "Enrage": 0},
        4: {"Assure, Demean, Attend, Question": 55, "Entertain, Distract, Distrust, Second Look": 35,
            "Befuddle, Trust, Value": 25, "Enrage": 5},
        5: {"Assure, Demean, Attend, Question": 60, "Entertain, Distract, Distrust, Second Look": 40,
            "Befuddle, Trust, Value": 30, "Enrage": 10},
        6: {"Assure, Demean, Attend, Question": 65, "Entertain, Distract, Distrust, Second Look": 45,
            "Befuddle, Trust, Value": 35, "Enrage": 15},
        7: {"Assure, Demean, Attend, Question": 70, "Entertain, Distract, Distrust, Second Look": 50,
            "Befuddle, Trust, Value": 40, "Enrage": 20},
        8: {"Assure, Demean, Attend, Question": 75, "Entertain, Distract, Distrust, Second Look": 55,
            "Befuddle, Trust, Value": 45, "Enrage": 25},
        9: {"Assure, Demean, Attend, Question": 80, "Entertain, Distract, Distrust, Second Look": 60,
            "Befuddle, Trust, Value": 50, "Enrage": 30},
        10: {"Assure, Demean, Attend, Question": 85, "Entertain, Distract, Distrust, Second Look": 65,
             "Befuddle, Trust, Value": 55, "Enrage": 35},
        11: {"Assure, Demean, Attend, Question": 90, "Entertain, Distract, Distrust, Second Look": 70,
             "Befuddle, Trust, Value": 60, "Enrage": 40},
        12: {"Assure, Demean, Attend, Question": 95, "Entertain, Distract, Distrust, Second Look": 75,
             "Befuddle, Trust, Value": 65, "Enrage": 45},
        13: {"Assure, Demean, Attend, Question": 96, "Entertain, Distract, Distrust, Second Look": 80,
             "Befuddle, Trust, Value": 70, "Enrage": 50},
        14: {"Assure, Demean, Attend, Question": 97, "Entertain, Distract, Distrust, Second Look": 85,
             "Befuddle, Trust, Value": 75, "Enrage": 55},
        15: {"Assure, Demean, Attend, Question": 98, "Entertain, Distract, Distrust, Second Look": 90,
             "Befuddle, Trust, Value": 80, "Enrage": 60},
        16: {"Assure, Demean, Attend, Question": 99, "Entertain, Distract, Distrust, Second Look": 95,
             "Befuddle, Trust, Value": 85, "Enrage": 65},
        17: {"Assure, Demean, Attend, Question": 99, "Entertain, Distract, Distrust, Second Look": 96,
             "Befuddle, Trust, Value": 90, "Enrage": 70}
    })
    charisma_adjustment: Dict[int, Dict[str, int]] = field(default_factory=lambda: {
        16: {"Assure, Demean, Attend, Question": 5, "Entertain, Distract, Distrust, Second Look": 10,
             "Befuddle, Trust, Value": 0, "Enrage": 0},
        17: {"Assure, Demean, Attend, Question": 10, "Entertain, Distract, Distrust, Second Look": 15,
             "Befuddle, Trust, Value": 5, "Enrage": 0},
        18: {"Assure, Demean, Attend, Question": 15, "Entertain, Distract, Distrust, Second Look": 20,
             "Befuddle, Trust, Value": 10, "Enrage": 0},
        19: {"Assure, Demean, Attend, Question": 20, "Entertain, Distract, Distrust, Second Look": 25,
             "Befuddle, Trust, Value": 15, "Enrage": 0},
        20: {"Assure, Demean, Attend, Question": 25, "Entertain, Distract, Distrust, Second Look": 30,
             "Befuddle, Trust, Value": 20, "Enrage": 5},
        21: {"Assure, Demean, Attend, Question": 30, "Entertain, Distract, Distrust, Second Look": 35,
             "Befuddle, Trust, Value": 25, "Enrage": 10},
        22: {"Assure, Demean, Attend, Question": 35, "Entertain, Distract, Distrust, Second Look": 40,
             "Befuddle, Trust, Value": 30, "Enrage": 20},
        23: {"Assure, Demean, Attend, Question": 40, "Entertain, Distract, Distrust, Second Look": 45,
             "Befuddle, Trust, Value": 35, "Enrage": 25},
        24: {"Assure, Demean, Attend, Question": 45, "Entertain, Distract, Distrust, Second Look": 50,
             "Befuddle, Trust, Value": 40, "Enrage": 30},
        25: {"Assure, Demean, Attend, Question": 50, "Entertain, Distract, Distrust, Second Look": 55,
             "Befuddle, Trust, Value": 45, "Enrage": 35}
    })
    tumbling_and_performing: Dict[int, Dict[str, Tuple[int, int]]] = field(default_factory=lambda: {
        1: {"Attack": 0, "Evasion": 10, "Falling": (25, 10), "Balance": 20, "Fire Breathing": 0, "Juggling": 25,
            "Knife Throwing": (0, 1), "Sword Swallowing": 0},
        2: {"Attack": 0, "Evasion": 15, "Falling": (50, 10), "Balance": 25, "Fire Breathing": 5, "Juggling": 30,
            "Knife Throwing": (0, 1), "Sword Swallowing": 0},
        3: {"Attack": 1, "Evasion": 20, "Falling": (75, 10), "Balance": 30, "Fire Breathing": 10, "Juggling": 35,
            "Knife Throwing": (0, 1), "Sword Swallowing": 0},
        4: {"Attack": 1, "Evasion": 25, "Falling": (25, 20), "Balance": 35, "Fire Breathing": 15, "Juggling": 40,
            "Knife Throwing": (1, 1), "Sword Swallowing": 5},
        5: {"Attack": 1, "Evasion": 30, "Falling": (50, 20), "Balance": 40, "Fire Breathing": 20, "Juggling": 45,
            "Knife Throwing": (1, 1), "Sword Swallowing": 10},
        6: {"Attack": 1, "Evasion": 35, "Falling": (75, 20), "Balance": 45, "Fire Breathing": 25, "Juggling": 50,
            "Knife Throwing": (1, 2), "Sword Swallowing": 15},
        7: {"Attack": 2, "Evasion": 40, "Falling": (25, 30), "Balance": 50, "Fire Breathing": 30, "Juggling": 55,
            "Knife Throwing": (2, 2), "Sword Swallowing": 20},
        8: {"Attack": 2, "Evasion": 45, "Falling": (50, 30), "Balance": 55, "Fire Breathing": 35, "Juggling": 60,
            "Knife Throwing": (2, 2), "Sword Swallowing": 25},
        9: {"Attack": 2, "Evasion": 50, "Falling": (75, 30), "Balance": 60, "Fire Breathing": 40, "Juggling": 65,
            "Knife Throwing": (2, 3), "Sword Swallowing": 30},
        10: {"Attack": 2, "Evasion": 55, "Falling": (25, 40), "Balance": 65, "Fire Breathing": 45, "Juggling": 70,
             "Knife Throwing": (2, 3), "Sword Swallowing": 35},
        11: {"Attack": 3, "Evasion": 60, "Falling": (50, 40), "Balance": 70, "Fire Breathing": 50, "Juggling": 75,
             "Knife Throwing": (3, 3), "Sword Swallowing": 40},
        12: {"Attack": 3, "Evasion": 60, "Falling": (75, 40), "Balance": 75, "Fire Breathing": 55, "Juggling": 80,
             "Knife Throwing": (3, 4), "Sword Swallowing": 45},
        13: {"Attack": 3, "Evasion": 60, "Falling": (25, 50), "Balance": 80, "Fire Breathing": 60, "Juggling": 85,
             "Knife Throwing": (3, 4), "Sword Swallowing": 50},
        14: {"Attack": 3, "Evasion": 60, "Falling": (50, 50), "Balance": 85, "Fire Breathing": 65, "Juggling": 90,
             "Knife Throwing": (3, 4), "Sword Swallowing": 55},
        15: {"Attack": 4, "Evasion": 60, "Falling": (75, 50), "Balance": 90, "Fire Breathing": 70, "Juggling": 95,
             "Knife Throwing": (3, 5), "Sword Swallowing": 60},
        16: {"Attack": 4, "Evasion": 60, "Falling": (25, 60), "Balance": 95, "Fire Breathing": 75, "Juggling": 96,
             "Knife Throwing": (4, 5), "Sword Swallowing": 65},
        17: {"Attack": 4, "Evasion": 60, "Falling": (50, 60), "Balance": 96, "Fire Breathing": 80, "Juggling": 97,
             "Knife Throwing": (4, 5), "Sword Swallowing": 70}
    })
    dexterity_adjustment: Dict[int, Dict[str, int]] = field(default_factory=lambda: {
        16: {"Attack": 1, "Evasion": 2, "Falling": 0, "Balance": 3, "Fire Breathing": 0, "Juggling": 5,
             "Knife Throwing": (0, 0), "Sword Swallowing": 0},
        17: {"Attack": 1, "Evasion": 3, "Falling": 0, "Balance": 6, "Fire Breathing": 0, "Juggling": 10,
             "Knife Throwing": (1, 0), "Sword Swallowing": 0},
        18: {"Attack": 2, "Evasion": 5, "Falling": 5, "Balance": 9, "Fire Breathing": 0, "Juggling": 15,
             "Knife Throwing": (1, 0), "Sword Swallowing": 0},
        19: {"Attack": 2, "Evasion": 8, "Falling": 10, "Balance": 12, "Fire Breathing": 0, "Juggling": 20,
             "Knife Throwing": (1, 1), "Sword Swallowing": 0},
        20: {"Attack": 3, "Evasion": 12, "Falling": 15, "Balance": 15, "Fire Breathing": 0, "Juggling": 25,
             "Knife Throwing": (2, 1), "Sword Swallowing": 0},
        21: {"Attack": 3, "Evasion": 17, "Falling": 20, "Balance": 17, "Fire Breathing": 0, "Juggling": 30,
             "Knife Throwing": (2, 2), "Sword Swallowing": 0},
        22: {"Attack": 4, "Evasion": 23, "Falling": 25, "Balance": 19, "Fire Breathing": 0, "Juggling": 35,
             "Knife Throwing": (2, 2), "Sword Swallowing": 0},
        23: {"Attack": 4, "Evasion": 30, "Falling": 30, "Balance": 21, "Fire Breathing": 0, "Juggling": 38,
             "Knife Throwing": (3, 2), "Sword Swallowing": 0},
        24: {"Attack": 5, "Evasion": 38, "Falling": 35, "Balance": 22, "Fire Breathing": 0, "Juggling": 41,
             "Knife Throwing": (3, 2), "Sword Swallowing": 0},
        25: {"Attack": 5, "Evasion": 47, "Falling": 40, "Balance": 23, "Fire Breathing": 0, "Juggling": 45,
             "Knife Throwing": (3, 3), "Sword Swallowing": 0}
    })
    racial_adjustment: Dict[str, Dict[str, int]] = field(default_factory=lambda: {
        "Gnome": {"Evasion": 5, "Juggling": 5},
        "Halfling": {"Evasion": 10, "Falling": 5, "Fire Breathing": 5, "Juggling": 0, "Knife Throwing": (-1, 0)}
    })
    armor_modifiers: Dict[str, Dict[str, int]] = field(default_factory=lambda: {
        "None": {"Attack": 0, "Evasion": 0, "Falling": 0, "Balance": 0, "Fire Breathing": 0, "Juggling": 0,
                 "Knife Throwing": (0, 0), "Sword Swallowing": 0},
        "Leather Cuirass or Lamellar": {"Attack": 0, "Evasion": 0, "Falling": 0, "Balance": -3, "Fire Breathing": 0,
                                        "Juggling": 0, "Knife Throwing": (0, 0), "Sword Swallowing": 0},
        "Elven Mail": {"Attack": 0, "Evasion": 0, "Falling": 0, "Balance": 0, "Fire Breathing": 0, "Juggling": 0,
                       "Knife Throwing": (0, 0), "Sword Swallowing": 0},
        "Brigandine, Furs, or Gambeson": {"Attack": 0, "Evasion": -5, "Falling": 0, "Balance": -6, "Fire Breathing": 0,
                                          "Juggling": -5, "Knife Throwing": (0, 0), "Sword Swallowing": 0},
        "Steel Scale or Lamellar": {"Attack": 0, "Evasion": -10, "Falling": -5, "Balance": -9, "Fire Breathing": 0,
                                    "Juggling": -10, "Knife Throwing": (-1, -1), "Sword Swallowing": 0},
        "Mail": {"Attack": -1, "Evasion": -15, "Falling": -10, "Balance": -12, "Fire Breathing": -5, "Juggling": -15,
                 "Knife Throwing": (-1, -2), "Sword Swallowing": 0},
        "Plated Mail": {"Attack": -1, "Evasion": -20, "Falling": -15, "Balance": -15, "Fire Breathing": -10,
                        "Juggling": -20, "Knife Throwing": (-2, -2), "Sword Swallowing": -5},
        "Plate Armor": {"Attack": -2, "Evasion": -25, "Falling": -20, "Balance": -20, "Fire Breathing": -15,
                        "Juggling": -30, "Knife Throwing": (-2, -3), "Sword Swallowing": -10},
        "Jousting Plate": {"Attack": -3, "Evasion": -30, "Falling": -25, "Balance": -25, "Fire Breathing": -20,
                           "Juggling": -40, "Knife Throwing": (-3, -3), "Sword Swallowing": -10}
    })
