import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWizard, QPushButton, QButtonGroup, QLineEdit, QLabel, QGroupBox, \
    QRadioButton, QGridLayout, QWizardPage

from New_Char_Wizard import Ui_Wizard
from Adv_Dark_Deep.Char_Creation import roll_abilities, race_vs_classes


class Wizard(QWizard, Ui_Wizard):
    gender: QButtonGroup
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
        self.gender = self.Gender_buttonGroup
        self.prime_class = self.First_Class_groupBox
        self.second_class = self.Second_Class_groupBox
        self.third_class = self.Third_Class_groupBox

        # Buttons
        self.roll_dice.clicked.connect(self.roll_attribs)
        self.button(QWizard.FinishButton).clicked.connect(self.finished)
        self.button(QWizard.NextButton).clicked.connect(self.possible_classes)

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

    def get_race(self):
        """Get the selected race radiobutton"""
        return self.race.checkedButton().text()

    def get_gender(self):
        """Get the selected gender radiobutton"""
        return self.gender.checkedButton().text()

    def possible_classes(self):
        """Determine which classes the character is eligible for, based on previous selections"""
        try:
            if (self.get_race() == "Dwarf, Hill" or self.get_race() == "Dwarf, Mountain" or
                    self.get_race() == "Dwarf, Grey"):
                race_class = race_vs_classes.multi_class["dwarf"]
            else:
                race_class = race_vs_classes.multi_class[self.get_race().lower()]
                self.enable_classes(race_class, 1)
            print(race_class)
        except KeyError:  # Error indicates not multi-class eligible
            race_class = race_vs_classes.single_class[self.get_race().lower()]
            self.enable_classes(race_class, 0)

    def enable_classes(self, classes, multi):
        """Enable radio button associated with authorized classes"""
        # TODO: Figure out how to not brute-force this
        # TODO: Allow user to go back and pick new race
        if multi == 0:  # Single class
            if "Bard" in classes:
                self.Bard_radioButton.setEnabled(True)
            if "Jester" in classes:
                self.Jester_radioButton.setEnabled(True)
            if "Cavalier" in classes:
                self.Cavalier_radioButton.setEnabled(True)
            if "Paladin" in classes:
                self.Paladin_radioButton.setEnabled(True)
            if "Cleric" in classes:
                self.Cleric_radioButton.setEnabled(True)
            if "Druid" in classes:
                self.Druid_radioButton.setEnabled(True)
            if "Mystic" in classes:
                self.Mystic_radioButton.setEnabled(True)
            if "Fighter" in classes:
                self.Fighter_radioButton.setEnabled(True)
            if "Barbarian" in classes:
                self.Barbarian_radioButton.setEnabled(True)
            if "Ranger" in classes:
                self.Ranger_radioButton.setEnabled(True)
            if "Mage" in classes:
                self.Mage_radioButton.setEnabled(True)
            if "Illusionist" in classes:
                self.Illusionist_radioButton.setEnabled(True)
            if "Savant" in classes:
                self.Savant_radioButton.setEnabled(True)
            if "Thief" in classes:
                self.Thief_radioButton.setEnabled(True)
            if "Thief-Acrobat" in classes:
                self.Thief_Acrobat_radioButton.setEnabled(True)
            if "Mountebank" in classes:
                self.Mountebank_radioButton.setEnabled(True)
            if "Assassin" in classes:
                self.Assassin_radioButton.setEnabled(True)
        elif multi == 1:
            print(classes)


    def finished(self):
        """Actions performed when 'Finish' button is clicked"""
        pass

app = QApplication(sys.argv)
w = Wizard()
if __name__ == "__main__":
    app.exec_()
