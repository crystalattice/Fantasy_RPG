from collections import namedtuple

iq = namedtuple("IQ", ["Max_Additional_Languages", "Immune_to_Illusion", "Max_Mage_Spell_Level"])

iq_1 = iq(0, 0, 0)
iq_2 = iq(0, 0, 0)
iq_3 = iq(0, 0, 0)
iq_4 = iq(0, 0, 0)
iq_5 = iq(0, 0, 0)
iq_6 = iq(0, 0, 0)
iq_7 = iq(0, 0, 0)
iq_8 = iq(1, 0, 0)
iq_9 = iq(1, 0, 4)
iq_10 = iq(2, 0, 5)
iq_11 = iq(2, 0, 5)
iq_12 = iq(3, 0, 6)
iq_13 = iq(3, 0, 6)
iq_14 = iq(4, 0, 7)
iq_15 = iq(4, 0, 7)
iq_16 = iq(5, 0, 8)
iq_17 = iq(6, 0, 8)
iq_18 = iq(7, 0, 9)
iq_19 = iq(7, 1, 9)
iq_20 = iq(7, 2, 9)
iq_21 = iq(7, 3, 9)
iq_22 = iq(7, 4, 9)
iq_23 = iq(7, 5, 9)
iq_24 = iq(7, 6, 9)
iq_25 = iq(7, 7, 9)

iq_abilities = (None, iq_1, iq_2, iq_3, iq_4, iq_5, iq_6, iq_7, iq_8, iq_9, iq_10, iq_11, iq_12, iq_13, iq_14, iq_15,
                iq_16, iq_17, iq_18, iq_19, iq_20, iq_21, iq_22, iq_23, iq_24, iq_25)


def get_iq_ability(iq_val, ability):
    """Get the appropriate ability for a given iq value"""
    ability_val = 0
    try:
        ability_val = iq_abilities[iq_val][ability]
        return ability_val
    except IndexError:
        print(ability_val, iq_val, ability)
