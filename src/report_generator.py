import json
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

INPUT_FILE = "data/nutrition_recommendations.json"
CSV_FILE = "data/nutrition_report.csv"
PDF_FILE = "data/nutrition_report.pdf"

def load_recommendations():
    """Loads nutrition recommendations from JSON."""
    with open(INPUT_FILE, "r") as file:
        return json.load(file)

def generate_csv(recommendations):
    """Generates a CSV report."""
    df = pd.DataFrame(recommendations)
    df.to_csv(CSV_FILE, index=False)
    print(f"CSV report saved: {CSV_FILE}")

def generate_pdf(recommendations):
    """Generates a PDF report."""
    c = canvas.Canvas(PDF_FILE, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)

    y = height - 50
    c.drawString(200, y, "Nutrition Recommendations Report")
    y -= 30

    for user in recommendations:
        c.drawString(50, y, f"Name: {user['name']}")
        c.drawString(250, y, f"Calories: {user['caloric_needs']} kcal")
        y -= 20
        c.drawString(50, y, f"Protein: {user['macronutrients']['protein']}, Carbs: {user['macronutrients']['carbs']}, Fat: {user['macronutrients']['fat']}")
        y -= 30
        if y < 100:
            c.showPage()
            y = height - 50
    
    c.save()
    print(f"PDF report saved: {PDF_FILE}")

def generate_reports():
    """Main function to generate reports."""
    recommendations = load_recommendations()
    generate_csv(recommendations)
    generate_pdf(recommendations)

if __name__ == "__main__":
    generate_reports()