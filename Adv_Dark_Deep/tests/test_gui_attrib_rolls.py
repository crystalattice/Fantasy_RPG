import pytest

from Qt_Designer import Char_Sheet


@pytest.fixture
def app(qtbot):
    test_basic_app = Char_Sheet.MainWindow()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


# Test character sheet dice rollers
expected_roll = []
for i in range(3, 19):
    expected_roll.append(str(i))


def test_2d6(app, qtbot):
    """Test the 2d6 sheet dice roller"""
    Char_Sheet.MainWindow.roll_2d6(app)

    assert app.STR_Output_label.text() in expected_roll
    assert app.Dex_Output_label.text() in expected_roll
    assert app.Wisdom_Output_label.text() in expected_roll
    assert app.IQ_Output_label.text() in expected_roll
    assert app.CON_Output_label.text() in expected_roll
    assert app.CHR_Output_label.text() in expected_roll


def test_3d6(app, qtbot):
    """Test the 3d6 sheet dice roller"""
    Char_Sheet.MainWindow.roll_3d6(app)

    assert app.STR_Output_label.text() in expected_roll
    assert app.Dex_Output_label.text() in expected_roll
    assert app.Wisdom_Output_label.text() in expected_roll
    assert app.IQ_Output_label.text() in expected_roll
    assert app.CON_Output_label.text() in expected_roll
    assert app.CHR_Output_label.text() in expected_roll


def test_4d6(app, qtbot):
    """Test the 4d6-least sheet dice roller"""
    Char_Sheet.MainWindow.roll_4d6(app)

    assert app.STR_Output_label.text() in expected_roll
    assert app.Dex_Output_label.text() in expected_roll
    assert app.Wisdom_Output_label.text() in expected_roll
    assert app.IQ_Output_label.text() in expected_roll
    assert app.CON_Output_label.text() in expected_roll
    assert app.CHR_Output_label.text() in expected_roll
