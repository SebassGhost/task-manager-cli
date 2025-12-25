import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\nTask Manager")
    print("1. Add task")
    print("2. List tasks")
    print("3. Toggle task status")
    print("4. Exit")

def add_task(tasks):
    title = input("Task title: ")
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['title']} [{status}]")

def toggle_task(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input("Select task number: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]["completed"] = not tasks[index]["completed"]
            save_tasks(tasks)
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            add_task(tasks)
        elif option == "2":
            list_tasks(tasks)
        elif option == "3":
            toggle_task(tasks)
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
