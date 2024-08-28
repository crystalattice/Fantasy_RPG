class MagicResistance:
    def __init__(self, resistance_type, caster_level):
        self.resistance_type = resistance_type.upper()  # Resistance type from A to T
        self.caster_level = caster_level

    def get_resistance_percentage(self):
        table = {
            'A': [55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 0, 0, 0],
            'B': [60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 0, 0],
            'C': [65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, 0],
            'D': [70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0],
            'E': [75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
            'F': [80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10],
            'G': [85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15],
            'H': [90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20],
            'I': [95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25],
            'J': [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30],
            'K': [100, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35],
            'L': [100, 100, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40],
            'M': [100, 100, 100, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45],
            'N': [100, 100, 100, 100, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50],
            'O': [100, 100, 100, 100, 100, 100, 95, 90, 85, 80, 75, 70, 65, 60, 55],
            'P': [100, 100, 100, 100, 100, 100, 100, 95, 90, 85, 80, 75, 70, 65, 60],
            'Q': [100, 100, 100, 100, 100, 100, 100, 100, 95, 90, 85, 80, 75, 70, 65],
            'R': [100, 100, 100, 100, 100, 100, 100, 100, 100, 95, 90, 85, 80, 75, 70],
            'S': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 95, 90, 85, 80, 75],
            'T': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 95, 90, 85, 80]
        }

        # Validate caster level
        if self.caster_level < 1 or self.caster_level > 15:
            raise ValueError("Caster level must be between 1 and 15.")

        # Validate resistance type
        if self.resistance_type not in table:
            raise ValueError(f"Invalid resistance type: {self.resistance_type}. Must be between 'A' and 'T'.")

        return table[self.resistance_type][self.caster_level - 1]

    def roll_resistance(self):
        from random import randint
        resistance_percentage = self.get_resistance_percentage()
        roll = randint(1, 100)
        print(f"Roll: {roll} - Resistance Percentage: {resistance_percentage}%")
        return roll <= resistance_percentage


# Example usage:
# Create an instance of MagicResistance with resistance type 'G' and caster level 10
magic_resistance = MagicResistance('G', 10)

# Check if the creature resists the magic
if magic_resistance.roll_resistance():
    print("The magic was resisted!")
else:
    print("The magic took effect!")
