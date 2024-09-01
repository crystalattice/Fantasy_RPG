import random

class Pursuit:
    def __init__(self, pursuer_speed, pursued_speed, pursuer_sight, pursued_sight):
        self.pursuer_speed = pursuer_speed
        self.pursued_speed = pursued_speed
        self.pursuer_sight = pursuer_sight
        self.pursued_sight = pursued_sight

    def dungeon_pursuit(self):
        if self.pursuer_speed < self.pursued_speed:
            give_up_sight = 100
            give_up_out_of_sight = 50
            give_up_time = 5
        elif self.pursuer_speed == self.pursued_speed:
            give_up_sight = 150
            give_up_out_of_sight = 80
            give_up_time = 10
        else:
            return "Pursuit is not possible. The pursued is too fast."

        return {
            "give_up_sight": give_up_sight,
            "give_up_out_of_sight": give_up_out_of_sight,
            "give_up_time": give_up_time
        }

    def wilderness_pursuit(self, terrain_type, modifiers, actively_hiding=False):
        base_chance = 50

        terrain_modifiers = {
            "close": -30,
            "open": 50,
            "semi-open": -10
        }

        for mod, value in modifiers.items():
            base_chance += value

        base_chance += terrain_modifiers.get(terrain_type, 0)

        if actively_hiding:
            base_chance -= 10  # additional penalty for actively hiding

        base_chance = max(0, min(100, base_chance))  # ensure chance is between 0% and 100%

        return base_chance

    def tracking_movement(self, tracking_chance, light_condition):
        movement_speed = 0

        if tracking_chance >= 71:
            movement_speed = 75 if light_condition == "good" else 67
        elif 31 <= tracking_chance <= 70:
            movement_speed = 67 if light_condition == "good" else 50
        elif tracking_chance <= 30:
            movement_speed = 50 if light_condition == "good" else 25

        return movement_speed

# Example Usage:

# Dungeon/City Pursuit
dungeon_pursuit = Pursuit(pursuer_speed=60, pursued_speed=90, pursuer_sight=True, pursued_sight=True)
pursuit_result = dungeon_pursuit.dungeon_pursuit()

if pursuit_result:
    print(f"Give up pursuit when in sight if distance exceeds {pursuit_result['give_up_sight']} feet.")
    print(f"Give up pursuit when out of sight if distance exceeds {pursuit_result['give_up_out_of_sight']} feet.")
    print(f"Pursuers will give up after {pursuit_result['give_up_time']} minutes if they cannot catch the pursued.")

# Wilderness/Village Pursuit
modifiers = {
    "rain_snow_hours": -25,
    "night_dark": -50,
    "open_terrain": 50,
    "pursued_force_less_legs": -10,
    "pursuing_force_ranger": 30,  # Example where ranger is level 2 (+30%)
}

wilderness_pursuit = Pursuit(pursuer_speed=60, pursued_speed=90, pursuer_sight=True, pursued_sight=True)
tracking_chance = wilderness_pursuit.wilderness_pursuit(terrain_type="open", modifiers=modifiers, actively_hiding=False)
print(f"Tracking success chance: {tracking_chance}%")

# Tracking Movement Speed
movement_speed = wilderness_pursuit.tracking_movement(tracking_chance=tracking_chance, light_condition="good")
print(f"Movement speed while tracking: {movement_speed}% of normal speed")
