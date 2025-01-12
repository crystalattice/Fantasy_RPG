from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class Barbarian:
    """
    The Barbarian class represents a warrior from the uncivilized wilds. 
    Barbarians are physically tough, skilled in wilderness survival, and exceptional warriors. 
    However, they have a deep distrust and dislike of magic and those who wield it.

    Attributes:
        level (int): The current level of the barbarian.
        experience_points (int): The total experience points accumulated by the barbarian.
        hit_points (int): The current hit points of the barbarian.
        strength (int): The strength score of the barbarian.
        dexterity (int): The dexterity score of the barbarian.
        constitution (int): The constitution score of the barbarian.
        alignment (str): The alignment of the barbarian, which must be non-lawful.
        weapons (List[str]): The list of weapons the barbarian is proficient with.
        weapon_specialization (Optional[Dict[str, Dict[str, int]]]): The specialization of the barbarian in specific weapons.
        armor_class_bonus (int): Bonus to Armor Class depending on the armor worn.
        base_movement_rate (int): The base movement rate of the barbarian.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    strength: int = 15
    dexterity: int = 14
    constitution: int = 15
    alignment: str = "chaotic neutral"
    weapons: List[str] = field(default_factory=lambda: ["hand axe", "knife", "spear"])
    weapon_specialization: Optional[Dict[str, Dict[str, int]]] = None
    armor_class_bonus: int = field(init=False)
    base_movement_rate: int = 150

    def __post_init__(self) -> None:
        """Initialize attributes that depend on the barbarian's level and abilities."""
        self.set_initial_attributes()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the barbarian based on their level and abilities."""
        self.starting_gold = self.roll_dice(5, 4) * 10
        self.hit_points = self.roll_dice(1, 12)
        self.update_armor_class_bonus()

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def advance_level(self) -> None:
        """Advances the barbarian to the next level, increasing hit points and adjusting abilities."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 12) if self.level <= 11 else 4
        self.update_armor_class_bonus()
        print(f"Level advanced to {self.level}. Hit points: {self.hit_points}")

    def update_armor_class_bonus(self) -> None:
        """Updates the armor class bonus based on the barbarian's dexterity and armor worn."""
        if self.dexterity > 14:
            self.armor_class_bonus = (self.dexterity - 14) * 2
        else:
            self.armor_class_bonus = 0
        print(f"Armor Class Bonus: {self.armor_class_bonus}")

    def detect_magic_or_illusion(self, concentration: bool = False) -> float:
        """
        Detects magic or illusions.

        Args:
            concentration (bool): Whether the barbarian is concentrating to detect an illusion.

        Returns:
            float: The chance to detect magic or illusion as a percentage.
        """
        if concentration:
            chance = min(5 * self.level, 75.0)
            print(f"Chance to detect illusion: {chance}%")
        else:
            chance = min(25 + (5 * self.level), 90.0)
            print(f"Chance to detect magic: {chance}%")
        return chance

    def calculate_attacks_per_round(self) -> int:
        """
        Calculate the number of attacks per round based on the barbarian's level.

        Returns:
            int: The number of attacks per round.
        """
        if self.level <= 5:
            return 1
        elif 6 <= self.level <= 10:
            return 3 // 2
        else:
            return 2

    def perform_attack(self, enemy_hit_dice: int) -> int:
        """
        Simulates an attack on an enemy, calculating the number of attacks and potential damage.

        Args:
            enemy_hit_dice (int): The hit dice of the enemy being attacked.

        Returns:
            int: The total damage inflicted on the enemy.
        """
        attacks = self.calculate_attacks_per_round()
        damage = 0

        for _ in range(attacks):
            damage += self.roll_dice(1, 8)  # Simulating a weapon damage roll

        print(f"Performed {attacks} attacks, total damage: {damage}")
        return damage

    def summon_horde(self) -> int:
        """
        Summons a horde of barbarians to follow the leader. This ability can be used starting at 8th level.

        Returns:
            int: The size of the summoned horde.
        """
        if self.level >= 8:
            base_horde_size = {8: 275, 9: 500, 10: 1000, 11: 1500, 12: 2000}
            horde_size = base_horde_size.get(self.level, 2000 + 500 * (self.level - 12))
            print(f"Horde size: {horde_size}")
            return horde_size
        else:
            print("Horde summoning not available at this level.")
            return 0
