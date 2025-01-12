import pickle

from Archived.Adv_Dark_Deep.Char_Creation import race_vs_attribs as rva


def make_race_lists():
    """Test the strength-associated abilities"""
    male_race_list = []
    female_race_list = []
    for strength in range(3, 19):
        for iq in range(3, 19):
            for wis in range(3, 19):
                for dex in range(3, 19):
                    for con in range(3, 19):
                        for chr in range(3, 19):
                            male_race_list.append({"STR": strength,
                                                   "IQ": iq,
                                                   "WIS": wis,
                                                   "DEX": dex,
                                                   "CON": con,
                                                   "CHR": chr,
                                                   "races": rva.get_acceptable_race("male", strength, iq, wis, dex, con,
                                                                                    chr)})
                            female_race_list.append({"STR": strength,
                                                     "IQ": iq,
                                                     "WIS": wis,
                                                     "DEX": dex,
                                                     "CON": con,
                                                     "CHR": chr,
                                                     "races": rva.get_acceptable_race("female", strength, iq, wis, dex,
                                                                                      con, chr)})
    with open("male_race_list", "wb") as male_races:
        pickle.dump(male_race_list, male_races)
    with open("female_race_list", "wb") as female_races:
        pickle.dump(female_race_list, female_races)


if __name__ == "__main__":
    make_race_lists()
