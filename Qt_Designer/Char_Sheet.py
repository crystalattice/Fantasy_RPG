import pickle
import sys
from typing import Dict, Any

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox, QComboBox, QSpinBox, QLabel, \
    QDialogButtonBox, QMessageBox

from Qt_Designer.ADD_Char_Sheet import Ui_MainWindow
from Adv_Dark_Deep.Char_Creation import roll_abilities, get_acceptable_class, strength_abilities, dex_abilities, \
    iq_abilities, wisdom_abilities, con_abilities, charisma_abilities, race_vs_attribs


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

        # Character sheet inputs-Info tab
        self.char_name: QLineEdit = self.Char_Name_lineEdit
        self.char_race: QComboBox = self.Race_comboBox
        self.char_class: QComboBox = self.Class_comboBox
        self.char_align: QComboBox = self.Alignment_comboBox
        self.char_age: QSpinBox = self.Age_spinBox
        self.char_gender: QComboBox = self.Gender_comboBox
        self.char_social_class: QComboBox = self.Social_Class_comboBox
        self.char_height: QSpinBox = self.Height_spinBox
        self.char_weight: QSpinBox = self.Weight_spinBox

        # Character sheet outputs
        self.strength: QLabel = self.STR_Output_label
        self.bonus_strength: QLabel = self.Exceptional_Output_label
        self.to_hit_bonus: QLabel = self.Hit_Bonus_label
        self.carry_bonus: QLabel = self.Carry_Bonus_Output_label
        self.damage_bonus: QLabel = self.Damage_Mod_Output_label
        self.stuck_doors: QLabel = self.Stuck_Doors_Output_label
        self.locked_doors_bonus: QLabel = self.Open_Doors_Output_label
        self.bend_bars: QLabel = self.Bend_Bars_Output_label

        self.dex: QLabel = self.Dex_Output_label
        self.init_adj: QLabel = self.Init_Adj_Output_label
        self.missile_adj: QLabel = self.Missile_Bonus_Output_label
        self.ac_adj: QLabel = self.AC_Adj_Output_label_55

        self.iq: QLabel = self.IQ_Output_label
        self.max_lang: QLabel = self.Lang_Output_label
        self.immune_illusion: QLabel = self.Immunity_Output_label
        self.max_spell_level: QLabel = self.Max_Level_Output_label

        self.wis: QLabel = self.Wisdom_Output_label
        self.magical_attack_adj: QLabel = self.Mag_Attack_Output_label
        self.cleric_spell_bonus: QLabel = self.Spell_Bonus_Output_label
        self.spell_failure: QLabel = self.Spell_Fail_Output_label
        self.immune_charm: QLabel = self.Immunity_Output_label_2

        self.con: QLabel = self.CON_Output_label
        self.hp_adj: QLabel = self.HP_Adj_Output_label
        self.sys_shock: QLabel = self.Sys_Shock_Output_label
        self.resurrection: QLabel = self.Resurrect_Output_label

        self.chr: QLabel = self.CHR_Output_label
        self.max_henchmen: QLabel = self.Henchmen_Output_label
        self.morale_adj: QLabel = self.Morale_Output_label
        self.reaction_adj: QLabel = self.React_Output_label

        self.char_2nd_class: str = "None"
        self.char_3rd_class: str = "None"

        # Actions
        # self.actionNew_Character.connect(self.new_character)
        self.actionOpen_Character.triggered.connect(self.open_character)
        self.actionSave_Character.triggered.connect(self.save_character)

        self.action3d6.triggered.connect(self.roll_3d6)
        self.action4d6_drop_lowest.triggered.connect(self.roll_4d6)
        self.action2d6_6.triggered.connect(self.roll_2d6)
        self.char_race.currentTextChanged.connect(self.race_selection)

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

    def save_character(self) -> None:
        """Save the current character sheet"""
        save_name: str = self.get_char_name()
        char_vals: dict[str | Any, str | Any] = {
            "str": self.strength.text(),
            "char_bonus_str": self.bonus_strength.text(),
            "to_hit_bonus": self.to_hit_bonus.text(),
            "dam_bonus": self.damage_bonus.text(),
            "carry_bonus": self.carry_bonus.text(),
            "stuck_doors": self.stuck_doors.text(),
            "locked_doors": self.locked_doors_bonus.text(),
            "bend_bars": self.bend_bars.text(),

            "char_dex": self.dex.text(),
            "init_adj": self.init_adj.text(),
            "missile_adj": self.missile_adj.text(),
            "ac_adj": self.ac_adj.text(),

            "char_wis": self.wis.text(),
            "magical_attack_adj": self.magical_attack_adj.text(),
            "cleric_spell_bonus": self.cleric_spell_bonus.text(),
            "spell_failure": self.spell_failure.text(),
            "immune_charm": self.immune_charm.text(),

            "char_iq": self.iq.text(),
            "max_lang": self.max_lang.text(),
            "immune_to_illusion": self.immune_illusion.text(),
            "max_spell_level": self.max_spell_level.text(),

            "char_chr": self.chr.text(),
            "max_henchmen": self.max_henchmen.text(),
            "morale_adj": self.morale_adj.text(),
            "reaction_adj": self.reaction_adj.text(),

            "char_con": self.con.text(),
            "hp_adj": self.hp_adj.text(),
            "system_shock": self.sys_shock.text(),
            "resurrect": self.resurrection.text(),

            "race": self.race_selection(),
            "class": self.class_selection(),
            "second_class": self.char_2nd_class,
            "third_class": self.char_3rd_class,
            "alignment": self.alignment_selection(),
            "age": self.get_age(),
            "gender": self.get_gender(),
            "social_class": self.get_social_class(),
            "height": self.get_height(),
            "weight": self.get_weight(),
        }
        if not "str":  # Assume no attributes created
            no_attribs_msg: QMessageBox | QMessageBox = QMessageBox()
            no_attribs_msg.setWindowTitle("Missing Attributes")
            no_attribs_msg.setText("You must roll for attributes prior to saving.\n"
                                   "Character not saved.")
            no_attribs_msg.setIcon(QMessageBox.Icon.Warning)
            button: QMessageBox.StandardButtons = no_attribs_msg.exec()
            button = QMessageBox.StandardButtons(button)
        if not save_name:
            no_name_msg: QMessageBox | QMessageBox = QMessageBox()
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

    def roll_3d6(self) -> None:
        rolls: list = roll_abilities.three_d6()
        self.insert_rolls(rolls)

    def roll_4d6(self) -> None:
        rolls: list = roll_abilities.four_d6_drop_lowest()
        self.insert_rolls(rolls)

    def roll_2d6(self) -> None:
        rolls: list = roll_abilities.two_d6_plus_6()
        self.insert_rolls(rolls)

    def insert_rolls(self, rolls) -> None:
        """Put the attribute rolls into their respective variables"""
        strength: int
        bonus_strength: int
        str_plus_bonus: int
        dex: int
        iq: int
        wis: int
        con: int
        charisma: int
        strength, dex, iq, wis, con, charisma = [rolls[i] for i in range(6)]
        # TODO: Add check to overwrite attribs
        # if self.strength.text():
        #     existing_attribs_msg = QMessageBox()
        #     existing_attribs_msg.setWindowTitle("Existing Attributes")
        #     existing_attribs_msg.setText("Your character already has attributes. Are you sure you want to reroll?")
        #     existing_attribs_msg.setIcon(QMessageBox.Icon.Warning)
        #     button = existing_attribs_msg.exec()
        #     button = QMessageBox.StandardButtons(button)
        # TODO: Check if PC allowed bonus strength
        if strength == 18:
            bonus_strength = roll_abilities.multi_die(1, 100)
            self.bonus_strength.setText(str(bonus_strength))
            str_plus_bonus = int(f"{strength}{bonus_strength}")
        else:
            self.bonus_strength.setText("0")
            str_plus_bonus = strength
        self.strength.setText(str(strength))
        self.to_hit_bonus.setText(str(strength_abilities.get_str_ability(str_plus_bonus, 0)))
        self.damage_bonus.setText(str(strength_abilities.get_str_ability(str_plus_bonus, 1)))
        self.carry_bonus.setText(str(strength_abilities.get_str_ability(str_plus_bonus, 2)))
        self.stuck_doors.setText(str(strength_abilities.get_str_ability(str_plus_bonus, 3)))
        self.locked_doors_bonus.setText(str(strength_abilities.get_str_ability(str_plus_bonus, 4)))
        self.bend_bars.setText(str(strength_abilities.get_str_ability(str_plus_bonus, 5)))

        self.iq.setText(str(iq))
        self.max_lang.setText(str(iq_abilities.get_iq_ability(iq, 0)))
        self.immune_illusion.setText(str(iq_abilities.get_iq_ability(iq, 1)))
        self.max_spell_level.setText(str(iq_abilities.get_iq_ability(iq, 2)))

        self.wis.setText(str(wis))
        self.magical_attack_adj.setText(str(wisdom_abilities.get_wis_ability(wis, 0)))
        self.cleric_spell_bonus.setText(str(wisdom_abilities.get_wis_ability(wis, 1)))
        self.spell_failure.setText(str(wisdom_abilities.get_wis_ability(wis, 2)))
        self.immune_charm.setText(str(wisdom_abilities.get_wis_ability(wis, 3)))

        self.dex.setText(str(dex))
        self.init_adj.setText(str(dex_abilities.get_dex_ability(dex, 0)))
        self.missile_adj.setText(str(dex_abilities.get_dex_ability(dex, 1)))
        self.ac_adj.setText(str(dex_abilities.get_dex_ability(dex, 2)))

        # TODO: account for HP re-roll
        self.con.setText(str(con))
        # TODO: account for fighter multiclass
        if self.char_class == "Fighter":
            self.hp_adj.setText(str(con_abilities.get_con_ability(con, 1)))
        else:
            self.hp_adj.setText(str(con_abilities.get_con_ability(con, 0)))
        self.sys_shock.setText(str(con_abilities.get_con_ability(con, 3)))
        self.resurrection.setText(str(con_abilities.get_con_ability(con, 4)))

        self.chr.setText(str(charisma))
        self.max_henchmen.setText(str(charisma_abilities.get_char_ability(charisma, 0)))
        self.morale_adj.setText(str(charisma_abilities.get_char_ability(charisma, 1)))
        self.reaction_adj.setText(str(charisma_abilities.get_char_ability(charisma, 2)))

        self.race_selection()

    # TODO: Consider making the following into properties
    # Saving character checks
    def get_char_name(self):
        """Assign input character name to variable"""
        return self.char_name.text()

    def get_gender(self):
        """Get character's gender"""
        return self.Gender_comboBox.currentText()

    # Race selection and associated information
    # TODO: Check attributes vs. race limits
    def race_selection(self):
        """Get the character's race.

        Race combobox will be populated by eligible races based on character's rolled abilities.
        """
        if self.wis.text() == "0":  # Assume no attributes created
            no_attribs_msg: QMessageBox | QMessageBox = QMessageBox()
            no_attribs_msg.setWindowTitle("Missing Attributes")
            no_attribs_msg.setText("You must roll for attributes before selecting a race.")
            no_attribs_msg.setIcon(QMessageBox.Icon.Warning)
            button: QMessageBox.StandardButtons = no_attribs_msg.exec()
            button = QMessageBox.StandardButtons(button)
            self.char_race.setCurrentIndex(0)
            # TODO: will cause the dialog box to appear twice
        races = race_vs_attribs.get_acceptable_race(self.get_gender(), int(self.strength.text()), int(self.iq.text()),
                                                    int(self.wis.text()), int(self.dex.text()), int(self.con.text()),
                                                    int(self.chr.text()))
        # self.char_race.clear()
        self.char_race.addItems(races)
        # self.class_selection()  # Use race to determine eligible classes
        # return self.char_race.currentText()

    # TODO: Check attributes vs. class mins
    def class_selection(self):
        """Get the character's class"""
        self.char_class.clear()
        classes = get_acceptable_class.get_one_class(self.char_race.currentText().lower())
        self.char_class.addItems(classes)

    def dual_class_selection(self) -> None:
        """If dual classed, get second class"""
        if self.Second_Class_comboBox.currentText() != "None":
            self.char_2nd_class = self.Second_Class_comboBox.currentText()

    def third_class_selection(self) -> None:
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
                self.char_3rd_class = self.Third_Class_comboBox.currentText()

    def alignment_selection(self):
        """Get character's alignment"""
        return self.Alignment_comboBox.currentText()

    def get_age(self):
        """Get character's age"""
        return self.Age_spinBox.text()

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
