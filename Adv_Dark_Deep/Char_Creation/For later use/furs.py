from typing import Dict, Optional


class FurItem:
    """
    Represents a fur item with its price and weight.
    """

    FUR_CATALOG = {
        'Bear pelt': {'price': 30, 'weight': 10},
        'Beaver pelt': {'price': 2, 'weight': 1},
        'Ermine pelt': {'price': 4, 'weight': 1},
        'Fox pelt': {'price': 3, 'weight': 1},
        'Marten pelt': {'price': 4, 'weight': 1},
        'Mink pelt': {'price': 3, 'weight': 1},
        'Muskrat': {'price': 1, 'weight': 1},
        'Sable pelt': {'price': 5, 'weight': 1},
        'Seal pelt': {'price': 5, 'weight': 2},
    }

    def __init__(self, fur_name: str):
        if fur_name not in self.FUR_CATALOG:
            raise ValueError(f"Fur item '{fur_name}' is not recognized.")
        fur_data = self.FUR_CATALOG[fur_name]
        self.name: str = fur_name
        self.price: float = fur_data['price']
        self.weight: float = fur_data['weight']

    def get_item_info(self) -> Dict[str, Optional[float]]:
        """Returns the details of the fur item."""
        return {
            'name': self.name,
            'price': self.price,
            'weight': self.weight,
        }

    def __repr__(self) -> str:
        """Returns a string representation of the fur item."""
        return f"FurItem({self.name}: Price {self.price} g.p., Weight {self.weight} lbs)"


# Example Usage
if __name__ == "__main__":
    # Create a fur item
    bear_pelt = FurItem('Bear pelt')

    # Display item details
    item_info = bear_pelt.get_item_info()
    print(f"Item Info: {item_info}")

    # Represent the item
    print(bear_pelt)
