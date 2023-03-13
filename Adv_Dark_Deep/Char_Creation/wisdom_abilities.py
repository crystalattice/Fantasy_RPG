from collections import namedtuple

wisdom_abilities = namedtuple("Wisdom", ["Magical_Attack_Adjustment", "Cleric_Bonus", "Spell_Failure", "Immune_to_Charm"])

wis_1 = wisdom_abilities(-5, "0", 100, 0)
wis_2 = wisdom_abilities(-4, "0", 100, 0)
wis_3 = wisdom_abilities(-3, "0", 100, 0)
wis_4 = wisdom_abilities(-2, "0", 100, 0)
wis_5 = wisdom_abilities(-1, "0", 100, 0)
wis_6 = wisdom_abilities(-1, "0", 100, 0)
wis_7 = wisdom_abilities(-1, "0", 100, 0)
wis_8 = wisdom_abilities(0, "0", 100, 0)
wis_9 = wisdom_abilities(0, "0", 20, 0)
wis_10 = wisdom_abilities(0, "0", 15, 0)
wis_11 = wisdom_abilities(0, "0", 10, 0)
wis_12 = wisdom_abilities(0, "0", 5, 0)
wis_13 = wisdom_abilities(0, "1x1", 0, 0)
wis_14 = wisdom_abilities(0, "2x1", 0, 0)
wis_15 = wisdom_abilities(1, "2x1, 1x2", 0, 0)
wis_16 = wisdom_abilities(2, "2x1, 2x2", 0, 0)
wis_17 = wisdom_abilities(3, "2x1, 2x2, 1x3", 0, 0)
wis_18 = wisdom_abilities(4, "2x1, 2x2, 1x3, 1x4", 0, 0)
wis_19 = wisdom_abilities(4, "3x1, 2x2, 1x3, 2x4", 0, 1)
wis_20 = wisdom_abilities(4, "3x1, 3x2, 1x3, 3x4", 0, 2)
wis_21 = wisdom_abilities(4, "3x1, 3x2, 2x3, 3x4, 1x5", 0, 3)
wis_22 = wisdom_abilities(4, "3x1, 3x2, 2x3, 4x4, 2x5", 0, 4)
wis_23 = wisdom_abilities(4, "3x1, 3x2, 2x3, 4x4, 4x5", 0, 5)
wis_24 = wisdom_abilities(4, "3x1, 3x2, 2x3, 4x4, 4x5, 2x6", 0, 6)
wis_25 = wisdom_abilities(4, "3x1, 3x2, 2x3, 4x4, 4x5, 3x6, 1x7", 0, 7)

wis_abilities = (None, wis_1, wis_2, wis_3, wis_4, wis_5, wis_6, wis_7, wis_8, wis_9, wis_10, wis_11, wis_12, wis_13, wis_14, wis_15,
                 wis_16, wis_17, wis_18, wis_19, wis_20, wis_21, wis_22, wis_23, wis_24, wis_25)


def get_wis_ability(wis_val, ability):
    """Get the appropriate ability for a given iq value"""
    ability_val = 0
    try:
        ability_val = wis_abilities[wis_val][ability]
        return ability_val
    except IndexError:
        print(ability_val, wis_val, ability)
