"""
Village Grievance Router
--------------------------
Villagers type their complaint in simple Telugu/English keywords.
This program detects which department it belongs to and prints
a formatted complaint letter.
"""

from datetime import date


def detect_department(complaint):
    complaint = complaint.lower()

    water_keywords = ["water", "neellu", "neeru", "manchineeru", "tap", "borewell"]
    road_keywords = ["road", "raasta", "gatti", "patch", "pothole", "street"]
    electricity_keywords = ["current", "electricity", "light", "transformer", "wire", "bill"]

    if any(word in complaint for word in water_keywords):
        return "Water Department"
    elif any(word in complaint for word in road_keywords):
        return "Roads & Infrastructure Department"
    elif any(word in complaint for word in electricity_keywords):
        return "Electricity Department"
    else:
        return "General Grievance Cell"


def generate_letter(name, village, complaint, department):
    today = date.today().strftime("%d-%m-%Y")

    letter = f"""
==================== COMPLAINT LETTER ====================

Date: {today}

To,
The Officer In-Charge,
{department},

Subject: Complaint regarding an issue in {village}

Respected Sir/Madam,

I, {name}, a resident of {village}, would like to bring to your
attention the following issue:

"{complaint}"

I kindly request you to take necessary action at the earliest.

Thank you.

Yours sincerely,
{name}
{village}

============================================================
"""
    return letter


def main():
    print("---- Village Grievance Router ----\n")

    name = input("Enter your name: ")
    village = input("Enter your village name: ")
    complaint = input("Describe your complaint: ")

    department = detect_department(complaint)
    letter = generate_letter(name, village, complaint, department)

    print(f"\nComplaint routed to: {department}\n")
    print(letter)

    # Optional: save the letter to a text file
    filename = f"complaint_{name.replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(letter)
    print(f"Letter saved as {filename}")


if __name__ == "__main__":
    main()