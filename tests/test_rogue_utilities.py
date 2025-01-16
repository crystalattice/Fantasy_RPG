import pytest
from src.utils.rogue_utilities import load_skills, apply_armor_penalties

@pytest.fixture
def sample_skills():
    return {
        "pick_pockets": 35,
        "open_locks": 29,
        "move_silently": 21,
        "hide_in_shadows": 15,
        "listen_at_doors": 10
    }

@pytest.fixture
def armor_penalties():
    return {
        "Plate armor": {
            "pick_pockets": -75,
            "open_locks": -40,
            "move_silently": -80,
            "hide_in_shadows": -75
        }
    }

def test_load_skills():
    skill_progression = {
        "pick_pockets": {"3": 30, "4": 35},
        "open_locks": {"3": 25, "4": 29}
    }
    level = 4
    expected = {"pick_pockets": 35, "open_locks": 29}
    assert load_skills(skill_progression, level) == expected

def test_apply_armor_penalties(sample_skills, armor_penalties):
    result = apply_armor_penalties(sample_skills, armor_penalties, "Plate armor")
    expected = {
        "pick_pockets": 0,
        "open_locks": 0,
        "move_silently": 0,
        "hide_in_shadows": 0,
        "listen_at_doors": 10  # No penalty defined
    }
    assert result == expected
