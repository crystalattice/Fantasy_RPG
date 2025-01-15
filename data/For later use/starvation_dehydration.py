from typing import Optional


class Character:
    """
    A class to represent a character's status in terms of food and water deprivation.
    """

    def __init__(self, strength: int, constitution: int, weight: str, gender: str, activity_level: str, temperature: int):
        self.strength = strength
        self.constitution = constitution
        self.weight = weight
        self.gender = gender
        self.activity_level = activity_level
        self.temperature = temperature
        self.privation_step = "None"
        self.priv_steps = ["Shaky", "Drained", "Debilitated", "Dying"]

    def starvation_days(self) -> int:
        """
        Calculate the minimum number of days the character can go without food before starvation sets in.

        :return: The number of days the character can go without food before starvation.
        """
        str_con_total = self.strength + self.constitution
        if str_con_total <= 15:
            return 4
        elif str_con_total <= 19:
            return 5
        elif str_con_total <= 24:
            return 6
        elif str_con_total <= 30:
            return 7
        elif str_con_total <= 35:
            return 8
        else:
            return 9

    def dehydration_days(self) -> int:
        """
        Calculate the number of days the character can go without water before dehydration sets in.

        :return: The number of days the character can go without water before dehydration.
        """
        days = 3
        if self.weight == "higher":
            days += 1
        if self.gender == "female":
            days += 1
        if self.activity_level == "resting":
            days += 1
        if self.temperature > 90:
            days -= 1
        if self.priv_steps == "not eating":
            days -= 1
        if (self.strength + self.constitution) < 8:
            days -= 1
        return max(1, days)

    def check_starvation(self, days_without_food: int) -> Optional[str]:
        """
        Perform a starvation check for the character based on the number of days without food.

        :param days_without_food: The number of days the character has gone without food.
        :return: The privation step the character has reached, if any.
        """
        if days_without_food > self.starvation_days():
            # Apply cumulative +1 penalty for each 12-hour period after the first failed check
            penalty = (days_without_food - self.starvation_days()) // 2
            check = max(self.strength, self.constitution) - penalty
            if check < 10:
                return self.advance_privation_step()
        return None

    def check_dehydration(self, days_without_water: int) -> Optional[str]:
        """
        Perform a dehydration check for the character based on the number of days without water.

        :param days_without_water: The number of days the character has gone without water.
        :return: The privation step the character has reached, if any.
        """
        if days_without_water > self.dehydration_days():
            return self.advance_privation_step()
        return None

    def advance_privation_step(self) -> str:
        """
        Advance the character to the next privation step.

        :return: The new privation step the character has reached.
        """
        if self.privation_step == "None":
            self.privation_step = self.priv_steps[0]
        else:
            current_step_index = self.priv_steps.index(self.privation_step)
            if current_step_index < len(self.priv_steps) - 1:
                self.privation_step = self.priv_steps[current_step_index + 1]
        return self.privation_step


# Example Usage:
# Create a character with a strength of 14, constitution of 12, higher weight, male, resting activity level, and 85°F temperature
character = Character(strength=14, constitution=12, weight="higher", gender="male", activity_level="resting", temperature=85)

# Simulate the effects of starvation after 7 days without food
starvation_result = character.check_starvation(days_without_food=7)
if starvation_result:
    print(f"Starvation effect: {starvation_result}")

# Simulate the effects of dehydration after 4 days without water
dehydration_result = character.check_dehydration(days_without_water=4)
if dehydration_result:
    print(f"Dehydration effect: {dehydration_result}")
