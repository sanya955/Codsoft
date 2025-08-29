tasks = []  # list of [task_name, done_status]

while True:
    print("\nTo-Do List Menu:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                status = "Done" if task[1] else "Not Done"
                print(f"{i}. {task[0]} [{status}]")

    elif choice == "2":
        title = input("Enter task name: ").strip()
        if title:
            tasks.append([title, False])
            print(f"Task '{title}' added.")
        else:
            print("Task name cannot be empty.")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task[0]} [{'Done' if task[1] else 'Not Done'}]")
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1][1] = True
                    print(f"Task '{tasks[num - 1][0]}' marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task[0]} [{'Done' if task[1] else 'Not Done'}]")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Task '{removed[0]}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
