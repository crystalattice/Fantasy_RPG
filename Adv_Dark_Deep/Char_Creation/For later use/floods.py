import random

class Flood:
    """Class to handle the effects of a flood on characters."""

    def __init__(self, duration: int):
        """
        Initialize the Flood with its duration.

        :param duration: Duration of the flood in minutes.
        """
        self.duration = duration

    def str_check(self, str_score: int) -> bool:
        """
        Perform a Strength check to see if the character can grab onto an object.

        :param str_score: Strength score of the character.
        :return: True if the check is successful, False otherwise.
        """
        return random.randint(1, 20) <= str_score

    def attempt_grab(self, str_score: int) -> bool:
        """
        Attempt to grab onto an object during the flood.

        :param str_score: Strength score of the character.
        :return: True if the character successfully grabs the object, False otherwise.
        """
        success = self.str_check(str_score)
        if success:
            print("Character successfully grabs an object.")
        else:
            print("Character fails to grab an object and is swept along by the flood.")
        return success

    def handle_flood(self, str_score: int) -> int:
        """
        Simulate the effects of a flood on a character.

        :param str_score: Strength score of the character.
        :return: Total damage taken by the character.
        """
        total_damage = 0
        minutes_passed = 0

        while minutes_passed < self.duration:
            print(f"Minute {minutes_passed + 1}:")
            if not self.attempt_grab(str_score):
                # If the character fails to grab, they take damage
                damage = random.randint(1, 4)
                total_damage += damage
                print(f"Character takes {damage} damage from being bashed against objects.")
            minutes_passed += 2

        print(f"Flood duration has ended. Total damage taken: {total_damage} HP")
        return total_damage

    @staticmethod
    def flash_flood_duration() -> int:
        """
        Determine the duration of a flash flood.

        :return: Duration of the flash flood in minutes.
        """
        return random.randint(1, 6) + 9


# Example Usage:
# Simulate a flash flood
flash_flood = Flood(Flood.flash_flood_duration())
print(f"Flash flood duration: {flash_flood.duration} minutes")

# Simulate a character with a STR score of 12
damage_taken = flash_flood.handle_flood(str_score=12)
print(f"Total damage taken by the character: {damage_taken} HP")
