if __name__ == "__main__":
    # Proficiency Example
    fighter_proficiency = WeaponProficiency('Fighter')
    print(fighter_proficiency)
    print(fighter_proficiency.get_proficiency_info())

    # Weapon Example
    battle_axe = Weapon('Axe, battle')
    print(battle_axe)
    print(battle_axe.get_weapon_info())

    # Multiple Weapons Example
    modifiers = MultipleWeapons.calculate_modifiers(weapon_length=23, dexterity=17)
    print(f"Primary Weapon Penalty: {modifiers['primary_penalty']}, Secondary Weapon Penalty: {modifiers['secondary_penalty']}")

    # Ranged Weapon Example
    short_bow = RangedWeapon('Bow, short', short_range=50, medium_range=100, long_range=150, rate_of_fire=2)
    print(short_bow)
    print(short_bow.get_ranged_info())
