from typing import Literal, Optional


class ExtremeTemperature:
    """Class to handle effects of extreme temperatures on characters."""

    def __init__(self, temperature: int, environment: Optional[str] = None):
        """
        Initialize with temperature and optional environment.

        :param temperature: The current temperature in Fahrenheit.
        :param environment: Type of environment ('cold', 'heat', or None).
        """
        self.temperature = temperature
        self.environment = environment

    def calculate_cold_damage(self, wind: bool = False, exposed: bool = False) -> int:
        """
        Calculate damage per minute due to cold temperatures.

        :param wind: Whether there is wind, doubling the damage.
        :param exposed: Whether hands, feet, or face are exposed.
        :return: Damage in hit points per minute.
        """
        damage_per_minute = max((self.temperature + 1) // -10, 0)
        if wind:
            damage_per_minute *= 2

        if exposed and damage_per_minute > 0:
            frostbite_threshold = 8
            frostbite_damage = 8 // damage_per_minute
            if frostbite_damage > 0:
                return frostbite_damage

        return damage_per_minute

    def calculate_heat_damage(self, constitution_check_failed: bool = False, heat_stroke: bool = False) -> int:
        """
        Calculate damage per 30 minutes due to heat.

        :param constitution_check_failed: Whether the constitution check has failed.
        :param heat_stroke: Whether the character is suffering from heat stroke.
        :return: Damage in hit points per 30 minutes.
        """
        if self.temperature < 100:
            return 0

        damage_per_30_minutes = max((self.temperature - 95) // 5, 1)

        if constitution_check_failed:
            if heat_stroke:
                # Heat stroke: Lose 1 point of constitution every 30 minutes.
                return damage_per_30_minutes

            # Damage taken due to heat exhaustion.
            return damage_per_30_minutes

        return 0

    def calculate_armor_temperature_adjustment(self,
                                               armor_type: Literal['brigandine', 'leather_cuirass', 'steel_cuirass',
                                               'furs', 'gambeson', 'jousting_plate',
                                               'leather_lamellar', 'steel_lamellar', 'mail',
                                               'plate', 'plated_mail', 'ring', 'leather_scale',
                                               'steel_scale'], environment: Literal['cold', 'heat']) -> int:
        """
        Calculate temperature adjustment due to armor.

        :param armor_type: Type of armor worn.
        :param environment: Environment type ('cold' or 'heat').
        :return: Temperature adjustment in Fahrenheit.
        """
        armor_effects = {
            'brigandine': {'cold': 5, 'heat': 20},
            'leather_cuirass': {'cold': 0, 'heat': 5},
            'steel_cuirass': {'cold': 0, 'heat': 5},
            'furs': {'cold': 15, 'heat': 25},
            'gambeson': {'cold': 25, 'heat': 45},
            'jousting_plate': {'cold': 15, 'heat': 35},
            'leather_lamellar': {'cold': 5, 'heat': 15},
            'steel_lamellar': {'cold': 0, 'heat': 10},
            'mail': {'cold': 5, 'heat': 15},
            'plate': {'cold': 15, 'heat': 35},
            'plated_mail': {'cold': 15, 'heat': 30},
            'ring': {'cold': 5, 'heat': 10},
            'leather_scale': {'cold': 5, 'heat': 15},
            'steel_scale': {'cold': 5, 'heat': 15}
        }

        return armor_effects[armor_type][environment]
