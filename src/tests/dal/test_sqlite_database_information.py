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

  def setUp(self):
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'twitter_ios.db')
    execute = sqlite_query_execution.SQLQueryExecution(file_path)
    self.database_information = \
      sqlite_database_information.SQLiteDatabaseInformation(
      execute)

  def testGetRequiredTables(self):
    """get the required tables if anything went wrong"""

    result = self.database_information.getTablesFromDatabase()
    self.assertTrue(len(result) == 7)
    self.assertEqual(result[0], 'Lists')
    self.assertEqual(result[1], 'ListsShadow')
    self.assertEqual(result[2], 'MyRetweets')
    self.assertEqual(result[3], 'Statuses')
    self.assertEqual(result[4], 'StatusesShadow')
    self.assertEqual(result[5], 'Users')
    self.assertEqual(result[6], 'UsersShadow')



if __name__ == '__main__':
  unittest.main()
