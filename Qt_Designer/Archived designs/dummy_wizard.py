import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWizardPage, QWizard
# from PyQt5.QtCore import Qt, pyqtSlot
# from PyQt5.QtWidgets import QApplication, QWizard, QPushButton, QButtonGroup, QLineEdit, QLabel, QGroupBox, \
#     QRadioButton, QGridLayout, QWizardPage

# from New_Char_Wizard import Ui_Wizard
from Adv_Dark_Deep.Char_Creation import roll_abilities, race_vs_classes, class_min_attribs


class Wizard(QWizard, QWizardPage):
    def __init__(self):
        super().__init__(parent=None)
        Wizard.setObjectName(self, "Wizard")
        Wizard.resize(self, 775, 485)

        self.race = ""

        self.firstPage = Page1(self)
        self.secondPage = Page2(self)
        self.thirdPage = Page3(self)
        self.fourthPage = Page4(self)

        self.addPage(Page1(self))
        self.addPage(Page2(self))
        self.addPage(Page3(self))
        self.addPage(Page4(self))

        self.button(QtWidgets.QWizard.FinishButton).clicked.connect(self.finished)

    def finished(self):
        """Actions performed when 'Finish' button is clicked"""
        pass


class Page1(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent=None)

        # self.FirstPage = QtWidgets.QWizardPage()
        # self.FirstPage.setObjectName("FirstPage")
        self.setTitle("Create a New Character")
        self.setSubTitle("This wizard will walk you through creating a character. It will help "
                         "you roll your character\'s attributes, pick a race and class, and provide your "
                         "initial hit points. ")
        self.layoutWidget = QtWidgets.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 257, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.Char_name_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Char_name_label.sizePolicy().hasHeightForWidth())
        self.Char_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.Char_name_label.setFont(font)
        self.Char_name_label.setWordWrap(True)
        self.Char_name_label.setObjectName("Char_name_label")
        self.horizontalLayout.addWidget(self.Char_name_label)
        self.Char_name_label.setText("Character Name")
        self.Char_Name_Out_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Char_Name_Out_lineEdit.sizePolicy().hasHeightForWidth())
        self.Char_Name_Out_lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.Char_Name_Out_lineEdit.setFont(font)
        self.Char_Name_Out_lineEdit.setObjectName("Char_Name_Out_lineEdit")
        self.horizontalLayout.addWidget(self.Char_Name_Out_lineEdit)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 30, 641, 181))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Rolling_Options_label = QtWidgets.QLabel(self.frame)
        self.Rolling_Options_label.setGeometry(QtCore.QRect(152, 10, 352, 149))
        self.Rolling_Options_label.setWordWrap(True)
        self.Rolling_Options_label.setObjectName("Rolling_Options_label")
        self.Rolling_Options_label.setText(
            "<html><head/><body><p>Attributes can be re-rolled; they will be saved when the wizard is "
            "finished.</p><p>*4d6, minus lowest: Four dice are rolled for each attribute, with the lowest value "
            "removed each time. </p><p>*3d6: Three dice are rolled for each attribute.</p><p>*2d6+6: Two dice are "
            "rolled for each attribute, adding six to the value. </p></body></html>")

        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 136, 114))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Roll_Attribs_pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Roll_Attribs_pushButton.setObjectName("Roll_Attribs_pushButton")
        self.Roll_Attribs_pushButton.setText("Roll Attributes")

        self.verticalLayout.addWidget(self.Roll_Attribs_pushButton)
        self.Four_dice_radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.Four_dice_radioButton.setChecked(True)
        self.Four_dice_radioButton.setObjectName("Four_dice_radioButton")
        self.Dice_Type_buttonGroup = QtWidgets.QButtonGroup()
        self.Dice_Type_buttonGroup.setObjectName("Dice_Type_buttonGroup")
        self.Dice_Type_buttonGroup.addButton(self.Four_dice_radioButton)
        self.verticalLayout.addWidget(self.Four_dice_radioButton)
        self.Four_dice_radioButton.setText("4d6, drop lowest")

        self.Three_dice_radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.Three_dice_radioButton.setObjectName("Three_dice_radioButton")
        self.Dice_Type_buttonGroup.addButton(self.Three_dice_radioButton)
        self.verticalLayout.addWidget(self.Three_dice_radioButton)
        self.Three_dice_radioButton.setText("3d6")

        self.Two_dice_radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.Two_dice_radioButton.setObjectName("Two_dice_radioButton")
        self.Dice_Type_buttonGroup.addButton(self.Two_dice_radioButton)
        self.verticalLayout.addWidget(self.Two_dice_radioButton)
        self.Two_dice_radioButton.setText("2d6+6")

        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(10, 220, 644, 64))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.STR_label = QtWidgets.QLabel(self.frame_2)
        self.STR_label.setWordWrap(True)
        self.STR_label.setObjectName("STR_label")
        self.verticalLayout_2.addWidget(self.STR_label)
        self.STR_Out_label = QtWidgets.QLabel(self.frame_2)
        self.STR_Out_label.setFrameShape(QtWidgets.QFrame.Box)
        self.STR_Out_label.setText("")
        self.STR_Out_label.setObjectName("STR_Out_label")
        self.verticalLayout_2.addWidget(self.STR_Out_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.STR_label.setText("Normal Strength")
        self.Exceptional_STR_label = QtWidgets.QLabel(self.frame_2)
        self.Exceptional_STR_label.setWordWrap(True)
        self.Exceptional_STR_label.setObjectName("Exceptional_STR_label")
        self.verticalLayout_3.addWidget(self.Exceptional_STR_label)
        self.Exceptional_STR_label.setText("Exceptional Strength")
        self.STR_Out_label_2 = QtWidgets.QLabel(self.frame_2)
        self.STR_Out_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.STR_Out_label_2.setText("")
        self.STR_Out_label_2.setObjectName("STR_Out_label_2")
        self.verticalLayout_3.addWidget(self.STR_Out_label_2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.DEX_label = QtWidgets.QLabel(self.frame_2)
        self.DEX_label.setObjectName("DEX_label")
        self.verticalLayout_4.addWidget(self.DEX_label)
        self.DEX_label.setText("Dexterity")
        self.DEX_Out_label = QtWidgets.QLabel(self.frame_2)
        self.DEX_Out_label.setFrameShape(QtWidgets.QFrame.Box)
        self.DEX_Out_label.setText("")
        self.DEX_Out_label.setObjectName("DEX_Out_label")
        self.verticalLayout_4.addWidget(self.DEX_Out_label)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.IQ_label = QtWidgets.QLabel(self.frame_2)
        self.IQ_label.setObjectName("IQ_label")
        self.verticalLayout_5.addWidget(self.IQ_label)
        self.IQ_label.setText("Intelligence")
        self.IQ_Out_label = QtWidgets.QLabel(self.frame_2)
        self.IQ_Out_label.setFrameShape(QtWidgets.QFrame.Box)
        self.IQ_Out_label.setText("")
        self.IQ_Out_label.setObjectName("IQ_Out_label")
        self.verticalLayout_5.addWidget(self.IQ_Out_label)

        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.WIS_label = QtWidgets.QLabel(self.frame_2)
        self.WIS_label.setObjectName("WIS_label")
        self.verticalLayout_6.addWidget(self.WIS_label)
        self.WIS_label.setText("Wisdom")
        self.WIS_Out_label = QtWidgets.QLabel(self.frame_2)
        self.WIS_Out_label.setFrameShape(QtWidgets.QFrame.Box)
        self.WIS_Out_label.setText("")
        self.WIS_Out_label.setObjectName("WIS_Out_label")
        self.verticalLayout_6.addWidget(self.WIS_Out_label)

        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.CON_label = QtWidgets.QLabel(self.frame_2)
        self.CON_label.setObjectName("CON_label")
        self.verticalLayout_7.addWidget(self.CON_label)
        self.CON_label.setText("Constitution")
        self.CON_Out_label = QtWidgets.QLabel(self.frame_2)
        self.CON_Out_label.setFrameShape(QtWidgets.QFrame.Box)
        self.CON_Out_label.setText("")
        self.CON_Out_label.setObjectName("CON_Out_label")
        self.verticalLayout_7.addWidget(self.CON_Out_label)

        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.CHR_label = QtWidgets.QLabel(self.frame_2)
        self.CHR_label.setObjectName("CHR_label")
        self.verticalLayout_8.addWidget(self.CHR_label)
        self.CHR_label.setText("Charisma")
        self.CHR_Out_label = QtWidgets.QLabel(self.frame_2)
        self.CHR_Out_label.setFrameShape(QtWidgets.QFrame.Box)
        self.CHR_Out_label.setText("")
        self.CHR_Out_label.setObjectName("CHR_Out_label")
        self.verticalLayout_8.addWidget(self.CHR_Out_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.roll_type = self.Dice_Type_buttonGroup
        self.Roll_Attribs_pushButton.clicked.connect(self.roll_attribs)

        self.name = self.Char_Name_Out_lineEdit
        self.strength = self.STR_Out_label
        self.bonus_strength = self.STR_Out_label_2
        self.dex = self.DEX_Out_label
        self.iq = self.IQ_Out_label
        self.wis = self.WIS_Out_label
        self.con = self.CON_Out_label
        self.chr = self.CHR_Out_label

        self.registerField("dex", self.DEX_Out_label)


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




class Page2(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setTitle("Character Race & Gender")
        self.setSubTitle("Select a character race. If your game allows UnderDark races as "
                         "player characters, click the checkbox to show those races. Also, "
                         "select a gender for your character.")
        # self = QtWidgets.QWizardPage()
        # self.setObjectName("wizardPage_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.Human_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Human_radioButton.setChecked(True)
        self.Human_radioButton.setObjectName("Human_radioButton")
        self.Human_radioButton.setText("Human")
        self.Race_buttonGroup = QtWidgets.QButtonGroup()
        self.Race_buttonGroup.setObjectName("Race_buttonGroup")
        self.Race_buttonGroup.addButton(self.Human_radioButton)
        self.gridLayout.addWidget(self.Human_radioButton, 0, 0, 1, 1)

        self.Elf_Wild_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Elf_Wild_radioButton.setChecked(False)
        self.Elf_Wild_radioButton.setObjectName("Elf_Wild_radioButton")
        self.Elf_Wild_radioButton.setText("Elf, Wild")

        self.Race_buttonGroup.addButton(self.Elf_Wild_radioButton)
        self.gridLayout.addWidget(self.Elf_Wild_radioButton, 0, 1, 1, 1)
        self.Dwarf_Hill_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Dwarf_Hill_radioButton.setChecked(False)
        self.Dwarf_Hill_radioButton.setObjectName("Dwarf_Hill_radioButton")
        self.Dwarf_Hill_radioButton.setText("Dwarf, Hill")
        self.Race_buttonGroup.addButton(self.Dwarf_Hill_radioButton)
        self.gridLayout.addWidget(self.Dwarf_Hill_radioButton, 1, 0, 1, 1)

        self.Elf_Wood_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Elf_Wood_radioButton.setChecked(False)
        self.Elf_Wood_radioButton.setObjectName("Elf_Wood_radioButton")
        self.Elf_Wood_radioButton.setText("Elf, Wood")
        self.Race_buttonGroup.addButton(self.Elf_Wood_radioButton)
        self.gridLayout.addWidget(self.Elf_Wood_radioButton, 1, 1, 1, 1)

        self.Dwarf_Mountain_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Dwarf_Mountain_radioButton.setChecked(False)
        self.Dwarf_Mountain_radioButton.setObjectName("Dwarf_Mountain_radioButton")
        self.Dwarf_Mountain_radioButton.setText("Dwarf, Mountain")
        self.Race_buttonGroup.addButton(self.Dwarf_Mountain_radioButton)
        self.gridLayout.addWidget(self.Dwarf_Mountain_radioButton, 2, 0, 1, 1)

        self.Gnome_Forest_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Gnome_Forest_radioButton.setChecked(False)
        self.Gnome_Forest_radioButton.setObjectName("Gnome_Forest_radioButton")
        self.Gnome_Forest_radioButton.setText("Gnome, Forest")
        self.Race_buttonGroup.addButton(self.Gnome_Forest_radioButton)
        self.gridLayout.addWidget(self.Gnome_Forest_radioButton, 2, 1, 1, 1)

        self.Elf_Half_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Elf_Half_radioButton.setChecked(False)
        self.Elf_Half_radioButton.setObjectName("Elf_Half_radioButton")
        self.Elf_Half_radioButton.setText("Half-Elf")
        self.Race_buttonGroup.addButton(self.Elf_Half_radioButton)
        self.gridLayout.addWidget(self.Elf_Half_radioButton, 3, 0, 1, 1)

        self.Gnome_Hill_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Gnome_Hill_radioButton.setChecked(False)
        self.Gnome_Hill_radioButton.setObjectName("Gnome_Hill_radioButton")
        self.Gnome_Hill_radioButton.setText("Gnome, Hill")
        self.Race_buttonGroup.addButton(self.Gnome_Hill_radioButton)
        self.gridLayout.addWidget(self.Gnome_Hill_radioButton, 3, 1, 1, 1)

        self.Elf_Gray_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Elf_Gray_radioButton.setChecked(False)
        self.Elf_Gray_radioButton.setObjectName("Elf_Gray_radioButton")
        self.Elf_Gray_radioButton.setText("Elf, Gray")
        self.Race_buttonGroup.addButton(self.Elf_Gray_radioButton)
        self.gridLayout.addWidget(self.Elf_Gray_radioButton, 4, 0, 1, 1)

        self.Halfling_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Halfling_radioButton.setChecked(False)
        self.Halfling_radioButton.setObjectName("Halfling_radioButton")
        self.Halfling_radioButton.setText("Halfling")
        self.Race_buttonGroup.addButton(self.Halfling_radioButton)
        self.gridLayout.addWidget(self.Halfling_radioButton, 4, 1, 1, 1)

        self.Elf_High_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Elf_High_radioButton.setChecked(False)
        self.Elf_High_radioButton.setObjectName("Elf_High_radioButton")
        self.Elf_High_radioButton.setText("Elf, High")
        self.Race_buttonGroup.addButton(self.Elf_High_radioButton)
        self.gridLayout.addWidget(self.Elf_High_radioButton, 5, 0, 1, 1)

        self.Half_Orc_radioButton = QtWidgets.QRadioButton(self.frame_4)
        self.Half_Orc_radioButton.setChecked(False)
        self.Half_Orc_radioButton.setObjectName("Half_Orc_radioButton")
        self.Half_Orc_radioButton.setText("Half-Orc")
        self.Race_buttonGroup.addButton(self.Half_Orc_radioButton)
        self.gridLayout.addWidget(self.Half_Orc_radioButton, 5, 1, 1, 1)

        self.horizontalLayout_7.addWidget(self.frame_4)
        self.UnderDark_groupBox = QtWidgets.QGroupBox(self)
        self.UnderDark_groupBox.setCheckable(True)
        self.UnderDark_groupBox.setChecked(False)
        self.UnderDark_groupBox.setObjectName("UnderDark_groupBox")
        self.UnderDark_groupBox.setTitle("UnderDark Races")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.UnderDark_groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.Dwarf_Gray_radioButton = QtWidgets.QRadioButton(self.UnderDark_groupBox)
        self.Dwarf_Gray_radioButton.setEnabled(False)
        self.Dwarf_Gray_radioButton.setChecked(False)
        self.Dwarf_Gray_radioButton.setObjectName("Dwarf_Gray_radioButton")
        self.Dwarf_Gray_radioButton.setText("Dwarf, Gray")
        self.Race_buttonGroup.addButton(self.Dwarf_Gray_radioButton)
        self.verticalLayout_9.addWidget(self.Dwarf_Gray_radioButton)

        self.Elf_Dark_radioButton = QtWidgets.QRadioButton(self.UnderDark_groupBox)
        self.Elf_Dark_radioButton.setEnabled(False)
        self.Elf_Dark_radioButton.setChecked(False)
        self.Elf_Dark_radioButton.setObjectName("Elf_Dark_radioButton")
        self.Elf_Dark_radioButton.setText("Elf, Dark")
        self.Race_buttonGroup.addButton(self.Elf_Dark_radioButton)
        self.verticalLayout_9.addWidget(self.Elf_Dark_radioButton)

        self.Gnome_Deep_radioButton = QtWidgets.QRadioButton(self.UnderDark_groupBox)
        self.Gnome_Deep_radioButton.setEnabled(False)
        self.Gnome_Deep_radioButton.setChecked(False)
        self.Gnome_Deep_radioButton.setObjectName("Gnome_Deep_radioButton")
        self.Gnome_Deep_radioButton.setText("Gnome, Deep")
        self.Race_buttonGroup.addButton(self.Gnome_Deep_radioButton)
        self.verticalLayout_9.addWidget(self.Gnome_Deep_radioButton)
        self.horizontalLayout_7.addWidget(self.UnderDark_groupBox)

        self.Gender_groupBox = QtWidgets.QGroupBox(self)
        self.Gender_groupBox.setObjectName("Gender_groupBox")
        self.Gender_groupBox.setTitle("Gender")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.Gender_groupBox)
        self.verticalLayout_16.setObjectName("verticalLayout_16")

        self.Male_radioButton = QtWidgets.QRadioButton(self.Gender_groupBox)
        self.Male_radioButton.setChecked(True)
        self.Male_radioButton.setObjectName("Male_radioButton")
        self.Male_radioButton.setText("Male")

        self.Gender_buttonGroup = QtWidgets.QButtonGroup()
        self.Gender_buttonGroup.setObjectName("Gender_buttonGroup")
        self.Gender_buttonGroup.addButton(self.Male_radioButton)
        self.verticalLayout_16.addWidget(self.Male_radioButton)

        self.Female_radioButton = QtWidgets.QRadioButton(self.Gender_groupBox)
        self.Female_radioButton.setObjectName("Female_radioButton")
        self.Female_radioButton.setText("Female")
        self.Gender_buttonGroup.addButton(self.Female_radioButton)
        self.verticalLayout_16.addWidget(self.Female_radioButton)
        self.horizontalLayout_7.addWidget(self.Gender_groupBox)

        Wizard.race = self.Race_buttonGroup
        # self.gender = self.Gender_buttonGroup

    def initializePage(self) -> None:
        print(self.field("dex"))
        super(Page2, self).initializePage()



class Page3(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        # self = QtWidgets.QWizardPage()
        # self.setObjectName("wizardPage_3")
        self.setTitle("Class Selection")
        self.setSubTitle(
            "Based on your attributes and race, the classes listed below are "
            "available to your character. Certain races can also be multi-classed.")

        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_3 = QtWidgets.QFrame(self)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.First_Class_groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.First_Class_groupBox.setObjectName("First_Class_groupBox")
        self.First_Class_groupBox.setTitle("Primary Class")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.First_Class_groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")

        self.Bard_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Bard_radioButton.setEnabled(False)
        self.Bard_radioButton.setObjectName("Bard_radioButton")
        self.Bard_radioButton.setText("Bard")
        self.verticalLayout_18.addWidget(self.Bard_radioButton)

        self.Jester_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Jester_radioButton.setEnabled(False)
        self.Jester_radioButton.setObjectName("Jester_radioButton")
        self.Jester_radioButton.setText("Jester")
        self.verticalLayout_18.addWidget(self.Jester_radioButton)

        self.Cavalier_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Cavalier_radioButton.setEnabled(False)
        self.Cavalier_radioButton.setObjectName("Cavalier_radioButton")
        self.Cavalier_radioButton.setText("Cavalier")
        self.verticalLayout_18.addWidget(self.Cavalier_radioButton)

        self.Paladin_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Paladin_radioButton.setEnabled(False)
        self.Paladin_radioButton.setObjectName("Paladin_radioButton")
        self.Paladin_radioButton.setText("Paladin")
        self.verticalLayout_18.addWidget(self.Paladin_radioButton)

        self.Cleric_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Cleric_radioButton.setEnabled(False)
        self.Cleric_radioButton.setObjectName("Cleric_radioButton")
        self.Cleric_radioButton.setText("Cleric")
        self.verticalLayout_18.addWidget(self.Cleric_radioButton)

        self.Druid_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Druid_radioButton.setEnabled(False)
        self.Druid_radioButton.setObjectName("Druid_radioButton")
        self.Druid_radioButton.setText("Druid")
        self.verticalLayout_18.addWidget(self.Druid_radioButton)

        self.Mystic_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Mystic_radioButton.setEnabled(False)
        self.Mystic_radioButton.setObjectName("Mystic_radioButton")
        self.Mystic_radioButton.setText("Mystic")
        self.verticalLayout_18.addWidget(self.Mystic_radioButton)

        self.Fighter_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Fighter_radioButton.setEnabled(False)
        self.Fighter_radioButton.setObjectName("Fighter_radioButton")
        self.Fighter_radioButton.setText("Fighter")
        self.verticalLayout_18.addWidget(self.Fighter_radioButton)

        self.Barbarian_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Barbarian_radioButton.setEnabled(False)
        self.Barbarian_radioButton.setObjectName("Barbarian_radioButton")
        self.Barbarian_radioButton.setText("Barbarian")
        self.verticalLayout_18.addWidget(self.Barbarian_radioButton)

        self.Ranger_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Ranger_radioButton.setEnabled(False)
        self.Ranger_radioButton.setObjectName("Ranger_radioButton")
        self.Ranger_radioButton.setText("Ranger")
        self.verticalLayout_18.addWidget(self.Ranger_radioButton)

        self.horizontalLayout_3.addLayout(self.verticalLayout_18)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.Mage_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Mage_radioButton.setEnabled(False)
        self.Mage_radioButton.setObjectName("Mage_radioButton")
        self.Mage_radioButton.setText("Mage")
        self.verticalLayout_17.addWidget(self.Mage_radioButton)

        self.Illusionist_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Illusionist_radioButton.setEnabled(False)
        self.Illusionist_radioButton.setObjectName("Illusionist_radioButton")
        self.Illusionist_radioButton.setText("Illusionist")
        self.verticalLayout_17.addWidget(self.Illusionist_radioButton)

        self.Savant_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Savant_radioButton.setEnabled(False)
        self.Savant_radioButton.setObjectName("Savant_radioButton")
        self.Savant_radioButton.setText("Savant")
        self.verticalLayout_17.addWidget(self.Savant_radioButton)

        self.Thief_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Thief_radioButton.setEnabled(False)
        self.Thief_radioButton.setObjectName("Thief_radioButton")
        self.Thief_radioButton.setText("Thief")
        self.verticalLayout_17.addWidget(self.Thief_radioButton)

        self.Thief_Acrobat_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Thief_Acrobat_radioButton.setEnabled(False)
        self.Thief_Acrobat_radioButton.setObjectName("Thief_Acrobat_radioButton")
        self.Thief_Acrobat_radioButton.setText("Thief-Acrobat")
        self.verticalLayout_17.addWidget(self.Thief_Acrobat_radioButton)

        self.Mountebank_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Mountebank_radioButton.setEnabled(False)
        self.Mountebank_radioButton.setObjectName("Mountebank_radioButton")
        self.Mountebank_radioButton.setText("Mountebank")
        self.verticalLayout_17.addWidget(self.Mountebank_radioButton)

        self.Assassin_radioButton = QtWidgets.QRadioButton(self.First_Class_groupBox)
        self.Assassin_radioButton.setEnabled(False)
        self.Assassin_radioButton.setObjectName("Assassin_radioButton")
        self.Assassin_radioButton.setText("Assassin")
        self.verticalLayout_17.addWidget(self.Assassin_radioButton)

        self.horizontalLayout_3.addLayout(self.verticalLayout_17)
        self.horizontalLayout_6.addWidget(self.First_Class_groupBox)
        self.Second_Class_groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.Second_Class_groupBox.setEnabled(False)
        self.Second_Class_groupBox.setObjectName("Second_Class_groupBox")
        self.Second_Class_groupBox.setTitle("Second Class")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Second_Class_groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        self.Bard_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Bard_radioButton_2.setObjectName("Bard_radioButton_2")
        self.Bard_radioButton_2.setText("Bard")
        self.verticalLayout_12.addWidget(self.Bard_radioButton_2)

        self.Jester_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Jester_radioButton_2.setObjectName("Jester_radioButton_2")
        self.Jester_radioButton_2.setText("Jester")
        self.verticalLayout_12.addWidget(self.Jester_radioButton_2)

        self.Cavalier_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Cavalier_radioButton_2.setObjectName("Cavalier_radioButton_2")
        self.Cavalier_radioButton_2.setText("Cavalier")
        self.verticalLayout_12.addWidget(self.Cavalier_radioButton_2)

        self.Paladin_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Paladin_radioButton_2.setObjectName("Paladin_radioButton_2")
        self.Paladin_radioButton_2.setText("Paladin")
        self.verticalLayout_12.addWidget(self.Paladin_radioButton_2)

        self.Cleric_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Cleric_radioButton_2.setObjectName("Cleric_radioButton_2")
        self.Cleric_radioButton_2.setText("Cleric")
        self.verticalLayout_12.addWidget(self.Cleric_radioButton_2)

        self.Druid_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Druid_radioButton_2.setObjectName("Druid_radioButton_2")
        self.Druid_radioButton_2.setText("Druid")
        self.verticalLayout_12.addWidget(self.Druid_radioButton_2)

        self.Mystic_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Mystic_radioButton_2.setObjectName("Mystic_radioButton_2")
        self.Mystic_radioButton_2.setText("Mystic")
        self.verticalLayout_12.addWidget(self.Mystic_radioButton_2)

        self.Fighter_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Fighter_radioButton_2.setObjectName("Fighter_radioButton_2")
        self.Fighter_radioButton_2.setText("Fighter")
        self.verticalLayout_12.addWidget(self.Fighter_radioButton_2)

        self.Barbarian_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Barbarian_radioButton_2.setObjectName("Barbarian_radioButton_2")
        self.Barbarian_radioButton_2.setText("Barbarian")
        self.verticalLayout_12.addWidget(self.Barbarian_radioButton_2)

        self.Ranger_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Ranger_radioButton_2.setObjectName("Ranger_radioButton_2")
        self.Ranger_radioButton_2.setText("Ranger")
        self.verticalLayout_12.addWidget(self.Ranger_radioButton_2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Mage_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Mage_radioButton_2.setObjectName("Mage_radioButton_2")
        self.Mage_radioButton_2.setText("Mage")
        self.verticalLayout_13.addWidget(self.Mage_radioButton_2)

        self.Illusionist_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Illusionist_radioButton_2.setObjectName("Illusionist_radioButton_2")
        self.Illusionist_radioButton_2.setText("Illusionist")
        self.verticalLayout_13.addWidget(self.Illusionist_radioButton_2)

        self.Savant_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Savant_radioButton_2.setObjectName("Savant_radioButton_2")
        self.Savant_radioButton_2.setText("Savant")
        self.verticalLayout_13.addWidget(self.Savant_radioButton_2)

        self.Thief_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Thief_radioButton_2.setObjectName("Thief_radioButton_2")
        self.Thief_radioButton_2.setText("Thief")
        self.verticalLayout_13.addWidget(self.Thief_radioButton_2)

        self.Thief_Acrobat_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Thief_Acrobat_radioButton_2.setObjectName("Thief_Acrobat_radioButton_2")
        self.Thief_Acrobat_radioButton_2.setText("Thief-Acrobat")
        self.verticalLayout_13.addWidget(self.Thief_Acrobat_radioButton_2)

        self.Mountebank_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Mountebank_radioButton_2.setObjectName("Mountebank_radioButton_2")
        self.Mountebank_radioButton_2.setText("Mountebank")
        self.verticalLayout_13.addWidget(self.Mountebank_radioButton_2)

        self.Assassin_radioButton_2 = QtWidgets.QRadioButton(self.Second_Class_groupBox)
        self.Assassin_radioButton_2.setObjectName("Assassin_radioButton_2")
        self.Assassin_radioButton_2.setText("Assassin")
        self.verticalLayout_13.addWidget(self.Assassin_radioButton_2)

        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.horizontalLayout_6.addWidget(self.Second_Class_groupBox)
        self.Third_Class_groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.Third_Class_groupBox.setEnabled(False)
        self.Third_Class_groupBox.setObjectName("Third_Class_groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Third_Class_groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")

        self.Bard_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Bard_radioButton_3.setObjectName("Bard_radioButton_3")
        self.Bard_radioButton_3.setText("Bard")
        self.verticalLayout_14.addWidget(self.Bard_radioButton_3)

        self.Jester_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Jester_radioButton_3.setObjectName("Jester_radioButton_3")
        self.Jester_radioButton_3.setText("Jester")
        self.verticalLayout_14.addWidget(self.Jester_radioButton_3)

        self.Cavalier_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Cavalier_radioButton_3.setObjectName("Cavalier_radioButton_3")
        self.Cavalier_radioButton_3.setText("Cavalier")
        self.verticalLayout_14.addWidget(self.Cavalier_radioButton_3)

        self.Paladin_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Paladin_radioButton_3.setObjectName("Paladin_radioButton_3")
        self.Paladin_radioButton_3.setText("Paladin")
        self.verticalLayout_14.addWidget(self.Paladin_radioButton_3)

        self.Cleric_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Cleric_radioButton_3.setObjectName("Cleric_radioButton_3")
        self.Cleric_radioButton_3.setText("Cleric")
        self.verticalLayout_14.addWidget(self.Cleric_radioButton_3)

        self.Druid_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Druid_radioButton_3.setObjectName("Druid_radioButton_3")
        self.Druid_radioButton_3.setText("Druid")
        self.verticalLayout_14.addWidget(self.Druid_radioButton_3)

        self.Mystic_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Mystic_radioButton_3.setObjectName("Mystic_radioButton_3")
        self.Mystic_radioButton_3.setText("Mystic")
        self.verticalLayout_14.addWidget(self.Mystic_radioButton_3)

        self.Fighter_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Fighter_radioButton_3.setObjectName("Fighter_radioButton_3")
        self.Fighter_radioButton_3.setText("Fighter")
        self.verticalLayout_14.addWidget(self.Fighter_radioButton_3)

        self.Barbarian_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Barbarian_radioButton_3.setObjectName("Barbarian_radioButton_3")
        self.Barbarian_radioButton_3.setText("Barbarian")
        self.verticalLayout_14.addWidget(self.Barbarian_radioButton_3)

        self.Ranger_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Ranger_radioButton_3.setObjectName("Ranger_radioButton_3")
        self.Ranger_radioButton_3.setText("Ranger")
        self.verticalLayout_14.addWidget(self.Ranger_radioButton_3)

        self.horizontalLayout_5.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.Mage_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Mage_radioButton_3.setObjectName("Mage_radioButton_3")
        self.Mage_radioButton_3.setText("Mage")
        self.verticalLayout_15.addWidget(self.Mage_radioButton_3)

        self.Illusionist_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Illusionist_radioButton_3.setObjectName("Illusionist_radioButton_3")
        self.Illusionist_radioButton_3.setText("Illusionist")
        self.verticalLayout_15.addWidget(self.Illusionist_radioButton_3)

        self.Savant_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Savant_radioButton_3.setObjectName("Savant_radioButton_3")
        self.Savant_radioButton_3.setText("Savant")
        self.verticalLayout_15.addWidget(self.Savant_radioButton_3)

        self.Thief_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Thief_radioButton_3.setObjectName("Thief_radioButton_3")
        self.Thief_radioButton_3.setText("Thief")
        self.verticalLayout_15.addWidget(self.Thief_radioButton_3)

        self.Thief_Acrobat_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Thief_Acrobat_radioButton_3.setObjectName("Thief_Acrobat_radioButton_3")
        self.Thief_Acrobat_radioButton_3.setText("Thief-Acrobat")
        self.verticalLayout_15.addWidget(self.Thief_Acrobat_radioButton_3)

        self.Mountebank_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Mountebank_radioButton_3.setObjectName("Mountebank_radioButton_3")
        self.Mountebank_radioButton_3.setText("Mountebank")
        self.verticalLayout_15.addWidget(self.Mountebank_radioButton_3)

        self.Assassin_radioButton_3 = QtWidgets.QRadioButton(self.Third_Class_groupBox)
        self.Assassin_radioButton_3.setObjectName("Assassin_radioButton_3")
        self.Assassin_radioButton_3.setText("Assassin")
        self.verticalLayout_15.addWidget(self.Assassin_radioButton_3)

        self.horizontalLayout_5.addLayout(self.verticalLayout_15)
        self.horizontalLayout_6.addWidget(self.Third_Class_groupBox)
        self.verticalLayout_11.addWidget(self.frame_3)

        self.prime_class = self.First_Class_groupBox
        self.second_class = self.Second_Class_groupBox
        self.third_class = self.Third_Class_groupBox

    def initializePage(self) -> None:
        """Determine which classes the character is eligible for, based on previous selections"""
        # TODO: Have a check to ensure that the attributes are rolled

        new_list = []
        try:
            if (self.get_race() == "Dwarf, Hill" or self.get_race() == "Dwarf, Mountain" or
                    self.get_race() == "Dwarf, Grey"):
                race_class = race_vs_classes.multi_class["dwarf"]
                multi = 1
            else:
                race_class = race_vs_classes.multi_class[self.get_race().lower()]
                multi = 1
        except KeyError:  # Error indicates not multi-class eligible
            race_class = race_vs_classes.single_class[self.get_race().lower()]
            multi = 0
        new_list = list(race_class)

        try:
            if int(self.dex.text()) < class_min_attribs.bard["dex"] or \
                    int(self.chr.text()) < class_min_attribs.bard["chr"]:
                new_list.remove("Bard")
            if int(self.iq.text()) < class_min_attribs.jester["iq"] or \
                    int(self.dex.text()) < class_min_attribs.jester["dex"] or \
                    int(self.chr.text()) < class_min_attribs.jester["chr"]:
                new_list.remove("Jester")
            if int(self.strength.text()) < class_min_attribs.cavalier["str"] or \
                    int(self.dex.text()) < class_min_attribs.cavalier["dex"] or \
                    int(self.con.text()) < class_min_attribs.cavalier["con"] or \
                    int(self.iq.text()) < class_min_attribs.cavalier["iq"] or \
                    int(self.wis.text()) < class_min_attribs.cavalier["wis"]:
                new_list.remove("Cavalier")
            if int(self.strength.text()) < class_min_attribs.paladin["str"] or \
                    int(self.dex.text()) < class_min_attribs.paladin["dex"] or \
                    int(self.con.text()) < class_min_attribs.paladin["con"] or \
                    int(self.iq.text()) < class_min_attribs.paladin["iq"] or \
                    int(self.wis.text()) < class_min_attribs.paladin["wis"] or \
                    int(self.chr.text()) < class_min_attribs.paladin["chr"]:
                new_list.remove("Paladin")
            if int(self.wis.text()) < class_min_attribs.cleric["wis"]:
                new_list.remove("Cleric")
            if int(self.wis.text()) < class_min_attribs.druid["wis"] or \
                    int(self.chr.text()) < class_min_attribs.druid["chr"]:
                new_list.remove("Druid")
            if int(self.wis.text()) < class_min_attribs.mystic["wis"] or \
                    int(self.dex.text()) < class_min_attribs.mystic["dex"]:
                new_list.remove("Mystic")
            if int(self.strength.text()) < class_min_attribs.fighter["str"] or \
                    int(self.con.text()) < class_min_attribs.fighter["con"]:
                new_list.remove("Fighter")
            if int(self.strength.text()) < class_min_attribs.barbarian["str"] or \
                    int(self.dex.text()) < class_min_attribs.barbarian["dex"] or \
                    int(self.con.text()) < class_min_attribs.barbarian["con"] or \
                    int(self.wis.text()) >= class_min_attribs.barbarian["wis"]:
                new_list.remove("Barbarian")
            if int(self.iq.text()) < class_min_attribs.ranger["iq"] or \
                    int(self.wis.text()) < class_min_attribs.ranger["wis"] or \
                    int(self.con.text()) < class_min_attribs.ranger["con"]:
                new_list.remove("Ranger")
            if int(self.iq.text()) < class_min_attribs.mage["iq"] or \
                    int(self.dex.text()) < class_min_attribs.mage["dex"]:
                new_list.remove("Mage")
            if int(self.dex.text()) < class_min_attribs.illusionist["dex"] or \
                    int(self.iq.text()) < class_min_attribs.illusionist["iq"]:
                new_list.remove("Illusionist")
            if int(self.iq.text()) < class_min_attribs.savant["iq"] or \
                    int(self.wis.text()) < class_min_attribs.savant["wis"]:
                new_list.remove("Savant")
            if int(self.dex.text()) < class_min_attribs.thief["dex"]:
                new_list.remove("Thief")
            if int(self.strength.text()) < class_min_attribs.thief_acrobat["str"] or \
                    int(self.dex.text()) < class_min_attribs.thief_acrobat["dex"]:
                new_list.remove("Thief-Acrobat")
            if int(self.dex.text()) < class_min_attribs.mountebank["dex"] or \
                    int(self.iq.text()) < class_min_attribs.mountebank["iq"] or \
                    int(self.chr.text()) < class_min_attribs.mountebank["chr"]:
                new_list.remove("Mountebank")
            if int(self.strength.text()) < class_min_attribs.assassin["str"] or \
                    int(self.dex.text()) < class_min_attribs.assassin["dex"] or \
                    int(self.iq.text()) < class_min_attribs.assassin["iq"]:
                new_list.remove("Assassin")
        except ValueError:
            pass

        self.enable_classes(new_list, multi)

    def enable_classes(self, classes, multi):
        """Enable radio button associated with authorized classes"""
        print(multi)
        # TODO: Figure out how to not brute-force this
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
            for item in classes:
                print(item)
            # for item in classes:
            #     print(item[0])
            #     if "Bard" in item[0]:
            #         print(item[0])
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

    def get_race(self):
        """Get the selected race radiobutton"""
        return Wizard.race.checkedButton().text()
    #
    # def get_gender(self):
    #     """Get the selected gender radiobutton"""
    #     return self.gender.checkedButton().text()


class Page4(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        # self.wizardPage_4 = QtWidgets.QWizardPage()
        # self.wizardPage_4.setObjectName("wizardPage_4")
        self.setTitle("Wrap-Up")
        self.setSubTitle("Click \"Finish\" to complete the basics of your character.")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Finish_Out_label = QtWidgets.QLabel(self)
        self.Finish_Out_label.setWordWrap(True)
        self.Finish_Out_label.setObjectName("Finish_Out_label")
        self.Finish_Out_label.setText(
            "<html><head/><body><p>Your character\'s information will be moved to a character sheet. In addition, "
            "your character\'s hit points, initial money, etc. will be auto-generated and added to the character "
            "sheet as well.<br/><br/></p></body></html>")
        self.verticalLayout_10.addWidget(self.Finish_Out_label)


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Wizard()
    w.show()
    app.exec_()


if __name__ == "__main__":
    sys.exit(main())
