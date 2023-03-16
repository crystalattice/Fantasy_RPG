import pytest

from Adv_Dark_Deep.Char_Creation import wisdom_abilities
from Qt_Designer import Char_Sheet


@pytest.fixture
def app(qtbot):
    test_basic_app = Char_Sheet.MainWindow()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


def test_wisdom_abilities(app, qtbot):
    """Test the strength-associated abilities"""
    for wis in range(1, 26):
        app.wis.setText(str(wis))
        app.magical_attack_adj.setText(str(wisdom_abilities.get_wis_ability(wis, 0)))
        app.cleric_spell_bonus.setText(str(wisdom_abilities.get_wis_ability(wis, 1)))
        app.spell_failure.setText(str(wisdom_abilities.get_wis_ability(wis, 2)))
        app.immune_charm.setText(str(wisdom_abilities.get_wis_ability(wis, 3)))

        assert app.Wisdom_Output_label.text() == str(wis)
        assert app.Mag_Attack_Output_label.text() == str(wisdom_abilities.wis_abilities[wis][0])
        assert app.Spell_Bonus_Output_label.text() == str(wisdom_abilities.wis_abilities[wis][1])
        assert app.Spell_Fail_Output_label.text() == str(wisdom_abilities.wis_abilities[wis][2])
        assert app.Immunity_Output_label_2.text() == str(wisdom_abilities.wis_abilities[wis][3])
