import random


class Disease:
    def __init__(self, constitution):
        self.constitution = constitution
        self.base_chance = 1  # Base 1% chance to contract a disease per week
        self.disease_data = [
            {"onset": "1d6 days", "effect": "-1 STR, -1 CON", "duration": "1d6 weeks", "fatality": 20},
            {"onset": "2d6 hours", "effect": "-1 INT, -1 DEX", "duration": "1d12 hours", "fatality": 50},
            {"onset": "4d6 hours", "effect": "-1 STR, -1 DEX, -1 CON, -1 CHA per month",
             "duration": "Continuous until any one statistic reaches 0", "fatality": 100},
            {"onset": "1d8 days", "effect": "Hearing loss", "duration": "1d3 weeks", "fatality": 10},
            {"onset": "2d4 days", "effect": "Blindness in one eye (-2 “to hit” with missile weapons)",
             "duration": "1d3 weeks", "fatality": 10},
            {"onset": "1d12 days", "effect": "Blindness", "duration": "1d3 weeks", "fatality": 10},
            {"onset": "1d6 days", "effect": "-1 DEX", "duration": "1d3 weeks", "fatality": 0},
            {"onset": "1d4 days", "effect": "-1 CON", "duration": "1d3 weeks", "fatality": 0},
            {"onset": "1d4 days", "effect": "-1 STR, -1 DEX", "duration": "1d12 months", "fatality": 10},
            {"onset": "1d8 days", "effect": "-1 CHA", "duration": "1d6 weeks", "fatality": 0},
            {"onset": "1d20 hours", "effect": "-1 DEX, -1 CON", "duration": "1d6 weeks", "fatality": 10},
            {"onset": "2d12 hours", "effect": "None", "duration": "1d6 weeks", "fatality": 10},
        ]

    def roll(self, dice_str):
        num, sides = map(int, dice_str.split('d'))
        return sum(random.randint(1, sides) for _ in range(num))

    def adjust_for_constitution(self):
        constitution_adjustments = {
            (3, 3): (2, 200, 2),
            (4, 6): (1, 150, 1),
            (7, 9): (0, 100, 0),
            (10, 12): (-1, 100, -1),
            (13, 15): (-2, 75, -2),
            (16, 17): (-3, 50, -3),
            (18, 18): (-4, 25, -4),
            (19, 22): (-7, 10, 0),
            (23, 25): (-10, 1, 0)
        }
        for key, value in constitution_adjustments.items():
            if self.constitution >= key[0] and self.constitution <= key[1]:
                return value
        return (0, 100, 0)  # Default no adjustment

    def contract_disease(self):
        contraction_adjustment, duration_adjustment, fatality_adjustment = self.adjust_for_constitution()

        # Base chance of contraction is modified by constitution adjustment
        contraction_chance = max(1, self.base_chance + contraction_adjustment)
        contracted = random.randint(1, 100) <= contraction_chance

        if not contracted:
            print("Character did not contract a disease.")
            return

        # Determine disease effects
        disease_roll = random.randint(1, 100)
        for index, disease in enumerate(self.disease_data):
            if disease_roll <= (index + 1) * (100 / len(self.disease_data)):
                onset = self.roll(disease['onset'])
                duration = self.roll(disease['duration']) * (duration_adjustment // 100)
                fatality_chance = max(0, disease['fatality'] + fatality_adjustment)
                break

        print(f"Disease contracted! Onset in {onset} days. Effect: {disease['effect']}. Duration: {duration} days.")

        # Determine fatality
        if random.randint(1, 100) <= fatality_chance:
            print("The disease was fatal.")
        else:
            print("The disease was not fatal.")

        # Chance for permanent effect
        if random.randint(1, 100) == 1:
            print("The disease left a permanent effect.")

    def contract_leprosy(self, contact_level):
        contact_chance = {
            "within 10 miles": 1 / 10000,
            "same room": 1,
            "same cup/bed": 2,
            "within 5'": 3,
            "physical contact": 10
        }
        if contact_level not in contact_chance:
            print("Invalid contact level.")
            return

        chance_to_contract = contact_chance[contact_level]
        if random.random() <= chance_to_contract / 100:
            print("Character contracted leprosy.")
            if random.randint(1, 100) <= 10:
                print("Leprosy was fatal within 1d6 months.")
            else:
                print("Leprosy was not fatal, but the character suffers permanent effects.")
        else:
            print("Character did not contract leprosy.")


# Example Usage:
character = Disease(constitution=14)
character.contract_disease()

# Example Usage for Leprosy:
character.contract_leprosy("same room")
