import click
from rich.console import Console
from rich.table import Table
from karyani.tasks import TaskManager

console = Console()


@click.group()
def main() -> None:
    """A simple CLI task manager with enhanced visuals."""


@click.command()
@click.argument('task')
@click.option('--due', '-d', help='Due date of the task.')
@click.option('--priority', '-p', type=click.Choice(['high', 'medium', 'low']), default='low', help='Priority of the task.')
def add(task: str, priority: str, due: str) -> None:
    """Add a new task."""
    priority_val = {'high': 1, 'medium': 2, 'low': 3}[priority]
    manager = TaskManager()
    manager.add_task(task, priority_val, due if due else '-')
    console.print(
        f"[green]Task added:[/green] {task} [green]with priority:[/green] {priority}")


@click.command()
@click.option('-p', '--priority', type=click.Choice(['high', 'medium', 'low']), help='Filter tasks by priority.')
@click.option('-s', '--status', type=click.Choice(['completed', 'pending']), help='Filter tasks by status.')
def list(priority: str, status: str) -> None:
    """List all tasks with a visually appealing format."""
    manager = TaskManager()
    tasks = manager.get_all_tasks()

    if priority:
        tasks = [task for task in tasks if task['priority']
                 == {'high': 1, 'medium': 2, 'low': 3}[priority]]
    if status:
        if status == 'pending':
            tasks = [task for task in tasks if not task['completed']]
        else:
            tasks = [task for task in tasks if task['completed']
                     == (status == 'completed')]

    if not tasks:
        console.print("[yellow]No tasks available.[/yellow]")
    else:
        table = Table(title="Your Tasks")
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Task", style="magenta", justify="center")
        table.add_column("Priority", justify="center")
        table.add_column("Due", justify="center")
        table.add_column("Status", style="green", justify="center")
        for i, task in enumerate(tasks, 1):
            status = "✅ Completed" if task['completed'] else "❌ Not Completed"
            priority_str = {1: '[bold red]high[/bold red]',
                            2: '[bold yellow]medium[/bold yellow]',
                            3: '[bold green]low[/bold green]'}[task['priority']]
            table.add_row(str(i), task['task'],
                          priority_str, task['due'], status)

        console.print("", table)
        console.print(f"\n[yellow]Total tasks: {len(tasks)}[/yellow], [green]Completed tasks: {len(
            [task for task in tasks if task['completed']])}[/green], [red]Pending tasks: {len([task for task in tasks if not task['completed']])}[/red]\n")


@click.command()
@click.argument('task_id', type=int)
def complete(task_id: int) -> None:
    """Mark a task as complete."""
    manager = TaskManager()
    result = manager.complete_task(task_id)
    console.print(result)


@click.command()
@click.argument('id', type=int, required=False)
@click.option('--all', '-a', is_flag=True, help='Clear all tasks, not just completed ones.')
def clear(all: bool, id: int) -> None:
    """Clears all completed tasks from karyani if no id is provided. Otherwise, clears the task with the provided id."""
    manager = TaskManager()
    if all:
        if id:
            manager.clear(id)
            console.print(f'[green]Task {id} has been cleared![/green]')
        else:
            manager.clear_all_tasks()
            console.print('[yellow]All tasks have been cleared![/yellow]')
    else:
        if id:
            manager.clear(id)
            console.print(f'[green]Task {id} has been cleared![/green]')
        else:
            manager.clear_completed_tasks()
            console.print(
                '[green]All completed tasks have been cleared![/green]')


@click.command()
@click.argument('id', type=int)
@click.option('--description', '-d', help='New description of the task.')
@click.option('--priority', '-p', type=click.Choice(['1', '2', '3']), help='New priority of the task.')
@click.option('--completed', '-c', is_flag=True, help='Mark task as completed.')
def update(id: int, description: str, priority: str, completed: bool) -> None:
    """Updates a task in karyani."""
    manager = TaskManager()
    task = manager.get_task(id)
    if task:
        if description:
            task['task'] = description
        if priority:
            task['priority'] = priority
        if completed:
            task['completed'] = True
        manager.save_tasks()
        console.print('[green]Task updated successfully![/green]')


main.add_command(add)
main.add_command(list)
main.add_command(complete)
main.add_command(clear)
main.add_command(update)

if __name__ == '__main__':
    main()
