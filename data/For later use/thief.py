from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Thief:
    """
    The Thief class represents a character adept in stealth, observation, and 
    various skills related to thievery and stealth. Thieves are versatile characters 
    capable of backstabbing, picking locks, disarming traps, and more.

    Attributes:
        level (int): The current level of the thief.
        experience_points (int): The total experience points accumulated by the thief.
        hit_points (int): The current hit points of the thief.
        dexterity (int): The dexterity score of the thief.
        skills (Dict[str, int]): The thief's skills and their current proficiency percentages.
        armor (str): The type of armor the thief is wearing.
        weapon_proficiency (List[str]): List of weapons the thief is proficient with.
        gold (int): The amount of gold the thief possesses.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    dexterity: int = 9
    skills: Dict[str, int] = field(default_factory=lambda: {
        "Pick Pockets": 30,
        "Open Locks": 25,
        "Find/Remove Traps": 20,
        "Move Silently": 15,
        "Hide in Shadows": 10,
        "Listen at Doors": 10,
        "Climb Walls": 85,
        "Read Languages": 0
    })
    armor: str = "leather"
    weapon_proficiency: List[str] = field(default_factory=lambda: ["short bow", "dagger", "long sword", "short sword"])
    gold: int = field(init=False)

    def __post_init__(self) -> None:
        """Initialize hit points and starting gold based on level."""
        self.set_initial_attributes()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the thief based on their level."""
        self.gold = self.roll_dice(2, 6) * 10
        self.hit_points = self.roll_dice(1, 6)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def advance_level(self) -> None:
        """Advances the thief to the next level, increasing hit points and skill percentages."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 6) if self.level <= 12 else 2
        self.update_skills()

    def update_skills(self) -> None:
        """Updates the thief's skills based on their level."""
        skill_progression = {
            2: {"Pick Pockets": 35, "Open Locks": 29, "Find/Remove Traps": 25, "Move Silently": 21,
                "Hide in Shadows": 15, "Listen at Doors": 10, "Climb Walls": 86},
            3: {"Pick Pockets": 40, "Open Locks": 33, "Find/Remove Traps": 30, "Move Silently": 27,
                "Hide in Shadows": 20, "Listen at Doors": 15, "Climb Walls": 87},
            # Continue this pattern up to level 17 as defined in the source material.
        }
        if self.level in skill_progression:
            for skill, value in skill_progression[self.level].items():
                self.skills[skill] = value

    def backstab(self, target: str) -> str:
        """
        Performs a backstab on a target, dealing extra damage if successful.

        Args:
            target (str): The name of the target to backstab.

        Returns:
            str: The result of the backstab attempt.
        """
        from random import randint
        if randint(1, 20) + 4 >= 10:  # Simplified for this example
            damage_multiplier = min((self.level // 4) + 2, 6)
            return f"Backstab successful! Damage to {target} multiplied by {damage_multiplier}."
        return f"Backstab attempt failed against {target}."

    def pick_pocket(self, target: str) -> str:
        """
        Attempts to pick the pocket of a target.

        Args:
            target (str): The name of the target to pickpocket.

        Returns:
            str: The result of the pickpocket attempt.
        """
        from random import randint
        chance = self.skills["Pick Pockets"] - (5 * self.level)
        if randint(1, 100) <= chance:
            return f"Successfully pickpocketed {target}."
        return f"Pickpocket attempt failed against {target}."

    def read_scroll(self, scroll: str) -> str:
        """
        Attempts to read a magical scroll.

        Args:
            scroll (str): The name of the scroll.

        Returns:
            str: The result of the scroll reading attempt.
        """
        if self.level >= 10:
            from random import randint
            if randint(1, 100) <= 75:  # 25% chance to fail
                if randint(1, 100) <= 10 * scroll.count(" "):  # Simplified spell reversal chance
                    return f"Scroll {scroll} misfired! Effects reversed!"
                return f"Successfully read scroll {scroll}."
            return f"Failed to read scroll {scroll}."
        return f"Cannot read scroll {scroll} at level {self.level}."


@dataclass
class ThiefAcrobat(Thief):
    """
    The ThiefAcrobat class represents a thief who specializes in acrobatics and physical prowess, 
    gaining additional skills such as tightrope walking, pole vaulting, and tumbling.

    Attributes:
        acrobat_skills (Dict[str, int]): Additional acrobatic skills.
        encumbrance_limit (int): The maximum encumbrance the thief-acrobat can carry while performing acrobatics.
    """

    acrobat_skills: Dict[str, int] = field(default_factory=lambda: {
        "Tightrope Walking": 75,
        "Pole Vaulting": 9,  # feet
        "High Jumping": 4,  # feet
        "Standing Jump": 5,  # feet
        "Running Jump": 9,  # feet
        "Tumbling Attack": 1,  # Bonus
        "Tumbling Evasion": 10,  # %
        "Avoid Falling Damage": 25  # % chance to avoid damage from falls 0-10 feet
    })
    encumbrance_limit: int = 45

    def advance_level(self) -> None:
        """Advances the thief-acrobat to the next level, increasing hit points and acrobat skills."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 6) if self.level <= 12 else 2
        self.update_acrobat_skills()

    def update_acrobat_skills(self) -> None:
        """Updates the thief-acrobat's skills based on their level."""
        acrobat_skill_progression = {
            7: {"Tightrope Walking": 80, "Pole Vaulting": 9.5, "High Jumping": 4.25, "Standing Jump": 5.5,
                "Running Jump": 9.5, "Tumbling Attack": 1, "Tumbling Evasion": 15, "Avoid Falling Damage": 50},
            8: {"Tightrope Walking": 85, "Pole Vaulting": 10, "High Jumping": 4.5, "Standing Jump": 6,
                "Running Jump": 10, "Tumbling Attack": 1, "Tumbling Evasion": 20, "Avoid Falling Damage": 75},
            # Continue this pattern up to level 23 as defined in the source material.
        }
        if self.level in acrobat_skill_progression:
            for skill, value in acrobat_skill_progression[self.level].items():
                self.acrobat_skills[skill] = value

    def perform_tightrope_walk(self) -> str:
        """
        Attempts to walk on a tightrope.

        Returns:
            str: The result of the tightrope walking attempt.
        """
        from random import randint
        if randint(1, 100) <= self.acrobat_skills["Tightrope Walking"]:
            return "Successfully walked the tightrope."
        return "Failed to walk the tightrope and fell."

    def perform_pole_vault(self) -> str:
        """
        Attempts to pole vault over an obstacle.

        Returns:
            str: The result of the pole vaulting attempt.
        """
        from random import randint
        if randint(1, 100) <= self.acrobat_skills["Pole Vaulting"] * 10:
            return f"Successfully pole vaulted {self.acrobat_skills['Pole Vaulting']} feet."
        return "Failed the pole vault attempt."

    def perform_tumbling_attack(self) -> str:
        """
        Attempts a tumbling attack.

        Returns:
            str: The result of the tumbling attack attempt.
        """
        from random import randint
        if randint(1, 20) + self.acrobat_skills["Tumbling Attack"] >= 10:  # Simplified for this example
            return "Tumbling attack successful!"
        return "Tumbling attack failed."

    def avoid_fall_damage(self, fall_distance: int) -> str:
        """
        Attempts to avoid fall damage based on fall distance.

        Args:
            fall_distance (int): The distance fallen in feet.

        Returns:
            str: The result of the fall damage avoidance attempt.
        """
        if fall_distance <= 10:
            chance_to_avoid = self.acrobat_skills["Avoid Falling Damage"]
        elif fall_distance <= 20:
            chance_to_avoid = self.acrobat_skills["Avoid Falling Damage"] // 2
        else:
            chance_to_avoid = 0

        from random import randint
        if randint(1, 100) <= chance_to_avoid:
            return f"Successfully avoided damage from a fall of {fall_distance} feet."
        return f"Failed to avoid fall damage from {fall_distance} feet."
