import random

class Character:
    def __init__(self, name, attributes, xp):
        self.name = name
        self.attributes = attributes  # Dictionary of attributes like {'strength': 15, 'dexterity': 16, 'intelligence': 14, ...}
        self.xp = xp  # Total XP
        self.skills = {}  # Dictionary to hold skill name and its details

    def add_skill(self, skill_name, skill_cost):
        if self.xp >= skill_cost:
            self.skills[skill_name] = {'level': 1, 'specialty': None}
            self.xp -= skill_cost
            print(f"Skill {skill_name} added at level 1. Remaining XP: {self.xp}")
        else:
            print(f"Not enough XP to learn {skill_name}.")

    def increase_skill_level(self, skill_name, skill_cost):
        if skill_name in self.skills:
            current_level = self.skills[skill_name]['level']
            cost_to_increase = skill_cost * (current_level + 1)
            if self.xp >= cost_to_increase:
                self.skills[skill_name]['level'] += 1
                self.xp -= cost_to_increase
                print(f"Skill {skill_name} increased to level {self.skills[skill_name]['level']}. Remaining XP: {self.xp}")
            else:
                print(f"Not enough XP to increase {skill_name} level.")
        else:
            print(f"Skill {skill_name} not found.")

    def perform_skill_check(self, skill_name, attribute_name, situational_modifier=0):
        if skill_name in self.skills:
            skill_level = self.skills[skill_name]['level']
            attribute_value = self.attributes.get(attribute_name, 0)
            roll = random.randint(1, 20)
            success_threshold = attribute_value - (2 * skill_level) + situational_modifier

            print(f"Rolling d20 for {skill_name} against {attribute_name}...")
            print(f"Roll: {roll}, Success Threshold: {success_threshold}")

            if roll <= success_threshold:
                print(f"{self.name} successfully used {skill_name}!")
                return True
            else:
                print(f"{self.name} failed to use {skill_name}.")
                return False
        else:
            print(f"{skill_name} is not learned by {self.name}.")
            return False

    def display_skills(self):
        print(f"Skills for {self.name}:")
        for skill, details in self.skills.items():
            print(f"- {skill}: Level {details['level']}, Specialty: {details['specialty']}")

    def set_specialty(self, skill_name, specialty):
        if skill_name in self.skills:
            self.skills[skill_name]['specialty'] = specialty
            print(f"Specialty for {skill_name} set to {specialty}.")
        else:
            print(f"Skill {skill_name} not found.")

# Example usage
if __name__ == "__main__":
    # Example attributes dictionary
    attributes = {
        'strength': 15,
        'dexterity': 17,
        'intelligence': 14,
        'wisdom': 12,
        'constitution': 13,
        'charisma': 10
    }

    # Create a character with some XP
    my_character = Character("Aragorn", attributes, 15000)

    # Add a skill
    my_character.add_skill("Ambush", 5000)

    # Increase a skill level
    my_character.increase_skill_level("Ambush", 5000)

    # Set a specialty
    my_character.set_specialty("Ambush", "Forest")

    # Perform a skill check
    my_character.perform_skill_check("Ambush", "dexterity", situational_modifier=-2)

    # Display skills
    my_character.display_skills()
