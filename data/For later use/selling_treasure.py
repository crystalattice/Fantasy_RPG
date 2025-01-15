from typing import Literal

def calculate_sale_price(treasure_type: Literal["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII"],
                         charisma: int,
                         buyer_history: bool = False,
                         stolen: bool = False,
                         use_fence: bool = False) -> float:
    """
    Calculate the sale price of a treasure item based on its type, the charisma of the seller,
    and other factors such as buyer history and whether the item was stolen.

    :param treasure_type: The type of treasure being sold, as indicated by a Roman numeral (I-XVIII).
    :param charisma: The charisma score of the seller (3-19+).
    :param buyer_history: Whether the buyer has a positive history with the seller (default: False).
    :param stolen: Whether the item was stolen and is easily identifiable (default: False).
    :param use_fence: Whether the seller is using a fence to sell stolen goods (default: False).
    :return: The sale price as a percentage of the treasure's value.
    """

    # Table 76: Sale of Treasure Items (Treasure Method I)
    sale_percentages = {
        "I": [35, 40, 45, 50, 55, 60, 65, 70],
        "II": [33, 38, 43, 48, 52, 57, 62, 67],
        "III": [33, 38, 43, 48, 52, 57, 62, 67],
        "IV": [32, 36, 41, 45, 50, 54, 59, 63],
        "V": [32, 36, 41, 45, 50, 54, 59, 63],
        "VI": [32, 36, 41, 45, 50, 54, 59, 63],
        "VII": [32, 36, 41, 45, 50, 54, 59, 63],
        "VIII": [32, 36, 41, 45, 50, 54, 59, 63],
        "IX": [26, 30, 34, 38, 41, 45, 49, 53],
        "X": [28, 30, 33, 35, 38, 40, 43, 45],
        "XI": [9, 10, 11, 13, 14, 15, 16, 18],
        "XIII": [55, 60, 65, 70, 75, 80, 85, 95],
        "XIV": [66, 70, 74, 78, 81, 85, 89, 96],
        "XV": [64, 68, 71, 75, 79, 83, 86, 94],
        "XVI": [89, 90, 91, 93, 94, 95, 96, 99],
        "XVII": [53, 58, 63, 68, 73, 78, 83, 93],
        "XVIII": [76, 78, 81, 83, 86, 88, 91, 96],
    }

    # Table 77: Sale of Treasure Items (Treasure Method II)
    sale_percentages_method_ii = {
        "Sundries": [35, 40, 45, 50, 55, 60, 65, 70],
        "Luxuries": [40, 45, 50, 55, 60, 65, 70, 80],
        "Art": [45, 50, 55, 60, 65, 70, 75, 85],
        "Jewelry": [50, 55, 60, 65, 70, 75, 80, 90],
        "Gems": [55, 60, 65, 70, 75, 80, 85, 95],
    }

    # Determine the index for charisma
    charisma_index = min(max(charisma - 3, 0), 7)

    # Get the base sale percentage
    if treasure_type in sale_percentages:
        sale_percentage = sale_percentages[treasure_type][charisma_index]
    else:
        raise ValueError("Invalid treasure type provided.")

    # Apply buyer history bonus
    if buyer_history:
        sale_percentage += 10

    # Apply penalties for stolen goods
    if stolen:
        if use_fence:
            sale_percentage = max(sale_percentage // 2, 10)
        else:
            # 90% chance of being turned over to the authorities if sold to a normal merchant
            return 0.0

    return sale_percentage

# Example usage
treasure_type = "I"
charisma = 15
buyer_history = True
stolen = True
use_fence = True

sale_price = calculate_sale_price(treasure_type, charisma, buyer_history, stolen, use_fence)
print(f"The sale price is {sale_price}% of the treasure's value.")
