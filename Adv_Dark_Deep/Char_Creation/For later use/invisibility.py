class Invisibility:
    def __init__(self, intelligence, level_or_hit_dice):
        self.intelligence = intelligence
        self.level_or_hit_dice = level_or_hit_dice

    def detect_invisible(self):
        detection_chance = self.calculate_detection_chance()
        if detection_chance > 0:
            print(f"Detection Chance: {detection_chance}%")
            detected = self.roll_detection(detection_chance)
            if detected:
                return "Invisible creature or object detected! Attack rolls suffer a -4 penalty, and the invisible creature gets a +4 bonus to saving throws."
            else:
                return "Invisible creature or object not detected."
        else:
            return "No chance to detect invisible creatures or objects."

    def calculate_detection_chance(self):
        table = [
            [0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 5, 10],
            [0, 0, 0, 0, 0, 5, 10, 15],
            [0, 0, 0, 0, 5, 10, 15, 25],
            [0, 0, 0, 5, 10, 15, 25, 35],
            [0, 0, 5, 10, 15, 25, 35, 45],
            [0, 5, 10, 25, 35, 45, 55, 55],
            [5, 10, 15, 35, 45, 55, 65, 75],
            [10, 15, 20, 45, 55, 65, 80, 95]
        ]

        intelligence_column = self.get_intelligence_column(self.intelligence)
        level_row = self.get_level_row(self.level_or_hit_dice)

        if intelligence_column is None or level_row is None:
            return 0

        return table[level_row][intelligence_column]

    def get_intelligence_column(self, intelligence):
        if intelligence >= 0 and intelligence <= 1:
            return 0
        elif intelligence >= 2 and intelligence <= 4:
            return 1
        elif intelligence >= 5 and intelligence <= 7:
            return 2
        elif intelligence >= 8 and intelligence <= 10:
            return 3
        elif intelligence >= 11 and intelligence <= 12:
            return 4
        elif intelligence >= 13 and intelligence <= 14:
            return 5
        elif intelligence >= 15 and intelligence <= 16:
            return 6
        elif intelligence >= 17:
            return 7
        else:
            return None

    def get_level_row(self, level_or_hit_dice):
        if level_or_hit_dice >= 7 and level_or_hit_dice <= 7:
            return 0
        elif level_or_hit_dice == 8:
            return 1
        elif level_or_hit_dice == 9:
            return 2
        elif level_or_hit_dice == 10:
            return 3
        elif level_or_hit_dice == 11:
            return 4
        elif level_or_hit_dice == 12:
            return 5
        elif level_or_hit_dice == 13:
            return 6
        elif level_or_hit_dice == 14:
            return 7
        elif level_or_hit_dice >= 15:
            return 8
        else:
            return None

    def roll_detection(self, detection_chance):
        from random import randint
        roll = randint(1, 100)
        print(f"Roll: {roll}")
        return roll <= detection_chance

# Example usage:
# Create an instance of Invisibility with intelligence score of 13 and level/hit dice of 10
invisibility = Invisibility(intelligence=13, level_or_hit_dice=10)

# Check if the invisible creature or object is detected
print(invisibility.detect_invisible())
