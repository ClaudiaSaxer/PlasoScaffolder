import os
import unittest
import shutil
from pathlib import Path

from plasoscaffolder.bll.services.sqlite_plugin_helper import *


class SqlitePluginHelperTest(unittest.TestCase):
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

  def test_formatter_file(self):
    actual = formatter_file_path(self.path, self.plugin_name)
    self.assertEqual(actual, self.formatter)

  def test_formatter_test_file(self):
    actual = formatter_test_file_path(self.path, self.plugin_name)
    self.assertEqual(self.formatter_test, actual)

  def test_parser_file(self):
    actual = parser_file_path(self.path, self.plugin_name)
    self.assertEqual(self.parser, actual)

  def test_parser_test_file(self):
    actual = parser_test_file_path(self.path, self.plugin_name)
    self.assertEqual(self.parser_test, actual)

  def test_plugin_exists_false(self):
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertFalse(actual)

  def test_plugin_exists_true_1(self):
    os.makedirs(os.path.dirname(self.parser))
    Path(self.parser).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)

  def test_plugin_exists_true_2(self):
    os.makedirs(os.path.dirname(self.parser_test))
    Path(self.parser_test).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)

  def test_plugin_exists_true_3(self):
    os.makedirs(os.path.dirname(self.formatter))
    Path(self.formatter).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)

  def test_plugin_exists_true_4(self):
    os.makedirs(os.path.dirname(self.formatter_test))
    Path(self.formatter_test).touch()
    actual = plugin_exists(self.path, self.plugin_name)
    self.assertTrue(actual)
    shutil.rmtree(self.path)


if __name__ == '__main__':
  unittest.main()
