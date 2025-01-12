import pytest

from Archived.Adv_Dark_Deep.Char_Creation import iq_abilities
from Archived.Qt_Designer import Char_Sheet


@pytest.fixture
def app(qtbot):
    test_basic_app = Char_Sheet.MainWindow()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


def test_iq_abilities(app, qtbot):
    """Test the strength-associated abilities"""
    for iq in range(1, 26):
        app.iq.setText(str(iq))
        app.max_lang.setText(str(iq_abilities.get_iq_ability(iq, 0)))
        app.immune_illusion.setText(str(iq_abilities.get_iq_ability(iq, 1)))
        app.max_spell_level.setText(str(iq_abilities.get_iq_ability(iq, 2)))

        assert app.IQ_Output_label.text() == str(iq)
        assert app.Lang_Output_label.text() == str(iq_abilities.iq_abilities[iq][0])
        assert app.Immunity_Output_label.text() == str(iq_abilities.iq_abilities[iq][1])
        assert app.Max_Level_Output_label.text() == str(iq_abilities.iq_abilities[iq][2])
