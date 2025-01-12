from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Druid:
    """
    The Druid class represents a follower of Nature, embodying its power and wisdom. Druids are a sub-class
    of clerics, but their devotion lies with the natural world rather than a specific deity. They possess unique
    abilities related to nature, including spellcasting, shape-changing, and woodcraft, and they hold a unique
    position in the druidic hierarchy.

    Attributes:
        level (int): The current level of the druid.
        experience_points (int): The total experience points accumulated by the druid.
        hit_points (int): The current hit points of the druid.
        wisdom (int): The wisdom score of the druid.
        charisma (int): The charisma score of the druid.
        alignment (str): The alignment of the druid, which must be neutral.
        armor (str): The type of armor the druid wears.
        shield (str): The type of shield the druid uses.
        weapons (List[str]): The list of weapons the druid is proficient with.
        spell_slots (Dict[int, int]): The number of spells available to the druid at different levels.
        druid_languages (List[str]): The list of languages known by the druid.
        shape_change_uses (int): The number of times the druid can use the shape-changing ability per day.
    """

    level: int = 1
    experience_points: int = 0
    hit_points: int = field(init=False)
    wisdom: int = 12
    charisma: int = 15
    alignment: str = "neutral"
    armor: str = "leather cuirass"
    shield: str = "small wooden shield"
    weapons: List[str] = field(default_factory=lambda: ["club", "dagger", "scimitar", "spear", "staff", "sling"])
    spell_slots: Dict[int, int] = field(default_factory=dict)
    druid_languages: List[str] = field(default_factory=lambda: ["Druidic"])
    shape_change_uses: int = 3

    def __post_init__(self) -> None:
        """Initialize attributes that depend on the druid's level and wisdom."""
        self.set_initial_attributes()
        self.set_spell_slots()
        self.set_druid_languages()

    def set_initial_attributes(self) -> None:
        """Sets the initial attributes of the druid based on their level and abilities."""
        self.starting_gold = self.roll_dice(3, 6) * 10
        self.hit_points = self.roll_dice(1, 8)

    def roll_dice(self, num_dice: int, num_sides: int) -> int:
        """Simulates rolling dice and returns the total rolled value."""
        from random import randint
        return sum(randint(1, num_sides) for _ in range(num_dice))

    def set_spell_slots(self) -> None:
        """Sets the spell slots available to the druid at different levels."""
        self.spell_slots = {
            1: {1: 2},
            2: {1: 2, 2: 1},
            3: {1: 3, 2: 2, 3: 1},
            4: {1: 4, 2: 2, 3: 2},
            5: {1: 4, 2: 3, 3: 2},
            6: {1: 4, 2: 3, 3: 2, 4: 1},
            7: {1: 4, 2: 4, 3: 3, 4: 1},
            8: {1: 4, 2: 4, 3: 3, 4: 2},
            9: {1: 5, 2: 4, 3: 3, 4: 2, 5: 1},
            10: {1: 5, 2: 4, 3: 3, 4: 3, 5: 2},
            11: {1: 5, 2: 5, 3: 3, 4: 3, 5: 2, 6: 1},
            12: {1: 5, 2: 5, 3: 4, 4: 4, 5: 3, 6: 2, 7: 1},
            13: {1: 6, 2: 5, 3: 5, 4: 5, 5: 4, 6: 3, 7: 2},
            14: {1: 6, 2: 6, 3: 6, 4: 6, 5: 5, 6: 4, 7: 3},
            15: {1: 6, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6},
        }

    def set_druid_languages(self) -> None:
        """Sets the languages known by the druid based on their level."""
        language_list = [
            "Atomie", "Centaur", "Dryad", "Elvish", "Faun", "Gnome", "Green Dragon",
            "Fairy Dragon", "Hill Giant", "Lizard Man", "Manticore", "Nixie", "Pixie",
            "Sprite", "Tree Man"
        ]
        for i in range(3, self.level + 1):
            if i - 3 < len(language_list):
                self.druid_languages.append(language_list[i - 3])

    def advance_level(self) -> None:
        """Advances the druid to the next level, increasing hit points and adjusting abilities."""
        self.level += 1
        self.hit_points += self.roll_dice(1, 8) if self.level <= 15 else 0

        # Potentially adjust spell slots and druid abilities if level thresholds are crossed
        if self.level >= 1:
            print(f"Updated spell slots: {self.spell_slots.get(self.level, {})}")

        if self.level >= 3:
            print(f"New language acquired: {self.druid_languages[-1]}")

    def shape_change(self, creature_type: str) -> str:
        """
        Changes the druid's form into a natural animal. This ability can be used up to three times per day.

        Args:
            creature_type (str): The type of natural animal to change into.

        Returns:
            str: Description of the shape change or error if conditions aren't met.
        """
        if self.shape_change_uses <= 0:
            return "You have exhausted your shape-changing ability for today."

        self.shape_change_uses -= 1

        # Simulate the healing effect that comes with shape changing
        healing_percentage = self.roll_dice(1, 6) * 10
        healed_hit_points = int(self.hit_points * (healing_percentage / 100))
        self.hit_points += healed_hit_points

        return (
            f"Shape changed into {creature_type}. Healed {healed_hit_points} hit points."
            f" {self.shape_change_uses} uses of shape-changing remaining today."
        )

    def create_magic_item(self, item_type: str) -> Optional[str]:
        """
        Creates a magic item if the druid's level is sufficient.

        Args:
            item_type (str): The type of magic item to create.

        Returns:
            Optional[str]: The created magic item, if successful; otherwise, None.
        """
        if self.level < 7:
            print("Druid level too low to create magic items.")
            return None

        print(f"{item_type} created successfully.")
        return f"Magic {item_type}"

    def enter_elemental_plane(self, plane: str) -> str:
        """
        Allows the druid to enter an elemental plane of existence based on their level.

        Args:
            plane (str): The elemental plane to enter.

        Returns:
            str: Description of the journey or an error if conditions aren't met.
        """
        plane_access = {
            17: "Elemental earth",
            18: "Elemental fire",
            19: "Elemental water",
            20: "Elemental air",
            21: "All meta-elemental planes: smoke, ice, ooze, magma",
            22: "Plane of shadow",
            23: "Any inner plane, alternate material planes, Concordance"
        }

        if self.level < 17:
            return "Druid level too low to enter elemental planes."

        if plane != plane_access.get(self.level, ""):
            return f"At level {self.level}, you can only enter the {plane_access[self.level]}."

        return f"Entered the {plane} plane successfully."

    def conjure_elemental(self, element: str) -> str:
        """
        Conjures an elemental or other creature from the elemental planes.

        Args:
            element (str): The elemental type to conjure.

        Returns:
            str: Description of the conjured elemental or error if conditions aren't met.
        """
        if self.level < 17:
            return "Druid level too low to conjure elementals."

        possible_elementals = {
            17: "Water elemental",
            18: "Air elemental",
            19: "Magma or Smoke meta-elemental",
            20: "Ice or Ooze meta-elemental"
        }

        if self.level < 23 and element not in possible_elementals.get(self.level, ""):
            return f"At level {self.level}, you can only conjure {possible_elementals[self.level]}."

        return f"Conjured a {element} elemental successfully."
