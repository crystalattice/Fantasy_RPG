import random
from typing import Dict, List, Tuple, Union

class TreasureGenerator:
    """
    A class to generate treasure based on the ADVENTURES DARK AND DEEP™ Bestiary treasure rules.
    Includes both a quick method (Method I) and a detailed method (Method II).
    """

    def __init__(self, treasure_value: int, treasure_type: str):
        self.treasure_value = treasure_value
        self.treasure_type = treasure_type.upper()

    def method_I(self) -> float:
        """
        Quick method to calculate treasure encumbrance based on treasure type and value.

        :return: Total encumbrance of the treasure in pounds.
        """
        encumbrance_factors = {
            "I": 30, "II": 25, "III": 22, "IV": 20, "V": 15,
            "VI": 7, "VII": 20, "VIII": 30, "IX": 40, "X": 50,
            "XI": 1/3, "XII": 1/10, "XIII": 1/100, "XIV": 1/3,
            "XV": 1/3, "XVI": 0.75, "XVII": 1/30, "XVIII": 2
        }

        encumbrance_factor = encumbrance_factors.get(self.treasure_type, 0)
        return self.treasure_value * encumbrance_factor

    def method_II(self) -> Dict[str, Union[float, List[Tuple[str, int]]]]:
        """
        Detailed method to calculate treasure composition and encumbrance based on treasure type.

        :return: A dictionary containing the detailed composition of the treasure and total encumbrance.
        """
        # Treasure composition percentages based on treasure type
        composition_table = {
            "I": {"Sundries": 100},
            "II": {"Sundries": 75, "Luxuries": 15, "Jewelry": 5, "Coins": 5},
            "III": {"Sundries": 50, "Luxuries": 25, "Art": 5, "Jewelry": 10, "Gems": 5, "Coins": 5},
            "IV": {"Sundries": 25, "Luxuries": 35, "Art": 10, "Jewelry": 15, "Gems": 5, "Coins": 10},
            # ... include other types as needed
        }

        treasure_composition = composition_table.get(self.treasure_type, {})
        treasure_breakdown = {}
        total_encumbrance = 0

        for category, percentage in treasure_composition.items():
            category_value = self.treasure_value * (percentage / 100)
            if category == "Coins":
                coins, encumbrance = self.generate_coins(category_value)
                treasure_breakdown[category] = coins
                total_encumbrance += encumbrance
            else:
                encumbrance = self.generate_sundries_or_luxuries(category_value)
                treasure_breakdown[category] = encumbrance[0]
                total_encumbrance += encumbrance[1]

        return {"composition": treasure_breakdown, "total_encumbrance": total_encumbrance}

    def generate_coins(self, value: float) -> Tuple[List[Tuple[str, int]], float]:
        """
        Generate coins based on the value.

        :param value: The value to convert into coins.
        :return: A list of tuples containing the coin type and quantity, and the total encumbrance.
        """
        coin_types = [("c.p.", 10), ("s.p.", 100), ("e.p.", 200), ("g.p.", 500), ("p.p.", 1000)]
        coins = []
        total_encumbrance = 0

        while value > 0:
            coin_type, coin_value = random.choice(coin_types)
            num_coins = min(int(value / coin_value), random.randint(1, 100))
            coins.append((coin_type, num_coins))
            total_encumbrance += num_coins * 0.1
            value -= num_coins * coin_value

        return coins, total_encumbrance

    def generate_sundries_or_luxuries(self, value: float) -> Tuple[str, float]:
        """
        Generate sundries or luxuries based on the value.

        :param value: The value to convert into sundries or luxuries.
        :return: A description and the total encumbrance.
        """
        # Here you can create more specific generators for each category
        items = ["bolt of cloth", "barrel of ale", "fur pelt", "golden necklace", "silver cup"]
        item = random.choice(items)
        encumbrance = value / random.uniform(10, 100)  # Simplified encumbrance calculation

        return item, encumbrance


# Example Usage:
treasure_value = 1000
treasure_type = "III"
treasure_generator = TreasureGenerator(treasure_value, treasure_type)

# Quick method (Method I)
quick_encumbrance = treasure_generator.method_I()
print(f"Quick Method Encumbrance: {quick_encumbrance} lbs")

# Detailed method (Method II)
detailed_treasure = treasure_generator.method_II()
print(f"Detailed Method Treasure Composition: {detailed_treasure['composition']}")
print(f"Total Encumbrance: {detailed_treasure['total_encumbrance']} lbs")
