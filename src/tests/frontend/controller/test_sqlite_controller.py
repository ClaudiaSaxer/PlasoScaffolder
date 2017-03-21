"""test class"""
import os
import pathlib
import tempfile
import unittest

from plasoscaffolder.common import file_handler
from plasoscaffolder.common import output_handler_file
from plasoscaffolder.frontend.controller import sqlite_controller
from tests.fake import fake_sqlite_plugin_helper


class SQLiteControllerTest(unittest.TestCase):
  """Tests the sqlite controller"""

  def testPluginNameIfNotExisting(self):
    """test method after getting the source path from the user"""

    output_handler = output_handler_file.OutputHandlerFile(
        'somefile', file_handler.FileHandler())
    plugin_helper = fake_sqlite_plugin_helper.FakeSQLitePluginHelper(
        file_exists=False)
    controller = sqlite_controller.SQLiteController(output_handler,
                                                    plugin_helper)
    actualName = 'the_plugin'
    controller._path= 'somepath'
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
          folder_exists=False, change_bool_after_every_call=True)
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
          file_exists=False, change_bool_after_every_call=True)
      controller = sqlite_controller.SQLiteController(output_handler,
                                                      plugin_helper)
      actualPath = 'testpath'
      controller.TestPath(None, None, actualPath)
      expected = 'File does not exists. Choose another: '
      actual = self._ReadFromFile(file)
      self.assertEqual(expected, actual)
      os.remove(file)

  def _ReadFromFile(self, path: str):
    """read from file helper"""
    with open(path, 'r') as f:
      return f.read()



if __name__ == '__main__':
  unittest.main()
