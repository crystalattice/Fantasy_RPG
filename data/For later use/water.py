import random

class Swimming:
    def __init__(self, armor_type, weight_carried):
        self.armor_type = armor_type
        self.weight_carried = weight_carried

    def can_swim(self):
        # Determine if swimming is possible based on armor type
        swim_ability = {
            "none": True,
            "helmet only": True,
            "leather cuirass": "awkward",
            "furs": "awkward",
            "gambeson": "awkward",
            "leather lamellar": "awkward",
            "ring armor": False,
            "brigandine armor": False,
            "leather scale": "awkward",
            "steel cuirass": "awkward",
            "steel lamellar": False,
            "steel scale": False,
            "mail": False,
            "plated mail": False,
            "plate armor": False,
            "jousting plate": False
        }

        swim_status = swim_ability.get(self.armor_type, False)
        if swim_status == True:
            print(f"Swimming is possible with {self.armor_type}.")
            return True
        elif swim_status == "awkward":
            print(f"Swimming is possible but awkward with {self.armor_type}.")
            return "awkward"
        else:
            print(f"Swimming is not possible with {self.armor_type}.")
            return False

    def check_drowning(self):
        swim_status = self.can_swim()
        if swim_status == "awkward":
            drowning_chance = 5 + (self.weight_carried // 5) * 2
            if self.weight_carried >= 20:
                print("The character will sink automatically due to excess weight.")
            else:
                roll = random.randint(1, 100)
                if roll <= drowning_chance:
                    print(f"Character drowns! Rolled {roll} against a drowning chance of {drowning_chance}%.")
                else:
                    print(f"Character swims successfully! Rolled {roll} against a drowning chance of {drowning_chance}%.")
        elif swim_status == True:
            print("Character swims successfully with no risk of drowning.")

class Underwater:
    def __init__(self, depth, water_type):
        self.depth = depth
        self.water_type = water_type

    def visibility(self):
        # Determine visibility based on depth and water type
        visibility_chart = {
            "fresh": [(10, 50), (20, 40), (30, 30), (40, 20), (50, 10), (60, 0), (70, 0), (80, 0), (90, 0), (100, 0)],
            "salt": [(10, 100), (20, 90), (30, 80), (40, 70), (50, 60), (60, 50), (70, 40), (80, 30), (90, 20), (100, 10)]
        }
        visibility_depths = visibility_chart.get(self.water_type, [])
        for vis_range in visibility_depths:
            if self.depth <= vis_range[0]:
                print(f"Visibility at {self.depth}' depth in {self.water_type} water: {vis_range[1]}'.")
                return vis_range[1]
        print(f"No visibility at {self.depth}' depth in {self.water_type} water.")
        return 0

    def combat_penalties(self, is_native=False):
        # Combat penalties for non-native underwater creatures
        if not is_native:
            print("Non-native underwater creature faces a +15 initiative penalty.")
        else:
            print("Native underwater creature has no initiative penalty.")

    def multiple_attackers(self, attacker_size, defender_size):
        # Determine how many attackers can engage a single defender underwater
        attack_chart = {
            "small": {"small": 8, "medium": 12, "large": 18},
            "medium": {"small": 6, "medium": 8, "large": 12},
            "large": {"small": 3, "medium": 6, "large": 8}
        }
        max_attackers = attack_chart.get(attacker_size, {}).get(defender_size, 0)
        print(f"{max_attackers} {attacker_size} attackers can engage a {defender_size} defender in underwater combat.")

    def backstab(self, from_below=True):
        if from_below:
            print("Attack from below! +4 to hit and thieves can backstab as if from behind.")
        else:
            print("Normal attack direction.")

# Example Usage:

# Swimming Example
swimming_character = Swimming("leather cuirass", 10)
swimming_character.check_drowning()

# Underwater Example
underwater_travel = Underwater(30, "salt")
underwater_travel.visibility()
underwater_travel.combat_penalties(is_native=False)
underwater_travel.multiple_attackers("small", "medium")
underwater_travel.backstab(from_below=True)
