# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Base for sql query validators"""
import sqlite3

from plasoscaffolder.dal import base_sql_query_validator


class BaseSQLQueryValidator(base_sql_query_validator.SQLQueryValidator):
  """Class representing the SQLite query validator

  Attributes:
    data: the data rows fetched after the execute of the sql query
    errorMessage: the error Message if something went wrong when executing
    the sql query
  """

  def __init__(self, database_path: str):
    """Initializes the SQL Query Validator

    Args:
      database_path: the path to the sqlite database schema
    """
    self.data = None
    self.errorMessage = None
    self._OpenConnection(database_path)
    self._connection = sqlite3.connect(database_path)

  def IsValid(self, query: str) -> bool:
    """Validate the SQL query.

    Args:
      query (str): The SQL query to validate on the SQLite database.

    Returns:
      bool: True if the query is valid. False if it has an error.

    """
    try:
      with self._connection:
        cursor = self._connection.execute(query)
        self.data = cursor.fetchall()
    except sqlite3.Error as error:
      print(error)
      self.errorMessage = error
      return False

    return True
