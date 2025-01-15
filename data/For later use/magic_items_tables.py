import random


class MagicItemGenerator:
    """
    A class to generate magic items based on the ADVENTURES DARK AND DEEP™ Bestiary rules.
    """

    def __init__(self):
        pass

    def generate_magic_item(self):
        """
        Generates a random magic item based on the provided tables.

        :return: A string describing the magic item.
        """
        item_type_roll = random.randint(1, 100)
        item_type = self.determine_item_type(item_type_roll)

        if item_type == "Armor or shield":
            return self.generate_armor_or_shield()
        elif item_type == "Book":
            return self.generate_book()
        elif item_type == "Charm":
            return self.generate_charm()
        elif item_type == "Garment":
            return self.generate_garment()
        elif item_type == "Potion or liquid":
            return self.generate_potion_or_liquid()
        elif item_type == "Ring":
            return self.generate_ring()
        elif item_type == "Rod":
            return self.generate_rod()
        elif item_type == "Scroll":
            return self.generate_scroll()
        elif item_type == "Spellbook":
            return "Spellbook"
        elif item_type == "Staff":
            return self.generate_staff()
        elif item_type == "Wand":
            return self.generate_wand()
        elif item_type == "Weapon":
            return self.generate_weapon()
        elif "Wondrous item" in item_type:
            return self.generate_wondrous_item(item_type)
        else:
            return "Unknown magic item"

    def determine_item_type(self, roll):
        """
        Determines the type of magic item based on the initial roll.

        :param roll: The roll result (1-100).
        :return: The type of magic item as a string.
        """
        if roll <= 15:
            return "Armor or shield"
        elif roll == 16:
            return "Book"
        elif roll <= 18:
            return "Charm"
        elif roll <= 22:
            return "Garment"
        elif roll <= 41:
            return "Potion or liquid"
        elif roll <= 46:
            return "Ring"
        elif roll == 47:
            return "Rod"
        elif roll <= 61:
            return "Scroll"
        elif roll <= 63:
            return "Spellbook"
        elif roll <= 65:
            return "Staff"
        elif roll <= 68:
            return "Wand"
        elif roll <= 94:
            return "Weapon"
        elif roll <= 96:
            return "Wondrous item (A-E)"
        elif roll <= 98:
            return "Wondrous item (E-J)"
        else:
            return "Wondrous item (J-Z)"

    def generate_armor_or_shield(self):
        """
        Generates a random magic armor or shield.

        :return: A string describing the magic armor or shield.
        """
        roll = random.randint(1, 100)
        if roll <= 56:
            return "Armor, enchanted"
        elif roll <= 65:
            return "Mail, elfin"
        else:
            return "Shield, enchanted"

    def generate_book(self):
        """
        Generates a random magic book.

        :return: A string describing the magic book.
        """
        roll = random.randint(1, 100)
        books = [
            "Blessed Book", "Book of Holy Benisons", "Book of Infinite Spells",
            "Book of Unholy Damnation", "Codex of Making Friends and Influencing People",
            "Libram of Gainful Conjuration", "Libram of Ineffable Damnation",
            "Libram of Silver Magic", "Manual of Bodily Health", "Manual of Gainful Exercise",
            "Manual of Golems", "Manual of Puissant Skill at Arms", "Manual of Quickness of Action",
            "Manual of Stealthy Pilfering", "Necrophidius Handbook", "Tome of Clear Thought",
            "Tome of Leadership and Influence", "Tome of Understanding", "Vacuous Grimoire"
        ]
        book_index = min(roll // 4, len(books) - 1)
        return books[book_index]

    def generate_charm(self):
        """
        Generates a random magic charm.

        :return: A string describing the magic charm.
        """
        roll = random.randint(1, 100)
        charms = [
            "Amulet of Inescapable Location", "Amulet of Life Protection", "Amulet of the Planes",
            "Amulet of Proof against Detection and Location", "Amulet of Undead Command",
            "Amulet of Undead Turning", "Brooch of Shielding", "Medallion of ESP",
            "Medallion of Thought Projection", "Necklace of Adaptation", "Necklace of Missiles",
            "Necklace of Prayer Beads", "Necklace of Strangulation", "Periapt of Foul Rotting",
            "Periapt of Health", "Periapt of Proof Against Poison", "Periapt of Wound Closure",
            "Phylactery of Faithfulness", "Phylactery of Long Years", "Phylactery of Monstrous Attention",
            "Phylactery of Shortened Years", "Scarab of Death", "Scarab of Enraging Enemies",
            "Scarab of Golem Slaying", "Scarab of Insanity", "Scarab of Protection",
            "Talisman of Pure Good", "Talisman of the Sphere", "Talisman of Ultimate Evil"
        ]
        charm_index = min(roll // 3, len(charms) - 1)
        return charms[charm_index]

    def generate_garment(self):
        """
        Generates a random magic garment.

        :return: A string describing the magic garment.
        """
        roll = random.randint(1, 100)
        garments = [
            "Boots of Dancing", "Boots of Elvenkind", "Boots of Levitation",
            "Boots of the North", "Boots of Speed", "Boots of Striding and Springing",
            "Boots of Varied Tracks", "Boots, Winged", "Bracers of Archery", "Bracers of Brachiation",
            "Bracers of Defense", "Bracers of Defenselessness", "Circlet of Domination",
            "Cloak of Arachnidia", "Cloak of the Bat", "Cloak of Displacement",
            "Cloak of Elvenkind", "Cloak of the Manta Ray", "Cloak of Poisonousness",
            "Cloak of Protection", "Cyclone Spitzhut", "Eyes of the Basilisk",
            "Eyes of Charming", "Eyes of the Eagle", "Eyes of Minute Seeing",
            "Eyes of Petrification", "Gauntlets of Ogre Power", "Girdle of Dwarvenkind",
            "Girdle of Femininity/Masculinity", "Girdle of Giant Strength",
            "Girdle of Many Pouches", "Gloves of Dexterity", "Gloves of Fumbling",
            "Gloves of Missile Snaring", "Gloves of Swimming and Climbing",
            "Gloves of Thievery", "Hat of Difference", "Hat of Disguise",
            "Hat of Stupidity", "Helm of Brilliance", "Helm of Comprehension",
            "Helm of Opposite Alignment", "Helm of Telepathy", "Helm of Teleportation",
            "Mantle of Starry Wandering", "Robe of the Archmagi", "Robe of Blending",
            "Robe of Eyes", "Robe of Powerlessness", "Robe of Scintillating Colors",
            "Robe of Stars", "Robe of Useful Items", "Robe of Vermin",
            "Shoes of Wandering", "Slippers of Kicking", "Slippers of Spider Climbing",
            "Wings of Flying"
        ]
        garment_index = min(roll // 2, len(garments) - 1)
        return garments[garment_index]

    def generate_potion_or_liquid(self):
        """
        Generates a random magic potion or liquid.

        :return: A string describing the magic potion or liquid.
        """
        roll = random.randint(1, 100)
        potions = [
            "Love Potion", "Oil of Acid Resistance", "Oil of Disenchantment",
            "Oil of Elemental Invulnerability", "Oil of Etherealness", "Oil of Fiery Burning",
            "Oil of Fumbling", "Oil of Impact", "Oil of Sharpness", "Oil of Slipperiness",
            "Oil of Timelessness", "Potion of Animal Control", "Potion of Beauty",
            "Potion of Clairaudience", "Potion of Clairvoyance", "Potion of Climbing",
            "Potion of Delusion", "Potion of Diminution", "Potion of Dragon Control",
            "Potion of ESP", "Potion of Extra Healing", "Potion of Fire Breath",
            "Potion of Fire Resistance", "Potion of Flying", "Potion of Gaseous Form",
            "Potion of Giant Control", "Potion of Giant Strength", "Potion of Glibness",
            "Potion of Growth", "Potion of Healing", "Potion of Health",
            "Potion of Heroism", "Potion of Human Control", "Potion of Invisibility",
            "Potion of Invulnerability", "Potion of Levitation", "Potion of Life",
            "Potion of Liquid Form", "Potion of Longevity", "Potion of Madness",
            "Potion of Persuasiveness", "Potion of Plant Control", "Potion of Poison",
            "Potion of Polymorph Self", "Potion of Rainbow Hues", "Potion of Speed",
            "Potion of Stammering and Stuttering", "Potion of Super Heroism",
            "Potion of Treasure Finding", "Potion of Undead Control", "Potion of Vitality",
            "Potion of Water Breathing", "Potion of Youth", "Sovereign Glue",
            "Sweet Water", "Ultimate Solution"
        ]
        potion_index = min(roll // 2, len(potions) - 1)
        return potions[potion_index]

    def generate_ring(self):
        """
        Generates a random magic ring.

        :return: A string describing the magic ring.
        """
        roll = random.randint(1, 100)
        rings = [
            "Ring of Animal Friendship", "Ring of Blinking", "Ring of Chameleon Power",
            "Ring of Clumsiness", "Ring of Contrariness", "Ring of Delusion",
            "Ring of Djinni Summoning", "Ring of Elemental Command", "Ring of Elvenkind",
            "Ring of Feather Falling", "Ring of Fire Resistance", "Ring of Free Action",
            "Ring of Influence", "Ring of Invisibility", "Ring of Jumping", "Ring of Magus",
            "Ring of Mammal Control", "Ring of Mind Shielding", "Ring of Protection",
            "Ring of the Ram", "Ring of Regeneration", "Ring of Shocking Grasp",
            "Ring of Shooting Stars", "Ring of Spell Storing", "Ring of Spell Turning",
            "Ring of Sustenance", "Ring of Swimming", "Ring of Telekinesis",
            "Ring of Truth", "Ring of Warmth", "Ring of Water Walking",
            "Ring of Weakness", "Ring of Wishes", "Ring of Wizardry", "Ring of X-ray Vision"
        ]
        ring_index = min(roll // 3, len(rings) - 1)
        return rings[ring_index]

    def generate_rod(self):
        """
        Generates a random magic rod.

        :return: A string describing the magic rod.
        """
        roll = random.randint(1, 100)
        rods = [
            "Rod of Absorption", "Rod of Beguiling", "Rod of Cancellation",
            "Rod of Flailing", "Rod of Lordly Might", "Rod of Passage",
            "Rod of Resurrection", "Rod of Rulership", "Rod of Security",
            "Rod of Smiting", "Rod of Splendor"
        ]
        rod_index = min(roll // 9, len(rods) - 1)
        return rods[rod_index]

    def generate_scroll(self):
        """
        Generates a random magic scroll.

        :return: A string describing the magic scroll.
        """
        roll = random.randint(1, 100)
        if roll <= 2:
            return "Scroll, cursed"
        elif roll <= 50:
            return self.generate_protection_scroll()
        else:
            return "Scroll, spell"

    def generate_protection_scroll(self):
        """
        Generates a random protection scroll.

        :return: A string describing the protection scroll.
        """
        roll = random.randint(1, 100)
        protection_scrolls = [
            "Protection from Acid", "Protection from Angels", "Protection from Archons",
            "Protection from Breath Weapons (dragon)", "Protection from Breath Weapons (non-dragon)",
            "Protection from Cold", "Protection from Daemons", "Protection from Demons",
            "Protection from Devas", "Protection from Devils", "Protection from Electricity",
            "Protection from Elementals", "Protection from Fire", "Protection from Gas",
            "Protection from Illusions", "Protection from Lycanthropes",
            "Protection from Magic", "Protection from Paralyzation",
            "Protection from Petrification", "Protection from Plants", "Protection from Poison",
            "Protection from Possession", "Protection from Traps", "Protection from Undead",
            "Protection from Water", "Protection from Weapons (blunt)",
            "Protection from Weapons (edged)", "Protection from Weapons (magical blunt)",
            "Protection from Weapons (magical edged)", "Protection from Weapons (magical missile)",
            "Protection from Weapons (magical piercing)", "Protection from Weapons (missile)",
            "Protection from Weapons (piercing)"
        ]
        scroll_index = min(roll // 3, len(protection_scrolls) - 1)
        return protection_scrolls[scroll_index]

    def generate_staff(self):
        """
        Generates a random magic staff.

        :return: A string describing the magic staff.
        """
        roll = random.randint(1, 100)
        staffs = [
            "Staff of Command", "Staff of Curing", "Staff of the Magi", "Staff of Power",
            "Staff of Serpents", "Staff of Slinging", "Staff-mace", "Staff-spear",
            "Staff of Striking", "Staff of Swarming", "Staff of Thunder and Lightning",
            "Staff of Withering", "Staff of the Woodlands"
        ]
        staff_index = min(roll // 8, len(staffs) - 1)
        return staffs[staff_index]

    def generate_wand(self):
        """
        Generates a random magic wand.

        :return: A string describing the magic wand.
        """
        roll = random.randint(1, 100)
        wands = [
            "Buckler Wand", "Wand of Conjuration", "Wand of Defoliation",
            "Wand of Earth and Stone", "Wand of Enemy Detection", "Wand of Fear",
            "Wand of Fire", "Wand of Fireballs", "Wand of Flame Extinguishing",
            "Wand of Force", "Wand of Frost", "Wand of Ice Storms",
            "Wand of Illumination", "Wand of Illusion", "Wand of Lightning",
            "Wand of Lightning Bolts", "Wand of Magic Detection",
            "Wand of Magic Missiles", "Wand of Metal and Mineral Detection",
            "Wand of Metal Command", "Wand of Negation", "Wand of Paralyzation",
            "Wand of Polymorphing", "Wand of Secret Door and Trap Detection",
            "Wand of Size Alteration", "Wand of Steam and Vapor", "Wand of Wonder"
        ]
        wand_index = min(roll // 4, len(wands) - 1)
        return wands[wand_index]

    def generate_weapon(self):
        """
        Generates a random magic weapon.

        :return: A string describing the magic weapon.
        """
        roll = random.randint(1, 100)
        if roll <= 80:
            return "Weapon, enchanted"
        else:
            return "Weapon (missile), enchanted"

    def generate_wondrous_item(self, item_type):
        """
        Generates a random wondrous item based on the item type.

        :param item_type: The category of wondrous item (A-E, E-J, J-Z).
        :return: A string describing the wondrous item.
        """
        roll = random.randint(1, 100)
        if item_type == "Wondrous item (A-E)":
            wondrous_items = [
                "Alchemy Jug", "Apparatus of the Crab", "Arrow of Direction",
                "Bag of Devouring", "Bag of Holding", "Bag of Transmuting",
                "Bag of Tricks", "Beads of Force", "Beaker of Plentiful Potions",
                "Boat, Folding", "Bowl of Water Elemental Command",
                "Bowl of Watery Death", "Brazier of Fire Elemental Command",
                "Brazier of Sleep Smoke", "Broom of Animated Attack",
                "Broom of Flying", "Candle of Invocation", "Carpet of Flying",
                "Censer of Air Elemental Command", "Censer of Summoning Hostile Air Elementals",
                "Chime of Hunger", "Chime of Interruption", "Chime of Opening",
                "Cornamuse of the Woodlands", "Crystal Ball", "Crystal Hypnosis Ball",
                "Cube of Force", "Cube of Frost Resistance", "Cubic Gate",
                "Dart of the Hornets’ Nest", "Decanter of Endless Water", "Deck of Illusions",
                "Deck of Many Things", "Doleful and Bright Candelabra", "Drum of Deafening",
                "Drum of Panic", "Dulcimer of Defense", "Dust of Appearance",
                "Dust of Disappearance", "Dust of Dryness", "Dust of Illusion",
                "Dust of Sneezing and Choking", "Dust of Tracelessness", "Efficient Quiver",
                "Efreeti Bottle", "Egg of Desire", "Egg of Reason"
            ]
        elif item_type == "Wondrous item (E-J)":
            wondrous_items = [
                "Egg of Shattering", "Ever-full Purse", "Ever-smoking Bottle",
                "Feather Token", "Figurine of Wondrous Power", "Flask of Curses",
                "Flowing Flagon", "Flute of Wonder", "Gem of Brightness",
                "Gem of Insight", "Gem of Seeing", "Hammer, Dwarven Thrower",
                "Handy Haversack", "Healing Ointment", "Helm of Underwater Action",
                "Horn of Blasting", "Horn of Bubbles", "Horn of Collapsing",
                "Horn of Fog", "Horn of Goodness/Evil", "Horn of the Tritons",
                "Horn of Valhalla", "Hornblade", "Horseshoes of a Zephyr",
                "Horseshoes of Speed", "Incense of Meditation", "Incense of Obsession",
                "Instant Fortress", "Instrument of the Bards", "Ioun Stones",
                "Iron Bands of Binding", "Iron Flask", "Javelin of Lightning", "Javelin of Piercing"
            ]
        else:
            wondrous_items = [
                "Jewel of Attacks", "Lens of Detection", "Lens of Ultravision",
                "Longtooth Dagger", "Lyre of Building", "Lyre of the Elements",
                "Mail, Elfin", "Mandolin of Might", "Marvelous Pigments",
                "Mattock of the Titans", "Maul of the Titans", "Mirror of Life Trapping",
                "Mirror of Mental Prowess", "Mirror of Opposition", "Net of Entrapment",
                "Net of Snaring", "Pearl of Folly", "Pearl of Loss", "Pearl of Power",
                "Pearl of the Sirens", "Pearl of Wisdom", "Pipes of the Sewers",
                "Portable Hole", "Pouch of Accessibility", "Prison of the Magus",
                "Rope of Climbing", "Rope of Constriction", "Rope of Entanglement",
                "Rug of Smothering", "Rug of Welcome", "Saw of Mighty Cutting",
                "Shadow Lanthorn", "Sheet of Smallness", "Spade of Colossal Excavation",
                "Spell Component Case, Enchanted", "Sphere of Annihilation",
                "Spoon of Stirring", "Stone Horse", "Stone of Controlling Earth Elementals",
                "Stone of Good Luck", "Stone of Weight", "Sustaining Spoon",
                "Trident of Fish Command", "Trident of Warning", "Trident of Yearning",
                "Well of Many Worlds", "Wind Fan"
            ]
        wondrous_index = min(roll // 2, len(wondrous_items) - 1)
        return wondrous_items[wondrous_index]


# Example usage:
magic_item_generator = MagicItemGenerator()
random_magic_item = magic_item_generator.generate_magic_item()
print(f"Generated Magic Item: {random_magic_item}")
