from typing import Dict, Optional


class Weapon:
    """
    Represents a weapon with its price, weight, and other characteristics.
    """

    WEAPON_CATALOG = {
        'Aklys': {'price': 2, 'weight': 3, 'unit': 'g.p.'},
        'Arrow, normal, dozen': {'price': 1, 'weight': 1, 'unit': 'g.p.'},
        'Arrow, normal, single': {'price': 0.2, 'weight': 0.2, 'unit': 'g.p.'},
        'Arrow, silver head, single': {'price': 1, 'weight': 0.2, 'unit': 'g.p.'},
        'Atlatl': {'price': 1, 'weight': 3, 'unit': 'g.p.'},
        'Axe, battle': {'price': 5, 'weight': 7, 'unit': 'g.p.'},
        'Axe, hand': {'price': 1, 'weight': 5, 'unit': 'g.p.'},
        'Axe, throwing': {'price': 1, 'weight': 5, 'unit': 'g.p.'},
        'Bardiche': {'price': 7, 'weight': 12, 'unit': 'g.p.'},
        'Bec de corbin': {'price': 6, 'weight': 10, 'unit': 'g.p.'},
        'Bill-guisarme': {'price': 6, 'weight': 15, 'unit': 'g.p.'},
        'Blowgun': {'price': 20, 'weight': 1, 'unit': 'g.p.'},
        'Blowgun needle': {'price': 0.1, 'weight': 0.1, 'unit': 'g.p.'},
        'Bow, composite, long': {'price': 100, 'weight': 8, 'unit': 'g.p.'},
        'Bow, composite, short': {'price': 75, 'weight': 5, 'unit': 'g.p.'},
        'Bow, long': {'price': 60, 'weight': 10, 'unit': 'g.p.'},
        'Bow, short': {'price': 15, 'weight': 5, 'unit': 'g.p.'},
        'Caltrop': {'price': 0.2, 'weight': 0.5, 'unit': 'g.p.'},
        'Crossbow bolt, hand': {'price': 10, 'weight': 0.1, 'unit': 'g.p.'},
        'Crossbow bolt, heavy': {'price': 0.2, 'weight': 0.2, 'unit': 'g.p.'},
        'Crossbow bolt, light': {'price': 0.1, 'weight': 0.1, 'unit': 'g.p.'},
        'Crossbow, hand': {'price': 300, 'weight': 2, 'unit': 'g.p.'},
        'Crossbow, heavy': {'price': 20, 'weight': 8, 'unit': 'g.p.'},
        'Crossbow, light': {'price': 12, 'weight': 5, 'unit': 'g.p.'},
        'Crossbow, repeating': {'price': 50, 'weight': 6, 'unit': 'g.p.'},
        'Crossbow, underwater': {'price': 120, 'weight': 5, 'unit': 'g.p.'},
        'Dagger': {'price': 2, 'weight': 1, 'unit': 'g.p.'},
        'Dart': {'price': 0.5, 'weight': 0.5, 'unit': 'g.p.'},
        'Falchion': {'price': 10, 'weight': 7, 'unit': 'g.p.'},
        'Fauchard': {'price': 3, 'weight': 6, 'unit': 'g.p.'},
        'Fauchard-fork': {'price': 8, 'weight': 8, 'unit': 'g.p.'},
        'Flail, footman’s': {'price': 3, 'weight': 15, 'unit': 'g.p.'},
        'Flail, horseman’s': {'price': 8, 'weight': 3, 'unit': 'g.p.'},
        'Garrote': {'price': 1, 'weight': 0.1, 'unit': 'e.p.'},
        'Glaive': {'price': 6, 'weight': 7, 'unit': 'g.p.'},
        'Glaive-guisarme': {'price': 10, 'weight': 10, 'unit': 'g.p.'},
        'Guisarme': {'price': 5, 'weight': 8, 'unit': 'g.p.'},
        'Guisarme-voulge': {'price': 7, 'weight': 15, 'unit': 'g.p.'},
        'Halberd': {'price': 9, 'weight': 17, 'unit': 'g.p.'},
        'Hammer, war': {'price': 1, 'weight': 5, 'unit': 'g.p.'},
        'Hammer, lucern': {'price': 7, 'weight': 15, 'unit': 'g.p.'},
        'Harpoon': {'price': 5, 'weight': 6, 'unit': 'g.p.'},
        'Hook fauchard': {'price': 6, 'weight': 8, 'unit': 'g.p.'},
        'Javelin': {'price': 0.1, 'weight': 2, 'unit': 'g.p.'},
        'Khopesh': {'price': 10, 'weight': 7, 'unit': 'g.p.'},
        'Knife': {'price': 1, 'weight': 0.5, 'unit': 'g.p.'},
        'Lance, light': {'price': 6, 'weight': 5, 'unit': 'g.p.'},
        'Lance, medium': {'price': 6, 'weight': 10, 'unit': 'g.p.'},
        'Lance, heavy': {'price': 6, 'weight': 15, 'unit': 'g.p.'},
        'Lasso': {'price': 0.5, 'weight': 2, 'unit': 'g.p.'},
        'Mace, footman’s': {'price': 8, 'weight': 10, 'unit': 'g.p.'},
        'Mace, horseman’s': {'price': 4, 'weight': 5, 'unit': 'g.p.'},
        'Mace, two-handed': {'price': 13, 'weight': 15, 'unit': 'g.p.'},
        'Man catcher': {'price': 25, 'weight': 8, 'unit': 'g.p.'},
        'Military fork': {'price': 4, 'weight': 7, 'unit': 'g.p.'},
        'Morning star': {'price': 5, 'weight': 12, 'unit': 'g.p.'},
        'Partisan': {'price': 10, 'weight': 8, 'unit': 'g.p.'},
        'Pick, military, footman’s': {'price': 8, 'weight': 6, 'unit': 'g.p.'},
        'Pick, military, horseman’s': {'price': 5, 'weight': 4, 'unit': 'g.p.'},
        'Pike, awl': {'price': 3, 'weight': 8, 'unit': 'g.p.'},
        'Pole axe': {'price': 8, 'weight': 15, 'unit': 'g.p.'},
        'Quarterstaff': {'price': 3, 'weight': 10, 'unit': 'g.p.'},
        'Ranseur': {'price': 4, 'weight': 5, 'unit': 'g.p.'},
        'Sap': {'price': 1, 'weight': 1, 'unit': 'g.p.'},
        'Scimitar': {'price': 15, 'weight': 4, 'unit': 'g.p.'},
        'Scythe': {'price': 18, 'weight': 10, 'unit': 'g.p.'},
        'Sling': {'price': 0.1, 'weight': 0.1, 'unit': 'g.p.'},
        'Sling bullets (dozen)': {'price': 0.1, 'weight': 1, 'unit': 'g.p.'},
        'Sling stones (dozen)': {'price': 0, 'weight': 0.5, 'unit': 'g.p.'},
        'Spear': {'price': 1, 'weight': 5, 'unit': 'g.p.'},
        'Spetum': {'price': 3, 'weight': 5, 'unit': 'g.p.'},
        'Spiked Buckler': {'price': 10, 'weight': 3, 'unit': 'g.p.'},
        'Staff sling': {'price': 2, 'weight': 10, 'unit': 'g.p.'},
        'Sword, bastard': {'price': 25, 'weight': 10, 'unit': 'g.p.'},
        'Sword, broad': {'price': 10, 'weight': 7, 'unit': 'g.p.'},
        'Sword, long': {'price': 15, 'weight': 6, 'unit': 'g.p.'},
        'Sword, short': {'price': 8, 'weight': 3, 'unit': 'g.p.'},
        'Sword, two-handed': {'price': 30, 'weight': 25, 'unit': 'g.p.'},
        'Trident': {'price': 4, 'weight': 5, 'unit': 'g.p.'},
        'Voulge': {'price': 2, 'weight': 12, 'unit': 'g.p.'},
        'Whip': {'price': 3, 'weight': 3, 'unit': 'g.p.'},
    }

    def __init__(self, name: str, material: Optional[str] = 'steel'):
        if name not in self.WEAPON_CATALOG:
            raise ValueError(f"Weapon '{name}' is not recognized.")

        self.name: str = name
        self.base_price: float = self.WEAPON_CATALOG[name]['price']
        self.weight: float = self.WEAPON_CATALOG[name]['weight']
        self.unit: str = self.WEAPON_CATALOG[name]['unit']
        self.material: str = material.lower()

        if self.material == 'silver':
            self.price = self.base_price + (10 * self.weight)
        elif self.material == 'iron':
            self.price = self.base_price
        else:  # Default is steel or similar materials
            self.price = self.base_price

    def calculate_saving_throw(self, missed_attack: bool) -> Optional[bool]:
        """
        Determines if a weapon made of iron is damaged after a missed attack.
        This method only applies to iron weapons.
        """
        if self.material != 'iron' or not missed_attack:
            return None

        import random
        success = random.randint(1, 20) >= 10  # Simplified saving throw mechanic
        if not success:
            print(f"The iron weapon {self.name} has been damaged.")
        return success

    def __repr__(self) -> str:
        """
        Returns a string representation of the weapon.
        """
        return (f"Weapon(Name: {self.name}, Material: {self.material.title()}, "
                f"Price: {self.price} {self.unit}, Weight: {self.weight} lbs.)")


# Example Usage
if __name__ == "__main__":
    # Create a weapon (e.g., 'Sword, long' made of silver)
    weapon = Weapon('Sword, long', material='silver')

    # Display the weapon's details
    print(weapon)

    # Check if an iron weapon is damaged after a missed attack
    iron_weapon = Weapon('Axe, battle', material='iron')
    print(iron_weapon.calculate_saving_throw(missed_attack=True))
