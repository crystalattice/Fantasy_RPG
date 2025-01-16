import json

def load_skills(skill_progression, level):
    """Load skills for a given level from progression data."""
    return {
        skill: skill_progression.get(skill, {}).get(str(level), 0.0)
        for skill in skill_progression
    }

def apply_armor_penalties(skills, armor_penalties, armor_type):
    """Apply armor penalties to a set of skills."""
    penalties = armor_penalties.get(armor_type, {})
    return {
        skill: max(0, skills.get(skill, 0.0) + penalties.get(skill, 0))
        for skill in skills
    }

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as file:
        return json.load(file)
