"""test class"""
import os
import pathlib
import tempfile
import unittest

from plasoscaffolder.common import file_handler
from plasoscaffolder.common import output_handler_file
from plasoscaffolder.frontend.controller import sqlite_controller
from tests.fake import fake_sqlite_plugin_helper
from tests.test_helper import path_helper


class SQLiteControllerTest(unittest.TestCase):
  """Tests the SQLite controller"""

  def testPluginNameIfExisting(self):
    """test method after getting the plugin name from the user if the plugin
    name already exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
      file = os.path.join(tmpdir, 'testfile')
      pathlib.Path(file).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          file, file_handler.FileHandler(), prompt_info='the_plugin',
          prompt_error='the_plugin', )
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          plugin_exists=True, change_bool_after_every_call_plugin_exists=True,
          valid_name=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actualName = 'the_plugin'
      controller._path = 'somepath'
      controller.PluginName(None, None, actualName)
      expected = 'Plugin exists. Choose new name: '
      actual = self._ReadFromFile(file)
      self.assertEqual(expected, actual)
      os.remove(file)

  def testPluginNameIfNotExisting(self):
    """test method after getting tplugin name from the user if the plugin
    name is new"""

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

  def testSourcePathIfNotExisting(self):
    """test method after getting the source path from the user"""
    with tempfile.TemporaryDirectory() as tmpdir:
      file = os.path.join(tmpdir, 'testfile')
      pathlib.Path(file).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          file, file_handler.FileHandler())
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          folder_exists=False, change_bool_after_every_call_folder_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actualPath = 'testpath'
      controller.SourcePath(None, None, actualPath)
      expected = 'Folder does not exists. Enter correct one: '
      actual = self._ReadFromFile(file)
      self.assertEqual(expected, actual)
      os.remove(file)

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
      file = os.path.join(tmpdir, 'testfile')
      pathlib.Path(file).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          file, file_handler.FileHandler())
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          file_exists=False, change_bool_after_every_call_file_exists=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actualPath = 'testpath'
      controller.TestPath(None, None, actualPath)
      expected = 'File does not exists. Choose another: '
      actual = self._ReadFromFile(file)
      self.assertEqual(expected, actual)
      os.remove(file)

  def testEvent(self):
    """test method after getting the events from the user"""

    output_handler = output_handler_file.OutputHandlerFile(
        'somefile', file_handler.FileHandler())
    plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
        folder_exists=True)
    controller = sqlite_controller.SQLiteController(output_handler,
                                                    plugin_helper)
    event = 'event1 event2 event3'
    controller.Event(None, None, event)
    actual = controller._events
    expected = ['Event1', 'Event2', 'Event3']
    self.assertEqual(actual, expected)

  def testValidatePluginNameIfOk(self):
    """test the validate plugin name method if ok"""
    plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
        valid_name=True)
    controller = sqlite_controller.SQLiteController(None, plugin_helper)
    valid_plugin = controller._ValidatePluginName("the_plugin")
    self.assertTrue(valid_plugin)

  def testValidatePluginNameIfNotOk(self):
    """test the validate plugin name method if not ok"""
    with tempfile.TemporaryDirectory() as tmpdir:
      file = os.path.join(tmpdir, 'testfile')
      pathlib.Path(file).touch()

      output_handler = output_handler_file.OutputHandlerFile(
          file, file_handler.FileHandler())
      plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
          valid_name=False, change_bool_after_every_call_valid_name=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      controller._ValidatePluginName("the_wrong_plugin_")
      expected = 'Plugin is not in a valide format. Choose new name [' \
                 'plugin_name_...]: '
      actual = self._ReadFromFile(file)
      self.assertEqual(expected, actual)
      os.remove(file)

  def testGenerateIfConfirmed(self):
    """test the generate if confirmed"""
    template_path = path_helper.TemplatePath()

    with tempfile.TemporaryDirectory() as tmpdir:
      file = os.path.join(tmpdir, 'testfile')
      pathlib.Path(file).touch()

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
      controller.Generate(template_path)
      expected = (
        'Do you want to Generate the files?'
        'create ' + os.path.join(tmpdir, 'plaso', 'formatters',
                                 'the_plugin.py') +
        'create ' + os.path.join(tmpdir, 'plaso', 'parsers', 'sqlite_plugins',
                                 'the_plugin.py') +
        'create ' + os.path.join(tmpdir, 'tests', 'formatters',
                                 'the_plugin.py') +
        'create ' + os.path.join(tmpdir, 'tests', 'parsers', 'sqlite_plugins',
                                 'the_plugin.py') +
        'copy ' + os.path.join(tmpdir, 'test_data', 'the_plugin.') +
        'create ' + os.path.join(tmpdir, 'plaso', 'parsers', 'sqlite_plugins',
                                 '__init__.py') +
        'create ' + os.path.join(tmpdir, 'plaso', 'formatters', '__init__.py'))

      actual = self._ReadFromFile(file)
      os.remove(file)

    self.assertEqual(expected, actual)

  def testGenerateIfNotConfirmed(self):
    """test the generate if confirmed"""
    template_path = path_helper.TemplatePath()

    with self.assertRaises(SystemExit):
      with tempfile.TemporaryDirectory() as tmpdir:
        file = os.path.join(tmpdir, 'testfile')
        pathlib.Path(file).touch()

        output_handler = output_handler_file.OutputHandlerFile(
            file, file_handler.FileHandler(), confirm=False)

        plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
            valid_name=False, change_bool_after_every_call_valid_name=True)
        controller = sqlite_controller.SQLiteController(output_handler,
                                                        plugin_helper)
        controller.Generate('not used')

        self.output.Confirm(template_path)

  def _ReadFromFile(self, path: str):
    """read from file helper"""
    with open(path, 'r') as f:
      return f.read()

  if __name__ == '__main__':
    unittest.main()
