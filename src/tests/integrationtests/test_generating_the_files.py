"""the integration tests"""
import os
import tempfile
import unittest

from plasoscaffolder.bll.services import sqlite_plugin_helper
from plasoscaffolder.bll.services import sqlite_plugin_path_helper
from plasoscaffolder.common import file_handler
from plasoscaffolder.dal import sqlite_query_execution
from plasoscaffolder.frontend.controller import sqlite_controller
from plasoscaffolder.model import sql_query_model
from tests.test_helper import output_handler_file
from tests.test_helper import path_helper


class GeneratingFilesTestCase(unittest.TestCase):
  """class to do a integration test"""

  def testNormalGenerate(self):
    expected_path = os.path.join(os.path.dirname(__file__),
                                 'expected_files')
    plugin_name = 'the_plugin'
    database_suffix = 'db'
    test_file = os.path.join(path_helper.TestDatabasePath(), 'twitter_ios.db')
    with tempfile.TemporaryDirectory() as tmpdir:
      output_path = os.path.join(tmpdir, "temp")

      file_handler.FileHandler()._CreateFolder(output_path)

      output_console_path = os.path.join(output_path, 'prompts.txt')
      output_handler = output_handler_file.OutputHandlerFile(
          file_path=output_console_path,
          file_handler=file_handler.FileHandler(), confirm=True)

      sqlite_path_helper = sqlite_plugin_path_helper.SQLitePluginPathHelper(
          path=output_path, plugin_name=plugin_name,
          database_suffix=database_suffix)

      plugin_helper = sqlite_plugin_helper.SQLitePluginHelper()
      controller = sqlite_controller.SQLiteController(
          output_handler=output_handler, plugin_helper=plugin_helper)

      query_execution = sqlite_query_execution.SQLQueryExecution(test_file)
      query_execution.tryToConnect()

      query_first = 'select * from users'
      query_data_first = plugin_helper.RunSQLQuery(query_first, query_execution)
      query_model_first = sql_query_model.SQLQueryModel(
          'select id from users', 'Users', query_data_first.columns, True)

      query_second = 'select * from statuses'
      query_data_second = plugin_helper.RunSQLQuery(query_second,
                                                    query_execution)
      query_model_second = sql_query_model.SQLQueryModel(
          'select id from users', 'Statuses', query_data_second.columns, False)

      sql_query = [query_model_first, query_model_second]

      controller._path = output_path
      controller._name = plugin_name
      controller._testfile = test_file
      controller._sql_query = sql_query
      controller._plugin_helper = plugin_helper
      controller._output_handler = output_handler
      controller._query_execution = query_execution

      controller.Generate(path_helper.TemplatePath())

      formatter_init = self._ReadFromFile(
          sqlite_path_helper.formatter_init_file_path)
      formatter = self._ReadFromFile(sqlite_path_helper.formatter_file_path)
      formatter_test = self._ReadFromFile(
          sqlite_path_helper.formatter_test_file_path)
      parser_init = self._ReadFromFile(
          sqlite_path_helper.parser_init_file_path)
      parser = self._ReadFromFile(sqlite_path_helper.parser_file_path)
      parser_test = self._ReadFromFile(sqlite_path_helper.parser_test_file_path)
      console_output = self._ReadFromFile(
          os.path.join(output_path, 'prompts.txt'))

      expected_formatter_init = self._ReadFromFile(os.path.join(
          expected_path, 'formatters_init.py'))
      expected_formatter = self._ReadFromFile(
          os.path.join(expected_path, 'formatters.py'))
      expected_formatter_test = self._ReadFromFile(os.path.join(
          expected_path, 'formatters_test.py'))
      expected_parser_init = self._ReadFromFile(
          os.path.join(expected_path, 'parsers_init.py'))
      expected_parser = self._ReadFromFile(
          os.path.join(expected_path, 'parsers.py'))
      expected_parser_test = self._ReadFromFile(
          os.path.join(expected_path, 'parsers_test.py'))
      expected_console_output = (
        'Do you want to Generate the files?create {0}create {1}create {2}create'
        ' {3}copy {4}create {5}create {6}'.format(
            sqlite_path_helper.formatter_file_path,
            sqlite_path_helper.parser_file_path,
            sqlite_path_helper.formatter_test_file_path,
            sqlite_path_helper.parser_test_file_path,
            sqlite_path_helper.database_path,
            sqlite_path_helper.parser_init_file_path,
            sqlite_path_helper.formatter_init_file_path))

      self.assertEqual(formatter_init, expected_formatter_init)
      self.assertEqual(formatter, expected_formatter)
      self.assertEqual(formatter_test, expected_formatter_test)
      self.assertEqual(parser_init, expected_parser_init)
      self.assertEqual(parser, expected_parser)
      self.assertEqual(parser_test, expected_parser_test)
      self.assertEqual(console_output, expected_console_output)

  def _ReadFromFile(self, path: str):
    """read from file helper"""
    with open(path, 'r') as f:
      return f.read()


if __name__ == '__main__':
  unittest.main()
