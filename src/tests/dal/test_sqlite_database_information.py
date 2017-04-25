# -*- coding: utf-8 -*-
# disable because its to silly for that long sql queries
# pylint: disable=bad-continuation
"""test class"""
import os
import unittest

from plasoscaffolder.dal import sqlite_database_information
from plasoscaffolder.dal import sqlite_query_execution
from tests.test_helper import path_helper


class SQLiteDatabaseInformationTest(unittest.TestCase):
  """test the SQLite Query execution test"""

  def testGetRequiredTables(self):
    """get the required tables if nothing went wrong"""

    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'twitter_ios.db')
    execute = sqlite_query_execution.SQLQueryExecution(file_path)
    connected = execute.tryToConnect()
    database_information = (
      sqlite_database_information.SQLiteDatabaseInformation(execute))

    result = database_information.getTablesFromDatabase()
    self.assertEqual(len(result), 7)
    self.assertTrue(connected)
    self.assertEqual(result[0], 'Lists')
    self.assertEqual(result[1], 'ListsShadow')
    self.assertEqual(result[2], 'MyRetweets')
    self.assertEqual(result[3], 'Statuses')
    self.assertEqual(result[4], 'StatusesShadow')
    self.assertEqual(result[5], 'Users')
    self.assertEqual(result[6], 'UsersShadow')

  def testGetRequiredTablesWithError(self):
    """get the required tables if anything went wrong"""
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'twitter_ios_error.db')
    execute = sqlite_query_execution.SQLQueryExecution(file_path)
    connected = execute.tryToConnect()
    database_information = (
      sqlite_database_information.SQLiteDatabaseInformation(execute))
    result = database_information.getTablesFromDatabase()

    self.assertEqual(result, [])
    self.assertFalse(connected)

  def testGetTableColumnsAndType(self):
    """get the required tables if anything went wrong"""
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'test_database_types.db')
    execute = sqlite_query_execution.SQLQueryExecution(file_path)
    connected = execute.tryToConnect()
    database_information = (
      sqlite_database_information.SQLiteDatabaseInformation(execute))
    actual_data = database_information.getTableColumnsAndType('nodata')
    expected_data = {'intval': 'int',
                     'integerval': 'integer',
                     'tinyintval': 'tinyint',
                     'smallintval': 'smallint',
                     'mediuintval': 'mediumint',
                     'bigintval': 'bigint',
                     'unsignedbigintval': 'unsigned big int',
                     'int2val': 'int2',
                     'int8val': 'int8',
                     'characterval': 'character(20)',
                     'varcharval': 'varchar(255)',
                     'varyingcharacterval': 'varying character(255)',
                     'ncharval': 'nchar(55)',
                     'nativecharacterval': 'native character(70)',
                     'nvarcharval': 'nvarchar(100)',
                     'textval': 'text',
                     'clobval': 'clob',
                     'blobval': 'blob',
                     'realval': 'real',
                     'doubleval': 'double',
                     'doubleprecisionval': 'double precision',
                     'floatval': 'float',
                     'numericval': 'numeric',
                     'decimalval': 'decimal(10,5)',
                     'booleanval': 'boolean',
                     'dateval': 'date',
                     'datetimeval': 'datetime'}
    self.assertEqual(len(actual_data), 27)
    self.assertEqual(actual_data, expected_data)
    self.assertTrue(connected)

  def testGetTableColumnsAndTypeWithError(self):
    """get the required tables if anything went wrong"""
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'test_database_types.db')
    execute = sqlite_query_execution.SQLQueryExecution(file_path)
    connected = execute.tryToConnect()
    database_information = (
      sqlite_database_information.SQLiteDatabaseInformation(execute))
    actual_data = database_information.getTableColumnsAndType('thisisnot')
    expected_data = {}
    self.assertEqual(len(actual_data), 0)
    self.assertEqual(actual_data, expected_data)
    self.assertTrue(connected)


if __name__ == '__main__':
  unittest.main()
