

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu options
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Function to view all tasks
def view_task():
    # Check if the tasks list is empty
    if not tasks:
        print("\nNo tasks available")
    else:
        # Display all tasks with their status
        print("\n--- Your Tasks ---")
        # Loop through the tasks list and display each task
        for index, task in enumerate(tasks, start=1):
            # Check if the task is completed
            status = "Done" if task["completed"] else "Not Done"
            # Print the task number, name, and status
            print(f"{index}. {task['name']} - {status}")

# Function to add a new task
def add_task():
    # Prompt the user to enter the task name
    task_name = input("\nEnter the task name: ")
    # Add the task to the tasks list as a dictionary
    tasks.append({"name": task_name, "completed": False})
    # Confirm that the task has been added
    print(f"Task '{task_name}' added successfully!")

# Function to mark a task as completed
def mark_completed():
    # Display all tasks
    view_task()
    try:
        # Prompt the user to enter the task number to mark as completed
        task_number = int(input("\nEnter the task number to mark as completed: "))
        # Check if the task number is valid
        if 1 <= task_number <= len(tasks):
            # Mark the task as completed
            tasks[task_number - 1]["completed"] = True
            # Confirm that the task has been marked as completed
            print(f"Task '{tasks[task_number - 1]['name']}' marked as completed!")
        else:
            # Display an error message if the task number is invalid
            print("Invalid task number.")
    except ValueError:
        # Handle invalid input (e.g., non-integer input)
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    # Display all tasks
    view_task()
    try:
        # Prompt the user to enter the task number to delete
        task_number = int(input("\nEnter the task number to delete: "))
        # Check if the task number is valid
        if 1 <= task_number <= len(tasks):
            # Remove the task from the tasks list
            deleted_task = tasks.pop(task_number - 1)
            # Confirm that the task has been deleted
            print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
            # Display an error message if the task number is invalid
            print("Invalid task number.")
    except ValueError:
        # Handle invalid input (e.g., non-integer input)
        print("Please enter a valid number.")

# Main function to run the program
def main():
    while True:
        # Display the menu
        show_menu()
        # Prompt the user to enter their choice
        choice = input("\nEnter your choice (1-5): ")

        # Handle the user's choice
        if choice == "1":
            view_task()  # View tasks
        elif choice == "2":
            add_task()  # Add a new task
        elif choice == "3":
            mark_completed()  # Mark a task as completed
        elif choice == "4":
            delete_task()  # Delete a task
        elif choice == "5":
            # Exit the program
            print("\nExiting the to-do list. Goodbye!")
            break
        else:
            # Handle invalid choices
            print("\nInvalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
