# -*- coding: utf-8 -*-
"""Base class for the Information for the SQLite Database"""
import abc


class BaseDatabaseInformation(object):
  """Base class representing the SQLite Query validator."""

  @abc.abstractmethod
  def GetTablesFromDatabase(self) -> [str]:
    """Executes the SQL Query.

    Returns:
      [str]: the name of the tables
    """

  @abc.abstractmethod
  def GetTableColumnsAndType(self, table: str, all_lowercase=False) -> [str]:
    """Returns the table information from the database

    Args:
      table (str): the name of the table

    Returns:
      {name, type}: the table information
    """
