import os

# Function to display menu options
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Save To-Do List")
    print("6. Load To-Do List")
    print("7. Exit")

# Function to view the tasks
def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{i}. {task['description']} - {status}")

# Function to add a task
def add_task(tasks):
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    print(f"Task '{description}' added.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: ")) - 1
        removed_task = tasks.pop(task_num)
        print(f"Task '{removed_task['description']}' removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to mark as completed: ")) - 1
        tasks[task_num]['completed'] = True
        print(f"Task '{tasks[task_num]['description']}' marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Function to save tasks to a file
def save_tasks(tasks, filename="todo_list.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['description']}|{task['completed']}\n")
    print(f"Tasks saved to {filename}.")

# Function to load tasks from a file
def load_tasks(filename="todo_list.txt"):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                description, completed = line.strip().split('|')
                tasks.append({"description": description, "completed": completed == 'True'})
        print(f"Tasks loaded from {filename}.")
    else:
        print(f"No saved file found. Starting with an empty list.")
    return tasks

# Main function
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            save_tasks(tasks)
        elif choice == '6':
            tasks = load_tasks()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
