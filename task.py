class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TodoList:
    def __init__(self):
        self.tasks = []

    # Function to add a new task
    def add_task(self, description, priority):
        new_task = Task(description, priority)
        self.tasks.append(new_task)
        print(f"Task '{description}' added.")

    # Function to remove a completed task
    def remove_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                print(f"Task '{description}' removed.")
                return
        print(f"Task '{description}' not found.")

    # Function to update task description
    def update_task_description(self, old_description, new_description):
        for task in self.tasks:
            if task.description == old_description:
                task.description = new_description
                print(f"Task '{old_description}' updated to '{new_description}'.")
                return
        print(f"Task '{old_description}' not found.")

    # Function to reorder tasks based on priority
    def reorder_tasks(self):
        self.tasks.sort(key=lambda task: task.priority)
        print("Tasks reordered based on priority.")

    # Function to display all tasks
    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for task in self.tasks:
                print(f"Description: {task.description}, Priority: {task.priority}")

# Example usage
if __name__ == "__main__":
    todo_list = TodoList()

    # Add new tasks
    todo_list.add_task("Complete project report", 2)
    todo_list.add_task("Review code", 1)
    todo_list.add_task("Prepare for meeting", 3)

    # Display tasks
    print("\nCurrent Tasks:")
    todo_list.display_tasks()

    # Update a task description
    todo_list.update_task_description("Review code", "Code review")

    # Remove a completed task
    todo_list.remove_task("Complete project report")

    # Reorder tasks based on priority
    todo_list.reorder_tasks()

    # Display tasks after reordering
    print("\nTasks after reordering:")
    todo_list.display_tasks()
