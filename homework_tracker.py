assignments = []

print("---- Homework Tracker ----")

while True:
    print("1. Add assignment")
    print("2. View assignments")
    print("3. Complete assignment")
    print("4. Save and Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number between 1 and 4.\n")
        continue

    if choice == 1:
        assignment = input("Enter the assignment name: ")
        priority = input("Enter the priority (High/Medium/Low): ")
        due_date = input("Enter the number of days until due: ")
        assignments.append((assignment, priority, due_date))
        print(f"Assignment '{assignment}' added.\n")
    elif choice == 2:
        if not assignments:
            print("No assignments yet.\n")
        else:
            print("Current assignments:")
            for index, (assignment, priority, due_date) in enumerate(assignments, start=1):
                print(f"{index}. {assignment} | {priority} | due in {due_date} days")
            print()
    elif choice == 3:
        if not assignments:
            print("No assignments to complete.\n")
            continue
        assignment = input("Enter the assignment name to complete: ")
        before_count = len(assignments)
        assignments = [item for item in assignments if item[0] != assignment]
        if len(assignments) < before_count:
            print(f"Assignment '{assignment}' marked as completed.\n")
        else:
            print(f"Assignment '{assignment}' not found.\n")
    elif choice == 4:
        print("Saving and exiting...")
        break
    else:
        print("Invalid choice. Please try again.\n")
