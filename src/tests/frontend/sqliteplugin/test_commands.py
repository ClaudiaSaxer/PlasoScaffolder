import unittest

from click.testing import CliRunner
from plasoscaffolder.frontend.main import entry_point


class SqliteCommandsTest(unittest.TestCase):

  def test_sqlite_help(self):
    runner = CliRunner()
    result = runner.invoke(entry_point, ['sqlite', '--help'])
    expected_output = (
    'Usage: entry_point sqlite [OPTIONS]\n'
    '\n'
    'Options:\n'
    '  -p, --path TEXT  The path to plaso\n'
    '  --name TEXT      The plugin name\n'
    '  --testfile TEXT  The testfile path\n'
    '  --help           Show this message and exit.\n')
    self.assertEqual(expected_output, str(result.output))
    self.assertEqual(0, result.exit_code)

if __name__ == '__main__':
  unittest.main()
