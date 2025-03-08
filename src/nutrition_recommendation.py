import json
import os

PROCESSED_DATA_FILE = "data/processed_data.json"
OUTPUT_FILE = "data/nutrition_recommendations.json"

def calculate_caloric_needs(user):
    """Calculates daily caloric needs using the Mifflin-St Jeor Equation."""
    if user["gender"].lower() == "male":
        bmr = 10 * user["weight"] + 6.25 * user["height"] - 5 * user["age"] + 5
    else:
        bmr = 10 * user["weight"] + 6.25 * user["height"] - 5 * user["age"] - 161

    activity_factors = {
        "sedentary": 1.2,
        "moderate": 1.55,
        "active": 1.75
    }
    
    activity_level = user["activity_level"].lower()
    return round(bmr * activity_factors.get(activity_level, 1.2))  # Default to sedentary

def generate_recommendations(user):
    """Generates a basic nutrition plan."""
    calories = calculate_caloric_needs(user)

    # Macronutrient breakdown (standard: 40% carbs, 30% protein, 30% fat)
    protein = round(0.3 * calories / 4)  # 1g protein = 4 kcal
    carbs = round(0.4 * calories / 4)    # 1g carbs = 4 kcal
    fat = round(0.3 * calories / 9)      # 1g fat = 9 kcal

    return {
        "name": user["name"],
        "caloric_needs": calories,
        "macronutrients": {
            "protein": f"{protein}g",
            "carbs": f"{carbs}g",
            "fat": f"{fat}g"
        },
        "recommendation": f"Consume {calories} kcal daily with a balanced diet including {protein}g protein, {carbs}g carbs, and {fat}g fat."
    }

def process_recommendations():
    """Processes all users' nutrition recommendations."""
    if not os.path.exists(PROCESSED_DATA_FILE):
        print("No processed data found. Run data_processing.py first.")
        return

    with open(PROCESSED_DATA_FILE, "r") as file:
        users = json.load(file)

    recommendations = [generate_recommendations(user) for user in users]

    with open(OUTPUT_FILE, "w") as file:
        json.dump(recommendations, file, indent=4)

    print("Nutrition recommendations saved successfully!")

if __name__ == "__main__":
    process_recommendations()
