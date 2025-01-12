from typing import Dict, Optional


class Barding:
    """Represents barding for mounts with type, price, weight, armor class, and movement penalty."""

    BARDING_CATALOG = {
        'Leather': {'price': 100, 'weight': 15, 'ac': 8, 'movement_penalty': -10},
        'Mail': {'price': 250, 'weight': 40, 'ac': 5, 'movement_penalty': -20},
        'Plate': {'price': 500, 'weight': 50, 'ac': 3, 'movement_penalty': -30},
    }

    def __init__(self, barding_type: str):
        if barding_type not in self.BARDING_CATALOG:
            raise ValueError(f"Barding type '{barding_type}' is not recognized.")
        barding_data = self.BARDING_CATALOG[barding_type]
        self.type: str = barding_type
        self.price: int = barding_data['price']
        self.weight: int = barding_data['weight']
        self.ac: int = barding_data['ac']
        self.movement_penalty: int = barding_data['movement_penalty']

    def get_barding_info(self) -> Dict[str, float]:
        """Returns the details of the barding."""
        return {
            'type': self.type,
            'price': self.price,
            'weight': self.weight,
            'armor_class': self.ac,
            'movement_penalty': self.movement_penalty
        }

    def __repr__(self) -> str:
        """Returns a string representation of the barding."""
        return (f"Barding({self.type}: Price {self.price} g.p., "
                f"Weight {self.weight} lbs, AC {self.ac}, "
                f"Movement Penalty {self.movement_penalty} ft/min)")


class Mount:
    """Represents a mount with its armor class and movement, including the effects of barding."""

    def __init__(self, base_ac: int, base_movement: int):
        self.base_ac: int = base_ac
        self.base_movement: int = base_movement
        self.barding: Optional[Barding] = None

    def equip_barding(self, barding_type: str) -> None:
        """Equips the mount with a barding, applying its effects."""
        self.barding = Barding(barding_type)
        print(f"Equipped {barding_type} barding on the mount.")

    def remove_barding(self) -> None:
        """Removes the barding from the mount."""
        if self.barding:
            print(f"Removed {self.barding.type} barding from the mount.")
            self.barding = None
        else:
            raise ValueError("No barding is currently equipped on the mount.")

    def calculate_total_ac(self) -> int:
        """
        Calculates the total armor class of the mount considering the barding.

        Returns:
            int: The total armor class of the mount.
        """
        if self.barding:
            total_ac = min(self.base_ac, self.barding.ac)  # Use the best (lowest) AC
        else:
            total_ac = self.base_ac
        return total_ac

    def calculate_movement(self) -> int:
        """
        Calculates the total movement speed of the mount considering the barding.

        Returns:
            int: The total movement speed of the mount.
        """
        if self.barding:
            total_movement = self.base_movement + self.barding.movement_penalty
        else:
            total_movement = self.base_movement
        return max(0, total_movement)  # Movement speed cannot be negative

    def get_mount_status(self) -> Dict[str, int]:
        """Returns the current status of the mount, including armor class and movement."""
        return {
            'armor_class': self.calculate_total_ac(),
            'movement': self.calculate_movement(),
        }

    def __repr__(self) -> str:
        """Returns a string representation of the mount's current status."""
        return (f"Mount(AC {self.calculate_total_ac()}, "
                f"Movement {self.calculate_movement()} ft/min, "
                f"Barding: {self.barding.type if self.barding else 'None'})")


# Example Usage
if __name__ == "__main__":
    mount = Mount(base_ac=9, base_movement=60)

    # Equip barding
    mount.equip_barding('Plate')

    # Calculate mount's AC and movement
    mount_status = mount.get_mount_status()
    print(f"Mount Status: AC {mount_status['armor_class']}, Movement {mount_status['movement']} ft/min")

    # Remove barding
    mount.remove_barding()
    print(mount)
