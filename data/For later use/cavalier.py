from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Cavalier:
    """
    The Cavalier class represents a knight-like character who is dedicated to a noble cause
    or individual. Cavaliers are known for their combat prowess, strict code of chivalry, and
    exceptional horsemanship.

    Attributes:
        level (int): The current level of the cavalier.
        experience_points (int): The total experience points accumulated by the cavalier.
        hit_points (int): The current hit points of the cavalier.
        alignment (str): The alignment of the cavalier, which must be lawful.
        social_class (str): The social class of the cavalier (lower, middle, or upper upper class).
        starting_gold (int): The amount of gold the cavalier starts with.
        armor (str): The type of armor the cavalier wears.
        shield (str): The type of shield the cavalier uses.
        weapons (List[str]): The list of weapons the cavalier is proficient with.
        mount (str): The type of mount the cavalier rides.
        retainers (List[Dict[str, Optional[str]]]): The retainers under the cavalier's command.
        horsemanship_abilities (Dict[int, str]): Special horsemanship abilities the cavalier gains at specific levels.
        to_hit_bonuses (Dict[int, Dict[str, int]]): Bonuses to hit with certain weapons based on the cavalier's level.
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

    def __post_init__(self) -> None:
        """Initialize attributes that depend on social class and level."""
        self.set_initial_attributes()
        self.set_horsemanship_abilities()
        self.set_to_hit_bonuses()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the cavalier based on social class."""
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
            self.starting_gold = self.roll_dice(3, 6) * 10
            self.armor = "plate armor and jousting plate armor"
            self.shield = "large shield"
            self.weapons = ["dagger", "mace", "lance", "long sword or broad sword"]
            self.mount = "heavy warhorse with leather barding"

        self.hit_points = self.roll_dice(1, 10)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def set_horsemanship_abilities(self) -> None:
        """Sets the horsemanship abilities based on cavalier level."""
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
        }

    def advance_level(self) -> None:
        """Advances the cavalier to the next level, increasing hit points and adjusting abilities."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 10) if self.level <= 10 else 3

        # Potentially adjust horsemanship abilities or to-hit bonuses if level thresholds are crossed
        if self.level in self.horsemanship_abilities:
            print(f"Gained horsemanship ability: {self.horsemanship_abilities[self.level]}")

        if self.level in self.to_hit_bonuses:
            print(f"Gained to-hit bonus with: {self.to_hit_bonuses[self.level]}")

    def add_retainer(self, retainer_level: int, retainer_role: Optional[str] = None) -> None:
        """
        Adds a retainer to the cavalier's retinue.

        Args:
            retainer_level (int): The level of the retainer.
            retainer_role (Optional[str]): The role of the retainer (e.g., herald, guard).
        """
        self.retainers.append({"level": retainer_level, "role": retainer_role})
        print(f"Added retainer: level {retainer_level}, role {retainer_role}")
