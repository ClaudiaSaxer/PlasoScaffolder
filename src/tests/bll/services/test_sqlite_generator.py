# -*- coding: utf-8 -*-
"""test class"""
import os
import tempfile
import unittest

from plasoscaffolder.bll.services.sqlite_generator import SQLiteGenerator
from plasoscaffolder.common.file_handler import FileHandler
from plasoscaffolder.common.output_handler_file import OutputHandlerFile
from tests.fake.fake_file_handler import FakeFileHandler
from tests.fake.fake_formatter_mapping import FakeFormatterMapper
from tests.fake.fake_init_mapping import FakeInitMapper
from tests.fake.fake_mapping_helper import FakeMappingHelper
from tests.fake.fake_parser_mapping import FakeParserMapper
from tests.fake.fake_sqlite_plugin_helper import FakeSQLitePluginHelper
from tests.fake.fake_sqlite_plugin_path_helper import FakeSQLitePluginPathHelper


class SQLiteGeneratorTest(unittest.TestCase):
  """the sqlite generator test"""

  def setUp(self):
    self.plugin_helper = FakeSQLitePluginHelper
    self.testfile = "temp"

  def tearDown(self):
    if os.path.isfile(self.testfile):
      os.remove(self.testfile)

  def testPrintCopy(self):
    """test the print for a copy"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSQLitePluginPathHelper
      file = os.path.join(tmpdir, '__testfile')
      generator = SQLiteGenerator(tmpdir, 'test', 'test', ['test'],
                                  OutputHandlerFile(file, FileHandler),
                                  self.plugin_helper, path_helper)
      generator._PrintCopy(file)  # pylint: disable=W0212
      expected = "copy " + file
      actual = self._ReadFromFile(file)
    self.assertEqual(expected, actual)

  def testPrintEdit(self):
    """test the print for a edit"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSQLitePluginPathHelper
      file = os.path.join(tmpdir, '__testfile')
      generator = SQLiteGenerator(tmpdir, 'test', 'test', ['test'],
                                  OutputHandlerFile(file, FileHandler),
                                  self.plugin_helper, path_helper)
      generator._PrintEdit(file)  # pylint: disable=W0212
      expected = "edit " + file
      actual = self._ReadFromFile(file)
    self.assertEqual(expected, actual)

  def testPrintCreate(self):
    """test the print for a create"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSQLitePluginPathHelper
      file = os.path.join(tmpdir, '__testfile')
      generator = SQLiteGenerator(tmpdir, 'test', 'test', ['test'],
                                  OutputHandlerFile(file, FileHandler),
                                  self.plugin_helper, path_helper)
      generator._PrintCreate(file)  # pylint: disable=W0212
      expected = "create " + file
      actual = self._ReadFromFile(file)
    self.assertEqual(expected, actual)

  def testGenerateSQLitePlugin(self):
    """test the output of a generation of a sqlite plugin"""
    file_handler = FakeFileHandler
    init_mapper = FakeInitMapper
    parser_mapper = FakeParserMapper
    formatter_mapper = FakeFormatterMapper
    mapping_helper = FakeMappingHelper
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSQLitePluginPathHelper
      file = os.path.join(tmpdir, '__testfile')
      generator = SQLiteGenerator(tmpdir, 'test', 'test', ['test'],
                                  OutputHandlerFile(file, FileHandler),
                                  self.plugin_helper, path_helper)
      generator.GenerateSQLitePlugin(tmpdir, file_handler, init_mapper,
                                     parser_mapper, formatter_mapper,
                                     mapping_helper)
      expected = ("create testcreate testcreate testcreate testcopy testcreate "
                  "testcreate test")
      actual = self._ReadFromFile(file)
    self.assertEqual(expected, actual)

  def testPrint(self):
    """test print"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSQLitePluginPathHelper
      file = os.path.join(tmpdir, '__testfile')
      generator = SQLiteGenerator(tmpdir, 'test', 'test', ['test'],
                                  OutputHandlerFile(file, FileHandler),
                                  self.plugin_helper, path_helper)
      generator._Print("test1", "test2", "test3", "test4", "test5", "test6",
                       "test7")  # pylint: disable=W0212
      actual = self._ReadFromFile(file)

    expected = "create test1create test2create test3create test4copy " \
               "test5create test6create test7"
    self.assertEqual(expected, actual)

  def _ReadFromFile(self, path: str):
    """read from file __helper"""
    with open(path, 'r') as f:
      return f.read()


if __name__ == '__main__':
  unittest.main()
