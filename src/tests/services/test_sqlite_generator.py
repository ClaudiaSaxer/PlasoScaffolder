# -*- coding: utf-8 -*-
import os
import unittest
from plasoscaffolder.bll.services.sqlite_generator import SqliteGenerator
from plasoscaffolder.bll.services.file_handler import FileHandler

from unittest.mock import MagicMock

from tests.test_helper.path_helper import template_path


class SqliteGeneratorTest(unittest.TestCase):
  def setUp(self):
    self.path = "temp"
    self.name = "pluginname"
    self.database = "temp" + os.sep + "database"
    output_lambda = lambda x: self._writeToFile(x)
    self.testfile = "testfile.py"

    self.generator = SqliteGenerator(self.path, self.name, self.database,
      output_lambda)

  def tearDown(self):
    if os.path.isfile(self.testfile):
      os.remove(self.testfile)

  def test_print_copy(self):
    self.generator._print_copy(self.testfile)
    actual = self._readFromFile()
    expected = "copy " + self.testfile
    self.assertEqual(expected, actual)

  def test_print_edit(self):
    self.generator._print_edit(self.testfile)
    actual = self._readFromFile()
    expected = "edit " + self.testfile
    self.assertEqual(expected, actual)

  def test_print_create(self):
    self.generator._print_create(self.testfile)
    actual = self._readFromFile()
    expected = "create " + self.testfile
    self.assertEqual(expected, actual)

  def test_generate_sqlite_plugin(self):
    file_handler = FileHandler()
    file_handler.create_file_from_path = MagicMock(return_value=self.testfile)
    file_handler.copy_file = MagicMock(return_value=self.testfile)
    file_handler.add_content = MagicMock(return_value=self.testfile)
    self.generator.generate_sqlite_plugin(file_handler,template_path())
    expected = "create testfile.pycreate testfile.pycreate testfile.pycreate " \
               "testfile.pycopy testfile.pycreate testfile.pycreate testfile.py"
    actual = self._readFromFile()
    self.assertEqual(expected, actual)

  def test_print(self):
    file_handler = FileHandler
    file_handler.create_file_from_path = MagicMock(return_value=self.testfile)
    file_handler.copy_file = MagicMock(return_value=self.testfile)
    file_handler.add_content = MagicMock(return_value=self.testfile)
    self.generator._print("test1", "test2", "test3", "test4", "test5", "test6",
      "test7")
    expected = "create test1create test2create test3create test4copy " \
               "test5create test6create test7"
    actual = self._readFromFile()
    self.assertEqual(expected, actual)

  def _writeToFile(self, content):
    with open(self.testfile, 'a') as f:
      f.write(content)

  def _readFromFile(self):
    with open(self.testfile, 'r') as f:
      return f.read()


if __name__ == '__main__':
  unittest.main()
