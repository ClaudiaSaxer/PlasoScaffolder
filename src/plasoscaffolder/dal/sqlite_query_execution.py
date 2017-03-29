# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Base for sql query validators"""
import sqlite3

from plasoscaffolder.dal import base_sql_query_execution


class SQLQueryExecution(base_sql_query_execution.BaseSQLQueryExecution):
  """Class representing the SQLite query validator
  """

  def __init__(self, database_path: str):
    """Initializes the SQL Query Validator

    Args:
      database_path: the path to the sqlite database schema
    """
    self._connection = sqlite3.connect(database_path)


  def executeQuery(self, query: str) -> base_sql_query_execution.SQLQueryData:
    """Executes the SQL query.

    Args:
      query (str): The SQL query to execute on the SQLite database.

    Returns:
      base_sql_query_execution.SQLQueryData: The data to the query"""
    query_data = base_sql_query_execution.SQLQueryData()
    try:
      with self._connection:
        cursor = self._connection.execute(query)
        query_data.data = cursor.fetchall()
    except sqlite3.Error as error:
      query_data.error_message = error
      query_data.has_error = True

    return query_data
