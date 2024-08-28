import random

class MagicItem:
    def __init__(self, name, item_type, command_word=None):
        self.name = name
        self.item_type = item_type  # e.g., 'wand', 'potion', 'ring', etc.
        self.command_word = command_word
        self.active = False

    def activate(self):
        if self.command_word:
            print(f"{self.name} is activated using the command word '{self.command_word}'.")
        else:
            print(f"{self.name} is activated.")
        self.active = True

    def deactivate(self):
        self.active = False
        print(f"{self.name} is deactivated.")

class Character:
    def __init__(self, name):
        self.name = name
        self.active_item = None
        self.worn_items = {"rings": [], "robes": None, "cloak": None, "gloves": None, "boots": None}
        self.consumed_potions = []

    def use_magic_item(self, item):
        if self.active_item and self.active_item != item:
            print(f"{self.name} can only use one active item per round. Deactivating {self.active_item.name}.")
            self.active_item.deactivate()

        self.active_item = item
        self.active_item.activate()

    def wear_item(self, item):
        if item.item_type == "ring":
            if len(self.worn_items["rings"]) >= 2:
                print(f"{self.name} is already wearing two rings. {item.name} cannot be worn.")
            else:
                self.worn_items["rings"].append(item)
                print(f"{self.name} wears the ring {item.name}.")
        elif item.item_type in self.worn_items:
            if self.worn_items[item.item_type]:
                print(f"{self.name} is already wearing a {item.item_type}. {item.name} cannot be worn.")
            else:
                self.worn_items[item.item_type] = item
                print(f"{self.name} wears the {item.item_type} {item.name}.")
        else:
            print(f"{item.item_type} is not a wearable item type.")

    def consume_potion(self, potion):
        time_to_consume = random.randint(1, 4) + 1  # 12-30 seconds
        print(f"{self.name} consumes {potion.name}, which takes {time_to_consume * 6} seconds.")

        # Check for potion compatibility if another potion is still active
        if self.consumed_potions:
            result = self.check_potion_compatibility(potion)
            print(result)
        else:
            print(f"{potion.name} is effective.")

        self.consumed_potions.append(potion)

    @staticmethod
    def check_potion_compatibility(new_potion):
        roll = random.randint(1, 100)
        compatibility_table = [
            (1, "Explosion: 6d10 damage to the drinker."),
            (2, "Poison: The drinker is dead (no save)."),
            (4, "Poison: STR and DEX -1 for 5d4 minutes. Only one potion works at half effect."),
            (9, "Incompatible: Both potions evaporate."),
            (16, "Incompatible: One potion cancels the other."),
            (26, "Incompatible: Both potions work at half effect."),
            (36, "Compatible: Both potions work normally."),
            (91, "Compatible: One potion works at 150% effect."),
            (100, "Compatible: One potion's effect becomes permanent.")
        ]
        for threshold, outcome in compatibility_table:
            if roll <= threshold:
                return outcome
        return "Compatible: Both potions work normally."

# Example usage:

# Creating magic items
wand_of_fireballs = MagicItem(name="Wand of Fireballs", item_type="wand", command_word="Ignis")
ring_of_protection = MagicItem(name="Ring of Protection", item_type="ring")
potion_of_healing = MagicItem(name="Potion of Healing", item_type="potion")

# Creating a character
aragorn = Character(name="Aragorn")

# Using magic items
aragorn.use_magic_item(wand_of_fireballs)

# Wearing items
aragorn.wear_item(ring_of_protection)

# Consuming a potion
aragorn.consume_potion(potion_of_healing)

# Attempting to use another active item in the same round
ring_of_invisibility = MagicItem(name="Ring of Invisibility", item_type="ring", command_word="Invisibilis")
aragorn.use_magic_item(ring_of_invisibility)

# Consuming another potion to check for compatibility
potion_of_strength = MagicItem(name="Potion of Strength", item_type="potion")
aragorn.consume_potion(potion_of_strength)
