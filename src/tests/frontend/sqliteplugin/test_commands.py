# -*- coding: utf-8 -*-
"""test the commands for the sqlite plugin"""
import unittest

from click.testing import CliRunner

from plasoscaffolder.frontend.sqliteplugin.commands import sqlite


class SqliteCommandsTest(unittest.TestCase):
  """testing the sqlite commands"""
  def test_sqlite_help(self):
    """testing the help argument"""
    runner = CliRunner()
    result = runner.invoke(sqlite, ['--help'])
    expected_output = ('Usage: sqlite [OPTIONS]\n'
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
