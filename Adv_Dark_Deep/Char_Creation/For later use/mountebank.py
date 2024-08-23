from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Mountebank:
    """
    The Mountebank is a sub-class of the thief, specializing in deception, verbal patter,
    and minor magic to con and swindle others. They rely on their charisma and dexterity
    to manipulate and deceive, rather than brute force.

    Attributes:
        level (int): The current level of the mountebank.
        experience_points (int): The total experience points accumulated by the mountebank.
        hit_points (int): The current hit points of the mountebank.
        dexterity (int): The dexterity score of the mountebank.
        charisma (int): The charisma score of the mountebank.
        skills (Dict[str, int]): The mountebank's skills and their current proficiency percentages.
        spells (Dict[int, List[str]]): The spells the mountebank has learned by level.
        alchemy (Dict[str, int]): The mountebank's alchemy skills for creating medicines and potions.
        armor (str): The type of armor the mountebank is wearing.
        weapon_proficiency (List[str]): List of weapons the mountebank is proficient with.
        gold (int): The amount of gold the mountebank possesses.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    dexterity: int = 9
    charisma: int = 12
    skills: Dict[str, int] = field(default_factory=lambda: {
        "Disguise": 0,
        "Pick Pockets": 30,
        "Sleight of Hand": 35,
        "Juggling": 25,
        "Knife Throwing": 0,  # ±0, +1
        "Verbal Patter": 40,  # Assure, Attend, Question
    })
    spells: Dict[int, List[str]] = field(default_factory=lambda: {1: []})
    alchemy: Dict[str, int] = field(default_factory=lambda: {
        "Medicine": 20,
        "Magic Potion": 0
    })
    armor: str = "leather"
    weapon_proficiency: List[str] = field(default_factory=lambda: ["dagger", "short sword", "quarterstaff", "sling"])
    gold: int = field(init=False)

    def __post_init__(self) -> None:
        """Initialize hit points and starting gold based on level."""
        self.set_initial_attributes()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the mountebank based on their level."""
        self.gold = self.roll_dice(2, 6) * 10
        self.hit_points = self.roll_dice(1, 6)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def advance_level(self) -> None:
        """Advances the mountebank to the next level, increasing hit points, skills, and spellcasting ability."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 6) if self.level <= 12 else 2
        self.update_skills()
        self.update_alchemy()

    def update_skills(self) -> None:
        """Updates the mountebank's skills based on their level."""
        skill_progression = {
            2: {"Pick Pockets": 35, "Sleight of Hand": 40, "Juggling": 30, "Verbal Patter": 45},
            3: {"Pick Pockets": 40, "Sleight of Hand": 45, "Juggling": 35, "Verbal Patter": 50},
            4: {"Pick Pockets": 45, "Sleight of Hand": 50, "Juggling": 40, "Verbal Patter": 55},
            # Continue this pattern up to level 17 as defined in the source material.
        }
        if self.level in skill_progression:
            for skill, value in skill_progression[self.level].items():
                self.skills[skill] = value

    def update_alchemy(self) -> None:
        """Updates the mountebank's alchemy skills based on their level."""
        alchemy_progression = {
            2: {"Medicine": 25, "Magic Potion": 0},
            3: {"Medicine": 30, "Magic Potion": 0},
            4: {"Medicine": 35, "Magic Potion": 10},
            # Continue this pattern up to level 17 as defined in the source material.
        }
        if self.level in alchemy_progression:
            for skill, value in alchemy_progression[self.level].items():
                self.alchemy[skill] = value

    def perform_disguise(self, target: str, disguise_type: str) -> str:
        """
        Attempts to disguise the mountebank as another person or being.

        Args:
            target (str): The target of the disguise.
            disguise_type (str): The type of disguise (race, gender, class, etc.).

        Returns:
            str: The result of the disguise attempt.
        """
        from random import randint
        base_chance = 98  # Base success chance
        modifiers = {
            "race": 2,
            "gender": 2,
            "class": 2
        }
        modifier = modifiers.get(disguise_type, 0)
        observer_int_wis = randint(10, 36)  # Simulate observer's INT + WIS
        observer_modifier = max(min((observer_int_wis - 19) // 3, 6), -7)
        chance_of_success = base_chance - modifier - observer_modifier

        if randint(1, 100) <= chance_of_success:
            return f"Successfully disguised as {target} ({disguise_type})."
        return f"Failed to disguise as {target} ({disguise_type})."

    def perform_verbal_patter(self, patter_type: str) -> str:
        """
        Attempts to use verbal patter to influence the target.

        Args:
            patter_type (str): The type of verbal patter (Assure, Attend, Befuddle, etc.).

        Returns:
            str: The result of the verbal patter attempt.
        """
        from random import randint
        base_chance = self.skills["Verbal Patter"]
        charisma_bonus = (self.charisma - 15) * 5 if self.charisma >= 16 else 0
        chance_of_success = base_chance + charisma_bonus

        if randint(1, 100) <= chance_of_success:
            return f"Successfully used {patter_type} patter."
        return f"Failed to use {patter_type} patter."

    def create_potion(self, potion_type: str) -> str:
        """
        Attempts to create a potion using alchemy.

        Args:
            potion_type (str): The type of potion (medicine or magic potion).

        Returns:
            str: The result of the potion creation attempt.
        """
        from random import randint
        chance_of_success = self.alchemy[potion_type]

        if randint(1, 100) <= chance_of_success:
            return f"Successfully created a {potion_type}."
        return f"Failed to create a {potion_type}. It might be snake oil."

    def cast_spell(self, spell_name: str) -> str:
        """
        Attempts to cast a spell from the mountebank's spellbook.

        Args:
            spell_name (str): The name of the spell.

        Returns:
            str: The result of the spellcasting attempt.
        """
        if spell_name in self.spells.get(self.level, []):
            return f"Successfully cast {spell_name}."
        return f"Failed to cast {spell_name}. Spell not available or level too low."
