"""
Aptura Tech Solution
Batch 3 Internship - Week 1
Task 1: Student Record System

A simple console-based student management system.
"""

import json
from pathlib import Path


DATA_FILE = Path("students.json")


# -----------------------------
# File Handling
# -----------------------------

def load_students():
    """Load student records from the JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Unable to load student records.")
        return []


def save_students(students):
    """Save student records to the JSON file."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


# -----------------------------
# Helper Functions
# -----------------------------

def find_student(students, student_id):
    """Find a student using their ID."""

    for student in students:
        if student["id"].lower() == student_id.lower():
            return student

    return None


def get_non_empty_input(message):
    """Get input that cannot be empty."""

    while True:
        value = input(message).strip()

        if value:
            return value

        print("Please enter a valid value.")


def get_marks():
    """Get valid marks between 0 and 100."""

    while True:
        try:
            marks = float(input("Marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def calculate_grade(marks):
    """Calculate grade according to marks."""

    if marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# -----------------------------
# Student Operations
# -----------------------------

def add_student(students):
    print("\n" + "-" * 45)
    print("ADD NEW STUDENT")
    print("-" * 45)

    student_id = get_non_empty_input("Student ID: ")

    if find_student(students, student_id):
        print("A student with this ID already exists.")
        return

    name = get_non_empty_input("Name: ")
    age = get_non_empty_input("Age: ")
    program = get_non_empty_input("Program: ")
    marks = get_marks()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "program": program,
        "marks": marks,
        "grade": calculate_grade(marks)
    }

    students.append(student)
    save_students(students)

    print(f"\n✓ {name} has been added successfully.")


def display_students(students):
    print("\n" + "=" * 70)
    print("STUDENT RECORDS")
    print("=" * 70)

    if not students:
        print("No student records found.")
        return

    print(
        f"{'ID':<10}"
        f"{'Name':<20}"
        f"{'Program':<18}"
        f"{'Marks':<10}"
        f"{'Grade':<6}"
    )

    print("-" * 70)

    for student in students:
        print(
            f"{student['id']:<10}"
            f"{student['name']:<20}"
            f"{student['program']:<18}"
            f"{student['marks']:<10.1f}"
            f"{student['grade']:<6}"
        )


def search_student(students):
    print("\n" + "-" * 45)
    print("SEARCH STUDENT")
    print("-" * 45)

    keyword = get_non_empty_input(
        "Enter student ID or name: "
    ).lower()

    results = []

    for student in students:
        if (
            keyword in student["id"].lower()
            or keyword in student["name"].lower()
        ):
            results.append(student)

    if results:
        display_students(results)
    else:
        print("No matching student found.")


def update_student(students):
    print("\n" + "-" * 45)
    print("UPDATE STUDENT")
    print("-" * 45)

    student_id = get_non_empty_input("Enter student ID: ")

    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print(f"\nUpdating record for: {student['name']}")

    new_name = input(
        f"Name [{student['name']}]: "
    ).strip()

    new_program = input(
        f"Program [{student['program']}]: "
    ).strip()

    if new_name:
        student["name"] = new_name

    if new_program:
        student["program"] = new_program

    update_marks = input(
        "Do you want to update marks? (y/n): "
    ).lower()

    if update_marks == "y":
        student["marks"] = get_marks()
        student["grade"] = calculate_grade(student["marks"])

    save_students(students)

    print("✓ Student record updated successfully.")


def delete_student(students):
    print("\n" + "-" * 45)
    print("DELETE STUDENT")
    print("-" * 45)

    student_id = get_non_empty_input("Enter student ID: ")

    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    confirmation = input(
        f"Are you sure you want to delete {student['name']}? (y/n): "
    ).lower()

    if confirmation == "y":
        students.remove(student)
        save_students(students)

        print("✓ Student deleted successfully.")

    else:
        print("Delete operation cancelled.")


def show_statistics(students):
    print("\n" + "=" * 45)
    print("CLASS STATISTICS")
    print("=" * 45)

    if not students:
        print("No records available.")
        return

    total_students = len(students)

    average_marks = sum(
        student["marks"] for student in students
    ) / total_students

    highest_scorer = max(
        students,
        key=lambda student: student["marks"]
    )

    passed_students = sum(
        student["marks"] >= 50
        for student in students
    )

    pass_rate = (
        passed_students / total_students
    ) * 100

    print(f"Total Students : {total_students}")
    print(f"Average Marks  : {average_marks:.2f}")
    print(
        f"Highest Scorer : "
        f"{highest_scorer['name']} "
        f"({highest_scorer['marks']:.1f})"
    )
    print(f"Pass Rate      : {pass_rate:.1f}%")


# -----------------------------
# Main Menu
# -----------------------------

def show_menu():
    print("\n")
    print("=" * 50)
    print("       STUDENT RECORD SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Statistics")
    print("0. Exit")

    print("-" * 50)


def main():

    students = load_students()

    while True:

        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            show_statistics(students)

        elif choice == "0":
            print("\nThank you for using Student Record System!")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()