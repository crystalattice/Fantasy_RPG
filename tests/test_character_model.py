from pathlib import Path

from src.characters import (
    AbilityScores,
    Character,
    CharacterClass,
    CharacterRepository,
    Identity,
    validate_character,
)


def make_character() -> Character:
    return Character(
        character_id="reginald",
        identity=Identity(
            name="Reginald",
            race="Human",
            alignment="Lawful Good",
            age=22,
            gender="Male",
            social_class="Freeman",
            height_inches=72,
            weight_pounds=190,
        ),
        abilities=AbilityScores(
            strength=18,
            exceptional_strength=76,
            dexterity=13,
            intelligence=10,
            wisdom=12,
            constitution=16,
            charisma=11,
        ),
        classes=[CharacterClass(name="Fighter")],
    )


def test_character_json_round_trip(tmp_path: Path) -> None:
    repository = CharacterRepository(tmp_path)
    original = make_character()

    path = repository.save(original)
    loaded = repository.load(original.character_id)

    assert path == tmp_path / "reginald.json"
    assert loaded == original
    assert repository.list_ids() == ["reginald"]


def test_legacy_pyqt_conversion() -> None:
    legacy = {
        "char_name": "Reginald",
        "str": "18",
        "char_bonus_str": "76",
        "char_dex": "13",
        "char_iq": "10",
        "char_wis": "12",
        "char_con": "16",
        "char_chr": "11",
        "race": "Human",
        "class": "Fighter",
        "second_class": "None",
        "third_class": "None",
        "alignment": "Lawful Good",
        "age": "22",
        "gender": "Male",
        "social_class": "Freeman",
        "height": "72",
        "weight": "190",
        "to_hit_bonus": "2",
        "dam_bonus": "4",
    }

    character = Character.from_legacy_pyqt("reginald", legacy)

    assert character.identity.name == "Reginald"
    assert character.abilities.exceptional_strength == 76
    assert character.classes == [CharacterClass(name="Fighter")]
    assert character.derived.strength_damage == 4


def test_complete_character_is_structurally_valid() -> None:
    assert validate_character(make_character()) == []


def test_exceptional_strength_requires_strength_18() -> None:
    character = make_character()
    character.abilities.strength = 17

    issues = validate_character(character)

    assert any(issue.field == "abilities.exceptional_strength" for issue in issues)


def test_incomplete_character_can_be_saved_as_draft() -> None:
    character = Character(character_id="draft", identity=Identity(name="Draft"))

    assert validate_character(character, complete_pc=False) == []
