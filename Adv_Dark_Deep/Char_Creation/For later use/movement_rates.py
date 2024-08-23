from typing import Dict, Optional


class Movement:
    """
    Handles both indoor and outdoor movement calculations based on burden, terrain, and environment.
    """

    # Base indoor movement rates (in feet per minute)
    INDOOR_MOVEMENT_RATES = {
        "man_sized": {"walking": 360, "running": 720, "moving_silently": 120},
        "small_sized": {"walking": 270, "running": 540, "moving_silently": 90}
    }

    # Base outdoor movement rates (in miles per day)
    OUTDOOR_MOVEMENT_RATES = {
        "light_burden": {"normal": 30, "rugged": 20, "very_rugged": 10},
        "medium_burden": {"normal": 20, "rugged": 10, "very_rugged": 5},
        "heavy_burden": {"normal": 10, "rugged": 5, "very_rugged": 2},
        "light_horse": {"normal": 60, "rugged": 25, "very_rugged": 5},
        "medium_horse": {"normal": 40, "rugged": 20, "very_rugged": 5},
        "heavy_horse": {"normal": 30, "rugged": 15, "very_rugged": 5},
        "draft_horse": {"normal": 30, "rugged": 15, "very_rugged": 5},
        "chariot": {"normal": 30, "rugged": 20, "very_rugged": 0},
        "cart": {"normal": 25, "rugged": 15, "very_rugged": 0},
        "wagon": {"normal": 25, "rugged": 10, "very_rugged": 0}
    }

    def __init__(self, size: Optional[str] = None, movement_type: Optional[str] = None,
                 burden: Optional[str] = None, terrain: Optional[str] = None):
        self.size: Optional[str] = size
        self.movement_type: Optional[str] = movement_type
        self.burden: Optional[str] = burden
        self.terrain: Optional[str] = terrain

    def calculate_indoor_movement(self) -> int:
        """
        Calculates indoor movement speed based on character size and movement type.
        """
        if self.size not in self.INDOOR_MOVEMENT_RATES:
            raise ValueError(f"Invalid size: {self.size}")

        if self.movement_type not in self.INDOOR_MOVEMENT_RATES[self.size]:
            raise ValueError(f"Invalid movement type: {self.movement_type}")

        return self.INDOOR_MOVEMENT_RATES[self.size][self.movement_type]

    def calculate_outdoor_movement(self) -> int:
        """
        Calculates overland travel distance per day based on burden and terrain.
        """
        if self.burden not in self.OUTDOOR_MOVEMENT_RATES:
            raise ValueError(f"Invalid burden type: {self.burden}")

        if self.terrain not in self.OUTDOOR_MOVEMENT_RATES[self.burden]:
            raise ValueError(f"Invalid terrain type: {self.terrain}")

        return self.OUTDOOR_MOVEMENT_RATES[self.burden][self.terrain]

    def __repr__(self) -> str:
        indoor_movement = f"Indoor Movement: {self.calculate_indoor_movement()} ft/min" if self.size and self.movement_type else ""
        outdoor_movement = f"Outdoor Movement: {self.calculate_outdoor_movement()} miles/day" if self.burden and self.terrain else ""
        return f"Movement({indoor_movement}, {outdoor_movement})"


# Example Usage
if __name__ == "__main__":
    # Example with indoor movement for a man-sized character walking
    indoor_movement = Movement(size="man_sized", movement_type="walking")
    print(indoor_movement)

    # Example with outdoor movement for a light burden in rugged terrain
    outdoor_movement = Movement(burden="light_burden", terrain="rugged")
    print(outdoor_movement)

    # Example combining indoor and outdoor movement
    combined_movement = Movement(size="small_sized", movement_type="moving_silently", burden="medium_horse",
                                 terrain="normal")
    print(combined_movement)
