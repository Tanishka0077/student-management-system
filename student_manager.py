import json
import os

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

# Add a new student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    students = load_students()
    students.append({"name": name, "roll": roll, "marks": marks})
    save_students(students)
    print(f"✓ Student '{name}' added successfully!")

# View all students
def view_students():
    students = load_students()
    if not students:
        print("No students found!")
        return
    print("\n---------- All Students ----------")
    for i, s in enumerate(students, 1):
        print(f"{i}. Name: {s['name']} | Roll: {s['roll']} | Marks: {s['marks']}")
    print("----------------------------------")

# Search student by name
def search_student():
    name = input("Enter name to search: ").lower()
    students = load_students()
    found = [s for s in students if name in s['name'].lower()]
    if found:
        print("\n---------- Search Results ----------")
        for s in found:
            print(f"Name: {s['name']} | Roll: {s['roll']} | Marks: {s['marks']}")
        print("------------------------------------")
    else:
        print("No student found with that name.")

# Delete student by roll number
def delete_student():
    roll = input("Enter roll number to delete: ")
    students = load_students()
    new_list = [s for s in students if s['roll'] != roll]
    if len(new_list) == len(students):
        print("No student found with that roll number.")
    else:
        save_students(new_list)
        print(f"✓ Student with roll {roll} deleted successfully!")

# Main menu
def menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("0. Exit")

    choice = input("\nEnter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "0":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice, try again.")

# Run the app
while True:
    menu()