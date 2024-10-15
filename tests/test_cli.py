import unittest
from click.testing import CliRunner
from karyani.cli import main


class TestTaskManagerCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_add_command(self):
        result = self.runner.invoke(main, ['add', 'Finish homework'])
        self.assertEqual(result.exit_code, 0)  # Check for successful execution
        self.assertIn('Task added: Finish homework',
                      result.output)  # Check output

    def test_list_command(self):
        result = self.runner.invoke(main, ['list'])
        self.assertEqual(result.exit_code, 0)  # Check for successful execution
        self.assertIn('Your tasks', result.output)  # Check output

    def test_add_command_missing_argument(self):
        result = self.runner.invoke(main, ['add'])
        # Should fail with missing argument
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn('Usage: karyani add [OPTIONS] TASK', result.output)


if __name__ == '__main__':
    unittest.main()
