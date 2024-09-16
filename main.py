from task_manager import TaskManager
from storage import Storage


def show_menu():
    print("\nTask Management System")
    print("======================")
    print("1. Add a New Task")
    print("2. Complete a Task")
    print("3. List All Tasks")
    print("4. Generate Task Report")
    print("5. Exit")


def get_user_choice():
    while True:
        try:
            choice = int(input("\nChoose an option (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a valid option (1-5).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


def prompt_task_details():
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    if not title or not description:
        print("Both title and description are required!")
        return None, None
    return title, description


def prompt_task_completion(manager: TaskManager):
    """Display pending tasks for completion and allow the user to select one."""
    tasks = manager.list_tasks(include_completed=False)  # Only show pending tasks
    if not tasks:
        print("No pending tasks to complete.")
        return None

    print("\nPending Tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. ID: {task.id}, Title: {task.title}")

    while True:
        try:
            task_choice = int(input("\nSelect the task number to mark as complete (or 0 to cancel): "))
            if task_choice == 0:
                return None  # User chose to cancel
            if 1 <= task_choice <= len(tasks):
                return tasks[task_choice - 1].id  # Return the selected task's ID
            else:
                print(f"Please choose a valid task number (1-{len(tasks)}) or 0 to cancel.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")


def main():
    storage = Storage()
    manager = TaskManager(storage)

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 1:
            # Add a new task
            title, description = prompt_task_details()
            if title and description:
                task = manager.add_task(title, description)
                print(f"Task '{task.title}' added successfully with ID: {task.id}.")
        
        elif choice == 2:
            # Complete a task
            task_id = prompt_task_completion(manager)
            if task_id:
                if manager.complete_task(task_id):
                    print(f"Task '{task_id}' marked as completed.")
                else:
                    print(f"Task with ID '{task_id}' not found.")

        elif choice == 3:
            # List tasks
            include_completed = input("Show completed tasks as well? (y/n): ").strip().lower() == 'y'
            tasks = manager.list_tasks(include_completed=include_completed)
            if tasks:
                print("\nTask List:")
                for task in tasks:
                    status = "Completed" if task.completed else "Pending"
                    print(f"ID: {task.id}, Title: {task.title} - {status}")
            else:
                print("No tasks found.")
        
        elif choice == 4:
            # Generate report
            report = manager.generate_report()
            print("\nTask Report:")
            print(f"Total Tasks: {report['total']}")
            print(f"Completed Tasks: {report['completed']}")
            print(f"Pending Tasks: {report['pending']}")
            print(f"Average Completion Time: {report['average_completion_time']}")
        
        elif choice == 5:
            # Exit
            print("Exiting the Task Management System. Goodbye!")
            break


if __name__ == "__main__":
    main()
