# -*- coding: utf-8 -*-
"""SQLite plugin helper"""
import os
import re

from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper
from plasoscaffolder.dal import base_sql_query_execution


class SQLitePluginHelper(base_sqlite_plugin_helper.BaseSQLitePluginHelper):
  """Class containing helper functions for the SQLite plugin"""

  def __init__(self):
    """Initializes the sqlite plugin halper"""
    super().__init__()

  def PluginExists(
      self,
      path: str,
      plugin_name: str,
      database_suffix: str,
      path_helper: base_sqlite_plugin_path_helper.BaseSQLitePluginPathHelper(),
  ) -> bool:
    """Checks if the plugin already exists.

    Args:
      database_suffix: the suffix of the database file
      path (str): the path of the plaso source
      plugin_name (str): the name of the plugin
      path_helper (BaseSQLitePluginHelper): the SQLite plugin helper

    Returns:
      bool: True if the plugin already exists. False if it does not.
    """

    helper = path_helper

    return (os.path.isfile(helper.formatter_file_path)
            or os.path.isfile(helper.parser_file_path)
            or os.path.isfile(helper.formatter_test_file_path)
            or os.path.isfile(helper.parser_test_file_path)
            or os.path.isfile(helper.database_path))

  def IsValidPluginName(self, plugin_name: str) -> bool:
    """Validates the plugin name.

    Args:
      plugin_name (str): the plugin name

    Returns:
      bool: true if the plugin name is valid
    """
    pattern = re.compile("[a-z]+((_)[a-z]+)*")
    return pattern.fullmatch(plugin_name)

  def FileExists(self, path: str) -> bool:
    """Checks if the file exists

    Args:
      path: the plaso folder path

    Returns: true if the file exists
    """
    return os.path.isfile(path)

  def FolderExists(self, path: str) -> bool:
    """Checks if folder exists

    Args:
      path: the plaso folder path

    Returns: true if the folder exists
    """
    return os.path.isdir(path)

  def RunSQLQuery(self, query: str,
                      executor: base_sql_query_execution.BaseSQLQueryExecution()):
    """ Validates the sql query
    
    Args:
      executor (base_sql_query_execution.SQLQueryExection()) the sql executor
      query (str): the SQL query 

    Returns:
      base_sql_query_execution.SQLQueryData: the data to the executed query
    """
    return executor.executeQuery(query)
