class RangedWeapon(Weapon):
    """Represents a ranged weapon with additional attributes like range and rate of fire."""

    def __init__(self, weapon_name: str, short_range: int, medium_range: int, long_range: int, rate_of_fire: int):
        super().__init__(weapon_name)
        self.short_range = short_range
        self.medium_range = medium_range
        self.long_range = long_range
        self.rate_of_fire = rate_of_fire

    def get_ranged_info(self) -> Dict[str, int]:
        """Returns the details of the ranged weapon."""
        return {
            'name': self.name,
            'short_range': self.short_range,
            'medium_range': self.medium_range,
            'long_range': self.long_range,
            'rate_of_fire': self.rate_of_fire,
            'damage_sm': self.damage_sm,
            'damage_l': self.damage_l,
        }

    def __repr__(self) -> str:
        return (f"RangedWeapon({self.name}: Short {self.short_range} yards, "
                f"Medium {self.medium_range} yards, Long {self.long_range} yards)")


if __name__ == "__main__":
    # Example Usage
    short_bow = RangedWeapon('Bow, short', short_range=50, medium_range=100, long_range=150, rate_of_fire=2)
    print(short_bow)
    print(short_bow.get_ranged_info())
