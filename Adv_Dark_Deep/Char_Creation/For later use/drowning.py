import random


class Drowning:
    def __init__(self, strength, constitution, encumbrance='none'):
        self.strength = strength
        self.constitution = constitution
        self.encumbrance = encumbrance
        self.time_treading = self.calculate_treading_time()
        self.time_holding_breath = self.calculate_breath_time()

    def calculate_treading_time(self):
        """Calculate time the character can tread water based on encumbrance."""
        if self.encumbrance == 'none':
            return self.strength * 10
        elif self.encumbrance == 'moderate':
            return (self.strength * 10) // 2
        elif self.encumbrance == 'heavy':
            return (self.strength * 10) // 4
        else:
            raise ValueError("Invalid encumbrance level. Choose from 'none', 'moderate', or 'heavy'.")

    def tread_water(self):
        """Simulate treading water."""
        minutes_treaded = 0
        while minutes_treaded < self.time_treading:
            print(f"Minute {minutes_treaded + 1}: Treading water successfully.")
            minutes_treaded += 1

        print("Treading time exhausted. Making STR checks to keep treading.")
        while True:
            if self.strength_check():
                print(f"Minute {minutes_treaded + 1}: Succeeded in treading water.")
                minutes_treaded += 1
            else:
                print(f"Minute {minutes_treaded + 1}: Failed to tread water. Character starts drowning.")
                return False

    def strength_check(self):
        """Simulate a strength check."""
        roll = random.randint(1, 20)
        return roll <= self.strength

    def calculate_breath_time(self):
        """Calculate time the character can hold their breath based on Constitution."""
        return self.constitution

    def hold_breath(self, combat=False, unprepared=False):
        """Simulate holding breath underwater."""
        time_modifier = 1
        if combat:
            time_modifier *= 0.5
        if unprepared:
            time_modifier *= 0.5

        total_time = int(self.time_holding_breath * time_modifier)
        print(f"Character can hold breath for {total_time} minutes under current conditions.")

        for minute in range(1, total_time + 1):
            print(f"Minute {minute}: Holding breath successfully.")

        penalty = 2
        while True:
            if self.constitution_check(penalty):
                print(f"Minute {total_time + 1}: Succeeded in holding breath, with a +{penalty} penalty.")
                total_time += 1
                penalty += 2
            else:
                print(f"Minute {total_time + 1}: Failed to hold breath, character starts drowning.")
                return False

    def constitution_check(self, penalty):
        """Simulate a constitution check with a penalty."""
        roll = random.randint(1, 20)
        return roll <= (self.constitution - penalty)


# Example Usage:
character = Drowning(strength=14, constitution=14, encumbrance='moderate')
character.tread_water()
character.hold_breath(combat=True, unprepared=False)
