from typing import Dict, Optional, Union
import random


class Poison:
    """
    Represents a poison with a specific type, onset time, damage, and cost per dose.
    It also handles the detection and effects of poison on a target.
    """

    POISON_CATALOG = {
        'Swallowed A': {
            'price': 5, 'onset_time': '2d4 min', 'damage': (10, 20), 'save_bonus': +4, 'detect_chance': 80
        },
        'Swallowed B': {
            'price': 30, 'onset_time': '1d4+1 min', 'damage': (15, 30), 'save_bonus': +3, 'detect_chance': 65
        },
        'Swallowed C': {
            'price': 200, 'onset_time': '1-2 min', 'damage': (20, 40), 'save_bonus': +2, 'detect_chance': 40
        },
        'Swallowed D': {
            'price': 500, 'onset_time': '6 sec', 'damage': (25, 'death'), 'save_bonus': +1, 'detect_chance': 15
        },
        'Swallowed E': {
            'price': 1000, 'onset_time': '1d4x10 min', 'damage': (30, 'death'), 'save_bonus': +1, 'detect_chance': 15
        },
        'Blade venom A': {
            'price': 10, 'onset_time': '1d4+1 min', 'damage': (0, 15), 'save_bonus': +4, 'detect_chance': 80
        },
        'Blade venom B': {
            'price': 75, 'onset_time': '1d3 min', 'damage': (0, 25), 'save_bonus': +3, 'detect_chance': 65
        },
        'Blade venom C': {
            'price': 600, 'onset_time': '1 min', 'damage': (0, 35), 'save_bonus': +2, 'detect_chance': 40
        },
        'Blade venom D': {
            'price': 1500, 'onset_time': '6 sec', 'damage': (0, 'death'), 'save_bonus': +1, 'detect_chance': 15
        },
        'Antidote A': {'price': 10},
        'Antidote B': {'price': 60},
        'Antidote C': {'price': 400},
        'Antidote D': {'price': 500},
    }

    def __init__(self, name: str):
        if name not in self.POISON_CATALOG:
            raise ValueError(f"Poison '{name}' is not recognized.")
        self.name: str = name
        self.price: int = self.POISON_CATALOG[name]['price']
        self.onset_time: Optional[str] = self.POISON_CATALOG[name].get('onset_time')
        self.damage: Optional[Union[int, str, tuple]] = self.POISON_CATALOG[name].get('damage')
        self.save_bonus: Optional[int] = self.POISON_CATALOG[name].get('save_bonus')
        self.detect_chance: Optional[int] = self.POISON_CATALOG[name].get('detect_chance')

    def use_poison(self, target_save_roll: int) -> Dict[str, Union[str, int, bool]]:
        """
        Determines the effect of the poison on the target based on their saving throw.
        """
        if self.name.startswith('Antidote'):
            return {'effect': 'Antidote used, poison neutralized', 'success': True}

        save_roll = target_save_roll + (self.save_bonus or 0)
        successful_save = save_roll >= 20

        if successful_save:
            damage = self.damage[0] if isinstance(self.damage, tuple) else 0
        else:
            damage = self.damage[1] if isinstance(self.damage, tuple) else 'death'

        detection = random.randint(1, 100) <= self.detect_chance if self.detect_chance else False

        return {
            'poison_type': self.name,
            'onset_time': self.onset_time,
            'damage': damage,
            'save_successful': successful_save,
            'detected': detection,
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the poison.
        """
        return (f"Poison(Name: {self.name}, Price: {self.price} g.p., Onset Time: {self.onset_time}, "
                f"Damage: {self.damage}, Save Bonus: {self.save_bonus}, Detect Chance: {self.detect_chance}%)")


# Example Usage
if __name__ == "__main__":
    # Create a poison (e.g., 'Swallowed C')
    poison = Poison('Swallowed C')

    # Simulate using the poison on a target with a saving throw roll of 14
    result = poison.use_poison(14)

    # Display the result of the poison use
    print(f"Poison Result: {result}")

    # Represent the poison
    print(poison)
