import pytest

from Adv_Dark_Deep.Char_Creation import dex_abilities
from Qt_Designer import Char_Sheet


@pytest.fixture
def app(qtbot):
    test_basic_app = Char_Sheet.MainWindow()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


def test_dex_abilities(app, qtbot):
    """Test the strength-associated abilities"""
    for dex in range(1, 26):
        app.dex.setText(str(dex))
        app.init_adj.setText(str(dex_abilities.get_dex_ability(dex, 0)))
        app.missile_adj.setText(str(dex_abilities.get_dex_ability(dex, 1)))
        app.ac_adj.setText(str(dex_abilities.get_dex_ability(dex, 2)))

        assert app.Dex_Output_label.text() == str(dex)
        if 7 <= dex <= 14:
            assert app.Init_Adj_Output_label.text() == str(dex_abilities.dex_7_14.Init_Adj)
            assert app.Missile_Bonus_Output_label.text() == str(dex_abilities.dex_7_14.Missile_Attack)
            assert app.AC_Adj_Output_label_55.text() == str(dex_abilities.dex_7_14.AC_Adj)
        elif dex == 15:
            assert app.Init_Adj_Output_label.text() == str(dex_abilities.dex_15.Init_Adj)
            assert app.Missile_Bonus_Output_label.text() == str(dex_abilities.dex_15.Missile_Attack)
            assert app.AC_Adj_Output_label_55.text() == str(dex_abilities.dex_15.AC_Adj)
        elif dex == 16:
            assert app.Init_Adj_Output_label.text() == str(dex_abilities.dex_16.Init_Adj)
            assert app.Missile_Bonus_Output_label.text() == str(dex_abilities.dex_16.Missile_Attack)
            assert app.AC_Adj_Output_label_55.text() == str(dex_abilities.dex_16.AC_Adj)
        elif dex == 17:
            assert app.Init_Adj_Output_label.text() == str(dex_abilities.dex_17.Init_Adj)
            assert app.Missile_Bonus_Output_label.text() == str(dex_abilities.dex_17.Missile_Attack)
            assert app.AC_Adj_Output_label_55.text() == str(dex_abilities.dex_17.AC_Adj)
        elif 18 <= dex <= 20:
            assert app.Init_Adj_Output_label.text() == str(dex_abilities.dex_18_20.Init_Adj)
            assert app.Missile_Bonus_Output_label.text() == str(dex_abilities.dex_18_20.Missile_Attack)
            assert app.AC_Adj_Output_label_55.text() == str(dex_abilities.dex_18_20.AC_Adj)
        elif 21 <= dex <= 23:
            assert app.Init_Adj_Output_label.text() == str(dex_abilities.dex_21_23.Init_Adj)
            assert app.Missile_Bonus_Output_label.text() == str(dex_abilities.dex_21_23.Missile_Attack)
            assert app.AC_Adj_Output_label_55.text() == str(dex_abilities.dex_21_23.AC_Adj)
        elif dex == 24 or dex == 25:
            assert app.Init_Adj_Output_label.text() == str(dex_abilities.dex_24_25.Init_Adj)
            assert app.Missile_Bonus_Output_label.text() == str(dex_abilities.dex_24_25.Missile_Attack)
            assert app.AC_Adj_Output_label_55.text() == str(dex_abilities.dex_24_25.AC_Adj)
        else:
            assert app.Init_Adj_Output_label.text() == str(dex_abilities.dex_abilities[dex][0])
            assert app.Missile_Bonus_Output_label.text() == str(dex_abilities.dex_abilities[dex][1])
            assert app.AC_Adj_Output_label_55.text() == str(dex_abilities.dex_abilities[dex][2])
