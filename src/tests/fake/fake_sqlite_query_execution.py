# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Base for SQL query validators"""

from plasoscaffolder.dal import base_sql_query_execution
from plasoscaffolder.dal import sql_query_data


class SQLQueryExecution(base_sql_query_execution.BaseSQLQueryExecution):
  """Class representing the SQLite Query validator"""

  def __init__(self, to_return: sql_query_data.SQLQueryData):
    """Initializes the SQL Query Validator

    Args:
      database_path: the path to the SQLite database schema
    """
    self.to_return = to_return

  def ExecuteQuery(
      self, query: str
  ) -> sql_query_data.SQLQueryData:
    """Executes the SQL Query."""
    return self.to_return

  def ExecuteReadOnlyQuery(self, query: str):
    """Executes the SQL Query if it is read only."""
    return self.to_return
