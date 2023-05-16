import Adv_Dark_Deep.Char_Creation.race_acceptable_classes as rac


def get_one_class(race: str) -> tuple:
    return rac.single_class[race]


def get_multi_class(race: str) -> tuple:
    """For the PC's race, get allowed multi-class combinations"""
    return rac.multi_class[race]


if __name__ == "__main__":
    print(get_one_class("dwarf, grey"))
    print(get_one_class("elf, half"))
    print(get_multi_class("dwarf"))
    print(get_multi_class("gnome, deep"))
