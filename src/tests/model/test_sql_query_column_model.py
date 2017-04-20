# -*- coding: utf-8 -*-
"""test class"""
import unittest

from plasoscaffolder.model import sql_query_column_model


class SQLColumnModelTest(unittest.TestCase):
  """test class for SQLColumnModel"""

  def testColumnAsSnakeCaseLongNameCamelCase(self):
    column = sql_query_column_model.SQLColumnModel('theOneLongColumnName')
    actual = column.ColumnAsSnakeCase()
    expected = 'the_one_long_column_name'
    self.assertEqual(actual, expected)

  def testColumnAsSnakeCaseLongNamePascalCase(self):
    column = sql_query_column_model.SQLColumnModel('TheOneLongColumnName')
    actual = column.ColumnAsSnakeCase()
    expected = 'the_one_long_column_name'
    self.assertEqual(actual, expected)

  def testColumnAsSnakeCaseShortName(self):
    column = sql_query_column_model.SQLColumnModel('short')
    actual = column.ColumnAsSnakeCase()
    expected = 'short'
    self.assertEqual(actual, expected)

  def testColumnAsDescriptionLongNameCamelCase(self):
    column = sql_query_column_model.SQLColumnModel('theOneLongColumnName')
    actual = column.ColumnAsDescription()
    expected = 'The One Long Column Name'
    self.assertEqual(actual, expected)

  def testColumnAsDescriptionLongNamePascalCase(self):
    column = sql_query_column_model.SQLColumnModel('TheOneLongColumnName')
    actual = column.ColumnAsDescription()
    expected = 'The One Long Column Name'
    self.assertEqual(actual, expected)

  def testColumnAsSnakeCaseShortName(self):
    column = sql_query_column_model.SQLColumnModel('short')
    actual = column.ColumnAsDescription()
    expected = 'Short'
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()
