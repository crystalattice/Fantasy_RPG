from collections import namedtuple
from typing import Type

dexterity: Type[namedtuple] = namedtuple("Dex", ["Init_Adj", "Missile_Attack", "AC_Adj"])
dex_1 = dexterity(5, -5, 6)
dex_2 = dexterity(4, -4, 5)
dex_3 = dexterity(3, -3, 4)
dex_4 = dexterity(2, -2, 3)
dex_5 = dexterity(1, -1, 2)
dex_6 = dexterity(0, 0, 1)
dex_7_14 = dexterity(0, 0, 0)
dex_15 = dexterity(0, 0, -1)
dex_16 = dexterity(-1, 1, -2)
dex_17 = dexterity(-2, 2, -3)
dex_18_20 = dexterity(-3, 3, -4)
dex_21_23 = dexterity(-4, 4, -5)
dex_24_25 = dexterity(-5, 5, -6)

# Offset tuple so values match possible attribute scores
dex_abilities = (None, dex_1, dex_2, dex_3, dex_4, dex_5, dex_6, dex_7_14, dex_15, dex_16, dex_17, dex_18_20,
                 dex_21_23, dex_24_25)


def get_dex_ability(dex_value: int, ability: int) -> int:
    """Get the appropriate ability for a given dexterity value.

    Values 15-17 are explicitly listed because, for some reason, the code could not figure out how to get a value from
    them, even though the other ability functions had no problem.
    """
    ability_val = 0
    try:
        if 7 <= dex_value <= 14:
            ability_val = dex_7_14[ability]
        elif dex_value == 15:
            ability_val = dex_15[ability]
        elif dex_value == 16:
            ability_val = dex_16[ability]
        elif dex_value == 17:
            ability_val = dex_17[ability]
        elif 18 <= dex_value <= 20:
            ability_val = dex_18_20[ability]
        elif 21 <= dex_value <= 23:
            ability_val = dex_21_23[ability]
        elif dex_value == 24 or dex_value == 25:
            ability_val = dex_24_25[ability]
        else:
            ability_val = dex_abilities[dex_value][ability]
        return ability_val
    except IndexError:
        print(ability_val, dex_value, ability)
