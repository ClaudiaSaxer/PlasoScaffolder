# -*- coding: utf-8 -*-
"""test class"""
import os
import unittest

from plasoscaffolder.dal import sqlite_query_execution
from tests.test_helper import path_helper


class SQLiteQueryExecutionTest(unittest.TestCase):
  """test the SQLite query execution test"""

  def setUp(self):
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'twitter_ios.db')
    self.execute = sqlite_query_execution.SQLQueryExecution(file_path)

  def testRollbackWorks(self):
    """testing if the rollback works"""
    query_select_all_users = 'SELECT * FROM Users'
    query_drop_table = 'DROP TABLE Users'
    result_users_before = self.execute.executeQuery(query_select_all_users)
    result_drop_table = self.execute.executeQuery(query_drop_table)
    result_users_after = self.execute.executeQuery(query_select_all_users)

    self.assertEqual(len(result_users_before.data),
                     len(result_users_after.data))
    self.assertTrue(len(result_users_after.data) is 25)
    self.assertTrue(len(result_users_before.data) is 25)
    self.assertFalse(result_drop_table.has_error)
    self.assertIsNone(result_drop_table.error_message)

  def testMultipleTestAfterOneAnother(self):
    """test two querys after another to test the connection is still open"""
    query_simple = (
      'SELECT createdDate, updatedAt, screenName, name, profileImageUrl,'
      'location, description, url, following, followersCount, '
      'followingCount'
      ' FROM Users ORDER BY createdDate')
    result_simple = self.execute.executeQuery(query_simple)

    query_join = ('SELECT Statuses.date AS date, Statuses.text AS text,'
                  ' Statuses.userId AS user_id, Users.name AS name, '
                  'Statuses.retweetCount AS '
                  'retweetCount, Statuses.favoriteCount AS favoriteCount, '
                  'Statuses.favorited AS favorited, Statuses.updatedAt AS '
                  'updatedAt '
                  'FROM Statuses LEFT join Users ON Statuses.userId = Users.id '
                  'ORDER BY date')
    result_join = self.execute.executeQuery(query_join)

    self.assertIsNone(result_join.error_message)
    self.assertIsNone(result_simple.error_message)
    self.assertFalse(result_simple.has_error)
    self.assertFalse(result_join.has_error)
    self.assertEqual(len(result_join.data), 67)
    self.assertEqual(len(result_simple.data), 25)

  def testQueryErrorNoSuchColumn(self):
    """test two querys after another to test the connection is still open"""
    query = 'SELECT createdDates FROM Users'
    result = self.execute.executeQuery(query)
    expected_error = 'no such column: createdDates'
    self.assertTrue(result.has_error)
    self.assertIsNone(result.data)
    self.assertEqual(str(result.error_message), expected_error)

  def testQueryErrorNoSuchTable(self):
    """test two querys after another to test the connection is still open"""
    query = 'SELECT createdDate FROM Userss'
    result = self.execute.executeQuery(query)
    expected_error = 'no such table: Userss'
    self.assertTrue(result.has_error)
    self.assertIsNone(result.data)
    self.assertEqual(str(result.error_message), expected_error)

  def testExecuteQuerySimple(self):
    """test the execution of a simple query"""
    query = ('SELECT createdDate, updatedAt, screenName, name, profileImageUrl,'
             'location, description, url, following, followersCount, '
             'followingCount'
             ' FROM Users ORDER BY createdDate')
    result = self.execute.executeQuery(query)
    expected_data = self._ReadFromFileRelative('expected_simple_query_data')
    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, str(result.data))

  def testExecuteQueryWithJoin(self):
    """test the execution of a more complex query"""
    query = ('SELECT Statuses.date AS date, Statuses.text AS text,'
             ' Statuses.userId AS user_id, Users.name AS name, '
             'Statuses.retweetCount AS '
             'retweetCount, Statuses.favoriteCount AS favoriteCount, '
             'Statuses.favorited AS favorited, Statuses.updatedAt AS updatedAt '
             'FROM Statuses LEFT join Users ON Statuses.userId = Users.id '
             'ORDER BY date')
    result = self.execute.executeQuery(query)
    expected_data = self._ReadFromFileRelative('expected_join_query_data')
    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, str(result.data))

  def _ReadFromFileRelative(self, path: str):
    """Read from file with relative path

    Args:
      path (str): the relative file path 

    Returns:
      str: content of the file"""
    current_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(current_dir, path)

    with open(abs_file_path, 'r', encoding='utf-8') as f:
      return f.read()




if __name__ == '__main__':
  unittest.main()
