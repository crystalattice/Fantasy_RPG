from collections import namedtuple
from typing import Type

strength: Type[namedtuple] = namedtuple("Strength",
                                        ["ToHit_Modifier", "Damage_Modifier", "Weight_Allowance", "Open_Stuck_Doors",
                                         "Open_Locked_Doors", "Bend_Bars_Lift_Gates"])
str_1 = strength(-5, -2, -55, 0, 0, 0)
str_2 = strength(-4, -2, -45, 0, 0, 0)
str_3 = strength(-3, -1, -35, 0.17, 0, 0)
str_4 = strength(-2, -1, -25, 0.17, 0, 0)
str_5 = strength(-2, -1, -25, 0.17, 0, 0)
str_6 = strength(-1, 0, -15, 0.17, 0, 0)
str_7 = strength(-1, 0, -15, 0.17, 0, 0)
str_8 = strength(0, 0, 0, 0.33, 0, 1)
str_9 = strength(0, 0, 0, 0.33, 0, 1)
str_10 = strength(0, 0, 0, 0.33, 0, 2)
str_11 = strength(0, 0, 0, 0.33, 0, 2)
str_12 = strength(0, 0, 10, 0.33, 0, 4)
str_13 = strength(0, 0, 10, 0.33, 0, 4)
str_14 = strength(0, 0, 20, 0.33, 0, 7)
str_15 = strength(0, 0, 20, 0.33, 0, 7)
str_16 = strength(0, 1, 35, 0.5, 0, 10)
str_17 = strength(1, 1, 50, 0.5, 0, 13)
str_18 = strength(1, 2, 75, 0.5, 0, 16)
str_181_1850 = strength(1, 3, 100, 0.5, 0, 20)
str_1851_1875 = strength(2, 3, 125, 0.67, 0, 25)
str_1876_1890 = strength(2, 4, 150, 0.67, 0, 30)
str_1891_1899 = strength(2, 5, 200, 0.67, 0.17, 35)
str_18100 = strength(3, 6, 300, 0.83, 0.33, 40)
str_19 = strength(3, 7, 450, 0.875, 0.5, 50)
str_20 = strength(3, 8, 500, 0.875, 0.5, 60)
str_21 = strength(4, 9, 600, 0.9, 0.67, 70)
str_22 = strength(4, 10, 750, 0.9, 0.67, 80)
str_23 = strength(5, 11, 900, 0.917, 0.83, 90)
str_24 = strength(6, 12, 1200, 0.917, 0.875, 100)
str_25 = strength(7, 14, 1500, 0.958, 0.9, 100)

# Offset tuple so values match possible attribute scores
str_abilities = (None, str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8, str_9, str_10, str_11, str_12, str_13,
                 str_14, str_15, str_16, str_17, str_18, str_19, str_20, str_21, str_22, str_23, str_24, str_25,
                 str_181_1850, str_1851_1875, str_1876_1890, str_1891_1899, str_18100,)


def get_str_ability(str_val: int, ability: int) -> int:
    """Get the appropriate ability for a given strength value"""
    try:
        if 181 <= str_val <= 1850:
            ability_val = str_181_1850[ability]
        elif 1851 <= str_val <= 1875:
            ability_val = str_1851_1875[ability]
        elif 1876 <= str_val <= 1890:
            ability_val = str_1876_1890[ability]
        elif 1891 <= str_val <= 1899:
            ability_val = str_1891_1899[ability]
        elif str_val == 18100:
            ability_val = str_18100[ability]
        else:
            ability_val = str_abilities[str_val][ability]
        return ability_val
    except IndexError:
        print(str_val, ability)
