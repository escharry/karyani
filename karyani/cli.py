import click

@click.group()
def main():
    """A simple CLI task manager."""
    pass

@click.command()
@click.argument('task')
def add(task):
    """Add a new task."""
    click.echo(f'Task added: {task}')

@click.command()
def list():
    """List all tasks."""
    click.echo('Here are your tasks...')

@click.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Mark a task as complete."""
    click.echo(f'Task {task_id} marked as complete.')

# Adding the commands to the main CLI group
main.add_command(add)
main.add_command(list)
main.add_command(complete)

if __name__ == '__main__':
    main()
