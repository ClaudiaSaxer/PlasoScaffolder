# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Base for sql Query validators"""
import sqlite3

from plasoscaffolder.dal import base_sql_query_execution


class SQLQueryExecution(base_sql_query_execution.BaseSQLQueryExecution):
  """Class representing the SQLite Query validator"""

  def __init__(self, database_path: str):
    """Initializes the SQL Query Validator

    Args:
      database_path: the path to the sqlite database schema
    """
    super().__init__()
    self._connection = sqlite3.connect(database_path)
    self._connection.isolation_level = None  # no autocommit mode

  def executeQuery(self, query: str) -> base_sql_query_execution.SQLQueryData:
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.

    Returns:
      base_sql_query_execution.SQLQueryData: The data to the Query
    """
    query_data = base_sql_query_execution.SQLQueryData()
    try:
      with self._connection:
        self._connection.execute("BEGIN")
        cursor = self._connection.execute(query)
        query_data.data = cursor.fetchall()
        if cursor.description is not None:
          query_data.columns = list(map(lambda x: x[0], cursor.description))
        self._connection.execute('ROLLBACK')
    except sqlite3.Error as error:
      query_data.error_message = error
      query_data.has_error = True

    return query_data
