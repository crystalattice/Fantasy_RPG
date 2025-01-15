import json

def create_spell():
    spell_name = input("Enter the spell name: ")
    spell_level = int(input("Enter the spell level (0-9): "))
    spell_school = input("Enter the spell school: ")
    casting_time = input("Enter the casting time: ")
    range_spell = input("Enter the range: ")
    components = input("Enter the components (e.g., V, S, M): ")
    duration = input("Enter the duration: ")
    description = input("Enter the description: ")

    spell = {
        "name": spell_name,
        "level": spell_level,
        "school": spell_school,
        "casting_time": casting_time,
        "range": range_spell,
        "components": components,
        "duration": duration,
        "description": description
    }

    return spell

def add_spell_to_dictionary(spell_dict, spell):
    spell_dict[spell["name"]] = spell

def main():
    spell_dict = {}

    while True:
        print("\nCreate a new spell:")
        spell = create_spell()
        add_spell_to_dictionary(spell_dict, spell)

        cont = input("\nDo you want to add another spell? (y/n): ").lower()
        if cont != 'y':
            break

    print("\nFinal spell dictionary:")
    print(json.dumps(spell_dict, indent=4))

    save = input("\nDo you want to save the spell dictionary to a file? (y/n): ").lower()
    if save == 'y':
        file_name = input("Enter the file name (without extension): ")
        with open(f"{file_name}.json", "w") as f:
            json.dump(spell_dict, f, indent=4)
        print(f"\nSpell dictionary saved to {file_name}.json")

if __name__ == "__main__":
    main()
