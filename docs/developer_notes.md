# Developer Notes

## Milestones and Decisions

### **Project Initialization**
- **Directory Structure**:
  - The project was restructured for modularity and scalability.
  - `data/` holds static data files, split by game system and purpose.
  - `src/` contains source code, organized by functional areas (e.g., `char_creation`, `equipment_management`).
  - `tests/` contains unit and integration tests for each module.
  - `docs/` contains developer notes, user help, and other documentation.
  - `Archived/` stores older or unused files for reference.

- **Rationale**:
  - The modular structure makes it easier to expand the project (e.g., supporting multiple game systems like Twilight 2000).
  - Placing JSON data in `data/` centralizes content for easier management and updates.

### **Equipment Module**
- **Features**:
  - Dynamically loads equipment data from JSON files.
  - Supports querying items by category (e.g., weapons, armor).
  - Includes functions to add new items and calculate inventory encumbrance.
- **Rationale**:
  - Equipment data is stored in separate JSON files for modularity (`armor.json`, `melee_weapons.json`, etc.).
  - This simplifies editing and allows for easy expansion as new equipment types are added.
  
### **JSON vs YAML Decision**
- **Decision**: Use JSON for all data files.
- **Reasoning**:
  - JSON is lightweight, supported natively by Python, and sufficient for storing structured data.
  - YAML's additional features (e.g., comments) weren’t necessary for this project since the files are largely static.

### **Future-Proofing for Multiple Game Systems**
- **Decision**:
  - Prepare the project for supporting additional game systems (e.g., Twilight 2000) by organizing `data/` and `src/` per system.
  - Use placeholders for future content (`data/twilight2000/`).

### **Spells and Data Splitting**
- **Decision**:
  - Store spells, equipment, and similar data in separate JSON files for each category (e.g., `cleric_spells.json`, `mage_spells.json`).
- **Rationale**:
  - Smaller files improve readability and make edits easier.
  - Each file focuses on a single category, simplifying updates and testing.

## Script Overview
### `name_fetcher.py`
- Processes given names alphabetically from `btn_givennames.txt`.
- Queries metadata from the Behind the Name API.
- Groups names by region in `given_names.json`.

### Surname Conversion
- Converts `btn_surnames.txt` directly to JSON format.

## Logic Highlights
1. **Processing Logic**:
   - Skips already-processed names.
   - Logs progress and saves incrementally.

2. **Error Handling**:
   - Logs API errors to `error_log.json` for later retries.

3. **Rate Limiting**:
   - Enforces a 9-second delay per request to adhere to API limits.
   - Pauses for 1 hour after 400 requests.

## Enhancements
- Incremental saving to prevent data loss.
- Conversion of `btn_surnames.txt` to `surnames.json`.

## Attribute Abilities Refactor

### Overview
The core attributes (strength, charisma, constitution, dexterity, intelligence, wisdom) have been refactored to:
1. Use `dataclass` structures for better readability and extensibility.
2. Avoid duplication by grouping shared values using ranges.
3. Enable JSON serialization for dynamic integration.

### Key Features
- **Range-Based Logic**:
  - Attributes like wisdom and dexterity group shared values into ranges, e.g., `"Wisdom 1-8"`.
- **Exceptional Values**:
  - Handles specific cases like `"Strength 18/91-99"`.
- **JSON Integration**:
  - Stores all abilities in structured JSON files for ease of use.

### Functions
#### Retrieval Functions
Each attribute has a dedicated retrieval function. Example for Strength:
```python
def get_strength_ability(str_val: Union[int, str], ability: StrengthModifier) -> Union[int, float]:
    """
    Retrieve the specific ability modifier for a given strength score.
    """
    ...
```

#### Serialization
Each attribute includes a serialization function to convert abilities to JSON. Example:
```python
def serialize_strength_abilities_to_json(output_file: str):
    """
    Serialize strength abilities to JSON format.
    """
    ...
```

### JSON File Paths
- All JSON files are stored in the `data/` directory:
  ```
  data/
  ├── charisma_abilities.json
  ├── constitution_abilities.json
  ...
  ```
## Race Attribute Limits

### Overview
Racial attribute limits are now stored in `race_attribute_limits.json`. This file defines minimum and maximum values for each core attribute (e.g., Strength, Intelligence) for every supported race and gender.

### Key Features
1. **Dynamic JSON Conversion**:
   - The `race_attribute_limits.json` file is generated dynamically from `namedtuple` data.
   - Avoids redundancy by iterating over a dictionary of races and genders.

2. **Scalable**:
   - Adding a new race or updating existing limits is as simple as modifying the source dictionary.

### JSON File Path
The racial attribute limits JSON file is stored in the `data/` directory:
```
data/
└── race_attribute_limits.json
```

### Script Overview
- The Python script dynamically converts `namedtuple` data to JSON.
- Key attributes include:
  - **STR**: Strength
  - **IQ**: Intelligence
  - **WIS**: Wisdom
  - **DEX**: Dexterity
  - **CON**: Constitution
  - **CHR**: Charisma

### Adding a New Race
To add a new race:
1. Define the limits using `Ability_Limits`:
   ```python
   new_race_limits = Ability_Limits(3, 18, 8, 18, 3, 18, 7, 19, 6, 18, 8, 18)
   ```
2. Add it to the `racial_limits` dictionary under the appropriate gender:
   ```python
   racial_limits["male"]["new_race"] = new_race_limits
   racial_limits["female"]["new_race"] = new_race_limits
   ```
3. Run the script to regenerate `race_attribute_limits.json`.

## Spell JSON Files

### Overview
Spell data for various classes has been implemented as JSON files. Each file organizes spells by level for efficient retrieval and integration with the application.

### File Structure
Each JSON file follows this structure:
```json
{
    "class_spells_by_level": {
        "first_level": ["Spell A", "Spell B"],
        "second_level": ["Spell C", "Spell D"]
    }
}
```

### Current Files
1. `bard_spells_by_level.json`
2. `jester_spells_by_level.json`
3. `cleric_spells_by_level.json`
4. `druid_spells_by_level.json`
5. `mage_spells_by_level.json`
6. `illusionist_spells_by_level.json`
7. `savant_spells_by_level.json`
8. `mountebank_spells_by_level.json`

### Integration Notes
- **File Location**: All spell files are stored in the `data/spells/` directory.
- **Access Pattern**: Use Python’s `json` module to load the data and access spells by level.

### Example Usage
To retrieve all third-level mage spells:
```python
import json

with open("data/spells/mage_spells_by_level.json", "r") as file:
    mage_spells = json.load(file)

third_level_spells = mage_spells["third_level"]
print(third_level_spells)
```
## Equipment and Gear JSON Files

### Overview
Equipment and gear are categorized into distinct JSON files to enable modular access and flexibility in usage.

### Categories and File Names
1. Animals: `animals.json`
2. Armor: `armor.json`
3. Clothing: `clothing.json`
4. Food and Drink: `food_and_drink.json`
5. Furs: `furs.json`
6. Hirelings: `hirelings.json`
7. Luxury Items: `luxury_items.json`
8. Miscellaneous Items: `miscellaneous_items.json`
9. Musical Instruments: `musical_instruments.json`
10. Poisons: `poisons.json`
11. Services: `services.json`
12. Transportation: `transportation.json`
13. Melee Weapons: `melee_weapons.json`

### File Structure
Each JSON file stores data as a list of dictionaries with fields relevant to the item type. For example:
- **Armor** includes fields like `type`, `price`, `weight`, `armor_value`, `base_ac`, and `movement`.
- **Food and Drink** includes fields like `type`, `price`, and `weight`.

### Access Example
To retrieve all available hirelings:
```python
import json

with open("data/equipment/hirelings.json", "r") as file:
    hirelings = json.load(file)

print(hirelings["hirelings"])
```