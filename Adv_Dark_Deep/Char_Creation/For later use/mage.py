from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Mage:
    """
    The Mage class represents a student of the arcane arts who uses knowledge of the 
    universe's mysteries to cast spells and create magical items. Due to their focus on 
    magical study, mages are weaker in melee combat.

    Attributes:
        level (int): The current level of the mage.
        experience_points (int): The total experience points accumulated by the mage.
        hit_points (int): The current hit points of the mage.
        intelligence (int): The intelligence score of the mage.
        dexterity (int): The dexterity score of the mage.
        spellbook (Dict[str, List[str]]): The spellbook containing the mage's spells.
        cantrips (List[str]): The list of cantrips the mage can cast.
        armor_equipped (bool): Whether the mage is wearing armor (disables spellcasting).
        weapon_proficiency (List[str]): The list of weapons the mage is proficient with.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    intelligence: int = 9
    dexterity: int = 6
    spellbook: Dict[str, List[str]] = field(default_factory=lambda: {
        "cantrips": [],
        "1st_level": ["read magic"],
        "2nd_level": [],
        "3rd_level": [],
        "4th_level": [],
        "5th_level": [],
        "6th_level": [],
        "7th_level": [],
        "8th_level": [],
        "9th_level": []
    })
    cantrips: List[str] = field(default_factory=list)
    armor_equipped: bool = False
    weapon_proficiency: List[str] = field(default_factory=lambda: ["dagger", "dart", "knife", "sling", "staff"])

    def __post_init__(self) -> None:
        """Initialize attributes that depend on the mage's level and abilities."""
        self.set_initial_attributes()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the mage based on their level and abilities."""
        self.starting_gold = self.roll_dice(2, 4) * 10
        self.hit_points = self.roll_dice(1, 4)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def advance_level(self) -> None:
        """Advances the mage to the next level, increasing hit points and allowing more spells to be memorized."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 4) if self.level <= 13 else 1
        print(f"Level advanced to {self.level}. Hit points: {self.hit_points}")

    def memorize_spells(self) -> None:
        """Determines the spells the mage can memorize at their current level."""
        spell_capacity = {
            1: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [2, 1, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 2, 0, 0, 0, 0, 0, 0, 0],
            5: [4, 2, 1, 0, 0, 0, 0, 0, 0],
            6: [4, 2, 2, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 2, 1, 0, 0, 0, 0, 0],
            8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            9: [4, 3, 3, 2, 1, 0, 0, 0, 0],
            10: [4, 4, 3, 2, 2, 0, 0, 0, 0],
            # Continue the table up to level 29 as in the provided text.
        }
        slots = spell_capacity.get(self.level, [5, 5, 5, 5, 5, 5, 5, 5, 5])

        # Assigning spell slots to the spellbook
        for i, slot_count in enumerate(slots):
            spell_level = f"{i + 1}st_level" if i < 3 else f"{i + 1}th_level"
            current_spells = len(self.spellbook[spell_level])
            if current_spells < slot_count:
                additional_spells = slot_count - current_spells
                self.spellbook[spell_level] += ["new_spell"] * additional_spells

        print(f"Spells memorized: {self.spellbook}")

    def create_magic_item(self, item_type: str) -> Optional[str]:
        """
        Creates a magical item if the mage's level is sufficient.

        Args:
            item_type (str): The type of magical item to be created.

        Returns:
            Optional[str]: The created magical item or None if creation failed.
        """
        if self.level >= 7:
            if item_type == "scroll":
                return "mage_scroll"
            elif self.level >= 12:
                if item_type in ["wand", "ring", "weapon"]:
                    return f"enchanted_{item_type}"
            elif self.level >= 16 and item_type == "permanent":
                return "permanent_magic_item"
        return None

    def use_magic_item(self, item_name: str) -> bool:
        """
        Uses a magic item, provided the mage is not wearing armor and the item is usable by mages.

        Args:
            item_name (str): The name of the magic item.

        Returns:
            bool: Whether the item was successfully used.
        """
        if not self.armor_equipped:
            print(f"{item_name} used successfully.")
            return True
        print(f"{item_name} use failed due to armor being equipped.")
        return False

    def cast_spell(self, spell_name: str) -> bool:
        """
        Casts a spell from the mage's spellbook, provided it is memorized.

        Args:
            spell_name (str): The name of the spell to cast.

        Returns:
            bool: Whether the spell was successfully cast.
        """
        for spells in self.spellbook.values():
            if spell_name in spells:
                print(f"{spell_name} cast successfully.")
                return True
        print(f"{spell_name} is not memorized or cannot be cast.")
        return False
