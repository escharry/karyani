import unittest
from click.testing import CliRunner
from karyani.cli import main

class TestTaskManagerCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_add_command(self):
        result = self.runner.invoke(main, ['add', 'Finish homework'])
        self.assertEqual(result.exit_code, 0)  # Check for successful execution
        self.assertIn('Task added: Finish homework', result.output)  # Check output

    def test_list_command(self):
        result = self.runner.invoke(main, ['list'])
        self.assertEqual(result.exit_code, 0)  # Check for successful execution
        self.assertIn('Here are your tasks...', result.output)  # Check output

    def test_add_command_missing_argument(self):
        result = self.runner.invoke(main, ['add'])
        self.assertNotEqual(result.exit_code, 0)  # Should fail with missing argument
        self.assertIn('Error: Missing argument "TASK".', result.output)  # Check error message

if __name__ == '__main__':
    unittest.main()
