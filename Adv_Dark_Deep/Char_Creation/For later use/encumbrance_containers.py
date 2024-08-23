from typing import Dict, Optional


class Container:
    """
    Represents a container that can hold items.
    """

    def __init__(self, name: str, capacity_cu_ft: float, capacity_coins: int, capacity_weight: float):
        self.name: str = name
        self.capacity_cu_ft: float = capacity_cu_ft
        self.capacity_coins: int = capacity_coins
        self.capacity_weight: float = capacity_weight

    def __repr__(self) -> str:
        return f"Container({self.name}, Capacity: {self.capacity_cu_ft} cu. ft., {self.capacity_coins} coins, {self.capacity_weight} lbs.)"


class Encumbrance:
    """
    Represents the encumbrance system, calculating the effect of carried items on a character's movement.
    """
    BASE_MOVEMENT = 360  # feet per minute, unencumbered

    def __init__(self, strength: int, weight: float, containers: Optional[Dict[str, Container]] = None):
        self.strength: int = strength
        self.weight: float = weight
        self.containers: Dict[str, Container] = containers if containers else {}
        self.carried_weight: float = 0

    def add_item(self, item_weight: float) -> None:
        """
        Adds the weight of an item to the carried weight.
        """
        self.carried_weight += item_weight

    def calculate_movement_penalty(self) -> int:
        """
        Calculates the movement penalty based on the weight carried.
        """
        total_weight = self.carried_weight + self.weight
        encumbrance_percentage = (total_weight - self.weight) / self.weight * 100

        penalty = int(encumbrance_percentage // 10) * 10
        return max(self.BASE_MOVEMENT - penalty, 10)

    def calculate_container_capacity(self, container_name: str, item_weight: float, item_volume: float) -> bool:
        """
        Checks if an item can be added to a specified container.
        """
        container = self.containers.get(container_name)
        if not container:
            raise ValueError(f"Container '{container_name}' not found.")

        if item_weight > container.capacity_weight or item_volume > container.capacity_cu_ft:
            return False

        container.capacity_weight -= item_weight
        container.capacity_cu_ft -= item_volume
        return True

    def __repr__(self) -> str:
        return f"Encumbrance(Strength: {self.strength}, Carried Weight: {self.carried_weight}, Movement Penalty: {self.calculate_movement_penalty()} feet/min)"


# Example Usage
if __name__ == "__main__":
    # Create containers
    backpack = Container(name="Backpack", capacity_cu_ft=3.0, capacity_coins=300, capacity_weight=30)
    large_chest = Container(name="Large Chest", capacity_cu_ft=12.0, capacity_coins=1500, capacity_weight=150)

    # Create an encumbrance object for a character with 15 STR and weighing 180 lbs
    encumbrance = Encumbrance(strength=15, weight=180, containers={"backpack": backpack, "large_chest": large_chest})

    # Add items to the character's carried weight
    encumbrance.add_item(50)  # 50 lbs of gear

    # Calculate movement penalty
    print(f"Current Movement Rate: {encumbrance.calculate_movement_penalty()} feet/min")

    # Add items to a container
    if encumbrance.calculate_container_capacity("backpack", item_weight=10, item_volume=1.0):
        print(
            f"Added item to backpack. Remaining capacity: {backpack.capacity_weight} lbs, {backpack.capacity_cu_ft} cu. ft.")
    else:
        print("Item too large/heavy for backpack.")

    # Display encumbrance status
    print(encumbrance)
