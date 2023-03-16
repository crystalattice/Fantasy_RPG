import pytest

from Adv_Dark_Deep.Char_Creation.Archived.basic_character import Character


class TestCharacterCreation:
    def test_empty_char(self):
        """Confirm all variables are properly created and initialized"""
        c = Character()
        assert c.strength == 0.0
        assert c.dexterity == 0
        assert c.intelligence == 0
        assert c.wisdom == 0
        assert c.constitution == 0
        assert c.charisma == 0
        assert c.ppd_save == 0
        assert c.pp_save == 0
        assert c.bw_save == 0
        assert c.rsw_save == 0
        assert c.spell_save == 0
        assert c.name == ''
        assert c.gender == ''
        assert c.race == ''
        assert c.subrace == ''
        assert c.social_class == ''
        assert c.alignment == ''
        assert c.age == 0
        assert c.height == 0.0
        assert c.weight == 0
        assert c.special_abilities == []
        assert c.experience == 0
        assert c.level == 0
        assert c.char_class == {}
        assert c.languages == []
        assert c.armour_class == 0
        assert c.hit_points == 0
        assert c.non_lethal_wounds == 0
        assert c.armour_worn == ''
        assert c.init_mod == 0
        assert c.surprise_mod == 0
        assert c.attack_column == ''
        assert c.weapons == {}
        assert c.skills == {}
        assert c.class_abilities == {}
        assert c.supplies == {}
        assert c.equipment == {}
        assert c.encumbrance == 0
        assert c.base_move == 0
        assert c.move_rate == 0
        assert c.magic_items == {}
        assert c.deeds_titles == ''
        assert c.spells_memorized == []
        assert c.spell_components == {}
        assert c.max_spells_memorized == {}


class TestAbilityRolls:
    def test_abilities_3d6(self):
        c = Character()
        c.ability_rolls(1)
        assert 3 <= c.strength <= 18
        assert 3 <= c.intelligence <= 18
        assert 3 <= c.wisdom <= 18
        assert 3 <= c.dexterity <= 18
        assert 3 <= c.constitution <= 18
        assert 3 <= c.charisma <= 18

    def test_abilities_4d6(self):
        c = Character()
        c.ability_rolls(2)
        assert 3 <= c.strength <= 18
        assert 3 <= c.intelligence <= 18
        assert 3 <= c.wisdom <= 18
        assert 3 <= c.dexterity <= 18
        assert 3 <= c.constitution <= 18
        assert 3 <= c.charisma <= 18

    def test_abilities_2d6(self):
        c = Character()
        c.ability_rolls(3)
        assert 3 <= c.strength <= 18
        assert 3 <= c.intelligence <= 18
        assert 3 <= c.wisdom <= 18
        assert 3 <= c.dexterity <= 18
        assert 3 <= c.constitution <= 18
        assert 3 <= c.charisma <= 18


class TestCharName:
    def test_name_set(self):
        c = Character()
        c.char_name("Sir Hector")
        assert c.name == "Sir Hector"

    def test_name_empty(self, monkeypatch):
        """Dynamically allow argument to be passed to input() function.

        Since char_name() uses input() to capture a character's name from the user, the monkeypatch calls the built-in
        function input() and uses a lambda function to pass an argument to input(). This argument is then passed to
        char_name() as if the user provided it.
        """
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "Sir Hector")
        c.char_name()
        assert c.name == "Sir Hector"


class TestCharGender:
    def test_male_letter(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "m")
        c.char_gender()
        assert c.gender == "Male"

    def test_male_word(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "male")
        c.char_gender()
        assert c.gender == "Male"

    def test_female_letter(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "f")
        c.char_gender()
        assert c.gender == "Female"

    def test_female_word(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "female")
        c.char_gender()
        assert c.gender == "Female"

    def test_invalid(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "123")
        with pytest.raises(ValueError) as excinfo:
            c.char_gender()
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Invalid selection"


class TestCharRace:
    def test_dwarf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "1")
        c.char_race()
        assert c.race == "Dwarf"

        approved_classes = c.multiclass_by_race()
        assert approved_classes == ["cleric/fighter",
                                    "cleric/thief (inc. acrobat)",
                                    "fighter/mountebank",
                                    "fighter/thief (inc. acrobat)"]

    def test_elf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_race()
        assert c.race == "Elf"

    def test_gnome(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "3")
        c.char_race()
        assert c.race == "Gnome"

    def test_halfling(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "4")
        c.char_race()
        assert c.race == "Halfling"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Jester', 'Cleric', 'Druid', 'Mystic', 'Fighter', 'Thief', 'Acrobat',
                                    'Mountebank']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["cleric/fighter",
                                         "cleric/thief (inc. acrobat)",
                                         "druid/fighter",
                                         "druid/thief (inc. acrobat)",
                                         "fighter/mountebank",
                                         "fighter/thief (inc. acrobat)",
                                         "jester/thief (inc. acrobat)",
                                         "mystic/fighter"]

    def test_half_orc(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "5")
        c.char_race()
        assert c.race == "Half-Orc"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Cleric', 'Fighter', 'Barbarian', 'Thief', 'Acrobat', 'Mountebank']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["cleric/fighter",
                                         "cleric/mountebank",
                                         "cleric/thief (inc. acrobat)",
                                         "fighter/mountebank",
                                         "fighter/thief (inc. acrobat)"]

    def test_human(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "6")
        c.char_race()
        assert c.race == "Human"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Jester', 'Cavalier', 'Paladin', 'Cleric', 'Druid', 'Mystic', 'Fighter',
                                    'Barbarian', 'Ranger', 'Mage', 'Illusionist', 'Savant', 'Thief', 'Acrobat',
                                    'Mountebank']

    def test_invalid(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "123")
        with pytest.raises(ValueError) as excinfo:
            c.char_race()
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Invalid selection"


class TestDwarfSubRace:
    def test_hill_dwarf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "1")
        c.char_race()
        assert c.race == "Dwarf"

        monkeypatch.setattr("builtins.input", lambda x: "1")
        c.char_subrace(1)
        assert c.subrace == "Hill Dwarf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Cleric', 'Fighter', 'Thief', 'Acrobat', 'Mountebank']

    def test_mtn_dwarf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "1")
        c.char_race()
        assert c.race == "Dwarf"

        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_subrace(1)
        assert c.subrace == "Mountain Dwarf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Cleric', 'Fighter', 'Thief', 'Acrobat', 'Mountebank']

    def test_grey_dwarf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "1")
        c.char_race()
        assert c.race == "Dwarf"

        monkeypatch.setattr("builtins.input", lambda x: "3")
        c.dm_underdark = True
        c.char_subrace(1)
        assert c.subrace == "Grey Dwarf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Cleric', 'Fighter', 'Thief', 'Acrobat', 'Mountebank']


class TestElfSubRace:
    def test_grey_elf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_race()
        assert c.race == "Elf"

        monkeypatch.setattr("builtins.input", lambda x: "1")
        c.char_subrace(2)
        assert c.subrace == "Grey Elf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Cleric', 'Druid', 'Mystic', 'Fighter', 'Ranger', 'Mage', 'Savant', 'Thief']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["cleric/fighter",
                                         "cleric/fighter/mage",
                                         "cleric/mage",
                                         "cleric/ranger",
                                         "cleric/ranger/mage",
                                         "cleric/savant",
                                         "cleric/thief (inc. acrobat)",
                                         "druid/ranger",
                                         "fighter/mage/mountebank",
                                         "fighter/mage/thief (inc. acrobat)",
                                         "fighter/mountebank",
                                         "fighter/savant/mountebank",
                                         "fighter/savant/thief (inc. acrobat)",
                                         "fighter/thief (inc. acrobat)",
                                         "mage (inc. savant)/thief (inc. acrobat)",
                                         "mage/mountebank",
                                         "savant/mountebank"]

    def test_half_elf(self, monkeypatch):
        """Half-elves use the same multi-classes as their elven parent's race"""
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_race()
        assert c.race == "Elf"

        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_subrace(2)
        assert c.subrace == "Half-Elf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Cavalier', 'Cleric', 'Druid', 'Mystic', 'Fighter', 'Ranger', 'Mage',
                                    'Savant', 'Thief', 'Mountebank']

    def test_high_elf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_race()
        assert c.race == "Elf"

        monkeypatch.setattr("builtins.input", lambda x: "3")
        c.char_subrace(2)
        assert c.subrace == "High Elf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Cavalier', 'Cleric', 'Druid', 'Mystic', 'Fighter', 'Ranger', 'Mage',
                                    'Savant', 'Thief', 'Mountebank']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["cleric/fighter",
                                         "cleric/fighter/mage",
                                         "cleric/fighter/savant",
                                         "cleric/mage",
                                         "cleric/ranger",
                                         "cleric/ranger/mage",
                                         "cleric/ranger/savant",
                                         "cleric/savant",
                                         "cleric/thief (inc. acrobat)",
                                         "druid/ranger",
                                         "fighter/mage",
                                         "fighter/mage (inc. savant)/thief (inc. acrobat or mountebank)",
                                         "fighter/mage/mountebank",
                                         "fighter/mountebank",
                                         "fighter/savant",
                                         "fighter/savant/mountebank",
                                         "fighter/savant/thief",
                                         "fighter/thief (inc. acrobat)",
                                         "mage (inc. savant)/thief (inc. acrobat or mountebank)",
                                         "mystic/fighter",
                                         "mystic/fighter/mage",
                                         "mystic/mage",
                                         "mystic/ranger",
                                         "mystic/savant",
                                         "mystic/thief (inc. acrobat)",
                                         "ranger/mage",
                                         "ranger/savant"]

    def test_wild_elf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_race()
        assert c.race == "Elf"

        monkeypatch.setattr("builtins.input", lambda x: "4")
        c.char_subrace(2)
        assert c.subrace == "Wild Elf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Druid', 'Mystic', 'Fighter', 'Thief', 'Acrobat']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["fighter/thief (inc. acrobat)"]

    def test_wood_elf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_race()
        assert c.race == "Elf"

        monkeypatch.setattr("builtins.input", lambda x: "5")
        c.char_subrace(2)
        assert c.subrace == "Wood Elf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Cleric', 'Druid', 'Mystic', 'Fighter', 'Ranger', 'Mage', 'Thief', 'Acrobat',
                                    'Mountebank']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["cleric/fighter",
                                         "cleric/fighter/mage",
                                         "cleric/ranger",
                                         "cleric/ranger/mage",
                                         "cleric/thief (inc. acrobat)",
                                         "druid/ranger",
                                         "fighter/mage",
                                         "fighter/mage/mountebank",
                                         "fighter/mage/thief (inc. acrobat)",
                                         "fighter/mountebank",
                                         "fighter/thief (inc. acrobat)",
                                         "mage/mountebank",
                                         "mage/thief (inc. acrobat)",
                                         "mystic/fighter",
                                         "mystic/fighter/mage",
                                         "mystic/mage",
                                         "mystic/ranger",
                                         "mystic/ranger/mage",
                                         "mystic/thief (inc. acrobat)"]

    def test_dark_elf(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_race()
        assert c.race == "Elf"

        monkeypatch.setattr("builtins.input", lambda x: "6")
        c.dm_underdark = True
        c.char_subrace(2)
        assert c.subrace == "Dark Elf"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Cavalier', 'Cleric', 'Fighter', 'Ranger', 'Mage', 'Savant', 'Thief',
                                    'Acrobat', 'Mountebank']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["cleric/fighter",
                                         "cleric/fighter/mage",
                                         "cleric/fighter/savant",
                                         "cleric/mage",
                                         "cleric/savant",
                                         "cleric/thief (inc. acrobat)",
                                         "fighter/mage",
                                         "fighter/mage (inc. savant)/thief (inc. acrobat)",
                                         "fighter/mage/mountebank",
                                         "fighter/mountebank",
                                         "fighter/savant",
                                         "fighter/savant/mountebank",
                                         "fighter/savant/thief (inc. acrobat)",
                                         "fighter/thief (inc. acrobat)",
                                         "mage/mountebank",
                                         "mage/thief (inc. acrobat)"]


class TestGnomeSubRace:
    def test_forest_gnome(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "3")
        c.char_race()
        assert c.race == "Gnome"

        monkeypatch.setattr("builtins.input", lambda x: "1")
        c.char_subrace(3)
        assert c.subrace == "Forest Gnome"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Jester', 'Druid', 'Fighter', 'Savant', 'Thief', 'Acrobat', 'Mountebank']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["druid/fighter",
                                         "druid/thief (inc. acrobat)",
                                         "fighter/savant",
                                         "fighter/thief (inc. acrobat)",
                                         "illusionist/mountebank",
                                         "jester/fighter",
                                         "savant/thief",
                                         "savant/mountebank"]

    def test_hill_gnome(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "3")
        c.char_race()
        assert c.race == "Gnome"

        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.char_subrace(3)
        assert c.subrace == "Hill Gnome"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Cleric', 'Fighter', 'Illusionist', 'Thief', 'Acrobat', 'Mountebank']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["cleric/fighter",
                                         "cleric/thief (inc. acrobat)",
                                         "druid/fighter",
                                         "druid/thief (inc. acrobat)",
                                         "fighter/mountebank",
                                         "fighter/thief (inc. acrobat)",
                                         "jester/thief (inc. acrobat)",
                                         "mystic/fighter"]

    def test_deep_gnome(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "3")
        c.char_race()
        assert c.race == "Gnome"

        monkeypatch.setattr("builtins.input", lambda x: "3")
        c.dm_underdark = True
        c.char_subrace(3)
        assert c.subrace == "Deep Gnome"

        approved_classes = c.class_by_race()
        assert approved_classes == ['Bard', 'Cleric', 'Fighter', 'Illusionist', 'Thief', 'Acrobat', 'Mountebank']

        approved_multiclasses = c.multiclass_by_race()
        assert approved_multiclasses == ["cleric/fighter",
                                         "cleric/thief (inc. acrobat)",
                                         "fighter/illusionist",
                                         "fighter/mountebank",
                                         "fighter/thief (inc. acrobat)",
                                         "illusionist/mountebank",
                                         "illusionist/thief (inc. acrobat)",
                                         "jester/fighter"]


class TestSocialClass:
    def test_argument(self):
        c = Character()
        c.set_social_class("Middle-Middle Class")
        assert c.social_class == "Middle-Middle Class"

    def test_random_roll(self):
        c = Character()
        c.set_social_class()
        print(c.social_class)
        assert c.social_class in ["Lower-Lower Class", "Middle-Lower Class", "Upper-Lower Class", "Lower-Middle Class",
                                  "Middle-Middle Class", "Upper-Middle Class", "Lower-Upper Class",
                                  "Middle-Upper Class", "Upper-Upper Class"]


class TestAlignment:
    def test_invalid_input(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "Lawful Good")
        with pytest.raises(ValueError):
            c.set_alignment()

    def test_invalid_number(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "11")
        with pytest.raises(KeyError):
            c.set_alignment()

    def test_lawful_good(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "1")
        c.set_alignment()
        assert c.alignment == "Lawful Good"

    def test_lawful_neutral(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "2")
        c.set_alignment()
        assert c.alignment == "Lawful Neutral"

    def test_lawful_evil(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "3")
        c.set_alignment()
        assert c.alignment == "Lawful Evil"

    def test_neutral_good(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "4")
        c.set_alignment()
        assert c.alignment == "Neutral Good"

    def test_neutral(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "5")
        c.set_alignment()
        assert c.alignment == "Neutral"

    def test_neutral_evil(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "6")
        c.set_alignment()
        assert c.alignment == "Neutral Evil"

    def test_chaotic_good(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "7")
        c.set_alignment()
        assert c.alignment == "Chaotic Good"

    def test_chaotic_neutral(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "8")
        c.set_alignment()
        assert c.alignment == "Chaotic Neutral"

    def test_chaotic_evil(self, monkeypatch):
        c = Character()
        monkeypatch.setattr("builtins.input", lambda x: "9")
        c.set_alignment()
        assert c.alignment == "Chaotic Evil"
