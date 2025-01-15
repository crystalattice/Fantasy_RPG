from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Mystic:
    """
    The Mystic class represents an initiate of an inner mystery tradition that seeks direct
    communion with the multiverse in order to achieve enlightenment. Mystics are known
    for their deep connection with ultimate reality, insight, and awareness, with powers
    centered on knowledge, defense, and spiritual asceticism.

    Attributes:
        level (int): The current level of the mystic.
        experience_points (int): The total experience points accumulated by the mystic.
        hit_points (int): The current hit points of the mystic.
        wisdom (int): The wisdom score of the mystic.
        dexterity (int): The dexterity score of the mystic.
        alignment (str): The alignment of the mystic, which must be any good alignment.
        weapons (List[str]): The list of weapons the mystic is proficient with.
        spell_slots (Dict[int, int]): The number of spells available to the mystic at different levels.
        meditation_benefits (Dict[str, int]): The benefits gained from meditation as the mystic progresses in levels.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    wisdom: int = 13
    dexterity: int = 9
    alignment: str = "good"
    weapons: List[str] = field(default_factory=lambda: ["club", "mace", "spear", "staff"])
    spell_slots: Dict[int, int] = field(default_factory=dict)
    meditation_benefits: Dict[str, int] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Initialize attributes that depend on the mystic's level and abilities."""
        self.set_initial_attributes()
        self.set_spell_slots()
        self.set_meditation_benefits()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the mystic based on their level and abilities."""
        self.starting_gold = self.roll_dice(3, 8) + 10
        self.hit_points = self.roll_dice(1, 6)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def set_spell_slots(self) -> None:
        """Sets the spell slots available to the mystic at different levels."""
        self.spell_slots = {
            1: {1: 1},
            2: {1: 2},
            3: {1: 2, 2: 1},
            4: {1: 3, 2: 2},
            5: {1: 3, 2: 3, 3: 1},
            6: {1: 3, 2: 3, 3: 2},
            7: {1: 3, 2: 3, 3: 2, 4: 1},
            8: {1: 3, 2: 3, 3: 3, 4: 2},
            9: {1: 4, 2: 4, 3: 3, 4: 2, 5: 1},
            10: {1: 4, 2: 4, 3: 3, 4: 3, 5: 2},
            11: {1: 5, 2: 4, 3: 4, 4: 3, 5: 2, 6: 1},
            12: {1: 6, 2: 5, 3: 5, 4: 3, 5: 2, 6: 2},
            13: {1: 6, 2: 6, 3: 6, 4: 4, 5: 2, 6: 2},
            14: {1: 6, 2: 6, 3: 6, 4: 5, 5: 3, 6: 2},
            15: {1: 7, 2: 7, 3: 7, 4: 5, 5: 4, 6: 2},
            16: {1: 7, 2: 7, 3: 7, 4: 6, 5: 5, 6: 3, 7: 1},
            17: {1: 8, 2: 8, 3: 8, 4: 6, 5: 5, 6: 3, 7: 1},
            18: {1: 8, 2: 8, 3: 8, 4: 7, 5: 6, 6: 4, 7: 1},
            19: {1: 9, 2: 9, 3: 9, 4: 7, 5: 6, 6: 4, 7: 2},
            20: {1: 9, 2: 9, 3: 9, 4: 8, 5: 7, 6: 5, 7: 2},
            21: {1: 9, 2: 9, 3: 9, 4: 9, 5: 8, 6: 6, 7: 2},
            22: {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 6, 7: 3},
            23: {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 7, 7: 3},
            24: {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 8, 7: 3},
            25: {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 8, 7: 4},
            26: {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 4},
            27: {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 5},
            28: {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 6},
            29: {1: 9, 2: 9, 3: 9, 4: 9, 5: 9, 6: 9, 7: 7},
        }

    def set_meditation_benefits(self) -> None:
        """Sets the meditation benefits gained by the mystic at different levels."""
        self.meditation_benefits = {
            "ESP_resistance": max(50 - (self.level - 2) * 2, 0) if self.level >= 2 else None,
            "levitation_weight": max(self.level * 5, 0) if self.level >= 4 else None,
            "pain_management": True if self.level >= 3 else False,
            "ethereal_travel": True if self.level >= 9 else False,
            "vow_of_silence": True if self.level >= 9 else False,
        }

    def advance_level(self) -> None:
        """Advances the mystic to the next level, increasing hit points and adjusting abilities."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 6) if self.level <= 11 else 2

        # Potentially adjust spell slots and meditation benefits if level thresholds are crossed
        if self.level >= 2:
            self.set_meditation_benefits()

        print(f"Level advanced to {self.level}. Updated spell slots: {self.spell_slots.get(self.level, {})}")

    def create_scroll(self) -> Optional[str]:
        """
        Allows the mystic to create scrolls with mystic spells inscribed upon them if the mystic's level is sufficient.

        Returns:
            Optional[str]: The created scroll if successful; otherwise, None.
        """
        if self.level < 7:
            print("Mystic level too low to create scrolls.")
            return None

        print("Scroll created successfully.")
        return "Mystic Scroll"

    def meditate(self) -> None:
        """
        Allows the mystic to meditate, gaining special benefits such as ESP resistance, levitation, and pain management.
        The specific benefits depend on the mystic's level.
        """
        if self.meditation_benefits["ESP_resistance"]:
            print(f"ESP resistance active: {self.meditation_benefits['ESP_resistance']}% resistance to mind-reading.")
        if self.meditation_benefits["levitation_weight"]:
            print(f"Levitation available for up to {self.meditation_benefits['levitation_weight']} lbs.")
        if self.meditation_benefits["pain_management"]:
            print("Pain management active. Mystic can operate up to -8 hit points without collapsing.")
        if self.meditation_benefits["ethereal_travel"]:
            print("Ethereal travel available once per day.")
        if self.meditation_benefits["vow_of_silence"]:
            print("Vow of silence taken. Mystic can cast spells without incantation.")

    def manage_pain(self) -> bool:
        """
        Allows the mystic to manage pain, functioning at up to -8 hit points before collapsing from physical damage.

        Returns:
            bool: True if the mystic is managing pain; otherwise, False.
        """
        if self.meditation_benefits["pain_management"]:
            print("Pain managed successfully. Mystic continues to function.")
            return True
        print("Pain management not available at this level.")
        return False

    def take_vow_of_silence(self) -> None:
        """
        Allows the mystic to take a vow of silence at 9th level, granting the ability to cast spells without incantation.
        """
        if self.level >= 9:
            self.meditation_benefits["vow_of_silence"] = True
            print("Vow of silence taken. Spells can be cast without incantation.")
        else:
            print("Mystic level too low to take a vow of silence.")

    def gain_disciples(self) -> Optional[List[str]]:
        """
        Grants the mystic a small cadre of students who seek to learn from the mystic's example at 9th level.

        Returns:
            Optional[List[str]]: A list of disciples if successful; otherwise, None.
        """
        if self.level >= 9:
            num_disciples = self.roll_dice(1, 6)
            disciples = [f"Disciple {i+1}" for i in range(num_disciples)]
            print(f"{num_disciples} disciples have joined the mystic.")
            return disciples
        print("Mystic level too low to gain disciples.")
        return None
