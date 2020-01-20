from dataclasses import dataclass, field
from typing import Type, Dict, Any, List

from Adv_Dark_Deep.Char_Creation import roll_abilities


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
    max_spells_memorized: Dict[str, int] = field(default_factory=dict) # Maximum number of spells memorized per level

    def ability_rolls(self, roll_method):
        """Roll the ability scores for the character."""

        if roll_method == 1:
            abil_scores = roll_abilities.three_d6()
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