import random
from typing import Dict


def calculate_potential_henchmen(population: int, density: str = "normal") -> int:
    """
    Calculate the number of potential henchmen in a given population.

    :param population: The population of the location.
    :param density: The density of adventurers ('high', 'normal', 'low').
    :return: Number of potential henchmen.
    """
    if density == "high":
        return population // 200
    elif density == "low":
        return population // 5000
    else:
        return population // 1000


def find_henchmen(method: str, potential_henchmen: int) -> int:
    """
    Determine how many henchmen respond based on the chosen method.

    :param method: The method used to find henchmen ('inns', 'crier', 'notices', 'agents').
    :param potential_henchmen: The total number of potential henchmen.
    :return: Number of henchmen responding.
    """
    if method == "inns":
        response_rate = random.randint(1, 4)
    elif method == "crier":
        response_rate = random.randint(1, 10)
    elif method == "notices":
        response_rate = random.randint(1, 4) * 10
    elif method == "agents":
        response_rate = random.randint(1, 4) * 10 + random.randint(1, 10)
    else:
        response_rate = 0

    return min((response_rate * potential_henchmen) // 100, potential_henchmen)


def check_henchman_limit(charisma: int) -> int:
    """
    Get the maximum number of henchmen a character can have based on charisma.

    :param charisma: The charisma score of the character.
    :return: The maximum number of henchmen.
    """
    charisma_henchmen_limit = {
        3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 4, 10: 4,
        11: 4, 12: 5, 13: 5, 14: 6, 15: 7, 16: 8, 17: 10,
        18: 15, 19: 20
    }
    return charisma_henchmen_limit.get(charisma, 4)


def determine_henchman_class_level(employer_level: int) -> Dict[str, int]:
    """
    Determine the class and level of a potential henchman.

    :param employer_level: The level of the employer.
    :return: A dictionary containing the class and level of the henchman.
    """
    classes = ["Fighter", "Cleric", "Thief", "Mage", "Druid", "Paladin", "Ranger", "Bard", "Mountebank"]
    henchman_class = random.choice(classes)
    henchman_level = 1

    if employer_level >= 11:
        if random.randint(1, 100) <= 25:
            henchman_level = random.choice([2, 3])

    return {"class": henchman_class, "level": henchman_level}


# Example usage:
if __name__ == "__main__":
    population = 20000
    potential_henchmen = calculate_potential_henchmen(population, "normal")

    responding_henchmen = find_henchmen("inns", potential_henchmen)

    charisma = 14
    max_henchmen = check_henchman_limit(charisma)
    print(f"Max Henchmen: {max_henchmen}")

    for _ in range(responding_henchmen):
        henchman = determine_henchman_class_level(12)
        print(f"New Henchman - Class: {henchman['class']}, Level: {henchman['level']}")
