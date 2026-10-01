
# Frame Representation in Python

frames = {
    "Student": {
        "Name": "Rahul",
        "Age": 21,
        "Course": "MCA",
        "Department": "Computer Science",
        "University": "DAVV"
    },

    "Teacher": {
        "Name": "Dr. Sharma",
        "Age": 45,
        "Subject": "Artificial Intelligence",
        "Department": "Computer Science",
        "University": "DAVV"
    },

    "Course": {
        "Name": "MCA",
        "Duration": "5 Years",
        "Degree": "Postgraduate",
        "Department": "Computer Science"
    }
}


def display_frame(frame_name):
    if frame_name in frames:
        print("\n===== FRAME:", frame_name, "=====")

        for slot, value in frames[frame_name].items():
            print(slot, ":", value)

    else:
        print("Frame not found.")


def display_all_frames():
    for frame_name in frames:
        display_frame(frame_name)


while True:
    print("\n===== FRAME REPRESENTATION MENU =====")
    print("1. Display All Frames")
    print("2. Search a Frame")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_all_frames()

    elif choice == "2":
        name = input("Enter Frame Name: ").strip()
        display_frame(name)

    elif choice == "3":
        print("Exiting Frame Representation.")
        break

    else:
        print("Invalid choice.")