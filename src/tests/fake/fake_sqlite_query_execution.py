# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Base for SQL query validators"""

from plasoscaffolder.dal import base_sql_query_execution


class SQLQueryExecution(base_sql_query_execution.BaseSQLQueryExecution):
  """Class representing the SQLite Query validator
  """

  def __init__(self, to_return: object):
    """Initializes the SQL Query Validator

    Args:
      database_path: the path to the SQLite database schema
    """
    self.to_return = to_return

  def executeQuery(self, query: str) -> base_sql_query_execution.SQLQueryData:
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.

    Returns:
      base_sql_query_execution.SQLQueryData: The data to the query"""
    return self.to_return
