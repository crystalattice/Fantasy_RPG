from typing import Dict, Optional


class Service:
    """
    Represents a service that can be hired or utilized in the game, including its price,
    duration, and any special conditions or notes.
    """

    SERVICE_CATALOG = {
        'Apartment': {
            'price': 10, 'unit': 'g.p./month',
            'notes': 'Per room, for characters inclined to settle without buying or building a home.'
        },
        'Appraisal': {
            'price': 5, 'unit': 'g.p./item', 'notes': 'For gem or jewelry appraisal.'
        },
        'Coach (between cities)': {
            'price': 1, 'unit': 'g.p./30 miles',
            'notes': 'Availability depends on the regularity of coach transportation in the setting.'
        },
        'Coach (within a city)': {
            'price': 1, 'unit': 's.p./trip', 'notes': 'Short trips within a city.'
        },
        'Crier': {
            'price': 10, 'unit': 's.p./day', 'monthly': 10, 'unit_monthly': 'g.p./month',
            'notes': 'Used to disseminate information in a town or city.'
        },
        'Inn (common room)': {
            'price': 2, 'unit': 's.p./night', 'range': (2, 8), 'notes': 'Shared room with up to 30 people.'
        },
        'Inn (private room)': {
            'price': 1, 'unit': 'g.p./night', 'notes': 'A private and usually secure room.'
        },
        'Messenger': {
            'price': 3, 'unit': 's.p./day', 'monthly': 50, 'unit_monthly': 's.p./month',
            'notes': 'Within a particular city or town.'
        },
    }

    def __init__(self, name: str):
        if name not in self.SERVICE_CATALOG:
            raise ValueError(f"Service '{name}' is not recognized.")
        self.name: str = name
        self.price: int = self.SERVICE_CATALOG[name]['price']
        self.unit: str = self.SERVICE_CATALOG[name]['unit']
        self.notes: str = self.SERVICE_CATALOG[name].get('notes', '')
        self.range: Optional[tuple] = self.SERVICE_CATALOG[name].get('range', None)
        self.monthly: Optional[int] = self.SERVICE_CATALOG[name].get('monthly', None)
        self.unit_monthly: Optional[str] = self.SERVICE_CATALOG[name].get('unit_monthly', None)

    def calculate_cost(self, duration: Optional[int] = 1, distance: Optional[int] = 0) -> Dict[str, str]:
        """
        Calculates the cost of the service based on duration or distance (if applicable).
        """
        if self.range:
            final_price = random.randint(*self.range)
        elif 'mile' in self.unit:
            final_price = self.price * (distance // 30)
        else:
            final_price = self.price * duration

        if self.monthly and duration > 30:
            final_price = (duration // 30) * self.monthly

        return {
            'service': self.name,
            'total_cost': f"{final_price} {self.unit if duration <= 30 else self.unit_monthly}",
            'notes': self.notes
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the service.
        """
        return (f"Service(Name: {self.name}, Price: {self.price} {self.unit}, Notes: {self.notes})")


# Example Usage
if __name__ == "__main__":
    # Create a service (e.g., 'Inn (private room)')
    service = Service('Inn (private room)')

    # Simulate booking the service for 3 nights
    result = service.calculate_cost(duration=3)

    # Display the result of the service cost
    print(f"Service Cost: {result}")

    # Represent the service
    print(service)
