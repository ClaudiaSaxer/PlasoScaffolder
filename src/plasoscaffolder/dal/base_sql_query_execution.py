# -*- coding: utf-8 -*-
# disable warning because default value is not dangerous here
# pylint: disable=dangerous-default-value
"""the SQLite Query validator"""
import abc


class SQLQueryData(object):
  """The Data to the executed query.

  Attributes:
    has_error (bool): if the query execution was erroneous
    data ([str]): the rows returned after execution
    error_message: the error message if the query was erroneous
    columns ([str]): the column names of the query"""

  def __init__(self, has_error=False, data=None, error_message=None,
               columns=[]):
    self.has_error = has_error
    self.data = data
    self.error_message = error_message
    self.columns = columns


class BaseSQLQueryExecution(object):
  """Class representing the SQLite query validator."""

  @abc.abstractmethod
  def executeQuery(self, query: str) -> SQLQueryData:
    """Executes the SQL query.

    Args:
      query (str): The SQL query to execute on the SQLite database.

    Returns:
      SQLQueryData: The data to the query"""

  @abc.abstractmethod
  def executeReadOnlyQuery(self, query: str):
    """Executes the SQL Query if it is read only.
  
      Args:
        query (str): The SQL Query to execute on the SQLite database.
  
      Returns:
        base_sql_query_execution.SQLQueryData: The data to the Query
      """
