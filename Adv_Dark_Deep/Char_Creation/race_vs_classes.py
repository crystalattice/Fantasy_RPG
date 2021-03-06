single_class = {
    "dwarf, grey": ("Cleric", "Fighter", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
    "dwarf, hill": ("Cleric", "Fighter", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
    "dwarf, mountain": ("Cleric", "Fighter", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
    "elf, dark, male": ("Bard", "Cavalier", "Cleric", "Fighter", "Ranger", "Mage", "Savant", "Thief", "Thief-Acrobat",
                        "Mountebank", "Assassin"),
    "elf, dark, female": ("Bard", "Cavalier", "Cleric", "Fighter", "Ranger", "Mage", "Savant", "Thief", "Thief-Acrobat",
                          "Mountebank", "Assassin"),
    "elf, gray": ("Bard", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Savant", "Thief", "Thief-Acrobat",
                  "Assassin"),
    "elf, half": ("Bard", "Cavalier", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Savant", "Thief",
                  "Thief-Acrobat", "Mountebank", "Assassin"),
    "elf, high": ("Bard", "Cavalier", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Savant", "Thief",
                  "Thief-Acrobat", "Mountebank", "Assassin"),
    "elf, wild": ("Druid", "Mystic", "Fighter", "Thief", "Thief-Acrobat"),
    "elf, wood": ("Bard", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Thief", "Thief-Acrobat",
                  "Mountebank", "Assassin"),
    "gnome, deep": ("Bard", "Cleric", "Fighter", "Illusionist", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
    "gnome, forest": ("Bard", "Jester", "Druid", "Fighter", "Savant", "Thief", "Thief-Acrobat", "Mountebank",
                      "Assassin"),
    "gnome, hill": ("Bard", "Cleric", "Fighter", "Illusionist", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
    "halfling": ("Bard", "Jester", "Cleric", "Druid", "Mystic", "Fighter", "Thief", "Thief-Acrobat", "Mountebank",
                 "Assassin"),
    "half_orc": ("Cleric", "Fighter", "Barbarian", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
    "human": ("Bard", "Jester", "Cavalier", "Paladin", "Cleric", "Druid", "Mystic", "Fighter", "Barbarian", "Ranger",
              "Mage", "Illusionist", "Savant", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
}
multi_class = {
    "dwarf": (
        ("Cleric", "Fighter"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat")
    ),
    "elf, dark": (
        ("Cleric", "Fighter"),
        ("Cleric", "Fighter", "Mage"),
        ("Cleric", "Fighter", "Savant"),
        ("Cleric", "Mage"),
        ("Cleric", "Savant"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Fighter", "Mage"),
        ("Fighter", "Mage", "Thief"),
        ("Fighter", "Mage", "Thief-Acrobat"),
        ("Fighter", "Savant"),
        ("Fighter", "Savant", "Thief"),
        ("Fighter", "Savant", "Thief-Acrobat"),
        ("Fighter", "Savant", "Mountebank"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Mage", "Mountebank"),
        ("Mage", "Thief"),
        ("Mage", "Thief-Acrobat")
    ),
    "elf, gray": (
        ("Cleric", "Fighter"),
        ("Cleric", "Fighter", "Mage"),
        ("Cleric", "Ranger"),
        ("Cleric", "Ranger", "Mage"),
        ("Cleric", "Mage"),
        ("Cleric", "Savant"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Druid", "Ranger"),
        ("Fighter", "Mage", "Mountebank"),
        ("Fighter", "Mage", "Thief"),
        ("Fighter", "Mage", "Thief-Acrobat"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Savant", "Mountebank"),
        ("Fighter", "Savant", "Thief"),
        ("Fighter", "Savant", "Thief"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Mage", "Thief"),
        ("Mage", "Thief-Acrobat"),
        ("Mage", "Mountebank"),
        ("Savant", "Thief"),
        ("Savant", "Thief-Acrobat"),
        ("Savant", "Mountebank")
    ),
    "elf, high": (
        ("Cleric", "Fighter"),
        ("Cleric", "Fighter", "Mage"),
        ("Cleric", "Fighter", "Savant"),
        ("Cleric", "Mage"),
        ("Cleric", "Ranger"),
        ("Cleric", "Ranger", "Mage"),
        ("Cleric", "Ranger", "Savant"),
        ("Cleric", "Savant"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Druid", "Ranger"),
        ("Fighter", "Mage"),
        ("Fighter", "Mage", "Thief"),
        ("Fighter", "Mage", "Thief-Acrobat"),
        ("Fighter", "Mage", "Mountebank"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Savant"),
        ("Fighter", "Savant", "Thief"),
        ("Fighter", "Savant", "Thief-Acrobat"),
        ("Fighter", "Savant", "Mountebank"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Mage", "Thief"),
        ("Mage", "Thief-Acrobat"),
        ("Mage", "Mountebank"),
        ("Mystic", "Fighter"),
        ("Mystic", "Fighter", "Mage"),
        ("Mystic", "Mage"),
        ("Mystic", "Ranger"),
        ("Mystic", "Savant"),
        ("Mystic", "Thief"),
        ("Mystic", "Thief-Acrobat"),
        ("Ranger", "Mage"),
        ("Ranger", "Savant"),
        ("Savant", "Thief"),
        ("Savant", "Thief-Acrobat"),
        ("Savant", "Mountebank")
    ),
    "elf, wild": (
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat")
    ),
    "elf, wood": (
        ("Cleric", "Fighter"),
        ("Cleric", "Fighter", "Mage"),
        ("Cleric", "Ranger"),
        ("Cleric", "Ranger", "Mage"),
        ("Cleric", "Mage"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Druid", "Ranger"),
        ("Fighter", "Mage", "Mountebank"),
        ("Fighter", "Mage", "Thief"),
        ("Fighter", "Savant", "Thief-Acrobat"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Mage", "Thief"),
        ("Mage", "Thief-Acrobat"),
        ("Mage", "Mountebank"),
        ("Mystic", "Fighter"),
        ("Mystic", "Fighter", "Mage"),
        ("Mystic", "Mage"),
        ("Mystic", "Ranger"),
        ("Mystic", "Thief"),
        ("Mystic", "Thief-Acrobat")
    ),
    "gnome, deep": (
        ("Cleric", "Fighter"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Fighter", "Illusionist"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Illusionist", "Mountebank"),
        ("Illusionist", "Thief"),
        ("Illusionist", "Thief-Acrobat"),
        ("Jester", "Fighter"),
        ("Fighter", "Assassin"),
        ("Illusionist", "Assassin")
    ),
    "gnome, forest": (
        ("Druid", "Fighter"),
        ("Druid", "Thief"),
        ("Druid", "Thief-Acrobat"),
        ("Fighter", "Savant"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Illusionist", "Mountebank"),
        ("Jester", "Fighter"),
        ("Savant", "Thief"),
        ("Savant", "Mountebank"),
        ("Fighter", "Assassin"),
        ("Illusionist", "Assassin")
    ),
    "gnome, hill": (
        ("Cleric", "Fighter"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Druid", "Fighter"),
        ("Druid", "Thief"),
        ("Druid", "Thief-Acrobat"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Jester", "Thief"),
        ("Jester", "Thief-Acrobat"),
        ("Mystic", "Fighter"),
        ("Fighter", "Assassin"),
        ("Illusionist", "Assassin")
    ),
    "halfling": (
        ("Cleric", "Fighter"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Druid", "Fighter"),
        ("Druid", "Thief"),
        ("Druid", "Thief-Acrobat"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Jester", "Thief"),
        ("Jester", "Thief-Acrobat"),
        ("Mystic", "Fighter")
    ),
    "half-orc": (
        ("Cleric", "Fighter"),
        ("Cleric", "Mountebank"),
        ("Cleric", "Thief"),
        ("Cleric", "Thief-Acrobat"),
        ("Fighter", "Mountebank"),
        ("Fighter", "Thief"),
        ("Fighter", "Thief-Acrobat"),
        ("Fighter", "Assassin"),
        ("Cleric", "Assassin")
    ),
}
