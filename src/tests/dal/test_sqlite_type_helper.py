# -*- coding: utf-8 -*-
# disable because its to silly for that long sql queries
# pylint: disable=bad-continuation
"""test class"""
import os
import unittest

from plasoscaffolder.dal import sqlite_query_execution, sqlite_type_helper
from plasoscaffolder.model import sql_query_column_model
from tests.test_helper import path_helper


class SQLiteQueryExecutionTest(unittest.TestCase):
  """test the SQLite Query execution test"""

  def setUp(self):
    self.sql_type_helper = sqlite_type_helper.SQLiteTypeHelper(None, None, None)

  def testGetDuplicateColumnNamesIfDistinct(self):
    """test a distinct list"""
    columns = list()
    columns.append(sql_query_column_model.SQLColumnModel('a'))
    columns.append(sql_query_column_model.SQLColumnModel('b'))
    columns.append(sql_query_column_model.SQLColumnModel('c'))
    result = self.sql_type_helper.GetDuplicateColumnNames(columns)
    expected = []
    self.assertEqual(result, expected)

  def testGetDuplicateColumnNamesIfOneDuplicate(self):
    """test a duplicate list with one duplicate"""
    columns = list()
    columns.append(sql_query_column_model.SQLColumnModel('a'))
    columns.append(sql_query_column_model.SQLColumnModel('a'))
    columns.append(sql_query_column_model.SQLColumnModel('b'))
    columns.append(sql_query_column_model.SQLColumnModel('c'))
    result = self.sql_type_helper.GetDuplicateColumnNames(columns)
    expected = ['a']
    self.assertEqual(result, expected)

  def testGetDuplicateColumnNamesIfMultipleDuplicates(self):
    """test a duplicate list with multiple duplicates"""
    columns = list()
    columns.append(sql_query_column_model.SQLColumnModel('a'))
    columns.append(sql_query_column_model.SQLColumnModel('a'))
    columns.append(sql_query_column_model.SQLColumnModel('a'))
    columns.append(sql_query_column_model.SQLColumnModel('b'))
    columns.append(sql_query_column_model.SQLColumnModel('b'))
    columns.append(sql_query_column_model.SQLColumnModel('c'))
    result = self.sql_type_helper.GetDuplicateColumnNames(columns)
    expected = ['a', 'b']
    self.assertEqual(result, expected)


if __name__ == '__main__':
  unittest.main()
