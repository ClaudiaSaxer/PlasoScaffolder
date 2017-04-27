# -*- coding: utf-8 -*-
# disable because its to silly for that long sql queries
# pylint: disable=bad-continuation
"""test class"""
import os
import unittest

from plasoscaffolder.dal import sqlite_query_execution
from tests.test_helper import path_helper


class SQLiteQueryExecutionTest(unittest.TestCase):
  """test the SQLite Query execution test"""

  def setUp(self):
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'twitter_ios.db')
    self.execute = sqlite_query_execution.SQLQueryExecution(file_path)
    self.execute.tryToConnect()

    file_path_types = os.path.join(database_path, 'test_database_types.db')
    self.execute_types = sqlite_query_execution.SQLQueryExecution(
        file_path_types)
    self.execute_types.tryToConnect()

    file_path_names = os.path.join(database_path, 'test_database_names.db')
    self.execute_names = sqlite_query_execution.SQLQueryExecution(
        file_path_names)
    self.execute_names.tryToConnect()

  def testTryToConnect(self):
    """try to connect without error"""
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'twitter_ios.db')
    execute = sqlite_query_execution.SQLQueryExecution(file_path)
    connected = execute.tryToConnect()
    self.assertTrue(connected)

  def testTryToConnectWithError(self):
    """try to connect 2 times resulting in a error"""
    database_path = path_helper.TestDatabasePath()
    file_path = os.path.join(database_path, 'twitter_ios_error.db')
    execute = sqlite_query_execution.SQLQueryExecution(file_path)
    connected = execute.tryToConnect()
    self.assertFalse(connected)

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
    query_simple = ('SELECT createdDate, updatedAt, screenName, '
                    'Name, profileImageUrl,'
                    'location, description, url, following, followersCount, '
                    'followingCount'
                    ' FROM Users ORDER BY createdDate')
    result_simple = self.execute.executeQuery(query_simple)

    query_join = ('SELECT Statuses.date AS date, Statuses.text AS text,'
                  ' Statuses.userId AS user_id, Users.Name AS Name, '
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
    expected_error = 'Error: no such column: createdDates'
    self.assertTrue(result.has_error)
    self.assertIsNone(result.data)
    self.assertEqual(str(result.error_message), expected_error)

  def testQueryErrorNoSuchTable(self):
    """test two querys after another to test the connection is still open"""
    query = 'SELECT createdDate FROM Userss'
    result = self.execute.executeQuery(query)
    expected_error = 'Error: no such table: Userss'
    self.assertTrue(result.has_error)
    self.assertIsNone(result.data)
    self.assertEqual(str(result.error_message), expected_error)

  def testQueryWarning(self):
    """test two querys after another to test the connection is still open"""
    query = 'SELECT id from users;Select id from users'
    result = self.execute.executeQuery(query)
    expected_error = 'Warning: You can only execute one statement at a time.'
    self.assertTrue(result.has_error)
    self.assertIsNone(result.data)
    self.assertEqual(str(result.error_message), expected_error)

  def testExecuteQueryDetailedSimple(self):
    """test the execution of a simple Query"""
    query = ('SELECT createdDate, updatedAt, screenName, Name, profileImageUrl,'
             'location, description, url, following, followersCount, '
             'followingCount'
             ' FROM Users ORDER BY createdDate')
    result = self.execute.executeQueryDetailed(query)
    expected_data = self._ReadFromFileRelative('expected_simple_query_data')
    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, str(result.data))

    self.assertEqual(result.columns[0].SQLColumn, 'createdDate')
    self.assertEqual(result.columns[1].SQLColumn, 'updatedAt')
    self.assertEqual(result.columns[2].SQLColumn, 'screenName')
    self.assertEqual(result.columns[3].SQLColumn, 'name')
    self.assertEqual(result.columns[4].SQLColumn, 'profileImageUrl')
    self.assertEqual(result.columns[5].SQLColumn, 'location')
    self.assertEqual(result.columns[6].SQLColumn, 'description')
    self.assertEqual(result.columns[7].SQLColumn, 'url')
    self.assertEqual(result.columns[8].SQLColumn, 'following')
    self.assertEqual(result.columns[9].SQLColumn, 'followersCount')
    self.assertEqual(result.columns[10].SQLColumn, 'followingCount')
    self.assertEqual(result.columns[0].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[1].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[2].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[3].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[4].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[5].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[6].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[7].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[8].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[9].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[10].ColumnTypeAsName(), 'int')

  def testExecuteQueryDetailedWithJoin(self):
    """test the execution of a more complex Query"""
    query = (
      'SELECT Statuses.date AS date, Statuses.text AS text,'
      ' Statuses.userId AS user_id, Users.Name AS Name, '
      'Statuses.retweetCount AS '
      'retweetCount, Statuses.favoriteCount AS favoriteCount, '
      'Statuses.favorited AS favorited, Statuses.updatedAt AS updatedAt '
      'FROM Statuses LEFT join Users ON Statuses.userId = Users.id '
      'ORDER BY date')
    result = self.execute.executeQueryDetailed(query)
    expected_data = self._ReadFromFileRelative('expected_join_query_data')
    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, str(result.data))

    self.assertEqual(result.columns[0].SQLColumn, 'date')
    self.assertEqual(result.columns[1].SQLColumn, 'text')
    self.assertEqual(result.columns[2].SQLColumn, 'user_id')
    self.assertEqual(result.columns[3].SQLColumn, 'Name')
    self.assertEqual(result.columns[4].SQLColumn, 'retweetCount')
    self.assertEqual(result.columns[5].SQLColumn, 'favoriteCount')
    self.assertEqual(result.columns[6].SQLColumn, 'favorited')
    self.assertEqual(result.columns[7].SQLColumn, 'updatedAt')
    self.assertEqual(result.columns[0].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[1].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[2].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[3].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[4].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[5].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[6].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[7].ColumnTypeAsName(), 'float')

  def testExecuteReadOnlyQueryWithSelect(self):
    """test execute read only with a simple select query"""
    query = 'SELECT id from users where id==2220776716'
    result = self.execute.executeReadOnlyQuery(query)
    expected = '[(2220776716,)]'
    self.assertFalse(result.has_error)
    self.assertEqual(str(result.data), expected)
    self.assertIsNone(result.error_message)
    self.assertEqual(result.columns[0].SQLColumn, 'id')
    self.assertEqual(result.columns[0].ColumnTypeAsName(), 'int')

  def testExecuteQueryDetailedSimple(self):
    """test the execution of a simple Query"""
    query = ('SELECT createdDate, updatedAt, screenName, Name, profileImageUrl,'
             'location, description, url, following, followersCount, '
             'followingCount'
             ' FROM Users ORDER BY createdDate')
    result = self.execute.executeQueryDetailed(query)
    expected_data = self._ReadFromFileRelative('expected_simple_query_data')
    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, str(result.data))

    self.assertEqual(result.columns[0].SQLColumn, 'createdDate')
    self.assertEqual(result.columns[1].SQLColumn, 'updatedAt')
    self.assertEqual(result.columns[2].SQLColumn, 'screenName')
    self.assertEqual(result.columns[3].SQLColumn, 'name')
    self.assertEqual(result.columns[4].SQLColumn, 'profileImageUrl')
    self.assertEqual(result.columns[5].SQLColumn, 'location')
    self.assertEqual(result.columns[6].SQLColumn, 'description')
    self.assertEqual(result.columns[7].SQLColumn, 'url')
    self.assertEqual(result.columns[8].SQLColumn, 'following')
    self.assertEqual(result.columns[9].SQLColumn, 'followersCount')
    self.assertEqual(result.columns[10].SQLColumn, 'followingCount')
    self.assertEqual(result.columns[0].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[1].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[2].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[3].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[4].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[5].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[6].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[7].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[8].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[9].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[10].ColumnTypeAsName(), 'int')

  def testExecuteQueryDetailedSimpleNoData(self):
    """test the execution of a simple Query"""
    query = ('SELECT * From nodata')
    result = self.execute_types.executeQueryDetailed(query)
    expected_data = '[]'
    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, str(result.data))

    self.assertEqual(result.columns[0].SQLColumn, 'intval')
    self.assertEqual(result.columns[1].SQLColumn, 'integerval')
    self.assertEqual(result.columns[2].SQLColumn, 'tinyintval')
    self.assertEqual(result.columns[3].SQLColumn, 'smallintval')
    self.assertEqual(result.columns[4].SQLColumn, 'mediuintval')
    self.assertEqual(result.columns[5].SQLColumn, 'bigintval')
    self.assertEqual(result.columns[6].SQLColumn, 'unsignedbigintval')
    self.assertEqual(result.columns[7].SQLColumn, 'int2val')
    self.assertEqual(result.columns[8].SQLColumn, 'int8val')
    self.assertEqual(result.columns[9].SQLColumn, 'characterval')
    self.assertEqual(result.columns[10].SQLColumn, 'varcharval')
    self.assertEqual(result.columns[11].SQLColumn, 'varyingcharacterval')
    self.assertEqual(result.columns[12].SQLColumn, 'ncharval')
    self.assertEqual(result.columns[13].SQLColumn, 'nativecharacterval')
    self.assertEqual(result.columns[14].SQLColumn, 'nvarcharval')
    self.assertEqual(result.columns[15].SQLColumn, 'textval')
    self.assertEqual(result.columns[16].SQLColumn, 'clobval')
    self.assertEqual(result.columns[17].SQLColumn, 'blobval')
    self.assertEqual(result.columns[18].SQLColumn, 'realval')
    self.assertEqual(result.columns[19].SQLColumn, 'doubleval')
    self.assertEqual(result.columns[20].SQLColumn, 'doubleprecisionval')
    self.assertEqual(result.columns[21].SQLColumn, 'floatval')
    self.assertEqual(result.columns[22].SQLColumn, 'numericval')
    self.assertEqual(result.columns[23].SQLColumn, 'decimalval')
    self.assertEqual(result.columns[24].SQLColumn, 'booleanval')
    self.assertEqual(result.columns[25].SQLColumn, 'dateval')
    self.assertEqual(result.columns[26].SQLColumn, 'datetimeval')
    self.assertEqual(result.columns[0].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[1].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[2].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[3].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[4].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[5].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[6].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[7].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[8].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[9].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[10].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[12].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[13].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[14].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[15].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[16].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[17].ColumnTypeAsName(), 'bytes')
    self.assertEqual(result.columns[18].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[19].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[20].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[21].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[22].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[23].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[24].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[25].ColumnTypeAsName(), 'float')
    self.assertEqual(result.columns[26].ColumnTypeAsName(), 'float')

  def testExecuteQueryDetailedJoinNoData(self):
    """test the execution of a join Query with no data"""
    query = (
    'SELECT t1.a, t2.a, t2.c, t1.b, t2.b from t1 join t2')
    result = self.execute_names.executeQueryDetailed(query)
    expected_data = '[]'
    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, str(result.data))

    self.assertEqual(result.columns[0].SQLColumn, 'a')
    self.assertEqual(result.columns[1].SQLColumn, 'a')
    self.assertEqual(result.columns[2].SQLColumn, 'c')
    self.assertEqual(result.columns[3].SQLColumn, 'b')
    self.assertEqual(result.columns[4].SQLColumn, 'b')
    self.assertEqual(result.columns[0].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[1].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[2].ColumnTypeAsName(), 'str')
    self.assertEqual(result.columns[3].ColumnTypeAsName(), 'int')
    self.assertEqual(result.columns[4].ColumnTypeAsName(), 'str')

  def testExecuteQuerySimple(self):
    """test the execution of a simple Query"""
    query = ('SELECT createdDate, updatedAt, screenName, Name, profileImageUrl,'
             'location, description, url, following, followersCount, '
             'followingCount'
             ' FROM Users ORDER BY createdDate')
    result = self.execute.executeQuery(query)
    expected_data = self._ReadFromFileRelative('expected_simple_query_data')
    self.assertIsNone(result.error_message)
    self.assertFalse(result.has_error)
    self.assertEqual(expected_data, str(result.data))
    self.assertIsNone(result.columns)

  def testExecuteReadOnlyQueryWithErrorBecauseOfDrop(self):
    """test execute read only with a drop query"""
    query = 'DROP table users'
    result = self.execute.executeReadOnlyQuery(query)
    expected_error = 'Query has to be a single SELECT query.'
    self.assertTrue(result.has_error)
    self.assertEqual(str(result.error_message), expected_error)
    self.assertIsNone(result.data)
    self.assertIsNone(result.columns)

  def testExecuteReadOnlyQueryWithErrorBecauseOfAlter(self):
    """test execute read only with a alter rename query"""
    query = 'Alter table users rename to users2'
    result = self.execute.executeReadOnlyQuery(query)
    expected_error = 'Query has to be a single SELECT query.'
    self.assertTrue(result.has_error)
    self.assertEqual(str(result.error_message), expected_error)
    self.assertIsNone(result.data)
    self.assertIsNone(result.columns)

  def testExecuteReadOnlyQueryWithWarning(self):
    """test execute read only with two queries at the same time"""
    query = 'SELECT id from users;SELECT id from users;'
    result = self.execute.executeReadOnlyQuery(query)
    expected_error = 'Query has to be a single SELECT query.'
    self.assertTrue(result.has_error)
    self.assertEqual(str(result.error_message), expected_error)
    self.assertIsNone(result.data)
    self.assertIsNone(result.columns)

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
