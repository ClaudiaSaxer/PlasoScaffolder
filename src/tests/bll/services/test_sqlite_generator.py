# -*- coding: utf-8 -*-
import os
import tempfile
import unittest
from plasoscaffolder.bll.services.sqlite_generator import SqliteGenerator
from plasoscaffolder.common.file_handler import FileHandler
from plasoscaffolder.common.output_handler_file import OutputHandlerFile
from tests.fake.fake_file_handler import FakeFileHandler
from tests.fake.fake_init_mapping import FakeInitMapper
from tests.fake.fake_mapping_helper import FakeMappingHelper
from tests.fake.fake_sqlite_plugin_helper import FakeSqlitePluginHelper
from tests.fake.fake_sqlite_plugin_path_helper import FakeSqlitePluginPathHelper


class SqliteGeneratorTest(unittest.TestCase):
  def setUp(self):

    self.output_lambda = lambda x: self._writeToFile(x)
    self.plugin_helper = FakeSqlitePluginHelper
    self.testfile = "temp"

  def tearDown(self):
    if os.path.isfile(self.testfile):
      os.remove(self.testfile)

  def test_print_copy(self):
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSqlitePluginPathHelper
      file = os.path.join(tmpdir, 'testfile')
      generator = SqliteGenerator(tmpdir, 'test', 'test',
        OutputHandlerFile(file, FileHandler), self.plugin_helper, path_helper)
      generator._print_copy(file)
      expected = "copy " + file
      actual = self._readFromFile(file)
    self.assertEqual(expected, actual)

  def test_print_edit(self):
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSqlitePluginPathHelper
      file = os.path.join(tmpdir, 'testfile')
      generator = SqliteGenerator(tmpdir, 'test', 'test',
        OutputHandlerFile(file, FileHandler), self.plugin_helper, path_helper)
      generator._print_edit(file)
      expected = "edit " + file
      actual = self._readFromFile(file)
    self.assertEqual(expected, actual)

  def test_print_create(self):
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSqlitePluginPathHelper
      file = os.path.join(tmpdir, 'testfile')
      generator = SqliteGenerator(tmpdir, 'test', 'test',
        OutputHandlerFile(file, FileHandler), self.plugin_helper, path_helper)
      generator._print_create(file)
      expected = "create " + file
      actual = self._readFromFile(file)

  def test_generate_sqlite_plugin(self):
    file_handler = FakeFileHandler
    init_mapper = FakeInitMapper
    mapping_helper = FakeMappingHelper
    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSqlitePluginPathHelper
      file = os.path.join(tmpdir, 'testfile')
      generator = SqliteGenerator(tmpdir, 'test', 'test',
        OutputHandlerFile(file, FileHandler), self.plugin_helper, path_helper)
      generator.generate_sqlite_plugin(tmpdir, file_handler, init_mapper,
        mapping_helper)
      out = os.path.join(tmpdir, 'test')
      init = os.path.join(tmpdir, '__init__.py')
      expected = (
        "create testcreate testcreate testcreate testcopy testcreate "
        "testcreate "
        "test")
      actual = self._readFromFile(file)
    self.assertEqual(expected, actual)

  def test_print(self):

    with tempfile.TemporaryDirectory() as tmpdir:
      path_helper = FakeSqlitePluginPathHelper
      file = os.path.join(tmpdir, 'testfile')
      generator = SqliteGenerator(tmpdir, 'test', 'test',
        OutputHandlerFile(file, FileHandler), self.plugin_helper, path_helper)
      generator._print("test1", "test2", "test3", "test4", "test5", "test6",
        "test7")
      actual = self._readFromFile(file)

    expected = "create test1create test2create test3create test4copy " \
               "test5create test6create test7"
    self.assertEqual(expected, actual)

  def _readFromFile(self, path: str):
    with open(path, 'r') as f:
      return f.read()


if __name__ == '__main__':
  unittest.main()
