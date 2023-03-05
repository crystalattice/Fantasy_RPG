from collections import namedtuple

dex_abilities = namedtuple("Dex", ["Init Bonus", "Missile Bonus", "AC Bonus"])

dex_1 = dex_abilities(5, -5, 6)
dex_2 = dex_abilities(4, -4, 5)
dex_3 = dex_abilities(3, -3, 4)
dex_4 = dex_abilities(2, -2, 3)
dex_5 = dex_abilities(1, -1, 2)
dex_6 = dex_abilities(0, 0, 1)
dex_7_14 = dex_abilities(0, 0, 0)
dex_15 = dex_abilities(0, 0, -1)
dex_16 = dex_abilities(-1, 1, -2)
dex_17 = dex_abilities(-2, 2, -3)
dex_18_20 = dex_abilities(-3, 3, -4)
dex_21_23 = dex_abilities(-4, 4, -5)
dex_24_25 = dex_abilities(-5, 5, -6)
