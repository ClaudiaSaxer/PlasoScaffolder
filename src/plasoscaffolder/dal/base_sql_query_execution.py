# -*- coding: utf-8 -*-
# disable warning because default value is not dangerous here
"""The SQLite Query validator."""
import abc


class BaseSQLQueryExecution(object):
  """Class representing the SQLite query validator."""

  @abc.abstractmethod
  def ExecuteQuery(self, query: str):
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.
      detailed (bool): True if additional information about the query is needed

    Returns:
      base_sql_query_execution.SQLQueryData: The data to the Query
    """

  @abc.abstractmethod
  def ExecuteReadOnlyQuery(self, query: str):
    """Executes the SQL Query if it is read only.

      Args:
        query (str): The SQL Query to execute on the SQLite database.

      Returns:
        sql_query_data.SQLQueryData: The data to the Query
    """
