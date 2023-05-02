import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWizard, QPushButton, QButtonGroup, QLineEdit, QLabel, QGroupBox, \
    QRadioButton, QGridLayout, QWizardPage, QWidget

import Adv_Dark_Deep
from New_Char_Wizard import Ui_Wizard
from Adv_Dark_Deep.Char_Creation import roll_abilities, get_acceptable_class, class_min_attribs, race_vs_attribs


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

        self.multi = None

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
        self.race = self.Race_groupBox
        self.prime_class = self.First_Class_groupBox
        self.second_class = self.Second_Class_groupBox
        self.third_class = self.Third_Class_groupBox

        # Buttons
        self.roll_dice.clicked.connect(self.roll_attribs)
        self.button(QWizard.FinishButton).clicked.connect(self.finished)
        self.button(QWizard.NextButton).clicked.connect(self.confirm_page)
        self.button(QWizard.BackButton).clicked.connect(self.confirm_page)
        # self.button(QWizard.NextButton).clicked.connect(self.possible_classes)

    def confirm_page(self):
        """Check for current Wizard page and apply appropriate method"""
        if self.currentId() == 1:
            self.populate_races()
        elif self.currentId() == 2:
            self.possible_classes()
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
        if self.Male_radioButton.isChecked():
            return "Male"
        else:
            return "Female"

    def populate_races(self):
        """Enable appropriate radio buttons for available races, based on attributes and gender"""
        races = race_vs_attribs.get_acceptable_race(self.get_gender(), int(self.strength.text()), int(self.iq.text()),
                                                    int(self.wis.text()), int(self.dex.text()), int(self.con.text()),
                                                    int(self.chr.text()))
        if "Dwarf, Hill" in races:
            self.Dwarf_Hill_radioButton.setEnabled(True)
        if "Dwarf, Grey (Duergar)" in races:
            self.Dwarf_Gray_radioButton.setEnabled(True)
        if "Dwarf, Mountain" in races:
            self.Dwarf_Mountain_radioButton.setEnabled(True)
        if "Elf, Dark (Drow)" in races:
            self.Elf_Dark_radioButton.setEnabled(True)
        if "Elf, Grey" in races:
            self.Elf_Gray_radioButton.setEnabled(True)
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

    def get_race(self):
        """Get the selected race radiobutton"""
        return self.race

    def possible_classes(self):
        """Determine which classes the character is eligible for, based on previous selections"""
        # TODO: Have a check to ensure that the attributes are rolled
        print(self.race)
        # print(get_acceptable_class.get_one_class(self.get_race()))
        # print(Adv_Dark_Deep.Char_Creation.get_acceptable_class.get_one_class(self.get_race()))
        # new_list = []
        # try:
        #     if (self.get_race() == "Dwarf, Hill" or self.get_race() == "Dwarf, Mountain" or
        #             self.get_race() == "Dwarf, Grey"):
        #         race_class = race_vs_classes.multi_class["dwarf"]
        #         self.multi = 1
        #     else:
        #         race_class = race_vs_classes.multi_class[self.get_race().lower()]
        #         self.multi = 1
        # except KeyError:  # Error indicates not multi-class eligible
        #     race_class = race_vs_classes.single_class[self.get_race().lower()]
        #     self.multi = 0
        # new_list = list(race_class)
        #
        # try:
        #     if int(self.dex.text()) < class_min_attribs.bard["dex"] or \
        #             int(self.chr.text()) < class_min_attribs.bard["chr"]:
        #         new_list.remove("Bard")
        #     if int(self.iq.text()) < class_min_attribs.jester["iq"] or \
        #             int(self.dex.text()) < class_min_attribs.jester["dex"] or \
        #             int(self.chr.text()) < class_min_attribs.jester["chr"]:
        #         new_list.remove("Jester")
        #     if int(self.strength.text()) < class_min_attribs.cavalier["str"] or \
        #             int(self.dex.text()) < class_min_attribs.cavalier["dex"] or \
        #             int(self.con.text()) < class_min_attribs.cavalier["con"] or \
        #             int(self.iq.text()) < class_min_attribs.cavalier["iq"] or \
        #             int(self.wis.text()) < class_min_attribs.cavalier["wis"]:
        #         new_list.remove("Cavalier")
        #     if int(self.strength.text()) < class_min_attribs.paladin["str"] or \
        #             int(self.dex.text()) < class_min_attribs.paladin["dex"] or \
        #             int(self.con.text()) < class_min_attribs.paladin["con"] or \
        #             int(self.iq.text()) < class_min_attribs.paladin["iq"] or \
        #             int(self.wis.text()) < class_min_attribs.paladin["wis"] or \
        #             int(self.chr.text()) < class_min_attribs.paladin["chr"]:
        #         new_list.remove("Paladin")
        #     if int(self.wis.text()) < class_min_attribs.cleric["wis"]:
        #         new_list.remove("Cleric")
        #     if int(self.wis.text()) < class_min_attribs.druid["wis"] or \
        #             int(self.chr.text()) < class_min_attribs.druid["chr"]:
        #         new_list.remove("Druid")
        #     if int(self.wis.text()) < class_min_attribs.mystic["wis"] or \
        #             int(self.dex.text()) < class_min_attribs.mystic["dex"]:
        #         new_list.remove("Mystic")
        #     if int(self.strength.text()) < class_min_attribs.fighter["str"] or \
        #             int(self.con.text()) < class_min_attribs.fighter["con"]:
        #         new_list.remove("Fighter")
        #     if int(self.strength.text()) < class_min_attribs.barbarian["str"] or \
        #             int(self.dex.text()) < class_min_attribs.barbarian["dex"] or \
        #             int(self.con.text()) < class_min_attribs.barbarian["con"] or \
        #             int(self.wis.text()) >= class_min_attribs.barbarian["wis"]:
        #         new_list.remove("Barbarian")
        #     if int(self.iq.text()) < class_min_attribs.ranger["iq"] or \
        #             int(self.wis.text()) < class_min_attribs.ranger["wis"] or \
        #             int(self.con.text()) < class_min_attribs.ranger["con"]:
        #         new_list.remove("Ranger")
        #     if int(self.iq.text()) < class_min_attribs.mage["iq"] or \
        #             int(self.dex.text()) < class_min_attribs.mage["dex"]:
        #         new_list.remove("Mage")
        #     if int(self.dex.text()) < class_min_attribs.illusionist["dex"] or \
        #             int(self.iq.text()) < class_min_attribs.illusionist["iq"]:
        #         new_list.remove("Illusionist")
        #     if int(self.iq.text()) < class_min_attribs.savant["iq"] or \
        #             int(self.wis.text()) < class_min_attribs.savant["wis"]:
        #         new_list.remove("Savant")
        #     if int(self.dex.text()) < class_min_attribs.thief["dex"]:
        #         new_list.remove("Thief")
        #     if int(self.strength.text()) < class_min_attribs.thief_acrobat["str"] or \
        #             int(self.dex.text()) < class_min_attribs.thief_acrobat["dex"]:
        #         new_list.remove("Thief-Acrobat")
        #     if int(self.dex.text()) < class_min_attribs.mountebank["dex"] or \
        #             int(self.iq.text()) < class_min_attribs.mountebank["iq"] or \
        #             int(self.chr.text()) < class_min_attribs.mountebank["chr"]:
        #         new_list.remove("Mountebank")
        #     if int(self.strength.text()) < class_min_attribs.assassin["str"] or \
        #             int(self.dex.text()) < class_min_attribs.assassin["dex"] or \
        #             int(self.iq.text()) < class_min_attribs.assassin["iq"]:
        #         new_list.remove("Assassin")
        # except ValueError:
        # pass

        # self.enable_classes(new_list)

    def enable_classes(self, classes):
        """Enable radio button associated with authorized classes"""
        print(self.race.checkedButton().text())
        if self.race.checkedButton().text() == "Human":
            multi = 0
        else:
            multi = 1
        print(multi)
        # TODO: Figure out how to not brute-force this
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
        if self.multi == 1:
            print(classes)
            for item in classes:
                if "Fighter" in item[1]:
                    print(item[1])
                    self.Fighter_radioButton_5.setEnabled(True)
            # for item in classes:
            #     print(item)
            #     if "Bard" in item[0]:
            #         self.Bard_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Bard_radioButton.setEnabled(False)
            #     elif "Jester" in item[0]:
            #         self.Jester_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Jester_radioButton.setEnabled(False)
            #     elif "Cavalier" in item[0]:
            #         self.Cavalier_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Cavalier_radioButton.setEnabled(False)
            #     elif "Paladin" in item[0]:
            #         self.Paladin_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Paladin_radioButton.setEnabled(False)
            #     elif "Cleric" in item[0]:
            #         self.Cleric_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Cleric_radioButton.setEnabled(False)
            #     elif "Druid" in item[0]:
            #         self.Druid_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Druid_radioButton.setEnabled(False)
            #     elif "Mystic" in item[0]:
            #         self.Mystic_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Mystic_radioButton.setEnabled(False)
            #     elif "Fighter" in item[0]:
            #         self.Fighter_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Fighter_radioButton.setEnabled(False)
            #     elif "Barbarian" in item[0]:
            #         self.Barbarian_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Barbarian_radioButton.setEnabled(False)
            #     elif "Ranger" in item[0]:
            #         self.Ranger_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Ranger_radioButton.setEnabled(False)
            #     elif "Mage" in item[0]:
            #         self.Mage_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Mage_radioButton.setEnabled(False)
            #     elif "Illusionist" in item[0]:
            #         self.Illusionist_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Illusionist_radioButton.setEnabled(False)
            #     elif "Savant" in item[0]:
            #         self.Savant_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Savant_radioButton.setEnabled(False)
            #     elif "Thief" in item[0]:
            #         self.Thief_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Thief_radioButton.setEnabled(False)
            #     elif "Thief-Acrobat" in item[0]:
            #         self.Thief_Acrobat_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Thief_Acrobat_radioButton.setEnabled(False)
            #     elif "Mountebank" in item[0]:
            #         self.Mountebank_radioButton.setEnabled(True)
            #     # else:
            #     #     self.Mountebank_radioButton.setEnabled(False)
            #     elif "Assassin" in item[0]:
            #         self.Assassin_radioButton.setEnabled(True)
            # else:
            #     self.Assassin_radioButton.setEnabled(False)

            # if "Bard" in item[1]:
            #     self.Bard_radioButton_2.setEnabled(True)
            # if "Jester" in item[1]:
            #     self.Jester_radioButton_2.setEnabled(True)
            # if "Cavalier" in item[1]:
            #     self.Cavalier_radioButton_2.setEnabled(True)
            # if "Paladin" in item[1]:
            #     self.Paladin_radioButton_2.setEnabled(True)
            # if "Cleric" in item[1]:
            #     self.Cleric_radioButton_2.setEnabled(True)
            # if "Druid" in item[1]:
            #     self.Druid_radioButton_2.setEnabled(True)
            # if "Mystic" in item[1]:
            #     self.Mystic_radioButton_2.setEnabled(True)
            # if "Fighter" in item[1]:
            #     self.Fighter_radioButton_2.setEnabled(True)
            # if "Barbarian" in item[1]:
            #     self.Barbarian_radioButton_2.setEnabled(True)
            # if "Ranger" in item[1]:
            #     self.Ranger_radioButton_2.setEnabled(True)
            # if "Mage" in item[1]:
            #     self.Mage_radioButton_2.setEnabled(True)
            # if "Illusionist" in item[1]:
            #     self.Illusionist_radioButton_2.setEnabled(True)
            # if "Savant" in item[1]:
            #     self.Savant_radioButton_2.setEnabled(True)
            # if "Thief" in item[1]:
            #     self.Thief_radioButton_2.setEnabled(True)
            # if "Thief-Acrobat" in item[1]:
            #     self.Thief_Acrobat_radioButton_2.setEnabled(True)
            # if "Mountebank" in item[1]:
            #     self.Mountebank_radioButton_2.setEnabled(True)
            # if "Assassin" in item[1]:
            #     self.Assassin_radioButton_2.setEnabled(True)
            #
            # try:
            #     if item[2]:
            #         if "Bard" in item[2]:
            #             self.Bard_radioButton_3.setEnabled(True)
            #         if "Jester" in item[2]:
            #             self.Jester_radioButton_3.setEnabled(True)
            #         if "Cavalier" in item[2]:
            #             self.Cavalier_radioButton_3.setEnabled(True)
            #         if "Paladin" in item[2]:
            #             self.Paladin_radioButton_3.setEnabled(True)
            #         if "Cleric" in item[2]:
            #             self.Cleric_radioButton_3.setEnabled(True)
            #         if "Druid" in item[2]:
            #             self.Druid_radioButton_3.setEnabled(True)
            #         if "Mystic" in item[2]:
            #             self.Mystic_radioButton_3.setEnabled(True)
            #         if "Fighter" in item[2]:
            #             self.Fighter_radioButton_3.setEnabled(True)
            #         if "Barbarian" in item[2]:
            #             self.Barbarian_radioButton_3.setEnabled(True)
            #         if "Ranger" in item[2]:
            #             self.Ranger_radioButton_3.setEnabled(True)
            #         if "Mage" in item[2]:
            #             self.Mage_radioButton_3.setEnabled(True)
            #         if "Illusionist" in item[2]:
            #             self.Illusionist_radioButton_3.setEnabled(True)
            #         if "Savant" in item[2]:
            #             self.Savant_radioButton_3.setEnabled(True)
            #         if "Thief" in item[2]:
            #             self.Thief_radioButton_3.setEnabled(True)
            #         if "Thief-Acrobat" in item[2]:
            #             self.Thief_Acrobat_radioButton_3.setEnabled(True)
            #         if "Mountebank" in item[2]:
            #             self.Mountebank_radioButton_3.setEnabled(True)
            #         if "Assassin" in item[2]:
            #             self.Assassin_radioButton_3.setEnabled(True)
            # except IndexError:
            #     pass

    def finished(self):
        """Actions performed when 'Finish' button is clicked"""
        pass


app = QApplication(sys.argv)
w = Wizard()
if __name__ == "__main__":
    app.exec_()
