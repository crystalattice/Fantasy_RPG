from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class Ranger:
    """
    The Ranger class represents a skilled warrior who specializes in woodcraft and tracking,
    often serving as a protector of civilization from the dangers of the wilderness.

    Attributes:
        level (int): The current level of the ranger.
        experience_points (int): The total experience points accumulated by the ranger.
        hit_points (int): The current hit points of the ranger.
        strength (int): The strength score of the ranger.
        intelligence (int): The intelligence score of the ranger.
        wisdom (int): The wisdom score of the ranger.
        constitution (int): The constitution score of the ranger.
        alignment (str): The alignment of the ranger, which must be good.
        weapons (List[str]): The list of weapons the ranger is proficient with.
        weapon_specialization (Optional[Dict[str, Dict[str, int]]]): The specialization of the ranger in specific weapons.
        tracking_skill_level (int): The level of proficiency the ranger has in tracking.
        followers (Optional[List[str]]): A list of followers the ranger attracts at higher levels.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    strength: int = 13
    intelligence: int = 13
    wisdom: int = 14
    constitution: int = 14
    alignment: str = "neutral good"
    weapons: List[str] = field(default_factory=lambda: ["longbow", "dagger", "longsword"])
    weapon_specialization: Optional[Dict[str, Dict[str, int]]] = None
    tracking_skill_level: int = 1
    followers: Optional[List[str]] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Initialize attributes that depend on the ranger's level and abilities."""
        self.set_initial_attributes()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the ranger based on their level and abilities."""
        self.starting_gold = self.roll_dice(5, 4) * 10
        self.hit_points = self.roll_dice(2, 8)
        self.update_tracking_skill()

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def advance_level(self) -> None:
        """Advances the ranger to the next level, increasing hit points and adjusting abilities."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 8) if self.level <= 12 else 2
        self.update_tracking_skill()
        print(f"Level advanced to {self.level}. Hit points: {self.hit_points}")

    def update_tracking_skill(self) -> None:
        """Updates the tracking skill level based on the ranger's experience level."""
        self.tracking_skill_level = self.level
        print(f"Tracking skill level: {self.tracking_skill_level}")

    def calculate_attacks_per_round(self) -> int:
        """
        Calculate the number of attacks per round based on the ranger's level.

        Returns:
            int: The number of attacks per round.
        """
        if self.level <= 7:
            return 1
        elif 8 <= self.level <= 14:
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

    def detect_giants_or_humanoids_bonus(self, creature_type: str) -> int:
        """
        Provides a combat bonus when fighting giants or humanoid creatures.

        Args:
            creature_type (str): The type of creature being fought (e.g., "giant", "orc").

        Returns:
            int: The bonus damage against the creature type.
        """
        giants_and_humanoids = [
            "bugbear", "cyclops", "ettin", "gnoll", "goblin", "hobgoblin", "kobold", "ogre",
            "orc", "troll", "giant"
        ]
        if creature_type in giants_and_humanoids:
            bonus = self.level
            print(f"Combat bonus against {creature_type}: +{bonus} damage")
            return bonus
        return 0

    def attempt_tracking(self, difficulty: int) -> bool:
        """
        Attempts to track a target based on the ranger's tracking skill.

        Args:
            difficulty (int): The difficulty level of the tracking attempt.

        Returns:
            bool: Whether the tracking attempt was successful.
        """
        success_chance = 50 + (self.tracking_skill_level * 5) - difficulty
        from random import randint
        roll = randint(1, 100)
        success = roll <= success_chance
        print(f"Tracking attempt: {'Success' if success else 'Failure'} (rolled {roll} vs {success_chance}%)")
        return success

    def summon_followers(self) -> None:
        """Summons a group of followers to join the ranger at 10th level or higher."""
        if self.level >= 10:
            from random import choice, randint
            potential_followers = [
                "Human cleric", "Human druid", "Human fighter", "Human ranger", "Human mage",
                "Dwarf fighter", "Elf fighter", "Gnome fighter", "Halfling fighter", "Black bear",
                "Brown bear", "Blink dog", "Centaur", "Hippogriff", "Pegasus", "Pseudo-dragon"
            ]
            num_followers = randint(2, 12)
            self.followers = [choice(potential_followers) for _ in range(num_followers)]
            print(f"Followers summoned: {self.followers}")
        else:
            print("Summoning followers is not available at this level.")
