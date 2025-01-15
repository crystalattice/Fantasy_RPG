from typing import Dict, Tuple, List
import random


class Dwarf:
    """
    Base class for all dwarf types, encapsulating common traits and abilities.
    """

    def __init__(self, gender: str, constitution: int, charisma: int):
        self.gender = gender
        self.constitution = constitution + 1  # +1 bonus to Constitution
        self.charisma = min(charisma - 1, 16)  # -1 penalty to Charisma, max 16 for non-dwarves
        self.saving_throw_bonus = self.get_saving_throw_bonus()
        self.detect_abilities = self.get_detect_abilities()
        self.giant_defense_bonus = -4  # All dwarves have a -4 to be hit by giant-type creatures
        self.languages = self.get_languages()
        self.infravision_range = self.get_infravision_range()

    def get_saving_throw_bonus(self) -> int:
        """
        Determines the saving throw bonus based on Constitution.
        """
        bonus_table = {
            (4, 6): 1,
            (7, 10): 2,
            (11, 13): 3,
            (14, 17): 4,
            (18, float('inf')): 5
        }
        for (low, high), bonus in bonus_table.items():
            if low <= self.constitution <= high:
                return bonus
        return 0

    def get_detect_abilities(self) -> Dict[str, int]:
        """
        Returns the detection abilities related to stonework and underground features.
        """
        return {
            "Detect sloping passages and tunnels": 75,
            "Detect new construction": 75,
            "Detect moving, shifting, etc., walls and rooms": 67,
            "Detect pit traps, falling blocks, etc.": 50,
            "Sense approximate depth": 50  # Chance of sensing depth below surface
        }

    def roll_dice(self, dice: str) -> int:
        """
        Rolls a specified number of dice in the format 'XdY' where X is the number of dice
        and Y is the number of sides on each die.

        Args:
            dice (str): A string representing the dice to roll, e.g., '2d8' or '1d12'.

        Returns:
            int: The total result of the dice rolls.
        """
        num, die = map(int, dice.split('d'))
        return sum(random.randint(1, die) for _ in range(num))

    def determine_height(self, roll: int, height_table: Dict[str, List[Tuple[Tuple[int, int], str]]]) -> int:
        """
        Determines the height of a Dwarf based on gender and a percentile roll.

        Args:
            roll (int): The percentile roll used to determine height.
            height_table (Dict[str, List[Tuple[Tuple[int, int], str]]]): The height table for the dwarf type.

        Returns:
            int: The height of the dwarf in inches.
        """
        for range_tuple, formula in height_table[self.gender]:
            if range_tuple[0] <= roll <= range_tuple[1]:
                if 'd' in formula:
                    base_height, dice = formula.split(' - ')[0], formula.split(' - ')[1] if '-' in formula else \
                    formula.split(' + ')[1]
                    base_height = int(base_height)
                    height_modifier = self.roll_dice(dice)
                    return base_height - height_modifier if '-' in formula else base_height + height_modifier
                else:
                    return int(formula)
        raise ValueError("Invalid roll or gender provided.")

    def determine_weight(self, roll: int, weight_table: Dict[str, List[Tuple[Tuple[int, int], str]]]) -> int:
        """
        Determines the weight of a Dwarf based on gender and a percentile roll.

        Args:
            roll (int): The percentile roll used to determine weight.
            weight_table (Dict[str, List[Tuple[Tuple[int, int], str]]]): The weight table for the dwarf type.

        Returns:
            int: The weight of the dwarf in pounds.
        """
        for range_tuple, formula in weight_table[self.gender]:
            if range_tuple[0] <= roll <= range_tuple[1]:
                if 'd' in formula:
                    if ' - ' in formula:
                        base_weight_str, dice = formula.split(' - ')
                        base_weight = int(base_weight_str)
                        weight_modifier = self.roll_dice(dice)
                        return base_weight - weight_modifier
                    elif ' + ' in formula:
                        base_weight_str, dice = formula.split(' + ')
                        base_weight = int(base_weight_str)
                        weight_modifier = self.roll_dice(dice)
                        return base_weight + weight_modifier
                else:
                    return int(formula)
        raise ValueError("Invalid roll or gender provided.")

    def get_languages(self) -> List[str]:
        """
        Returns the languages known by the dwarf. To be overridden by subclasses.

        Returns:
            List[str]: A list of languages known by the dwarf.
        """
        return []

    def get_infravision_range(self) -> int:
        """
        Returns the infravision range of the dwarf in feet. To be overridden by subclasses.

        Returns:
            int: The infravision range in feet.
        """
        return 0


class GreyDwarf(Dwarf):
    """
    Class for Grey Dwarves, a subclass of Dwarf with additional traits and abilities.
    """

    def __init__(self, gender: str, constitution: int, charisma: int):
        super().__init__(gender, constitution, charisma)
        self.special_immunities = ["Illusion Spells", "Paralyzation or Paralysis Attacks", "Magical Poisons"]
        self.surprise_chance = 3 / 6
        self.being_surprised_chance = 1 / 10

    def get_languages(self) -> List[str]:
        """
        Returns the languages known by Grey Dwarves.

        Returns:
            List[str]: A list of languages known by the Grey Dwarf.
        """
        return ["Dwarvish", "Undercommon"]

    def get_infravision_range(self) -> int:
        """
        Returns the infravision range of Grey Dwarves.

        Returns:
            int: The infravision range in feet.
        """
        return 120


class HillDwarf(Dwarf):
    """
    Class for Hill Dwarves, a subclass of Dwarf with additional traits and abilities.
    """

    def __init__(self, gender: str, constitution: int, charisma: int):
        super().__init__(gender, constitution, charisma)
        self.combat_bonus_vs_enemies = ["Goblin", "Hobgoblin", "Orc", "Half-Orc"]

    def get_languages(self) -> List[str]:
        """
        Returns the languages known by Hill Dwarves.

        Returns:
            List[str]: A list of languages known by the Hill Dwarf.
        """
        return ["Common", "Dwarvish", "Gnomish", "Goblin", "Kobold", "Orcish"]

    def get_infravision_range(self) -> int:
        """
        Returns the infravision range of Hill Dwarves.

        Returns:
            int: The infravision range in feet.
        """
        return 60


class MountainDwarf(Dwarf):
    """
    Class for Mountain Dwarves, a subclass of Dwarf with additional traits and abilities.
    """

    def __init__(self, gender: str, constitution: int, charisma: int):
        super().__init__(gender, constitution, charisma)

    def get_languages(self) -> List[str]:
        """
        Returns the languages known by Mountain Dwarves.

        Returns:
            List[str]: A list of languages known by the Mountain Dwarf.
        """
        return ["Common", "Dwarvish", "Gnomish", "Goblin", "Kobold", "Orcish"]

    def get_infravision_range(self) -> int:
        """
        Returns the infravision range of Mountain Dwarves.

        Returns:
            int: The infravision range in feet.
        """
        return 60

if __name__ == "__main__":
    # Example of creating a Grey Dwarf character and determining height and weight
    grey_dwarf = GreyDwarf(gender="Male", constitution=16, charisma=14)
    height_roll = 50  # Example roll
    weight_roll = 66  # Example roll

    grey_dwarf_height_table = {
        "Male": [
            ((1, 4), "44"), ((5, 15), "45"), ((16, 26), "46"), ((27, 37), "47"),
            ((38, 60), "48"), ((61, 71), "49"), ((72, 81), "50"), ((82, 91), "51"),
            ((92, 94), "52"), ((95, 97), "53"), ((98, 100), "54")
        ],
        "Female": [
            ((1, 4), "42"), ((5, 15), "43"), ((16, 26), "44"), ((27, 37), "45"),
            ((38, 59), "46"), ((60, 71), "47"), ((72, 83), "48"), ((84, 95), "49"),
            ((96, 100), "50")
        ]
    }

    grey_dwarf_weight_table = {
        "Male": [
            ((1, 20), "150 - 2d8"), ((21, 35), "150 - 1d8"), ((36, 49), "150"),
            ((50, 65), "150 + 1d8"), ((66, 100), "150 + 2d12")
        ],
        "Female": [
            ((1, 20), "120 - 2d8"), ((21, 35), "120 - 1d8"), ((36, 49), "120"),
            ((50, 65), "120 + 1d8"), ((66, 100), "120 + 2d10")
        ]
    }

    height = grey_dwarf.determine_height(height_roll, grey_dwarf_height_table)
    weight = grey_dwarf.determine_weight(weight_roll, grey_dwarf_weight_table)

    print(f"Grey Dwarf Height: {height} inches, Weight: {weight} pounds")
