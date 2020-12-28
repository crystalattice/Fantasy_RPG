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

        # Character sheet outputs
        self.str = self.STR_Output_label
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
                # str, dex, iq, wis, con, chr = [rolls[i] for i in range(6)]
                self.str.setText(str(rolls[0]))
                self.dex.setText(str(rolls[1]))
                self.iq.setText(str(rolls[2]))
                self.wis.setText(str(rolls[3]))
                self.con.setText(str(rolls[4]))
                self.chr.setText(str(rolls[5]))

            elif roll_type == "3d6":
                print(roll_abilities.three_d6())
            elif roll_type == "4d6":
                print(roll_abilities.four_d6_drop_lowest())
            else:
                raise ValueError
        except ValueError:
            print("Invalid roll type")



app = QApplication(sys.argv)
w = MainWindow()
if __name__ == "__main__":
    app.exec_()
