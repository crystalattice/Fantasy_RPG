import random
from typing import Dict


class Character:
    """
    Represents a character in the game with attributes, experience points (XP),
    social class, literacy, and financial management related to monthly expenses.
    """

    def __init__(self, name: str, attributes: Dict[str, int], xp: int, character_class: str,
                 social_class: Dict[str, str], race: str) -> None:
        """
        Initializes a new character.

        :param name: The name of the character.
        :param attributes: A dictionary containing the character's attributes (e.g., strength, dexterity).
        :param xp: The character's experience points.
        :param character_class: The character's class (e.g., Fighter, Mage).
        :param social_class: A dictionary with 'class' and 'description' keys representing the character's social class.
        :param race: The race of the character (e.g., Human, Elf, Half-Orc).
        """
        self.name: str = name
        self.attributes: Dict[str, int] = attributes
        self.xp: int = xp
        self.character_class: str = character_class
        self.social_class: Dict[str, str] = social_class
        self.race: str = race
        self.gold: int = self.determine_starting_money()
        self.literate: bool = self.determine_literacy()

    def determine_starting_money(self) -> int:
        """
        Determines the starting money for the character based on their class.

        :return: The amount of starting money in gold pieces.
        """
        starting_money_table: Dict[str, tuple[int, int]] = {
            'Bard': (20, 120),
            'Jester': (20, 80),
            'Cavalier': (0, 0),  # Special, handled separately
            'Paladin': (0, 0),  # Special, handled separately
            'Cleric': (30, 180),
            'Druid': (30, 180),
            'Mystic': (13, 24),
            'Fighter': (50, 200),
            'Barbarian': (50, 200),
            'Ranger': (50, 200),
            'Mage': (20, 80),
            'Illusionist': (20, 80),
            'Savant': (20, 80),
            'Thief': (20, 120),
            'Mountebank': (20, 120)
        }

        if self.character_class in ['Cavalier', 'Paladin']:
            # Cavaliers and Paladins have special rules for starting money
            print(f"{self.character_class}s have special rules for starting money.")
            return 0  # Placeholder for special handling

        min_money, max_money = starting_money_table.get(self.character_class, (0, 0))
        starting_money = random.randint(min_money, max_money)

        return starting_money

    # Example methods like determine_literacy() and other existing methods


# Example usage
if __name__ == "__main__":
    # Create a character with attributes, XP, social class, and race
    attributes: Dict[str, int] = {'strength': 15, 'dexterity': 12, 'intelligence': 14, 'wisdom': 10, 'constitution': 13,
                                  'charisma': 11}
    social_class: Dict[str, str] = {'class': 'Lower Middle Class',
                                    'description': 'Artisans, craftsmen, minor merchants, itinerant cavaliers, druids, rangers'}

    # Create a character
    legolas = Character("Legolas", attributes, 0, "Ranger", social_class, "Elf")

    # Check starting money
    print(f"{legolas.name} starts with {legolas.gold} gold pieces.")
