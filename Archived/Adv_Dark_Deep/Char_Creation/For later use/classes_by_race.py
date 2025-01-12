from dataclasses import dataclass, field
from typing import Dict, Tuple, List

@dataclass
class RaceClasses:
    single_class: Dict[str, Tuple[str, ...]] = field(default_factory=dict)
    multi_class: Dict[str, List[Tuple[str, ...]]] = field(default_factory=dict)

    def __post_init__(self):
        self.single_class = {
            "Dwarf, Grey": ("Cleric", "Fighter", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
            "Dwarf, Hill": ("Cleric", "Fighter", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
            "Dwarf, Mountain": ("Cleric", "Fighter", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
            "Elf, Dark (Drow)": ("Bard", "Cavalier", "Cleric", "Fighter", "Ranger", "Mage", "Savant", "Thief", "Thief-Acrobat",
                                "Mountebank", "Assassin"),
            "Elf, Grey": ("Bard", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Savant", "Thief", "Thief-Acrobat",
                          "Assassin"),
            "Half-Elf": ("Bard", "Cavalier", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Savant", "Thief",
                          "Thief-Acrobat", "Mountebank", "Assassin"),
            "Elf, High": ("Bard", "Cavalier", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Savant", "Thief",
                          "Thief-Acrobat", "Mountebank", "Assassin"),
            "Elf, Wild": ("Druid", "Mystic", "Fighter", "Thief", "Thief-Acrobat"),
            "Elf, Wood": ("Bard", "Cleric", "Druid", "Mystic", "Fighter", "Ranger", "Mage", "Thief", "Thief-Acrobat",
                          "Mountebank", "Assassin"),
            "Gnome, Deep (Svirfneblin)": ("Bard", "Cleric", "Fighter", "Illusionist", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
            "Gnome, Forest": ("Bard", "Jester", "Druid", "Fighter", "Savant", "Thief", "Thief-Acrobat", "Mountebank",
                              "Assassin"),
            "Gnome, Hill": ("Bard", "Cleric", "Fighter", "Illusionist", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
            "Halfling": ("Bard", "Jester", "Cleric", "Druid", "Mystic", "Fighter", "Thief", "Thief-Acrobat", "Mountebank",
                         "Assassin"),
            "Half-Orc": ("Cleric", "Fighter", "Barbarian", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
            "Human": ("Bard", "Jester", "Cavalier", "Paladin", "Cleric", "Druid", "Mystic", "Fighter", "Barbarian", "Ranger",
                      "Mage", "Illusionist", "Savant", "Thief", "Thief-Acrobat", "Mountebank", "Assassin"),
        }

        self.multi_class = {
            "Dwarf": [
                ("Cleric", "Fighter"),
                ("Cleric", "Thief"),
                ("Cleric", "Thief-Acrobat"),
                ("Fighter", "Mountebank"),
                ("Fighter", "Thief"),
                ("Fighter", "Thief-Acrobat")
            ],
            "Elf, Dark (Drow)": [
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
            ],
            "Elf, Grey": [
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
            ],
            "Elf, High": [
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
            ],
            "Elf, Wild": [
                ("Fighter", "Thief"),
                ("Fighter", "Thief-Acrobat")
            ],
            "Elf, Wood": [
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
            ],
            "Gnome, Deep (Svirfneblin)": [
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
            ],
            "Gnome, Forest": [
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
            ],
            "Gnome, Hill": [
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
            ],
            "Halfling": [
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
            ],
            "Half-Orc": [
                ("Cleric", "Fighter"),
                ("Cleric", "Mountebank"),
                ("Cleric", "Thief"),
                ("Cleric", "Thief-Acrobat"),
                ("Fighter", "Mountebank"),
                ("Fighter", "Thief"),
                ("Fighter", "Thief-Acrobat"),
                ("Fighter", "Assassin"),
                ("Cleric", "Assassin")
            ],
        }

    def get_single_class_options(self, race: str) -> Tuple[str, ...]:
        return self.single_class.get(race, ())

    def get_multi_class_options(self, race: str) -> List[Tuple[str, ...]]:
        return self.multi_class.get(race, [])


# Example usage:
if __name__ == "__main__":
    rc = RaceClasses()
    print("Single class options for 'Elf, High':", rc.get_single_class_options("Elf, High"))
    print("Multi-class options for 'Elf, High':", rc.get_multi_class_options("Elf, High"))
