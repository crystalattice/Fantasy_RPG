from typing import Dict, Optional


class Armor:
    """Represents an armor piece with type, price, weight, and effect on armor class."""

    ARMOR_CATALOG = {
        'Brigandine armor': {'price': 30, 'weight': 20, 'base_ac': 6},
        'Buckler': {'price': 7, 'weight': 5, 'base_ac': 1},
        'Buckler, spiked': {'price': 10, 'weight': 3, 'base_ac': 1},
        'Cuirass (leather)': {'price': 3, 'weight': 15, 'base_ac': 8},
        'Cuirass (steel)': {'price': 60, 'weight': 25, 'base_ac': 6},
        'Furs': {'price': 2, 'weight': 8, 'base_ac': 9},
        'Gambeson': {'price': 4, 'weight': 10, 'base_ac': 7},
        'Helmet, great': {'price': 15, 'weight': 10, 'base_ac': 0},  # AC bonus depends on circumstances
        'Jousting Plate': {'price': 4000, 'weight': 100, 'base_ac': 2},
        'Lamellar (leather)': {'price': 15, 'weight': 20, 'base_ac': 7},
        'Lamellar armor (steel)': {'price': 35, 'weight': 30, 'base_ac': 5},
        'Mail': {'price': 75, 'weight': 30, 'base_ac': 5},
        'Pavise': {'price': 40, 'weight': 30, 'base_ac': 2},  # Typically used as cover, AC effect conditional
        'Plate armor': {'price': 400, 'weight': 45, 'base_ac': 3},
        'Plated mail': {'price': 90, 'weight': 35, 'base_ac': 4},
        'Ring armor': {'price': 30, 'weight': 25, 'base_ac': 6},
        'Scale armor (leather)': {'price': 25, 'weight': 30, 'base_ac': 7},
        'Scale armor (steel)': {'price': 45, 'weight': 40, 'base_ac': 5},
        'Shield, large': {'price': 15, 'weight': 10, 'base_ac': 2},
        'Shield, medium': {'price': 10, 'weight': 7, 'base_ac': 1},
    }

    def __init__(self, armor_type: str):
        if armor_type not in self.ARMOR_CATALOG:
            raise ValueError(f"Armor type '{armor_type}' is not recognized.")
        armor_data = self.ARMOR_CATALOG[armor_type]
        self.type = armor_type
        self.price = armor_data['price']
        self.weight = armor_data['weight']
        self.base_ac = armor_data['base_ac']

    def get_armor_info(self) -> Dict[str, float]:
        """Returns the details of the armor piece."""
        return {
            'type': self.type,
            'price': self.price,
            'weight': self.weight,
            'base_ac': self.base_ac
        }

    def __repr__(self) -> str:
        """Returns a string representation of the armor."""
        return (f"Armor({self.type}: Price {self.price} g.p., "
                f"Weight {self.weight} lbs, Base AC {self.base_ac})")


class ArmorInventory:
    """Manages a character's armor inventory and calculates the total armor class."""

    def __init__(self):
        self.inventory: Dict[str, Armor] = {}

    def add_armor(self, armor_type: str) -> None:
        """Adds a piece of armor to the inventory."""
        armor = Armor(armor_type)
        self.inventory[armor_type] = armor
        print(f"Added {armor_type} to inventory.")

    def remove_armor(self, armor_type: str) -> None:
        """Removes a piece of armor from the inventory."""
        if armor_type in self.inventory:
            del self.inventory[armor_type]
            print(f"Removed {armor_type} from inventory.")
        else:
            raise ValueError(f"Armor type '{armor_type}' is not in the inventory.")

    def calculate_total_ac(self, dexterity_bonus: Optional[int] = 0) -> int:
        """
        Calculates the total armor class based on the inventory and dexterity bonus.

        Args:
            dexterity_bonus (int): The bonus to AC provided by the character's dexterity.

        Returns:
            int: The total calculated armor class.
        """
        base_ac = 10  # Default unarmored AC
        for armor in self.inventory.values():
            base_ac -= armor.base_ac  # AC decreases as armor gets better

        total_ac = base_ac - dexterity_bonus
        return max(0, total_ac)  # AC cannot be less than 0

    def get_inventory(self) -> Dict[str, Armor]:
        """Returns the current inventory of armor."""
        return self.inventory

    def __repr__(self) -> str:
        """Returns a string representation of the current armor inventory."""
        return f"Armor Inventory: {[armor.type for armor in self.inventory.values()]}"


# Example Usage
armor_inventory = ArmorInventory()

# Add some armor
armor_inventory.add_armor('Mail')
armor_inventory.add_armor('Shield, large')

# Calculate total AC with a dexterity bonus of 2
total_ac = armor_inventory.calculate_total_ac(dexterity_bonus=2)
print(f"Total Armor Class: {total_ac}")

# View inventory
print(armor_inventory)

# Remove armor
armor_inventory.remove_armor('Shield, large')
print(armor_inventory)
