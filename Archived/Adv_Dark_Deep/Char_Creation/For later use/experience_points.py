from typing import List, Dict, Optional


class Character:
    """
    Represents a character in the game, including XP and leveling up.
    """

    LEVEL_UP_XP_REQUIREMENTS = {
        'fighter': [0, 2000, 4000, 8000, 16000],  # Example levels
        'mage': [0, 2500, 5000, 10000, 20000],
        'thief': [0, 1200, 2400, 4800, 9600],
        # Add other classes and their level-up XP requirements here
    }

    def __init__(self, name: str, character_class: str, level: int = 1, xp: int = 0):
        self.name: str = name
        self.character_class: str = character_class
        self.level: int = level
        self.xp: int = xp
        self.needs_training: bool = False
        self.training_cost: Optional[int] = None

    def add_xp(self, amount: int) -> None:
        """
        Adds XP to the character and checks if they can level up.
        """
        if self.needs_training:
            print(f"{self.name} needs training before gaining more XP.")
            return

        self.xp += amount
        print(f"{self.name} gains {amount} XP. Total XP: {self.xp}.")

        self.check_level_up()

    def check_level_up(self) -> None:
        """
        Checks if the character has enough XP to level up and handles leveling up.
        """
        next_level_xp = self.LEVEL_UP_XP_REQUIREMENTS[self.character_class][self.level]
        if self.xp >= next_level_xp:
            self.level_up()

    def level_up(self) -> None:
        """
        Handles the process of leveling up the character.
        """
        self.level += 1
        self.needs_training = True
        self.training_cost = 1500 * self.level
        print(f"{self.name} has leveled up to level {self.level}!")
        print(f"{self.name} now requires training costing {self.training_cost} gold pieces to proceed.")

    def train(self, trainer_level: int, payment: int) -> None:
        """
        Trains the character, allowing them to complete the level-up process.
        """
        if trainer_level >= self.level + 2 and payment >= self.training_cost:
            print(f"{self.name} has been successfully trained and is now fully level {self.level}.")
            self.needs_training = False
            self.training_cost = None
        else:
            print(f"{self.name} could not complete training. Requirements not met.")

    def max_xp_before_training(self) -> int:
        """
        Calculates the maximum XP the character can have before needing training.
        """
        return self.LEVEL_UP_XP_REQUIREMENTS[self.character_class][self.level + 1] - 1

    def __repr__(self) -> str:
        return f"{self.name} (Class: {self.character_class}, Level: {self.level}, XP: {self.xp}, Needs Training: {self.needs_training})"


# Example Usage
if __name__ == "__main__":
    reginald = Character(name="Reginald", character_class="fighter", level=3, xp=7500)
    reginald.add_xp(2000)  # Should trigger level up
    print(reginald)

    # Attempting to train Reginald with insufficient trainer level or funds
    reginald.train(trainer_level=4, payment=2000)  # Should succeed
    print(reginald)

    # Try to add more XP after training is required
    reginald.add_xp(2000)  # Should allow more XP since training was completed
    print(reginald)
