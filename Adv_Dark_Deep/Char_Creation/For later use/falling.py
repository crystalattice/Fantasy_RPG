from typing import Literal, Optional


class FallingDamage:
    """Class to handle falling damage based on various scenarios."""

    def __init__(self, distance: int, surface_type: Optional[str] = None, slope_type: Optional[str] = None):
        """
        Initialize with the distance fallen and optional surface or slope types.

        :param distance: Distance fallen in feet.
        :param surface_type: Type of surface ('rough', 'normal', 'smooth', 'soft').
        :param slope_type: Type of slope ('gentle', 'moderate').
        """
        self.distance = distance
        self.surface_type = surface_type
        self.slope_type = slope_type

    def calculate_vertical_fall_damage(self) -> int:
        """
        Calculate damage for a straight or near-vertical fall.

        :return: Damage in hit points.
        """
        if self.distance < 10:
            return 0

        damage = 0
        if self.distance <= 50:
            damage = (self.distance // 10) * 6
        else:
            damage = 5 * 6  # Damage for first 50 feet
            damage += sum(6 for _ in range(51, self.distance + 1, 10))

        return damage

    def calculate_slope_fall_damage(self) -> int:
        """
        Calculate damage for a fall down a slope based on surface and slope type.

        :return: Damage in hit points.
        """
        if not self.surface_type or not self.slope_type:
            raise ValueError("Both surface_type and slope_type must be specified for slope fall damage.")

        # Define base damage values
        base_damage = {
            'gentle': {
                'rough': (20, 50, 1, 3, 6),
                'normal': (30, 50, 1, 3, 6),
                'smooth': (40, 40, 1, 3, 3),
                'soft': (50, 50, 0, 0, 3)
            },
            'moderate': {
                'rough': (10, 40, 1, 6, 6),
                'normal': (20, 40, 1, 6, 6),
                'smooth': (30, 30, 1, 3, 6),
                'soft': (50, 50, 0, 0, 6)
            }
        }

        base_values = base_damage[self.slope_type][self.surface_type]
        initial_distance, additional_distance, dice_min, dice_initial, dice_additional = base_values

        if self.distance <= initial_distance:
            return 0

        damage = max((self.distance - initial_distance) // 10, 0) * dice_min
        if self.distance > additional_distance:
            damage += (self.distance - additional_distance) // 40 * dice_additional

        return damage

    def calculate_pit_fall_damage(self, pit_depth: int, spikes: bool = False) -> int:
        """
        Calculate damage from falling into a pit trap, with optional spike damage.

        :param pit_depth: Depth of the pit in feet.
        :param spikes: Whether the pit has spikes at the bottom.
        :return: Damage in hit points.
        """
        damage = self.calculate_vertical_fall_damage()

        if spikes:
            # Assuming the saving throw fails
            damage += 6  # 1d6 for spike damage

        return damage

    def calculate_water_fall_damage(self, swim_skill: bool = False) -> int:
        """
        Calculate damage from falling into water.

        :param swim_skill: Whether the character has swimming skill.
        :return: Damage in hit points.
        """
        if self.distance <= 20:
            return 0

        if swim_skill:
            max_safe_dive = 40
            if self.distance <= max_safe_dive:
                return 0
            else:
                penalty = (self.distance - max_safe_dive) // 10
                # Assume a failed skill check
                return penalty * 6  # 1d6 per 10 feet after 40 feet

        # For characters without swimming skill
        return self.calculate_vertical_fall_damage()


# Example Usage:
fall = FallingDamage(distance=60)
vertical_damage = fall.calculate_vertical_fall_damage()
print(f"Vertical Fall Damage: {vertical_damage} HP")

slope_fall = FallingDamage(distance=50, surface_type='rough', slope_type='moderate')
slope_damage = slope_fall.calculate_slope_fall_damage()
print(f"Slope Fall Damage: {slope_damage} HP")

pit_fall = FallingDamage(distance=30)
pit_damage = pit_fall.calculate_pit_fall_damage(pit_depth=30, spikes=True)
print(f"Pit Fall Damage: {pit_damage} HP")

water_fall = FallingDamage(distance=50)
water_damage = water_fall.calculate_water_fall_damage(swim_skill=True)
print(f"Water Fall Damage: {water_damage} HP")
