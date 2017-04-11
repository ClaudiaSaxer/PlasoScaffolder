# -*- coding: utf-8 -*-
"""Base class for the Information for the SQLite Database"""
import abc


class BaseDatabaseInformation(object):
  """Base class representing the SQLite Query validator
  """

  @abc.abstractmethod
  def getTablesFromDatabase(self) -> [str]:
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.

    Returns:
      [str]: the names of the tables"""
