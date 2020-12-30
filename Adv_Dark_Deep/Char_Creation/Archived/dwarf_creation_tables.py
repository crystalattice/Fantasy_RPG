def poison_save_bonus(con):
    """Saving throw bonus due to Constitution

    Applies to all poisons and venom, spells, and rods/staves/wands
    """
    if con in range(4, 7):
        save = 1
    elif con in range(7, 11):
        save = 2
    elif con in range(11, 14):
        save = 3
    elif con in range(14, 18):
        save = 4
    elif con >= 18:
        save = 5
    else:
        save = 0

    return save


def special_abilities(dwarf_type):
    spec_abil = "Detect sloping passages and tunnels (75%)\nDetect new construction (75%)\nDetect moving, shifting, " \
                "etc. walls and rooms\nDetect pit traps, falling blocks, etc. (50%) " \
                "[All of the previous within 10 feet]"
    languages = ""
    if dwarf_type == "Grey Dwarf":
        spec_abil += "\nUnaffected by illusions, paralyzation, or paralysis\nImmune to magical poisons"
        languages += "Dwarvish, Undercommon"
        infravision = 120
