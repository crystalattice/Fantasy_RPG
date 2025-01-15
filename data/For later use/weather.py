import random


class Weather:
    """
    A class to simulate weather conditions, including temperature, cloud cover, wind speed, fog, sandstorms, and tornadoes.
    """

    def __init__(self):
        self.temperature = self.roll_temperature()
        self.cloud_cover, self.precipitation = self.roll_cloud_cover_precipitation()
        self.wind_speed, self.missile_modifier = self.roll_wind_speed()
        self.fog = self.check_for_fog()
        self.sandstorm = False
        self.tornado = False

    def roll_temperature(self) -> tuple[str, int]:
        """
        Determine the temperature and the modifier for the next roll.

        :return: A tuple containing the temperature description and its corresponding modifier for the next roll.
        """
        roll = random.randint(1, 100)
        if roll <= 5:
            return "Sweltering", -15
        elif 6 <= roll <= 15:
            return "Hot", -10
        elif 16 <= roll <= 30:
            return "Warm", -5
        elif 31 <= roll <= 70:
            return "Average", 0
        elif 71 <= roll <= 85:
            return "Cool", +5
        elif 86 <= roll <= 95:
            return "Cold", +10
        else:
            return "Bitter cold", +15

    def roll_cloud_cover_precipitation(self) -> tuple[str, str]:
        """
        Determine the cloud cover and precipitation.

        :return: A tuple containing the cloud cover description and the type of precipitation.
        """
        roll = random.randint(1, 100)
        if roll <= 10:
            return "Very clear", "None"
        elif 11 <= roll <= 50:
            return "Clear", "None"
        elif 51 <= roll <= 65:
            return "Light clouds/hazy", "None"
        elif 66 <= roll <= 80:
            return "Partly cloudy", "None"
        elif 81 <= roll <= 90:
            return "Heavy clouds", "Fog"
        elif 91 <= roll <= 95:
            return "Heavy clouds", "Light rain/mist/snow/hail"
        else:
            return "Heavy clouds", "Heavy rain/snow/hail/sleet"

    def roll_wind_speed(self) -> tuple[str, dict[str, int]]:
        """
        Determine the wind speed and its effect on missile weapon accuracy.

        :return: A tuple containing the wind speed description and a dictionary of missile weapon accuracy modifiers by range.
        """
        roll = random.randint(1, 100)
        if roll <= 10:
            return "Dead calm", {"Short": 0, "Medium": 0, "Long": 0}
        elif 11 <= roll <= 35:
            return "Calm", {"Short": 0, "Medium": 0, "Long": 0}
        elif 36 <= roll <= 75:
            return "Light breeze", {"Short": 0, "Medium": 0, "Long": 0}
        elif 76 <= roll <= 89:
            return "Light wind", {"Short": -1, "Medium": -2, "Long": -3}
        elif 90 <= roll <= 99:
            return "Strong wind", {"Short": -2, "Medium": -3, "Long": -4}
        elif roll == 100:
            return "Gale", {"Short": -4, "Medium": "**", "Long": "**"}

    def check_for_fog(self) -> bool:
        """
        Determine if fog is present based on the temperature and season.

        :return: Boolean indicating if fog is present.
        """
        fog_chance = {
            "Spring": {"Cold": 35, "Hot": 25},
            "Summer": {"Cold": 45, "Cool": 35},
            "Autumn": {"Cold": 25, "Hot": 35},
            "Winter": {"Cool": 35, "Hot": 45},
        }
        season = random.choice(["Spring", "Summer", "Autumn", "Winter"])
        temp = self.temperature[0]

        if temp in fog_chance.get(season, {}):
            return random.randint(1, 100) <= fog_chance[season][temp]
        return False

    def simulate_sandstorm(self):
        """
        Simulate the effects of a sandstorm.
        """
        self.sandstorm = True
        print("A sandstorm is occurring! All creatures suffer -2 'to hit' in melee. Missile combat is impossible.")
        choking = random.randint(1, 6) == 1
        if choking:
            print("Someone is choking on the sand! They will suffocate in 1d6+2 minutes if not protected.")

    def simulate_tornado(self):
        """
        Simulate the effects of a tornado.
        """
        self.tornado = True
        damage = sum(random.randint(1, 20) for _ in range(4))
        print(f"A tornado has hit! All caught in it take {damage} hp damage from flying debris.")
        height = sum(random.randint(1, 6) for _ in range(10))
        distance = sum(random.randint(1, 6) for _ in range(10)) * 100
        print(f"They are lifted {height} feet in the air and carried {distance} yards before being dropped!")

    def tornado_damage_to_structure(self, structure_type: str) -> tuple[str, int]:
        """
        Calculate damage to structures caused by a tornado.

        :param structure_type: The type of structure (Wood, Sod, Wood & Stone, Stone).
        :return: A tuple of the effect on the structure and the damage to occupants.
        """
        roll = random.randint(1, 6)
        if structure_type == "Wood":
            roll += 0
        elif structure_type == "Sod":
            roll -= 1
        elif structure_type == "Wood & Stone":
            roll -= 2
        elif structure_type == "Stone":
            roll -= 3

        damage = 0
        if roll <= 1:
            return "No effect", damage
        elif roll == 2:
            damage = sum(random.randint(1, 6) for _ in range(3))
            return "Structure damaged", damage
        elif roll == 3:
            damage = sum(random.randint(1, 8) for _ in range(3))
            return "Structure destroyed", damage
        elif roll == 4:
            damage = sum(random.randint(1, 10) for _ in range(3))
            return "Structure destroyed", damage
        elif roll == 5:
            damage = sum(random.randint(1, 10) for _ in range(3))
            return "Structure destroyed", damage
        elif roll >= 6:
            damage = sum(random.randint(1, 10) for _ in range(3))
            return "Structure destroyed", damage

# Example Usage:
weather = Weather()
print(f"Temperature: {weather.temperature[0]}")
print(f"Cloud Cover: {weather.cloud_cover}")
print(f"Precipitation: {weather.precipitation}")
print(f"Wind Speed: {weather.wind_speed}")
print(f"Missile Modifiers: {weather.missile_modifier}")
print(f"Fog: {weather.fog}")

# Simulate sandstorm and tornado
weather.simulate_sandstorm()
weather.simulate_tornado()

# Calculate tornado damage to different structure types
structure_type = "Wood & Stone"
effect, occupant_damage = weather.tornado_damage_to_structure(structure_type)
print(f"Structure Type: {structure_type} | Effect: {effect} | Occupant Damage: {occupant_damage} hp")
