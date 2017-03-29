# -*- coding: utf-8 -*-
"""testing the main"""
import unittest

from click.testing import CliRunner

from plasoscaffolder.frontend import main


class MainTest(unittest.TestCase):
  """the main test"""

  def testMainHelp(self):
    """testing the help of the main"""
    runner = CliRunner()
    result = runner.invoke(main.entry_point, ['--help'])
    expected_output = ('Usage: entry_point [OPTIONS] COMMAND [ARGS]...\n'
                       '\n'
                       'Options:\n'
                       '  --help  Show this message and exit.\n'
                       '\n'
                       'Commands:''\n'
                       '  sqlite\n')

    self.assertEqual(expected_output, str(result.output))
    self.assertEqual(0, result.exit_code)

  def testSQLiteHelp(self):
    """testing the main of the sqlite"""
    runner = CliRunner()
    result = runner.invoke(main.entry_point, ['sqlite', '--help'])
    expected_output = ('Usage: entry_point sqlite [OPTIONS]\n'
                       '\n'
                       'Options:\n'
                       '  --path TEXT      The path to plaso\n'
                       '  --name TEXT      The plugin name\n'
                       '  --testfile TEXT  The testfile path\n'
                       '  --event TEXT     The plugin events\n'
                       '  --sql            The output example flag for the SQL Query for the plugin.\n'
                       '  --help           Show this message and exit.\n')
    self.assertEqual(expected_output, str(result.output))
    self.assertEqual(0, result.exit_code)


if __name__ == '__main__':
  unittest.main()