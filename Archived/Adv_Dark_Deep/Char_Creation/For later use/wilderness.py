import random


class WildernessTravel:
    def __init__(self, terrain, party_size, near_settlement=False, road=False):
        self.terrain = terrain
        self.party_size = party_size
        self.near_settlement = near_settlement
        self.road = road
        self.encounter_chance = self.calculate_encounter_chance()
        self.lost_chance = self.calculate_lost_chance()

    def calculate_encounter_chance(self):
        # Determine base encounter chance based on terrain
        terrain_encounter_chance = {
            "plain": 10,
            "scrub": 10,
            "forest": 5,
            "desert": 5,
            "hills": 5,
            "mountains": 5,
            "marsh": 5,
            "road": 15
        }
        chance = terrain_encounter_chance.get(self.terrain, 0)

        if self.road:
            chance += 15
        if self.near_settlement:
            chance += 10 if self.near_settlement == "within 5 miles" else 8

        return chance

    def calculate_lost_chance(self):
        # Determine base lost chance based on terrain
        terrain_lost_chance = {
            "plain": 10,
            "scrub": 30,
            "forest": 70,
            "desert": 40,
            "hills": 20,
            "mountains": 50,
            "marsh": 60
        }
        chance = terrain_lost_chance.get(self.terrain, 0)

        if self.near_settlement:
            chance -= 5

        return chance

    def check_encounter(self):
        roll = random.randint(1, 100)
        if roll <= self.encounter_chance:
            print("Random encounter! Roll on the appropriate table.")
        else:
            print("No encounter.")

    def check_if_lost(self, weather_clear=True):
        if not weather_clear:
            self.lost_chance += 20

        roll = random.randint(1, 100)
        if roll <= self.lost_chance:
            direction_roll = random.randint(1, 12)
            directions = ["Forward-right", "Right", "Back-right", "Backwards",
                          "Back-left", "Left", "Forward-left"]
            new_direction = directions[(direction_roll - 1) // 2]
            print(f"The party is lost and is heading {new_direction}.")
        else:
            print("The party is not lost.")

    def forced_march(self, on_foot=True):
        if on_foot:
            speed_increase = 1 / 3
            constitution_check = random.choice([True, False])
            if not constitution_check:
                print("Forced march successful, but party members take 1 HP damage.")
            else:
                print("Forced march successful, no damage taken.")
        else:
            speed_increase = 0.2
            lameness_check = random.randint(1, 100)
            if lameness_check <= 10:
                lame_percentage = random.randint(1, 10)
                lame_animals = max(1, int(self.party_size * (lame_percentage / 100.0)))
                print(f"Forced march successful, but {lame_animals} animal(s) went lame.")
            else:
                print("Forced march successful, no animals went lame.")

        print(f"Speed increased by {speed_increase * 100:.1f}%.")


# Example Usage:
terrain = "forest"
party_size = 30
near_settlement = "within 5 miles"
road = True

travel = WildernessTravel(terrain, party_size, near_settlement, road)
travel.check_encounter()
travel.check_if_lost(weather_clear=False)
travel.forced_march(on_foot=False)
