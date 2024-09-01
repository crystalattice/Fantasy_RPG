import random


class Henchman:
    def __init__(self, name, race, character_class, level=1):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.experience_points = 0
        self.loyalty = 100  # Loyalty is a percentage, starts at 100%

    def gain_experience(self, exp):
        # Henchmen gain 50% of the experience points
        gained_exp = exp * 0.5
        self.experience_points += gained_exp
        required_exp = [1000, 3000, 6000, 12000, 25000, 50000, 100000, 200000, 400000, 600000]
        if self.level < len(required_exp) and self.experience_points >= required_exp[self.level - 1]:
            self.level_up()

    def level_up(self):
        self.level += 1
        print(f"{self.name} has leveled up! Now at level {self.level}.")

    def adjust_loyalty(self, adjustment):
        self.loyalty += adjustment
        if self.loyalty > 100:
            self.loyalty = 100
        elif self.loyalty < 0:
            self.loyalty = 0
        print(f"{self.name}'s loyalty is now {self.loyalty}%.")

    def check_loyalty(self):
        if self.loyalty < 50:
            print(f"{self.name} is considering leaving due to low loyalty.")
        elif self.loyalty < 25:
            print(f"{self.name} is very likely to leave unless treated better soon.")


def find_henchmen(town_population, activity_level="normal"):
    if activity_level == "high":
        ratio = 200
    elif activity_level == "low":
        ratio = 5000
    else:
        ratio = 1000

    available_henchmen = town_population // ratio
    print(f"There are {available_henchmen} potential henchmen available in the town.")

    henchmen_list = []
    for _ in range(available_henchmen):
        race = determine_race()
        character_class = determine_class()
        name = generate_name(race)
        henchmen_list.append(Henchman(name, race, character_class))

    return henchmen_list


def determine_class():
    roll = random.randint(1, 100)
    if 1 <= roll <= 10:
        return "Bard"
    elif 11 <= roll <= 12:
        return "Jester"
    elif 13 <= roll <= 21:
        return "Cavalier"
    elif 22 <= roll <= 23:
        return "Paladin"
    elif 24 <= roll <= 35:
        return "Cleric"
    elif 36 <= roll <= 37:
        return "Druid"
    elif 38 <= roll <= 39:
        return "Mystic"
    elif 40 <= roll <= 68:
        return "Fighter"
    elif 69 <= roll <= 71:
        return "Barbarian"
    elif 72 <= roll <= 74:
        return "Ranger"
    elif 75 <= roll <= 85:
        return "Mage"
    elif 86 <= roll <= 87:
        return "Illusionist"
    elif 88 <= roll <= 89:
        return "Savant"
    elif 90 <= roll <= 98:
        return "Thief"
    else:
        return "Mountebank"


def determine_race():
    # A placeholder function, modify based on your game's racial composition
    races = ["Human", "Elf", "Dwarf", "Half-Elf", "Gnome", "Halfling", "Half-Orc"]
    return random.choice(races)


def generate_name(race):
    # A placeholder function for generating names, modify as needed
    if race == "Elf":
        return random.choice(["Elandril", "Lothariel", "Faelwen"])
    elif race == "Dwarf":
        return random.choice(["Thorin", "Borin", "Gloin"])
    elif race == "Human":
        return random.choice(["John", "Arthur", "Morgan"])
    elif race == "Half-Orc":
        return random.choice(["Grukk", "Thogg", "Morg"])
    # Add more names for other races
    return "Unknown"


# Example Usage
town_population = 10000
henchmen = find_henchmen(town_population, activity_level="normal")

# Example of interacting with a henchman
henchmen[0].gain_experience(500)
henchmen[0].adjust_loyalty(-10)
henchmen[0].check_loyalty()
