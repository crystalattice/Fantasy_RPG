import random
import time

class Dungeon:
    def __init__(self, encounter_chance=1, interval=60, noisy=False):
        self.encounter_chance = encounter_chance  # Chance of encounter (e.g., 1 in 6)
        self.interval = interval  # Time between checks in minutes
        self.noisy = noisy  # If the party is making noise, encounter chance is increased

    def check_for_encounter(self):
        roll = random.randint(1, 6)
        encounter = roll <= self.encounter_chance
        print(f"Rolling for encounter... (Roll: {roll})")

        if encounter:
            print("Random encounter occurs!")
            self.handle_encounter()
        else:
            print("No encounter.")

    def handle_encounter(self):
        # Define encounter logic here, e.g., generating a random monster or event
        # This could be expanded to include different types of encounters
        print("You encounter a wandering monster!")

    def start_exploration(self, duration_hours):
        for hour in range(duration_hours):
            print(f"\nHour {hour + 1} in the dungeon:")
            self.check_for_encounter()

            if self.noisy:
                print("The party is making noise, increasing the chance of an encounter...")
                self.check_for_encounter()

            time.sleep(1)  # Simulates time passing, adjust for real-time or skip in actual gameplay

    def camp_out(self, duration_hours):
        print("\nThe party is camping out in the dungeon...")
        self.start_exploration(duration_hours)


# Example Usage
dungeon = Dungeon(encounter_chance=1, interval=60, noisy=False)

# Simulate dungeon exploration for 5 hours
dungeon.start_exploration(duration_hours=5)

# Simulate camping out in the dungeon for 8 hours
dungeon.camp_out(duration_hours=8)
