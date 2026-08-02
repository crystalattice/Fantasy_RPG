from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

SCHEMA_VERSION = 1


@dataclass(slots=True)
class Identity:
    name: str = ""
    race: str = ""
    alignment: str = ""
    age: int | None = None
    gender: str = ""
    social_class: str = ""
    height_inches: int | None = None
    weight_pounds: int | None = None


@dataclass(slots=True)
class AbilityScores:
    strength: int | None = None
    exceptional_strength: int | None = None
    dexterity: int | None = None
    intelligence: int | None = None
    wisdom: int | None = None
    constitution: int | None = None
    charisma: int | None = None


@dataclass(slots=True)
class DerivedAbilities:
    strength_to_hit: int | None = None
    strength_damage: int | None = None
    strength_weight: int | None = None
    open_stuck_doors: float | None = None
    open_locked_doors: float | None = None
    bend_bars_lift_gates: int | None = None

    initiative_adjustment: int | None = None
    missile_adjustment: int | None = None
    armor_class_adjustment: int | None = None

    maximum_languages: int | None = None
    immunity_to_illusion: str | int | None = None
    maximum_spell_level: int | None = None

    magical_attack_adjustment: int | None = None
    cleric_bonus_spells: str | int | None = None
    spell_failure_chance: int | None = None
    immunity_to_charm: str | int | None = None

    hit_point_adjustment: int | None = None
    system_shock_chance: int | None = None
    resurrection_survival_chance: int | None = None

    maximum_henchmen: int | None = None
    morale_adjustment: int | None = None
    reaction_adjustment: int | None = None


@dataclass(slots=True)
class CharacterClass:
    name: str
    level: int = 1
    experience: int = 0


@dataclass(slots=True)
class Character:
    """Canonical character record derived from the existing ADD PyQt sheet.

    The model deliberately contains the full character-sheet spine while allowing
    incomplete values during guided creation. Validation determines whether a
    character is complete enough to save as a finished PC.
    """

    character_id: str
    identity: Identity = field(default_factory=Identity)
    abilities: AbilityScores = field(default_factory=AbilityScores)
    derived: DerivedAbilities = field(default_factory=DerivedAbilities)
    classes: list[CharacterClass] = field(default_factory=list)
    languages: list[str] = field(default_factory=list)
    secondary_skills: list[str] = field(default_factory=list)
    proficiencies: list[str] = field(default_factory=list)
    inventory: list[dict[str, Any]] = field(default_factory=list)
    spells: list[dict[str, Any]] = field(default_factory=list)
    notes: str = ""
    creation_log: list[dict[str, Any]] = field(default_factory=list)
    schema_version: int = SCHEMA_VERSION

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Character":
        return cls(
            character_id=str(data["character_id"]),
            identity=Identity(**data.get("identity", {})),
            abilities=AbilityScores(**data.get("abilities", {})),
            derived=DerivedAbilities(**data.get("derived", {})),
            classes=[CharacterClass(**item) for item in data.get("classes", [])],
            languages=list(data.get("languages", [])),
            secondary_skills=list(data.get("secondary_skills", [])),
            proficiencies=list(data.get("proficiencies", [])),
            inventory=list(data.get("inventory", [])),
            spells=list(data.get("spells", [])),
            notes=str(data.get("notes", "")),
            creation_log=list(data.get("creation_log", [])),
            schema_version=int(data.get("schema_version", 1)),
        )

    @classmethod
    def from_legacy_pyqt(cls, character_id: str, values: dict[str, Any]) -> "Character":
        """Convert the dictionary shape used by Archived/Qt_Designer/Char_Sheet.py."""

        def optional_int(value: Any) -> int | None:
            if value in (None, "", "None"):
                return None
            return int(value)

        classes = []
        for key in ("class", "second_class", "third_class"):
            value = values.get(key)
            if value and value != "None":
                classes.append(CharacterClass(name=str(value)))

        return cls(
            character_id=character_id,
            identity=Identity(
                name=str(values.get("char_name", values.get("name", ""))),
                race=str(values.get("race", "")),
                alignment=str(values.get("alignment", "")),
                age=optional_int(values.get("age")),
                gender=str(values.get("gender", "")),
                social_class=str(values.get("social_class", "")),
                height_inches=optional_int(values.get("height")),
                weight_pounds=optional_int(values.get("weight")),
            ),
            abilities=AbilityScores(
                strength=optional_int(values.get("str", values.get("char_str"))),
                exceptional_strength=optional_int(
                    values.get("char_bonus_str", values.get("exceptional_strength"))
                ),
                dexterity=optional_int(values.get("char_dex")),
                intelligence=optional_int(values.get("char_iq")),
                wisdom=optional_int(values.get("char_wis")),
                constitution=optional_int(values.get("char_con")),
                charisma=optional_int(values.get("char_chr")),
            ),
            derived=DerivedAbilities(
                strength_to_hit=optional_int(values.get("to_hit_bonus")),
                strength_damage=optional_int(values.get("dam_bonus")),
                strength_weight=optional_int(values.get("carry_bonus")),
                open_stuck_doors=_optional_float(values.get("stuck_doors")),
                open_locked_doors=_optional_float(values.get("locked_doors")),
                bend_bars_lift_gates=optional_int(values.get("bend_bars")),
                initiative_adjustment=optional_int(values.get("init_adj")),
                missile_adjustment=optional_int(values.get("missile_adj")),
                armor_class_adjustment=optional_int(values.get("ac_adj")),
                maximum_languages=optional_int(values.get("max_lang")),
                immunity_to_illusion=values.get("immune_to_illusion"),
                maximum_spell_level=optional_int(values.get("max_spell_level")),
                magical_attack_adjustment=optional_int(values.get("magical_attack_adj")),
                cleric_bonus_spells=values.get("cleric_spell_bonus"),
                spell_failure_chance=optional_int(values.get("spell_failure")),
                immunity_to_charm=values.get("immune_charm"),
                hit_point_adjustment=optional_int(values.get("hp_adj")),
                system_shock_chance=optional_int(values.get("system_shock")),
                resurrection_survival_chance=optional_int(values.get("resurrect")),
                maximum_henchmen=optional_int(values.get("max_henchmen")),
                morale_adjustment=optional_int(values.get("morale_adj")),
                reaction_adjustment=optional_int(values.get("reaction_adj")),
            ),
            classes=classes,
        )


def _optional_float(value: Any) -> float | None:
    if value in (None, "", "None"):
        return None
    return float(value)
