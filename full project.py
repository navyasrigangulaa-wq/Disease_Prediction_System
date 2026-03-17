# =========================================
# DISEASE PREDICTION SYSTEM (FULL PROJECT)
# No external libraries required
# =========================================

FILE_NAME = "history.txt"

# ------------------------------
# Function: Input Validation
# ------------------------------
def get_input(question):
    while True:
        ans = input(question + " (yes/no): ").lower()
        if ans in ["yes", "no"]:
            return ans == "yes"
        else:
            print("Invalid input! Please enter yes or no.")

# ------------------------------
# Function: Predict Disease
# ------------------------------
def predict_disease(symptoms):
    fever, cough, headache, fatigue, body_pain, nausea = symptoms

    if fever and cough and body_pain:
        return "Flu", 90
    elif cough and not fever:
        return "Cold", 80
    elif fever and headache and body_pain:
        return "Typhoid", 85
    elif headache and not fever:
        return "Migraine", 75
    elif fever and nausea and fatigue:
        return "Dengue", 88
    elif fatigue and body_pain and not fever:
        return "Stress", 70
    else:
        return "Unknown", 50

# ------------------------------
# Function: Precautions
# ------------------------------
def show_precautions(disease):
    print("\nPrecautions:")

    precautions_dict = {
        "Flu": [
            "Take rest",
            "Drink plenty of fluids",
            "Take proper medication"
        ],
        "Cold": [
            "Stay warm",
            "Drink hot fluids",
            "Steam inhalation"
        ],
        "Typhoid": [
            "Consult doctor",
            "Drink clean water",
            "Avoid outside food"
        ],
        "Migraine": [
            "Rest in dark room",
            "Avoid noise",
            "Stay hydrated"
        ],
        "Dengue": [
            "Consult doctor immediately",
            "Drink fluids",
            "Avoid mosquito exposure"
        ],
        "Stress": [
            "Exercise regularly",
            "Take rest",
            "Practice relaxation"
        ],
        "Unknown": [
            "Consult doctor for proper diagnosis"
        ]
    }

    for item in precautions_dict.get(disease, []):
        print("-", item)

# ------------------------------
# Function: Save History
# ------------------------------
def save_history(name, disease, confidence):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name} - {disease} ({confidence}%)\n")

# ------------------------------
# Function: View History
# ------------------------------
def view_history():
    print("\n===== HISTORY =====")
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("No history found.")

# ------------------------------
# Function: Clear History
# ------------------------------
def clear_history():
    open(FILE_NAME, "w").close()
    print("History cleared successfully!")

# ------------------------------
# Function: Disease Check
# ------------------------------
def check_disease(name):
    print("\nAnswer the following questions:")

    fever = get_input("Do you have fever?")
    cough = get_input("Do you have cough?")
    headache = get_input("Do you have headache?")
    fatigue = get_input("Do you feel fatigue?")
    body_pain = get_input("Do you have body pain?")
    nausea = get_input("Do you have nausea?")

    symptoms = (fever, cough, headache, fatigue, body_pain, nausea)

    disease, confidence = predict_disease(symptoms)

    print("\nPredicted Disease:", disease)
    print("Confidence Level:", str(confidence) + "%")

    show_precautions(disease)

    save_history(name, disease, confidence)

# ------------------------------
# Function: About Project
# ------------------------------
def about():
    print("\n=== About Project ===")
    print("This is a simple Disease Prediction System.")
    print("It predicts disease based on symptoms using rule-based logic.")
    print("Developed using Python without external libraries.")

# ------------------------------
# Main Program
# ------------------------------
def main():
    print("===================================")
    print("   DISEASE PREDICTION SYSTEM")
    print("===================================")

    name = input("Enter your name: ")

    while True:
        print("\n========= MENU =========")
        print("1. Predict Disease")
        print("2. View History")
        print("3. Clear History")
        print("4. About Project")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_disease(name)

        elif choice == "2":
            view_history()

        elif choice == "3":
            clear_history()

        elif choice == "4":
            about()

        elif choice == "5":
            print("\nThank you for using the system!")
            break

        else:
            print("Invalid choice! Try again.")

# ------------------------------
# Run Program
# ------------------------------
main()