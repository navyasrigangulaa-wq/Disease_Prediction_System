# Disease Prediction System (No libraries needed)

print("=== Disease Prediction System ===")
print("Answer with yes or no\n")

# Take input
fever = input("Do you have fever? ").lower()
cough = input("Do you have cough? ").lower()
headache = input("Do you have headache? ").lower()
fatigue = input("Do you feel fatigue? ").lower()
body_pain = input("Do you have body pain? ").lower()

# Convert to simple values
fever = fever == "yes"
cough = cough == "yes"
headache = headache == "yes"
fatigue = fatigue == "yes"
body_pain = body_pain == "yes"

# Simple logic (rule-based prediction)

if fever and cough and body_pain:
    print("\nPredicted Disease: Flu")

elif cough and not fever:
    print("\nPredicted Disease: Cold")

elif fever and headache and body_pain:
    print("\nPredicted Disease: Typhoid")

elif headache and not fever:
    print("\nPredicted Disease: Migraine")

else:
    print("\nDisease not identified. Please consult a doctor.")

print("\nThank you!")