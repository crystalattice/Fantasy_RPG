from typing import Optional, Dict, List


class Hireling:
    """
    Represents a hireling with specific skills, wages, and other attributes.
    """

    HIRELING_CATALOG = {
        'Alchemist': {'monthly_wage': 300, 'daily_wage': None, 'skills': ['Alchemy']},
        'Bearer/Porter': {'monthly_wage': 1, 'daily_wage': 0.1, 'skills': []},
        'Drover': {'monthly_wage': 5, 'daily_wage': 0.5, 'skills': ['Animal Handling']},
        'Jeweler': {'monthly_wage': 100, 'daily_wage': None, 'skills': ['Jeweler']},
        'Lantern-bearer': {'monthly_wage': 1, 'daily_wage': 0.5, 'skills': []},
        'Leather Worker': {'monthly_wage': 0.2, 'daily_wage': 3, 'skills': []},
        'Marine': {'monthly_wage': 3, 'daily_wage': None, 'skills': ['Fighter']},
        'Oarsman': {'monthly_wage': 5, 'daily_wage': None, 'skills': ['Seamanship']},
        'Pack Handler': {'monthly_wage': 3, 'daily_wage': 0.2, 'skills': ['Animal Handling']},
        'Sage': {'monthly_wage': 'Special', 'daily_wage': 'Special', 'skills': ['Scholarship']},
        'Sailor': {'monthly_wage': 2, 'daily_wage': None, 'skills': ['Seamanship']},
        'Ship’s Master': {'monthly_wage': 100, 'daily_wage': None, 'skills': ['Seamanship']},
        'Ship’s Mate': {'monthly_wage': 30, 'daily_wage': None, 'skills': ['Seamanship']},
        'Valet/Lackey': {'monthly_wage': 0.5, 'daily_wage': 0.3, 'skills': []},
    }

    WAGE_MULTIPLIERS = {
        1: 1,
        2: 4,
        3: 10,
        4: 19,
        5: 31,
    }

    def __init__(self, name: str, skill_level: int = 1):
        if name not in self.HIRELING_CATALOG:
            raise ValueError(f"Hireling '{name}' is not recognized.")
        self.name: str = name
        self.skill_level: int = skill_level
        self.skills: List[str] = self.HIRELING_CATALOG[name]['skills']
        self.base_monthly_wage: Optional[float] = self.HIRELING_CATALOG[name]['monthly_wage']
        self.base_daily_wage: Optional[float] = self.HIRELING_CATALOG[name]['daily_wage']

    @property
    def monthly_wage(self) -> Optional[float]:
        """Calculate the monthly wage based on the skill level."""
        if self.base_monthly_wage is not None and isinstance(self.base_monthly_wage, (int, float)):
            return self.base_monthly_wage * self.WAGE_MULTIPLIERS[self.skill_level]
        return self.base_monthly_wage

    @property
    def daily_wage(self) -> Optional[float]:
        """Calculate the daily wage based on the skill level."""
        if self.base_daily_wage is not None and isinstance(self.base_daily_wage, (int, float)):
            return self.base_daily_wage * self.WAGE_MULTIPLIERS[self.skill_level]
        return self.base_daily_wage

    def get_hireling_info(self) -> Dict[str, Optional[float]]:
        """Return the details of the hireling."""
        return {
            'name': self.name,
            'skill_level': self.skill_level,
            'skills': self.skills,
            'monthly_wage': self.monthly_wage,
            'daily_wage': self.daily_wage,
        }

    def __repr__(self) -> str:
        """Return a string representation of the hireling."""
        return (f"Hireling({self.name}, Skill Level {self.skill_level}, "
                f"Monthly Wage: {self.monthly_wage} g.p., Daily Wage: {self.daily_wage} g.p.)")


class Sage(Hireling):
    """
    Represents a sage with additional attributes for long-term employment.
    """

    def __init__(self, skill_level: int = 1):
        super().__init__('Sage', skill_level)
        self.initial_material_expenditure: int = 20000
        self.research_grants: int = 200 * self.skill_level

    def calculate_initial_efficiency(self) -> float:
        """
        Calculate the initial efficiency based on the initial material expenditure.
        """
        efficiency = 50 + (self.initial_material_expenditure - 20000) / 1000
        return min(100, efficiency)

    def __repr__(self) -> str:
        """Return a string representation of the sage."""
        return (f"Sage(Skill Level {self.skill_level}, Monthly Wage: {self.monthly_wage} g.p., "
                f"Research Grants: {self.research_grants} g.p., Initial Efficiency: {self.calculate_initial_efficiency()}%)")


# Example Usage
if __name__ == "__main__":
    # Create a hireling (e.g., a Jeweler with skill level 2)
    jeweler = Hireling('Jeweler', skill_level=2)

    # Display hireling details
    hireling_info = jeweler.get_hireling_info()
    print(f"Hireling Info: {hireling_info}")

    # Represent the hireling
    print(jeweler)

    # Create a sage and calculate initial efficiency
    sage = Sage(skill_level=3)
    print(sage)
