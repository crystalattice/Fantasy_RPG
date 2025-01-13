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