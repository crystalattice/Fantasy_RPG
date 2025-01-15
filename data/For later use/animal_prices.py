from typing import Dict
from currency import MonetarySystem

class AnimalMarket:
    """Handles the purchase and sale of animals with their respective prices."""

    # Prices of animals in gold pieces (g.p.)
    ANIMAL_PRICES = {
        'Chicken': 0.015,  # 3 copper pieces
        'Cow': 10,
        'Dog, guard': 25,
        'Dog, hunting': 17,
        'Donkey': 8,
        'Goat': 1,
        'Hawk, large': 40,
        'Hawk, small': 18,
        'Horse, draft': 30,
        'Horse, war, heavy': 300,
        'Horse, war, light': 150,
        'Horse, war, medium': 225,
        'Horse, riding': 25,
        'Mule': 20,
        'Ox': 15,
        'Pigeon': 0.01,  # 2 copper pieces
        'Pig': 3,
        'Pony': 15,
        'Sheep': 2,
        'Songbird': 0.02  # 4 copper pieces
    }

    def __init__(self):
        self.inventory = {}

    def buy_animal(self, animal: str, quantity: int, currency_system) -> None:
        """
        Buys a specific number of animals, deducting the cost from the currency system.

        Args:
            animal (str): The type of animal to purchase.
            quantity (int): The number of animals to purchase.
            currency_system (MonetarySystem): The currency system to deduct from.

        Raises:
            ValueError: If the animal type is not recognized or there are insufficient funds.
        """
        if animal not in self.ANIMAL_PRICES:
            raise ValueError(f"Animal '{animal}' is not available for purchase.")

        total_cost = self.ANIMAL_PRICES[animal] * quantity
        current_gold = currency_system.convert_to_gold()

        if total_cost > current_gold:
            raise ValueError("Insufficient funds to purchase the animals.")

        currency_system.subtract_currency(gold=total_cost)
        self.inventory[animal] = self.inventory.get(animal, 0) + quantity
        print(f"Purchased {quantity} {animal}(s) for {total_cost} gold pieces.")

    def sell_animal(self, animal: str, quantity: int, currency_system) -> None:
        """
        Sells a specific number of animals, adding the revenue to the currency system.

        Args:
            animal (str): The type of animal to sell.
            quantity (int): The number of animals to sell.
            currency_system (MonetarySystem): The currency system to add to.

        Raises:
            ValueError: If the animal type is not recognized or there are insufficient animals to sell.
        """
        if animal not in self.inventory or self.inventory[animal] < quantity:
            raise ValueError(f"Insufficient '{animal}' in inventory to sell.")

        total_revenue = self.ANIMAL_PRICES[animal] * quantity
        currency_system.add_currency(gold=total_revenue)
        self.inventory[animal] -= quantity

        if self.inventory[animal] == 0:
            del self.inventory[animal]

        print(f"Sold {quantity} {animal}(s) for {total_revenue} gold pieces.")

    def get_inventory(self) -> Dict[str, int]:
        """Returns the current inventory of animals."""
        return self.inventory

    def get_animal_price(self, animal: str) -> float:
        """Returns the price of a specific animal in gold pieces."""
        return self.ANIMAL_PRICES.get(animal, 0)

    def __repr__(self) -> str:
        """Returns a string representation of the current animal inventory."""
        return f"Animal Inventory: {self.inventory}"


# Example Usage
currency_system = MonetarySystem(copper=10000, silver=500, electrum=10, gold=5, platinum=1)
animal_market = AnimalMarket()

animal_market.buy_animal('Cow', 2, currency_system)
print(currency_system)
print(animal_market)

animal_market.sell_animal('Cow', 1, currency_system)
print(currency_system)
print(animal_market)
