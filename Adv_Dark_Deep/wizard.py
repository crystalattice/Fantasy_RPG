import pickle
import random
from pathlib import Path

# Import relevant functions from modules
from app.models.characters.creation import roll_abilities, get_acceptable_class, race_vs_attribs, con_abilities

# Initialize the character dictionary
character = {}


# Roll for ability scores
def roll_attribs() -> tuple[int, int, int, int, int, int, int]:
    """Prompt user for rolling method and assign values to attributes."""
    roll_method = input(
        "Choose rolling method for abilities: 1 = 4d6 (drop lowest), 2 = 3d6, 3 = 2d6+6. Enter a number: "
        )
    if roll_method == "1":
        rolls = roll_abilities.four_d6_drop_lowest()
    elif roll_method == "2":
        rolls = roll_abilities.three_d6()
    elif roll_method == "3":
        rolls = roll_abilities.two_d6_plus_6()
    else:
        raise ValueError("Invalid choice. Choose option 1, 2, or 3.")

    strength, dex, iq, wis, con, charisma = rolls[:6]
    bonus_strength = roll_abilities.multi_die(1, 100) if strength == 18 else 0

    return strength, bonus_strength, dex, iq, wis, con, charisma


# Choose sex
def get_sex() -> str:
    """Allow user to select character's sex."""
    sex_choice = input("Select your character's sex: [M]ale or [F]emale ").strip().lower()
    if sex_choice == "m":
        return "male"
    elif sex_choice == "f":
        return "female"
    else:
        raise ValueError("Invalid choice. Please enter M or F.")


# Display and select race
def populate_races(sex: str, strength: int, dex: int, iq: int, wis: int, con: int, charisma: int) -> dict[int, str]:
    """Generate available races based on attributes and sex."""
    races = race_vs_attribs.get_acceptable_race(sex, strength, iq, wis, dex, con, charisma)
    possible_races = [race for race in races if race]
    return {i + 1: race for i, race in enumerate(possible_races)}


def get_race(available_races: dict[int, str]) -> str:
    """Prompt user to select a race from available options."""
    for num, race in available_races.items():
        print(f"{num}: {race}")
    race_choice = int(input("Enter the number of your character's race: "))
    return available_races[race_choice]


# Enable class options based on race
def enable_classes(race: str) -> None:
    """Display and allow selection of classes based on race."""
    multi_class_enabled = race != "Human"
    acceptable_classes = ["Bard", "Jester", "Cavalier", "Paladin", "Cleric", "Druid", "Mystic", "Fighter",
                          "Barbarian", "Ranger", "Mage", "Illusionist", "Savant", "Thief", "Thief-Acrobat",
                          "Mountebank", "Assassin"]
    character['class'] = input(f"Select your class ({', '.join(acceptable_classes)}): ").capitalize()
    if multi_class_enabled:
        character['multi_class'] = input("Enter secondary class (optional): ").capitalize()


# Calculate starting HP
def starting_hp(con_bonus: int) -> None:
    """Calculate and store starting HP based on character class and Constitution bonus."""
    class_hp = {
        "Bard": 6, "Jester": 6, "Mystic": 6, "Thief": 6, "Thief-Acrobat": 6, "Mountebank": 6, "Assassin": 6,
        "Cavalier": 10, "Paladin": 10, "Fighter": 10, "Cleric": 8, "Druid": 8, "Barbarian": 12, "Ranger": 16,
        "Mage": 4, "Illusionist": 4, "Savant": 4
    }
    character['hp'] = class_hp.get(character['class'], 4) + con_bonus
    print(f"Starting HP: {character['hp']}")


# Calculate starting money
def starting_money() -> None:
    """Calculate and store starting money based on character class."""
    money_ranges = {
        "Thief": (20, 120), "Thief-Acrobat": (20, 120), "Assassin": (20, 120),
        "Mountebank": (20, 120), "Bard": (20, 120), "Mage": (20, 80), "Illusionist": (20, 80),
        "Savant": (20, 80), "Jester": (20, 80), "Cleric": (30, 180), "Druid": (30, 180), "Mystic": (13, 24),
        "Fighter": (50, 200), "Barbarian": (50, 200), "Ranger": (50, 200), "Cavalier": (70, 140),
        "Paladin": (70, 140)
    }
    char_class = character['class']
    character['money'] = random.randint(*money_ranges.get(char_class, (20, 80)))
    print(f"Starting Money: {character['money']} gold pieces")


# Determine social class
def social_class() -> None:
    """Determine social class based on character class."""
    lower_classes = ["Thief", "Thief-Acrobat", "Assassin", "Mountebank"]
    middle_classes = ["Bard", "Barbarian", "Jester"]
    upper_classes = ["Fighter", "Paladin", "Cavalier"]
    if character['class'] in lower_classes:
        character['social_class'] = "Lower-Lower Class"
    elif character['class'] in middle_classes:
        character['social_class'] = "Middle-Lower Class"
    else:
        character['social_class'] = "Upper-Lower Class"
    print(f"Social Class: {character['social_class']}")


# Save character data to file
def save_character() -> None:
    """Save character data to file."""
    save_dir = Path(Path.home().joinpath("Adv_Dark_Deep", "Characters"))
    Path.mkdir(save_dir, parents=True, exist_ok=True)
    file_name = input("Enter character name for save file: ")
    with open(save_dir / f"{file_name}.pkl", "wb") as f:
        pickle.dump(character, f)
    print("Character saved!")


# Main character creation flow
if __name__ == "__main__":
    STR, EXP_STR, DEX, IQ, WIS, CON, CHR = roll_attribs()
    print(
        f"Attributes: STR: {STR}, Exceptional STR: {EXP_STR}, DEX: {DEX}, IQ: {IQ}, WIS: {WIS}, CON: {CON}, CHR: {CHR}"
        )
    character['sex'] = get_sex()
    available_races = populate_races(character['sex'], STR, DEX, IQ, WIS, CON, CHR)
    character['race'] = get_race(available_races)
    enable_classes(character['race'])
    con_bonus = con_abilities.get_con_ability(CON, 1)  # Replace with correct method to get Constitution bonus
    starting_hp(con_bonus)
    starting_money()
    social_class()

    # Display character summary
    print("\nCharacter Summary:")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

    # Optionally save character
    if input("Save character? (y/n): ").lower() == 'y':
        save_character()
