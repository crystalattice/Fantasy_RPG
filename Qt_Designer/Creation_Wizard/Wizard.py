import pickle
import random
import sys
from pathlib import Path

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWizard, QPushButton, QButtonGroup, QLineEdit, QLabel, QGroupBox, \
    QRadioButton, QGridLayout, QWizardPage, QWidget, QMessageBox

import Adv_Dark_Deep
from New_Char_Wizard import Ui_Wizard
from Adv_Dark_Deep.Char_Creation import roll_abilities, get_acceptable_class, class_min_attribs, race_vs_attribs


class Wizard(QWizard, Ui_Wizard):
    gender: QButtonGroup
    char_3rd_class: QGroupBox
    char_2nd_class: QGroupBox
    char_class: QGroupBox
    race: QButtonGroup
    chr: QLabel
    con: QLabel
    wis: QLabel
    iq: QLabel
    dex: QLabel
    bonus_strength: QLabel
    strength: QLabel
    bonus_strength: QLabel
    char_name: QLineEdit
    roll_dice: QPushButton
    roll_type: QButtonGroup

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.age = 0
        self.setupUi(self)
        self.show()

        # Dice objects
        self.roll_type = self.Dice_Type_buttonGroup
        self.roll_dice = self.Roll_Attribs_pushButton

        # Data for char sheet
        self.char_name = self.Char_Name_Out_lineEdit
        self.strength = self.STR_Out_label
        self.bonus_strength = self.STR_Out_label_2
        self.dex = self.DEX_Out_label
        self.iq = self.IQ_Out_label
        self.wis = self.WIS_Out_label
        self.con = self.CON_Out_label
        self.chr = self.CHR_Out_label
        self.multi = False
        self.classes = ()
        self.social_class = ""
        self.money = 0

        # Buttons
        self.roll_dice.clicked.connect(self.roll_attribs)
        self.button(QWizard.FinishButton).clicked.connect(self.finished)
        self.button(QWizard.NextButton).clicked.connect(self.confirm_page)
        self.button(QWizard.BackButton).clicked.connect(self.confirm_page)

    def confirm_page(self):
        """Check for current Wizard page and apply appropriate method"""
        if self.currentId() == 1:
            self.populate_races()
        elif self.currentId() == 2:
            self.enable_classes()
        elif self.currentId() == 3:
            self.multi_class()

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

    def get_gender(self):
        """Get the selected gender radiobutton"""
        return self.Gender_buttonGroup.checkedButton().text()

    def populate_races(self):
        """Enable appropriate radio buttons for available races, based on attributes and gender.

        Provides a check to ensure name and attributes are provided before moving on.
        """
        if not self.char_name.text():
            no_name_msg: QMessageBox | QMessageBox = QMessageBox()
            no_name_msg.setWindowTitle("Missing Character Name")
            no_name_msg.setText("You must provide a character name prior to saving. Please go back and ensure your"
                                "character has a name.")
            no_name_msg.setIcon(QMessageBox.Icon.Warning)
            button = no_name_msg.exec()
            button = QMessageBox.StandardButtons(button)

        try:
            races = race_vs_attribs.get_acceptable_race(self.get_gender(), int(self.strength.text()),
                                                        int(self.iq.text()),
                                                        int(self.wis.text()), int(self.dex.text()),
                                                        int(self.con.text()),
                                                        int(self.chr.text()))
            if "Dwarf, Hill" in races:
                self.Dwarf_Hill_radioButton.setEnabled(True)
            if "Dwarf, Grey (Duergar)" in races:
                self.Dwarf_Grey_radioButton.setEnabled(True)
            if "Dwarf, Mountain" in races:
                self.Dwarf_Mountain_radioButton.setEnabled(True)
            if "Elf, Dark (Drow)" in races:
                self.Elf_Dark_radioButton.setEnabled(True)
            if "Elf, Grey" in races:
                self.Elf_Grey_radioButton.setEnabled(True)
            if "Half-Elf" in races:
                self.Elf_Half_radioButton.setEnabled(True)
            if "Elf, High" in races:
                self.Elf_High_radioButton.setEnabled(True)
            if "Elf, Wood" in races:
                self.Elf_Wood_radioButton.setEnabled(True)
            if "Elf, Wild" in races:
                self.Elf_Wild_radioButton.setEnabled(True)
            if "Gnome, Deep (Svirfneblin)" in races:
                self.Gnome_Deep_radioButton.setEnabled(True)
            if "Gnome, Forest" in races:
                self.Gnome_Forest_radioButton.setEnabled(True)
            if "Gnome, Hill" in races:
                self.Gnome_Hill_radioButton.setEnabled(True)
            if "Halfling" in races:
                self.Halfling_radioButton.setEnabled(True)
            if "Half-Orc" in races:
                self.Half_Orc_radioButton.setEnabled(True)
        except ValueError:
            no_attribs_msg: QMessageBox | QMessageBox = QMessageBox()
            no_attribs_msg.setWindowTitle("Missing Attributes")
            no_attribs_msg.setText("You must roll for attributes prior to saving. Please go back and generate "
                                   "attributes.")
            no_attribs_msg.setIcon(QMessageBox.Icon.Warning)
            button: QMessageBox.StandardButtons = no_attribs_msg.exec()
            button = QMessageBox.StandardButtons(button)

    def get_race(self):
        """Get the selected race radiobutton"""
        return self.Race_buttonGroup.checkedButton().text()

    def enable_classes(self):
        """Enable radio button associated with authorized classes"""
        # TODO: Check race vs class for Assassin
        if self.get_race() == "Human":
            self.multi = False
        else:
            self.multi = True
        self.classes = get_acceptable_class.get_one_class(self.get_race())

        if "Bard" in self.classes:
            self.Bard_radioButton.setEnabled(True)
        if "Jester" in self.classes:
            self.Jester_radioButton.setEnabled(True)
        if "Cavalier" in self.classes:
            self.Cavalier_radioButton.setEnabled(True)
        if "Paladin" in self.classes:
            self.Paladin_radioButton.setEnabled(True)
        if "Cleric" in self.classes:
            self.Cleric_radioButton.setEnabled(True)
        if "Druid" in self.classes:
            self.Druid_radioButton.setEnabled(True)
        if "Mystic" in self.classes:
            self.Mystic_radioButton.setEnabled(True)
        if "Fighter" in self.classes:
            self.Fighter_radioButton.setEnabled(True)
        if "Barbarian" in self.classes:
            self.Barbarian_radioButton.setEnabled(True)
        if "Ranger" in self.classes:
            self.Ranger_radioButton.setEnabled(True)
        if "Mage" in self.classes:
            self.Mage_radioButton.setEnabled(True)
        if "Illusionist" in self.classes:
            self.Illusionist_radioButton.setEnabled(True)
        if "Savant" in self.classes:
            self.Savant_radioButton.setEnabled(True)
        if "Thief" in self.classes:
            self.Thief_radioButton.setEnabled(True)
        if "Thief-Acrobat" in self.classes:
            self.Thief_Acrobat_radioButton.setEnabled(True)
        if "Mountebank" in self.classes:
            self.Mountebank_radioButton.setEnabled(True)
        if "Assassin" in self.classes:
            self.Assassin_radioButton.setEnabled(True)

    def multi_class(self):
        """Enable multiclass selections"""
        try:
            self.First_Class_buttonGroup.checkedButton().text()
        except AttributeError:
            no_name_msg: QMessageBox | QMessageBox = QMessageBox()
            no_name_msg.setWindowTitle("Missing Character Class")
            no_name_msg.setText("Your character must have at least one class. Please go back and select a primary "
                                "class.")
            no_name_msg.setIcon(QMessageBox.Icon.Warning)
            button = no_name_msg.exec()
            button = QMessageBox.StandardButtons(button)

        if self.multi is True:
            if "Bard" in self.classes:
                self.Bard_radioButton_5.setEnabled(True)
                self.Bard_radioButton_6.setEnabled(True)
            if "Jester" in self.classes:
                self.Jester_radioButton_5.setEnabled(True)
                self.Jester_radioButton_6.setEnabled(True)
            if "Cavalier" in self.classes:
                self.Cavalier_radioButton_5.setEnabled(True)
                self.Cavalier_radioButton_6.setEnabled(True)
            if "Paladin" in self.classes:
                self.Paladin_radioButton_5.setEnabled(True)
                self.Paladin_radioButton_6.setEnabled(True)
            if "Cleric" in self.classes:
                self.Cleric_radioButton_5.setEnabled(True)
                self.Cleric_radioButton_6.setEnabled(True)
            if "Druid" in self.classes:
                self.Druid_radioButton_5.setEnabled(True)
                self.Druid_radioButton_6.setEnabled(True)
            if "Mystic" in self.classes:
                self.Mystic_radioButton_5.setEnabled(True)
                self.Mystic_radioButton_6.setEnabled(True)
            if "Fighter" in self.classes:
                self.Fighter_radioButton_5.setEnabled(True)
                self.Fighter_radioButton_6.setEnabled(True)
            if "Barbarian" in self.classes:
                self.Barbarian_radioButton_5.setEnabled(True)
                self.Barbarian_radioButton_6.setEnabled(True)
            if "Ranger" in self.classes:
                self.Ranger_radioButton_5.setEnabled(True)
                self.Ranger_radioButton_6.setEnabled(True)
            if "Mage" in self.classes:
                self.Mage_radioButton_5.setEnabled(True)
                self.Mage_radioButton_6.setEnabled(True)
            if "Illusionist" in self.classes:
                self.Illusionist_radioButton_5.setEnabled(True)
                self.Illusionist_radioButton_6.setEnabled(True)
            if "Savant" in self.classes:
                self.Savant_radioButton_5.setEnabled(True)
                self.Savant_radioButton_6.setEnabled(True)
            if "Thief" in self.classes:
                self.Thief_radioButton_5.setEnabled(True)
                self.Thief_radioButton_6.setEnabled(True)
            if "Thief-Acrobat" in self.classes:
                self.Thief_Acrobat_radioButton_5.setEnabled(True)
                self.Thief_Acrobat_radioButton_6.setEnabled(True)
            if "Mountebank" in self.classes:
                self.Mountebank_radioButton_5.setEnabled(True)
                self.Mountebank_radioButton_6.setEnabled(True)
            if "Assassin" in self.classes:
                self.Assassin_radioButton_5.setEnabled(True)
                self.Assassin_radioButton_6.setEnabled(True)

    def get_classes(self):
        """Get the primary and multi-classes, if available"""
        char_class = self.First_Class_buttonGroup.checkedButton().text()
        if self.multi is True:
            char_2nd_class = self.Second_Class_buttonGroup.checkedButton().text()
            char_3rd_class = self.Third_Class_buttonGroup.checkedButton().text()
        else:
            char_2nd_class = ""
            char_3rd_class = ""
        return char_class, char_2nd_class, char_3rd_class

    def starting_hp(self):
        """Calculate starting hit points"""
        pass

    def starting_money(self):
        """Calculate starting money"""
        if self.char_class == "Thief" or self.char_class == "Thief_Acrobat" or self.char_class == "Assassin" \
                or self.char_class == "Mountebank" or self.char_class == "Bard":
            self.money = random.randint(20, 120)
        elif self.char_class == "Mage" or self.char_class == "Illusionist" or self.char_class == "Savant" \
                or self.char_class == "Jester":
            self.money = random.randint(20, 80)
        elif self.char_class == "Cleric" or self.char_class == "Druid":
            self.money = random.randint(30, 180)
        elif self.char_class == "Mystic":
            self.money = random.randint(13, 24)
        elif self.char_class == "Fighter" or self.char_class == "Barbarian" or self.char_class == "Ranger":
            self.money = random.randint(50, 200)
        elif self.char_class == "Cavalier" or self.char_class == "Paladin":
            self.money = (random.randint(1, 2) + 6) * 10

    def social_class(self):
        """Determine character's social class"""
        if self.char_class == "Thief" or self.char_class == "Thief_Acrobat" or self.char_class == "Assassin" \
                or self.char_class == "Mountebank":
            self.social_class = "Lower-Lower Class"
        elif self.char_class == "Bard" or self.char_class == "Barbarian" or self.char_class == "Jester":
            self.social_class = "Middle-Lower Class"
        elif self.char_class == "Fighter":
            self.social_class = "Upper-Lower Class"
        elif self.char_class == "Druid" or self.char_class == "Ranger" or self.char_class == "Mystic":
            self.social_class = "Lower-Middle Class"
        elif self.char_class == "Mage" or self.char_class == "Illusionist" or self.char_class == "Savant":
            self.social_class = "Middle-Middle Class"
        elif self.char_class == "Cleric":
            self.social_class = "Upper-Middle Class"
        elif self.char_class == "Paladin" or self.char_class == "Cavalier":
            self.social_class = "Lower-Upper Class"

    def initial_age(self):
        """Determine starting age"""
        if self.char_class == "Bard":
            if "Elf" in self.race:
                self.age = roll_abilities.multi_die(4, 8) + 300
            elif "Gnome" in self.race:
                self.age = roll_abilities.multi_die(2, 6) + 200
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(2, 12) + 30
            elif self.race == "Halfling":
                self.age = roll_abilities.multi_die(1, 6) + 26
            else:  # Default Human
                self.age = roll_abilities.multi_die(1, 4) + 16
        elif self.char_class == "Jester":
            if "Gnome" in self.race:
                self.age = roll_abilities.multi_die(1, 6) + 200
            elif self.race == "Halfling":
                self.age = roll_abilities.multi_die(1, 8) + 24
            else:  # Default Human
                self.age = roll_abilities.multi_die(1, 4) + 16
        elif self.char_class == "Cavalier":
            if "Elf" in self.race:
                self.age = roll_abilities.multi_die(10, 10) + 500
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(2, 4) + 40
            else:
                self.age = roll_abilities.multi_die(1, 4) + 18
        elif self.char_class == "Paladin":  # Can only be human
            self.age = roll_abilities.multi_die(1, 4) + 17
        elif self.char_class == "Cleric":
            if "Dwarf" in self.race:
                self.age = roll_abilities.multi_die(2, 20) + 250
            elif "Elf" in self.race:
                self.age = roll_abilities.multi_die(10, 10) + 500
            elif "Gnome" in self.race:
                self.age = roll_abilities.multi_die(3, 12) + 300
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(2, 4) + 40
            elif self.race == "Halfling":
                self.age = roll_abilities.multi_die(2, 4) + 38
            elif self.race == "Half-Orc":
                self.age = roll_abilities.multi_die(1, 4) + 20
            else:
                self.age = roll_abilities.multi_die(1, 4) + 18
        elif self.char_class == "Druid":
            if "Elf" in self.race:
                self.age = roll_abilities.multi_die(8, 10) + 500
            elif "Gnome" in self.race:
                self.age = roll_abilities.multi_die(1, 12) + 300
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(2, 4) + 40
            elif self.race == "Halfling":
                self.age = roll_abilities.multi_die(1, 4) + 38
            else:
                self.age = roll_abilities.multi_die(1, 4) + 18
        elif self.char_class == "Mystic":
            if "Elf" in self.race:
                self.age = roll_abilities.multi_die(9, 10) + 500
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(1, 4) + 40
            elif self.race == "Halfling":
                self.age = roll_abilities.multi_die(1, 4) + 38
            else:
                self.age = roll_abilities.multi_die(1, 4) + 18
        elif self.char_class == "Fighter":
            if "Dwarf" in self.race:
                self.age = roll_abilities.multi_die(5, 4) + 40
            elif "Elf" in self.race:
                self.age = roll_abilities.multi_die(5, 6) + 130
            elif "Gnome" in self.race:
                self.age = roll_abilities.multi_die(5, 4) + 60
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(3, 4) + 22
            elif self.race == "Halfling":
                self.age = roll_abilities.multi_die(3, 4) + 20
            elif self.race == "Half-Orc":
                self.age = roll_abilities.multi_die(1, 4) + 13
            else:
                self.age = roll_abilities.multi_die(1, 4) + 15
        elif self.char_class == "Barbarian":
            self.age = roll_abilities.multi_die(1, 4) + 14
        elif self.char_class == "Ranger":
            if "Elf" in self.race:
                self.age = roll_abilities.multi_die(3, 8) + 160
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(2, 6) + 30
            else:
                self.age = roll_abilities.multi_die(1, 4) + 20
        elif self.char_class == "Mage":
            if "Elf" in self.race:
                self.age = roll_abilities.multi_die(3, 6) + 150
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(2, 8) + 30
            else:
                self.age = roll_abilities.multi_die(2, 8) + 24
        elif self.char_class == "Illusionist":
            if "Gnome" in self.char_class:
                self.age = roll_abilities.multi_die(2, 12) + 100
            else:
                self.age = roll_abilities.multi_die(1, 6) + 30
        elif self.char_class == "Savant":
            if "Elf" in self.char_class:
                self.age = roll_abilities.multi_die(3, 8) + 180
            elif "Gnome" in self.char_class:
                self.age = roll_abilities.multi_die(3, 12) + 100
            elif self.char_class == "Half-Elf":
                self.age = roll_abilities.multi_die(3, 6) + 34
            else:
                self.age = roll_abilities.multi_die(2, 6) + 28
        elif self.char_class == "Thief" or self.char_class == "Thief-Acrobat" or self.char_class == "Mountebank":
            if "Dwarf" in self.race:
                self.age = roll_abilities.multi_die(3, 6) + 75
            elif "Elf" in self.race:
                self.age = roll_abilities.multi_die(5, 6) + 100
            elif "Gnome" in self.race:
                self.age = roll_abilities.multi_die(5, 4) + 80
            elif self.race == "Half-Elf":
                self.age = roll_abilities.multi_die(3, 8) + 22
            elif self.race == "Halfling":
                self.age = roll_abilities.multi_die(2, 4) + 40
            elif self.race == "Half-Orc":
                self.age = roll_abilities.multi_die(2, 4) + 20
            else:
                self.age = roll_abilities.multi_die(1, 4) + 18
    def finished(self):
        """Actions performed when 'Finish' button is clicked"""
        char_class, char_2nd_class, char_3rd_class = self.get_classes()

        wizard_save_name: str = self.char_name.text()
        char_vals: dict[str | Any, str | Any] = {
            "char_name": self.char_name.text(),
            "char_str": int(self.strength.text()),
            "char_bonus_str": int(self.bonus_strength.text()),
            "char_dex": int(self.dex.text()),
            "char_wis": int(self.wis.text()),
            "char_iq": int(self.iq.text()),
            "char_chr": int(self.chr.text()),
            "char_con": int(self.con.text()),
            "char_race": self.get_race(),
            "char_class": char_class,
            "char_2nd_class": char_2nd_class,
            "char_3rd_class": char_3rd_class,
            "char_social_class": self.social_class
        }
        save_dir = Path(Path.home().joinpath("Adv_Dark_Deep").joinpath("Characters"))
        Path.mkdir(save_dir, parents=True, exist_ok=True)
        wizard_character = save_dir.joinpath(wizard_save_name)
        with open(f"{wizard_character}", "wb") as save_file:
            pickle.dump(char_vals, save_file)


app = QApplication(sys.argv)
w = Wizard()
if __name__ == "__main__":
    app.exec_()
