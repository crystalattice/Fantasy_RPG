import pytest

from Adv_Dark_Deep.Char_Creation import strength_abilities, iq_abilities, dex_abilities, wisdom_abilities, \
    con_abilities, charisma_abilities
from Qt_Designer import Char_Sheet


@pytest.fixture
def app(qtbot):
    test_basic_app = Char_Sheet.MainWindow()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


expected_roll = []
for i in range(3, 19):
    expected_roll.append(str(i))

full_range = []
for i in range(1, 26):
    full_range.append(i)


def test_2d6(app, qtbot):
    Char_Sheet.MainWindow.roll_2d6(app)

    assert app.STR_Output_label.text() in expected_roll
    assert app.Dex_Output_label.text() in expected_roll
    assert app.Wisdom_Output_label.text() in expected_roll
    assert app.IQ_Output_label.text() in expected_roll
    assert app.CON_Output_label.text() in expected_roll
    assert app.CHR_Output_label.text() in expected_roll


def test_3d6(app, qtbot):
    Char_Sheet.MainWindow.roll_3d6(app)

    assert app.STR_Output_label.text() in expected_roll
    assert app.Dex_Output_label.text() in expected_roll
    assert app.Wisdom_Output_label.text() in expected_roll
    assert app.IQ_Output_label.text() in expected_roll
    assert app.CON_Output_label.text() in expected_roll
    assert app.CHR_Output_label.text() in expected_roll


def test_4d6(app, qtbot):
    Char_Sheet.MainWindow.roll_4d6(app)

    assert app.STR_Output_label.text() in expected_roll
    assert app.Dex_Output_label.text() in expected_roll
    assert app.Wisdom_Output_label.text() in expected_roll
    assert app.IQ_Output_label.text() in expected_roll
    assert app.CON_Output_label.text() in expected_roll
    assert app.CHR_Output_label.text() in expected_roll


def test_strength_abilities(app, qtbot):
    for val in full_range:
        strength = val
        app.strength.setText(str(strength))
        app.to_hit_bonus.setText(str(strength_abilities.get_str_ability(strength, 0)))
        app.damage_bonus.setText(str(strength_abilities.get_str_ability(strength, 1)))
        app.carry_bonus.setText(str(strength_abilities.get_str_ability(strength, 2)))
        app.stuck_doors.setText(str(strength_abilities.get_str_ability(strength, 3)))
        app.locked_doors_bonus.setText(str(strength_abilities.get_str_ability(strength, 4)))
        app.bend_bars.setText(str(strength_abilities.get_str_ability(strength, 5)))

        assert app.STR_Output_label.text() == str(strength)
        assert app.Hit_Bonus_label.text() == str(strength_abilities.str_abilities[val][0])
        assert app.Damage_Mod_Output_label.text() == str(strength_abilities.str_abilities[val][1])
        assert app.Carry_Bonus_Output_label.text() == str(strength_abilities.str_abilities[val][2])
        assert app.Stuck_Doors_Output_label.text() == str(strength_abilities.str_abilities[val][3])
        assert app.Open_Doors_Output_label.text() == str(strength_abilities.str_abilities[val][4])
        assert app.Bend_Bars_Output_label.text() == str(strength_abilities.str_abilities[val][5])


def test_exceptional_str_abilities(app, qtbot):
    bonus = []
    for j in range(1, 101):
        bonus.append(int(f"{18}{j}"))

    for val in bonus:
        app.to_hit_bonus.setText(str(strength_abilities.get_str_ability(val, 0)))
        app.damage_bonus.setText(str(strength_abilities.get_str_ability(val, 1)))
        app.carry_bonus.setText(str(strength_abilities.get_str_ability(val, 2)))
        app.stuck_doors.setText(str(strength_abilities.get_str_ability(val, 3)))
        app.locked_doors_bonus.setText(str(strength_abilities.get_str_ability(val, 4)))
        app.bend_bars.setText(str(strength_abilities.get_str_ability(val, 5)))

        if 181 <= val <= 1850:
            assert app.Hit_Bonus_label.text() == str(strength_abilities.str_181_1850.ToHit_Modifier)
            assert app.Damage_Mod_Output_label.text() == str(strength_abilities.str_181_1850.Damage_Modifier)
            assert app.Carry_Bonus_Output_label.text() == str(strength_abilities.str_181_1850.Weight_Allowance)
            assert app.Stuck_Doors_Output_label.text() == str(strength_abilities.str_181_1850.Open_Stuck_Doors)
            assert app.Open_Doors_Output_label.text() == str(strength_abilities.str_181_1850.Open_Locked_Doors)
            assert app.Bend_Bars_Output_label.text() == str(strength_abilities.str_181_1850.Bend_Bars_Lift_Gates)
        if 1851 <= val <= 1875:
            assert app.Hit_Bonus_label.text() == str(strength_abilities.str_1851_1875.ToHit_Modifier)
            assert app.Damage_Mod_Output_label.text() == str(strength_abilities.str_1851_1875.Damage_Modifier)
            assert app.Carry_Bonus_Output_label.text() == str(strength_abilities.str_1851_1875.Weight_Allowance)
            assert app.Stuck_Doors_Output_label.text() == str(strength_abilities.str_1851_1875.Open_Stuck_Doors)
            assert app.Open_Doors_Output_label.text() == str(strength_abilities.str_1851_1875.Open_Locked_Doors)
            assert app.Bend_Bars_Output_label.text() == str(strength_abilities.str_1851_1875.Bend_Bars_Lift_Gates)
        if 1876 <= val <= 1890:
            assert app.Hit_Bonus_label.text() == str(strength_abilities.str_1876_1890.ToHit_Modifier)
            assert app.Damage_Mod_Output_label.text() == str(strength_abilities.str_1876_1890.Damage_Modifier)
            assert app.Carry_Bonus_Output_label.text() == str(strength_abilities.str_1876_1890.Weight_Allowance)
            assert app.Stuck_Doors_Output_label.text() == str(strength_abilities.str_1876_1890.Open_Stuck_Doors)
            assert app.Open_Doors_Output_label.text() == str(strength_abilities.str_1876_1890.Open_Locked_Doors)
            assert app.Bend_Bars_Output_label.text() == str(strength_abilities.str_1876_1890.Bend_Bars_Lift_Gates)
        if 1891 <= val <= 1899:
            assert app.Hit_Bonus_label.text() == str(strength_abilities.str_1891_1899.ToHit_Modifier)
            assert app.Damage_Mod_Output_label.text() == str(strength_abilities.str_1891_1899.Damage_Modifier)
            assert app.Carry_Bonus_Output_label.text() == str(strength_abilities.str_1891_1899.Weight_Allowance)
            assert app.Stuck_Doors_Output_label.text() == str(strength_abilities.str_1891_1899.Open_Stuck_Doors)
            assert app.Open_Doors_Output_label.text() == str(strength_abilities.str_1891_1899.Open_Locked_Doors)
            assert app.Bend_Bars_Output_label.text() == str(strength_abilities.str_1891_1899.Bend_Bars_Lift_Gates)
        if val == 18100:
            assert app.Hit_Bonus_label.text() == str(strength_abilities.str_18100.ToHit_Modifier)
            assert app.Damage_Mod_Output_label.text() == str(strength_abilities.str_18100.Damage_Modifier)
            assert app.Carry_Bonus_Output_label.text() == str(strength_abilities.str_18100.Weight_Allowance)
            assert app.Stuck_Doors_Output_label.text() == str(strength_abilities.str_18100.Open_Stuck_Doors)
            assert app.Open_Doors_Output_label.text() == str(strength_abilities.str_18100.Open_Locked_Doors)
            assert app.Bend_Bars_Output_label.text() == str(strength_abilities.str_18100.Bend_Bars_Lift_Gates)
