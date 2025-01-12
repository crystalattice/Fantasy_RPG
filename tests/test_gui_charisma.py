import pytest

from Archived.Adv_Dark_Deep.Char_Creation import charisma_abilities
from Archived.Qt_Designer import Char_Sheet


@pytest.fixture
def app(qtbot):
    test_basic_app = Char_Sheet.MainWindow()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


def test_charisma_abilities(app, qtbot):
    """Test the strength-associated abilities"""
    for char in range(1, 26):
        app.chr.setText(str(char))
        app.max_henchmen.setText(str(charisma_abilities.get_char_ability(char, 0)))
        app.morale_adj.setText(str(charisma_abilities.get_char_ability(char, 1)))
        app.reaction_adj.setText(str(charisma_abilities.get_char_ability(char, 2)))

        assert app.CHR_Output_label.text() == str(char)
        if char < 9:
            assert app.Henchmen_Output_label.text() == str(charisma_abilities.char_abilities[char][0])
            assert app.Morale_Output_label.text() == str(charisma_abilities.char_abilities[char][1])
            assert app.React_Output_label.text() == str(charisma_abilities.char_abilities[char][2])
        elif 9 <= char <= 11:
            assert app.Henchmen_Output_label.text() == str(charisma_abilities.char_9_11.Max_Henchmen)
            assert app.Morale_Output_label.text() == str(charisma_abilities.char_9_11.Morale_Adj)
            assert app.React_Output_label.text() == str(charisma_abilities.char_9_11.React_Adj)
        else:
            assert app.Henchmen_Output_label.text() == str(charisma_abilities.char_abilities[char - 2][0])
            assert app.Morale_Output_label.text() == str(charisma_abilities.char_abilities[char - 2][1])
            assert app.React_Output_label.text() == str(charisma_abilities.char_abilities[char - 2][2])
