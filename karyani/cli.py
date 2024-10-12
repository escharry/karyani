import click
from rich.console import Console
from rich.table import Table
from tabulate import tabulate
from karyani.tasks import TaskManager

console = Console()

@click.group()
def main():
    """A simple CLI task manager with enhanced visuals."""
    pass

@click.command()
@click.argument('task')
def add(task):
    """Add a new task."""
    manager = TaskManager()
    manager.add_task(task)
    console.print(f"[green]Task added:[/green] {task}")

@click.command()
def list():
    """List all tasks with a visually appealing format."""
    manager = TaskManager()
    tasks = manager.get_all_tasks()

    if not tasks:
        console.print("[yellow]No tasks available.[/yellow]")
    else:
        # Rich Table
        table = Table(title="Your Tasks")
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Task", style="magenta")
        table.add_column("Status", style="green", justify="center")

        for i, task in enumerate(tasks, 1):
            status = "✅ Completed" if task['completed'] else "❌ Not Completed"
            table.add_row(str(i), task['task'], status)

        console.print(table)

@click.command()
@click.argument('task_id', type=int)
def complete(task_id: int):
    """Mark a task as complete."""
    manager = TaskManager()
    result = manager.complete_task(task_id)
    
    if result:
        console.print(f"[green]Task {task_id} marked as complete![/green]")
    else:
        console.print(f"[red]Task {task_id} not found.[/red]")

# Adding the commands to the main CLI group
main.add_command(add)
main.add_command(list)
main.add_command(complete)

if __name__ == '__main__':
    main()
