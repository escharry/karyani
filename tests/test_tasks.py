import unittest
from click.testing import CliRunner
from karyani.cli import main, add, list, complete
from karyani.tasks import TaskManager
import os

class TestTaskManagerCLI(unittest.TestCase):

    def setUp(self):
        """Set up a temporary tasks file for testing."""
        # Use a different file for testing to avoid overwriting real data
        self.test_file = 'test_tasks.json'
        TaskManager.TASKS_FILE = self.test_file  # Point the task manager to the test file
        self.runner = CliRunner()
        self.manager = TaskManager()
        # Ensure the test file starts empty
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Clean up after tests by removing the test file."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        """Test adding a task via the CLI."""
        result = self.runner.invoke(add, ['Finish homework'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Task added: Finish homework', result.output)

        # Verify the task was actually added in the task manager
        tasks = self.manager.list_tasks()
        self.assertIn('Finish homework', tasks)

    def test_list_tasks(self):
        """Test listing tasks via the CLI."""
        self.manager.add_task("Do laundry")
        self.manager.add_task("Buy groceries")
        result = self.runner.invoke(list)
        self.assertEqual(result.exit_code, 0)
        self.assertIn('1. Do laundry (not completed)', result.output)
        self.assertIn('2. Buy groceries (not completed)', result.output)

    def test_complete_task(self):
        """Test completing a task via the CLI."""
        self.manager.add_task("Complete assignment")
        result = self.runner.invoke(complete, ['1'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Task 1 marked as complete.', result.output)

        # Verify the task was marked as complete
        tasks = self.manager.list_tasks()
        self.assertIn('Complete assignment (completed)', tasks)

    def test_invalid_task_completion(self):
        """Test handling invalid task ID for completion."""
        result = self.runner.invoke(complete, ['999'])  # Non-existent task ID
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Invalid task ID.', result.output)

if __name__ == '__main__':
    unittest.main()
