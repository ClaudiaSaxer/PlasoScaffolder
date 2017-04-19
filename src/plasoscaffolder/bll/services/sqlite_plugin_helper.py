# -*- coding: utf-8 -*-
# Disable linting until PyCQA/astroid/issues/362 is fixed.
# pylint: skip-file
"""SQLite plugin helper"""
import functools
import os
import re

from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper
from plasoscaffolder.dal import base_sql_query_execution
from plasoscaffolder.model import sql_query_model


class SQLitePluginHelper(base_sqlite_plugin_helper.BaseSQLitePluginHelper):
  """Class containing helper functions for the SQLite plugin"""

  def __init__(self):
    """Initializes the SQLite plugin helper"""
    super().__init__()
    self._plugin_name_pattern = re.compile("[a-z]+((_)[a-z]+)*")
    self._row_name_pattern = re.compile("[A-Z]+([a-zA-Z])*")

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
      plugin_name (str): the Name of the plugin
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
    """Validates the plugin Name.

    Args:
      plugin_name (str): the plugin Name

    Returns:
      bool: true if the plugin Name is valid
    """
    return self._plugin_name_pattern.fullmatch(plugin_name)


  def IsValidRowName(self, row_name: str) -> bool:
    """Validates the row name.

    Args:
      row_name (str): the row name

    Returns:
      bool: true if the row name is valid
    """
    return self._row_name_pattern.fullmatch(row_name)

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
      base_sql_query_execution.SQLQueryData: data returned by executing the
        query
    """
    return executor.executeReadOnlyQuery(query)


  def GetDistinctColumnsFromSQLQueryData(
      self,
      queries: [sql_query_model.SQLQueryModel]) -> [str]:
    """
    Get a distinct list of all attributes from multiple queries

    Args:
      queries ([sql_query_model.SQLQueryModel]): an array of multiple
        sql query data objects

    Returns:
      [str]: a distinct list of all attributes used in the query
    """
    distinct_columns = []
    if len(queries) != 0:
      list_of_list_of_column_model = map(lambda x: x.Columns, queries)
      list_of_column_model = functools.reduce(
          lambda x, y: x + y, list_of_list_of_column_model)
      list_of_columns_snake_case = list(
          map(lambda x: x.ColumnAsSnakeCase(), list_of_column_model))
      distinct_columns = sorted(set().union(list_of_columns_snake_case))
    return distinct_columns
