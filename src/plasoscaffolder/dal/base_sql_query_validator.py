# -*- coding: utf-8 -*-
"""the SQLite query validator"""
import abc


class SQLQueryValidator(object):
  """Class representing the SQLite query validator

  Attributes:
    data: the data rows fetched after the execute of the sql query
    errorMessage: the error Message if something went wrong when executing
    the sql query
  """

  @abc.abstractmethod
  def IsValid(self, query: str) -> bool:
    """Validate the SQL query.

    Args:
      query (str): The SQL query to validate on the SQLite database.

    Returns:
      bool: True if the query is valid. False if it has an error."""
