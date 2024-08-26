from typing import Dict, List


class WeaponProficiency:
    """Represents weapon proficiency rules for different classes."""

    PROFICIENCY_RULES = {
        'Bard': {'initial': 2, 'new_every': 3, 'penalty': -3},
        'Jester': {'initial': 2, 'new_every': 4, 'penalty': -4, 'thrown_penalty': -2},
        'Cavalier': {'initial': 3, 'new_every': 2, 'penalty': -3},
        'Paladin': {'initial': 3, 'new_every': 2, 'penalty': -3},
        'Cleric': {'initial': 2, 'new_every': 4, 'penalty': -3},
        'Druid': {'initial': 2, 'new_every': 5, 'penalty': -4},
        'Mystic': {'initial': 2, 'new_every': 5, 'penalty': -4},
        'Fighter': {'initial': 4, 'new_every': 3, 'penalty': -2},
        'Barbarian': {'initial': 6, 'new_every': 2, 'penalty': -1},
        'Ranger': {'initial': 3, 'new_every': 3, 'penalty': -2},
        'Mage': {'initial': 1, 'new_every': 6, 'penalty': -5},
        'Illusionist': {'initial': 1, 'new_every': 6, 'penalty': -5},
        'Savant': {'initial': 1, 'new_every': 6, 'penalty': -5},
        'Thief': {'initial': 2, 'new_every': 4, 'penalty': -3},
        'Acrobat': {'initial': 2, 'new_every': 4, 'penalty': -3},
        'Mountebank': {'initial': 2, 'new_every': 4, 'penalty': -3},
    }

    def __init__(self, character_class: str):
        if character_class not in self.PROFICIENCY_RULES:
            raise ValueError(f"Character class '{character_class}' is not recognized.")
        self.character_class = character_class
        self.initial_proficiencies = self.PROFICIENCY_RULES[character_class]['initial']
        self.new_proficiency_every = self.PROFICIENCY_RULES[character_class]['new_every']
        self.penalty = self.PROFICIENCY_RULES[character_class]['penalty']

    def get_proficiency_info(self) -> Dict[str, int]:
        """Returns the proficiency details for the character class."""
        return {
            'initial_proficiencies': self.initial_proficiencies,
            'new_proficiency_every': self.new_proficiency_every,
            'penalty': self.penalty,
        }

    def __repr__(self) -> str:
        return f"WeaponProficiency(Class: {self.character_class}, Initial: {self.initial_proficiencies}, Penalty: {self.penalty})"


if __name__ == "__main__":
    # Example Usage
    fighter_proficiency = WeaponProficiency('Fighter')
    print(fighter_proficiency)
    print(fighter_proficiency.get_proficiency_info())

