from typing import Dict


class Character:
    """
    Represents a character in the game with attributes, experience points (XP),
    social class, literacy, and financial management related to monthly expenses.
    """

    def __init__(self, name: str, attributes: Dict[str, int], xp: int, character_class: str, gold: int,
                 social_class: Dict[str, str], race: str) -> None:
        """
        Initializes a new character.

        :param name: The name of the character.
        :param attributes: A dictionary containing the character's attributes (e.g., strength, dexterity).
        :param xp: The character's experience points.
        :param character_class: The character's class (e.g., Fighter, Mage).
        :param gold: The amount of gold the character possesses.
        :param social_class: A dictionary with 'class' and 'description' keys representing the character's social class.
        :param race: The race of the character (e.g., Human, Elf, Half-Orc).
        """
        self.name: str = name
        self.attributes: Dict[str, int] = attributes
        self.xp: int = xp
        self.character_class: str = character_class
        self.gold: int = gold  # Character's total gold pieces
        self.social_class: Dict[str, str] = social_class  # Social class dict with class name and description
        self.race: str = race  # Character's race
        self.literate: bool = self.determine_literacy()  # Determine literacy upon initialization
        self.monthly_expense_quality: str = 'Poor'  # Default living quality, can be 'Poor', 'Good', or 'Fine'
        self.track_time_passed: int = 0  # Tracks the number of days passed in-game

    def determine_literacy(self) -> bool:
        """
        Determines if the character is literate based on their social class, character class, and race.

        :return: True if the character is literate, False otherwise.
        """
        literacy_table: Dict[str, Dict[str, int]] = {
            'Lower Class': {'Bard': 17, 'Cleric': 19, 'Fighter': 9, 'Mage': 100, 'Thief': 14},
            'Middle Class - Lower Rung': {'Bard': 23, 'Cleric': 25, 'Fighter': 15, 'Mage': 100, 'Thief': 20},
            'Middle Class - Middle Rung': {'Bard': 29, 'Cleric': 31, 'Fighter': 21, 'Mage': 100, 'Thief': 26},
            'Lower Middle Class': {'Bard': 64, 'Cleric': 66, 'Fighter': 56, 'Mage': 100, 'Thief': 61},
            'Middle Class': {'Bard': 73, 'Cleric': 75, 'Fighter': 65, 'Mage': 100, 'Thief': 70},
            'Upper Middle Class': {'Bard': 82, 'Cleric': 84, 'Fighter': 74, 'Mage': 100, 'Thief': 79},
            'Lower Upper Class': {'Bard': 94, 'Cleric': 96, 'Fighter': 86, 'Mage': 100, 'Thief': 91},
            'Middle Upper Class': {'Bard': 98, 'Cleric': 98, 'Fighter': 98, 'Mage': 100, 'Thief': 98},
            'Upper Class': {'Bard': 100, 'Cleric': 100, 'Fighter': 100, 'Mage': 100, 'Thief': 100}
        }

        class_name: str = self.social_class['class']
        base_literacy_chance: int = literacy_table.get(class_name, {}).get(self.character_class, 0)

        # Apply racial modifiers
        if self.race in ['Elf', 'Halfling']:
            base_literacy_chance += 15
        elif self.race == 'Half-Orc':
            base_literacy_chance -= 10

        # Ensure the chance is between 0 and 100
        base_literacy_chance = max(0, min(100, base_literacy_chance))

        # Determine literacy by rolling a percentage
        roll: int = random.randint(1, 100)
        is_literate: bool = roll <= base_literacy_chance

        return is_literate

    def learn_literacy(self) -> None:
        """
        Enables the character to become literate after a period of study.
        The study period is 6 months minus 1 week per point of intelligence.
        """
        if not self.literate:
            weeks_to_learn: int = max(1, 24 - self.attributes.get('intelligence', 10))
            print(f"{self.name} will need {weeks_to_learn} weeks to become literate.")
            # Simulate learning (this would typically be spread over in-game time)
            self.track_time(weeks_to_learn * 7)
            self.literate = True
            print(f"{self.name} has become literate after {weeks_to_learn} weeks of study.")

    def track_time(self, days: int) -> None:
        """
        Tracks the passage of time and handles monthly expense deduction and literacy learning.

        :param days: Number of in-game days to track.
        """
        self.track_time_passed += days
        if self.track_time_passed >= 30:  # Assuming 30 days per in-game month
            self.deduct_monthly_expense()
            self.track_time_passed = 0  # Reset counter for the next month

    # Existing methods for monthly expenses would go here...


# Example usage
if __name__ == "__main__":
    # Create a character with attributes, XP, gold, social class, and race
    attributes: Dict[str, int] = {'strength': 15, 'dexterity': 17, 'intelligence': 14, 'wisdom': 12, 'constitution': 13,
                                  'charisma': 10}
    social_class: Dict[str, str] = {'class': 'Middle Class - Upper Rung',
                                    'description': 'Rich merchants, high officers, low-level clerics, high-level fighters'}

    # Create a character
    legolas = Character("Legolas", attributes, 15000, "Fighter", 500, social_class, "Elf")

    # Check literacy status
    if legolas.literate:
        print(f"{legolas.name} is literate.")
    else:
        print(f"{legolas.name} is illiterate. Beginning literacy training...")
        legolas.learn_literacy()

    # Track time and manage monthly expenses
    legolas.track_time(30)  # Simulate the passage of 30 days (1 month)
