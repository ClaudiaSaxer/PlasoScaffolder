# -*- coding: utf-8 -*-
"""test class"""
# pylint: disable=protected-access
# because tests should access protected members
import os
import pathlib
import tempfile
import unittest
from unittest import mock

from plasoscaffolder.common import file_handler
from plasoscaffolder.dal import base_sql_query_execution
from plasoscaffolder.frontend.controller import sqlite_controller
from plasoscaffolder.model import event_model
from plasoscaffolder.model import sql_query_model
from tests.fake import fake_sqlite_plugin_helper
from tests.fake import fake_sqlite_query_execution
from tests.test_helper import output_handler_file
from tests.test_helper import path_helper

class SQLiteControllerTest(unittest.TestCase):
  """Tests the SQLite controller"""

  def testPluginNameIfExisting(self):
    """test method after getting the plugin Name from the user if the plugin
    Name already exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler(), prompt_info='the_plugin',
          prompt_error='the_plugin', )
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          plugin_exists=True, change_bool_after_every_call_plugin_exists=True,
          valid_name=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actualName = 'the_plugin'
      controller._path = 'somepath'
      controller.PluginName(None, None, actualName)
      expected = 'Plugin exists. Choose new Name'
      actual = self._ReadFromFile(path)
      self.assertEqual(expected, actual)

  def testPluginNameIfNotExisting(self):
    """test method after getting tplugin Name from the user if the plugin
    Name is new"""

    output_handler = output_handler_file.OutputHandlerFile(
        'somefile', file_handler.FileHandler())
    plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
        plugin_exists=False)
    controller = sqlite_controller.SQLiteController(output_handler,
                                                    plugin_helper)
    actualName = 'the_plugin'
    controller._path = 'somepath'
    controller.PluginName(None, None, actualName)
    self.assertEqual(actualName, controller._name)

  def testSourcePathIfExisting(self):
    """test method after getting the source path from the user"""

    output_handler = output_handler_file.OutputHandlerFile(
        'somefile', file_handler.FileHandler())
    plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
        folder_exists=True)
    controller = sqlite_controller.SQLiteController(output_handler,
                                                    plugin_helper)
    actualPath = 'testpath'
    controller.SourcePath(None, None, actualPath)
    self.assertEqual(actualPath, controller._path)

  def testCreateSQLQueryModelWithUserInputNoError(self):
    """test method CreateEventModelWithUserInput"""

    fake_execution = fake_sqlite_query_execution.SQLQueryExecution(
        base_sql_query_execution.SQLQueryData(has_error=False)
    )
    sql_query = 'SELECT createdDate FROM Users ORDER BY createdDate'
    name = 'Contact'
    expected_name = 'Parse{0}Row'.format(name)
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler(), prompt_info=name)
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          folder_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actual = controller._CreateSQLQueryModelWithUserInput(sql_query, False,
                                                            fake_execution)
      prompt_output_actual = self._ReadFromFile(path)
      prompt_output_expected = 'What kind of row does the SQL Query parse?'

      expected = sql_query_model.SQLQueryModel(sql_query, expected_name, [])

      self.assertEqual(expected.Name, actual.Name)
      self.assertEqual(expected.Query, actual.Query)
      self.assertEqual(prompt_output_expected, prompt_output_actual)

  def testCreateSQLQueryModelWithUserInputWithError(self):
    """test method CreateEventModelWithUserInput"""
    error_message = "Some Error..."
    fake_execution = fake_sqlite_query_execution.SQLQueryExecution(
        base_sql_query_execution.SQLQueryData(has_error=True,
                                              error_message=error_message)
    )
    sql_query = 'SELECT createdDate FROM Users ORDER BY createdDate'
    name = 'Contact'
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler(), prompt_info=name)
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          folder_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actual = controller._CreateSQLQueryModelWithUserInput(sql_query, False,
                                                            fake_execution)
      self.assertIsNone(actual)

  def testSqlQuery(self):
    """test method after getting the source path from the user"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler(), confirm=False)
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper()
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)

      controller._CreateSQLQueryModelWithUserInput = mock.MagicMock(
          return_value=base_sql_query_execution.SQLQueryData(
              data='test', has_error=False, error_message=None))

      actual = controller.SQLQuery(None, None, True)

      prompt_output_actual = self._ReadFromFile(path)

      prompt_output_expected = ('Please write your SQL script for the '
                                'pluginDo you want to add another Query?')

      self.assertEqual(len(actual), 1)
      self.assertEqual(actual[0].data, 'test')
      self.assertEqual(actual[0].has_error, False)
      self.assertEqual(actual[0].error_message, None)
      self.assertEqual(prompt_output_actual, prompt_output_expected)

  def testSqlQueryMultiple(self):
    """test method after getting the source path from the user"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler(), confirm=True, confirm_amount_same=3)
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper()
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)

      controller._CreateSQLQueryModelWithUserInput = mock.MagicMock(
          return_value=base_sql_query_execution.SQLQueryData(
              data='test', has_error=False, error_message=None))

      actual = controller.SQLQuery(None, None, True)

      prompt_output_expected = ('Please write your SQL script for the '
                                'pluginDo you want to add another Query?') * 3

      prompt_output_actual = self._ReadFromFile(path)
      self.assertEqual(len(actual), 3)
      self.assertEqual(actual[0].data, 'test')
      self.assertEqual(actual[0].has_error, False)
      self.assertEqual(actual[0].error_message, None)
      self.assertEqual(actual[1].data, 'test')
      self.assertEqual(actual[1].has_error, False)
      self.assertEqual(actual[1].error_message, None)
      self.assertEqual(actual[2].data, 'test')
      self.assertEqual(actual[2].has_error, False)
      self.assertEqual(actual[2].error_message, None)
      self.assertEqual(prompt_output_actual, prompt_output_expected)

  def testSourcePathIfNotExisting(self):
    """test method after getting the source path from the user"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler())
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          folder_exists=False, change_bool_after_every_call_folder_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actualPath = 'testpath'
      controller.SourcePath(None, None, actualPath)
      expected = 'Folder does not exists. Enter correct one'
      actual = self._ReadFromFile(path)
      self.assertEqual(expected, actual)

  def testTestPathIfExisting(self):
    """test method after getting the source path from the user"""

    output_handler = output_handler_file.OutputHandlerFile(
        'somefile', file_handler.FileHandler())
    plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
        file_exists=True)
    controller = sqlite_controller.SQLiteController(output_handler,
                                                    plugin_helper)
    actualPath = 'testpath'
    controller.TestPath(None, None, actualPath)
    self.assertEqual(actualPath, controller._testfile)

  def testTestPathIfNotExisting(self):
    """test method after getting the source path from the user"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler())
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          file_exists=False, change_bool_after_every_call_file_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actualPath = 'testpath'
      controller.TestPath(None, None, actualPath)
      expected = 'File does not exists. Choose another.'
      actual = self._ReadFromFile(path)
      self.assertEqual(expected, actual)

  def testEvent(self):
    """test method after getting the events from the user"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler(), confirm=False)
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          folder_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      event = 'event1 event2 event3'
      controller.Event(None, None, event)
      actual = controller._events
      expected = [event_model.EventModel('Event1'),
                  event_model.EventModel('Event2'),
                  event_model.EventModel('Event3')]
      actual_prompt_output = self._ReadFromFile(path)
      expected_prompt_output = ('Does the event Event1 need customizing?'
                                'Does the event Event2 need customizing?'
                                'Does the event Event3 need customizing?')

    self.assertEqual(actual[0].Name, expected[0].Name)
    self.assertEqual(actual[1].Name, expected[1].Name)
    self.assertEqual(actual[2].Name, expected[2].Name)
    self.assertEqual(actual[0].NeedsCustomizing, expected[0].NeedsCustomizing)
    self.assertEqual(actual[1].NeedsCustomizing, expected[1].NeedsCustomizing)
    self.assertEqual(actual[2].NeedsCustomizing, expected[2].NeedsCustomizing)
    self.assertEqual(actual_prompt_output, expected_prompt_output)

  def testCreateEventModelWithUserInputIfTrue(self):
    """test method create event model with user input"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      event_name = 'Event'
      customize = True
      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler(), confirm=customize)
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          folder_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actual = controller._CreateEventModelWithUserInput(event_name)
      prompt_output_actual = self._ReadFromFile(path)
      prompt_output_expected = 'Does the event Event need customizing?'

      expected = event_model.EventModel(event_name, customize)

    self.assertEqual(actual.Name, expected.Name)
    self.assertEqual(actual.NeedsCustomizing, expected.NeedsCustomizing)
    self.assertEqual(prompt_output_actual, prompt_output_expected)

  def testCreateEventModelWithUserInputIfFalse(self):
    """test method create event model with user input"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      event_name = 'Event'
      customize = False
      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler(), confirm=customize)
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          folder_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actual = controller._CreateEventModelWithUserInput(event_name)
      prompt_output_actual = self._ReadFromFile(path)
      prompt_output_expected = 'Does the event Event need customizing?'

      expected = event_model.EventModel(event_name, customize)
    self.assertEqual(actual.Name, expected.Name)
    self.assertEqual(actual.NeedsCustomizing, expected.NeedsCustomizing)
    self.assertEqual(prompt_output_actual, prompt_output_expected)

  def testValidatePluginNameIfOk(self):
    """test the validate plugin Name method if ok"""
    plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
        valid_name=True)
    controller = sqlite_controller.SQLiteController(None, plugin_helper)
    valid_plugin = controller._ValidatePluginName("the_plugin")
    self.assertTrue(valid_plugin)

  def testValidatePluginNameIfNotOk(self):
    """test the validate plugin Name method if not ok"""
    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler())
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          valid_name=False, change_bool_after_every_call_valid_name=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      controller._ValidatePluginName("the_wrong_plugin_")
      expected = ('Plugin is not in a valide format. Choose new Name ['
                  'plugin_name_...]: ')
      actual = self._ReadFromFile(path)
      self.assertEqual(expected, actual)

  def testCreateSQLQueryModelWithUserInput(self):
    """test the creation of the sql Query model with the user input"""
    query = "select x"
    with_examples = True
    query_execution = fake_sqlite_query_execution.SQLQueryExecution(
        base_sql_query_execution.SQLQueryData(
            data=['first', 'second', 'third', 'fourth']))

    with tempfile.TemporaryDirectory() as tmpdir:
      path = os.path.join(tmpdir, 'testfile')
      pathlib.Path(path).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          path, file_handler.FileHandler())
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper()
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      controller._CreateSQLQueryModelWithUserInput(
          query, with_examples, query_execution
      )
      expected = ('Your Query output could look like this.'
                  '[]'
                  'first'
                  'second'
                  'third'
                  'Do you want to add this Query?'
                  'What kind of row does the SQL Query parse?')

      actual = self._ReadFromFile(path)
      self.assertEqual(expected, actual)

  def testGenerateIfConfirmed(self):
    """ test the generate if confirmed"""
    template_path = path_helper.TemplatePath()

    with tempfile.TemporaryDirectory() as tmpdir:
      file = os.path.join(tmpdir, 'testfile')
      pathlib.Path(file).touch()

      fake_execution = fake_sqlite_query_execution.SQLQueryExecution(
          base_sql_query_execution.SQLQueryData(has_error=False, data=[(1, 2)])
      )

      output_handler = output_handler_file.OutputHandlerFile(
          file, file_handler.FileHandler(), confirm=True)
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          valid_name=False, change_bool_after_every_call_valid_name=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)

      controller._path = tmpdir
      controller._name = "the_plugin"
      controller._testfile = file
      controller._events = ['Event1', 'Event2', 'Event3']
      controller._query_execution = fake_execution
      controller.Generate(template_path)
      file1 = os.path.join(tmpdir, 'plaso', 'formatters', 'the_plugin.py')
      file2 = os.path.join(tmpdir, 'plaso', 'parsers', 'sqlite_plugins',
                           'the_plugin.py')
      file3 = os.path.join(tmpdir, 'tests', 'formatters', 'the_plugin.py')
      file4 = os.path.join(tmpdir, 'tests', 'parsers', 'sqlite_plugins',
                           'the_plugin.py')
      file5 = os.path.join(tmpdir, 'test_data', 'the_plugin.')
      file6 = os.path.join(tmpdir, 'plaso', 'parsers', 'sqlite_plugins',
                           '__init__.py')
      file7 = os.path.join(tmpdir, 'plaso', 'formatters', '__init__.py')
      expected = ('Do you want to Generate the files?create {0}create {1}'
                  'create {2}create {3}copy {4}create {5}create {6}'
                  .format(file1, file2, file3, file4, file5, file6, file7))

      actual = self._ReadFromFile(file)
      self.assertEqual(expected, actual)

  def testGenerateIfNotConfirmed(self):
    """test the generate if confirmed """
    template_path = path_helper.TemplatePath()

    with self.assertRaises(SystemExit):
      with tempfile.TemporaryDirectory() as tmpdir:
        file = os.path.join(tmpdir, 'testfile')
        pathlib.Path(file).touch()

        output_handler = output_handler_file.OutputHandlerFile(
            file, file_handler.FileHandler(), confirm=False)

        plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
            valid_name=False,
            change_bool_after_every_call_valid_name=True)
        controller = sqlite_controller.SQLiteController(output_handler,
                                                        plugin_helper)
        controller.Generate('not used')

        self.assertFalse(template_path)

  def _ReadFromFile(self, path: str):
    """Read from file

    Args:
      path (str): the file path

      path (str): the file path

    Returns:
      str: content of the file"""
    with open(path, 'r') as f:
      return f.read()
    os.remove(path)


if __name__ == '__main__':
  unittest.main()
