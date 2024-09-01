class Climbing:
    def __init__(self, base_climb_rate, base_success_chance):
        self.base_climb_rate = base_climb_rate  # Base climbing rate (feet/minute)
        self.base_success_chance = base_success_chance  # Base success chance (percentage)

    def attempt_climb(self, surface_condition):
        if surface_condition == "normal":
            climb_rate = self.base_climb_rate
            success_chance = self.base_success_chance
        elif surface_condition == "slightly_slippery":
            climb_rate = self.base_climb_rate / 2
            success_chance = self.base_success_chance / 2
        elif surface_condition == "very_slippery":
            climb_rate = self.base_climb_rate / 4
            success_chance = self.base_success_chance / 10
        else:
            print("Unknown surface condition.")
            return False

        print(f"Climbing at a rate of {climb_rate} feet per minute with a {success_chance}% chance of success.")

        roll = random.randint(1, 100)
        if roll <= success_chance:
            print("Climb successful!")
            return True
        else:
            print("Climb failed!")
            return False

# Example Usage
thief_climb = Climbing(base_climb_rate=18, base_success_chance=80)  # Example for a rough surface
mage_climb = Climbing(base_climb_rate=6, base_success_chance=40)    # Example for a smooth surface

# Attempting to climb different surfaces
thief_climb.attempt_climb("normal")
thief_climb.attempt_climb("slightly_slippery")
thief_climb.attempt_climb("very_slippery")

mage_climb.attempt_climb("normal")
mage_climb.attempt_climb("slightly_slippery")
mage_climb.attempt_climb("very_slippery")
