# -*- coding: utf-8 -*-
"""Test class"""
import os
import tempfile
import unittest

from plasoscaffolder.bll.services.sqlite_plugin_helper import SQLitePluginHelper
from tests.fake.fake_sqlite_plugin_path_helper import FakeSQLitePluginPathHelper


class SQLitePluginHelperTest(unittest.TestCase):
  """  Class representing a test case testing the SQLite plugin helper"""

  def setUp(self):
    self.helper = SQLitePluginHelper()

  def test_PluginExistsIfFalse(self):
    """Tests the plugin exists method if none exists."""

    actual = self.helper.PluginExists('temp', 'plugin_test',
                                       FakeSQLitePluginPathHelper)
    self.assertFalse(actual)

  def test_PluginExistsIfTrue(self):
    """Tests the plugin exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
      file_path = os.path.join(tmpdir, 'test')
      new_file = open(file_path, 'a')
      helper = SQLitePluginHelper()
      actual = helper.PluginExists(tmpdir, new_file.name,
                                    FakeSQLitePluginPathHelper)
      new_file.close()
      os.remove(file_path)

    self.assertTrue(actual)

  def test_FileExistsIfTrue(self):
    """ test the method that checks if the file exists """

    with tempfile.TemporaryDirectory() as tmpdir:
      with tempfile.TemporaryFile(dir=tmpdir) as fp:
        helper = SQLitePluginHelper()
        actual = helper.FileExists(fp.name)

    self.assertTrue(actual)

  def testFolderExistsIfTrue(self):
    """test the method that checks if folder exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
      helper = SQLitePluginHelper()
      actual = helper.FolderExists(tmpdir)

    self.assertTrue(actual)

  def testIsValidPluginNameExpected(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "this_is_a_test"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertTrue(actual)

  def testIsValidPluginNameWithEndingUnderscore(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "this_is_a_"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertFalse(actual)

  def testIsValidPluginNameOnlyOneWordLowercase(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "this"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertTrue(actual)

  def testIsValidPluginNameOneWordUppercase(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "This"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertFalse(actual)

  def testIsValidPluginNameWithNumber(self):
    """tests the plugin name validation."""
    helper = SQLitePluginHelper()
    plugin_name = "this3"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertFalse(actual)


if __name__ == '__main__':
  unittest.main()
