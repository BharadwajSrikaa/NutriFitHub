import json
import os

DATA_FILE = "data/user_data.json"

def collect_user_data():
    """Collects user data from the command line."""
    user_data = {
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: ")),
        "gender": input("Enter your gender (M/F/Other): "),
        "weight": float(input("Enter your weight (kg): ")),
        "height": float(input("Enter your height (cm): ")),
        "activity_level": input("Enter your activity level (Sedentary/Moderate/Active): "),
        "dietary_preferences": input("Enter dietary preferences (e.g., vegetarian, vegan, keto, etc.): "),
        "health_goals": input("Enter your health goals (e.g., weight loss, muscle gain, maintenance): ")
    }

    save_data(user_data)
    print("\nUser data saved successfully!")

def save_data(data):
    """Saves user data to a JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.append(data)

    with open(DATA_FILE, "w") as file:
        json.dump(existing_data, file, indent=4)

if __name__ == "__main__":
    collect_user_data()