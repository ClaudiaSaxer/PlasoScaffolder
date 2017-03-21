# -*- coding: utf-8 -*-
"""test class"""
import os
import tempfile
import unittest

from plasoscaffolder.bll.services import sqlite_generator
from plasoscaffolder.common import file_handler
from plasoscaffolder.common import output_handler_file
from tests.fake import fake_file_handler
from tests.fake import fake_formatter_mapping
from tests.fake import fake_init_mapping
from tests.fake import fake_mapping_helper
from tests.fake import fake_parser_mapping
from tests.fake import fake_sqlite_plugin_helper
from tests.fake import fake_sqlite_plugin_path_helper
from tests.test_helper import path_helper


class SQLiteGeneratorTest(unittest.TestCase):
  """the sqlite generator test"""

  def setUp(self):
    self.plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper( )
    self.template_path = path_helper.TemplatePath()

  def testPrintCopy(self):
    """test the print for a copy"""
    with tempfile.TemporaryDirectory() as tmpdir:
      fake_path_helper = \
        fake_sqlite_plugin_path_helper.FakeSQLitePluginPathHelper(
            self.template_path, 'test',
            'db')
      file = os.path.join(tmpdir, 'testfile')
      generator = sqlite_generator.SQLiteGenerator(
          tmpdir, 'test', 'test', ['test'],
          output_handler_file.OutputHandlerFile(file,
                                                file_handler.FileHandler()),
          self.plugin_helper, fake_path_helper)
      generator._PrintCopy(file)  # pylint: disable=W0212
      expected = "copy " + file
      actual = self._ReadFromFile(file)
    self.assertEqual(expected, actual)

  def testPrintEdit(self):
    """test the print for a edit"""
    with tempfile.TemporaryDirectory() as tmpdir:
      fake_path_helper = \
        fake_sqlite_plugin_path_helper.FakeSQLitePluginPathHelper(
            self.template_path, 'test',
            'db')
      file = os.path.join(tmpdir, 'testfile')
      generator = sqlite_generator.SQLiteGenerator(
          tmpdir, 'test', 'test', ['test'],
          output_handler_file.OutputHandlerFile(file,
                                                file_handler.FileHandler()),
          self.plugin_helper, fake_path_helper)
      generator._PrintEdit(file)  # pylint: disable=W0212
      expected = "edit " + file
      actual = self._ReadFromFile(file)
    self.assertEqual(expected, actual)

  def testPrintCreate(self):
    """test the print for a create"""
    with tempfile.TemporaryDirectory() as tmpdir:
      fake_path_helper = \
        fake_sqlite_plugin_path_helper.FakeSQLitePluginPathHelper(
            self.template_path, 'test',
            'db')
      file = os.path.join(tmpdir, 'testfile')
      generator = sqlite_generator.SQLiteGenerator(
          tmpdir, 'test', 'test', ['test'],
          output_handler_file.OutputHandlerFile(file,
                                                file_handler.FileHandler()),
          self.plugin_helper, fake_path_helper)
      generator._PrintCreate(file)  # pylint: disable=W0212
      expected = "create " + file
      actual = self._ReadFromFile(file)
    self.assertEqual(expected, actual)

  def testGenerateSQLitePlugin(self):
    """test the output of a generation of a sqlite plugin"""
    fake_handler = fake_file_handler.FakeFileHandler()
    mapping_helper = fake_mapping_helper.FakeMappingHelper(self.template_path)
    init_mapper = fake_init_mapping.FakeInitMapper(self.template_path,
                                                   mapping_helper)
    parser_mapper = fake_parser_mapping.FakeParserMapper(self.template_path,
                                                         mapping_helper)
    formatter_mapper = fake_formatter_mapping.FakeFormatterMapper(
        self.template_path, mapping_helper)
    with tempfile.TemporaryDirectory() as tmpdir:
      fake_path_helper = \
        fake_sqlite_plugin_path_helper.FakeSQLitePluginPathHelper(
            self.template_path, 'test',
            'db')
      file = os.path.join(tmpdir, 'testfile')
      generator = sqlite_generator.SQLiteGenerator(
          tmpdir, 'test', 'test', ['test'],
          output_handler_file.OutputHandlerFile(file,
                                                file_handler.FileHandler()),
          self.plugin_helper, fake_path_helper)
      generator.GenerateSQLitePlugin(tmpdir, fake_handler, init_mapper,
                                     parser_mapper, formatter_mapper,
                                     mapping_helper)
      expected = ("create testcreate testcreate testcreate testcopy testcreate "
                  "testcreate test")
      actual = self._ReadFromFile(file)
    self.assertEqual(expected, actual)

  def testPrint(self):
    """test print"""
    with tempfile.TemporaryDirectory() as tmpdir:
      fake_path_helper = \
        fake_sqlite_plugin_path_helper.FakeSQLitePluginPathHelper(
            self.template_path, 'test', 'db')
      file = os.path.join(tmpdir, 'testfile')
      generator = sqlite_generator.SQLiteGenerator(
          tmpdir, 'test', 'test', ['test'],
          output_handler_file.OutputHandlerFile(file,
                                                file_handler.FileHandler()),
          self.plugin_helper, fake_path_helper)
      generator._Print("test1", "test2", "test3", "test4", "test5", "test6",
                       "test7")  # pylint: disable=W0212
      actual = self._ReadFromFile(file)

    expected = "create test1create test2create test3create test4copy " \
               "test5create test6create test7"
    self.assertEqual(expected, actual)

  def _ReadFromFile(self, path: str):
    """read from file helper"""
    with open(path, 'r') as f:
      return f.read()


if __name__ == '__main__':
  unittest.main()
