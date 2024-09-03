import random


class Hunting:
    """
    A class to simulate the process of hunting, including locating prey and taking it down.
    """

    def __init__(self, terrain: str, season: str, number_of_hunters: int = 1):
        self.terrain = terrain.capitalize()
        self.season = season.capitalize()
        self.number_of_hunters = number_of_hunters
        self.prey_found = False
        self.prey_type = None
        self.prey_number = 0
        self.range = 0
        self.threat_encountered = False

    def locate_prey(self) -> bool:
        """
        Determine if prey is found based on the terrain, season, and number of hunters.

        :return: Boolean indicating if prey was found.
        """
        terrain_chances = {
            "Plains": {"Spring": 40, "Summer": 50, "Autumn": 50, "Winter": 25},
            "Forest": {"Spring": 50, "Summer": 50, "Autumn": 50, "Winter": 30},
            "Hills": {"Spring": 40, "Summer": 40, "Autumn": 40, "Winter": 25},
            "Mountains": {"Spring": 30, "Summer": 30, "Autumn": 30, "Winter": 15},
            "Desert": {"Spring": 5, "Summer": 5, "Autumn": 5, "Winter": 10},
            "Marsh": {"Spring": 35, "Summer": 50, "Autumn": 50, "Winter": 20},
        }

        base_chance = terrain_chances.get(self.terrain, {}).get(self.season, 0)
        adjusted_chance = max(5, base_chance - 5 * (self.number_of_hunters - 1))
        roll = random.randint(1, 100)
        self.prey_found = roll <= adjusted_chance
        return self.prey_found

    def encounter_prey(self):
        """
        Determine the type of prey encountered if prey is found.

        :return: None
        """
        if not self.prey_found:
            return

        roll = random.randint(1, 6)
        prey_types = {
            1: ("Bird", random.randint(3, 6) * 10),
            2: ("Bird", random.randint(1, 6) * 10),
            3: ("Animal", random.randint(1, 10) * 10),
            4: ("Animal", random.randint(1, 6) * 30 + 50),
            5: ("Animal", random.randint(1, 3) * 30 + 30),
            6: ("Threat", random.randint(1, 3) * 30 + 30)
        }
        self.prey_type, self.range = prey_types[roll]
        self.threat_encountered = self.prey_type == "Threat"
        self.prey_number = roll

    def hunt(self):
        """
        Execute the hunting process, including locating prey and determining the encounter details.

        :return: Dictionary containing the details of the hunt.
        """
        hunting_duration = random.randint(1, 6)  # Time spent hunting in hours
        hunt_successful = self.locate_prey()
        self.encounter_prey()

        hunt_details = {
            "Hunting Duration (hours)": hunting_duration,
            "Prey Found": hunt_successful,
            "Prey Type": self.prey_type,
            "Prey Number": self.prey_number,
            "Range (yards)": self.range,
            "Threat Encountered": self.threat_encountered
        }
        return hunt_details

    def food_acquired(self) -> int:
        """
        Calculate the amount of food acquired from the hunt based on the prey type.

        :return: The number of days' worth of food acquired.
        """
        if not self.prey_found:
            return 0

        if self.prey_type == "Bird":
            return self.prey_number  # Each bird feeds 1 person for 1 day
        elif self.prey_type == "Animal":
            if self.prey_number > 1:
                return self.prey_number * 10  # Big game feeds 10 days per animal
            else:
                return random.randint(1, 4)  # Small game feeds 1-4 days per animal
        elif self.threat_encountered:
            return random.randint(10, 20)  # Threat-type animals provide more food

        return 0


# Example Usage:
hunting_trip = Hunting(terrain="Forest", season="Summer", number_of_hunters=2)
hunt_results = hunting_trip.hunt()
food_acquired = hunting_trip.food_acquired()

print(f"Hunting Results: {hunt_results}")
print(f"Food Acquired (days): {food_acquired}")
