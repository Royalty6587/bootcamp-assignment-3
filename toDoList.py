# Simple To-Do List Application

# Initialize an empty to-do list
to_do_list = []

# Function to display all tasks
def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(to_do_list, 1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' has been added.")

# Function to remove a task by index
def remove_task(index):
    if index > 0 and index <= len(to_do_list):
        removed = to_do_list.pop(index - 1)
        print(f"Task '{removed}' has been removed.")
    else:
        print("Invalid task number.")

# Main function to manage the to-do list
def to_do_list_manager():
    while True:
        print("\n1. View tasks\n2. Add task\n3. Remove task\n4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task you want to add: ")
            add_task(task)
        elif choice == '3':
            view_tasks()
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the to-do list manager
to_do_list_manager()
