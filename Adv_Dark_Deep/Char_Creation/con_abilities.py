from collections import namedtuple

constitution = namedtuple("Con", ["HP_Bonus", "Fighter_HP_Bonus", "Reroll_HD", "System_Shock", "Resurrection"])
con_1 = constitution(-4, 0, "5, 6, 7, 8, 9, 10", 25, 30)
con_2 = constitution(-3, 0, "6, 7, 8, 9, 10", 30, 35)
con_3 = constitution(-2, 0, "", 35, 40)
con_4 = constitution(-1, 0, "", 40, 45)
con_5 = constitution(-1, 0, "", 45, 50)
con_6 = constitution(-1, 0, "", 50, 55)
con_7 = constitution(0, 0, "", 55, 60)
con_8 = constitution(0, 0, "", 60, 65)
con_9 = constitution(0, 0, "", 65, 70)
con_10 = constitution(0, 0, "", 70, 75)
con_11 = constitution(0, 0, "", 75, 80)
con_12 = constitution(0, 0, "", 80, 85)
con_13 = constitution(0, 0, "", 85, 90)
con_14 = constitution(0, 0, "", 88, 92)
con_15 = constitution(1, 1, "", 91, 94)
con_16 = constitution(2, 2, "", 95, 96)
con_17 = constitution(2, 3, "", 97, 98)
con_18 = constitution(2, 4, "", 99, 100)
con_19_20 = constitution(2, 5, "1", 99, 100)
con_21_22 = constitution(2, 6, "1, 2", 99, 100)
con_23 = constitution(2, 6, "1, 2, 3", 99, 100)
con_24_25 = constitution(2, 7, "1, 2, 3", 99, 100)

con_abilities = (None, con_1, con_2, con_3, con_4, con_5, con_6, con_7, con_8, con_9, con_10, con_11, con_12, con_13,
                 con_14, con_15, con_16, con_17, con_18, con_19_20, con_21_22, con_23, con_24_25)


def get_con_ability(con_val, ability):
    """Get the appropriate ability for a given constitution value"""
    ability_val = 0
    try:
        if con_val == 19 or con_val == 20:
            ability_val = con_19_20[ability]
        elif con_val == 21 or con_val == 22:
            ability_val = con_21_22[ability]
        elif con_val == 24 or con_val == 25:
            ability_val = con_24_25[ability]
        else:
            ability_val = con_abilities[con_val][ability]
        return ability_val
    except IndexError:
        print(ability_val, con_val, ability)
