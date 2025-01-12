class Quicksand:
    """
    A class to represent the mechanics of quicksand encounters.
    """

    def __init__(self, strength: int, can_swim: bool, encumbrance: str):
        self.strength = strength
        self.can_swim = can_swim
        self.encumbrance = encumbrance
        self.minutes_in_quicksand = 0
        self.time_left_treading = self.calculate_treading_time()

    def calculate_treading_time(self) -> int:
        """
        Calculate the time a character can tread water in quicksand based on their strength and encumbrance.

        :return: The number of minutes the character can tread water.
        """
        base_time = 5 * self.strength
        if self.encumbrance == "moderate":
            base_time //= 2
        elif self.encumbrance == "heavy":
            base_time //= 4
        return base_time

    def move_in_quicksand(self) -> str:
        """
        Simulate the character's movement in quicksand.

        :return: A string describing the character's progress or need for a STR check.
        """
        if self.can_swim:
            self.minutes_in_quicksand += 1
            return "Character swims 10 feet closer to the edge."
        else:
            if self.time_left_treading > 0:
                self.time_left_treading -= 10
                self.minutes_in_quicksand += 10
                return f"Character treads water, {self.time_left_treading} minutes left before needing a STR check."
            else:
                return "Character must make a STR check every 10 minutes to stay afloat."

    def check_str(self) -> bool:
        """
        Perform a strength check for the character to stay afloat.

        :return: True if the character succeeds, False if they fail.
        """
        success_threshold = 10
        return self.strength >= success_threshold

    def hold_breath(self) -> int:
        """
        Calculate the time the character can hold their breath after sinking in quicksand.

        :return: The number of minutes the character can hold their breath.
        """
        # Referencing the drowning mechanics
        return self.strength


# Example Usage:
# Create a character with a strength of 12, who cannot swim, is moderately encumbered
character_in_quicksand = Quicksand(strength=12, can_swim=False, encumbrance="moderate")

# Simulate the character's interaction with quicksand
for _ in range(5):  # Simulate 5 turns
    print(character_in_quicksand.move_in_quicksand())

# After the treading time is up, the character must make a STR check to stay afloat
if not character_in_quicksand.check_str():
    print(f"Character fails the STR check and sinks. Can hold breath for {character_in_quicksand.hold_breath()} minutes.")
else:
    print("Character succeeds the STR check and remains afloat.")
