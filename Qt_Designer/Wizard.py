import sys

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWizard, QPushButton

from New_Char_Wizard import Ui_Wizard
from Adv_Dark_Deep.Char_Creation import roll_abilities


class Wizard(QWizard, Ui_Wizard):
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
        self.race = self.Char_Race_buttonGroup
        self.prime_class = self.First_Class_groupBox
        self.second_class = self.Second_Class_groupBox
        self.third_class = self.Third_Class_groupBox

        # Buttons
        self.roll_dice.clicked.connect(self.roll_attribs)
        self.button(QWizard.FinishButton).clicked.connect(self.finished)

    def roll_attribs(self):
        """Roll the dice for character attributes"""
        if self.roll_type.checkedButton().text() == "4d6, drop lowest":
            rolls = roll_abilities.four_d6_drop_lowest()
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
        elif self.roll_type.checkedButton().text() == "3d6":
            rolls = roll_abilities.three_d6()
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
        elif self.roll_type.checkedButton().text() == "2d6+6":
            rolls = roll_abilities.two_d6_plus_6()
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

    # def exceptional_str(self):
    #     """Percentile bonus for normal strength of 18"""
    #     roll = roll_abilities.multi_die(1, 100)
    #     self.bonus_str.setText(roll)

    def finished(self):
        """Actions performed when 'Finish' button is clicked"""
        print(self.name.text())


app = QApplication(sys.argv)
w = Wizard()
if __name__ == "__main__":
    app.exec_()
