from typing import Dict, Optional, Union, Tuple

class MiscellaneousItem:
    """
    Represents a miscellaneous item with a specific price, weight, and any special notes.
    """

    MISCELLANEOUS_ITEM_CATALOG = {
        'Acid, flask': {'price': '10 g.p.', 'weight': 2, 'notes': 'Causes 1d6 h.p. of damage if it hits. Container must fail a saving throw vs. crushing blow.'},
        'Backpack, leather': {'price': '2 g.p.', 'weight': 2},
        'Belladonna': {'price': '4 s.p.', 'weight': None},
        'Belt pouch, large': {'price': '1 g.p.', 'weight': 1},
        'Belt pouch, small': {'price': '15 s.p.', 'weight': 0.5},
        'Birdcage': {'price': '5 s.p.', 'weight': 5},
        'Bit, bridle, harness (for horse, etc.)': {'price': '1 g.p.', 'weight': 5},
        'Box, iron, large': {'price': '28 g.p.', 'weight': (100, 500)},
        'Box, iron, small': {'price': '9 g.p.', 'weight': (20, 50)},
        'Box, lead, small': {'price': '20 g.p.', 'weight': 2},
        'Candle': {'price': '1 s.p.', 'weight': 0.5},
        'Case, bone (for maps, scrolls, etc.)': {'price': '5 g.p.', 'weight': 5},
        'Case, leather (for maps, scrolls, etc.)': {'price': '15 s.p.', 'weight': 2},
        'Chest, wood, large': {'price': '17 s.p.', 'weight': (50, 150)},
        'Chest, wood, small': {'price': '8 s.p.', 'weight': (10, 25)},
        'Crampons (pair)': {'price': '4 g.p.', 'weight': 5, 'notes': 'Allows walking on ice or slippery surfaces without falling.'},
        'Drill, iron': {'price': '5 g.p.', 'weight': 5, 'notes': 'Bores through stone or wood. Makes a loud grinding noise heard up to 120 feet.'},
        'Garlic': {'price': '5 c.p.', 'weight': None},
        'Grappling hook': {'price': '5 g.p.', 'weight': 10, 'notes': 'Used to attach a rope to distant surfaces.'},
        'Holy symbol, iron': {'price': '2 g.p.', 'weight': 0.2},
        'Holy symbol, silver': {'price': '50 g.p.', 'weight': 0.2},
        'Holy symbol, wooden': {'price': '7 s.p.', 'weight': 0.1},
        'Holy water, vial': {'price': '25 g.p.', 'weight': 2},
        'Lantern, bullseye': {'price': '12 g.p.', 'weight': 6},
        'Lantern, hooded': {'price': '7 g.p.', 'weight': 6},
        'Marotte': {'price': '4 g.p.', 'weight': 0.5, 'notes': 'A jester’s stick with a doll-like head.'},
        'Mirror, metal, large': {'price': '10 g.p.', 'weight': 0.5},
        'Mirror, silver, small': {'price': '20 g.p.', 'weight': 0.5},
        'Oil, flask': {'price': '1 g.p.', 'weight': 2, 'notes': 'Causes 2d6 h.p. of damage if set alight, 1d6 on the following round.'},
        'Pickaxe': {'price': '20 g.p.', 'weight': 20},
        'Pole, 10’': {'price': '3 c.p.', 'weight': 10},
        'Pulley': {'price': '25 g.p.', 'weight': 6},
        'Quiver, arrow, 1 dozen': {'price': '8 s.p.', 'weight': 3},
        'Quiver, arrow, 1 score': {'price': '12 s.p.', 'weight': 3},
        'Quiver, crossbow bolt, 20': {'price': '15 s.p.', 'weight': 3},
        'Quiver, crossbow bolt, 40': {'price': '1 g.p.', 'weight': 3},
        'Rope, 50’': {'price': '4 s.p.', 'weight': 7},
        'Sack, large': {'price': '16 c.p.', 'weight': 2},
        'Sack, small': {'price': '10 c.p.', 'weight': 0.5},
        'Saddle': {'price': '10 g.p.', 'weight': 35},
        'Saddle bags': {'price': '4 g.p.', 'weight': 15},
        'Saddle blanket': {'price': '3 s.p.', 'weight': 2},
        'Shovel': {'price': '10 g.p.', 'weight': 18},
        'Skin (holds 1 gallon water or wine)': {'price': '15 s.p.', 'weight': 0.5, 'notes': 'Weight is 9 lbs when full.'},
        'Spike, iron': {'price': '1 c.p.', 'weight': 1},
        'Tinder box, flint and steel': {'price': '1 g.p.', 'weight': 0.2},
        'Tool, hand (shovel, pick, etc.)': {'price': '2 g.p.', 'weight': 5},
        'Tools, alchemy': {'price': '200 - 1,000 g.p.', 'weight': '10 / g.p. cost'},
        'Tools, armor-making/blacksmithing/weapon-making': {'price': '310 - 400 g.p.', 'weight': '10 / g.p. cost'},
        'Tools, lock-picks': {'price': '30 g.p.', 'weight': 2},
        'Torch': {'price': '1 c.p.', 'weight': 2},
        'Vial, empty': {'price': '3 g.p.', 'weight': 2},
        'Whistle': {'price': '1 s.p.', 'weight': 0.1, 'notes': 'Can be heard up to 1,000 feet away.'},
        'Wolvesbane': {'price': '10 s.p.', 'weight': None},
    }

    def __init__(self, name: str):
        if name not in self.MISCELLANEOUS_ITEM_CATALOG:
            raise ValueError(f"Miscellaneous item '{name}' is not recognized.")
        self.name: str = name
        self.price: str = self.MISCELLANEOUS_ITEM_CATALOG[name]['price']
        self.weight: Optional[Union[float, Tuple[int, int]]] = self.MISCELLANEOUS_ITEM_CATALOG[name].get('weight')
        self.notes: Optional[str] = self.MISCELLANEOUS_ITEM_CATALOG[name].get('notes')

    def get_item_info(self) -> Dict[str, Union[str, Optional[float]]]:
        """
        Returns the details of the miscellaneous item.
        """
        return {
            'name': self.name,
            'price': self.price,
            'weight': self.weight,
            'notes': self.notes,
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the miscellaneous item.
        """
        return f"MiscellaneousItem(Name: {self.name}, Price: {self.price}, Weight: {self.weight}, Notes: {self.notes})"


# Example Usage
if __name__ == "__main__":
    # Create a miscellaneous item (e.g., 'Grappling hook')
    grappling_hook = MiscellaneousItem('Grappling hook')

    # Display item details
    item_info = grappling_hook.get_item_info()
    print(f"Item Info: {item_info}")

    # Represent the miscellaneous item
    print(grappling_hook)
