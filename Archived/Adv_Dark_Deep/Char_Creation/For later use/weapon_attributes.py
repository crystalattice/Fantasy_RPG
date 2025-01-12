from typing import Dict, Optional
import random


class Weapon:
    """Represents a weapon with attributes like cost, weight, speed, damage, material (iron, silver, etc.), and adjustments vs. armor."""

    WEAPON_CATALOG = {
        'Axe, battle': {'cost': 5, 'weight': 7, 'length': 4, 'space': 4, 'speed': 7, 'damage_sm': '1d8', 'damage_l': '1d8'},
        'Dagger': {'cost': 2, 'weight': 1, 'length': 15, 'space': 1, 'speed': 2, 'damage_sm': '1d4', 'damage_l': '1d3'},
        'Sword, long': {'cost': 15, 'weight': 6, 'length': 42, 'space': 3, 'speed': 5, 'damage_sm': '1d8', 'damage_l': '1d12'},
        # Add more weapons as needed...
    }

    ADJUSTMENT_TABLE = {
        'Axe, battle': {'Plate Armor': -2, 'Mail': -1, 'Leather': +1, 'Shield Only': +1, 'None': +2},
        'Dagger': {'Plate Armor': -4, 'Mail': -3, 'Leather': 0, 'Shield Only': +1, 'None': +3},
        'Sword, long': {'Plate Armor': 0, 'Mail': +1, 'Leather': +1, 'Shield Only': +1, 'None': +2},
        # Add more weapons with their respective adjustments...
    }

    def __init__(self, weapon_name: str, material: Optional[str] = "steel"):
        if weapon_name not in self.WEAPON_CATALOG:
            raise ValueError(f"Weapon '{weapon_name}' is not recognized.")
        weapon_data = self.WEAPON_CATALOG[weapon_name]
        self.name = weapon_name
        self.cost = weapon_data['cost']
        self.weight = weapon_data['weight']
        self.length = weapon_data['length']
        self.space = weapon_data['space']
        self.speed = weapon_data['speed']
        self.damage_sm = weapon_data['damage_sm']
        self.damage_l = weapon_data['damage_l']
        self.material = material
        self.damage_penalty = 0

        # Material-specific modifications
        if self.material == "silver":
            self.cost += self.weight * 10
            self.saving_throw_penalty = -2
        elif self.material == "iron":
            self.saving_throw_penalty = 0
        else:
            self.saving_throw_penalty = None  # Regular steel weapons don't need to save

        # Load weapon adjustment vs. armor
        self.adjustment = self.ADJUSTMENT_TABLE.get(weapon_name, {})

    def make_saving_throw(self, dc: int) -> bool:
        """Simulates a saving throw for the weapon, returning True if successful, False if not."""
        if self.saving_throw_penalty is not None:
            roll = random.randint(1, 20)
            success = roll >= dc + self.saving_throw_penalty
            if not success:
                self.damage_penalty -= 1
            return success
        return True  # No saving throw needed for steel weapons

    def get_weapon_info(self) -> Dict[str, str]:
        """Returns the details of the weapon."""
        return {
            'name': self.name,
            'cost': self.cost,
            'weight': self.weight,
            'length': self.length,
            'space': self.space,
            'speed': self.speed,
            'damage_sm': f"{self.damage_sm}{self.damage_penalty:+d}",
            'damage_l': f"{self.damage_l}{self.damage_penalty:+d}",
            'material': self.material,
        }

    def get_adjustment_vs_armor(self, armor_type: str) -> int:
        """Returns the weapon's adjustment against a specific type of armor."""
        return self.adjustment.get(armor_type, 0)

    def __repr__(self) -> str:
        return (f"Weapon({self.name}: Material {self.material}, Cost {self.cost} g.p., "
                f"Damage S/M {self.damage_sm}, Damage L {self.damage_l})")


if __name__ == "__main__":
    # Example Usage
    silver_dagger = Weapon('Dagger', material='silver')
    print(silver_dagger)
    print(silver_dagger.get_weapon_info())

    iron_sword = Weapon('Sword, long', material='iron')
    print(iron_sword)
    print(f"Initial Damage: {iron_sword.get_weapon_info()['damage_sm']}")
    # Simulating a miss and checking the saving throw
    if not iron_sword.make_saving_throw(15):
        print(f"Damage after fail: {iron_sword.get_weapon_info()['damage_sm']}")

    steel_axe = Weapon('Axe, battle')
    print(steel_axe)
    print(steel_axe.get_weapon_info())
