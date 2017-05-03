# -*- coding: utf-8 -*-
# Disable linting until PyCQA/astroid/issues/362 is fixed.
# pylint: skip-file
"""SQLite plugin helper."""
import functools
import os
import re

from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper
from plasoscaffolder.dal import base_sql_query_execution
from plasoscaffolder.model import sql_query_column_model
from plasoscaffolder.model import sql_query_model


class SQLitePluginHelper(base_sqlite_plugin_helper.BaseSQLitePluginHelper):
  """Class containing helper functions for the SQLite plugin."""

  _PLUGIN_NAME_PATTERN = re.compile("[a-z]+((_)[a-z]+)*")
  _ROW_NAME_PATTERN = re.compile("[A-Z]+([a-zA-Z])*")
  _COMMA_SEPARATED_PATTERN = re.compile("[a-zA-Z0-9]+((,)[a-zA-Z0-9]+)*")

  def __init__(self):
    """Initializes the SQLite plugin helper."""
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
    return self._PLUGIN_NAME_PATTERN.fullmatch(plugin_name)

  def IsValidRowName(self, row_name: str) -> bool:
    """Validates the row name.

    Args:
      row_name (str): the row name

    Returns:
      bool: true if the row name is valid
    """
    return self._ROW_NAME_PATTERN.fullmatch(row_name)

  def IsValidCommaSeparatedString(self, text: str) -> bool:
    """Validates a comma separated string

    Args:
      text (str): the string to validate

    Returns:
      bool: true if the text is valid
    """
    return self._COMMA_SEPARATED_PATTERN.fullmatch(text)

  def FileExists(self, path: str) -> bool:
    """Checks if the file exists.

    Args:
      path: the plaso folder path

    Returns: true if the file exists
    """
    return os.path.isfile(path)

  def FolderExists(self, path: str) -> bool:
    """Checks if folder exists.

    Args:
      path: the plaso folder path

    Returns: true if the folder exists
    """
    return os.path.isdir(path)

  def RunSQLQuery(self, query: str,
                  executor: base_sql_query_execution.BaseSQLQueryExecution()):
    """Validates the sql query.

    Args:
      executor (base_sql_query_execution.SQLQueryExection()) the sql executor
      query (str): the SQL query

    Returns:
      base_sql_query_execution.SQLQueryData: data returned by executing the
          query
    """
    return executor.ExecuteReadOnlyQuery(query)

  def GetDistinctColumnsFromSQLQueryData(
      self,
      queries: [sql_query_model.SQLQueryModel]) -> [str]:
    """Get a distinct list of all attributes from multiple queries.

    Args:
      queries ([sql_query_model.SQLQueryModel]): an array of multiple
          sql query data objects

    Returns:
      list[str]: all distinct attributes used in the query
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

  def GetAssumedTimestamps(self, columns: [
    sql_query_column_model.SQLColumnModel]) -> [str]:
    """Gets all columns assumed that they are timestamps
    
    Args:
      columns ([sql_query_column_model.SQLColumnModel]): the columns from the 
          SQL query

    Returns:
      [str]: the names from the columns assumed they could be a timestamp
    """
    assumed_columns = filter(
        lambda name: 'time' in name.lower() or 'date' in name.lower(),
        map(lambda column: column.SQLColumn, columns))
    return list(assumed_columns)

  def GetColumnsAndTimestampColumn(
      self, columns: [sql_query_column_model.SQLColumnModel], timestamps: [str]) -> (
      [sql_query_column_model.SQLColumnModel],
      [sql_query_column_model.SQLColumnModel]):
    """Splits the column list into a list of simple columns and a list for
    timestamp event columns
    
    Args:
      columns ([sql_query_column_model.SQLColumnModel]): the list with all the columns from the query
      timestamps ([str]): the timestamp events

    Returns:
      ([sql_query_column_model.SQLColumnModel],
          [sql_query_column_model.SQLColumnModel]): a tuple of columns,
          the first are the normal columns, the second are the timestamp events
    """
    normal_columns = list()
    timestamp_columns = list()
    for column in columns:
      if column.SQLColumn in timestamps:
        timestamp_columns.append(column)
      else:
        normal_columns.append(column)
    return normal_columns, timestamp_columns
