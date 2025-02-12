def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip().split("|", 1) for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task, completed in tasks:
            file.write(f"{task}|{completed}\n")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append([task, "False"])
    save_tasks(tasks)
    print("Task added successfully!\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
    else:
        for idx, (task, completed) in enumerate(tasks, 1):
            status = "[✓]" if completed == "True" else "[ ]"
            print(f"{idx}. {status} {task}")
    print()

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no][1] = "True"
            save_tasks(tasks)
            print("Task marked as completed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks.pop(task_no)
            save_tasks(tasks)
            print("Task removed successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("To-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
