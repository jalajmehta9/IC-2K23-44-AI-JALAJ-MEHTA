# Vacuum Cleaner Problem

room_a = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_b = input("Enter status of Room B (Clean/Dirty): ").capitalize()

location = input("Enter vacuum location (A/B): ").upper()

print("\nInitial State:")
print("Room A:", room_a)
print("Room B:", room_b)
print("Vacuum Location:", location)

# If vacuum is in Room A
if location == "A":

    if room_a == "Dirty":
        print("\nAction: Suck dirt from Room A")
        room_a = "Clean"

    if room_b == "Dirty":
        print("Action: Move from A to B")
        location = "B"

        print("Action: Suck dirt from Room B")
        room_b = "Clean"

# If vacuum is in Room B
elif location == "B":

    if room_b == "Dirty":
        print("\nAction: Suck dirt from Room B")
        room_b = "Clean"

    if room_a == "Dirty":
        print("Action: Move from B to A")
        location = "A"

        print("Action: Suck dirt from Room A")
        room_a = "Clean"

else:
    print("Invalid location!")

print("\nFinal State:")
print("Room A:", room_a)
print("Room B:", room_b)
print("Vacuum Location:", location)

if room_a == "Clean" and room_b == "Clean":
    print("\nGoal Achieved: Both rooms are clean.")