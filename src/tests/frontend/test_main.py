import unittest
from click.testing import CliRunner
from plasoscaffolder.frontend.main import entry_point


class MainTest(unittest.TestCase):
  def test_main_help(self):
    runner = CliRunner()
    result = runner.invoke(entry_point, ['--help'])
    expected_output = (
      'Usage: entry_point [OPTIONS] COMMAND [ARGS]...\n'
      '\n'
      'Options:\n'
      '  --help  Show this message and exit.\n'
      '\n'
      'Commands:''\n'
      '  sqlite\n'
    )

    self.assertEqual(expected_output, str(result.output))
    self.assertEqual(0, result.exit_code)

  def test_sqlite_help(self):
    runner = CliRunner()
    result = runner.invoke(entry_point, ['sqlite', '--help'])
    expected_output = (
    'Usage: entry_point sqlite [OPTIONS]\n'
    '\n'
    'Options:\n'
    '  --path TEXT      The path to plaso\n'
    '  --name TEXT      The plugin name\n'
    '  --testfile TEXT  The testfile path\n'
    '  --event TEXT     The plugin events\n'
    '  --help           Show this message and exit.\n')
    self.assertEqual(expected_output, str(result.output))
    self.assertEqual(0, result.exit_code)

if __name__ == '__main__':
  unittest.main()
