from typing import Dict, Optional


class Armor:
    """Represents an armor piece with type, price, weight, and effect on armor class."""

    ARMOR_CATALOG = {
        'Brigandine armor': {'price': 30, 'weight': 20, 'base_ac': 6, 'includes_helmet': True},
        'Buckler': {'price': 7, 'weight': 5, 'base_ac': 1, 'shield_size': 'Small'},
        'Buckler, spiked': {'price': 10, 'weight': 3, 'base_ac': 1, 'shield_size': 'Small'},
        'Cuirass (leather)': {'price': 3, 'weight': 15, 'base_ac': 8, 'includes_helmet': False},
        'Cuirass (steel)': {'price': 60, 'weight': 25, 'base_ac': 6, 'includes_helmet': False},
        'Furs': {'price': 2, 'weight': 8, 'base_ac': 9, 'includes_helmet': False},
        'Gambeson': {'price': 4, 'weight': 10, 'base_ac': 7, 'includes_helmet': False},
        'Helmet, great': {'price': 15, 'weight': 10, 'base_ac': 1, 'helmet_type': 'great'},
        'Jousting Plate': {'price': 4000, 'weight': 100, 'base_ac': 2, 'includes_helmet': True},
        'Lamellar (leather)': {'price': 15, 'weight': 20, 'base_ac': 7, 'includes_helmet': False},
        'Lamellar armor (steel)': {'price': 35, 'weight': 30, 'base_ac': 5, 'includes_helmet': False},
        'Mail': {'price': 75, 'weight': 30, 'base_ac': 5, 'includes_helmet': True},
        'Pavise': {'price': 40, 'weight': 30, 'base_ac': 2, 'shield_size': 'Special'},  # Typically used as cover, AC effect conditional
        'Plate armor': {'price': 400, 'weight': 45, 'base_ac': 3, 'includes_helmet': True},
        'Plated mail': {'price': 90, 'weight': 35, 'base_ac': 4, 'includes_helmet': True},
        'Ring armor': {'price': 30, 'weight': 25, 'base_ac': 6, 'includes_helmet': False},
        'Scale armor (leather)': {'price': 25, 'weight': 30, 'base_ac': 7, 'includes_helmet': False},
        'Scale armor (steel)': {'price': 45, 'weight': 40, 'base_ac': 5, 'includes_helmet': False},
        'Shield, large': {'price': 15, 'weight': 10, 'base_ac': 2, 'shield_size': 'Large'},
        'Shield, medium': {'price': 10, 'weight': 7, 'base_ac': 1, 'shield_size': 'Medium'},
    }

    def __init__(self, armor_type: str, is_magical: bool = False, magic_bonus: int = 0, wearing_helmet: bool = True):
        if armor_type not in self.ARMOR_CATALOG:
            raise ValueError(f"Armor type '{armor_type}' is not recognized.")
        armor_data = self.ARMOR_CATALOG[armor_type]
        self.type = armor_type
        self.price = armor_data['price']
        self.weight = armor_data['weight']
        self.base_ac = armor_data['base_ac']
        self.shield_size = armor_data.get('shield_size', None)
        self.includes_helmet = armor_data.get('includes_helmet', False)
        self.helmet_type = armor_data.get('helmet_type', None)
        self.is_magical = is_magical
        self.magic_bonus = magic_bonus
        self.durability_points = 21 + (magic_bonus * 20) if self.shield_size else None
        self.wearing_helmet = wearing_helmet

    def get_armor_info(self) -> Dict[str, float]:
        """Returns the details of the armor piece."""
        return {
            'type': self.type,
            'price': self.price,
            'weight': self.weight,
            'base_ac': self.base_ac,
            'is_magical': self.is_magical,
            'magic_bonus': self.magic_bonus,
            'durability_points': self.durability_points,
            'wearing_helmet': self.wearing_helmet
        }

    def reduce_points(self, damage: int) -> None:
        """Reduces the durability points of the shield."""
        if self.durability_points is not None:
            self.durability_points -= damage
            print(f"{self.type} shield durability reduced by {damage}. Remaining points: {self.durability_points}.")
            if self.durability_points <= 0:
                print(f"{self.type} shield is destroyed!")

    def __repr__(self) -> str:
        """Returns a string representation of the armor."""
        return (f"Armor({self.type}: Price {self.price} g.p., "
                f"Weight {self.weight} lbs, Base AC {self.base_ac})")


class ArmorInventory:
    """Manages a character's armor inventory and calculates the total armor class."""

    def __init__(self, use_optional_shield_rules: bool = False):
        self.inventory: Dict[str, Armor] = {}
        self.use_optional_shield_rules = use_optional_shield_rules
        self.helmet_ac_bonus = 1

    def add_armor(self, armor_type: str, is_magical: bool = False, magic_bonus: int = 0, wearing_helmet: bool = True) -> None:
        """Adds a piece of armor to the inventory."""
        armor = Armor(armor_type, is_magical=is_magical, magic_bonus=magic_bonus, wearing_helmet=wearing_helmet)
        self.inventory[armor_type] = armor
        print(f"Added {armor_type} to inventory.")

    def remove_armor(self, armor_type: str) -> None:
        """Removes a piece of armor from the inventory."""
        if armor_type in self.inventory:
            del self.inventory[armor_type]
            print(f"Removed {armor_type} from inventory.")
        else:
            raise ValueError(f"Armor type '{armor_type}' is not in the inventory.")

    def calculate_total_ac(self, dexterity_bonus: Optional[int] = 0, opponents: int = 1) -> int:
        """
        Calculates the total armor class based on the inventory, dexterity bonus, and opponents faced.

        Args:
            dexterity_bonus (int): The bonus to AC provided by the character's dexterity.
            opponents (int): The number of opponents faced in the round.

        Returns:
            int: The total calculated armor class.
        """
        base_ac = 10  # Default unarmored AC
        shield_ac = 0
        helmet_ac = 0

        for armor in self.inventory.values():
            if armor.shield_size:
                if armor.shield_size == 'Special':
                    # Pavise doesn't contribute to AC directly
                    continue
                if armor.shield_size == 'Small' and opponents > 1:
                    continue
                if armor.shield_size == 'Medium' and opponents > 2:
                    continue
                if armor.shield_size == 'Large' and opponents > 3:
                    continue
                shield_ac = max(shield_ac, armor.base_ac + (2 if self.use_optional_shield_rules else 1) + (2 if armor.is_magical else 0))
            else:
                base_ac -= armor.base_ac  # AC decreases as armor gets better
                if armor.includes_helmet and armor.wearing_helmet:
                    helmet_ac = self.helmet_ac_bonus
                elif not armor.wearing_helmet:
                    base_ac += 1  # No helmet increases AC by 1

        total_ac = base_ac - shield_ac - dexterity_bonus - helmet_ac
        return max(0, total_ac)  # AC cannot be less than 0

    def apply_damage_to_shield(self, attack_roll: int, required_roll: int, damage: int) -> None:
        """
        Applies damage to the shield if the attack hits it.

        Args:
            attack_roll (int): The roll needed to hit the character.
            required_roll (int): The required roll to hit without the shield.
            damage (int): The damage done to the shield.
        """
        if not self.use_optional_shield_rules:
            return

        for armor in self.inventory.values():
            if armor.shield_size and attack_roll < required_roll and attack_roll >= required_roll - 2:
                # Shield takes the hit
                if not armor.is_magical or (armor.is_magical and attack_roll < required_roll - armor.magic_bonus):
                    armor.reduce_points(damage)
                else:
                    print(f"The magic of {armor.type} absorbs the blow!")

    def calculate_movement(self) -> int:
        """
        Calculates the movement rate based on the inventory.

        Returns:
            int: The calculated movement rate in feet per minute.
        """
        movement_penalty = 0

        for armor in self.inventory.values():
            if armor.type in ['Mail', 'Plated mail', 'Plate armor']:
                movement_penalty = 50  # Heavy armor penalties
            elif armor.type in ['Brigandine armor', 'Scale armor (leather)', 'Lamellar (leather)']:
                movement_penalty = 25  # Medium armor penalties

        base_movement = 360  # Standard movement rate
        return base_movement - movement_penalty

    def get_inventory(self) -> Dict[str, Armor]:
        """Returns the current inventory of armor."""
        return self.inventory

    def __repr__(self) -> str:
        """Returns a string representation of the current armor inventory."""
        return f"Armor Inventory: {[armor.type for armor in self.inventory.values()]}"


# Example Usage
armor_inventory = ArmorInventory(use_optional_shield_rules=True)

# Add some armor
armor_inventory.add_armor('Mail', is_magical=True, magic_bonus=2, wearing_helmet=True)
armor_inventory.add_armor('Shield, large', is_magical=True, magic_bonus=2)

# Calculate total AC with a dexterity bonus of 2 and facing 2 opponents
total_ac = armor_inventory.calculate_total_ac(dexterity_bonus=2, opponents=2)
print(f"Total Armor Class: {total_ac}")

# Calculate movement rate
movement_rate = armor_inventory.calculate_movement()
print(f"Movement Rate: {movement_rate} feet per minute")

# Apply damage to shield
armor_inventory.apply_damage_to_shield(attack_roll=14, required_roll=16, damage=5)

# View inventory
print(armor_inventory)

# Remove armor
armor_inventory.remove_armor('Shield, large')
print(armor_inventory)
