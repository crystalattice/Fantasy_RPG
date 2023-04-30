from collections import namedtuple
from typing import Type

ability_limits: Type[namedtuple] = namedtuple("Ability_Limits", ["STR_min", "STR_max", "IQ_min", "IQ_max", "WIS_min",
                                                                 "WIS_max", "DEX_min", "DEX_max", "CON_min", "CON_max",
                                                                 "CHR_min", "CHR_max"])

male_dwarf = ability_limits(8, 18, 3, 18, 3, 18, 3, 17, 12, 19, 3, 16)
female_dwarf = ability_limits(8, 17, 3, 18, 3, 18, 3, 17, 12, 19, 3, 16)
male_dark_elf = ability_limits(3, 18, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18)
female_dark_elf = ability_limits(3, 16, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18)
male_grey_elf = ability_limits(3, 18, 8, 19, 3, 18, 7, 18, 6, 18, 8, 18)
female_grey_elf = ability_limits(3, 16, 8, 19, 3, 18, 7, 18, 6, 18, 8, 18)
male_half_elf = ability_limits(3, 18, 4, 18, 3, 18, 6, 18, 6, 18, 3, 18)
female_half_elf = ability_limits(3, 17, 4, 18, 3, 18, 6, 18, 6, 18, 3, 18)
male_high_elf = ability_limits(3, 18, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18)
female_high_elf = ability_limits(3, 16, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18)
male_wild_elf = ability_limits(3, 18, 7, 17, 3, 18, 7, 18, 6, 18, 8, 18)
female_wild_elf = ability_limits(3, 18, 7, 17, 3, 18, 7, 18, 6, 18, 8, 18)
male_wood_elf = ability_limits(3, 18, 7, 17, 3, 18, 7, 18, 6, 18, 8, 18)
female_wood_elf = ability_limits(3, 16, 7, 17, 3, 18, 7, 18, 6, 18, 8, 18)
male_gnome = ability_limits(6, 18, 7, 18, 3, 18, 3, 18, 8, 18, 3, 18)
female_gnome = ability_limits(6, 15, 7, 18, 3, 18, 3, 18, 8, 18, 3, 18)
male_halfling = ability_limits(6, 17, 6, 18, 3, 17, 8, 18, 10, 19, 3, 18)
female_halfling = ability_limits(6, 14, 6, 18, 3, 17, 8, 18, 10, 19, 3, 18)
male_half_orc = ability_limits(6, 18, 3, 17, 3, 14, 3, 17, 13, 19, 3, 12)
female_half_orc = ability_limits(6, 18, 3, 17, 3, 14, 3, 17, 13, 19, 3, 12)

race_abil_limits = (male_dwarf, female_dwarf, male_dark_elf, female_dark_elf, male_grey_elf, female_grey_elf,
                    male_half_elf, female_half_elf, male_high_elf, female_high_elf, male_wild_elf, female_wild_elf,
                    male_wood_elf, female_wood_elf, male_gnome, female_gnome, male_halfling, female_halfling,
                    male_half_orc, female_half_orc)


def get_acceptable_race(gender: str, strength: int, iq: int, wis: int, dex: int, con: int, chr: int) -> list:
    avail_races = ["Human"]
    if gender == "Male":
        if (
                male_dwarf.STR_min <= strength <= male_dwarf.STR_max and
                male_dwarf.IQ_min <= iq <= male_dwarf.IQ_max and
                male_dwarf.WIS_min <= wis <= male_dwarf.WIS_max and
                male_dwarf.DEX_min <= dex <= male_dwarf.DEX_max and
                male_dwarf.CON_min <= con <= male_dwarf.CON_max and
                male_dwarf.CHR_min <= chr <= male_dwarf.CHR_max
        ):
            avail_races.extend(["Dwarf, Grey (Duergar)", "Dwarf, Hill", "Dwarf, Mountain"])

        if (
                male_dark_elf.STR_min <= strength <= male_dark_elf.STR_max and
                male_dark_elf.IQ_min <= iq <= male_dark_elf.IQ_max and
                male_dark_elf.WIS_min <= wis <= male_dark_elf.WIS_max and
                male_dark_elf.DEX_min <= dex <= male_dark_elf.DEX_max and
                male_dark_elf.CON_min <= con <= male_dark_elf.CON_max and
                male_dark_elf.CHR_min <= chr <= male_dark_elf.CHR_max
        ):
            avail_races.append("Elf, Dark (Drow)")
        if (
                male_grey_elf.STR_min <= strength <= male_grey_elf.STR_max and
                male_grey_elf.IQ_min <= iq <= male_grey_elf.IQ_max and
                male_grey_elf.WIS_min <= wis <= male_grey_elf.WIS_max and
                male_grey_elf.DEX_min <= dex <= male_grey_elf.DEX_max and
                male_grey_elf.CON_min <= con <= male_grey_elf.CON_max and
                male_grey_elf.CHR_min <= chr <= male_grey_elf.CHR_max
        ):
            avail_races.append("Elf, Grey")
        if (
                male_half_elf.STR_min <= strength <= male_half_elf.STR_max and
                male_half_elf.IQ_min <= iq <= male_half_elf.IQ_max and
                male_half_elf.WIS_min <= wis <= male_half_elf.WIS_max and
                male_half_elf.DEX_min <= dex <= male_half_elf.DEX_max and
                male_half_elf.CON_min <= con <= male_half_elf.CON_max and
                male_half_elf.CHR_min <= chr <= male_half_elf.CHR_max
        ):
            avail_races.append("Half-Elf")
        if (
                male_high_elf.STR_min <= strength <= male_high_elf.STR_max and
                male_high_elf.IQ_min <= iq <= male_high_elf.IQ_max and
                male_high_elf.WIS_min <= wis <= male_high_elf.WIS_max and
                male_high_elf.DEX_min <= dex <= male_high_elf.DEX_max and
                male_high_elf.CON_min <= con <= male_high_elf.CON_max and
                male_high_elf.CHR_min <= chr <= male_high_elf.CHR_max
        ):
            avail_races.append("Elf, High")
        if (
                male_wild_elf.STR_min <= strength <= male_wild_elf.STR_max and
                male_wild_elf.IQ_min <= iq <= male_wild_elf.IQ_max and
                male_wild_elf.WIS_min <= wis <= male_wild_elf.WIS_max and
                male_wild_elf.DEX_min <= dex <= male_wild_elf.DEX_max and
                male_wild_elf.CON_min <= con <= male_wild_elf.CON_max and
                male_wild_elf.CHR_min <= chr <= male_wild_elf.CHR_max
        ):
            avail_races.append("Elf, Wild")
        if (
                male_wood_elf.STR_min <= strength <= male_wood_elf.STR_max and
                male_wood_elf.IQ_min <= iq <= male_wood_elf.IQ_max and
                male_wood_elf.WIS_min <= wis <= male_wood_elf.WIS_max and
                male_wood_elf.DEX_min <= dex <= male_wood_elf.DEX_max and
                male_wood_elf.CON_min <= con <= male_wood_elf.CON_max and
                male_wood_elf.CHR_min <= chr <= male_wood_elf.CHR_max
        ):
            avail_races.append("Elf, Wood")
        if (
                male_gnome.STR_min <= strength <= male_gnome.STR_max and
                male_gnome.IQ_min <= iq <= male_gnome.IQ_max and
                male_gnome.WIS_min <= wis <= male_gnome.WIS_max and
                male_gnome.DEX_min <= dex <= male_gnome.DEX_max and
                male_gnome.CON_min <= con <= male_gnome.CON_max and
                male_gnome.CHR_min <= chr <= male_gnome.CHR_max
        ):
            avail_races.extend(["Gnome, Deep (Svirfneblin)", "Gnome, Forest", "Gnome, Hill"])
        if (
                male_halfling.STR_min <= strength <= male_halfling.STR_max and
                male_halfling.IQ_min <= iq <= male_halfling.IQ_max and
                male_halfling.WIS_min <= wis <= male_halfling.WIS_max and
                male_halfling.DEX_min <= dex <= male_halfling.DEX_max and
                male_halfling.CON_min <= con <= male_halfling.CON_max and
                male_halfling.CHR_min <= chr <= male_halfling.CHR_max
        ):
            avail_races.append("Halfling")
        if (
                male_half_orc.STR_min <= strength <= male_half_orc.STR_max and
                male_half_orc.IQ_min <= iq <= male_half_orc.IQ_max and
                male_half_orc.WIS_min <= wis <= male_half_orc.WIS_max and
                male_half_orc.DEX_min <= dex <= male_half_orc.DEX_max and
                male_half_orc.CON_min <= con <= male_half_orc.CON_max and
                male_half_orc.CHR_min <= chr <= male_half_orc.CHR_max
        ):
            avail_races.append("Half-Orc")
    else:  # Females
        if (
                female_dwarf.STR_min <= strength <= female_dwarf.STR_max and
                female_dwarf.IQ_min <= iq <= female_dwarf.IQ_max and
                female_dwarf.WIS_min <= wis <= female_dwarf.WIS_max and
                female_dwarf.DEX_min <= dex <= female_dwarf.DEX_max and
                female_dwarf.CON_min <= con <= female_dwarf.CON_max and
                female_dwarf.CHR_min <= chr <= female_dwarf.CHR_max
        ):
            avail_races.extend(["Dwarf, Grey (Duergar)", "Dwarf, Hill", "Dwarf, Mountain"])
        if (
                female_dark_elf.STR_min <= strength <= female_dark_elf.STR_max and
                female_dark_elf.IQ_min <= iq <= female_dark_elf.IQ_max and
                female_dark_elf.WIS_min <= wis <= female_dark_elf.WIS_max and
                female_dark_elf.DEX_min <= dex <= female_dark_elf.DEX_max and
                female_dark_elf.CON_min <= con <= female_dark_elf.CON_max and
                female_dark_elf.CHR_min <= chr <= female_dark_elf.CHR_max
        ):
            avail_races.append("Elf, Dark (Drow)")
        if (
                female_grey_elf.STR_min <= strength <= female_grey_elf.STR_max and
                female_grey_elf.IQ_min <= iq <= female_grey_elf.IQ_max and
                female_grey_elf.WIS_min <= wis <= female_grey_elf.WIS_max and
                female_grey_elf.DEX_min <= dex <= female_grey_elf.DEX_max and
                female_grey_elf.CON_min <= con <= female_grey_elf.CON_max and
                female_grey_elf.CHR_min <= chr <= female_grey_elf.CHR_max
        ):
            avail_races.append("Elf, Grey")
        if (
                female_half_elf.STR_min <= strength <= female_half_elf.STR_max and
                female_half_elf.IQ_min <= iq <= female_half_elf.IQ_max and
                female_half_elf.WIS_min <= wis <= female_half_elf.WIS_max and
                female_half_elf.DEX_min <= dex <= female_half_elf.DEX_max and
                female_half_elf.CON_min <= con <= female_half_elf.CON_max and
                female_half_elf.CHR_min <= chr <= female_half_elf.CHR_max
        ):
            avail_races.append("Half-Elf")
        if (
                female_high_elf.STR_min <= strength <= female_high_elf.STR_max and
                female_high_elf.IQ_min <= iq <= female_high_elf.IQ_max and
                female_high_elf.WIS_min <= wis <= female_high_elf.WIS_max and
                female_high_elf.DEX_min <= dex <= female_high_elf.DEX_max and
                female_high_elf.CON_min <= con <= female_high_elf.CON_max and
                female_high_elf.CHR_min <= chr <= female_high_elf.CHR_max
        ):
            avail_races.append("Elf, High")
        if (
                female_wild_elf.STR_min <= strength <= female_wild_elf.STR_max and
                female_wild_elf.IQ_min <= iq <= female_wild_elf.IQ_max and
                female_wild_elf.WIS_min <= wis <= female_wild_elf.WIS_max and
                female_wild_elf.DEX_min <= dex <= female_wild_elf.DEX_max and
                female_wild_elf.CON_min <= con <= female_wild_elf.CON_max and
                female_wild_elf.CHR_min <= chr <= female_wild_elf.CHR_max
        ):
            avail_races.append("Elf, Wild")
        if (
                female_wood_elf.STR_min <= strength <= female_wood_elf.STR_max and
                female_wood_elf.IQ_min <= iq <= female_wood_elf.IQ_max and
                female_wood_elf.WIS_min <= wis <= female_wood_elf.WIS_max and
                female_wood_elf.DEX_min <= dex <= female_wood_elf.DEX_max and
                female_wood_elf.CON_min <= con <= female_wood_elf.CON_max and
                female_wood_elf.CHR_min <= chr <= female_wood_elf.CHR_max
        ):
            avail_races.append("Elf, Wood")
        if (
                female_gnome.STR_min <= strength <= female_gnome.STR_max and
                female_gnome.IQ_min <= iq <= female_gnome.IQ_max and
                female_gnome.WIS_min <= wis <= female_gnome.WIS_max and
                female_gnome.DEX_min <= dex <= female_gnome.DEX_max and
                female_gnome.CON_min <= con <= female_gnome.CON_max and
                female_gnome.CHR_min <= chr <= female_gnome.CHR_max
        ):
            avail_races.extend(["Gnome, Deep (Svirfneblin)", "Gnome, Forest", "Gnome, Hill"])
        if (
                female_halfling.STR_min <= strength <= female_halfling.STR_max and
                female_halfling.IQ_min <= iq <= female_halfling.IQ_max and
                female_halfling.WIS_min <= wis <= female_halfling.WIS_max and
                female_halfling.DEX_min <= dex <= female_halfling.DEX_max and
                female_halfling.CON_min <= con <= female_halfling.CON_max and
                female_halfling.CHR_min <= chr <= female_halfling.CHR_max
        ):
            avail_races.append("Halfling")
        if (
                female_half_orc.STR_min <= strength <= female_half_orc.STR_max and
                female_half_orc.IQ_min <= iq <= female_half_orc.IQ_max and
                female_half_orc.WIS_min <= wis <= female_half_orc.WIS_max and
                female_half_orc.DEX_min <= dex <= female_half_orc.DEX_max and
                female_half_orc.CON_min <= con <= female_half_orc.CON_max and
                female_half_orc.CHR_min <= chr <= female_half_orc.CHR_max
        ):
            avail_races.append("Half-Orc")
    return avail_races


if __name__ == "__main__":
    print(get_acceptable_race("male", 9, 5, 10, 6, 13, 9))
    print(get_acceptable_race("female", 13, 13, 12, 14, 12, 12))
