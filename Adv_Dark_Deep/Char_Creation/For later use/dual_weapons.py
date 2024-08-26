class MultipleWeapons:
    """Handles the penalties and modifiers for using multiple weapons in combat."""

    MULTIPLE_WEAPON_MODIFIERS = {
        'dexterity_16': {'primary_penalty': -1, 'secondary_penalty': -3},
        'dexterity_17': {'primary_penalty': 0, 'secondary_penalty': -2},
        'dexterity_18': {'primary_penalty': 0, 'secondary_penalty': -1},
        'dexterity_19': {'primary_penalty': 0, 'secondary_penalty': 0},
    }

    @staticmethod
    def calculate_modifiers(weapon_length: int, dexterity: int) -> Dict[str, int]:
        """Calculates the 'to hit' penalties for using two weapons based on weapon length and dexterity."""
        if dexterity < 16:
            return {'primary_penalty': -6, 'secondary_penalty': -10}
        elif dexterity > 19:
            return {'primary_penalty': 0, 'secondary_penalty': 0}

        dexterity_key = f'dexterity_{dexterity}'
        if weapon_length >= 24:
            primary_penalty = MultipleWeapons.MULTIPLE_WEAPON_MODIFIERS[dexterity_key]['primary_penalty'] - 6
            secondary_penalty = MultipleWeapons.MULTIPLE_WEAPON_MODIFIERS[dexterity_key]['secondary_penalty'] - 6
        else:
            primary_penalty = MultipleWeapons.MULTIPLE_WEAPON_MODIFIERS[dexterity_key]['primary_penalty'] - 2
            secondary_penalty = MultipleWeapons.MULTIPLE_WEAPON_MODIFIERS[dexterity_key]['secondary_penalty'] - 2

        return {'primary_penalty': primary_penalty, 'secondary_penalty': secondary_penalty}

    def __repr__(self) -> str:
        return f"MultipleWeapons() - Handles multiple weapon penalties."


if __name__ == "__main__":
    # Example Usage
    modifiers = MultipleWeapons.calculate_modifiers(weapon_length=23, dexterity=17)
    print(
        f"Primary Weapon Penalty: {modifiers['primary_penalty']}, Secondary Weapon Penalty: {modifiers['secondary_penalty']}")
