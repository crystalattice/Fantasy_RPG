import random
from typing import List

class Landslide:
    """
    A class to represent the mechanics of a landslide and its effects on characters.
    """
    def __init__(self):
        self.attack_column_g_damage = 4  # Represents damage done by rocks in attack column G (1d4)
        self.attack_column_l_damage = 8  # Represents damage done by rocks in attack column L (1d8)

    def landslide_damage_on_slope(self, dexterity_check: bool) -> int:
        """
        Calculate the damage a character takes if caught in a landslide on a slope.

        :param dexterity_check: Whether the character succeeded in a DEX check to halve the damage.
        :return: Total damage taken during the landslide.
        """
        total_minutes = random.randint(2, 5)  # 1d4+1 minutes
        total_damage = 0

        for minute in range(total_minutes):
            rocks = random.randint(1, 6)  # 1d6 rocks per minute
            for _ in range(rocks):
                damage = random.randint(1, self.attack_column_g_damage)  # 1d4 damage per rock
                if dexterity_check:
                    damage = max(1, damage // 2)  # Halve the damage if DEX check succeeded, minimum 1
                total_damage += damage

            # Check if swept down the slope
            if total_damage > 20:
                total_damage += self.falling_damage()
                break

        return total_damage

    def landslide_damage_at_cliff_base(self) -> int:
        """
        Calculate the damage a character takes if caught in a landslide at the base of a cliff.

        :return: Total damage taken during the landslide.
        """
        total_minutes = random.randint(1, 2)
        total_damage = 0

        for minute in range(total_minutes):
            rocks = random.randint(0, 3)  # 1d4-1 rocks per minute
            for _ in range(rocks):
                damage = random.randint(1, self.attack_column_l_damage)  # 1d8 damage per rock
                shield_deflect = random.random() < 0.75  # 75% chance to deflect with a shield
                if not shield_deflect:
                    total_damage += damage

        return total_damage

    @staticmethod
    def falling_damage() -> int:
        """
        Calculate falling damage when swept down a slope during a landslide.

        :return: Falling damage based on the distance fallen.
        """
        # Assuming a random fall distance of 20-50 feet for the purpose of this example
        distance = random.randint(20, 50)
        damage = (distance // 10) * random.randint(1, 6)  # 1d6 damage per 10 feet fallen
        return damage


class Mudslide:
    """
    A class to represent the mechanics of a mudslide and its effects on characters.
    """
    @staticmethod
    def mudslide_effect() -> str:
        """
        Determine the effect of a mudslide on a character.

        :return: Description of the effect (carried to the base of the slope and into a quicksand-like pool).
        """
        return "Carried to the base of the slope and treated as being in quicksand."


# Example Usage:
# Creating an instance of the Landslide class
landslide = Landslide()

# Simulating a landslide on a slope with a successful DEX check
damage_on_slope = landslide.landslide_damage_on_slope(dexterity_check=True)
print(f"Damage taken on slope: {damage_on_slope} HP")

# Simulating a landslide at the base of a cliff without shield protection
damage_at_cliff_base = landslide.landslide_damage_at_cliff_base()
print(f"Damage taken at cliff base: {damage_at_cliff_base} HP")

# Simulating the effect of a mudslide
mudslide_effect = Mudslide.mudslide_effect()
print(mudslide_effect)
