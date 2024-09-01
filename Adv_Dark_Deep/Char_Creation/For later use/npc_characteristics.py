import random


class NPC:
    def __init__(self, character_class):
        self.character_class = character_class
        self.ability_scores = self.adjust_ability_scores()
        self.alignment = self.random_alignment()
        self.possessions = self.random_possessions()
        self.personality_traits = self.generate_personality_traits()
        self.physical_traits = self.generate_physical_traits()

    def adjust_ability_scores(self):
        # Base ability scores (can be adjusted as needed)
        scores = {
            "STR": 10,
            "INT": 10,
            "WIS": 10,
            "DEX": 10,
            "CON": 10,
            "CHA": 10
        }

        # Ability score adjustments by class
        adjustments = {
            "Bard": {"CHA": +2},
            "Jester": {"DEX": +1, "CHA": +2},
            "Cavalier": {"STR": +2, "CON": +1},
            "Paladin": {"STR": +1, "CHA": +2},
            "Cleric": {"WIS": +2, "CHA": +1},
            "Druid": {"WIS": +2, "CHA": +1},
            "Mystic": {"INT": +1, "WIS": +2},
            "Commoner": {},
            "Laborer": {"STR": +3},
            "Mercenary": {"STR": +1, "CON": +2},
            "Merchant": {"INT": +1, "CHA": +1},
            "Fighter": {"STR": +2, "CON": +1},
            "Barbarian": {"STR": +1, "CON": +2},
            "Ranger": {"STR": +2, "CON": +1},
            "Mage": {"INT": +2, "DEX": +1},
            "Illusionist": {"INT": +2, "DEX": +2},
            "Savant": {"INT": +2, "WIS": +1},
            "Thief": {"INT": +1, "DEX": +2},
            "Acrobat": {"STR": +1, "DEX": +2},
            "Mountebank": {"DEX": +1, "CHA": +2}
        }

        # Apply adjustments based on class
        if self.character_class in adjustments:
            for key, value in adjustments[self.character_class].items():
                scores[key] += value

        return scores

    def random_alignment(self):
        roll = random.randint(1, 100)
        if 1 <= roll <= 10:
            return "Lawful Good"
        elif 11 <= roll <= 20:
            return "Lawful Neutral"
        elif 21 <= roll <= 30:
            return "Lawful Evil"
        elif 31 <= roll <= 40:
            return "Neutral Evil"
        elif 41 <= roll <= 50:
            return "Chaotic Evil"
        elif 51 <= roll <= 60:
            return "Chaotic Neutral"
        elif 61 <= roll <= 70:
            return "Chaotic Good"
        elif 71 <= roll <= 80:
            return "Neutral Good"
        else:
            return "Neutral"

    def random_possessions(self):
        roll = random.randint(1, 100)
        if 1 <= roll <= 10:
            return "None"
        elif 11 <= roll <= 30:
            return "Limited"
        elif 31 <= roll <= 70:
            return "Average"
        elif 71 <= roll <= 80:
            return "Above Average"
        elif 81 <= roll <= 90:
            return "Extensive"
        else:
            return "Great"

    def generate_personality_traits(self):
        personality_traits = [
            "Abrasive", "Aesthetic", "Aggressive", "Aloof", "Altruist", "Antagonistic",
            "Anti-social", "Arrogant", "Bawdy", "Blustering", "Brave", "Brooding",
            "Careless", "Cheerful", "Conscientious", "Contrarian", "Courteous", "Cowardly",
            "Craven", "Creative", "Crude", "Cruel", "Deceitful", "Diplomatic", "Disciplined",
            "Drunkard", "Easygoing", "Energetic", "Eventempered", "Extroverted", "Fastidious",
            "Focused", "Foolhardy", "Forceful", "Forgiving", "Friendly", "Gambler", "Gourmet",
            "Greedy", "Hard-hearted", "Haughty", "Hedonist", "Helpful", "Honorable", "Hostile",
            "Hotheaded", "Humble", "Inquisitive", "Intellectual", "Interested in history", "Interested in legends",
            "Interested in nature", "Interested in politics", "Interested in religion", "Interested in sports",
            "Introverted",
            "Irreverent", "Jealous", "Lazy", "Loquacious", "Low self-esteem", "Loyal", "Lusty", "Meticulous",
            "Mischievous",
            "Miserly", "Modest", "Neurotic", "Obsequious", "Obsessive", "Optimist", "Overbearing", "Perceptive",
            "Perverted",
            "Pessimist", "Pious", "Proud", "Rash", "Religious", "Reverent", "Rude", "Sadistic", "Scheming", "Secretive",
            "Sensitive", "Sloppy", "Sober", "Spendthrift", "Studious", "Suspicious", "Teetotaler", "Thrifty",
            "Trusting",
            "Truthful", "Undisciplined", "Unfeeling", "Vengeful", "Violent", "Virtuous", "Wastrel"
        ]

        num_traits = random.randint(2, 5)  # Choose 1d4+1 traits
        selected_traits = random.sample(personality_traits, num_traits)
        return selected_traits

    def generate_physical_traits(self):
        physical_traits = [
            "Always snacking", "Bad breath", "Bald", "Beady eyes", "Beauty mark", "Beer belly",
            "Big bushy beard", "Big ears", "Big teeth", "Blinks often", "Body odor", "Bounces leg (seated)",
            "Braided beard", "Braided hair", "Broad forehead", "Broad nose", "Burn mark", "Chuckles",
            "Cleft chin", "Cleft palate", "Clumsy", "Cowlick", "Cracks knuckles", "Cringes", "Curly hair",
            "Distinctive birthmark", "Double chin", "Eye patch", "Face scar", "Flaxen hair", "Flirts", "Freckles",
            "Frizzy hair", "Gaudy jewelry", "Goatee", "Grinds teeth", "Growls", "Harelip", "Haughty expression",
            "Hawk nose", "Heterochromia", "Laughs obnoxiously", "Licks his lips", "Lisps", "Long fingernails",
            "Long hair", "Lots of makeup", "Missing many teeth", "Missing most teeth", "Missing one eye", "Mole",
            "Monocle", "Nervous tic", "No earlobes", "Obese", "Overweight", "Painted fingernails", "Pale skin",
            "Perfect teeth", "Picks fingernails", "Picks teeth", "Pimples", "Plays with knife", "Plump", "Pointed chin",
            "Pointed nose", "Pug nose", "Purses lips", "Repeats last words", "Repeats others’ words", "Round face",
            "Scruffy looking", "Short", "Simpers", "Slender", "Spits", "Squints", "Stares", "Stocky", "Stuffy nose",
            "Stumbles", "Sucks teeth", "Sweet smell", "Tall", "Tanned", "Tattoos", "Thick lips", "Thin", "Thin lips",
            "Thinning hair", "Tosses/catches item", "Unibrow", "Very long fingers", "Voluptuous figure",
            "Waxed mustache",
            "Wheezes", "Wild eyes", "Winks", "Yellow teeth", "Zaftig"
        ]

        num_traits = random.randint(1, 3)  # Choose 1d3 traits
        selected_traits = random.sample(physical_traits, num_traits)
        return selected_traits

    def display_npc(self):
        print(f"Class: {self.character_class}")
        print(f"Ability Scores: {self.ability_scores}")
        print(f"Alignment: {self.alignment}")
        print(f"Possessions: {self.possessions}")
        print(f"Personality Traits: {', '.join(self.personality_traits)}")
        print(f"Physical Traits: {', '.join(self.physical_traits)}")


# Example usage
npc_class = random.choice([
    "Bard", "Jester", "Cavalier", "Paladin", "Cleric", "Druid", "Mystic",
    "Commoner", "Laborer", "Mercenary", "Merchant", "Fighter", "Barbarian",
    "Ranger", "Mage", "Illusionist", "Savant", "Thief", "Acrobat", "Mountebank"
])

npc = NPC(npc_class)
npc.display_npc()
