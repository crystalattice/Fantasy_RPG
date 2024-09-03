import random
from typing import Dict, List, Tuple, Union

class TreasureGenerator:
    """
    A class to generate treasure based on the ADVENTURES DARK AND DEEP™ Bestiary treasure rules.
    Uses Method II for detailed treasure generation.
    """

    def __init__(self, treasure_value: int, treasure_type: str):
        self.treasure_value = treasure_value
        self.treasure_type = treasure_type.upper()

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
            # Add other treasure types as needed
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
            elif category == "Sundries":
                items, encumbrance = self.generate_sundries(category_value)
                treasure_breakdown[category] = items
                total_encumbrance += encumbrance
            elif category == "Luxuries":
                items, encumbrance = self.generate_luxuries(category_value)
                treasure_breakdown[category] = items
                total_encumbrance += encumbrance
            elif category == "Art":
                items, encumbrance = self.generate_art(category_value)
                treasure_breakdown[category] = items
                total_encumbrance += encumbrance
            elif category == "Jewelry":
                items, encumbrance = self.generate_jewelry(category_value)
                treasure_breakdown[category] = items
                total_encumbrance += encumbrance
            elif category == "Gems":
                items, encumbrance = self.generate_gems(category_value)
                treasure_breakdown[category] = items
                total_encumbrance += encumbrance

        return {"composition": treasure_breakdown, "total_encumbrance": total_encumbrance}

    def generate_coins(self, value: float) -> Tuple[List[Tuple[str, int]], float]:
        """
        Generate coins based on the value.

        :param value: The value to convert into coins.
        :return: A list of tuples containing the coin type and quantity, and the total encumbrance.
        """
        coin_types = [("c.p.", 0.01), ("s.p.", 0.1), ("e.p.", 0.5), ("g.p.", 1), ("p.p.", 5)]
        coins = []
        total_encumbrance = 0

        while value > 0:
            coin_type, coin_value = random.choice(coin_types)
            num_coins = min(int(value / coin_value), random.randint(1, 100))
            if num_coins > 0:
                coins.append((coin_type, num_coins))
                total_encumbrance += num_coins * 0.1
                value -= num_coins * coin_value

        return coins, total_encumbrance

    def generate_sundries(self, value: float) -> Tuple[List[Tuple[str, int]], float]:
        """
        Generate sundries based on the value.

        :param value: The value to convert into sundries.
        :return: A list of tuples containing the sundry type and quantity, and the total encumbrance.
        """
        sundry_table = [
            ("Ale (barrel)", 12, 250),
            ("Candle (score)", 1, 10),
            ("Charcoal (bag)", 2, 10),
            ("Cloth (bolt)", 12, 16),
            ("Cotton (short bale)", 3, 22),
            ("Dye (pint)", 5, 2),
            # Add all other sundries from the table
        ]

        items = []
        total_encumbrance = 0

        while value > 0:
            item, item_value, item_encumbrance = random.choice(sundry_table)
            if item_value <= value:
                items.append((item, 1))
                total_encumbrance += item_encumbrance
                value -= item_value

        return items, total_encumbrance

    def generate_luxuries(self, value: float) -> Tuple[List[Tuple[str, int]], float]:
        """
        Generate luxuries based on the value.

        :param value: The value to convert into luxuries.
        :return: A list of tuples containing the luxury type and quantity, and the total encumbrance.
        """
        luxury_table = [
            ("Alchemical instruments", random.randint(1, 8) * 100, lambda v: v / 4),
            ("Astrolabe", 250, 45),
            ("Bell, bronze", 5, 1),
            ("Bell, silver", 10, 1),
            ("Book, illuminated (large)", 300, 100),
            # Add all other luxuries from the table
        ]

        items = []
        total_encumbrance = 0

        while value > 0:
            item, item_value, enc_func = random.choice(luxury_table)
            if item_value <= value:
                items.append((item, 1))
                total_encumbrance += enc_func(item_value)
                value -= item_value

        return items, total_encumbrance

    def generate_art(self, value: float) -> Tuple[List[Tuple[str, int]], float]:
        """
        Generate art based on the value.

        :param value: The value to convert into art.
        :return: A list of tuples containing the art type and quantity, and the total encumbrance.
        """
        art_table = [
            ("Carving, ivory, large", lambda: random.randint(3, 12) * 20, 15),
            ("Carving, ivory, medium", lambda: random.randint(2, 12) * 20, 10),
            ("Carving, ivory, small", lambda: random.randint(1, 12) * 20, 5),
            # Add all other art from the table
        ]

        items = []
        total_encumbrance = 0

        while value > 0:
            item, value_func, item_encumbrance = random.choice(art_table)
            item_value = value_func()
            if item_value <= value:
                items.append((item, 1))
                total_encumbrance += item_encumbrance
                value -= item_value

        return items, total_encumbrance

    def generate_jewelry(self, value: float) -> Tuple[List[Tuple[str, int]], float]:
        """
        Generate jewelry based on the value.

        :param value: The value to convert into jewelry.
        :return: A list of tuples containing the jewelry type and quantity, and the total encumbrance.
        """
        jewelry_table = [
            ("Ivory, silver", lambda: random.randint(1, 10) * 100),
            ("Silver and gold", lambda: random.randint(2, 12) * 100),
            ("Gold", lambda: random.randint(3, 18) * 100),
            # Add all other jewelry from the table
        ]

        items = []
        total_encumbrance = 0

        while value > 0:
            material_func = random.choice(jewelry_table)
            material_value = material_func[1]()
            if material_value <= value:
                items.append((material_func[0], 1))
                total_encumbrance += 1  # Each piece of jewelry is worth 1 lb.
                value -= material_value

        return items, total_encumbrance

    def generate_gems(self, value: float) -> Tuple[List[Tuple[str, int]], float]:
        """
        Generate gems based on the value.

        :param value: The value to convert into gems.
        :return: A list of tuples containing the gem type and quantity, and the total encumbrance.
        """
        gem_type_table = [
            ("Hardstone", 1),
            ("Semi-precious", 5),
            ("Fancy", 10),
            ("Precious", 50),
            ("Gemstone", 100),
            ("Jewel", 500)
        ]

        gem_size_table = [
            (1, 5), (5, 10), (10, 50), (50, 100), (100, 500), (500, 1000)
        ]

        items = []
        total_encumbrance = 0

        while value > 0:
            gem_type, base_value = random.choice(gem_type_table)
            size_value = random.choice(gem_size_table)[1]
            gem_value = base_value * size_value
            if gem_value <= value:
                items.append((gem_type, 1))
                total_encumbrance += gem_value / 100
                value -= gem_value

        return items, total_encumbrance

# Example Usage:
treasure_value = 1000
treasure_type = "III"
treasure_generator = TreasureGenerator(treasure_value, treasure_type)

# Detailed method (Method II)
detailed_treasure = treasure_generator.method_II()
print(f"Detailed Method Treasure Composition: {detailed_treasure['composition']}")
print(f"Total Encumbrance: {detailed_treasure['total_encumbrance']} lbs")
