from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Savant:
    """
    The Savant class represents a specialist in knowledge, divination, and detection,
    with unique abilities to access spells usually exclusive to clerics, as well as
    creating magical items and using scrolls of various classes.

    Attributes:
        level (int): The current level of the savant.
        experience_points (int): The total experience points accumulated by the savant.
        hit_points (int): The current hit points of the savant.
        intelligence (int): The intelligence score of the savant.
        wisdom (int): The wisdom score of the savant.
        spellbook (Dict[str, List[str]]): The spellbook containing the savant's spells.
        cantrips (List[str]): The list of cantrips the savant can cast.
        armor_equipped (bool): Whether the savant is wearing armor (disables spellcasting).
        weapon_proficiency (List[str]): The list of weapons the savant is proficient with.
        scholarship (str): The initial field of scholarship, default is "Occultism".
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    intelligence: int = 14
    wisdom: int = 12
    spellbook: Dict[str, List[str]] = field(default_factory=lambda: {
        "cantrips": [],
        "1st_level": ["read savant magic"],
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
    scholarship: str = "Occultism"

    def __post_init__(self) -> None:
        """Initialize attributes that depend on the savant's level and abilities."""
        self.set_initial_attributes()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the savant based on their level and abilities."""
        self.starting_gold = self.roll_dice(2, 4) * 10
        self.hit_points = self.roll_dice(1, 4)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def advance_level(self) -> None:
        """Advances the savant to the next level, increasing hit points and allowing more spells to be memorized."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 4) if self.level <= 12 else 2
        print(f"Level advanced to {self.level}. Hit points: {self.hit_points}")

    def memorize_spells(self) -> None:
        """Determines the spells the savant can memorize at their current level."""
        spell_capacity = {
            1: [1, 0, 0, 0, 0, 0, 0, 0, 0],
            2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
            3: [2, 1, 0, 0, 0, 0, 0, 0, 0],
            4: [3, 2, 0, 0, 0, 0, 0, 0, 0],
            5: [3, 2, 1, 0, 0, 0, 0, 0, 0],
            6: [3, 3, 2, 0, 0, 0, 0, 0, 0],
            7: [4, 3, 2, 1, 0, 0, 0, 0, 0],
            8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
            9: [4, 4, 3, 2, 1, 0, 0, 0, 0],
            10: [4, 4, 3, 3, 2, 0, 0, 0, 0],
            # Continue the table up to level 27 as in the provided text.
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
        Creates a magical item if the savant's level is sufficient.

        Args:
            item_type (str): The type of magical item to be created.

        Returns:
            Optional[str]: The created magical item or None if creation failed.
        """
        if self.level >= 7:
            if item_type == "scroll":
                return "savant_scroll"
            elif self.level >= 13:
                if item_type in ["staff", "ring", "wand"]:
                    return f"enchanted_{item_type}"
            elif self.level >= 16 and item_type == "permanent":
                return "permanent_magic_item"
        return None

    def use_scroll(self, scroll_type: str, spell_level: int) -> bool:
        """
        Allows the savant to use scrolls from different classes depending on their level.

        Args:
            scroll_type (str): The type of scroll being used (mage, cleric, druid, mystic, illusionist).
            spell_level (int): The level of the spell on the scroll.

        Returns:
            bool: Whether the scroll was successfully used.
        """
        if self.level >= 5 and scroll_type == "mage":
            failure_chance = self.scroll_failure_chance(self.intelligence, spell_level, "mage")
        elif self.level >= 7 and scroll_type in ["cleric", "illusionist"]:
            failure_chance = self.scroll_failure_chance(self.wisdom, spell_level, scroll_type)
        elif self.level >= 9 and scroll_type in ["druid", "mystic"]:
            failure_chance = self.scroll_failure_chance(self.wisdom, spell_level, scroll_type)
        else:
            print(f"Cannot use {scroll_type} scrolls at this level.")
            return False

        from random import randint
        if randint(1, 100) > failure_chance:
            print(f"Successfully used {scroll_type} scroll of level {spell_level}.")
            return True
        print(f"Failed to use {scroll_type} scroll of level {spell_level}.")
        return False

    def scroll_failure_chance(self, attribute: int, spell_level: int, scroll_type: str) -> int:
        """
        Calculates the failure chance of using a scroll based on the savant's attributes.

        Args:
            attribute (int): The intelligence or wisdom score of the savant.
            spell_level (int): The level of the spell on the scroll.
            scroll_type (str): The type of scroll being used (mage, cleric, druid, mystic, illusionist).

        Returns:
            int: The failure chance percentage.
        """
        failure_chances = {
            "mage": {14: 10, 17: 5, 18: 2},
            "cleric": {12: 20, 14: 10, 17: 5, 18: 2},
            "druid": {12: 25, 14: 15, 17: 10, 18: 7},
            "mystic": {12: 25, 14: 15, 17: 10, 18: 7},
            "illusionist": {14: 10, 17: 5, 18: 2}
        }
        base_chance = failure_chances.get(scroll_type, {}).get(attribute, 100)
        return base_chance + (spell_level * 5)  # Penalty per spell level

    def cast_spell(self, spell_name: str) -> bool:
        """
        Casts a spell from the savant's spellbook, provided it is memorized.

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

    def research_spell(self, spell_name: str) -> bool:
        """
        Allows the savant to research and learn a new spell, adding it to the spellbook.

        Args:
            spell_name (str): The name of the spell to research.

        Returns:
            bool: Whether the spell was successfully researched and added to the spellbook.
        """
        if self.level >= 7:
            self.spellbook["new_research"] = self.spellbook.get("new_research", []) + [spell_name]
            print(f"{spell_name} added to spellbook through research.")
            return True
        print(f"{spell_name} could not be researched.")
        return False
