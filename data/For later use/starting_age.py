import random
from typing import Dict, List, Tuple

class CharacterAge:
    """Handles age calculation and effects of aging on ability scores."""

    AGE_TABLE = {
        'Bard': {'Dwarf': None, 'Elf': (4, 8, 300), 'Gnome': (2, 6, 200), 'Half-elf': (2, 12, 30),
                 'Halfling': (1, 6, 26), 'Half-orc': None, 'Human': (1, 4, 16)},
        'Jester': {'Dwarf': None, 'Elf': None, 'Gnome': (1, 6, 200), 'Half-elf': None,
                   'Halfling': (1, 8, 24), 'Half-orc': None, 'Human': (1, 4, 16)},
        'Cavalier': {'Dwarf': None, 'Elf': (10, 10, 500), 'Gnome': None, 'Half-elf': (2, 4, 40),
                     'Halfling': None, 'Half-orc': None, 'Human': (1, 4, 18)},
        'Paladin': {'Dwarf': None, 'Elf': None, 'Gnome': None, 'Half-elf': None,
                    'Halfling': None, 'Half-orc': None, 'Human': (1, 4, 17)},
        'Cleric': {'Dwarf': (2, 20, 250), 'Elf': (10, 10, 500), 'Gnome': (3, 12, 300), 'Half-elf': (2, 4, 40),
                   'Halfling': (2, 4, 38), 'Half-orc': (1, 4, 20), 'Human': (1, 4, 18)},
        'Druid': {'Dwarf': None, 'Elf': (8, 10, 500), 'Gnome': (1, 12, 300), 'Half-elf': (2, 4, 40),
                  'Halfling': (1, 4, 38), 'Half-orc': None, 'Human': (1, 4, 18)},
        'Mystic': {'Dwarf': (9, 10, 500), 'Elf': None, 'Gnome': (1, 4, 40), 'Half-elf': (1, 4, 38),
                   'Halfling': None, 'Half-orc': None, 'Human': (1, 4, 18)},
        'Fighter': {'Dwarf': (5, 4, 40), 'Elf': (5, 6, 130), 'Gnome': (5, 4, 60), 'Half-elf': (3, 4, 22),
                    'Halfling': (3, 4, 20), 'Half-orc': (1, 4, 13), 'Human': (1, 4, 15)},
        'Barbarian': {'Dwarf': None, 'Elf': None, 'Gnome': None, 'Half-elf': None,
                      'Halfling': None, 'Half-orc': None, 'Human': (1, 4, 14)},
        'Ranger': {'Dwarf': None, 'Elf': (3, 8, 160), 'Gnome': None, 'Half-elf': (2, 6, 30),
                   'Halfling': None, 'Half-orc': None, 'Human': (1, 4, 20)},
        'Mage': {'Dwarf': None, 'Elf': (3, 6, 150), 'Gnome': None, 'Half-elf': (2, 8, 30),
                 'Halfling': None, 'Half-orc': None, 'Human': (2, 8, 24)},
        'Illusionist': {'Dwarf': None, 'Elf': None, 'Gnome': (2, 12, 100), 'Half-elf': None,
                        'Halfling': None, 'Half-orc': None, 'Human': (1, 6, 30)},
        'Savant': {'Dwarf': None, 'Elf': (3, 8, 180), 'Gnome': (3, 12, 100), 'Half-elf': (3, 6, 34),
                   'Halfling': None, 'Half-orc': None, 'Human': (2, 6, 28)},
        'Thief': {'Dwarf': (3, 6, 75), 'Elf': (5, 6, 100), 'Gnome': (5, 4, 80), 'Half-elf': (3, 8, 22),
                  'Halfling': (2, 4, 40), 'Half-orc': (2, 4, 20), 'Human': (1, 4, 18)},
        'Mountebank': {'Dwarf': (3, 6, 75), 'Elf': (5, 6, 100), 'Gnome': (5, 4, 80), 'Half-elf': (3, 8, 22),
                       'Halfling': (2, 4, 40), 'Half-orc': (2, 4, 20), 'Human': (1, 4, 18)},
    }

    AGE_EFFECTS = {
        'Young adult': {'wisdom': -1, 'constitution': +1},
        'Mature': {'strength': +1, 'wisdom': +1},
        'Middle age': {'strength': -1, 'constitution': -1, 'intelligence': +1, 'wisdom': +1},
        'Old': {'strength': -2, 'dexterity': -2, 'constitution': -1, 'wisdom': +1},
        'Very old': {'strength': -1, 'dexterity': -1, 'constitution': -1, 'intelligence': +1, 'wisdom': +1},
    }

    AGE_CATEGORIES = ['Young adult', 'Mature', 'Middle age', 'Old', 'Very old']

    def __init__(self, character_class: str, race: str):
        self.character_class = character_class
        self.race = race
        self.age = self.calculate_starting_age()

    def calculate_starting_age(self) -> int:
        """Calculates the starting age based on character class and race."""
        age_data = self.AGE_TABLE.get(self.character_class, {}).get(self.race)
        if age_data:
            num_dice, dice_size, base_age = age_data
            return sum(random.randint(1, dice_size) for _ in range(num_dice)) + base_age
        return 0

    def apply_aging_effects(self, age_category: str, current_abilities: Dict[str, int]) -> Dict[str, int]:
        """Applies the effects of aging on the character's abilities."""
        effects = self.AGE_EFFECTS.get(age_category, {})
        for ability, modifier in effects.items():
            current_abilities[ability] = max(min(current_abilities[ability] + modifier, 18), 3)  # Bound within 3-18
        return current_abilities

    def age_character(self, years_passed: int, current_abilities: Dict[str, int]) -> Dict[str, int]:
        """Ages the character by the specified number of years and applies ability score adjustments."""
        age_progression = self.AGE_CATEGORIES.copy()
        current_age = self.age

        for category in age_progression:
            if current_age < years_passed:
                current_abilities = self.apply_aging_effects(category, current_abilities)
            current_age += years_passed

        return current_abilities

    def get_current_age_category(self) -> str:
        """Returns the current age category based on the character's age."""
        for category in self.AGE_CATEGORIES:
            if self.age <= self.AGE_EFFECTS[category]:
                return category
        return 'Very old'

# Example Usage
character = CharacterAge(character_class='Thief', race='Human')
starting_age = character.calculate_starting_age()
print(f"Starting Age: {starting_age}")

# Example of applying aging effects
initial_abilities = {'strength': 15, 'dexterity': 14, 'constitution': 13, 'intelligence': 12, 'wisdom': 10, 'charisma': 9}
aged_abilities = character.age_character(years_passed=30, current_abilities=initial_abilities)
print(f"Aged Abilities: {aged_abilities}")
