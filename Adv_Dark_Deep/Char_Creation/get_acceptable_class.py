from typing import List

import Adv_Dark_Deep.Char_Creation.race_acceptable_classes as rac
# from Qt_Designer.Char_Sheet import MainWindow as mw


def get_one_class(race: str) -> tuple:
    """For the PC's race, get acceptable single class types"""
    # char_class = []
    # if race == "dwarf, grey":
    #     return rac.single_class["dwarf, grey"]
    return rac.single_class[race]


def get_multi_class(race: str) -> tuple:
    """For the PC's race, get allowed multi-class combinations"""
    return rac.multi_class[race]


# def get_classes(race: str) -> list:
#     """Get character classes available to a particular race"""
#     # global classes
#     char_classes: List[tuple] = []
#     if race == "Hill Dwarf":
#         # classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Dwarf_Hill)
#         # classes = rac.
#         pass
#     elif race == "Grey Dwarf":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Dwarf_Gray)
#     elif race == "Mountain Dwarf":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Dwarf_Mountain)
#     elif race == "Dark Elf":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Dark)
#     elif race == "Grey Elf":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Gray)
#     elif race == "Half-Elf":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Half)
#     elif race == "High Elf":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_High)
#     elif race == "Wild Elf":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Wild)
#     elif race == "Wood Elf":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Wood)
#     elif race == "Deep Gnome":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Gnome_Deep)
#     elif race == "Forest Gnome":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Gnome_Forest)
#     elif race == "Hill Gnome":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Gnome_Hill)
#     elif race == "Halfling":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Halfling)
#     elif race == "Half-Orc":
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Orc_Half)
#     else:  # Assume human as default
#         classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Human)
#
#     for avail_classes in classes:
#         char_classes.append(avail_classes)
#
#     return char_classes

if __name__ == "__main__":
    print(get_one_class("dwarf, grey"))
    print(get_one_class("elf, half"))
    print(get_multi_class("dwarf"))
    print(get_multi_class("gnome, deep"))
