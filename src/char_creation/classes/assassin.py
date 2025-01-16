import json
from typing import Dict, List, Optional

class Assassin:
    def __init__(self, race: str, strength: int, dexterity: int, intelligence: int, level: int = 1):
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.level = level
        self.experience_points = 0
        self.hit_points = self.calculate_hit_points()
        self.skill_progression = self.load_json("/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/classes_data/assassin/assassin_skills.json")
        self.skills = self.load_skills()

        # Load JSON data for level limits, skill adjustments, and armor penalties
        self.level_limits = self.load_json("/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/classes_data/assassin/assassin_level_limits.json")
        self.armor_penalties = self.load_json(
            "/home/codyjackson/PycharmProjects/RPGs/data/adventures_dark_deep/classes_data/assassin/assassin_armor_penalties.json"
            )

        self.validate_level()

    @staticmethod
    def load_json(file_path: str) -> Dict:
        try:
            print(f"Loading file: {file_path}")
            with open(file_path, "r") as file:
                data = json.load(file)
                print(f"Loaded data from {file_path}: {data}")
                return data
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return {}

    def calculate_hit_points(self) -> int:
        """Calculate hit points based on level."""
        return sum([self.roll_d6() for _ in range(self.level)])

    @staticmethod
    def roll_d6() -> int:
        import random
        return random.randint(1, 6)

    def validate_level(self):
        """Ensure the level does not exceed racial limits."""
        max_level = self.level_limits.get(self.race, {}).get(str(self.strength), 15)
        if self.level > max_level:
            self.level = max_level

    def load_skills(self) -> Dict[str, float]:
        """Initialize skills based on level and progression table."""
        skills_data = self.skill_progression
        print(f"Skill progression data: {skills_data}")

        loaded_skills = {
            skill: skills_data.get(skill, {}).get(str(self.level), 0.0)
            for skill in skills_data
        }

        print(f"Loaded skills for Level {self.level}: {loaded_skills}")
        return loaded_skills

    def apply_armor_penalties(self, armor_type: str):
        """Apply armor penalties to skills."""
        penalties = self.armor_penalties.get(armor_type, {})
        print(f"Applying armor penalties for: {armor_type}")
        for skill in self.skills:
            penalty = penalties.get(skill, None)
            if penalty is None:
                print(f"  No penalty defined for {skill}")
                continue
            before = self.skills[skill]
            after = max(0, before + penalty)
            self.skills[skill] = after
            print(f"  {skill}: {before}% -> {after}%")

    def level_up(self):
        """Increase level and recalculate skills and hit points."""
        if self.level < 15:  # Maximum level for assassins
            self.level += 1
            self.hit_points += self.roll_d6()
            self.skills = self.load_skills()

    def display_skills(self):
        """Print the current skill percentages."""
        print(f"Skills for {self.race} Assassin (Level {self.level}):")
        for skill, chance in self.skills.items():
            print(f"  {skill}: {chance}%")

    def display_unmodified_skills(self):
        """Print the current unmodified skill percentages."""
        skills_data = self.skill_progression.get("assassin_skills", {})
        unmodified_skills = {
            skill: skills_data.get(skill, {}).get(str(self.level), 0.0)
            for skill in skills_data
        }
        print(f"Unmodified Skills for {self.race} Assassin (Level {self.level}):")
        for skill, chance in unmodified_skills.items():
            print(f"  {skill}: {chance}%")


# Example Usage
if __name__ == "__main__":
    assassin = Assassin(race="Dwarf", strength=18, dexterity=16, intelligence=12, level=4)

    # Display skills before penalties
    assassin.load_skills()
    assassin.display_skills()

    # Apply penalties for Plate armor
    assassin.apply_armor_penalties("Plate armor")
    assassin.display_skills()

