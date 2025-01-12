import logging
import os
import json
import time
import requests
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
API_KEY = os.getenv("BTN_API_KEY")
BASE_URL = "https://www.behindthename.com/api/lookup.json"

# File paths
GIVEN_NAMES_FILE = "/home/codyjackson/PycharmProjects/RPGs/data/character_names/btn_givennames.txt"
OUTPUT_GIVEN_NAMES = "data/character_names/given_names.json"
ERROR_LOG_FILE = "data/character_names/error_log.json"

# API limits
HOURLY_LIMIT = 400
REQUEST_DELAY = 9  # 1 request every 9 seconds

# Set up logging
logging.basicConfig(
    filename="name_fetcher.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message: str):
    """Log an informational message."""
    print(message)  # Print to console for immediate feedback
    logging.info(message)

def log_error(message: str):
    """Log an error message."""
    print(message)  # Print to console for immediate feedback
    logging.error(message)

def fetch_name_metadata(name: str) -> dict:
    """
    Fetch metadata for a given name using Behind the Name API.

    Args:
        name (str): The name to query.

    Returns:
        dict: Metadata including usage categories or an error log entry.
    """
    response = requests.get(BASE_URL, params={"key": API_KEY, "name": name})
    if response.status_code == 200:
        try:
            data = response.json()
            if isinstance(data, list):  # Valid response
                usages = [usage["usage_code"] for usage in data[0].get("usages", [])]
                return {"name": name, "categories": usages}
            elif isinstance(data, dict) and "error_code" in data:  # Service error
                log_error(f"Service error for {name}: {data['error']}")
                return {"name": name, "categories": [], "error": data["error"]}
        except (ValueError, KeyError):
            pass
    else:
        log_error(f"HTTP error for {name}: {response.status_code}")
    return {"name": name, "categories": [], "error": "Request failed"}


def process_and_group_names(input_file: str, output_file: str, error_file: str, batch_size: int = 400):
    """
    Process given names from a text file, fetch metadata, and group by region.

    Args:
        input_file (str): Path to the input file containing names.
        output_file (str): Path to save grouped names by region.
        error_file (str): Path to save names with errors.
        batch_size (int): Number of names to process in a single run.
    """
    # Load existing data
    grouped_names = {}
    if os.path.exists(output_file):
        with open(output_file, "r") as file:
            existing_data = json.load(file)

        # Convert flat list to grouped dictionary if necessary
        if isinstance(existing_data, list):
            for entry in existing_data:
                for category in entry.get("categories", []):
                    if category not in grouped_names:
                        grouped_names[category] = []
                    grouped_names[category].append(
                        {"name": entry["name"], "gender": entry.get("gender")}
                    )
        elif isinstance(existing_data, dict):
            grouped_names = existing_data

    error_log = []
    if os.path.exists(error_file):
        with open(error_file, "r") as file:
            error_log = json.load(file)

    # Cache processed names
    processed_names_set = {item["name"] for region in grouped_names.values() for item in region}

    # Process names from the input file
    with open(input_file, "r") as file:
        names = file.readlines()

    requests_this_hour = 0

    for i, line in enumerate(names, start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # Skip comments and empty lines

        if "\t" not in line:
            continue  # Skip invalid lines

        name, gender = line.split("\t")

        # Skip already processed names
        if name in processed_names_set:
            continue

        log_info(f"Processing {name} ({i}/{len(names)})...")

        # Enforce hourly limit
        if requests_this_hour >= HOURLY_LIMIT:
            log_info("Hourly limit reached. Pausing for 1 hour...")
            time.sleep(3600)
            requests_this_hour = 0

        # Fetch metadata
        metadata = fetch_name_metadata(name)
        if "error" in metadata:
            error_log.append(metadata)
        else:
            for region in metadata["categories"]:
                if region not in grouped_names:
                    grouped_names[region] = []
                grouped_names[region].append({"name": name, "gender": gender})

        # Save progress
        with open(output_file, "w") as file:
            json.dump(grouped_names, file, indent=4)
        with open(error_file, "w") as file:
            json.dump(error_log, file, indent=4)

        # Update counters and add delay
        requests_this_hour += 1
        time.sleep(REQUEST_DELAY)

    log_info("Processing complete!")

# Example usage
if __name__ == "__main__":
    log_info("Processing given names...")
    process_and_group_names(GIVEN_NAMES_FILE, OUTPUT_GIVEN_NAMES, ERROR_LOG_FILE, batch_size=400)
