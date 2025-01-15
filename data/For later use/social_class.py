import random

class Character:
    def __init__(self, name, attributes, xp, character_class):
        self.name = name
        self.attributes = attributes  # Dictionary of attributes like {'strength': 15, 'dexterity': 16, 'intelligence': 14, ...}
        self.xp = xp  # Total XP
        self.character_class = character_class  # e.g., Fighter, Mage, etc.
        self.skills = {}  # Dictionary to hold skill name and its details
        self.social_class = None  # Social class will be assigned
        self.assign_social_class()  # Automatically assign social class upon character creation

    def assign_social_class(self):
        """
        Assigns a social class to the character based on a percentage roll and character class.
        """
        roll = random.randint(1, 100)
        social_class_data = {
            'Lower Class': [(1, 4), 'Freedmen, peasantry, beggars, low-level thieves'],
            'Middle Class - Lower Rung': [(5, 10), 'Laborers, shepherds, performers, barbarians, low-level bards, soldiers'],
            'Middle Class - Middle Rung': [(11, 20), 'Artisans, craftsmen, minor merchants, itinerant cavaliers, druids, rangers'],
            'Middle Class - Upper Rung': [(21, 35), 'Small landholders, merchants, petty nobility, low-level mages'],
            'Upper Class - Lower Rung': [(36, 55), 'Rich merchants, high officers, low-level clerics, high-level fighters'],
            'Upper Class - Middle Rung': [(56, 87), 'Lesser cavaliers, paladins, high-level mages'],
            'Upper Class - Upper Rung': [(88, 96), 'Cavaliers, high-level paladins, high-level clerics, nobility'],
            'Royalty': [(97, 100), 'Royalty, great nobility']
        }

        for cls, (range_values, description) in social_class_data.items():
            if range_values[0] <= roll <= range_values[1]:
                self.social_class = {'class': cls, 'description': description}
                break

        print(f"{self.name} has been assigned to the {self.social_class['class']} ({self.social_class['description']}).")

    def check_class_restrictions(self):
        """
        Ensures the character's social class is appropriate for their chosen class.
        """
        required_classes = {
            'Mage': ['Middle Class - Lower Rung', 'Middle Class - Middle Rung', 'Middle Class - Upper Rung', 'Upper Class'],
            'Cavalier': ['Upper Class - Lower Rung', 'Upper Class - Middle Rung', 'Upper Class - Upper Rung', 'Royalty'],
            'Paladin': ['Upper Class - Lower Rung', 'Upper Class - Middle Rung', 'Upper Class - Upper Rung', 'Royalty'],
            # Add other character class restrictions as necessary
        }

        if self.character_class in required_classes:
            allowed_classes = required_classes[self.character_class]
            if self.social_class['class'] not in allowed_classes:
                print(f"{self.character_class} class requires a higher social class than {self.social_class['class']}. Consider adjusting the character's social class.")
                # Here you might re-roll or allow the player to choose an appropriate social class

    def display_social_class(self):
        """
        Displays the social class and description of the character.
        """
        if self.social_class:
            print(f"Social Class: {self.social_class['class']} - {self.social_class['description']}")
        else:
            print("Social class has not been assigned.")

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

    # Create a character with some XP and a specific class
    my_character = Character("Aragorn", attributes, 15000, "Mage")

    # Check if the character's social class is appropriate for their character class
    my_character.check_class_restrictions()

    # Display social class
    my_character.display_social_class()
