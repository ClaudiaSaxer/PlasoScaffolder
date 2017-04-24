# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Base for sql Query validators"""
import sqlite3

from plasoscaffolder.dal import base_sql_query_execution
from plasoscaffolder.dal import explain_query_plan
from plasoscaffolder.model import sql_query_column_model


class SQLQueryExecution(base_sql_query_execution.BaseSQLQueryExecution):
  """Class representing the SQLite Query validator"""

  def __init__(self, database_path: str):
    """Initializes the SQL Query Validator

    Args:
      database_path: the path to the SQLite database schema
    """
    super().__init__()
    self._database_path = database_path
    self._connection = None
    self._explain = None

  def tryToConnect(self) -> bool:
    """Try to open the database File

    Returns:
      bool: if the file can be opened and is a database file
    """
    try:
      self._connection = sqlite3.connect(self._database_path)
      self._connection.isolation_level = None  # no autocommit mode
      self._explain = explain_query_plan.ExplainQueryPlan(self)
      # this query failes if is not a database or locked or anything went wrong
      self._connection.execute('PRAGMA schema_version')
    except sqlite3.Error:
      return False

    return True

  def executeQuery(self, query: str,
                   detailed: bool = True
                   ) -> base_sql_query_execution.SQLQueryData:
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.
      detailed (bool): True if additional information about the query is needed

    Returns:
      base_sql_query_execution.SQLQueryData: The data to the Query
    """
    query_data = base_sql_query_execution.SQLQueryData()
    try:
      with self._connection:
        self._connection.execute('BEGIN')
        cursor = self._connection.execute(query)
        query_data.data = cursor.fetchall()
        if detailed:
          query_data.columns = self._getColumnInformation(
              cursor, query_data.data)
        self._connection.execute('ROLLBACK')
    except sqlite3.Error as error:
      query_data.error_message = 'Error: {0}'.format(str(error))
      query_data.has_error = True
    except sqlite3.Warning as warning:
      query_data.error_message = 'Warning: {0}'.format(str(warning))
      query_data.has_error = True
    return query_data

  def _getColumnInformation(
      self, cursor, query_data: []
  ) -> [sql_query_column_model.SQLColumnModel]:
    """get Information for the column out of the cursor

    Args:
      cursor: the cursor
      query_data: the data of the query

    Returns:
      list(sql_query_column_model.SQLColumnModel): a list with all the columns
    """
    if cursor.description is not None:
      column_types = list()
      for y in query_data[0]:
        column_types.append(type(y))

      sql_column = list()
      for i in range(0, len(cursor.description)):
        sql_column.append(sql_query_column_model.SQLColumnModel(
            cursor.description[i][0], column_types[i]))
      return sql_column
    return None

  def executeReadOnlyQuery(self, query: str):
    """Executes the SQL Query if it is read only.

      Args:
        query (str): The SQL Query to execute on the SQLite database.

      Returns:
        base_sql_query_execution.SQLQueryData: The data to the Query
      """
    query_data = self.executeQuery(query)
    if not query_data.has_error:
      if not self._explain.isReadOnly(query):
        query_data.data = None
        query_data.has_error = True
        query_data.error_message = 'Query has to be a SELECT query.'
    return query_data
