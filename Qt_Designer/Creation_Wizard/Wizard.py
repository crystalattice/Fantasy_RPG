import pickle
import random
import sys
from pathlib import Path
from typing import Tuple

from PyQt5.QtWidgets import QApplication, QWizard, QPushButton, QButtonGroup, QLineEdit, QLabel, QMessageBox

from Adv_Dark_Deep.Char_Creation import roll_abilities, get_acceptable_class, race_vs_attribs, con_abilities
from New_Char_Wizard import Ui_Wizard


class Wizard(QWizard, Ui_Wizard):
    age: int
    hp: int
    money: int
    social_class: str
    classes: tuple
    multi: bool
    gender: QButtonGroup
    char_3rd_class: str
    char_2nd_class: str
    char_class: str
    race: str
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        self.char_class = ""
        self.char_2nd_class = ""
        self.char_3rd_class = ""
        self.social_class = ""
        self.money = 0
        self.hp = 0
        self.age = 0
        self.height = 0
        self.weight = 0
        self.alignment = ""

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

    def roll_attribs(self) -> None:
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

    def insert_rolls(self, rolls) -> None:
        """Put the attribute rolls into their respective variables"""
        strength: str
        bonus_strength: str
        dex: str
        iq: str
        wis: str
        con: str
        charisma: str
        strength, dex, iq, wis, con, charisma = [str(rolls[i]) for i in range(6)]
        if strength == "18":
            self.bonus_strength.setText(str(roll_abilities.multi_die(1, 100)))
        else:
            self.bonus_strength.setText("0")
        self.strength.setText(strength)
        self.dex.setText(dex)
        self.iq.setText(iq)
        self.wis.setText(wis)
        self.con.setText(con)
        self.chr.setText(charisma)

    def get_gender(self) -> str:
        """Get the selected gender radiobutton"""
        return self.Gender_buttonGroup.checkedButton().text()

    def populate_races(self) -> None:
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
            races: list = race_vs_attribs.get_acceptable_race(self.get_gender(),
                                                              int(self.strength.text()),
                                                              int(self.iq.text()),
                                                              int(self.wis.text()),
                                                              int(self.dex.text()),
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

    def get_race(self) -> str:
        """Get the selected race radiobutton"""
        return self.Race_buttonGroup.checkedButton().text()

    def enable_classes(self) -> None:
        """Enable radio button associated with authorized classes"""
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

    def multi_class(self) -> None:
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

    def get_classes(self) -> None:
        """Get the primary and multi-classes, if available"""
        self.char_class = self.First_Class_buttonGroup.checkedButton().text()
        if self.multi is True:
            self.char_2nd_class = self.Second_Class_buttonGroup.checkedButton().text()
            self.char_3rd_class = self.Third_Class_buttonGroup.checkedButton().text()
        else:
            self.char_2nd_class = ""
            self.char_3rd_class = ""

    def starting_hp(self) -> None:
        """Calculate starting hit points"""
        hp = 0
        if self.char_class == "Bard" or self.char_class == "Jester" or self.char_class == "Mystic" \
                or self.char_class == "Thief" or self.char_class == "Thief-Acrobat" or self.char_class == "Mountebank" \
                or self.char_class == "Assassin":
            hp = 6
        elif self.char_class == "Cavalier" or self.char_class == "Paladin" or self.char_class == "Fighter":
            hp = 10
        elif self.char_class == "Cleric" or self.char_class == "Druid":
            hp = 8
        elif self.char_class == "Barbarian":
            hp = 12
        elif self.char_class == "Ranger":
            hp = 16
        elif self.char_class == "Mage" or self.char_class == "Illusionist" or self.char_class == "Savant":
            hp = 4
        hp_bonus = con_abilities.get_con_ability(int(self.con.text()), 0)
        self.hp = hp + hp_bonus

    def starting_money(self) -> None:
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

    def social_class(self) -> None:
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

    def initial_age(self) -> None:
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

    def initial_height(self) -> None:
        """Calculate character's height"""
        race = self.get_race()
        roll = roll_abilities.multi_die(1, 100)

        if race == "Dwarf, Grey (Duergar)":
            if self.gender == "Male":
                if 1 <= roll <= 4:
                    self.height = 44
                elif 5 <= roll <= 15:
                    self.height = 45
                elif 16 <= roll <= 26:
                    self.height = 46
                elif 27 <= roll <= 37:
                    self.height = 47
                elif 38 <= roll <= 60:
                    self.height = 48
                elif 61 <= roll <= 71:
                    self.height = 49
                elif 72 <= roll <= 81:
                    self.height = 50
                elif 82 <= roll <= 91:
                    self.height = 51
                elif 92 <= roll <= 94:
                    self.height = 52
                elif 95 <= roll <= 97:
                    self.height = 53
                else:
                    self.height = 54
            else:  # Female
                if 1 <= roll <= 4:
                    self.height = 42
                elif 5 <= roll <= 15:
                    self.height = 43
                elif 16 <= roll <= 26:
                    self.height = 44
                elif 27 <= roll <= 37:
                    self.height = 45
                elif 38 <= roll <= 59:
                    self.height = 46
                elif 60 <= roll <= 71:
                    self.height = 47
                elif 72 <= roll <= 83:
                    self.height = 48
                elif 84 <= roll <= 95:
                    self.height = 49
                else:
                    self.height = 50
        elif self.race == "Dwarf, Hill":
            if self.gender == "Male":
                if 1 <= roll <= 15:
                    self.height = 48 - roll_abilities.multi_die(1, 4)
                elif 16 <= roll <= 36:
                    self.height = 48 - roll_abilities.multi_die(1, 3)
                elif 37 <= roll <= 59:
                    self.height = 48
                elif 60 <= roll <= 80:
                    self.height = 48 + roll_abilities.multi_die(1, 3)
                else:
                    self.height = 48 + roll_abilities.multi_die(1, 6)
            else:  # Female
                if 1 <= roll <= 15:
                    self.height = 46 - roll_abilities.multi_die(1, 4)
                elif 16 <= roll <= 36:
                    self.height = 46 - roll_abilities.multi_die(1, 3)
                elif 37 <= roll <= 59:
                    self.height = 46
                elif 60 <= roll <= 80:
                    self.height = 46 + roll_abilities.multi_die(1, 3)
                else:
                    self.height = 46 + roll_abilities.multi_die(1, 4)
        elif self.race == "Dwarf, Mountain":
            if self.gender == "Male":
                if 1 <= roll <= 15:
                    self.height = 54 - roll_abilities.multi_die(1, 4)
                elif 16 <= roll <= 36:
                    self.height = 54 - roll_abilities.multi_die(1, 3)
                elif 37 <= roll <= 59:
                    self.height = 54
                elif 60 <= roll <= 80:
                    self.height = 54 + roll_abilities.multi_die(1, 3)
                else:
                    self.height = 54 + roll_abilities.multi_die(1, 6)
            else:  # Female
                if 1 <= roll <= 15:
                    self.height = 52 - roll_abilities.multi_die(1, 4)
                elif 16 <= roll <= 36:
                    self.height = 52 - roll_abilities.multi_die(1, 3)
                elif 37 <= roll <= 59:
                    self.height = 52
                elif 60 <= roll <= 80:
                    self.height = 52 + roll_abilities.multi_die(1, 3)
                else:
                    self.height = 52 + roll_abilities.multi_die(1, 6)
        elif self.race == "Elf, Dark (Drow)":
            if self.gender == "Male":
                if 1 <= roll <= 31:
                    self.height = 60 - roll_abilities.multi_die(1, 4)
                elif 32 <= roll <= 59:
                    self.height = 60
                elif 60 <= roll <= 80:
                    self.height = 60 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 60 + roll_abilities.multi_die(1, 6)
            else:
                if 1 <= roll <= 10:
                    self.height = 54 - roll_abilities.multi_die(1, 4)
                elif 11 <= roll <= 31:
                    self.height = 54 - roll_abilities.multi_die(1, 3)
                elif 32 <= roll <= 59:
                    self.height = 54
                elif 60 <= roll <= 80:
                    self.height = 54 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 54 + roll_abilities.multi_die(1, 6)
        elif self.race == "Elf, Grey":
            if self.gender == "Male":
                if 1 <= roll <= 31:
                    self.height = 62 - roll_abilities.multi_die(1, 4)
                elif 32 <= roll <= 59:
                    self.height = 62
                elif 60 <= roll <= 80:
                    self.height = 62 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 62 + roll_abilities.multi_die(1, 6)
            else:
                if 1 <= roll <= 10:
                    self.height = 56 - roll_abilities.multi_die(1, 4)
                elif 11 <= roll <= 31:
                    self.height = 56 - roll_abilities.multi_die(1, 3)
                elif 32 <= roll <= 59:
                    self.height = 56
                elif 60 <= roll <= 80:
                    self.height = 56 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 56 + roll_abilities.multi_die(1, 6)
        elif self.race == "Half-Elf":
            if self.gender == "Male":
                if 1 <= roll <= 35:
                    self.height = 66 - roll_abilities.multi_die(1, 6)
                elif 36 <= roll <= 50:
                    self.height = 66 - roll_abilities.multi_die(1, 4)
                elif 51 <= roll <= 64:
                    self.height = 66
                elif 65 <= roll <= 80:
                    self.height = 66 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 66 + roll_abilities.multi_die(1, 6)
            else:
                if 1 <= roll <= 35:
                    self.height = 621 - roll_abilities.multi_die(1, 6)
                elif 36 <= roll <= 50:
                    self.height = 62 - roll_abilities.multi_die(1, 4)
                elif 51 <= roll <= 64:
                    self.height = 62
                elif 65 <= roll <= 80:
                    self.height = 62 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 62 + roll_abilities.multi_die(1, 6)
        elif self.race == "Elf, High":
            if self.gender == "Male":
                if 1 <= roll <= 31:
                    self.height = 60 - roll_abilities.multi_die(1, 4)
                elif 32 <= roll <= 59:
                    self.height = 60
                elif 60 <= roll <= 80:
                    self.height = 60 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 60 + roll_abilities.multi_die(1, 6)
            else:
                if 1 <= roll <= 10:
                    self.height = 54 - roll_abilities.multi_die(1, 4)
                elif 11 <= roll <= 31:
                    self.height = 54 - roll_abilities.multi_die(1, 3)
                elif 32 <= roll <= 59:
                    self.height = 54
                elif 60 <= roll <= 80:
                    self.height = 54 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 56 + roll_abilities.multi_die(1, 6)
        elif self.race == "Elf, Wild":
            if self.gender == "Male":
                if 1 <= roll <= 31:
                    self.height = 52 - roll_abilities.multi_die(1, 4)
                elif 32 <= roll <= 59:
                    self.height = 52
                elif 60 <= roll <= 80:
                    self.height = 52 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 52 + roll_abilities.multi_die(1, 6)
            else:
                if 1 <= roll <= 10:
                    self.height = 48 - roll_abilities.multi_die(1, 4)
                elif 11 <= roll <= 31:
                    self.height = 48 - roll_abilities.multi_die(1, 3)
                elif 32 <= roll <= 59:
                    self.height = 48
                elif 60 <= roll <= 80:
                    self.height = 48 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 48 + roll_abilities.multi_die(1, 6)
        elif self.race == "Elf, Wood":
            if self.gender == "Male":
                if 1 <= roll <= 31:
                    self.height = 58 - roll_abilities.multi_die(1, 4)
                elif 32 <= roll <= 59:
                    self.height = 58
                elif 60 <= roll <= 80:
                    self.height = 58 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 58 + roll_abilities.multi_die(1, 6)
            else:
                if 1 <= roll <= 10:
                    self.height = 52 - roll_abilities.multi_die(1, 4)
                elif 11 <= roll <= 31:
                    self.height = 52 - roll_abilities.multi_die(1, 3)
                elif 32 <= roll <= 59:
                    self.height = 52
                elif 60 <= roll <= 80:
                    self.height = 52 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 52 + roll_abilities.multi_die(1, 6)
        elif self.race == "Gnome, Deep (Svirfneblin)" or self.race == "Gnome, Forest" or self.race == "Gnome, Hill":
            if self.gender == "Male":
                if 1 <= roll <= 40:
                    self.height = 39 - roll_abilities.multi_die(1, 3)
                elif 41 <= roll <= 65:
                    self.height = 39
                else:
                    self.height = 39 + roll_abilities.multi_die(1, 3)
            else:
                if 1 <= roll <= 40:
                    self.height = 36 - roll_abilities.multi_die(1, 3)
                elif 41 <= roll <= 65:
                    self.height = 36
                else:
                    self.height = 36 + roll_abilities.multi_die(1, 3)
        elif self.race == "Halfling":
            if self.gender == "Male":
                if 1 <= roll <= 34:
                    self.height = 36 - roll_abilities.multi_die(1, 3)
                elif 35 <= roll <= 56:
                    self.height = 36
                elif 57 <= roll <= 90:
                    self.height = 36 + roll_abilities.multi_die(1, 3)
                else:
                    self.height = 36 + roll_abilities.multi_die(1, 6)
            else:
                if 1 <= roll <= 34:
                    self.height = 33 - roll_abilities.multi_die(1, 3)
                elif 35 <= roll <= 56:
                    self.height = 33
                else:
                    self.height = 36 + roll_abilities.multi_die(1, 3)
        elif self.race == "Half-Orc":
            if self.gender == "Male":
                if 1 <= roll <= 55:
                    self.height = 66 - roll_abilities.multi_die(1, 4)
                elif 56 <= roll <= 65:
                    self.height = 66
                else:
                    self.height = 66 + roll_abilities.multi_die(1, 4)
            else:
                if 1 <= roll <= 45:
                    self.height = 62 - roll_abilities.multi_die(1, 6)
                elif 46 <= roll <= 55:
                    self.height = 62 - roll_abilities.multi_die(1, 4)
                elif 56 <= roll <= 65:
                    self.height = 62
                elif 66 <= roll <= 75:
                    self.height = 62 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 62 + roll_abilities.multi_die(1, 8)
        else: # Human
            if self.gender == "Male":
                if 1 <= roll <= 20:
                    self.height = 72 - roll_abilities.multi_die(1, 12)
                elif 21 <= roll <= 40:
                    self.height = 72 - roll_abilities.multi_die(1, 4)
                elif 41 <= roll <= 60:
                    self.height = 72
                elif 61 <= roll <= 80:
                    self.height = 72 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 72 + roll_abilities.multi_die(1, 12)
            else:
                if 1 <= roll <= 20:
                    self.height = 66 - roll_abilities.multi_die(1, 6)
                elif 21 <= roll <= 40:
                    self.height = 66 - roll_abilities.multi_die(1, 4)
                elif 41 <= roll <= 60:
                    self.height = 66
                elif 61 <= roll <= 80:
                    self.height = 66 + roll_abilities.multi_die(1, 4)
                else:
                    self.height = 66 + roll_abilities.multi_die(1, 8)

    def initial_weight(self) -> None:
        """Calculate character's weight"""
        pass

    def get_alignment(self) -> None:
        """Get selected alignment"""
        pass

    def finished(self) -> None:
        """Actions performed when 'Finish' button is clicked"""
        wizard_save_name: str = self.char_name.text()
        char_vals: dict[str, str] = {
            "char_name": self.char_name.text(),
            "char_str": int(self.strength.text()),
            "char_bonus_str": int(self.bonus_strength.text()),
            "char_dex": int(self.dex.text()),
            "char_wis": int(self.wis.text()),
            "char_iq": int(self.iq.text()),
            "char_chr": int(self.chr.text()),
            "char_con": int(self.con.text()),
            "char_race": self.get_race(),
            "char_class": self.char_class,
            "char_2nd_class": self.char_2nd_class,
            "char_3rd_class": self.char_3rd_class,
            "char_social_class": self.social_class,
            "char_hp": self.hp,
            "char_money": self.money,
            "char_age": self.age,
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
