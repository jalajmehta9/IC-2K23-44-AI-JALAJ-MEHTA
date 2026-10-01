
# University Knowledge Base

university = {
    "students": {
        "101": {"name": "Rahul", "course": "MCA", "department": "Computer Science"},
        "102": {"name": "Priya", "course": "BCA", "department": "Computer Science"},
        "103": {"name": "Amit", "course": "MBA", "department": "Management"}
    },

    "teachers": {
        "T01": {"name": "Dr. Sharma", "subject": "Artificial Intelligence"},
        "T02": {"name": "Dr. Verma", "subject": "Database Management"}
    },

    "courses": {
        "MCA": "Master of Computer Applications",
        "BCA": "Bachelor of Computer Applications",
        "MBA": "Master of Business Administration"
    }
}


def search_student(student_id):
    student = university["students"].get(student_id)

    if student:
        print("\nStudent Found!")
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Department:", student["department"])
    else:
        print("Student not found.")


def display_teachers():
    print("\nTeacher Information:")
    for teacher_id, details in university["teachers"].items():
        print(teacher_id, "-", details["name"],
              "| Subject:", details["subject"])


def display_courses():
    print("\nAvailable Courses:")
    for code, name in university["courses"].items():
        print(code, "-", name)


while True:
    print("\n===== UNIVERSITY KNOWLEDGE BASE =====")
    print("1. Search Student")
    print("2. Display Teachers")
    print("3. Display Courses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        search_student(student_id)

    elif choice == "2":
        display_teachers()

    elif choice == "3":
        display_courses()

    elif choice == "4":
        print("Exiting University Knowledge Base.")
        break

    else:
        print("Invalid choice. Try again.")