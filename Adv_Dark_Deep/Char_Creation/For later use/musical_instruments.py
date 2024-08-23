from typing import Dict, Optional, Union

class MusicalInstrument:
    """
    Represents a musical instrument with a specific price, weight, and any special notes.
    """

    MUSICAL_INSTRUMENT_CATALOG = {
        'Bagpipe': {'price': '60 g.p.', 'weight': 20},
        'Bladder pipe': {'price': '8 g.p.', 'weight': 2},
        'Cornamuse': {'price': '24 g.p.', 'weight': 5},
        'Crumhorn': {'price': '16 g.p.', 'weight': 3},
        'Drum': {'price': '4 g.p.', 'weight': 8},
        'Dulcian': {'price': '19 g.p.', 'weight': 4},
        'Dulcimer': {'price': '20 g.p.', 'weight': 6},
        'Flute': {'price': '5 g.p.', 'weight': 1},
        'Gamba': {'price': '40 g.p.', 'weight': 10, 'notes': 'Played with a bow, and invariably while seated.'},
        'Gemshorn': {'price': '2 g.p.', 'weight': 1},
        'Harp': {'price': '75 g.p.', 'weight': 14},
        'Harpsichord': {'price': '250 g.p.', 'weight': 200, 'notes': 'Too large to be portable.'},
        'Hurdy-gurdy': {'price': '100 g.p.', 'weight': 12},
        'Kortholt': {'price': '8 g.p.', 'weight': 2},
        'Lute': {'price': '25 g.p.', 'weight': 7},
        'Lyre': {'price': '150 g.p.', 'weight': 15},
        'Mandolin': {'price': '28 g.p.', 'weight': 10},
        'Organ': {'price': '300 g.p. and up', 'weight': '300+', 'notes': 'Requires at least two people to play.'},
        'Organetto': {'price': '110 g.p.', 'weight': 10, 'notes': 'A one-man instrument, very portable, usually played while seated.'},
        'Psaltery': {'price': '90 g.p.', 'weight': 11},
        'Racket': {'price': '22 g.p.', 'weight': 2},
        'Rebec': {'price': '30 g.p.', 'weight': 5},
        'Recorder': {'price': '6 g.p.', 'weight': 1},
        'Sacbut': {'price': '30 g.p.', 'weight': 6},
        'Shepherd’s shawm': {'price': '18 g.p.', 'weight': 6},
        'Trumpet': {'price': '6 g.p.', 'weight': 4},
        'Viol': {'price': '30 g.p.', 'weight': 8, 'notes': 'Akin to a small gamba, held between the knees and played while seated.'},
        'Zink': {'price': '15 g.p.', 'weight': 2},
    }

    def __init__(self, name: str):
        if name not in self.MUSICAL_INSTRUMENT_CATALOG:
            raise ValueError(f"Musical instrument '{name}' is not recognized.")
        self.name: str = name
        self.price: str = self.MUSICAL_INSTRUMENT_CATALOG[name]['price']
        self.weight: Optional[Union[float, str]] = self.MUSICAL_INSTRUMENT_CATALOG[name].get('weight')
        self.notes: Optional[str] = self.MUSICAL_INSTRUMENT_CATALOG[name].get('notes')

    def get_instrument_info(self) -> Dict[str, Union[str, Optional[float]]]:
        """
        Returns the details of the musical instrument.
        """
        return {
            'name': self.name,
            'price': self.price,
            'weight': self.weight,
            'notes': self.notes,
        }

    def __repr__(self) -> str:
        """
        Returns a string representation of the musical instrument.
        """
        return f"MusicalInstrument(Name: {self.name}, Price: {self.price}, Weight: {self.weight}, Notes: {self.notes})"


# Example Usage
if __name__ == "__main__":
    # Create a musical instrument (e.g., 'Harp')
    harp = MusicalInstrument('Harp')

    # Display instrument details
    instrument_info = harp.get_instrument_info()
    print(f"Instrument Info: {instrument_info}")

    # Represent the musical instrument
    print(harp)
