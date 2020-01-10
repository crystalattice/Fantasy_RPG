class Character:
    """Basic character information, common to all player characters"""

    def __init__(self):
        self.strength = float
        self.dexterity = int
        self.intelligence = int
        self.wisdom = int
        self.constitution = int
        self.charisma = int

        self.save_vs_ppd = int  # Save vs. poison, paralyzation, death
        self.save_vs_pp = int  # Save vs. petrification, polymorph
        self.save_vs_bw = int  # Save vs. breath weapon
        self.save_vs_rsw = int  # Save vs. rods, staves, wands
        self.save_vs_spell = int  # Save vs. magic spells and spell-like effects

        self.name = ""
        self.gender = ""
        self.race = ""
        self.subrace = ""
        self.social_class = ""
        self.alignment = ""
        self.age = int
        self.height = float
        self.weight = int
        self.special_abilities = ""
        self.experience = int
        self.level = int
        self.languages = ""

        self.armour_class = int
        self.hit_points = int
        self.armour_worn = ""
        self.init_mod = int  # Initiative modifier
        self.surprise_mod = int  # Modifier to be surprised
        self.attack_column = ""  # Attack column (Adv. Dark & Deep only)
        self.weapons = []

        self.skills = {}
        self.class_abilities = {}

        self.supplies = {}  # Expendable items
        self.equipment = []  # Non-expendable items
        self.encumberance = int  # Mass of all equipment, supplies, weapons, armour, etc.
        self.base_move = int  # Unencumbered move rate
        self.move_rate = int  # Current movement rate
        self.magic_items = []

        self.deeds_titles = ""  # Estates, property, and named titles, e.g. Duke

        self.mount_name = ""
        self.mount_type = ""
        self.mount_hp = int  # Hit points for mount
        self.mount_ac = int  # Armour class of mount

        self.spells = []
        self.spell_components = {}
        self.max_spells_memorized = {}  # Maximum number of spells memorized per level
