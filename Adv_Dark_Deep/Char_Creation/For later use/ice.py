import random

class Ice:
    """Class to handle the effects of moving across slippery ice."""

    def __init__(self, normal_speed: int):
        """
        Initialize the Ice class with the creature's normal movement speed.

        :param normal_speed: The normal movement speed of the creature.
        """
        self.normal_speed = normal_speed
        self.ice_speed = normal_speed * 0.25  # Speed reduced to 25% on ice

    def dex_check(self, dex_score: int) -> bool:
        """
        Perform a Dexterity check to see if the creature can remain standing on the ice.

        :param dex_score: Dexterity score of the creature.
        :return: True if the check is successful, False otherwise.
        """
        return random.randint(1, 20) <= dex_score

    def move_across_ice(self, dex_score: int) -> bool:
        """
        Simulate moving across slippery ice. Each round, the creature must make a DEX check.

        :param dex_score: Dexterity score of the creature.
        :return: True if the creature successfully remains standing, False otherwise.
        """
        success = self.dex_check(dex_score)
        if success:
            print(f"Creature moves {self.ice_speed} feet across the ice without falling.")
        else:
            print("Creature falls and must spend the next round getting up.")
        return success


# Example Usage:
# Simulate a creature with a normal speed of 30 feet and a DEX score of 14 moving across ice.
ice_surface = Ice(normal_speed=30)

# Simulate one round of movement on the ice
moved_successfully = ice_surface.move_across_ice(dex_score=14)

if not moved_successfully:
    print("The creature will need to spend the next round getting up.")
else:
    print("The creature continues to move across the ice.")
