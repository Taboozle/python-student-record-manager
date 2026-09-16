import json

DATA_FILE = "students.json"


def load_students():
    """Load student records from the JSON file."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: The student data file is invalid.")
        return []


def save_students(students):
    """Save student records to the JSON file."""
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(students, file, indent=4)

    except OSError:
        print("Error: Student records could not be saved.")


def add_student(students):
    """Add a new student record."""
    print("\n--- Add Student ---")

    student_number = input("Student number: ").strip()

    if not student_number:
        print("Student number cannot be empty.")
        return

    for student in students:
        if student["student_number"].lower() == student_number.lower():
            print("A student with that number already exists.")
            return

    name = input("Student name: ").strip()
    course = input("Course: ").strip()
    year = input("Year of study: ").strip()

    if not name or not course or not year:
        print("All fields are required.")
        return

    student = {
        "student_number": student_number,
        "name": name,
        "course": course,
        "year": year
    }

    students.append(student)
    save_students(students)

    print("Student added successfully.")


def view_students(students):
    """Display all student records."""
    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for number, student in enumerate(students, start=1):
        print(f"\nStudent {number}")
        print(f"Student Number: {student['student_number']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Year: {student['year']}")


def search_student(students):
    """Search for a student using their student number."""
    print("\n--- Search Student ---")

    student_number = input("Enter student number: ").strip()

    for student in students:
        if student["student_number"].lower() == student_number.lower():
            print("\nStudent found:")
            print(f"Student Number: {student['student_number']}")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Year: {student['year']}")
            return

    print("Student not found.")


def update_student(students):
    """Update an existing student record."""
    print("\n--- Update Student ---")

    student_number = input("Enter student number: ").strip()

    for student in students:
        if student["student_number"].lower() == student_number.lower():

            print("Press Enter to keep the current value.")

            new_name = input(
                f"Name [{student['name']}]: "
            ).strip()

            new_course = input(
                f"Course [{student['course']}]: "
            ).strip()

            new_year = input(
                f"Year [{student['year']}]: "
            ).strip()

            if new_name:
                student["name"] = new_name

            if new_course:
                student["course"] = new_course

            if new_year:
                student["year"] = new_year

            save_students(students)

            print("Student record updated successfully.")
            return

    print("Student not found.")


def delete_student(students):
    """Delete a student record."""
    print("\n--- Delete Student ---")

    student_number = input("Enter student number: ").strip()

    for student in students:
        if student["student_number"].lower() == student_number.lower():

            confirmation = input(
                f"Delete {student['name']}? (y/n): "
            ).strip().lower()

            if confirmation == "y":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")


def display_menu():
    """Display the application's main menu."""
    print("\n==============================")
    print("   Student Record Manager")
    print("==============================")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")


def main():
    students = load_students()

    while True:
        display_menu()

        choice = input("\nSelect an option (1-6): ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()