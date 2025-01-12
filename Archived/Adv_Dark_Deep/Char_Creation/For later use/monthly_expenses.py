from typing import Dict, Optional
import random


class Character:
    """
    Represents a character in the game with attributes, experience points (XP),
    social class, and financial management related to monthly expenses.
    """

    def __init__(self, name: str, attributes: Dict[str, int], xp: int, character_class: str, gold: int,
                 social_class: Dict[str, str]) -> None:
        """
        Initializes a new character.

        :param name: The name of the character.
        :param attributes: A dictionary containing the character's attributes (e.g., strength, dexterity).
        :param xp: The character's experience points.
        :param character_class: The character's class (e.g., Fighter, Mage).
        :param gold: The amount of gold the character possesses.
        :param social_class: A dictionary with 'class' and 'description' keys representing the character's social class.
        """
        self.name: str = name
        self.attributes: Dict[str, int] = attributes
        self.xp: int = xp
        self.character_class: str = character_class
        self.gold: int = gold  # Character's total gold pieces
        self.social_class: Dict[str, str] = social_class  # Social class dict with class name and description
        self.monthly_expense_quality: str = 'Poor'  # Default living quality, can be 'Poor', 'Good', or 'Fine'
        self.track_time_passed: int = 0  # Tracks the number of days passed in-game

    def set_living_quality(self, quality: str) -> None:
        """
        Sets the character's living quality for monthly expenses.

        :param quality: The quality of living ('Poor', 'Good', 'Fine').
        """
        if quality in ['Poor', 'Good', 'Fine']:
            self.monthly_expense_quality = quality
        else:
            print("Invalid living quality. Please choose 'Poor', 'Good', or 'Fine'.")

    def get_monthly_expense(self) -> int:
        """
        Calculates the monthly expense based on the character's social class and living quality.

        :return: The cost of monthly living in gold pieces.
        """
        expense_table: Dict[str, Dict[str, int]] = {
            'Lower Class': {'Poor': 1, 'Good': 2, 'Fine': 10},  # Silver and Gold
            'Middle Class - Lower Rung': {'Poor': 1, 'Good': 2, 'Fine': 5},
            'Middle Class - Middle Rung': {'Poor': 2, 'Good': 5, 'Fine': 10},
            'Lower Middle Class': {'Poor': 10, 'Good': 25, 'Fine': 50},
            'Middle Class': {'Poor': 25, 'Good': 100, 'Fine': 125},
            'Upper Middle Class': {'Poor': 100, 'Good': 250, 'Fine': 500},
            'Lower Upper Class': {'Poor': 250, 'Good': 500, 'Fine': 1250},
            'Middle Upper Class': {'Poor': 500, 'Good': 1000, 'Fine': 2500},
            'Upper Class': {'Poor': 1000, 'Good': 2000, 'Fine': 5000}
        }

        # Retrieve the expense based on social class and quality of living
        class_name: str = self.social_class['class']
        return expense_table.get(class_name, {}).get(self.monthly_expense_quality, 0)

    def deduct_monthly_expense(self) -> None:
        """
        Deducts the appropriate monthly expense from the character's gold.
        """
        expense: int = self.get_monthly_expense()

        if self.gold >= expense:
            self.gold -= expense
            print(
                f"{self.name} has been charged {expense} gold pieces for {self.monthly_expense_quality} living. Remaining gold: {self.gold} gp.")
        else:
            print(f"{self.name} cannot afford {self.monthly_expense_quality} living. Gold remaining: {self.gold} gp.")
            self.check_social_downgrade()

    def check_social_downgrade(self) -> None:
        """
        Checks if the character should be downgraded in social class due to lack of funds.
        """
        if self.gold < self.get_monthly_expense():
            roll: int = random.randint(1, 12)
            if roll == 1:
                self.downgrade_social_class()
            else:
                print(f"{self.name} maintains their social class despite financial difficulties.")

    def downgrade_social_class(self) -> None:
        """
        Downgrades the character's social class one rank if they can't afford their lifestyle.
        """
        downgrade_map: Dict[str, str] = {
            'Upper Class': 'Middle Upper Class',
            'Middle Upper Class': 'Lower Upper Class',
            'Lower Upper Class': 'Upper Middle Class',
            'Upper Middle Class': 'Middle Class',
            'Middle Class': 'Lower Middle Class',
            'Lower Middle Class': 'Middle Class - Upper Rung',
            'Middle Class - Upper Rung': 'Middle Class - Middle Rung',
            'Middle Class - Middle Rung': 'Middle Class - Lower Rung',
            'Middle Class - Lower Rung': 'Lower Class'
        }

        current_class: str = self.social_class['class']
        if current_class in downgrade_map:
            new_class: str = downgrade_map[current_class]
            self.social_class['class'] = new_class
            print(f"{self.name} has been downgraded to {new_class} due to insufficient funds.")

    def track_time(self, days: int) -> None:
        """
        Tracks the passage of time and triggers monthly expense deduction.

        :param days: Number of in-game days to track.
        """
        self.track_time_passed += days
        if self.track_time_passed >= 30:  # Assuming 30 days per in-game month
            self.deduct_monthly_expense()
            self.track_time_passed = 0  # Reset counter for the next month


# Example usage
if __name__ == "__main__":
    # Create a character with attributes, XP, gold, and social class
    attributes: Dict[str, int] = {'strength': 15, 'dexterity': 17, 'intelligence': 14, 'wisdom': 12, 'constitution': 13,
                                  'charisma': 10}
    social_class: Dict[str, str] = {'class': 'Middle Class - Upper Rung',
                                    'description': 'Rich merchants, high officers, low-level clerics, high-level fighters'}

    # Create a character
    aragorn = Character("Aragorn", attributes, 15000, "Fighter", 500, social_class)

    # Set living quality to "Good"
    aragorn.set_living_quality("Good")

    # Track time and handle monthly expenses
    aragorn.track_time(30)  # Simulate the passage of 30 days (1 month)
