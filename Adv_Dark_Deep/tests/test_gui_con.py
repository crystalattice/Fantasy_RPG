import pytest

from Adv_Dark_Deep.Char_Creation import con_abilities
from Qt_Designer import Char_Sheet


@pytest.fixture
def app(qtbot):
    test_basic_app = Char_Sheet.MainWindow()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


def test_con_abilities(app, qtbot):
    """Test the strength-associated abilities"""
    for con in range(1, 26):
        app.con.setText(str(con))
        app.hp_adj.setText(str(con_abilities.get_con_ability(con, 0)))
        app.sys_shock.setText(str(con_abilities.get_con_ability(con, 3)))
        app.resurrection.setText(str(con_abilities.get_con_ability(con, 4)))

        assert app.CON_Output_label.text() == str(con)
        if con == 19 or con == 20:
            assert app.HP_Adj_Output_label.text() == str(con_abilities.con_19_20.HP_Bonus)
            assert app.Sys_Shock_Output_label.text() == str(con_abilities.con_19_20.System_Shock)
            assert app.Resurrect_Output_label.text() == str(con_abilities.con_19_20.Resurrection)
        elif con == 21 or con == 22:
            assert app.HP_Adj_Output_label.text() == str(con_abilities.con_21_22.HP_Bonus)
            assert app.Sys_Shock_Output_label.text() == str(con_abilities.con_21_22.System_Shock)
            assert app.Resurrect_Output_label.text() == str(con_abilities.con_21_22.Resurrection)
        elif con == 23:
            assert app.HP_Adj_Output_label.text() == str(con_abilities.con_23.HP_Bonus)
            assert app.Sys_Shock_Output_label.text() == str(con_abilities.con_23.System_Shock)
            assert app.Resurrect_Output_label.text() == str(con_abilities.con_23.Resurrection)
        elif con == 24 or con == 25:
            assert app.HP_Adj_Output_label.text() == str(con_abilities.con_24_25.HP_Bonus)
            assert app.Sys_Shock_Output_label.text() == str(con_abilities.con_24_25.System_Shock)
            assert app.Resurrect_Output_label.text() == str(con_abilities.con_24_25.Resurrection)
        else:
            assert app.HP_Adj_Output_label.text() == str(con_abilities.con_abilities[con][0])
            assert app.Sys_Shock_Output_label.text() == str(con_abilities.con_abilities[con][3])
            assert app.Resurrect_Output_label.text() == str(con_abilities.con_abilities[con][4])
