import json

# Original dictionaries
single_class = {
    "Dwarf, Grey": ("Cleric", "Fighter", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
    "Dwarf, Hill": ("Cleric", "Fighter", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
    "Elf, Dark (Drow)": ("Bard", "Cavalier", "Cleric", "Fighter", "Ranger", "Mage", "Savant", "Thief", "Thief-Acrobat",
                        "Mountebank", "Assassin"),
    "Half-Elf": ("Bard", "Cavalier", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Savant", "Thief",
                "Thief-Acrobat", "Mountebank", "Assassin"),
    "Human": ("Bard", "Jester", "Cavalier", "Paladin", "Cleric", "Druid", "Mystic", "Fighter", "Barbarian", "Ranger",
              "Mage", "Illusionist", "Savant", "Thief", "Thief-Acrobat", "Mountebank", "Assassin")
}

multi_class = {
    "Dwarf": (
        ("Cleric", "Fighter"),
        ("Cleric", "Thief"),
        ("Fighter", "Mountebank")
    ),
    "Elf, Dark (Drow)": (
        ("Cleric", "Fighter"),
        ("Cleric", "Fighter", "Mage"),
        ("Fighter", "Mage", "Thief")
    ),
    "Human": (
        ("Cleric", "Fighter"),
        ("Fighter", "Mage"),
        ("Mage", "Thief")
    )
}

# Combine into a single dictionary
race_classes = {"single_class": single_class, "multi_class": multi_class}

# Convert to JSON-compatible format
race_classes_json = {
    "single_class": {k: list(v) for k, v in single_class.items()},
    "multi_class": {k: [list(combination) for combination in v] for k, v in multi_class.items()}
}

# Save to a JSON file
output_file = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/character_creation/race_acceptable_classes.json"
with open(output_file, "w") as file:
    json.dump(race_classes_json, file, indent=4)
print(f"Converted race acceptable classes to {output_file}")
