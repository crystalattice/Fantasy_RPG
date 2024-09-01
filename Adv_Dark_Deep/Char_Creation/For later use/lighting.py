class LightSource:
    def __init__(self, name, range_ft, duration_minutes):
        self.name = name
        self.range_ft = range_ft  # Light range in feet
        self.duration_minutes = duration_minutes  # Duration in minutes
        self.remaining_minutes = duration_minutes

    def use_light(self, minutes_used):
        self.remaining_minutes -= minutes_used
        if self.remaining_minutes <= 0:
            print(f"{self.name} has burned out.")
            return False
        else:
            print(f"{self.name} has {self.remaining_minutes} minutes of light remaining.")
            return True

class DungeonWithLight(Dungeon):
    def __init__(self, encounter_chance=1, interval=60, noisy=False):
        super().__init__(encounter_chance, interval, noisy)
        self.light_sources = []

    def add_light_source(self, light_source):
        self.light_sources.append(light_source)
        print(f"Added light source: {light_source.name} with a range of {light_source.range_ft}' and duration of {light_source.duration_minutes} minutes.")

    def start_exploration(self, duration_hours):
        total_minutes = duration_hours * 60
        for minute in range(0, total_minutes, self.interval):
            hour = minute // 60 + 1
            print(f"\nHour {hour} in the dungeon:")
            self.check_for_encounter()

            if self.noisy:
                print("The party is making noise, increasing the chance of an encounter...")
                self.check_for_encounter()

            for light in self.light_sources:
                if not light.use_light(self.interval):
                    self.light_sources.remove(light)
                    print(f"The party is now without a {light.name}.")

            if not self.light_sources:
                print("The party is now in total darkness!")
                break

            time.sleep(1)

    def camp_out(self, duration_hours):
        print("\nThe party is camping out in the dungeon...")
        self.start_exploration(duration_hours)


# Example Usage
torch = LightSource(name="Torch", range_ft=30, duration_minutes=60)
lantern = LightSource(name="Lantern", range_ft=60, duration_minutes=240)

dungeon = DungeonWithLight(encounter_chance=1, interval=60, noisy=False)
dungeon.add_light_source(torch)
dungeon.add_light_source(lantern)

# Simulate dungeon exploration for 5 hours
dungeon.start_exploration(duration_hours=5)

# Simulate camping out in the dungeon for 8 hours
dungeon.camp_out(duration_hours=8)
