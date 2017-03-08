import os
import unittest
import shutil
from pathlib import Path

from plasoscaffolder.bll.services.sqlite_plugin_helper import *


class SqlitePluginHelperTest(unittest.TestCase):
  """  Class representing a test case testing the SQLite plugin helper"""
  path = "temp"
  plugin_name = "plugin_test"
  plugin_file = plugin_name + ".py"
  formatter = path + os.sep + "plaso" + os.sep + "formatters" + os.sep + \
              plugin_file
  formatter_test = path + os.sep + "tests" + os.sep + "formatters" + os.sep + \
                   plugin_file
  parser = path + os.sep + "plaso" + os.sep + "parsers" + os.sep + \
           "sqlite_plugins" + os.sep + plugin_file
  parser_test = path + os.sep + "tests" + os.sep + "parsers" + os.sep + \
                "sqlite_plugins" + os.sep + plugin_file
  database = path + os.sep + "test_data" + os.sep + plugin_name + ".db"

  def test_formatter_file(self):
    """Tests the creation of the path for the formatter file."""
    actual = formatter_file_path(self.path, self.plugin_name)
    self.assertEqual(actual, self.formatter)

  def test_formatter_test_file(self):
    """Tests the creation of the path for the formatter test file."""
    actual = formatter_test_file_path(self.path, self.plugin_name)
    self.assertEqual(self.formatter_test, actual)

  def test_parser_file(self):
    """Tests the creation of the path for the parser file."""
    actual = parser_file_path(self.path, self.plugin_name)
    self.assertEqual(self.parser, actual)

  def test_parser_test_file(self):
    """Tests the creation of the path for the parser test file."""
    actual = parser_test_file_path(self.path, self.plugin_name)
    self.assertEqual(self.parser_test, actual)

  def test_database_file(self):
    """Tests the creation of the path for the database file."""
    actual = database_path(self.path, self.plugin_name)
    self.assertEqual(self.database, actual)

  def test_plugin_exists_false(self):
    """Tests the plugin exists method if none exists."""
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertFalse(actual)

  def test_plugin_exists_true_1(self):
    """Tests the plugin exists method if the parser file exists."""
    os.makedirs(os.path.dirname(self.parser))
    Path(self.parser).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)

  def test_plugin_exists_true_2(self):
    """Tests the plugin exists method if the parser test file exists."""
    os.makedirs(os.path.dirname(self.parser_test))
    Path(self.parser_test).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)

  def test_plugin_exists_true_3(self):
    """Tests the plugin exists method if the formatter file exists."""
    os.makedirs(os.path.dirname(self.formatter))
    Path(self.formatter).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)

  def test_plugin_exists_true_4(self):
    """Tests the plugin exists method if the formatter test file exists."""
    os.makedirs(os.path.dirname(self.formatter_test))
    Path(self.formatter_test).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)

  def test_plugin_exists_true_5(self):
    """Tests the plugin exists method if the database file exists."""
    os.makedirs(os.path.dirname(self.database))
    Path(self.database).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)

  def test_file_exists(self):
    """ test the method that checks if the file exists """
    expected_content = "this is test content."
    source = "temp"
    self.assertFalse(file_exists(source))
    with open(source, "a+") as f:
      f.write(expected_content)
    self.assertTrue(isfile(source))
    os.remove(source)


  def test_folder_exists(self):
    """test the method that checks if folder exists"""
    source = "temp"
    self.assertFalse(folder_exists(source))
    os.makedirs(source)
    self.assertTrue(folder_exists(source))
    os.removedirs(source)

if __name__ == '__main__':
  unittest.main()
