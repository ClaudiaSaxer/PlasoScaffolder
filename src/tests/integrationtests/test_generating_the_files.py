"""the integration tests"""
import filecmp
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

      formatter_init_path = sqlite_path_helper.formatter_init_file_path
      formatter_path = sqlite_path_helper.formatter_file_path
      formatter_test_path = sqlite_path_helper.formatter_test_file_path
      parser_init_path = sqlite_path_helper.parser_init_file_path
      parser_path = sqlite_path_helper.parser_file_path
      parser_test_path = sqlite_path_helper.parser_test_file_path
      database_path = sqlite_path_helper.database_path
      console_output_path = os.path.join(output_path, 'prompts.txt')

      expected_formatter_init_path = os.path.join(
          expected_path, 'formatters_init.py')
      expected_formatter_path = os.path.join(expected_path, 'formatters.py')
      expected_formatter_test_path = os.path.join(
          expected_path, 'formatters_test.py')
      expected_parser_init_path = os.path.join(expected_path, 'parsers_init.py')
      expected_parser_path = os.path.join(expected_path, 'parsers.py')
      expected_parser_test_path = os.path.join(expected_path, 'parsers_test.py')
      expected_database_path = os.path.join(expected_path, 'test_file.db')
      expected_console_output = (
        'Do you want to Generate the files?create {0}create {1}create {2}create'
        ' {3}copy {4}create {5}create {6}'.format(
            formatter_path, parser_path, formatter_test_path, parser_test_path,
            database_path, parser_init_path, formatter_init_path))

      self.assertTrue(
          filecmp.cmp(formatter_init_path, expected_formatter_init_path))
      self.assertTrue(filecmp.cmp(formatter_path, expected_formatter_path))
      self.assertTrue(
          filecmp.cmp(formatter_test_path, expected_formatter_test_path))
      self.assertTrue(filecmp.cmp(parser_init_path, expected_parser_init_path))
      self.assertTrue(filecmp.cmp(parser_path, expected_parser_path))
      self.assertTrue(filecmp.cmp(parser_test_path, expected_parser_test_path))
      self.assertTrue(filecmp.cmp(database_path, expected_database_path))
      self.assertEqual(self._ReadFromFile(console_output_path),
                       expected_console_output)

  def _ReadFromFile(self, path: str):
    """read from file helper"""
    with open(path, 'r') as f:
      return f.read()


if __name__ == '__main__':
  unittest.main()
