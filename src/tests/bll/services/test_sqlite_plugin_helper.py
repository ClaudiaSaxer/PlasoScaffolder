# -*- coding: utf-8 -*-
import unittest
import tempfile
from plasoscaffolder.bll.services.sqlite_plugin_helper import *
from tests.fake.fake_sqlite_plugin_path_helper import FakeSQLitePluginPathHelper


class SQLitePluginHelperTest(unittest.TestCase):
  """  Class representing a test case testing the SQLite plugin helper"""

  def setUp(self):
    self.helper = SQLitePluginHelper()

  def test_plugin_exists_false(self):
    """Tests the plugin exists method if none exists."""

    actual = self.helper.plugin_exists('temp', 'plugin_test', FakeSQLitePluginPathHelper)
    self.assertFalse(actual)

  def test_plugin_exists_true(self):
    """Tests the plugin exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
      file_path = os.path.join(tmpdir,'test')
      new_file = open(file_path,'a')
      helper = SQLitePluginHelper()
      actual = helper.plugin_exists(tmpdir, new_file.name, FakeSQLitePluginPathHelper)
      new_file.close()
      os.remove(file_path)


    self.assertTrue(actual)

  def test_file_exists(self):
    """ test the method that checks if the file exists """

    with tempfile.TemporaryDirectory() as tmpdir:
      with tempfile.TemporaryFile(dir=tmpdir) as fp:
        helper = SQLitePluginHelper()
        actual = helper.file_exists(fp.name)

    self.assertTrue(actual)

  def test_folder_exists(self):
    """test the method that checks if folder exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
      helper = SQLitePluginHelper()
      actual = helper.folder_exists(tmpdir)

    self.assertTrue(actual)

  def test_validate_plugin_name_1(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "this_is_a_test"
    actual = helper.valide_plugin_name(plugin_name)
    self.assertTrue(actual)

  def test_validate_plugin_name_2(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "this_is_a_"
    actual = helper.valide_plugin_name(plugin_name)
    self.assertFalse(actual)

  def test_validate_plugin_name_3(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "this"
    actual = helper.valide_plugin_name(plugin_name)
    self.assertTrue(actual)

  def test_validate_plugin_name_4(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "This"
    actual = helper.valide_plugin_name(plugin_name)
    self.assertFalse(actual)

  def test_validate_plugin_name_5(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "this3"
    actual = helper.valide_plugin_name(plugin_name)
    self.assertFalse(actual)

if __name__ == '__main__':
  unittest.main()
