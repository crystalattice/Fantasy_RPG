import pytest
from Adv_Dark_Deep.Char_Creation import roll_abilities


class Test3d6:
    def test_multiple_rolls(self):
        for i in range(25):  # Run 25 tests (equals 150 rolls)
            rolls = roll_abilities.three_d6()
            for val in rolls:
                assert 3 <= val <= 18


class Test4d6:
    def test_multiple_rolls(self):
        for i in range(25):
            rolls = roll_abilities.four_d6_drop_lowest()
            for val in rolls:
                assert 3 <= val <= 18


class Test2d6:
    def test_multiple_rolls(self):
        for i in range(25):
            rolls = roll_abilities.two_d6_plus_6()
            for val in rolls:
                assert 3 <= val <= 18
