from typing import Dict, Optional, Union

class LuxuryItem:
    """
    Represents a luxury item with a specific price and weight.
    """

    LUXURY_ITEM_CATALOG = {
        'Brocade, rug, or tapestry': {'price': (1, 20), 'price_unit': 'g.p. / sq. yard', 'weight': 10, 'weight_unit': 'lbs. / sq. yard'},
        'Incense, rare': {'price': (4, 30), 'price_unit': 'g.p. / stick', 'weight': 0.1, 'weight_unit': 'lbs.'},
        'Ivory': {'price': (3, 6), 'price_unit': 'g.p. / lb.', 'weight': 0.1, 'weight_unit': 'lbs.'},
        'Pepper': {'price': 1, 'price_unit': 'g.p. / ounce', 'weight': 0.1, 'weight_unit': 'lbs.'},
        'Perfume, rare': {'price': (1, 6), 'price_unit': 'g.p. / dram', 'weight': 0.1, 'weight_unit': 'lbs.'},
        'Silk': {'price': (1, 3), 'price_unit': 'g.p. / sq. yard', 'weight': 1, 'weight_unit': 'lbs. / sq. yard'},
        'Spice, rare': {'price': (1, 4), 'price_unit': 's.p. / scruple', 'weight': 0.1, 'weight_unit': 'lbs.'},
        'Unguent, rare': {'price': (10, 60), 'price_unit': 'g.p. / gill', 'weight': 0.1, 'weight_unit': 'lbs.'},
    }

    def __init__(self, name: str):
        if name not in self.LUXURY_ITEM_CATALOG:
            raise ValueError(f"Luxury item '{name}' is not recognized.")
        self.name: str = name
        self.price_range: Union[int, tuple] = self.LUXURY_ITEM_CATALOG[name]['price']
        self.price_unit: str = self.LUXURY_ITEM_CATALOG[name]['price_unit']
        self.weight: float = self.LUXURY_ITEM_CATALOG[name]['weight']
        self.weight_unit: str = self.LUXURY_ITEM_CATALOG[name]['weight_unit']

    def get_price(self) -> str:
        """
        Returns a string representing the price range of the luxury item.
        """
        if isinstance(self.price_range, tuple):
            return f"{self.price_range[0]}-{self.price_range[1]} {self.price_unit}"
        return f"{self.price_range} {self.price_unit}"

    def get_weight(self) -> str:
        """
        Returns a string representing the weight of the luxury item.
        """
        return f"{self.weight} {self.weight_unit}"

    def get_item_info(self) -> Dict[str, Union[str, float]]:
        """
        Returns the details of the luxury item.
        """
        return {
            'name': self.name,
            'price': self.get_price(),
            'weight': self.get_weight(),
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the luxury item.
        """
        return f"LuxuryItem(Name: {self.name}, Price: {self.get_price()}, Weight: {self.get_weight()})"


# Example Usage
if __name__ == "__main__":
    # Create a luxury item (e.g., 'Silk')
    silk = LuxuryItem('Silk')

    # Display luxury item details
    item_info = silk.get_item_info()
    print(f"Luxury Item Info: {item_info}")

    # Represent the luxury item
    print(silk)
