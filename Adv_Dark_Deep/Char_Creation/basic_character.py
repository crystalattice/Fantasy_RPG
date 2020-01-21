from collections import namedtuple
from dataclasses import dataclass, field
from typing import Type, Dict, Any, List

from Adv_Dark_Deep.Char_Creation import roll_abilities

dm_underdark = False  # Value to allow DM to allow Underdark (subterranean) races as player characters


@dataclass()
class Character:
    """Basic character information, common to all player characters"""
    strength: float = 0.0
    dexterity: int = 0
    intelligence: int = 0
    wisdom: int = 0
    constitution: int = 0
    charisma: int = 0

    save_vs_ppd: int = 0  # Save vs. poison, paralyzation, death
    save_vs_pp: int = 0  # Save vs. petrification, polymorph
    save_vs_bw: int = 0  # Save vs. breath weapon
    save_vs_rsw: int = 0  # Save vs. rods, staves, wands
    save_vs_spell: int = 0  # Save vs. magic spells and spell-like effects

    name: str = ""
    gender: str = ""
    race: str = ""
    subrace: str = ""  # If available, specific type of race, e.g. hill dwarf, high elf, etc.
    social_class: str = ""
    alignment: str = ""
    age: int = 0
    height: float = 0.0
    weight: int = 0
    special_abilities: List[str] = field(default_factory=list)
    experience: int = 0
    level: int = 0
    languages: List[str] = field(default_factory=list)

    armour_class: int = 0
    hit_points: int = 0
    non_lethal_wounds: int = 0
    armour_worn: str = ""
    init_mod: int = 0  # Initiative modifier
    surprise_mod: int = 0  # Modifier to be surprised
    attack_column: str = ""  # Attack column (Adv. Dark & Deep only)
    weapons: Dict[str, int] = field(default_factory=dict)

    skills: Dict[str, int] = field(default_factory=dict)
    class_abilities: Dict[str, int] = field(default_factory=dict)

    supplies: Dict[str, int] = field(default_factory=dict)  # Expendable items
    equipment: Dict[str, int] = field(default_factory=dict)  # Non-expendable items
    encumberance: int = 0  # Mass of all equipment, supplies, weapons, armour, etc.
    base_move: int = 0  # Unencumbered move rate
    move_rate: int = 0  # Current move rate
    magic_items: Dict[str, int] = field(default_factory=dict)

    deeds_titles: str = ""  # Estates, property, and named titles, e.g. Duke

    mount_name: str = ""
    mount_type: str = ""
    mount_hp: int = 0  # Hit points of mount
    mount_armour: str = ""
    mount_ac: int = 0  # Armour class of mount

    spells_memorized: List[str] = field(default_factory=list)
    spell_components: Dict[str, int] = field(default_factory=dict)
    max_spells_memorized: Dict[str, int] = field(default_factory=dict)  # Maximum number of spells memorized per level

    def ability_rolls(self, roll_method: int) -> None:
        """Roll the ability scores for the character.

        :type roll_method: int
        """
        if roll_method == 1:
            abil_scores: list = roll_abilities.three_d6()
        elif roll_method == 2:
            abil_scores = roll_abilities.four_d6_drop_lowest()
        elif roll_method == 3:
            abil_scores = roll_abilities.two_d6_plus_6()
        else:
            raise ValueError("Invalid selection")

        self.strength = abil_scores[0]
        self.dexterity = abil_scores[1]
        self.intelligence = abil_scores[2]
        self.wisdom = abil_scores[3]
        self.constitution = abil_scores[4]
        self.charisma = abil_scores[5]

    def char_name(self, name=None) -> None:
        """Name of the character"""
        if not name:
            self.name = input("Enter character's name: ")
        else:
            self.name = name

    def char_gender(self) -> None:
        """Sex of the character

        Currently, only male and female sex/gender is provided.
        """
        char_gender: str = input("Enter the character's sex [M/F]: ").upper()
        try:
            if char_gender == "M" or char_gender == "MALE":
                self.gender = "Male"
            elif char_gender == "F" or char_gender == "FEMALE":
                self.gender = "Female"
            else:
                raise ValueError("Invalid selection")
        except ValueError as e:
            print(e)

    def char_race(self) -> None:
        """Primary race of character, e.g. dwarf, elf, human, etc."""
        char_race: int = int(
            input("Enter the number for the primary race of your character [1: dwarf, 2: elf, 3: gnome, "
                  "4: halfling, 5: half-orc, 6: human]: "))
        try:
            if char_race == 1:
                self.race = "Dwarf"
                self.char_subrace(char_race)
            elif char_race == 2:
                self.race = "Elf"
            elif char_race == 3:
                self.race = "Gnome"
            elif char_race == 4:
                self.race = "Halfling"
            elif char_race == 5:
                self.race = "Half-Orc"
            elif char_race == 6:
                self.race = "Human"
            else:
                raise ValueError("Invalid selection")
        except ValueError as e:
            print(e)

    def char_subrace(self, race: int) -> None:
        """Selected subrace of character, if available"""
        if race == 1:
            subrace_choice: Dict[int, str] = {1: "Hill Dwarf", 2: "Mountain Dwarf"}
            if dm_underdark:
                subrace_choice[3] = "Grey Dwarf"
        elif race == 2:
            subrace_choice = {1: "Grey Elf", 2: "Half-Elf", 3: "High Elf", 4: "Wild Elf", 5: "Wood Elf"}
            if dm_underdark:
                subrace_choice[6] = "Dark Elf"
        elif race == 3:
            subrace_choice = {1: "Forest Gnome", 2: "Hill Gnome"}
            if dm_underdark:
                subrace_choice[3] = "Deep Gnome"

        subrace_num: int = int(input(f"Enter the subrace of your character {subrace_choice}"))

        self.subrace = subrace_choice[subrace_num]
