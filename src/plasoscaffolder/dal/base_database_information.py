# -*- coding: utf-8 -*-
"""Base class for the Information for the SQLite Database"""
import abc


class BaseDatabaseInformation(object):
  """Base class representing the SQLite Query validator."""

  @abc.abstractmethod
  def getTablesFromDatabase(self) -> [str]:
    """Executes the SQL Query.

    Returns:
      [str]: the name of the tables
    """
