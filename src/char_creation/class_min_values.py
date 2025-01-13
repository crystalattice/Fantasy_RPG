import json

# Original data from class_min_attribs.py
class_min_attribs = {
    "bard": {"dex": 14, "chr": 14},
    "jester": {"iq": 13, "dex": 13, "chr": 13},
    "cavalier": {"str": 14, "dex": 14, "con": 14, "iq": 10, "wis": 10},
    "paladin": {"str": 14, "dex": 14, "con": 14, "iq": 10, "wis": 13, "chr": 17},
    "cleric": {"wis": 9},
    "druid": {"wis": 12, "chr": 15},
    "mystic": {"wis": 13, "dex": 9},
    "fighter": {"str": 9, "con": 7},
    "barbarian": {"str": 15, "dex": 14, "con": 15, "wis": 16},
    "ranger": {"iq": 13, "wis": 14, "con": 14},
    "mage": {"iq": 9, "dex": 6},
    "illusionist": {"dex": 16, "iq": 15},
    "savant": {"iq": 14, "wis": 12},
    "thief": {"dex": 9},
    "thief_acrobat": {"str": 15, "dex": 16},
    "mountebank": {"dex": 9, "iq": 10, "chr": 12},
    "assassin": {"str": 12, "dex": 12, "iq": 11}
}

# Convert to JSON and save to file
output_file = "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/character_creation/class_min_attribs.json"
with open(output_file, "w") as file:
    json.dump(class_min_attribs, file, indent=4)
print(f"Converted class minimum attributes to {output_file}")
