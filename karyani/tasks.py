import json
import os

TASKS_FILE = 'tasks.json'


class TaskManager:
    def __init__(self) -> None:
        # Load tasks from a file or create an empty list if the file doesn't exist
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def add_task(self, task: str, prio: int, due: str) -> None:
        """Add a task and save to file."""
        self.tasks.append({"task": task, "priority": prio,
                          "completed": False, "due": due})
        self.save_tasks()

    def list_tasks(self) -> None:
        """List all tasks."""
        if not self.tasks:
            return 'No tasks found.'
        return '\n'.join([f'{i + 1}. {t["task"]} ({"completed" if t["completed"] else "not completed"})' for i, t in enumerate(self.tasks)])

    def get_all_tasks(self):  # -> list[Any]:
        """Return all tasks."""
        return sorted(self.tasks, key=lambda task: int(task['priority']))

    def complete_task(self, task_id: int) -> str:
        """Mark a task as complete and save to file."""
        if 0 < task_id <= len(self.tasks):
            if self.tasks[task_id - 1]["completed"]:
                return f'[yellow]Task {task_id} is already marked as complete![/yellow]'
            self.tasks[task_id - 1]["completed"] = True
            self.save_tasks()
            return f'[green]Task {task_id} marked as complete.[/green]'
        else:
            return '[red]Invalid task ID.[/red]'

    def clear_completed_tasks(self) -> None:
        """Clears completed tasks in karyani."""
        self.tasks = [task for task in self.tasks if not task['completed']]
        self.save_tasks()

    def clear_all_tasks(self) -> None:
        """Clears all tasks in karyani."""
        self.tasks = []
        self.save_tasks()

    def clear(self, id: int) -> None:
        """Clears a task by ID."""
        if 0 < id <= len(self.tasks):
            self.tasks.pop(id - 1)
            self.save_tasks()

    def save_tasks(self) -> None:
        """Save tasks to the tasks.json file."""
        self.tasks = sorted(self.tasks, key=lambda task: int(task['priority']))

        with open(TASKS_FILE, 'w') as file:
            json.dump(self.tasks, file)

    def get_task(self, id: int) -> str:
        """Get a task by ID."""
        if 0 < id <= len(self.tasks):
            return self.tasks[id - 1]
        else:
            return None
