import random

class MoltenLava:
    """
    A class to represent the mechanics of molten lava and its effects on characters.
    """

    def __init__(self):
        self.no_skin_damage_far = 6  # 1d6 damage for distances 200-500 yards with no skin
        self.no_skin_damage_near = 12 # 2d6 damage for distances 5-200 yards with no skin
        self.with_skin_damage_close = 6  # 1d6 damage per round after the first round for distances up to 5 yards with skin

    def damage_from_distance(self, distance: int, lava_skin: bool = False) -> int:
        """
        Calculate the damage a character takes based on their distance from molten lava.

        :param distance: The distance of the character from the lava in yards.
        :param lava_skin: Whether the lava is covered with a "skin" or not.
        :return: Total damage per round or segment based on proximity to the lava.
        """
        if not lava_skin:
            if 200 <= distance <= 500:
                return random.randint(1, self.no_skin_damage_far)  # 1d6 damage per round
            elif 5 <= distance < 200:
                return random.randint(2, self.no_skin_damage_near)  # 2d6 damage per round
            elif distance < 5:
                return random.randint(2, self.no_skin_damage_near) * 2  # 2d6 damage per segment (2 segments per round)
        else:
            if distance < 5:
                return random.randint(1, self.with_skin_damage_close)  # 1d6 damage per round after the 1st round

        return 0  # No damage if outside of the damage radius or if lava is skinned and far away

    @staticmethod
    def contact_with_lava(has_escape_option: bool) -> int:
        """
        Calculate the damage when a character falls into molten lava.

        :param has_escape_option: Whether the character has an option to escape the lava.
        :return: Damage taken based on whether the character escapes or not.
        """
        if has_escape_option:
            # Saving throw success: 10d6 damage and escape
            return random.randint(10, 60)  # 10d6 damage
        else:
            # No escape: Fatal outcome
            return -1  # Indicates death

# Example Usage:
# Creating an instance of the MoltenLava class
lava = MoltenLava()

# Simulating damage based on distance from molten lava with no skin
damage_at_distance = lava.damage_from_distance(distance=100)
print(f"Damage taken at 100 yards from lava (no skin): {damage_at_distance} HP per round")

# Simulating damage based on distance from molten lava with skin
damage_close_to_skin = lava.damage_from_distance(distance=3, lava_skin=True)
print(f"Damage taken at 3 yards from lava (with skin): {damage_close_to_skin} HP per round")

# Simulating contact with molten lava with a successful escape
damage_on_contact = lava.contact_with_lava(has_escape_option=True)
if damage_on_contact == -1:
    print("Character failed to escape from lava and perished.")
else:
    print(f"Damage taken from contact with lava (successful escape): {damage_on_contact} HP")

# Simulating contact with molten lava without escape
damage_on_contact_no_escape = lava.contact_with_lava(has_escape_option=False)
if damage_on_contact_no_escape == -1:
    print("Character failed to escape from lava and perished.")
else:
    print(f"Damage taken from contact with lava (no escape): {damage_on_contact_no_escape} HP")
