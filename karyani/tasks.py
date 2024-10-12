import json
import os

TASKS_FILE = 'tasks.json'

class TaskManager:
    def __init__(self):
        # Load tasks from a file or create an empty list if the file doesn't exist
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def add_task(self, task: str):
        """Add a task and save to file."""
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        return f'Task added: {task}'

    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            return 'No tasks found.'
        return '\n'.join([f'{i + 1}. {t["task"]} ({"completed" if t["completed"] else "not completed"})' for i, t in enumerate(self.tasks)])
    
    def get_all_tasks(self):
        """Return all tasks."""
        return self.tasks

    def complete_task(self, task_id: int):
        """Mark a task as complete and save to file."""
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1]["completed"] = True
            self.save_tasks()
            return f'Task {task_id} marked as complete.'
        else:
            return 'Invalid task ID.'

    def save_tasks(self):
        """Save tasks to the tasks.json file."""
        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file)
