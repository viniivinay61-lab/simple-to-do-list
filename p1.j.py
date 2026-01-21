tasks = []

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. {task['name']} [{status}]")

while True:
    print("\nMenu:")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Remove a Task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_tasks()

    elif choice == "2":
        name = input("Enter task name: ")
        tasks.append({"name": name, "done": False})
        print("Task added.")

    elif choice == "3":
        display_tasks()
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        display_tasks()
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")