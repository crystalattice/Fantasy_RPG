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