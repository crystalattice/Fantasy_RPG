from collections import namedtuple
from typing import Type

char_abilities: Type[namedtuple] = namedtuple("Char", ["Max_Henchmen", "Morale_Adj", "React_Adj"])
char_1 = char_abilities(0, -8, -35)
char_2 = char_abilities(0, -7, -30)
char_3 = char_abilities(1, -6, -25)
char_4 = char_abilities(1, -5, -20)
char_5 = char_abilities(2, -4, -15)
char_6 = char_abilities(2, -3, -10)
char_7 = char_abilities(3, -2, -5)
char_8 = char_abilities(3, -1, 0)
char_9_11 = char_abilities(4, 0, 0)
char_12 = char_abilities(5, 0, 0)
char_13 = char_abilities(5, 0, 5)
char_14 = char_abilities(6, 1, 10)
char_15 = char_abilities(7, 3, 15)
char_16 = char_abilities(8, 4, 25)
char_17 = char_abilities(10, 6, 30)
char_18 = char_abilities(15, 8, 35)
char_19 = char_abilities(20, 10, 40)
char_20 = char_abilities(25, 12, 45)
char_21 = char_abilities(30, 14, 50)
char_22 = char_abilities(35, 16, 55)
char_23 = char_abilities(40, 18, 60)
char_24 = char_abilities(45, 20, 65)
char_25 = char_abilities(50, 20, 70)

# Offset tuple so values match possible attribute scores
char_abilities = (None, char_1, char_2, char_3, char_4, char_5, char_6, char_7, char_8, char_9_11, char_12, char_13,
                  char_14, char_15, char_16, char_17, char_18, char_19, char_20, char_21, char_22, char_23, char_24,
                  char_25)


def get_char_ability(char_val: int, ability: int) -> int:
    """Get the appropriate ability for a given charisma value"""
    ability_val = 0
    try:
        if char_val < 9:
            ability_val = char_abilities[char_val][ability]
        elif 9 <= char_val <= 11:
            ability_val = char_9_11[ability]
        else:
            ability_val = char_abilities[char_val - 2][ability]
        return ability_val
    except IndexError:
        print(ability_val, char_val, ability)
