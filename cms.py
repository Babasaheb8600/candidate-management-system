import os

# ============================================
# CANDIDATE MANAGEMENT SYSTEM
# Built by: Babasaheb Khedkar
# Date: June 2026
# Skills used: All 9 Python lessons
# ============================================

FILE = "candidates.txt"

# ── FUNCTION 1: Add a candidate ──
def add_candidate():
    print("\n--- Add New Candidate ---")
    name   = input("Enter name: ")
    city   = input("Enter city: ")
    cgpa   = float(input("Enter CGPA: "))
    skill = input("Enter top skill (one skill only, no commas): ")
    degree = input("Has degree? (yes/no): ")

    with open(FILE, "a") as f:
        f.write(f"{name},{city},{cgpa},{skill},{degree}\n")

    print(f"Candidate '{name}' added successfully!")

# ── FUNCTION 2: View all candidates ──
def view_candidates():
    print("\n--- All Candidates ---")
    if not os.path.exists(FILE):
        print("No candidates found.")
        return

    with open(FILE, "r") as f:
        lines = f.readlines()

    if len(lines) == 0:
        print("No candidates found.")
        return

    for i, line in enumerate(lines, 1):
        parts = line.strip().split(",")
        print(f"{i}. Name: {parts[0]} | City: {parts[1]} | "
              f"CGPA: {parts[2]} | Skill: {parts[3]} | "
              f"Degree: {parts[4]}")

# ── FUNCTION 3: Search by name ──
def search_candidate():
    print("\n--- Search Candidate ---")
    search = input("Enter name to search: ").lower()

    if not os.path.exists(FILE):
        print("No candidates found.")
        return

    with open(FILE, "r") as f:
        lines = f.readlines()

    found = False
    for line in lines:
        parts = line.strip().split(",")
        if search in parts[0].lower():
            print(f"Found: Name: {parts[0]} | City: {parts[1]} | "
                  f"CGPA: {parts[2]} | Skill: {parts[3]}")
            found = True

    if not found:
        print(f"No candidate found with name '{search}'.")

# ── FUNCTION 4: Check eligibility ──
def check_eligibility():
    print("\n--- Eligibility Check ---")
    if not os.path.exists(FILE):
        print("No candidates found.")
        return

    with open(FILE, "r") as f:
        lines = f.readlines()

    print(f"{'Name':<15} {'CGPA':<8} {'Degree':<8} {'Status'}")
    print("-" * 50)

    for line in lines:
        parts = line.strip().split(",")
        name   = parts[0]
        cgpa   = float(parts[2])
        degree = parts[4]

        if cgpa >= 6.0 and degree == "yes":
            status = "ELIGIBLE"
        elif cgpa >= 6.0:
            status = "Needs degree"
        else:
            status = "Low CGPA"

        print(f"{name:<15} {cgpa:<8} {degree:<8} {status}")

# ── FUNCTION 5: Show statistics ──
def show_stats():
    print("\n--- Statistics ---")
    if not os.path.exists(FILE):
        print("No candidates found.")
        return

    with open(FILE, "r") as f:
        lines = f.readlines()

    if len(lines) == 0:
        print("No data available.")
        return

    total    = len(lines)
    cgpa_list = []
    eligible  = 0

    for line in lines:
        parts = line.strip().split(",")
        cgpa  = float(parts[2])
        cgpa_list.append(cgpa)
        if cgpa >= 6.0 and parts[4] == "yes":
            eligible += 1

    avg_cgpa = sum(cgpa_list) / total
    highest  = max(cgpa_list)
    lowest   = min(cgpa_list)

    print(f"Total candidates : {total}")
    print(f"Eligible         : {eligible}")
    print(f"Not eligible     : {total - eligible}")
    print(f"Average CGPA     : {avg_cgpa:.2f}")
    print(f"Highest CGPA     : {highest}")
    print(f"Lowest CGPA      : {lowest}")

# ── MAIN MENU ──
def main():
    print("=" * 45)
    print("   CANDIDATE MANAGEMENT SYSTEM")
    print("   Built by Babasaheb Khedkar")
    print("=" * 45)

    while True:
        print("\n--- MENU ---")
        print("1. Add candidate")
        print("2. View all candidates")
        print("3. Search candidate")
        print("4. Check eligibility")
        print("5. Show statistics")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_candidate()
        elif choice == "2":
            view_candidates()
        elif choice == "3":
            search_candidate()
        elif choice == "4":
            check_eligibility()
        elif choice == "5":
            show_stats()
        elif choice == "6":
            print("\nThank you! Goodbye.")
            break
        else:
            print("Invalid choice! Please enter 1 to 6.")

# ── START PROGRAM ──
main()
