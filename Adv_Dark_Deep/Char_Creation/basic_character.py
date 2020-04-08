from dataclasses import dataclass, field
from typing import Dict, List

from Adv_Dark_Deep.Char_Creation import roll_abilities, race_vs_class, race_vs_multiclass
from Adv_Dark_Deep.dice_roller import multi_die


@dataclass()
class Character:
    """Basic character information, common to all player characters"""
    def __init__(self, strength=0.0, dexterity=0, intelligence=0, wisdom=0, constitution=0, charisma=0,
                 ppd_save=0, pp_save=0, bw_save=0, rsw_save=0, spell_save=0, name="", gender="", race="",
                 dm_underdark=False, social_class="", alignment="", char_class=None, experience=0.0, level=0,
                 armour_class=0, hit_points=0, non_lethal_wounds=0, armour_worn="", init_mod=0, surprise_mod=0,
                 attack_column="", weapons=None, skills=None, class_abilities=None, supplies=None, equipment=None,
                 encumbrance=0, move_rate=0, magic_items=None, deeds_titles="",  spells_memorized=None, spell_components=None,
                 max_spells_memorized=None, subrace="", age=0, height=0.0, weight=0, special_abilities=None,
                 languages=None, base_move=0, want_multiclass=False, approved_classes=None):
        # TODO: Remove init() method and move default values to variable assignment

        # Generic information for all characters
        self._strength: float = strength
        self._dexterity: int = dexterity
        self._intelligence: int = intelligence
        self._wisdom: int = wisdom
        self._constitution: int = constitution
        self._charisma: int = charisma

        self._ppd_save: int = ppd_save  # Save vs. poison, paralyzation, death
        self._pp_save: int = pp_save  # Save vs. petrification, polymorph
        self._bw_save: int = bw_save  # Save vs. breath weapon
        self._rsw_save: int = rsw_save  # Save vs. rods, staves, wands
        self._spell_save: int = spell_save  # Save vs. magic spells and spell-like effects

        self._name: str = name
        self._gender: str = gender
        self._race: str = race
        self._dm_underdark = dm_underdark  # DM allows Underdark (subterranean) races as player characters

        self._social_class: str = social_class
        self._alignment: str = alignment
        self._experience: float = experience
        self._level: int = level

        if char_class is None:  # Corrects mutable argument
            char_class = {}
        self._char_class: Dict[str, int] = char_class  # Dictionary in case PC is multi/dual classed

        self._armour_class: int = armour_class
        self._hit_points: int = hit_points
        self._non_lethal_wounds: int = non_lethal_wounds
        self._armour_worn: str = armour_worn
        self._init_mod: int = init_mod  # Initiative modifier
        self._surprise_mod: int = surprise_mod  # Modifier to be surprised
        self._attack_column: str = attack_column  # Attack column (Adv. Dark & Deep only)

        if weapons is None:
            weapons = {}
        self._weapons: Dict[str, int] = weapons

        if skills is None:
            skills = {}
        self._skills: Dict[str, int] = skills

        if class_abilities is None:
            class_abilities = {}
        self._class_abilities: Dict[str, int] = class_abilities

        if supplies is None:
            supplies = {}
        self._supplies: Dict[str, int] = supplies  # Expendable items

        if equipment is None:
            equipment = {}
            self._equipment: Dict[str, int] = equipment  # Non-expendable items

        self._encumbrance: int = encumbrance  # Mass of all equipment, supplies, weapons, armour, etc.
        self._move_rate: int = move_rate  # Current move rate

        if magic_items is None:
            magic_items = {}
        self._magic_items: Dict[str, int] = magic_items

        self._deeds_titles: str = deeds_titles  # Estates, property, and named titles, e.g. Duke

        if spells_memorized is None:
            spells_memorized = []
        self._spells_memorized: List[str] = spells_memorized

        if spell_components is None:
            spell_components = {}
        self._spell_components: Dict[str, int] = spell_components

        if max_spells_memorized is None:
            max_spells_memorized = {}
        self._max_spells_memorized: Dict[str, int] = max_spells_memorized  # Maximum number of spells memorized per level

        # Race-specific information
        self._subrace: str = subrace  # If available, specific type of race, e.g. hill dwarf, high elf, etc.
        self._age: int = age
        self._height: float = height
        self._weight: int = weight

        if special_abilities is None:
            special_abilities = []
        self._special_abilities: List[str] = special_abilities

        if languages is None:
            languages = []
        self._languages: List[str] = languages

        self._base_move: int = base_move  # Unencumbered move rate
        self._want_multiclass: bool = want_multiclass

        if approved_classes is None:
            approved_classes = []
        self._approved_classes: List[str] = approved_classes

    # Properties
    @property
    def strength(self) -> float:
        return self._strength

    @strength.setter
    def strength(self, value: float) -> None:
        self._strength = value

    @property
    def dexterity(self) -> int:
        return self._dexterity

    @dexterity.setter
    def dexterity(self, value: int) -> None:
        self._dexterity = value

    @property
    def intelligence(self) -> int:
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value: int) -> None:
        self._intelligence = value

    @property
    def wisdom(self) -> int:
        return self._wisdom

    @wisdom.setter
    def wisdom(self, value: int) -> None:
        self._wisdom = value

    @property
    def constitution(self) -> int:
        return self._constitution

    @constitution.setter
    def constitution(self, value: int) -> None:
        self._constitution = value

    @property
    def charisma(self) -> int:
        return self._charisma

    @charisma.setter
    def charisma(self, value: int) -> None:
        self._charisma = value

    @property
    def ppd_save(self) -> int:
        return self._ppd_save

    @ppd_save.setter
    def ppd_save(self, value: int) -> None:
        self._ppd_save = value

    @property
    def pp_save(self) -> int:
        return self._pp_save

    @pp_save.setter
    def pp_save(self, value: int) -> None:
        self._pp_save = value

    @property
    def rsw_save(self) -> int:
        return self._rsw_save

    @rsw_save.setter
    def rsw_save(self, value: int) -> None:
        self._rsw_save = value

    @property
    def bw_save(self) -> int:
        return self._bw_save

    @bw_save.setter
    def bw_save(self, value: int) -> None:
        self._bw_save = value

    @property
    def spell_save(self) -> int:
        return self._spell_save

    @spell_save.setter
    def spell_save(self, value: int) -> None:
        self._spell_save = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: int) -> None:
        self._name = value

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, value: str) -> None:
        self._gender = value

    @property
    def race(self) -> str:
        return self._race

    @race.setter
    def race(self, value: str) -> None:
        self._race = value

    @property
    def dm_underdark(self) -> bool:
        return self._dm_underdark

    @dm_underdark.setter
    def dm_underdark(self, value: bool) -> None:
        self._dm_underdark = value

    @property
    def social_class(self) -> str:
        return self._social_class

    @social_class.setter
    def social_class(self, value: str) -> None:
        self._social_class = value

    @property
    def alignment(self) -> str:
        return self._alignment

    @alignment.setter
    def alignment(self, value: str) -> None:
        self._alignment = value

    @property
    def experience(self) -> float:
        return self._experience

    @experience.setter
    def experience(self, value: float) -> None:
        self._experience = value

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int) -> None:
        self._level = value

    @property
    def char_class(self) -> dict:
        return self._char_class

    @char_class.setter
    def char_class(self, value: dict) -> None:
        self._char_class = value

    @property
    def armour_class(self) -> int:
        return self._armour_class

    @armour_class.setter
    def armour_class(self, value: int) -> None:
        self._armour_class = value

    @property
    def hit_points(self) -> int:
        return self._hit_points

    @hit_points.setter
    def hit_points(self, value: int) -> None:
        self._hit_points = value

    @property
    def non_lethal_wounds(self) -> int:
        return self._non_lethal_wounds

    @non_lethal_wounds.setter
    def non_lethal_wounds(self, value: int) -> None:
        self._non_lethal_wounds = value

    @property
    def armour_worn(self) -> str:
        return self._armour_worn

    @armour_worn.setter
    def armour_worn(self, value: str) -> None:
        self._armour_worn = value

    @property
    def init_mod(self) -> int:
        return self._init_mod

    @init_mod.setter
    def init_mod(self, value: int) -> None:
        self._init_mod = value

    @property
    def surprise_mod(self) -> int:
        return self._surprise_mod

    @surprise_mod.setter
    def surprise_mod(self, value: int) -> None:
        self._surprise_mod = value

    @property
    def attack_column(self) -> str:
        return self._attack_column

    @attack_column.setter
    def attack_column(self, value: str) -> None:
        self._attack_column = value

    @property
    def weapons(self) -> dict:
        return self._weapons

    @weapons.setter
    def weapons(self, value: dict) -> None:
        self._weapons = value

    @property
    def skills(self) -> dict:
        return self._skills

    @skills.setter
    def skills(self, value: dict) -> None:
        self._skills = value

    @property
    def class_abilities(self) -> dict:
        return self._class_abilities

    @class_abilities.setter
    def class_abilities(self, value: dict) -> None:
        self._class_abilities = value

    @property
    def supplies(self) -> dict:
        return self._supplies

    @supplies.setter
    def supplies(self, value: dict) -> None:
        self._supplies = value

    @property
    def equipment(self) -> dict:
        return self._equipment

    @equipment.setter
    def equipment(self, value: dict) -> None:
        self._equipment = value

    @property
    def encumbrance(self) -> int:
        return self._encumbrance

    @encumbrance.setter
    def encumbrance(self, value: int) -> None:
        self._encumbrance = value

    @property
    def move_rate(self) -> int:
        return self._move_rate

    @move_rate.setter
    def move_rate(self, value: int) -> None:
        self._move_rate = value

    @property
    def magic_items(self) -> dict:
        return self._magic_items

    @magic_items.setter
    def magic_items(self, value: dict) -> None:
        self._magic_items = value

    @property
    def deeds_titles(self) -> str:
        return self._deeds_titles

    @deeds_titles.setter
    def deeds_titles(self, value: str) -> None:
        self._deeds_titles = value

    @property
    def spells_memorized(self) -> list:
        return self._spells_memorized

    @spells_memorized.setter
    def spells_memorized(self, value: list) -> None:
        self._spells_memorized = value

    @property
    def spell_components(self) -> dict:
        return self._spell_components

    @spell_components.setter
    def spell_components(self, value: dict) -> None:
        self._spell_components = value

    @property
    def max_spells_memorized(self) -> dict:
        return self._max_spells_memorized

    @max_spells_memorized.setter
    def max_spells_memorized(self, value: dict) -> None:
        self._max_spells_memorized = value

    @property
    def subrace(self) -> str:
        return self._subrace

    @subrace.setter
    def subrace(self, value: str) -> None:
        self._subrace = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def weight(self) -> int:
        return self._weight

    @weight.setter
    def weight(self, value: int) -> None:
        self._weight = value

    @property
    def special_abilities(self) -> list:
        return self._special_abilities

    @special_abilities.setter
    def special_abilities(self, value: list) -> None:
        self._special_abilities = value

    @property
    def languages(self) -> list:
        return self._languages

    @languages.setter
    def languages(self, value: list) -> None:
        self._languages = value

    @property
    def base_move(self) -> int:
        return self._base_move

    @base_move.setter
    def base_move(self, value: int) -> None:
        self._base_move = value

# TODO: Figure out if want_multiclass is necessary
    @property
    def want_multiclass(self) -> bool:
        return self._want_multiclass

    @want_multiclass.setter
    def want_multiclass(self, value: bool) -> None:
        self._want_multiclass = value

    @property
    def approved_classes(self) -> list:
        return self._approved_classes

    @approved_classes.setter
    def approved_classes(self, value: list) -> None:
        self._approved_classes = value

    # Normal methods
    def ability_rolls(self, roll_method: int) -> None:
        """Roll the ability scores for the character.

        :type roll_method: int
        """
        if roll_method == 1:
            ability_scores: list = roll_abilities.three_d6()
        elif roll_method == 2:
            ability_scores = roll_abilities.four_d6_drop_lowest()
        elif roll_method == 3:
            ability_scores = roll_abilities.two_d6_plus_6()
        else:
            raise ValueError("Invalid selection")

        self.strength = ability_scores[0]
        self.dexterity = ability_scores[1]
        self.intelligence = ability_scores[2]
        self.wisdom = ability_scores[3]
        self.constitution = ability_scores[4]
        self.charisma = ability_scores[5]

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
            raise  # Re-raise error for testing

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
            raise  # Re-raise for testing

    def char_subrace(self, race: int) -> None:
        """Selected subrace of character, if available"""
        if race == 1:
            subrace_choice: Dict[int, str] = {1: "Hill Dwarf", 2: "Mountain Dwarf"}
            if self.dm_underdark:
                subrace_choice[3] = "Grey Dwarf"
        elif race == 2:
            subrace_choice = {1: "Grey Elf", 2: "Half-Elf", 3: "High Elf", 4: "Wild Elf", 5: "Wood Elf"}
            if self.dm_underdark:
                subrace_choice[6] = "Dark Elf"
        elif race == 3:
            subrace_choice = {1: "Forest Gnome", 2: "Hill Gnome"}
            if self.dm_underdark:
                subrace_choice[3] = "Deep Gnome"

        subrace_num: int = int(input(f"Enter the subrace of your character {subrace_choice}"))

        self.subrace = subrace_choice[subrace_num]

    def class_by_race(self):
        """Acceptable classes based on race of character"""
        race_classes = []
        # if self.subrace and self.want_multiclass is False:
        if self.subrace:
            approved_classes = race_vs_class.get_classes(self.subrace)
        else:
            approved_classes = race_vs_class.get_classes(self.race)

        # Convert the list of tuples that was returned to a list of strings for acceptable classes
        for value in approved_classes:
            race_classes.append(value[0])

        return race_classes

    def multiclass_by_race(self):
        """Acceptable multiclass combos based on character race

        Half-elves have class limits based on elf parent's race.
        """
        race_multiclass = []
        # if self.subrace and not self.race == "Dwarf" and self.want_multiclass is True:
        if self.subrace and not self.race == "Dwarf":
            approved_classes = race_vs_multiclass.get_classes(self.subrace)
        else:
            approved_classes = race_vs_multiclass.get_classes(self.race)

        # Convert the list of tuples that was returned to a list of strings for acceptable classes
        for value in approved_classes:
            race_multiclass.append(value[0])

        return race_multiclass

    def set_social_class(self, social_class=None):
        """If not defined, randomly assign a social class to the character."""
        if social_class:
            self.social_class = social_class
        else:
            roll = multi_die(1, 100)
            if 1 <= roll <= 4:
                self.social_class = "Lower-Lower Class"
            elif 5 <= roll <= 10:
                self.social_class = "Middle-Lower Class"
            elif 11 <= roll <= 20:
                self.social_class = "Upper-Lower Class"
            elif 21 <= roll <= 35:
                self.social_class = "Lower-Middle Class"
            elif 36 <= roll <= 55:
                self.social_class = "Middle-Middle Class"
            elif 56 <= roll <= 87:
                self.social_class = "Upper-Middle Class"
            elif 88 <= roll <= 96:
                self.social_class = "Lower-Upper Class"
            elif 97 <= roll <= 99:
                self.social_class = "Middle-Upper Class"
            else:
                self.social_class = "Upper-Upper Class"

    def set_alignment(self):
        """Pick the character's alignment

        The user's input should be an integer. The integer is used as the key for the dictionary, which returns the
        associated alignment value.
        """
        alignment_choices: Dict[int, str] = {1: "Lawful Good", 2: "Lawful Neutral", 3: "Lawful Evil", 4: "Neutral Good",
                                             5: "Neutral",
                                             6: "Neutral Evil", 7: "Chaotic Good", 8: "Chaotic Neutral",
                                             9: "Chaotic Evil"}
        chosen_alignment: str = input("Pick your alignment from the following: 1) Lawful Good, 2) Lawful Neutral, "
                                      "3) Lawful Evil, 4) Neutral Good, 5) Neutral, 6) Neutral Evil, 7) Chaotic Good,"
                                      "8) Chaotic Neutral, 9) Chaotic Evil")
        try:
            self.alignment = alignment_choices[int(chosen_alignment)]
        except ValueError:
            print("Please select the number associated with the alignment")
            raise
        except KeyError:
            print("Please select a number from 1-9")
            raise

