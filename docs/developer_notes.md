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
  
