from dataclasses import dataclass
from typing import Type, Dict, Any, List


@dataclass()
class Character:
    """Basic character information, common to all player characters"""
    strength: Type[float]
    dexterity: Type[int]
    intelligence: Type[int]
    wisdom: Type[int]
    constitution: Type[int]
    charisma: Type[int]

    save_vs_ppd: Type[int]  # Save vs. poison, paralyzation, death
    save_vs_pp: Type[int]  # Save vs. petrification, polymorph
    save_vs_bw: Type[int]  # Save vs. breath weapon
    save_vs_rsw: Type[int]  # Save vs. rods, staves, wands
    save_vs_spell: Type[int]  # Save vs. magic spells and spell-like effects

    name: str
    gender: str
    race: str
    subrace: str
    social_class: str
    alignment: str
    age: Type[int]
    height: Type[float]
    weight: Type[int]
    special_abilities: List[str]
    experience: Type[int]
    level: Type[int]
    languages: List[str]

    armour_class: Type[int]
    hit_points: Type[int]
    non_lethal_wounds: Type[int]
    armour_worn: str
    init_mod: Type[int]  # Initiative modifier
    surprise_mod: Type[int]  # Modifier to be surprised
    attack_column: str  # Attack column (Adv. Dark & Deep only)
    weapons: Dict[str, int]

    skills: Dict[str, int]
    class_abilities: Dict[str, int]

    supplies: Dict[str, int]  # Expendable items
    equipment: Dict[str, int]  # Non-expendable items
    encumberance: Type[int]  # Mass of all equipment, supplies, weapons, armour, etc.
    base_move: Type[int]  # Unencumbered move rate
    move_rate: Type[int]  # Current move rate
    magic_items: Dict[str, int]

    deeds_titles: str  # Estates, property, and named titles, e.g. Duke

    mount_name: str
    mount_type: str
    mount_hp: Type[int]  # Hit points of mount
    mount_armour: str
    mount_ac: Type[int]  # Armour class of mount

    spells_memorized: List[str]
    spell_components: Dict[str, int]
    max_spells_memorized: Dict[str, int]  # Maximum number of spells memorized per level

    def ability_rolls(self, roll_method):
        """Roll the ability scores for the character."""
        pass