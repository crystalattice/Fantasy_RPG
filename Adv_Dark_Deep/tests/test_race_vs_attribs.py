import pickle
import pytest

# from Adv_Dark_Deep.Char_Creation import race_vs_attribs as rva

with open("male_race_list", "rb") as male_list:
    male_list = pickle.load(male_list)


with open("female_race_list", "rb") as female_list:
    female_list = pickle.load(female_list)


class TestMaleRaceVsAttribs:
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
            if male_list[i]["IQ"] >= 8 and male_list[i]["CON"] >= 6 and male_list[i]["CHR"] >= 8 \
                    and 7 <= male_list[i]["DEX"] <= 19:
                assert "dark elf" in male_list[i]["races"]

    def test_male_grey_elf(self):
        for i in range(len(male_list)):
            if male_list[i]["IQ"] >= 8 and male_list[i]["CON"] >= 6 and male_list[i]["CHR"] >= 8 \
                    and male_list[i]["DEX"] >= 7:
                assert "grey elf" in male_list[i]["races"]

    def test_male_half_elf(self):
        for i in range(len(male_list)):
            if male_list[i]["IQ"] >= 4 and male_list[i]["CON"] >= 6 and male_list[i]["DEX"] >= 6:
                assert "half elf" in male_list[i]["races"]

    def test_male_high_elf(self):
        for i in range(len(male_list)):
            if male_list[i]["IQ"] >= 8 and male_list[i]["CON"] >= 6 and male_list[i]["CHR"] >= 8 \
                    and 7 <= male_list[i]["DEX"] <= 19:
                assert "high elf" in male_list[i]["races"]

    def test_male_wild_elf(self):
        for i in range(len(male_list)):
            if 7 <= male_list[i]["IQ"] <= 17 and male_list[i]["CON"] >= 6 and male_list[i]["CHR"] >= 8 \
                    and male_list[i]["DEX"] >= 7:
                assert "wild elf" in male_list[i]["races"]

    def test_male_wood_elf(self):
        for i in range(len(male_list)):
            if 7 <= male_list[i]["IQ"] <= 17 and male_list[i]["CON"] >= 6 and male_list[i]["CHR"] >= 8 \
                    and male_list[i]["DEX"] >= 7:
                assert "wood elf" in male_list[i]["races"]

    def test_male_gnome(self):
        for i in range(len(male_list)):
            if male_list[i]["STR"] >= 6 and male_list[i]["IQ"] >= 7 and male_list[i]["CON"] >= 8:
                assert "gnome" in male_list[i]["races"]

    def test_male_halfling(self):
        for i in range(len(male_list)):
            if 6 <= male_list[i]["STR"] <= 17 and male_list[i]["IQ"] >= 6 and male_list[i]["WIS"] <= 17 \
                    and 10 <= male_list[i]["CON"] <= 19 and male_list[i]["DEX"] >= 8:
                assert "halfling" in male_list[i]["races"]

    def test_male_half_orc(self):
        for i in range(len(male_list)):
            if male_list[i]["STR"] >= 6 and male_list[i]["IQ"] <= 17 and male_list[i]["WIS"] <= 14 \
                    and 13 <= male_list[i]["CON"] <= 19 and male_list[i]["DEX"] <= 17 and male_list[i]["CHR"] <= 12:
                assert "half orc" in male_list[i]["races"]


class TestFemaleRaceVsAttribs:
    def test_human(self):
        for i in range(len(female_list)):
            if female_list[i]["CON"] < 6:
                assert female_list[i]["races"] == []

    def test_female_dwarf(self):
        for i in range(len(female_list)):
            if 8 <= female_list[i]["STR"] <= 17 and 12 <= female_list[i]["CON"] <= 19 and female_list[i]["CHR"] <= 16 \
                    and female_list[i]["DEX"] <= 17:
                assert "dwarf" in female_list[i]["races"]

    def test_female_drow(self):
        for i in range(len(female_list)):
            if female_list[i]["STR"] <= 16 and female_list[i]["IQ"] >= 8 and female_list[i]["CON"] >= 6 \
                    and female_list[i]["CHR"] >= 8 and 7 <= female_list[i]["DEX"] <= 19:
                assert "dark elf" in female_list[i]["races"]

    def test_female_grey_elf(self):
        for i in range(len(female_list)):
            if female_list[i]["STR"] <= 16 and 8 <= female_list[i]["IQ"] <= 19 and female_list[i]["CON"] >= 6 \
                    and female_list[i]["CHR"] >= 8 and female_list[i]["DEX"] >= 7:
                assert "grey elf" in female_list[i]["races"]

    def test_female_half_elf(self):
        for i in range(len(female_list)):
            if female_list[i]["STR"] <= 17 and female_list[i]["IQ"] >= 4 and female_list[i]["CON"] >= 6 \
                    and female_list[i]["DEX"] >= 6:
                assert "half elf" in female_list[i]["races"]

    def test_female_high_elf(self):
        for i in range(len(female_list)):
            if female_list[i]["STR"] <= 16 and female_list[i]["IQ"] >= 8 and female_list[i]["CON"] >= 6 \
                    and female_list[i]["CHR"] >= 8 and 7 <= female_list[i]["DEX"] <= 19:
                assert "high elf" in female_list[i]["races"]

    def test_female_wild_elf(self):
        for i in range(len(female_list)):
            if 7 <= female_list[i]["IQ"] <= 17 and female_list[i]["CON"] >= 6 and female_list[i]["CHR"] >= 8 \
                    and female_list[i]["DEX"] >= 7:
                assert "wild elf" in female_list[i]["races"]

    def test_female_wood_elf(self):
        for i in range(len(female_list)):
            if female_list[i]["STR"] <= 16 and 7 <= female_list[i]["IQ"] <= 17 and female_list[i]["CON"] >= 6 \
                    and female_list[i]["CHR"] >= 8 and female_list[i]["DEX"] >= 7:
                assert "wood elf" in female_list[i]["races"]

    def test_female_gnome(self):
        for i in range(len(female_list)):
            if 6 <= female_list[i]["STR"] <= 15 and female_list[i]["IQ"] >= 7 and female_list[i]["CON"] >= 8:
                assert "gnome" in female_list[i]["races"]

    def test_female_halfling(self):
        for i in range(len(female_list)):
            if 6 <= female_list[i]["STR"] <= 14 and female_list[i]["IQ"] >= 6 and female_list[i]["WIS"] <= 17 \
                    and 10 <= female_list[i]["CON"] <= 19 and female_list[i]["DEX"] >= 8:
                assert "halfling" in female_list[i]["races"]

    def test_female_half_orc(self):
        for i in range(len(female_list)):
            if female_list[i]["STR"] >= 6 and female_list[i]["IQ"] <= 17 and female_list[i]["WIS"] <= 14 \
                    and 13 <= female_list[i]["CON"] <= 19 and female_list[i]["DEX"] <= 17 and female_list[i]["CHR"] <= 12:
                assert "half orc" in female_list[i]["races"]
