from typing import Dict, Optional


class ClothingItem:
    """
    Represents a piece of clothing with its price, weight, and any special effects
    such as temperature adjustments or movement penalties.
    """

    CLOTHING_CATALOG = {
        'Belt': {'price': 0.3, 'weight': 0.3},
        'Boots, high, hard': {'price': 2, 'weight': 6},
        'Boots, high, soft': {'price': 1, 'weight': 3},
        'Boots, low, hard': {'price': 1, 'weight': 6},
        'Boots, low, soft': {'price': 0.8, 'weight': 3},
        'Cap': {'price': 0.1, 'weight': 0.2},
        'Cloak/jacket, bear': {'price': 300, 'weight': 5},
        'Cloak/jacket, beaver': {'price': 200, 'weight': 5},
        'Cloak/jacket, ermine': {'price': 3600, 'weight': 5},
        'Cloak/jacket, fox': {'price': 300, 'weight': 5},
        'Cloak/jacket, marten': {'price': 400, 'weight': 5},
        'Cloak/jacket, mink': {'price': 2700, 'weight': 5},
        'Cloak/jacket, muskrat': {'price': 100, 'weight': 5},
        'Cloak/jacket, sable': {'price': 4500, 'weight': 5},
        'Cloak/jacket, seal': {'price': 125, 'weight': 5},
        'Cloak/jacket, cloth': {'price': 0.5, 'weight': 3},
        'Cloak/jacket, leather': {'price': 5, 'weight': 4},
        'Clothing, set, arctic': {'price': 15, 'weight': 45, 'temp_adjustment': 40, 'movement_penalty': -50},
        'Clothing, set, cold weather': {'price': 7, 'weight': 25, 'temp_adjustment': 20, 'movement_penalty': -25},
        'Clothing, set, lower class': {'price': 0.1, 'weight': 3},
        'Clothing, set, middle class': {'price': 1, 'weight': 3},
        'Clothing, set, upper class': {'price': 10, 'weight': 3},
        'Coat, bear': {'price': 600, 'weight': 7},
        'Coat, beaver': {'price': 400, 'weight': 7},
        'Coat, ermine': {'price': 7200, 'weight': 7},
        'Coat, fox': {'price': 600, 'weight': 7},
        'Coat, marten': {'price': 800, 'weight': 7},
        'Coat, mink': {'price': 5400, 'weight': 7},
        'Coat, muskrat': {'price': 200, 'weight': 7},
        'Coat, sable': {'price': 9000, 'weight': 7},
        'Coat, seal': {'price': 250, 'weight': 7},
        'Coat, cloth': {'price': 1, 'weight': 5},
        'Coat, leather': {'price': 10, 'weight': 6},
        'Girdle, wide': {'price': 2, 'weight': 2},
        'Girdle, normal': {'price': 1, 'weight': 1},
        'Hat': {'price': 0.7, 'weight': 0.3},
        'Robe': {'price': 0.6, 'weight': 5},
        'Trim, bear': {'price': 30, 'weight': 0},
        'Trim, beaver': {'price': 20, 'weight': 0},
        'Trim, ermine': {'price': 120, 'weight': 0},
        'Trim, fox': {'price': 30, 'weight': 0},
        'Trim, marten': {'price': 40, 'weight': 0},
        'Trim, mink': {'price': 90, 'weight': 0},
        'Trim, muskrat': {'price': 10, 'weight': 0},
        'Trim, sable': {'price': 150, 'weight': 0},
        'Trim, seal': {'price': 25, 'weight': 0},
    }

    def __init__(self, clothing_type: str):
        if clothing_type not in self.CLOTHING_CATALOG:
            raise ValueError(f"Clothing type '{clothing_type}' is not recognized.")
        clothing_data = self.CLOTHING_CATALOG[clothing_type]
        self.type: str = clothing_type
        self.price: float = clothing_data['price']
        self.weight: float = clothing_data['weight']
        self.temp_adjustment: Optional[int] = clothing_data.get('temp_adjustment', 0)
        self.movement_penalty: Optional[int] = clothing_data.get('movement_penalty', 0)

    def get_clothing_info(self) -> Dict[str, Optional[float]]:
        """Returns the details of the clothing item."""
        return {
            'type': self.type,
            'price': self.price,
            'weight': self.weight,
            'temp_adjustment': self.temp_adjustment,
            'movement_penalty': self.movement_penalty,
        }

    def __repr__(self) -> str:
        """Returns a string representation of the clothing item."""
        return (f"ClothingItem({self.type}: Price {self.price} g.p., "
                f"Weight {self.weight} lbs, Temp Adjustment {self.temp_adjustment}°, "
                f"Movement Penalty {self.movement_penalty}%)")


# Example Usage
if __name__ == "__main__":
    # Create a clothing item
    arctic_clothing = ClothingItem('Clothing, set, arctic')

    # Display clothing details
    clothing_info = arctic_clothing.get_clothing_info()
    print(f"Clothing Info: {clothing_info}")

    # Represent the clothing item
    print(arctic_clothing)
