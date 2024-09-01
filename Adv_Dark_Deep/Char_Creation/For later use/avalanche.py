import random


class Avalanche:
    def __init__(self, size, location):
        self.size = size  # small, medium, large
        self.location = location  # base of slope, slope itself

    def roll_damage(self, dice_str):
        num, sides = map(int, dice_str.split('d'))
        return sum(random.randint(1, sides) for _ in range(num))

    def resolve(self):
        damage_table = {
            "small": {"base of slope": "2d10", "slope": "3d10"},
            "medium": {"base of slope": "2d12", "slope": "3d12"},
            "large": {"base of slope": "2d20", "slope": "3d20"}
        }

        damage_roll = self.roll_damage(damage_table[self.size][self.location])
        print(f"A {self.size} avalanche on the {self.location} does {damage_roll} damage!")

        # Determine if the character is carried away
        if self.location == "slope":
            if random.randint(1, 100) <= 50:  # 50% chance if taking cover
                print("Character is carried away by the avalanche!")
            else:
                print("Character was not carried away by the avalanche.")

        # Constitution check to avoid suffocation
        con_check = random.randint(1, 20)
        if con_check > 10:  # Assuming 10 as a CON value check threshold
            print("Character is unconscious and will suffocate in 1d6+4 minutes.")
            suffocation_time = random.randint(1, 6) + 4
            print(f"Suffocation time: {suffocation_time} minutes")
        else:
            print("Character remains conscious after the avalanche.")

        # Chance of locating a buried comrade
        int_check = random.randint(1, 20)
        intelligence = random.randint(1, 20)  # Example Intelligence score
        base_chance = 10
        locate_chance = base_chance + intelligence + (25 if con_check <= 10 else 0)

        if random.randint(1, 100) <= locate_chance:
            print("Successfully located a buried comrade.")
        else:
            print("Failed to locate a buried comrade.")


# Example Usage:
avalanche = Avalanche(size="large", location="slope")
avalanche.resolve()
