import pytest

from PyQt5 import QtCore

from Qt_Designer import Char_Sheet


@pytest.fixture
def app(qtbot):
    test_basic_app = Char_Sheet.MainWindow()
    qtbot.addWidget(test_basic_app)

    return test_basic_app


expected_vals = []
for i in range(3, 19):
    expected_vals.append(str(i))


def test_2d6(app, qtbot):
    Char_Sheet.MainWindow.roll_2d6(app)

    assert app.STR_Output_label.text() in expected_vals
    assert app.Dex_Output_label.text() in expected_vals
    assert app.Wisdom_Output_label.text() in expected_vals
    assert app.IQ_Output_label.text() in expected_vals
    assert app.CON_Output_label.text() in expected_vals
    assert app.CHR_Output_label.text() in expected_vals


def test_3d6(app, qtbot):
    Char_Sheet.MainWindow.roll_3d6(app)

    assert app.STR_Output_label.text() in expected_vals
    assert app.Dex_Output_label.text() in expected_vals
    assert app.Wisdom_Output_label.text() in expected_vals
    assert app.IQ_Output_label.text() in expected_vals
    assert app.CON_Output_label.text() in expected_vals
    assert app.CHR_Output_label.text() in expected_vals


def test_4d6(app, qtbot):
    Char_Sheet.MainWindow.roll_4d6(app)

    assert app.STR_Output_label.text() in expected_vals
    assert app.Dex_Output_label.text() in expected_vals
    assert app.Wisdom_Output_label.text() in expected_vals
    assert app.IQ_Output_label.text() in expected_vals
    assert app.CON_Output_label.text() in expected_vals
    assert app.CHR_Output_label.text() in expected_vals

