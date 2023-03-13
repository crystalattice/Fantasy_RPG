from collections import namedtuple

dex = namedtuple("Dex", ["Init_Bonus", "Missile_Bonus", "AC_Bonus"])

dex_1 = dex(5, -5, 6)
dex_2 = dex(4, -4, 5)
dex_3 = dex(3, -3, 4)
dex_4 = dex(2, -2, 3)
dex_5 = dex(1, -1, 2)
dex_6 = dex(0, 0, 1)
dex_7_14 = dex(0, 0, 0)
dex_15 = dex(0, 0, -1)
dex_16 = dex(-1, 1, -2)
dex_17 = dex(-2, 2, -3)
dex_18_20 = dex(-3, 3, -4)
dex_21_23 = dex(-4, 4, -5)
dex_24_25 = dex(-5, 5, -6)

dex_abilities = (None, dex_1, dex_2, dex_3, dex_4, dex_5, dex_6, dex_7_14, dex_15, dex_16, dex_17, dex_18_20, dex_21_23,
                 dex_24_25)


def get_dex_ability(dex_val, ability):
    """Get the appropriate ability for a given dexterity value"""
    ability_val = 0
    try:
        if 7 < dex_val <= 14:
            ability_val = dex_7_14[ability]
        elif 18 < dex_val <= 20:
            ability_val = dex_18_20[ability]
        elif 21 < dex_val <= 23:
            ability_val = dex_21_23[ability]
        elif dex_val == 24 or dex_val == 25:
            ability_val = dex_24_25[ability]
        else:
            ability_val = dex_abilities[dex_val][ability]
        return ability_val
    except IndexError:
        print(ability_val, dex_val, ability)