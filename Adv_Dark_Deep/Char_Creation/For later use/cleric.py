from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Cleric:
    """
    The Cleric class represents a follower of a deity, pantheon, or religion who receives divine abilities
    and is an able warrior for the defense and advancement of their faith. Clerics have access to a variety
    of spells focused on healing, defense, and divination, and they possess the ability to turn undead.

    Attributes:
        level (int): The current level of the cleric.
        experience_points (int): The total experience points accumulated by the cleric.
        hit_points (int): The current hit points of the cleric.
        wisdom (int): The wisdom score of the cleric.
        alignment (str): The alignment of the cleric, as dictated by their deity.
        social_class (str): The social class of the cleric.
        starting_gold (int): The amount of gold the cleric starts with.
        armor (str): The type of armor the cleric wears.
        shield (str): The type of shield the cleric uses.
        weapons (List[str]): The list of weapons the cleric is proficient with.
        deity (str): The deity or pantheon the cleric serves.
        spell_slots (Dict[int, int]): The number of spells available to the cleric at different levels.
        turn_undead_table (Dict[int, List[int]]): The table used for determining the success of turning undead.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    wisdom: int = 9
    alignment: str = "lawful good"
    social_class: str = "commoner"
    starting_gold: int = field(init=False)
    armor: str = "chain mail"
    shield: str = "large shield"
    weapons: List[str] = field(default_factory=lambda: ["club", "mace", "flail", "hammer", "quarterstaff"])
    deity: str = "Generic Deity"
    spell_slots: Dict[int, int] = field(default_factory=dict)
    turn_undead_table: Dict[int, List[int]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Initialize attributes that depend on the cleric's level and wisdom."""
        self.set_initial_attributes()
        self.set_spell_slots()
        self.set_turn_undead_table()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the cleric based on social class."""
        self.starting_gold = self.roll_dice(3, 6) * 10
        self.hit_points = self.roll_dice(1, 8)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def set_spell_slots(self) -> None:
        """Sets the spell slots available to the cleric at different levels."""
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
        }

    def set_turn_undead_table(self) -> None:
        """Sets the table for turning undead based on cleric level."""
        self.turn_undead_table = {
            1: [10, 13, 16, 19, 20],
            2: [7, 10, 13, 16, 19, 20],
            3: [4, 7, 10, 13, 16, 19],
            4: [0, 4, 7, 10, 13, 16, 19, 20],
            5: [0, 0, 4, 7, 10, 13, 16, 19],
            6: [0, 0, 0, 4, 7, 10, 13, 16, 19, 20],
            7: [0, 0, 0, 0, 4, 7, 10, 13, 16, 19],
            8: [0, 0, 0, 0, 0, 4, 7, 10, 13, 16],
            9: [0, 0, 0, 0, 0, 0, 4, 7, 10, 13],
            10: [0, 0, 0, 0, 0, 0, 0, 4, 7, 10],
            11: [0, 0, 0, 0, 0, 0, 0, 0, 4, 7],
            12: [0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            13: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        }

    def advance_level(self) -> None:
        """Advances the cleric to the next level, increasing hit points and adjusting abilities."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 8) if self.level <= 9 else 2

        # Potentially adjust spell slots and turning abilities if level thresholds are crossed
        if self.level >= 1:
            print(f"Updated spell slots: {self.spell_slots.get(self.level, {})}")

        if self.level in self.turn_undead_table:
            print(f"Updated turn undead table for level {self.level}")

    def turn_undead(self, undead_type: int) -> bool:
        """
        Attempts to turn undead or extra-planar entities.

        Args:
            undead_type (int): The type of undead creature to turn, based on the cleric's level.

        Returns:
            bool: True if the undead was successfully turned, False otherwise.
        """
        from random import randint

        required_roll = self.turn_undead_table[self.level][undead_type]
        roll = randint(1, 20)

        if roll >= required_roll:
            print("Successfully turned the undead.")
            return True
        else:
            print("Failed to turn the undead.")
            return False

    def receive_spell(self, spell_level: int) -> Optional[str]:
        """
        Attempts to receive a spell from the deity or servitors based on the cleric's level.

        Args:
            spell_level (int): The level of the spell to receive.

        Returns:
            Optional[str]: The spell granted, if successful; otherwise, None.
        """
        if spell_level > 7 or spell_level < 1:
            print("Invalid spell level.")
            return None

        if spell_level > 5 and self.wisdom < 17:
            print("Cleric's wisdom is too low to receive higher-level spells.")
            return None

        if spell_level > 3:
            print("Spell received from a servitor.")
        else:
            print("Spell received from the deity directly.")

        # Simulate the spell received
        return f"Spell of level {spell_level}"

    def create_magic_item(self, item_type: str) -> Optional[str]:
        """
        Creates a magic item if the cleric's level is sufficient.

        Args:
            item_type (str): The type of magic item to create.

        Returns:
            Optional[str]: The created magic item, if successful; otherwise, None.
        """
        if self.level < 7:
            print("Cleric level too low to create magic items.")
            return None

        print(f"{item_type} created successfully.")
        return f"Magic {item_type}"
