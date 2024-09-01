class SpellCaster:
    def __init__(self, alignment, spell_type):
        self.alignment = alignment
        self.spell_type = spell_type

    def calculate_cost(self, spell_name, spell_level=None):
        base_cost = 0

        if self.spell_type == "cleric":
            base_cost = self.cleric_spell_cost(spell_name)
        elif self.spell_type == "mage":
            base_cost = self.mage_spell_cost(spell_level, spell_name)

        return base_cost

    def cleric_spell_cost(self, spell_name):
        cleric_spell_costs = {
            "Astral spell": 5000,
            "Atonement": 500,
            "Augury": 300,
            "Bless": 5,
            "Commune": 1000,
            "Continual light": 500,
            "Control weather": 10000,
            "Cure blindness": 1000,
            "Cure disease": 1000,
            "Cure light wounds": 100,
            "Cure serious wounds": 350,
            "Cure critical wounds": 600,
            "Detect evil": 100,
            "Detect magic": 150,
            "Dispel evil": 1000,
            "Dispel magic": 500,
            "Divination": 1000,
            "Earthquake": 10000,
            "Exorcise": 7000,
            "Find the path": 5500,
            "Gate": 50000,
            "Glyph of warding": 500,
            "Heal": 200,
            "Neutralize poison": 1000,
            "Part water": 11000,
            "Plane shift": 4000,
            "Prayer": 250,
            "Protection from evil": 50,
            "Purify food and drink": 100,
            "Raise dead": 5500,
            "Regenerate": 15000,
            "Remove curse": 2500,
            "Resist cold": 50,
            "Resist fire": 300,
            "Restoration": 10000,
            "Silence 15' radius": 300,
            "Slow poison": 600,
            "Speak with dead": 500,
            "Tongues": 500,
            "True seeing": 3600
        }

        return cleric_spell_costs.get(spell_name, 0)

    def mage_spell_cost(self, spell_level, spell_name):
        mage_spell_costs = {
            "Alteration": [20, 200, 400, 800, 1200, 2000, 2800, 3600, 4200, 4800],
            "Abjuration": [10, 100, 200, 400, 700, 1100, 1600, 2200, 2900, 3700],
            "Conjuration/Summoning": [20, 200, 300, 500, 800, 1200, 1700, 2300, 3000, 3800],
            "Evocation/Invocation": [20, 200, 350, 550, 750, 1050, 1400, 1800, 2250, 2750],
            "Enchantment/Charm": [5, 50, 100, 150, 200, 300, 400, 500, 600, 800],
            "Divination": [10, 100, 250, 500, 950, 1550, 2300, 3200, 4250, 5450],
            "Illusion/Phantasm": [10, 100, 250, 500, 950, 1550, 2300, 3200, 4250, 5450]
        }

        return mage_spell_costs.get(spell_name, [0] * 10)[spell_level - 1]

    def adjust_cost_for_alignment(self, cost, client_alignment):
        alignment_difference = {
            ("good", "evil"): 3,
            ("evil", "good"): 3,
            ("good", "neutral"): 2,
            ("neutral", "good"): 2,
            ("evil", "neutral"): 2,
            ("neutral", "evil"): 2,
            ("good", "good"): 1,
            ("neutral", "neutral"): 1,
            ("evil", "evil"): 1,
        }

        adjustment = alignment_difference.get((self.alignment, client_alignment), 1)
        return cost * adjustment


# Example usage:

# Create an NPC spellcaster with alignment "neutral" and type "cleric"
npc_spellcaster = SpellCaster(alignment="neutral", spell_type="cleric")

# Calculate the base cost for the spell "Cure light wounds"
spell_name = "Cure light wounds"
base_cost = npc_spellcaster.calculate_cost(spell_name)

# Adjust the cost based on the alignment of the client
client_alignment = "good"
total_cost = npc_spellcaster.adjust_cost_for_alignment(base_cost, client_alignment)

print(f"Total cost for casting {spell_name}: {total_cost} gold pieces")

# For a mage spell
npc_spellcaster = SpellCaster(alignment="evil", spell_type="mage")
spell_name = "Evocation/Invocation"
spell_level = 5
base_cost = npc_spellcaster.calculate_cost(spell_name, spell_level)
total_cost = npc_spellcaster.adjust_cost_for_alignment(base_cost, client_alignment)

print(f"Total cost for casting a level {spell_level} {spell_name} spell: {total_cost} gold pieces")
