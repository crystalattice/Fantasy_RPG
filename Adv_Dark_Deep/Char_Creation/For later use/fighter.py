from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Fighter:
    """
    The Fighter class represents a warrior skilled in combat, capable of using a wide variety of weapons and armor.
    Fighters are versatile combatants, ranging from mercenaries to knights, and can specialize in specific weapons
    to gain significant combat advantages.

    Attributes:
        level (int): The current level of the fighter.
        experience_points (int): The total experience points accumulated by the fighter.
        hit_points (int): The current hit points of the fighter.
        strength (int): The strength score of the fighter.
        constitution (int): The constitution score of the fighter.
        alignment (str): The alignment of the fighter, which can be of any type.
        weapons (List[str]): The list of weapons the fighter is proficient with.
        weapon_specialization (Optional[Dict[str, Dict[str, int]]]): The specialization of the fighter in a specific weapon.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    strength: int = 9
    constitution: int = 7
    alignment: str = "neutral"
    weapons: List[str] = field(default_factory=lambda: ["long sword", "bow", "axe"])
    weapon_specialization: Optional[Dict[str, Dict[str, int]]] = None

    def __post_init__(self) -> None:
        """Initialize attributes that depend on the fighter's level and abilities."""
        self.set_initial_attributes()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the fighter based on their level and abilities."""
        self.starting_gold = self.roll_dice(5, 4) * 10
        self.hit_points = self.roll_dice(1, 10)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def exceptional_strength(self) -> Optional[int]:
        """
        If the fighter has a strength score of 18, roll percentile dice for exceptional strength.
        Returns:
            Optional[int]: The percentile score if the fighter has 18 strength; otherwise, None.
        """
        if self.strength == 18:
            from random import randint
            exceptional_score = randint(1, 100)
            print(f"Exceptional strength: 18/{exceptional_score}")
            return exceptional_score
        print("No exceptional strength applicable.")
        return None

    def advance_level(self) -> None:
        """Advances the fighter to the next level, increasing hit points and adjusting abilities."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 10) if self.level <= 11 else 3
        print(f"Level advanced to {self.level}. Hit points: {self.hit_points}")

    def weapon_specialize(self, weapon: str) -> None:
        """
        Allows the fighter to specialize in a weapon, gaining bonuses to hit and damage.

        Args:
            weapon (str): The specific weapon to specialize in.
        """
        if not self.weapon_specialization:
            self.weapon_specialization = {}

        if weapon in self.weapon_specialization:
            print(f"Already specialized in {weapon}.")
            return

        if self.level < 1:
            print("Weapon specialization not available at this level.")
            return

        self.weapon_specialization[weapon] = {"to_hit": 1, "damage": 2}
        print(f"Weapon specialization in {weapon} granted: +1 to hit, +2 to damage.")

    def calculate_attacks_per_round(self) -> int:
        """
        Calculate the number of attacks per round based on the fighter's level.

        Returns:
            int: The number of attacks per round.
        """
        if self.level <= 6:
            return 1
        elif 7 <= self.level <= 12:
            return 3 // 2
        else:
            return 2

    def gain_experience_bonus(self) -> None:
        """
        Grants an experience point bonus if the fighter's strength is 15 or higher.
        """
        if self.strength >= 15:
            bonus = int(self.experience_points * 0.10)
            self.experience_points += bonus
            print(f"Experience bonus applied: {bonus} points.")
        else:
            print("No experience bonus applicable.")

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
