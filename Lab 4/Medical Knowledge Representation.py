
# Medical Knowledge Representation
# Simple Rule-Based Medical Expert System

def diagnose(symptoms):
    rules = {
        "Common Cold": {"cough", "sneezing", "runny nose"},
        "Flu": {"fever", "cough", "body pain", "headache"},
        "Malaria": {"fever", "chills", "sweating"},
        "Migraine": {"headache", "nausea", "sensitivity to light"},
        "Food Poisoning": {"vomiting", "diarrhea", "stomach pain"}
    }

    matches = []

    for disease, required_symptoms in rules.items():
        matched = symptoms.intersection(required_symptoms)

        if matched:
            score = len(matched)
            matches.append((disease, score, len(required_symptoms)))

    if not matches:
        print("\nNo matching condition found.")
        return

    matches.sort(key=lambda item: item[1], reverse=True)

    print("\nPossible conditions based on symptoms:")

    for disease, score, total in matches:
        print(f"{disease}: {score}/{total} symptoms matched")

    print("\nNote: This is an educational demonstration,")
    print("not a medical diagnosis. Consult a qualified doctor.")


print("===== MEDICAL KNOWLEDGE SYSTEM =====")
print("Enter symptoms separated by commas.")

print("\nAvailable symptoms:")
print("fever, cough, sneezing, runny nose, body pain,")
print("headache, chills, sweating, nausea,")
print("sensitivity to light, vomiting, diarrhea, stomach pain")

user_input = input("\nEnter your symptoms: ")

symptoms = {
    symptom.strip().lower()
    for symptom in user_input.split(",")
    if symptom.strip()
}

diagnose(symptoms)