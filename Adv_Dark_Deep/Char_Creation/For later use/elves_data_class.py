from typing import List, Dict, Tuple, Union
from dataclasses import dataclass, field
import random

@dataclass
class Elf:
    """
    Base class for Elves, representing common attributes and methods.
    """
    gender: str
    strength: int
    intelligence: int
    wisdom: int
    dexterity: int
    constitution: int
    charisma: int
    infravision_range: int = 60  # Default infravision range for all elves
    languages: List[str] = field(default_factory=lambda: ["Elvish", "Common"])
    resistances: Dict[str, int] = field(default_factory=lambda: {
        "sleep": 90,
        "charm": 90
    })
    secret_door_detection: Tuple[int, int] = (1, 2)  # (chance without searching, chance when searching)
    concealed_door_detection: int = 3  # chance when searching
    base_move_rate: int = 120  # Default movement rate
    surprise_chance: Tuple[int, int] = (4, 2)  # (chance in optimal conditions, chance otherwise)

    def detect_secret_doors(self, searching: bool = False) -> int:
        """
        Returns the chance to detect secret doors.
        """
        return self.secret_door_detection[1] if searching else self.secret_door_detection[0]

    def detect_concealed_doors(self) -> int:
        """
        Returns the chance to detect concealed doors when searching.
        """
        return self.concealed_door_detection

    def move_quietly(self) -> int:
        """
        Returns the chance to surprise opponents when moving quietly.
        """
        return self.surprise_chance[0] if self.meets_movement_requirements() else self.surprise_chance[1]

    def meets_movement_requirements(self) -> bool:
        """
        Determines if the elf meets the requirements to move quietly.
        """
        # This function would contain logic to check if the elf is meeting the specific movement conditions
        return True

    def determine_height(self, height_roll: int, height_table: Dict[str, List[Tuple[Tuple[int, int], str]]]) -> int:
        """
        Determines the height of an elf based on gender and a percentile roll.
        """
        for range_tuple, height in height_table[self.gender]:
            if range_tuple[0] <= height_roll <= range_tuple[1]:
                return int(height)
        raise ValueError("Invalid roll provided.")

    def determine_weight(self, weight_roll: int, weight_table: Dict[str, List[Tuple[Tuple[int, int], str]]]) -> int:
        """
        Determines the weight of an elf based on gender and a percentile roll.
        """
        for range_tuple, formula in weight_table[self.gender]:
            if range_tuple[0] <= weight_roll <= range_tuple[1]:
                if 'd' in formula:
                    base_weight_str, dice = formula.split(' - ') if ' - ' in formula else formula.split(' + ')
                    base_weight = int(base_weight_str)
                    weight_modifier = self.roll_dice(dice)
                    return base_weight - weight_modifier if ' - ' in formula else base_weight + weight_modifier
                else:
                    return int(formula)
        raise ValueError("Invalid roll provided.")

    @staticmethod
    def roll_dice(dice: str) -> int:
        """
        Simulates rolling dice (e.g., '2d8') and returns the total result.
        """
        num, sides = map(int, dice.split('d'))
        return sum(random.randint(1, sides) for _ in range(num))


@dataclass
class DarkElf(Elf):
    """
    Class representing Dark Elves, with their unique attributes.
    """
    magic_resistance_bonus: int = 2
    base_move_rate: int = 120  # Dark elves have a standard movement rate of 120’
    infravision_range: int = 120  # Extended infravision for dark elves
    stone_detection_abilities: Dict[str, int] = field(default_factory=lambda: {
        "slope": 75,
        "new_construction": 75,
        "shifting_walls": 67,
        "pit_traps": 50,
        "depth_sensing": 50
    })
    surprise_chance: Tuple[int, int] = (1, 8)  # Dark elves are only surprised 1 in 8 times
    sunlight_penalties: Dict[str, int] = field(default_factory=lambda: {
        "dexterity": -2,
        "to_hit": -2,
        "enemy_saving_throw_bonus": 2
    })
    special_spells: List[str] = field(default_factory=lambda: ["dancing lights", "faerie fire", "darkness 5' radius"])

    def get_sunlight_penalties(self):
        """
        Applies penalties for being in sunlight.
        """
        self.dexterity += self.sunlight_penalties["dexterity"]
        # Apply other penalties as needed

    def cast_special_spell(self, spell_name: str):
        """
        Allows the dark elf to cast one of their special innate spells.
        """
        if spell_name in self.special_spells:
            return f"{spell_name} cast successfully!"
        else:
            return f"{spell_name} is not available."


@dataclass
class GreyElf(Elf):
    """
    Class representing Grey Elves, with their unique attributes.
    """
    intelligence_bonus: int = 1
    weapon_bonus: Dict[str, int] = field(default_factory=lambda: {
        "longbow": 1,
        "shortbow": 1,
        "longsword": 1,
        "shortsword": 1
    })

    def attack_bonus(self, weapon: str) -> int:
        """
        Returns the attack bonus for the specified weapon.
        """
        return self.weapon_bonus.get(weapon, 0)


@dataclass
class HighElf(Elf):
    """
    Class representing High Elves, with their unique attributes.
    """
    dexterity_bonus: int = 1
    constitution_penalty: int = -1
    weapon_bonus: Dict[str, int] = field(default_factory=lambda: {
        "longbow": 1,
        "shortbow": 1,
        "longsword": 1,
        "shortsword": 1
    })


@dataclass
class WildElf(Elf):
    """
    Class representing Wild Elves, with their unique attributes.
    """
    strength_bonus: int = 2
    intelligence_penalty: int = -1
    weapon_bonus: Dict[str, int] = field(default_factory=lambda: {
        "longbow": 1,
        "shortbow": 1,
        "longsword": 1,
        "shortsword": 1
    })
    trap_setting_chance: int = 90  # 90% chance to set traps in woodland settings


@dataclass
class WoodElf(Elf):
    """
    Class representing Wood Elves, with their unique attributes.
    """
    strength_bonus: int = 1
    intelligence_penalty: int = -1
    weapon_bonus: Dict[str, int] = field(default_factory=lambda: {
        "longbow": 1,
        "shortbow": 1,
        "longsword": 1,
        "shortsword": 1
    })
    woodland_animal_friendship: bool = True

if __name__ == "__main__":
    # Example of creating a Dark Elf character and determining height and weight
    dark_elf = DarkElf(gender="Male", strength=16, intelligence=14, wisdom=13, dexterity=18, constitution=10, charisma=15)
    height_roll = 45  # Example roll
    weight_roll = 55  # Example roll

    dark_elf_height_table = {
        "Male": [
            ((1, 10), "60 - 1d4"), ((11, 31), "60 - 1d4"), ((32, 59), "60"),
            ((60, 80), "60 + 1d4"), ((81, 100), "60 + 1d6")
        ],
        "Female": [
            ((1, 10), "54 - 1d4"), ((11, 31), "54 - 1d3"), ((32, 59), "54"),
            ((60, 80), "54 + 1d4"), ((81, 100), "54 + 1d6")
        ]
    }

    dark_elf_weight_table = {
        "Male": [
            ((1, 15), "100 - 1d10"), ((16, 38), "100 - 1d8"), ((39, 67), "100"),
            ((68, 90), "100 + 1d8"), ((91, 100), "100 + 1d20")
        ],
        "Female": [
            ((1, 15), "80 - 1d10"), ((16, 38), "80 - 1d4"), ((39, 67), "80"),
            ((68, 90), "80 + 1d4"), ((91, 100), "80 + 2d6")
        ]
    }

    height = dark_elf.determine_height(height_roll, dark_elf_height_table)
    weight = dark_elf.determine_weight(weight_roll, dark_elf_weight_table)

    print(f"Dark Elf Height: {height} inches, Weight: {weight} pounds")
