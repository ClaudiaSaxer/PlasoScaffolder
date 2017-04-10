# -*- coding: utf-8 -*-
"""Base class for sqlite plugin helper"""
import abc

from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper
from plasoscaffolder.dal import base_sql_query_execution


class BaseSQLitePluginHelper(object):
  """Class representing the base class for the sqlite plugin helper."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def PluginExists(
      self,
      path: str,
      plugin_name: str,
      database_suffix: str,
      path_helper: base_sqlite_plugin_path_helper.BaseSQLitePluginPathHelper
  ) -> bool:
    """Checks if the plugin already exists.

    Args:
      database_suffix: the suffix of the database file
      path (str): the path of the plaso source
      plugin_name (str): the name of the plugin
      path_helper (BaseSqlitePluginHelper): the sqlite plugin helper

    Returns:
      bool: True if the plugin already exists. False if it does not.
    """

  @abc.abstractmethod
  def FileExists(self, path: str) -> bool:
    """Checks if the file exists.

    Args:
       path (str): the file path
    """

  @abc.abstractmethod
  def FolderExists(self, path: str) -> bool:
    """Checks if folder exists.

    Args:
      path (str): the folder path
    """

  @abc.abstractmethod
  def IsValidPluginName(self, plugin_name: str) -> bool:
    """Validates the plugin name.

    Args:
      plugin_name (str): the plugin name

    Returns:
      bool: true if the plugin name is valid
    """

  @abc.abstractmethod
  def RunSQLQuery(self, query: str,
                  executor: base_sql_query_execution.BaseSQLQueryExecution):
    """ Validates the sql query

    Args:
      executor (base_sql_query_execution.SQLQueryExecution): to validate the 
      SQL queries provided by the user
      query (str): the SQL query 

    Returns:
      base_sql_query_execution.SQLQueryData: the data to the executed query
    """
