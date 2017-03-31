# -*- coding: utf-8 -*-
"""the SQLite Query validator"""
import abc


class SQLQueryData(object):
  """The Data to the executed Query

  Attributes:
    has_error (bool): if the Query execution was erroneous
    data ([str]): the rows returned after execution
    error_message: hte error message if the Query was erroneous"""

  def __init__(self, has_error=False, data=None, error_message=None):
    self.has_error = has_error
    self.data = data
    self.error_message = error_message


class BaseSQLQueryExecution(object):
  """Class representing the SQLite Query validator"""

  @abc.abstractmethod
  def executeQuery(self, query: str) -> SQLQueryData:
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.

    Returns:
      SQLQueryData: The data to the Query"""
