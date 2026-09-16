tasks = []

while True:
    print("\n--- Student Task Manager ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4.Exit")
    print("5.About")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
