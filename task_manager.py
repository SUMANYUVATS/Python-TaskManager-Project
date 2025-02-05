import os

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a file"""
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = [task.strip() for task in file.readlines()]

    def save_tasks(self):
        """Save tasks to a file"""
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self):
        """Add a new task to the task list"""
        task = input("Enter the new task: ")
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        """View all tasks"""
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Your tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def mark_completed(self):
        """Mark a task as completed by removing it"""
        self.view_tasks()
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_number <= len(self.tasks):
                completed_task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"Task '{completed_task}' completed and removed from the list!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

    def menu(self):
        """Show the main menu of the application"""
        while True:
            print("\nTask Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Exit")

            try:
                choice = int(input("Select an option (1-4): "))
                if choice == 1:
                    self.add_task()
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    self.mark_completed()
                elif choice == 4:
                    print("Exiting Task Manager. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.menu()
