# -*- coding: utf-8 -*-
"""Test class"""
import os
import tempfile
import unittest

from plasoscaffolder.bll.services import sqlite_plugin_helper
from plasoscaffolder.dal import base_sql_query_execution
from plasoscaffolder.model import sql_query_column_model
from plasoscaffolder.model import sql_query_model
from tests.fake import (fake_sqlite_plugin_path_helper,
                        fake_sqlite_query_execution)
from tests.test_helper import path_helper


class SQLitePluginHelperTest(unittest.TestCase):
  """  Class representing a test case testing the SQLite plugin helper"""

  def setUp(self):
    self.helper = sqlite_plugin_helper.SQLitePluginHelper()
    self.template_path = path_helper.TemplatePath()

  def test_PluginExistsIfFalse(self):
    """Tests the plugin exists method if none exists."""

    actual = self.helper.PluginExists(
        'temp', 'plugin_test', 'db',
        fake_sqlite_plugin_path_helper.FakeSQLitePluginPathHelper(
            self.template_path, 'test', 'db'))
    self.assertFalse(actual)

  def test_PluginExistsIfTrue(self):
    """Tests the plugin exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
      file_path = os.path.join(tmpdir, 'test')
      new_file = open(file_path, 'a')
      helper = sqlite_plugin_helper.SQLitePluginHelper()
      actual = helper.PluginExists(
          tmpdir, new_file.name, 'db',
          fake_sqlite_plugin_path_helper.FakeSQLitePluginPathHelper(
              self.template_path, new_file.name, 'db'))
      new_file.close()
      os.remove(file_path)

    self.assertTrue(actual)

  def test_FileExistsIfTrue(self):
    """ test the method that checks if the file exists """

    with tempfile.TemporaryDirectory() as tmpdir:
      with tempfile.TemporaryFile(dir=tmpdir) as fp:
        helper = sqlite_plugin_helper.SQLitePluginHelper()
        actual = helper.FileExists(fp.name)

    self.assertTrue(actual)

  def testFolderExistsIfTrue(self):
    """test the method that checks if folder exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
      helper = sqlite_plugin_helper.SQLitePluginHelper()
      actual = helper.FolderExists(tmpdir)

    self.assertTrue(actual)

  def testRunSQLQuery(self):
    """test run sql query"""
    data = base_sql_query_execution.SQLQueryData(
        columns=[], data=[], has_error=False, error_message=None)
    executor = fake_sqlite_query_execution.SQLQueryExecution(data)
    helper = sqlite_plugin_helper.SQLitePluginHelper()
    actual = helper.RunSQLQuery('my query', executor)
    self.assertFalse(actual.has_error)
    self.assertIsNone(actual.error_message)
    self.assertEqual(actual.columns, [])
    self.assertEqual(actual.data, [])

  def testIsValidPluginNameExpected(self):
    """tests the plugin Name validation."""
    helper = sqlite_plugin_helper.SQLitePluginHelper()
    plugin_name = "this_is_a_test"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertTrue(actual)

  def testIsValidPluginNameWithEndingUnderscore(self):
    """tests the plugin Name validation."""
    helper = sqlite_plugin_helper.SQLitePluginHelper()
    plugin_name = "this_is_a_"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertFalse(actual)

  def testIsValidPluginNameOnlyOneWordLowercase(self):
    """tests the plugin Name validation."""
    helper = sqlite_plugin_helper.SQLitePluginHelper()
    plugin_name = "this"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertTrue(actual)

  def testIsValidPluginNameOneWordUppercase(self):
    """tests the plugin Name validation."""
    helper = sqlite_plugin_helper.SQLitePluginHelper()
    plugin_name = "This"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertFalse(actual)

  def testIsValidPluginNameWithNumber(self):
    """tests the plugin Name validation."""
    helper = sqlite_plugin_helper.SQLitePluginHelper()
    plugin_name = "this3"
    actual = helper.IsValidPluginName(plugin_name)
    self.assertFalse(actual)

  def testGetDistinctColumnsFromSQLQueryData(self):
    """test the creating of a distinct list of all attributes of the queries"""
    helper = sqlite_plugin_helper.SQLitePluginHelper()
    queries = list()
    column1 = sql_query_model.SQLQueryModel(
        columns=[sql_query_column_model.SQLColumnModel('createdDate'),
                 sql_query_column_model.SQLColumnModel('updatedAt'),
                 sql_query_column_model.SQLColumnModel('screenName')],
        query="", name="", needs_customizing=False)
    column2 = sql_query_model.SQLQueryModel(
        columns=[sql_query_column_model.SQLColumnModel('profileImageUrl'),
                 sql_query_column_model.SQLColumnModel('screenName'),
                 sql_query_column_model.SQLColumnModel('userId')],
        query="", name="", needs_customizing=False)
    column3 = sql_query_model.SQLQueryModel(
        columns=[sql_query_column_model.SQLColumnModel('screenName'),
                 sql_query_column_model.SQLColumnModel('createdDate'),
                 sql_query_column_model.SQLColumnModel('createdDate')],
        query="", name="", needs_customizing=False)
    column4 = sql_query_model.SQLQueryModel(
        columns=[sql_query_column_model.SQLColumnModel('screenNameSecond'),
                 sql_query_column_model.SQLColumnModel('createdDate')],
        query="", name="", needs_customizing=False)
    queries.append(column1)
    queries.append(column2)
    queries.append(column3)
    queries.append(column4)
    actual = helper.GetDistinctColumnsFromSQLQueryData(queries)
    expected = ['created_date', 'profile_image_url', 'screen_name',
                'screen_name_second', 'updated_at', 'user_id']

    self.assertEqual(actual, expected)

  def testGetDistinctColumnsFromSQLQueryDataEmpty(self):
    """test the creating of a distinct list of all attributes of the queries
    with an empty array"""
    helper = sqlite_plugin_helper.SQLitePluginHelper()
    queries = list()
    column1 = sql_query_model.SQLQueryModel(
        columns=[], query="", name="", needs_customizing=False)
    column2 = sql_query_model.SQLQueryModel(
        columns=[sql_query_column_model.SQLColumnModel('first')],
        query="", name="", needs_customizing=False)
    queries.append(column1)
    queries.append(column2)
    actual = helper.GetDistinctColumnsFromSQLQueryData(queries)
    expected = ['first']
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  unittest.main()
