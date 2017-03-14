import unittest
import click
from click.testing import CliRunner
from plasoscaffolder.frontend.main import entry_point


class MyTestCase(unittest.TestCase):
  def test_sqlite_help(self):
    runner = CliRunner()
    result = runner.invoke(entry_point, ['--help'])
    expected_output = (
      'Usage: entry_point [OPTIONS] COMMAND [ARGS]...'
      '\n'
      '\n'
      'Options:'
      '\n'
      '  --help  '
      'Show this message and exit.'
      '\n'
      '\n'
      'Commands:'
      '\n'
      '  sqlite\n'
    )

    self.assertEqual(expected_output, str(result.output))
    self.assertEqual(0, result.exit_code)


if __name__ == '__main__':
  unittest.main()
