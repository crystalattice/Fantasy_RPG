from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Paladin:
    """
    The Paladin class represents a knight dedicated to the cause of lawful good, inspired by unwavering faith.
    Paladins are paragons of chivalry and martial prowess, with special abilities related to their devotion.

    Attributes:
        level (int): The current level of the paladin.
        experience_points (int): The total experience points accumulated by the paladin.
        hit_points (int): The current hit points of the paladin.
        alignment (str): The alignment of the paladin, which must be lawful good.
        social_class (str): The social class of the paladin (lower, middle, or upper upper class).
        starting_gold (int): The amount of gold the paladin starts with.
        armor (str): The type of armor the paladin wears.
        shield (str): The type of shield the paladin uses.
        weapons (List[str]): The list of weapons the paladin is proficient with.
        mount (str): The type of mount the paladin rides.
        retainers (List[Dict[str, Optional[str]]]): The retainers under the paladin's command.
        horsemanship_abilities (Dict[int, str]): Special horsemanship abilities the paladin gains at specific levels.
        to_hit_bonuses (Dict[int, Dict[str, int]]): Bonuses to hit with certain weapons based on the paladin's level.
        spell_slots (Dict[int, int]): The number of spells available to the paladin at different levels.
        disease_cures_per_week (int): The number of times per week the paladin can cure disease.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    alignment: str = field(default="lawful good")
    social_class: str = field(default="lower upper")
    starting_gold: int = field(init=False)
    armor: str = field(init=False)
    shield: str = field(init=False)
    weapons: List[str] = field(default_factory=list)
    mount: str = field(init=False)
    retainers: List[Dict[str, Optional[str]]] = field(default_factory=list)
    horsemanship_abilities: Dict[int, str] = field(default_factory=dict)
    to_hit_bonuses: Dict[int, Dict[str, int]] = field(default_factory=dict)
    spell_slots: Dict[int, int] = field(default_factory=dict)
    disease_cures_per_week: int = 1

    def __post_init__(self) -> None:
        """Initialize attributes that depend on social class and level."""
        self.set_initial_attributes()
        self.set_horsemanship_abilities()
        self.set_to_hit_bonuses()
        self.set_spell_slots()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the paladin based on social class."""
        if self.social_class == "lower upper":
            self.starting_gold = self.roll_dice(1, 2) + 6 * 10
            self.armor = "plated mail"
            self.shield = "large shield"
            self.weapons = ["dagger", "lance", "long sword or broad sword"]
            self.mount = "medium warhorse"
        elif self.social_class == "middle upper":
            self.starting_gold = self.roll_dice(1, 12) * 10
            self.armor = "plate armor"
            self.shield = "large shield"
            self.weapons = ["dagger", "lance", "long sword or broad sword"]
            self.mount = "heavy warhorse"
        elif self.social_class == "upper upper":
            self.starting_gold = self.roll_dice(2, 6) * 10
            self.armor = "jousting plate and full plate armor"
            self.shield = "large shield"
            self.weapons = ["dagger", "mace", "lance", "long sword or broad sword"]
            self.mount = "heavy warhorse with leather barding"

        self.hit_points = self.roll_dice(1, 10)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def set_horsemanship_abilities(self) -> None:
        """Sets the horsemanship abilities based on paladin level."""
        self.horsemanship_abilities = {
            3: "Leap into the saddle within 1 segment",
            4: "Good-aligned female elf cavaliers may use unicorns as steeds",
            5: "Urge steed to go 20'/round faster for up to 1 hour",
            7: "Use a pegasus as a mount",
            9: "Use a hippogriff as a mount",
            11: "Use a griffon as a mount",
        }

    def set_to_hit_bonuses(self) -> None:
        """Sets the bonuses 'to hit' based on level and weapon."""
        self.to_hit_bonuses = {
            1: {"lance (mounted)": 1},
            3: {"broad sword, long sword, or scimitar": 1},
            5: {"horseman’s mace, horseman’s flail, or military pick": 1},
            7: {"lance (mounted)": 2},
            9: {"weapon chosen at 3rd level": 2},
            11: {"weapon chosen at 5th level": 2},
            13: {"lance (mounted)": 3},
            15: {"weapon chosen at 3rd level": 3},
            17: {"weapon chosen at 5th level": 3},
        }

    def set_spell_slots(self) -> None:
        """Sets the spell slots available to the paladin at different levels."""
        self.spell_slots = {
            9: {1: 1},
            10: {1: 2},
            11: {1: 2, 2: 1},
            12: {1: 2, 2: 2},
            13: {1: 2, 2: 2, 3: 1},
            14: {1: 3, 2: 2, 3: 1},
            15: {1: 3, 2: 2, 3: 1, 4: 1},
            16: {1: 3, 2: 3, 3: 1, 4: 1},
            17: {1: 3, 2: 3, 3: 2, 4: 1},
            18: {1: 3, 2: 3, 3: 3, 4: 1},
            19: {1: 3, 2: 3, 3: 3, 4: 2},
            20: {1: 3, 2: 3, 3: 3, 4: 3},
        }

    def advance_level(self) -> None:
        """Advances the paladin to the next level, increasing hit points and adjusting abilities."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 10) if self.level <= 10 else 3

        # Potentially adjust horsemanship abilities, to-hit bonuses, or spell slots if level thresholds are crossed
        if self.level in self.horsemanship_abilities:
            print(f"Gained horsemanship ability: {self.horsemanship_abilities[self.level]}")

        if self.level in self.to_hit_bonuses:
            print(f"Gained to-hit bonus with: {self.to_hit_bonuses[self.level]}")

        if self.level >= 9:
            print(f"Gained spell slots: {self.spell_slots.get(self.level, {})}")

    def add_retainer(self, retainer_level: int, retainer_role: Optional[str] = None) -> None:
        """
        Adds a retainer to the paladin's retinue.

        Args:
            retainer_level (int): The level of the retainer.
            retainer_role (Optional[str]): The role of the retainer (e.g., herald, guard).
        """
        self.retainers.append({"level": retainer_level, "role": retainer_role})
        print(f"Added retainer: level {retainer_level}, role {retainer_role}")

    def cure_disease(self) -> None:
        """Cures disease, with the number of uses per week increasing as the paladin advances in level."""
        print(f"Used cure disease. Remaining uses this week: {self.disease_cures_per_week}")
        self.disease_cures_per_week -= 1
        if self.disease_cures_per_week < 0:
            self.disease_cures_per_week = 0
