from typing import Dict, Optional


class FoodAndDrinkItem:
    """
    Represents a food or drink item with its price and weight.
    """

    FOOD_DRINK_CATALOG = {
        'Ale, pint': {'price': 0.1, 'weight': 1},
        'Beer, small, pint': {'price': 0.05, 'weight': 1},
        'Meal, standard': {'price': 0.1, 'weight': 2},
        'Meal, rich': {'price': 1, 'weight': 3},
        'Horse fodder, 1 day': {'price': 0.1, 'weight': 10},
        'Mead, pint': {'price': 0.5, 'weight': 5},
        'Rations, dry tack, 1 week': {'price': 5, 'weight': 7},
        'Rations, standard, 1 week': {'price': 3, 'weight': 20},
        'Wine, pint': {'price': 0.5, 'weight': 5},
    }

    def __init__(self, item_name: str):
        if item_name not in self.FOOD_DRINK_CATALOG:
            raise ValueError(f"Food or drink item '{item_name}' is not recognized.")
        item_data = self.FOOD_DRINK_CATALOG[item_name]
        self.name: str = item_name
        self.price: float = item_data['price']
        self.weight: float = item_data['weight']

    def get_item_info(self) -> Dict[str, Optional[float]]:
        """Returns the details of the food or drink item."""
        return {
            'name': self.name,
            'price': self.price,
            'weight': self.weight,
        }

    def __repr__(self) -> str:
        """Returns a string representation of the food or drink item."""
        return f"FoodAndDrinkItem({self.name}: Price {self.price} g.p., Weight {self.weight} lbs)"


# Example Usage
if __name__ == "__main__":
    # Create a food or drink item
    rations = FoodAndDrinkItem('Rations, dry tack, 1 week')

    # Display item details
    item_info = rations.get_item_info()
    print(f"Item Info: {item_info}")

    # Represent the item
    print(rations)
