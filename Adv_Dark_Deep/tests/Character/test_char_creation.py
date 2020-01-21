import pytest

from Adv_Dark_Deep.Char_Creation.basic_character import Character


class TestCharacterCreation:
    def test_empty_char(self):
        c = Character()
        assert c.strength == 0.0
        assert c.dexterity == 0
        assert c.intelligence == 0
        assert c.wisdom == 0
        assert c.constitution == 0
        assert c.charisma == 0
        assert c.save_vs_ppd == 0
        assert c.save_vs_pp == 0
        assert c.save_vs_bw == 0
        assert c.save_vs_rsw == 0
        assert c.save_vs_spell == 0
        assert c.name == ''
        assert c.gender == ''
        assert c.race == ''
        assert c.subrace == ''
        assert c.social_class == ''
        assert c.alignment == ''
        assert c.age == 0
        assert c.height == 0.0
        assert c.weight ==0
        assert c.special_abilities == []
        assert c.experience == 0
        assert c.level == 0
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
        assert c.encumberance == 0
        assert c.base_move == 0
        assert c.move_rate == 0
        assert c.magic_items == {}
        assert c.deeds_titles == ''
        assert c.mount_name == ''
        assert c.mount_type == ''
        assert c.mount_hp == 0
        assert c.mount_armour == ''
        assert c.mount_ac == 0
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
