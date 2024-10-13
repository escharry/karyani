import click
from rich.console import Console
from rich.table import Table
from tabulate import tabulate
from karyani.tasks import TaskManager

console = Console()

@click.group()
def main() -> None:
    """A simple CLI task manager with enhanced visuals."""

@click.command()
@click.argument('task')
@click.option('--priority', '-p', type=click.Choice(['1', '2', '3']), default='3', help='Priority of the task (1=high, 2=medium, 3=low).')
def add(task, priority) -> None:
    """Add a new task."""
    manager = TaskManager()
    manager.add_task(task, priority)
    console.print(f"[green]Task added:[/green] {task} [green]with priority {priority}[/green]")

@click.command()
def list() -> None:
    """List all tasks with a visually appealing format."""
    manager = TaskManager()
    tasks = manager.get_all_tasks()

    if not tasks:
        console.print("[yellow]No tasks available.[/yellow]")
    else:
        table = Table(title="Your Tasks")
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Task", style="magenta")
        table.add_column("Priority", style="red", justify="center")
        table.add_column("Status", style="green", justify="center")

        for i, task in enumerate(tasks, 1):
            status = "✅ Completed" if task['completed'] else "❌ Not Completed"
            table.add_row(str(i), task['task'], str(task['priority']), status)

        console.print(table)

@click.command()
@click.argument('task_id', type=int)
def complete(task_id: int) -> None:
    """Mark a task as complete."""
    manager = TaskManager()
    result = manager.complete_task(task_id)
    console.print(result)

@click.command()
@click.option('--all', '-a', is_flag=True, help='Clear all tasks, not just completed ones.')
def clear(all: bool) -> None:
    """Clears all completed tasks from karyani."""
    manager = TaskManager()
    if all:
        manager.clear_all_tasks()
        click.echo('All tasks have been cleared!')
    else:
        manager.clear_completed_tasks()
        click.echo('All completed tasks have been cleared!')


main.add_command(add)
main.add_command(list)
main.add_command(complete)
main.add_command(clear)

if __name__ == '__main__':
    main()
