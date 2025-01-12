import random

class Earthquake:
    def __init__(self, intensity):
        self.intensity = intensity

    def simulate_earthquake(self):
        if self.intensity == 'light':
            return self.light_earthquake()
        elif self.intensity == 'moderate':
            return self.moderate_earthquake()
        elif self.intensity == 'strong':
            return self.strong_earthquake()
        else:
            raise ValueError("Invalid intensity. Choose from 'light', 'moderate', or 'strong'.")

    def light_earthquake(self):
        duration = random.randint(1, 3)  # Light quakes last only a few seconds
        print(f"Light earthquake lasting {duration} seconds.")
        print("Effects:")
        print("- Ruins spell concentration.")
        print("- Thieves have a 50% chance of springing traps while disarming.")
        print("- Delicate activities are threatened.")
        return duration

    def moderate_earthquake(self):
        duration = random.randint(10, 15)  # 1d6+9 seconds, rarely up to 30 seconds
        if random.randint(1, 100) <= 30:
            duration = 30
        print(f"Moderate earthquake lasting {duration} seconds.")
        print("Effects:")
        print("- Affects an area up to 5 miles in radius.")
        print("- Climbing requires both DEX and STR checks with half the normal chance of success.")
        print("- Missile fire is done at a -5 penalty 'to hit'.")
        if random.randint(1, 100) <= 20:
            fissure_length = random.randint(6, 36)  # 6d6 yards
            fissure_depth = random.randint(6, 36)  # 6d6 feet
            print(f"- A fissure opens up, {fissure_length} yards long and {fissure_depth} feet deep.")
        else:
            print("- No fissure opens up.")
        return duration

    def strong_earthquake(self):
        duration = random.randint(40, 90)  # 1d6+3x10 seconds
        print(f"Strong earthquake lasting {duration} seconds.")
        print("Effects:")
        print("- Affects an area 12 to 100 miles in radius.")
        print("- Climbing is impossible.")
        print("- Melee combat has a -6 penalty 'to hit'.")
        print("- Missile fire is impossible.")
        if random.randint(1, 100) <= 40:
            fissure_length = random.randint(6, 36)  # 6d6 yards
            fissure_depth = random.randint(6, 36)  # 6d6 feet
            print(f"- A fissure opens up, {fissure_length} yards long and {fissure_depth} feet deep.")
        else:
            print("- No fissure opens up.")
        if random.randint(1, 100) <= 15:
            liquefaction_radius = random.randint(10, 40)  # 10-40 yards in radius
            print(f"- Soil liquefaction occurs in a {liquefaction_radius}-yard radius, turning it into quicksand.")
        else:
            print("- No soil liquefaction occurs.")
        return duration

# Example Usage:
earthquake_sim = Earthquake(intensity='strong')
earthquake_sim.simulate_earthquake()
