# To-Do List Program in Python

# List to store the tasks
todo_list = []

# Function to display the tasks
def show_tasks():
    if len(todo_list) == 0:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to add a task to the list
def add_task():
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f"'{task}' has been added to your to-do list.")

# Function to remove a task from the list
def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 0 < task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def mark_task_completed():
    show_tasks()
    try:
        task_num = int(input("Enter the number of the task to mark as completed: "))
        if 0 < task_num <= len(todo_list):
            task = todo_list[task_num - 1] + " (Completed)"
            todo_list[task_num - 1] = task
            print(f"'{task}' is marked as completed.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

# Main menu function to interact with the user
def main_menu():
    while True:
        print("\n--- To-Do List ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task Completed")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_task_completed()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Start the program
if __name__ == "__main__":
    main_menu()
