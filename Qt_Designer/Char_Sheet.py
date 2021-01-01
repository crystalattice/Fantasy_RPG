import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox, QComboBox, QSpinBox, QLabel

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
        self.char_multi_class: QCheckBox = self.Multi_Class_checkBox
        self.char_dual_class: QCheckBox = self.Dual_Class_checkBox
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
        self.dex: QLabel = self.Dex_Output_label
        self.iq: QLabel = self.IQ_Output_label
        self.wis: QLabel = self.Wisdom_Output_label
        self.con: QLabel = self.CON_Output_label
        self.chr: QLabel = self.CHR_Output_label

        # Actions
        self.actionNew_Character.connect(self.new_character)
        self.actionOpen_Character.connect(self.open_character)
        self.actionSave_Character.connect(self.save_character)

        self.action3d6.triggered.connect(lambda: self.roll_stats("3d6"))
        self.action4d6_drop_lowest.triggered.connect(lambda: self.roll_stats("4d6"))
        self.action2d6_6.triggered.connect(lambda: self.roll_stats("2d6"))

    # File menu
    def new_character(self):
        """Create a new character"""
        pass

    def open_character(self):
        """Open an existing character"""
        pass

    def save_character(self):
        """Save the current character sheet"""
        pass

    # def roll_stats(self, roll_type):
    #     """Clicking the menu option will generate new stats for the character and populate default data in the sheet."""
    #     try:
    #         if roll_type == "2d6":
    #             rolls = roll_abilities.two_d6_plus_6()
    #             strength, dex, iq, wis, con, chr = [str(rolls[i]) for i in range(6)]
    #             self.strength.setText(strength)
    #             self.dex.setText(dex)
    #             self.iq.setText(iq)
    #             self.wis.setText(wis)
    #             self.con.setText(con)
    #             self.chr.setText(chr)
    #         if roll_type == "3d6":
    #             rolls = roll_abilities.three_d6()
    #             strength, dex, iq, wis, con, chr = [str(rolls[i]) for i in range(6)]
    #             self.strength.setText(strength)
    #             self.dex.setText(dex)
    #             self.iq.setText(iq)
    #             self.wis.setText(wis)
    #             self.con.setText(con)
    #             self.chr.setText(chr)
    #         if roll_type == "4d6":
    #             rolls = roll_abilities.four_d6_drop_lowest()
    #             strength, dex, iq, wis, con, chr = [str(rolls[i]) for i in range(6)]
    #             self.strength.setText(strength)
    #             self.dex.setText(dex)
    #             self.iq.setText(iq)
    #             self.wis.setText(wis)
    #             self.con.setText(con)
    #             self.chr.setText(chr)
    #         else:
    #             raise ValueError
    #     except ValueError:
    #         print("Invalid roll type")

    # Saving character checks
    def get_char_name(self):
        """Assign input character name to variable"""
        try:
            if not self.char_name:
                raise ValueError
        except ValueError:
            print("You need a character name to save.")

    # Race selection and associated information
    def race_class_selection(self):
        pass


app = QApplication(sys.argv)
w = MainWindow()
if __name__ == "__main__":
    app.exec_()
