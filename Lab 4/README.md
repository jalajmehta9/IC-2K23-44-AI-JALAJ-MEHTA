# Knowledge Representation Programs in Python

This repository contains four Python programs demonstrating foundational Artificial Intelligence (AI) knowledge representation techniques. The examples cover frame representation, a rule-based medical knowledge system, semantic network construction, and a university knowledge base.

## Project Contents

| File | Topic | Main Functionality |
|---|---|---|
| `Frame Representation(2).py` | Frame Representation | Stores information in frames and allows users to display all frames or search for a particular frame. |
| `Medical Knowledge Representation(1).py` | Rule-Based Medical Knowledge Representation | Matches user-entered symptoms against predefined conditions and displays possible matches. |
| `Semantic Network Construction(2).py` | Semantic Network | Represents entities and their relationships and allows users to display the network or search relationships for a node. |
| `University Knowledge Base(2).py` | University Knowledge Base | Stores sample student, teacher, and course information and provides menu-based search and display operations. |

## Requirements

- Python 3.x
- No third-party libraries are required.
- The programs use Python's built-in data structures and features, including dictionaries, sets, loops, functions, and conditional statements.

## How to Run

Open a terminal in the folder containing the Python files and run each program separately:

```bash
python "Frame Representation(2).py"
python "Medical Knowledge Representation(1).py"
python "Semantic Network Construction(2).py"
python "University Knowledge Base(2).py"
```

If your system uses `python3` to run Python 3, replace `python` with `python3`.

---

## 1. Frame Representation

**File:** `Frame Representation(2).py`

### Objective

Demonstrate frame-based knowledge representation by storing information about entities as frames. Each frame contains slots (attributes) and their corresponding values.

### Frames in the Program

The program defines three frames in a nested Python dictionary named `frames`:

- **Student:** Stores the name, age, course, department, and university of a sample student.
- **Teacher:** Stores the name, age, subject, department, and university of a sample teacher.
- **Course:** Stores the course name, duration, degree type, and department.

### Main Functions

- `display_frame(frame_name)`: Checks whether a frame exists. If it does, it prints all its slots and values; otherwise, it displays `Frame not found.`
- `display_all_frames()`: Iterates through all defined frames and displays each one.

### Menu Options

1. Display All Frames
2. Search a Frame
3. Exit

The menu repeats until the user chooses to exit.

---

## 2. Medical Knowledge Representation

**File:** `Medical Knowledge Representation(1).py`

### Objective

Demonstrate a simple rule-based medical expert system. It compares symptoms entered by the user with predefined symptom sets and displays possible matching conditions.

### Knowledge Base

The program defines the following condition-to-symptom rules:

| Condition | Symptoms in the Rule |
|---|---|
| Common Cold | cough, sneezing, runny nose |
| Flu | fever, cough, body pain, headache |
| Malaria | fever, chills, sweating |
| Migraine | headache, nausea, sensitivity to light |
| Food Poisoning | vomiting, diarrhea, stomach pain |

### How It Works

1. The program displays the available symptoms.
2. The user enters symptoms separated by commas.
3. The input is split into individual symptoms, stripped of surrounding spaces, and converted to lowercase.
4. The symptoms are stored in a Python set.
5. `diagnose(symptoms)` compares the entered symptoms with each condition's symptom set using set intersection.
6. Each condition with at least one matching symptom is added to a results list.
7. Results are sorted by the number of matched symptoms, in descending order.
8. The program displays each possible condition and its match score in the form `matched/total`.

If no condition has any matching symptoms, the program displays `No matching condition found.`

**Important:** This is an educational programming demonstration, not a medical diagnosis or a substitute for professional medical advice. Its symptom rules are simplified and cannot reliably identify or rule out illnesses. Consult a qualified healthcare professional for medical concerns.

---

## 3. Semantic Network Construction

**File:** `Semantic Network Construction(2).py`

### Objective

Represent knowledge as a semantic network: a collection of nodes connected through named relationships.

### Network Representation

The semantic network is stored in a nested dictionary named `semantic_network`. Its nodes and relationships include:

| Node | Relationship | Connected Node |
|---|---|---|
| Student | `is_a` | Person |
| Student | `studies` | Course |
| Student | `belongs_to` | University |
| Teacher | `is_a` | Person |
| Teacher | `teaches` | Course |
| Teacher | `works_at` | University |
| Course | `offered_by` | University |
| Course | `has_subject` | Subject |
| University | `has` | Department |

### Main Functions

- `display_network()`: Displays every node and its relationships in an arrow-style format.
- `search_relation(node)`: Displays the relationships connected to a specified node. If the node is not present in the dictionary, it displays `Node not found.`

### Menu Options

1. Display Semantic Network
2. Search Relationships
3. Exit

The menu repeats until the user chooses to terminate the program.

**Note:** The program displays only the relationships explicitly defined in the dictionary. It does not implement automatic relationship inference or graph traversal.

---

## 4. University Knowledge Base

**File:** `University Knowledge Base(2).py`

### Objective

Create a small university information system using a Python dictionary as a knowledge base. It stores sample student records, teacher details, and available courses.

### Knowledge Base Structure

The `university` dictionary contains three main sections.

**Students**

| Student ID | Name | Course | Department |
|---|---|---|---|
| 101 | Rahul | MCA | Computer Science |
| 102 | Priya | BCA | Computer Science |
| 103 | Amit | MBA | Management |

**Teachers**

| Teacher ID | Name | Subject |
|---|---|---|
| T01 | Dr. Sharma | Artificial Intelligence |
| T02 | Dr. Verma | Database Management |

**Courses**

| Course Code | Course Name |
|---|---|
| MCA | Master of Computer Applications |
| BCA | Bachelor of Computer Applications |
| MBA | Master of Business Administration |

### Main Functions

- `search_student(student_id)`: Searches for a student using the supplied ID. If found, it displays the student's name, course, and department. Otherwise, it displays `Student not found.`
- `display_teachers()`: Displays all teacher IDs, names, and subjects.
- `display_courses()`: Displays all course codes and their full names.

### Menu Options

1. Search Student
2. Display Teachers
3. Display Courses
4. Exit

The menu repeats until the user chooses to exit.

---

## Concepts Demonstrated

| Concept | Demonstrated In |
|---|---|
| Knowledge representation | All four programs |
| Frames, slots, and values | Frame Representation |
| Nested dictionaries | Frame Representation and University Knowledge Base |
| Rule-based knowledge representation | Medical Knowledge Representation |
| Symptom matching using set intersection | Medical Knowledge Representation |
| Sorting results by match score | Medical Knowledge Representation |
| Semantic nodes and named relationships | Semantic Network Construction |
| Searching stored relationships | Semantic Network Construction |
| Knowledge-base organization | University Knowledge Base |
| Menu-driven interaction | Frame Representation, Semantic Network Construction, and University Knowledge Base |
| Functions, loops, and conditional statements | All four programs |

## Conclusion

These programs demonstrate different ways of representing and accessing knowledge in Python. Frame representation organizes information into entities and attributes, the medical example uses predefined rules to compare symptoms, semantic networks connect concepts through named relationships, and the university knowledge base stores structured institutional information.

Together, the examples introduce important AI knowledge representation concepts using simple Python data structures and interactive programs.
