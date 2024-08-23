from typing import Optional, Dict


class Transportation:
    """
    Represents a transportation option that can be bought or hired, including its price,
    and additional notes regarding its usage.
    """

    TRANSPORTATION_CATALOG = {
        'Boat, long': {
            'price': 150, 'unit': 'g.p.', 'notes': 'Long boat suitable for river or lake travel.'
        },
        'Boat, small': {
            'price': 75, 'unit': 'g.p.', 'notes': 'Small boat, suitable for short trips.'
        },
        'Canoe, large': {
            'price': 300, 'unit': 'g.p.', 'notes': 'Holds 9 normal characters or 6 with heavy gear. Weighs 160 lbs.'
        },
        'Canoe, small': {
            'price': 100, 'unit': 'g.p.', 'notes': 'Holds 3 normal characters or 2 with heavy gear. Weighs 80 lbs.'
        },
        'Canvas': {
            'price': 10, 'unit': 'g.p.', 'notes': 'Repairs 1 hit point of damage on a ship. Encumbrance: 20 lbs.'
        },
        'Caravan travel': {
            'price': 10, 'unit': 'c.p./mile', 'notes': 'Cost varies depending on frequency and danger of the route.'
        },
        'Cart': {
            'price': 50, 'unit': 'g.p.', 'notes': 'Basic cart, requires an animal to pull.'
        },
        'Chariot, 1-man': {
            'price': 200, 'unit': 'g.p.', 'notes': '1-man chariot, cannot travel through close or rough terrain.'
        },
        'Chariot, 2-man': {
            'price': 500, 'unit': 'g.p.', 'notes': '2-man chariot, allows missile weapon firing with -2 penalty.'
        },
        'Lumber': {
            'price': 10, 'unit': 'g.p.', 'notes': 'Repairs 1 hit point of damage on a ship. Encumbrance: 20 lbs.'
        },
        'Raft, small': {
            'price': 50, 'unit': 'g.p.', 'notes': 'Small raft, suitable for short river crossings.'
        },
        'River ferry': {
            'price': 5, 'unit': 's.p.', 'notes': 'Cost for crossing a river by ferry.'
        },
        'River/lake voyage': {
            'price': 1, 'unit': 's.p./mile', 'notes': 'Travel cost per mile on a river or lake.'
        },
        'Sea voyage': {
            'price': 5, 'unit': 'c.p./mile', 'notes': 'Cost per mile for sea travel, varies with danger and frequency.'
        },
        'Wagon': {
            'price': 150, 'unit': 'g.p.', 'notes': 'Basic wagon, requires an animal to pull.'
        },
        'Wagon plus drover': {
            'price': 1, 'unit': 's.p./mile', 'notes': 'Wagon with driver, cost per mile.'
        },
    }

    def __init__(self, name: str):
        if name not in self.TRANSPORTATION_CATALOG:
            raise ValueError(f"Transportation option '{name}' is not recognized.")
        self.name: str = name
        self.price: int = self.TRANSPORTATION_CATALOG[name]['price']
        self.unit: str = self.TRANSPORTATION_CATALOG[name]['unit']
        self.notes: str = self.TRANSPORTATION_CATALOG[name].get('notes', '')

    def calculate_cost(self, distance: Optional[int] = 0, quantity: Optional[int] = 1) -> Dict[str, str]:
        """
        Calculates the cost of the transportation based on distance or quantity.
        """
        if 'mile' in self.unit:
            final_price = self.price * distance
        else:
            final_price = self.price * quantity

        return {
            'transportation': self.name,
            'total_cost': f"{final_price} {self.unit}",
            'notes': self.notes
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the transportation option.
        """
        return f"Transportation(Name: {self.name}, Price: {self.price} {self.unit}, Notes: {self.notes})"


# Example Usage
if __name__ == "__main__":
    # Create a transportation option (e.g., 'Wagon plus drover')
    transportation = Transportation('Wagon plus drover')

    # Calculate the cost for traveling 50 miles
    result = transportation.calculate_cost(distance=50)

    # Display the result of the transportation cost
    print(f"Transportation Cost: {result}")

    # Represent the transportation option
    print(transportation)
