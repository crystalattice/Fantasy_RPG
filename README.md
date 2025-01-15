# RPG Application

## Overview
This is a modular RPG application focused on managing tabletop games like *Adventures Dark and Deep* (ADD). The application supports:
- Character creation and management.
- Equipment handling.
- Travel and adventure logging.
- Rules and combat mechanics.

### Directory Structure
- `data/`: Static data files (e.g., equipment, spells) split by game system.
- `src/`: Source code for core functionality, organized by modules.
- `tests/`: Unit and integration tests.
- `docs/`: Developer notes, user help, and other documentation.
- `Archived/`: Older or unused files for reference.

### Current Features
- **Equipment Module**:
  - Load equipment data from JSON files.
  - Query items by type, name, or attributes.
  - Add new items dynamically.
  - Calculate inventory encumbrance.

### Planned Features
- Character manager for ADD.
- Travel log integration.
- Support for additional game systems (e.g., Twilight 2000).

# Name and Metadata Processor

## Overview
This project processes names (given names and surnames) to extract metadata using the Behind the Name API. The processed data is saved in JSON format, grouped by region, and used for generating characters or NPCs in RPG systems.

## Current Features
- **Given Name Processing**:
  - Extracts metadata (e.g., region and gender) for given names using the API.
  - Saves processed names into `given_names.json`, grouped by region.
- **Surname Conversion**:
  - Converts the `btn_surnames.txt` file directly into a JSON format.
- **Error Logging**:
  - Names that encounter API errors are saved to `error_log.json` for future retries.
- **Rate Limiting**:
  - Adheres to API limits with a delay of 9 seconds per request and hourly pauses after 400 requests.

## Directory Structure
```
data/
├── character_names/
│   ├── given_names.json
│   ├── surnames.json
│   ├── error_log.json
```

## How to Use
1. **Run the Name Processor**:
   ```bash
   python name_fetcher.py
   ```
2. **Monitor Logs**:
   - Logs are saved to `name_fetcher.log`. Use `tail` to monitor progress:
     ```bash
     tail -f name_fetcher.log
     ```
3. **Generated Files**:
   - `given_names.json`: Grouped names by region.
   - `surnames.json`: Surnames in JSON format.
   - `error_log.json`: Failed names for retries.

## Attribute Abilities

The application now supports dynamically loading abilities for core attributes (e.g., strength, charisma) from JSON files. Each attribute includes defined ranges and their corresponding abilities, making it easy to retrieve values programmatically.

### Supported Attributes
- Strength
- Charisma
- Constitution
- Dexterity
- Intelligence
- Wisdom

### How It Works
1. **Data Structure**:
   - Each attribute maps ranges of values to abilities (e.g., Strength 18/01-50).
   - Data is stored in JSON files for easy access and editing.

2. **Dynamic Retrieval**:
   - Use the attribute-specific retrieval functions to access abilities by value:
     ```python
     from strength_abilities import get_strength_ability, StrengthModifier

     strength_value = "18/91-99"
     modifier = StrengthModifier.DAMAGE
     value = get_strength_ability(strength_value, modifier)
     print(value)
     ```

3. **JSON Storage**:
   - Each attribute’s abilities are stored in a corresponding JSON file:
     ```
     data/
     ├── charisma_abilities.json
     ├── constitution_abilities.json
     ├── dex_abilities.json
     ├── iq_abilities.json
     ├── strength_abilities.json
     └── wisdom_abilities.json
     ```

4. **Customization**:
   - You can update JSON files directly to modify or extend abilities without changing the code.

### Example JSON Entry
```json
{
    "range": [1, 2, 3, 4, 5, 6, 7, 8],
    "Magical_Attack_Adjustment": -1,
    "Cleric_Bonus": "0",
    "Spell_Failure": 100,
    "Immune_to_Charm": 0
}
```
## Race Attribute Limits

The application now supports dynamically managing racial attribute limits for both male and female characters. These limits include minimum and maximum values for core attributes (e.g., Strength, Intelligence) and are stored in a JSON format for flexibility and ease of modification.

### How It Works
1. **Data Structure**:
   - Attribute limits are grouped by gender and race.
   - Each attribute (e.g., Strength, Intelligence) is represented by its minimum and maximum permissible values.

2. **Dynamic Retrieval**:
   - Use the provided functions or load the JSON file directly to retrieve limits for a specific race and gender.

3. **JSON Storage**:
   - All racial limits are stored in `race_attribute_limits.json`:
     ```
     data/
     └── race_attribute_limits.json
     ```

### Example JSON Entry
```json
{
    "male": {
        "dwarf": {
            "STR": [8, 18],
            "IQ": [3, 18],
            "WIS": [3, 18],
            "DEX": [3, 17],
            "CON": [12, 19],
            "CHR": [3, 16]
        }
    }
}
```

### Usage Example
Retrieve racial limits dynamically in Python:
```python
import json

# Load the JSON file
with open("data/race_attribute_limits.json", "r") as file:
    race_limits = json.load(file)

# Example: Get attribute limits for male dwarves
male_dwarf_limits = race_limits["male"]["dwarf"]
print(male_dwarf_limits["STR"])  # Output: [8, 18]
```
## Spells by Level

The application now supports spell data for the following classes, categorized by levels:

- Bard Spells
- Jester Spells
- Cleric Spells
- Druid Spells
- Mage Spells
- Illusionist Spells
- Savant Spells
- Mountebank Spells

### Spell Data Structure
Each spell data file is stored in JSON format, where spells are grouped by their respective levels. For example:
```json
{
    "first_level": ["Spell A", "Spell B"],
    "second_level": ["Spell C", "Spell D"]
}
```

### JSON File Locations
All spell JSON files are located in the `data/spells/` directory:
- `bard_spells_by_level.json`
- `jester_spells_by_level.json`
- `cleric_spells_by_level.json`
- `druid_spells_by_level.json`
- `mage_spells_by_level.json`
- `illusionist_spells_by_level.json`
- `savant_spells_by_level.json`
- `mountebank_spells_by_level.json`


## Equipment and Gear

The application includes comprehensive data for various types of equipment and gear. Each category is stored in a separate JSON file for modularity and easy access.

### Categories
1. Animals (`animals.json`)
2. Armor (`armor.json`)
3. Clothing (`clothing.json`)
4. Food and Drink (`food_and_drink.json`)
5. Furs (`furs.json`)
6. Hirelings (`hirelings.json`)
7. Luxury Items (`luxury_items.json`)
8. Miscellaneous Items (`miscellaneous_items.json`)
9. Musical Instruments (`musical_instruments.json`)
10. Poisons (`poisons.json`)
11. Services (`services.json`)
12. Transportation (`transportation.json`)
13. Melee Weapons (`melee_weapons.json`)

### JSON File Locations
All files are stored in the `data/equipment/` directory.

### Example File Structure
Each file organizes items in a list of dictionaries. For example, `armor.json`:
```json
{
    "armor": [
        {
            "type": "Plate Armor",
            "price": "400 g.p.",
            "weight": 45,
            "armor_value": 7,
            "base_ac": 3,
            "movement": "50%"
        }
    ]
}
```