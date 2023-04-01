import pickle
import pytest

from Adv_Dark_Deep.Char_Creation import race_vs_attribs as rva

with open("male_race_list", "rb") as male_list:
    male_list = pickle.load(male_list)


# with open("female_race_list", "rb") as female_list:
#     female_list = pickle.load(female_list)


class TestRaceVsAttribs:
    def test_human(self):
        for i in range(len(male_list)):
            if male_list[i]["CON"] < 6:
                assert male_list[i]["races"] == []

    def test_male_dwarf(self):
        for i in range(len(male_list)):
            if male_list[i]["STR"] >= 8 and 12 <= male_list[i]["CON"] <= 19 and male_list[i]["CHR"] <= 16 \
                    and male_list[i]["DEX"] <= 17:
                assert "dwarf" in male_list[i]["races"]

    def test_male_drow(self):
        for i in range(len(male_list)):
            if male_list[i]["IQ"] >= 8 and male_list[i]["CON"] >= 7 and male_list[i]["CHR"] >= 8 \
                    and 7 <= male_list[i]["DEX"] <= 19:
                assert "dark elf" in male_list[i]["races"]
        #     if male_list[i]["CON"] == 19:
        #         assert "halfling" in male_list[i]["races"]
        #         assert "half orc" in male_list[i]["races"]
        #     if male_list[i]["IQ"] == 19:
        #         assert "grey elf" in male_list[i]["races"]
        #     if male_list[i]["DEX"] == 19:
        #         assert "dark elf" in male_list[i]["races"]
        #         assert "high elf" in male_list[i]["races"]
        # # print(make_male_list())
