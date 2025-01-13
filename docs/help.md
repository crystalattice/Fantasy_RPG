# RPG Application Help

## Equipment Module
### How to Load Items
- Equipment data is stored in JSON files under `data/adventures_dark_deep/equipment/`.
- Categories include:
  - `armor.json`: Armor and shields.
  - `melee_weapons.json`: Swords, axes, and other close-combat weapons.
  - `ranged_weapons.json`: Bows, crossbows, and similar.
  - `gear.json`: General adventuring gear.

### How to Query Items
- Use the `list_items(category)` function to retrieve all items in a category.
- Example:
  ```python
  from src.equipment_management.equipment_module import list_items
  weapons = list_items("melee_weapons")
  print(weapons)
  
### How to Calculate Encumbrance
- Use the calculate_encumbrance(inventory) function to compute total weight.
- Example:
```python 
inventory = [{"name": "Longsword", "weight": 4}, {"name": "Chainmail", "weight": 40}]
total_weight = calculate_encumbrance(inventory)
print("Encumbrance:", total_weight)
```
### Adding New Items
- To add a new item, update the relevant JSON file in data/adventures_dark_deep/equipment/:
``` python 
{
  "name": "Warhammer",
  "type": "melee",
  "cost": 20,
  "weight": 6,
  "damage": "1d8",
  "speed": 7
}
```

Alternatively, use the ```add_item()``` function in the equipment module.

## How to Run
### Given Names Processing
1. Place the `btn_givennames.txt` file in the `data/character_names/` directory.
2. Run the script:
   ```bash
   python name_fetcher.py
   ```

### Surname Conversion
1. Place the `btn_surnames.txt` file in the `data/character_names/` directory.
2. Run the conversion function:
   ```bash
   python -c "from name_fetcher import convert_surnames_to_json; convert_surnames_to_json('data/character_names/btn_surnames.txt', 'data/character_names/surnames.json')"
   ```

## File Descriptions
- `given_names.json`: Grouped by region with gender and metadata.
- `surnames.json`: List of surnames.
- `error_log.json`: Names that failed during metadata processing.

## Troubleshooting
1. **Script Stops Unexpectedly**:
   - Check `name_fetcher.log` for errors.
   - Restart the script to resume from the last processed name.

2. **Hourly Limit Reached**:
   - The script will pause for 1 hour and resume automatically.

## Attribute Abilities

### Supported Attributes
- Strength
- Charisma
- Constitution
- Dexterity
- Intelligence
- Wisdom

### Using Abilities
Each attribute provides functions for retrieving abilities based on value. Example for Charisma:
```python
from charisma_abilities import get_charisma_ability

charisma_value = 16
ability = "morale_adj"
value = get_charisma_ability(charisma_value, ability)
print(f"Charisma {charisma_value} - {ability}: {value}")
```

### Customizing Abilities
Modify abilities by editing the corresponding JSON file in `data/`. Example (`charisma_abilities.json`):
```json
{
    "range": [16],
    "max_henchmen": 8,
    "morale_adj": 4,
    "react_adj": 25
}
```
## Race Attribute Limits

### Overview
Racial attribute limits define the permissible ranges for core attributes (e.g., Strength, Intelligence) for each race and gender.

### Using Attribute Limits
To access attribute limits:
1. Open `race_attribute_limits.json`.
2. Retrieve the limits for a specific race and gender.

Example:
```python
import json

with open("data/race_attribute_limits.json", "r") as file:
    race_limits = json.load(file)

# Example: Get attribute limits for female high elves
female_high_elf_limits = race_limits["female"]["high_elf"]
print(female_high_elf_limits["DEX"])  # Output: [7, 19]
```

### Adding or Updating Races
1. Edit the source dictionary in the Python script.
2. Regenerate `race_attribute_limits.json` by running the script.

### File Location
The attribute limits are stored in:
```
data/
└── race_attribute_limits.json
```