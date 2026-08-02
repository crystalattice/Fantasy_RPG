from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .model import Character

Severity = Literal["error", "warning"]


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    field: str
    message: str
    severity: Severity = "error"


def validate_character(character: Character, *, complete_pc: bool = True) -> list[ValidationIssue]:
    """Validate structural invariants without duplicating rules-table logic.

    Race, class, alignment, proficiency, spell, and equipment legality should be
    delegated to the canonical ADD rules services as those are extracted from the
    existing character-creation code and JSON tables.
    """

    issues: list[ValidationIssue] = []

    if not character.character_id.strip():
        issues.append(ValidationIssue("character_id", "Character ID is required."))
    if not character.identity.name.strip():
        issues.append(ValidationIssue("identity.name", "Character name is required."))

    ability_values = {
        "strength": character.abilities.strength,
        "dexterity": character.abilities.dexterity,
        "intelligence": character.abilities.intelligence,
        "wisdom": character.abilities.wisdom,
        "constitution": character.abilities.constitution,
        "charisma": character.abilities.charisma,
    }
    for name, value in ability_values.items():
        if value is None:
            if complete_pc:
                issues.append(ValidationIssue(f"abilities.{name}", f"{name.title()} is required."))
            continue
        if not 1 <= value <= 25:
            issues.append(
                ValidationIssue(f"abilities.{name}", f"{name.title()} must be between 1 and 25.")
            )

    exceptional = character.abilities.exceptional_strength
    if exceptional is not None:
        if character.abilities.strength != 18:
            issues.append(
                ValidationIssue(
                    "abilities.exceptional_strength",
                    "Exceptional strength is only valid when Strength is 18.",
                )
            )
        if not 1 <= exceptional <= 100:
            issues.append(
                ValidationIssue(
                    "abilities.exceptional_strength",
                    "Exceptional strength must be between 1 and 100.",
                )
            )

    if complete_pc:
        if not character.identity.gender.strip():
            issues.append(ValidationIssue("identity.gender", "Gender is required."))
        if not character.identity.race.strip():
            issues.append(ValidationIssue("identity.race", "Race is required."))
        if not character.classes:
            issues.append(ValidationIssue("classes", "At least one class is required."))
        if not character.identity.alignment.strip():
            issues.append(ValidationIssue("identity.alignment", "Alignment is required."))

    if len(character.classes) > 3:
        issues.append(ValidationIssue("classes", "A character may not have more than three classes."))

    seen_classes: set[str] = set()
    for index, character_class in enumerate(character.classes):
        field = f"classes[{index}]"
        normalized_name = character_class.name.strip().casefold()
        if not normalized_name:
            issues.append(ValidationIssue(f"{field}.name", "Class name is required."))
        elif normalized_name in seen_classes:
            issues.append(ValidationIssue(field, "Duplicate classes are not allowed."))
        else:
            seen_classes.add(normalized_name)
        if character_class.level < 1:
            issues.append(ValidationIssue(f"{field}.level", "Class level must be at least 1."))
        if character_class.experience < 0:
            issues.append(ValidationIssue(f"{field}.experience", "Experience may not be negative."))

    for field, value in (
        ("identity.age", character.identity.age),
        ("identity.height_inches", character.identity.height_inches),
        ("identity.weight_pounds", character.identity.weight_pounds),
    ):
        if value is not None and value <= 0:
            issues.append(ValidationIssue(field, "Value must be greater than zero."))

    return issues
