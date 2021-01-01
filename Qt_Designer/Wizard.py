import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWizard, QPushButton, QButtonGroup, QLineEdit, QLabel, QGroupBox

from New_Char_Wizard import Ui_Wizard
from Adv_Dark_Deep.Char_Creation import roll_abilities


class Wizard(QWizard, Ui_Wizard):
    third_class: QGroupBox
    second_class: QGroupBox
    prime_class: QGroupBox
    race: QButtonGroup
    chr: QLabel
    con: QLabel
    wis: QLabel
    iq: QLabel
    dex: QLabel
    bonus_strength: QLabel
    strength: QLabel
    bonus_strength: QLabel
    name: QLineEdit
    roll_dice: QPushButton
    roll_type: QButtonGroup

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

        # Dice objects
        self.roll_type = self.Dice_Type_buttonGroup
        self.roll_dice = self.Roll_Attribs_pushButton

        # Data for char sheet
        self.name = self.Char_Name_Out_lineEdit
        self.strength = self.STR_Out_label
        self.bonus_strength = self.STR_Out_label_2
        self.dex = self.DEX_Out_label
        self.iq = self.IQ_Out_label
        self.wis = self.WIS_Out_label
        self.con = self.CON_Out_label
        self.chr = self.CHR_Out_label
        self.race = self.Race_buttonGroup
        self.prime_class = self.First_Class_groupBox
        self.second_class = self.Second_Class_groupBox
        self.third_class = self.Third_Class_groupBox

        # Buttons
        self.roll_dice.clicked.connect(self.roll_attribs)
        self.button(QWizard.FinishButton).clicked.connect(self.finished)
        self.UnderDark_checkBox.stateChanged.connect(self.under_dark_checked)

    def roll_attribs(self):
        """Roll the dice for character attributes"""
        if self.roll_type.checkedButton().text() == "4d6, drop lowest":
            rolls: list = roll_abilities.four_d6_drop_lowest()
            self.insert_rolls(rolls)
        elif self.roll_type.checkedButton().text() == "3d6":
            rolls: list = roll_abilities.three_d6()
            self.insert_rolls(rolls)
        elif self.roll_type.checkedButton().text() == "2d6+6":
            rolls: list = roll_abilities.two_d6_plus_6()
            self.insert_rolls(rolls)

    def insert_rolls(self, rolls):
        """Put the attribute rolls into their respective variables"""
        strength: str
        bonus_strength: str
        dex: str
        iq: str
        wis: str
        con: str
        chr: str
        strength, dex, iq, wis, con, chr = [str(rolls[i]) for i in range(6)]
        if strength == "18":
            self.bonus_strength.setText(str(roll_abilities.multi_die(1, 100)))
        else:
            self.bonus_strength.setText("0")
        self.strength.setText(strength)
        self.dex.setText(dex)
        self.iq.setText(iq)
        self.wis.setText(wis)
        self.con.setText(con)
        self.chr.setText(chr)

    def under_dark_checked(self):
        """
        If UnderDark races allowed, enable them in the groupbox.

        Toggles between enabled and disabled to ensure that the UnderDark races aren't left enabled.
        """
        if self.UnderDark_checkBox.isChecked():
            self.Gnome_Deep_radioButton.setEnabled(True)
            self.Elf_Dark_radioButton.setEnabled(True)
            self.Dwarf_Gray_radioButton.setEnabled(True)
        else:
            self.Gnome_Deep_radioButton.setEnabled(False)
            self.Elf_Dark_radioButton.setEnabled(False)
            self.Dwarf_Gray_radioButton.setEnabled(False)

    def finished(self):
        """Actions performed when 'Finish' button is clicked"""
        print(self.name.text())


app = QApplication(sys.argv)
w = Wizard()
if __name__ == "__main__":
    app.exec_()
