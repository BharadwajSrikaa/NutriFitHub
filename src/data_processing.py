import json
import os

DATA_FILE = "data/user_data.json"

def load_data():
    """Loads user data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def validate_and_process(user):
    """Validates and processes user data."""
    try:
        user["age"] = int(user["age"]) if user["age"] > 0 else None
        user["weight"] = float(user["weight"]) if user["weight"] > 0 else None
        user["height"] = float(user["height"]) if user["height"] > 0 else None

        if None in [user["age"], user["weight"], user["height"]]:
            return None  # Invalid data

        # Normalize activity level to lowercase
        user["activity_level"] = user["activity_level"].strip().lower()

        return user
    except ValueError:
        return None  # Invalid data format

def process_data():
    """Processes all user data."""
    data = load_data()
    processed_data = [validate_and_process(user) for user in data if validate_and_process(user)]

    if processed_data:
        with open("data/processed_data.json", "w") as file:
            json.dump(processed_data, file, indent=4)
        print("Processed data saved successfully!")
    else:
        print("No valid data to process.")

if __name__ == "__main__":
    process_data()
