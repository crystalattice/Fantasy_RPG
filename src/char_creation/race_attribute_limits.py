import json
from collections import namedtuple

# Define the namedtuple structure
Ability_Limits = namedtuple("Ability_Limits", ["STR_min", "STR_max", "IQ_min", "IQ_max", "WIS_min", "WIS_max",
                                               "DEX_min", "DEX_max", "CON_min", "CON_max", "CHR_min", "CHR_max"])

# Define the racial ability limits for males and females
racial_limits = {
    "male": {
        "dwarf": Ability_Limits(8, 18, 3, 18, 3, 18, 3, 17, 12, 19, 3, 16),
        "dark_elf": Ability_Limits(3, 18, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18),
        "grey_elf": Ability_Limits(3, 18, 8, 19, 3, 18, 7, 18, 6, 18, 8, 18),
        "half_elf": Ability_Limits(3, 18, 4, 18, 3, 18, 6, 18, 6, 18, 3, 18),
        "high_elf": Ability_Limits(3, 18, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18),
        "wild_elf": Ability_Limits(3, 18, 7, 17, 3, 18, 7, 18, 6, 18, 8, 18),
        "wood_elf": Ability_Limits(3, 18, 7, 17, 3, 18, 7, 18, 6, 18, 8, 18),
        "gnome": Ability_Limits(6, 18, 7, 18, 3, 18, 3, 18, 8, 18, 3, 18),
        "halfling": Ability_Limits(6, 17, 6, 18, 3, 17, 8, 18, 10, 19, 3, 18),
        "half_orc": Ability_Limits(6, 18, 3, 17, 3, 14, 3, 17, 13, 19, 3, 12),
    },
    "female": {
        "dwarf": Ability_Limits(8, 17, 3, 18, 3, 18, 3, 17, 12, 19, 3, 16),
        "dark_elf": Ability_Limits(3, 16, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18),
        "grey_elf": Ability_Limits(3, 16, 8, 19, 3, 18, 7, 18, 6, 18, 8, 18),
        "half_elf": Ability_Limits(3, 17, 4, 18, 3, 18, 6, 18, 6, 18, 3, 18),
        "high_elf": Ability_Limits(3, 16, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18),
        "wild_elf": Ability_Limits(3, 17, 7, 17, 3, 18, 7, 18, 6, 18, 8, 18),
        "wood_elf": Ability_Limits(3, 16, 7, 17, 3, 18, 7, 18, 6, 18, 8, 18),
        "gnome": Ability_Limits(6, 15, 7, 18, 3, 18, 3, 18, 8, 18, 3, 18),
        "halfling": Ability_Limits(6, 14, 6, 18, 3, 17, 8, 18, 10, 19, 3, 18),
        "half_orc": Ability_Limits(6, 18, 3, 17, 3, 14, 3, 17, 13, 19, 3, 12),
    }
}

# Convert namedtuples to JSON-compatible format
race_attribute_limits = {
    gender: {
        race: {attr.split("_")[0]: [getattr(limits, f"{attr}_min"), getattr(limits, f"{attr}_max")]
               for attr in ["STR", "IQ", "WIS", "DEX", "CON", "CHR"]}
        for race, limits in races.items()
    }
    for gender, races in racial_limits.items()
}

# Save to JSON file
output_file = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/character_creation/race_attribute_limits.json"
with open(output_file, "w") as file:
    json.dump(race_attribute_limits, file, indent=4)
print(f"Converted race attribute limits to {output_file}")
