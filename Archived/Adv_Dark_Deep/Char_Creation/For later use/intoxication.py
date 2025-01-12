from typing import Dict


class Character:
    """
    A class to represent a character with a constitution score and race,
    which influences how much they can drink before becoming intoxicated.
    """

    def __init__(self, constitution: int, race: str = "Human"):
        """
        Initialize a character with constitution score and race.

        :param constitution: The constitution score of the character.
        :param race: The race of the character (default is "Human").
        """
        self.constitution = constitution
        self.race = race
        self.intoxication_level = 0
        self.extra_drinks = self.get_extra_drinks()

    def get_extra_drinks(self) -> int:
        """
        Determine the number of extra drinks a character can have before
        moving up the intoxication scale based on race.

        :return: The number of extra drinks (0 for humans, 2 for dwarves and half-orcs, 1 for halflings).
        """
        if self.race in ["Dwarf", "Half-Orc"]:
            return 2
        elif self.race == "Halfling":
            return 1
        return 0

    def drinks_to_intoxication(self) -> Dict[str, int]:
        """
        Calculate the number of drinks required to reach each level of intoxication
        based on the character's constitution score.

        :return: A dictionary with keys 'slightly', 'somewhat', 'very', 'passed_out'
                 and values representing the number of drinks needed to reach each level.
        """
        intoxication_table = {
            (3, 6): (1, 2, 3, 4),
            (7, 8): (3, 5, 7, 9),
            (9, 12): (5, 7, 9, 11),
            (13, 15): (7, 9, 11, 13),
            (16, 17): (9, 11, 13, 15),
            (18, 18): (11, 13, 15, 17),
            (19, float('inf')): (13, 15, 17, float('inf'))
        }

        for key, value in intoxication_table.items():
            if key[0] <= self.constitution <= key[1]:
                return {
                    'slightly': value[0] + self.extra_drinks,
                    'somewhat': value[1] + self.extra_drinks,
                    'very': value[2] + self.extra_drinks,
                    'passed_out': value[3] + self.extra_drinks
                }
        return {}

    def consume_drinks(self, drinks: int) -> None:
        """
        Consume a certain number of drinks and update the intoxication level.

        :param drinks: The number of drinks consumed.
        """
        levels = self.drinks_to_intoxication()
        if drinks >= levels['passed_out']:
            self.intoxication_level = 4  # Passed out
        elif drinks >= levels['very']:
            self.intoxication_level = 3  # Very intoxicated
        elif drinks >= levels['somewhat']:
            self.intoxication_level = 2  # Somewhat intoxicated
        elif drinks >= levels['slightly']:
            self.intoxication_level = 1  # Slightly intoxicated
        else:
            self.intoxication_level = 0  # Not intoxicated

    def intoxication_effects(self) -> Dict[str, int]:
        """
        Return the effects based on the current level of intoxication.

        :return: A dictionary with keys representing affected attributes and values representing penalties or bonuses.
        """
        effects = {
            1: {'INT': -1, 'WIS': -1, 'Morale': +1},
            2: {'INT': -3, 'WIS': -4, 'DEX': -2, 'CHA': -1, 'to_hit': -1, 'extra_hp': +1},
            3: {'INT': -6, 'WIS': -7, 'DEX': -5, 'CHA': -4, 'to_hit': -5, 'extra_hp': +3},
            4: {'status': 'passed out'}
        }
        return effects.get(self.intoxication_level, {})

    def sober_up(self) -> None:
        """
        Reduce the intoxication level by one step every two hours.

        This simulates the character sobering up.
        """
        if self.intoxication_level > 0:
            self.intoxication_level -= 1


# Example Usage:
# Create a character with a specific constitution score and race
character = Character(constitution=14, race="Dwarf")

# Determine the number of drinks required to reach different intoxication levels
print(character.drinks_to_intoxication())  # Outputs: {'slightly': 9, 'somewhat': 11, 'very': 13, 'passed_out': 15}

# Simulate consuming drinks
character.consume_drinks(12)
print(f"Intoxication Level: {character.intoxication_level}")  # Outputs: 2 (Somewhat intoxicated)

# Get the effects of the current intoxication level
print(
    character.intoxication_effects())  # Outputs: {'INT': -3, 'WIS': -4, 'DEX': -2, 'CHA': -1, 'to_hit': -1, 'extra_hp': +1}

# Simulate sobering up over time
character.sober_up()
print(f"Intoxication Level after sobering up: {character.intoxication_level}")  # Outputs: 1 (Slightly intoxicated)
