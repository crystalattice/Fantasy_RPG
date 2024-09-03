import random

class SleepDeprivation:
    """
    A class to represent the mechanics of sleep deprivation.
    """

    def __init__(self):
        self.hours_slept = 0
        self.penalty = 0
        self.days_without_sleep = 0

    def rest(self, hours: int) -> None:
        """
        Simulate a character resting for a certain number of hours.

        :param hours: The number of hours the character sleeps.
        """
        self.hours_slept = hours
        if self.hours_slept >= 7:
            self.reset_deprivation()
        elif self.hours_slept >= self.required_sleep():
            self.days_without_sleep = 0
        else:
            self.increase_penalty()

    def required_sleep(self) -> int:
        """
        Calculate the required sleep for a character in a 24-hour period.

        :return: The number of hours required for sleep.
        """
        return random.randint(1, 3) + 2

    def increase_penalty(self) -> None:
        """
        Increase the penalty for sleep deprivation after inadequate rest.
        """
        self.days_without_sleep += 1
        self.penalty += 1

    def apply_penalty(self) -> str:
        """
        Apply the cumulative penalty to all rolls due to sleep deprivation.

        :return: A string describing the current penalty.
        """
        return f"Penalty of -{self.penalty} or -{self.penalty * 5}% to all rolls due to sleep deprivation."

    def collapse(self) -> bool:
        """
        Determine if the character collapses from exhaustion after too many days without proper sleep.

        :return: True if the character collapses, False otherwise.
        """
        if self.days_without_sleep >= random.randint(2, 8):
            return True
        return False

    def forced_sleep(self) -> int:
        """
        Determine how long the character will sleep after collapsing from exhaustion.

        :return: The number of hours the character will sleep.
        """
        return sum(random.randint(1, 4) for _ in range(3))

    def reset_deprivation(self) -> None:
        """
        Reset the sleep deprivation status after a full night's rest.
        """
        self.penalty = 0
        self.days_without_sleep = 0

# Example Usage:
# Create a sleep deprivation tracker
sleep_deprivation = SleepDeprivation()

# Simulate a character sleeping for 4 hours
sleep_deprivation.rest(4)
print(sleep_deprivation.apply_penalty())

# Check if the character collapses after several days without proper sleep
if sleep_deprivation.collapse():
    sleep_duration = sleep_deprivation.forced_sleep()
    print(f"Character collapses from exhaustion and will sleep for {sleep_duration} hours.")
else:
    print("Character manages to stay awake.")

# Simulate a full night's sleep
sleep_deprivation.rest(7)
print("Character slept for 7 hours and is fully rested.")
