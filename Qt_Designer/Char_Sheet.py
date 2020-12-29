import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from ADD_Char_Sheet import Ui_MainWindow
from Adv_Dark_Deep.Char_Creation import roll_abilities


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

        # Character sheet inputs
        self.char_name = self.Char_Name_lineEdit
        self.char_race = self.Race_comboBox
        self.char_multi_class = self.Multi_Class_checkBox
        self.char_dual_class = self.Dual_Class_checkBox
        self.char_class = self.Class_comboBox
        self.char_2nd_class = self.Second_Class_comboBox
        self.char_3rd_class = self.Third_Class_comboBox
        self.char_align = self.Alignment_comboBox
        self.char_age = self.Age_spinBox
        self.char_gender = self.Gender_comboBox
        self.char_social_class = self.Social_Class_comboBox
        self.char_height = self.Height_spinBox
        self.char_weight = self.Weight_spinBox

        # Character sheet outputs
        self.strength = self.STR_Output_label
        self.dex = self.Dex_Output_label
        self.iq = self.IQ_Output_label
        self.wis = self.Wisdom_Output_label
        self.con = self.CON_Output_label
        self.chr = self.CHR_Output_label

        # Actions
        self.action3d6.triggered.connect(lambda: self.roll_stats("3d6"))
        self.action4d6_drop_lowest.triggered.connect(lambda: self.roll_stats("4d6"))
        self.action2d6_6.triggered.connect(lambda: self.roll_stats("2d6"))

    def roll_stats(self, roll_type):
        """
        Clicking the menu option will generate new stats for the character and populate default data in the sheet.
        """
        try:
            if roll_type == "2d6":
                rolls = roll_abilities.two_d6_plus_6()
                strength, dex, iq, wis, con, chr = [str(rolls[i]) for i in range(6)]
                self.strength.setText(strength)
                self.dex.setText(dex)
                self.iq.setText(iq)
                self.wis.setText(wis)
                self.con.setText(con)
                self.chr.setText(chr)
            if roll_type == "3d6":
                rolls = roll_abilities.three_d6()
                strength, dex, iq, wis, con, chr = [str(rolls[i]) for i in range(6)]
                self.strength.setText(strength)
                self.dex.setText(dex)
                self.iq.setText(iq)
                self.wis.setText(wis)
                self.con.setText(con)
                self.chr.setText(chr)
            if roll_type == "4d6":
                rolls = roll_abilities.four_d6_drop_lowest()
                strength, dex, iq, wis, con, chr = [str(rolls[i]) for i in range(6)]
                self.strength.setText(strength)
                self.dex.setText(dex)
                self.iq.setText(iq)
                self.wis.setText(wis)
                self.con.setText(con)
                self.chr.setText(chr)
            else:
                raise ValueError
        except ValueError:
            print("Invalid roll type")



app = QApplication(sys.argv)
w = MainWindow()
if __name__ == "__main__":
    app.exec_()
