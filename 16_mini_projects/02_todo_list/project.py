"""Console to-do list mini-project."""

def show_menu():
    print("\nTo-Do Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")


def todo_app():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    todo_app()
