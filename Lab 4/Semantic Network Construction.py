
# Semantic Network Construction
# No external libraries required

semantic_network = {
    "Student": {
        "is_a": "Person",
        "studies": "Course",
        "belongs_to": "University"
    },

    "Teacher": {
        "is_a": "Person",
        "teaches": "Course",
        "works_at": "University"
    },

    "Course": {
        "offered_by": "University",
        "has_subject": "Subject"
    },

    "University": {
        "has": "Department"
    }
}


def display_network():
    print("\n===== SEMANTIC NETWORK =====")

    for node, relations in semantic_network.items():
        print("\nNode:", node)

        for relation, connected_node in relations.items():
            print(f"  --{relation}--> {connected_node}")


def search_relation(node):
    if node in semantic_network:
        print("\nRelationships of", node)

        for relation, connected_node in semantic_network[node].items():
            print(node, "--", relation, "-->", connected_node)

    else:
        print("Node not found.")


while True:
    print("\n===== SEMANTIC NETWORK MENU =====")
    print("1. Display Semantic Network")
    print("2. Search Relationships")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_network()

    elif choice == "2":
        node = input("Enter node name: ").strip()
        search_relation(node)

    elif choice == "3":
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")