import pickle
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox, QComboBox, QSpinBox, QLabel, \
    QDialogButtonBox, QMessageBox

from ADD_Char_Sheet import Ui_MainWindow
from Adv_Dark_Deep.Char_Creation import roll_abilities, race_vs_classes


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

        # Character sheet inputs-Info tab
        self.char_name: QLineEdit = self.Char_Name_lineEdit
        self.char_race: QComboBox = self.Race_comboBox
        self.char_class: QComboBox = self.Class_comboBox
        self.char_2nd_class: QComboBox = self.Second_Class_comboBox
        self.char_3rd_class: QComboBox = self.Third_Class_comboBox
        self.char_align: QComboBox = self.Alignment_comboBox
        self.char_age: QSpinBox = self.Age_spinBox
        self.char_gender: QComboBox = self.Gender_comboBox
        self.char_social_class: QComboBox = self.Social_Class_comboBox
        self.char_height: QSpinBox = self.Height_spinBox
        self.char_weight: QSpinBox = self.Weight_spinBox

        # Character sheet outputs
        self.strength: QLabel = self.STR_Output_label
        self.bonus_strength: QLabel = self.Exceptional_Output_label
        self.dex: QLabel = self.Dex_Output_label
        self.iq: QLabel = self.IQ_Output_label
        self.wis: QLabel = self.Wisdom_Output_label
        self.con: QLabel = self.CON_Output_label
        self.chr: QLabel = self.CHR_Output_label

        # Actions
        # self.actionNew_Character.connect(self.new_character)
        self.actionOpen_Character.triggered.connect(self.open_character)
        self.actionSave_Character.triggered.connect(self.save_character)

        self.action3d6.triggered.connect(self.roll_3d6)
        self.action4d6_drop_lowest.triggered.connect(self.roll_4d6)
        self.action2d6_6.triggered.connect(self.roll_2d6)

    # File menu
    def new_character(self):
        """Create a new character"""
        pass

    def open_character(self):
        """Open an existing character"""
        with open("bob", "rb") as character:
            unpickle = pickle.load(character)
            self.strength.setText(unpickle["str"])
            self.bonus_strength.setText(unpickle["char_exp_str"])
            self.dex.setText(unpickle["char_dex"])
            self.wis.setText(unpickle["char_wis"])
            self.iq.setText(unpickle["char_iq"])
            self.chr.setText(unpickle["char_chr"])
            self.con.setText(unpickle["char_con"])

    def save_character(self):
        """Save the current character sheet"""
        save_name = self.get_char_name()
        char_vals = {
            "str": self.strength.text(),
            "char_exp_str": self.bonus_strength.text(),
            "char_dex": self.dex.text(),
            "char_wis": self.wis.text(),
            "char_iq": self.iq.text(),
            "char_chr": self.chr.text(),
            "char_con": self.con.text(),
            "race": self.race_selection(),
            "class": self.class_selection(),
            "second_class": self.dual_class_selection(),
            "third_class": self.third_class_selection(),
            "alignment": self.alignment_selection(),
            "age": self.get_age(),
            "gender": self.get_gender(),
            "social_class": self.get_social_class(),
            "height": self.get_height(),
            "weight": self.get_weight(),
        }
        if not "str":  # Assume no attributes created
            no_attribs_msg = QMessageBox()
            no_attribs_msg.setWindowTitle("Missing Attributes")
            no_attribs_msg.setText("You must roll for attributes prior to saving.\n"
                                   "Character not saved.")
            no_attribs_msg.setIcon(QMessageBox.Icon.Warning)
            button = no_attribs_msg.exec()
            button = QMessageBox.StandardButtons(button)
        if not save_name:
            no_name_msg = QMessageBox()
            no_name_msg.setWindowTitle("Missing Character Name")
            no_name_msg.setText("You must provide a character name prior to saving.\n"
                                "Character not saved.")
            no_name_msg.setIcon(QMessageBox.Icon.Warning)
            button = no_name_msg.exec()
            button = QMessageBox.StandardButtons(button)
        else:
            # with open(f"{save_name}", "wb") as save_file:
            #     pickle.dump(char_vals, save_file)
            # TODO: remove after testing
            # with open(f"{save_name}", "rb") as open_file:
            #     print(pickle.load(save_file))
            print(char_vals)

    def roll_3d6(self):
        rolls: list = roll_abilities.three_d6()
        self.insert_rolls(rolls)

    def roll_4d6(self):
        rolls: list = roll_abilities.four_d6_drop_lowest()
        self.insert_rolls(rolls)

    def roll_2d6(self):
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
        # TODO: Add check to overwrite attribs
        # if self.strength.text():
        #     existing_attribs_msg = QMessageBox()
        #     existing_attribs_msg.setWindowTitle("Existing Attributes")
        #     existing_attribs_msg.setText("Your character already has attributes. Are you sure you want to reroll?")
        #     existing_attribs_msg.setIcon(QMessageBox.Icon.Warning)
        #     button = existing_attribs_msg.exec()
        #     button = QMessageBox.StandardButtons(button)
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

    # TODO: Consider making the following into properties
    # Saving character checks
    def get_char_name(self):
        """Assign input character name to variable"""
        return self.char_name.text()

    # Race selection and associated information
    # TODO: Check attributes vs. race limits
    def race_selection(self):
        """Get the character's race"""
        return self.char_race.currentText()

    # TODO: Check attributes vs. class mins
    def class_selection(self):
        """Get the character's class"""
        return self.char_class.currentText()

    def dual_class_selection(self):
        """If dual classed, get second class"""
        if self.Second_Class_comboBox.currentText() != "None":
            return self.Second_Class_comboBox.currentText()

    def third_class_selection(self):
        """If multi-classed, get third class"""
        if self.Second_Class_comboBox.currentText() == "None" and self.Third_Class_comboBox.currentText() != "None":
            multi_class_msg = QMessageBox()
            multi_class_msg.setWindowTitle("Invalid Classes")
            multi_class_msg.setText("Your character cannot have a third class without having a second class.\n"
                                    "Character not saved.")
            multi_class_msg.setIcon(QMessageBox.Icon.Warning)
            button = multi_class_msg.exec()
            button = QMessageBox.StandardButtons(button)
        else:
            if self.Third_Class_comboBox.currentText() != "None":
                return self.Third_Class_comboBox.currentText()

    def alignment_selection(self):
        """Get character's alignment"""
        return self.Alignment_comboBox.currentText()

    def get_age(self):
        """Get character's age"""
        return self.Age_spinBox.text()

    def get_gender(self):
        """Get character's gender"""
        return self.Gender_comboBox.currentText()

    def get_social_class(self):
        """Get character's social class"""
        return self.Social_Class_comboBox.currentText()

    def get_height(self):
        """Get character's height"""
        return self.Height_spinBox.text()

    def get_weight(self):
        """Get character's weight"""
        return self.Weight_spinBox.text()


app = QApplication(sys.argv)
w = MainWindow()
if __name__ == "__main__":
    app.exec_()
