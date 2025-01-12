import random

class VolcanicEruption:
    """
    A class to represent the different types of volcanic eruptions and their effects.
    """

    def __init__(self):
        self.eruption_type = self.determine_eruption_type()

    def determine_eruption_type(self) -> tuple[str, int]:
        """
        Determine the type of volcanic eruption and its duration.

        :return: A tuple containing the type of eruption and its duration in days or weeks.
        """
        roll = random.randint(1, 20)
        if roll == 1:
            return "Explosion", 1  # 1 day
        elif 2 <= roll <= 5:
            return "Lava", sum(random.randint(1, 6) for _ in range(2))  # 2d6 days
        elif 6 <= roll <= 8:
            return "Lava plus explosion", sum(random.randint(1, 4) for _ in range(2))  # 2d4 days
        elif 9 <= roll <= 11:
            return "Ash", random.randint(2, 5) + random.randint(1, 4)  # 1d4+2 weeks
        elif 12 <= roll <= 14:
            return "Ash", random.randint(1, 3)  # 1d3 weeks
        elif 15 <= roll <= 17:
            return "Ash plus lava", (random.randint(1, 3), sum(random.randint(1, 6) for _ in range(2)))  # Ash: 1d3 weeks, Lava: 2d6 days
        elif 18 <= roll <= 19:
            return "Ash plus poison gas", (random.randint(1, 3), 1)  # Ash: 1d3 weeks, Gas: 1 day
        elif roll == 20:
            return "Ash plus explosion", (random.randint(1, 3), 1)  # Ash: 1d3 weeks, Explosion: 1 day

    def explosion_damage(self, distance_yards: int) -> tuple[int, int]:
        """
        Calculate the chance of being hit and the damage based on distance from the explosion.

        :param distance_yards: The distance in yards from the explosion.
        :return: A tuple of the chance of being hit (as a percentage) and the damage in d6.
        """
        if distance_yards <= 100:
            return 45, 12 * random.randint(1, 6)
        elif 101 <= distance_yards <= 200:
            return 40, 11 * random.randint(1, 6)
        elif 201 <= distance_yards <= 300:
            return 35, 10 * random.randint(1, 6)
        elif 301 <= distance_yards <= 400:
            return 30, 9 * random.randint(1, 6)
        elif 401 <= distance_yards <= 500:
            return 25, 8 * random.randint(1, 8)
        elif 501 <= distance_yards <= 600:
            return 20, 7 * random.randint(1, 6)
        elif 601 <= distance_yards <= 700:
            return 15, 5 * random.randint(1, 6)
        elif 701 <= distance_yards <= 800:
            return 10, 4 * random.randint(1, 6)
        elif 801 <= distance_yards <= 900:
            return 5, 3 * random.randint(1, 6)
        elif 901 <= distance_yards <= 1000:
            return 1, 2 * random.randint(1, 6)
        else:
            return 0, 0  # Out of range

    def ash_damage(self, distance_yards: int) -> tuple[int, bool]:
        """
        Calculate the damage from burning ash and determine if the character must make a saving throw.

        :param distance_yards: The distance in yards from the volcanic eruption.
        :return: A tuple of the damage in d3 per 10 minutes and a boolean indicating if a saving throw is required.
        """
        if distance_yards <= 2000:
            return random.randint(1, 3), True
        return 0, False

    def choking_damage(self) -> int:
        """
        Calculate the damage from choking on volcanic ash.

        :return: The damage in d4 per minute.
        """
        return random.randint(1, 4)

# Example Usage:
eruption = VolcanicEruption()
eruption_type, duration = eruption.eruption_type
print(f"Eruption Type: {eruption_type} | Duration: {duration}")

# Calculate damage from an explosion at a certain distance
distance = 250  # Example distance in yards
chance, damage = eruption.explosion_damage(distance)
print(f"Distance: {distance} yards | Chance of Being Hit: {chance}% | Damage: {damage} hp")

# Calculate damage from ash at a certain distance
ash_distance = 1500  # Example distance in yards
ash_damage, requires_save = eruption.ash_damage(ash_distance)
print(f"Distance: {ash_distance} yards | Ash Damage: {ash_damage} hp per 10 minutes | Requires Save: {requires_save}")

# Calculate choking damage from ash
if requires_save:
    choking_damage = eruption.choking_damage()
    print(f"Choking Damage: {choking_damage} hp per minute")
