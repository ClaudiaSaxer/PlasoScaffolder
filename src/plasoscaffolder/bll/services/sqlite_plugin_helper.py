# -*- coding: utf-8 -*-
"""SQLite plugin helper"""
import os
import re

from plasoscaffolder.bll.services.base_sqlite_plugin_helper import \
  BaseSQLitePluginHelper
from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSQLitePluginPathHelper


class SQLitePluginHelper(BaseSQLitePluginHelper):
  """Class containing helper functions for the SQLite plugin"""

  def __init__(self):
    """Initializes the sqlite plugin halper"""
    super().__init__()

  def PluginExists(self, path: str, plugin_name: str,
                    sqlitePluginPathHelper: BaseSQLitePluginPathHelper) -> bool:
    """Checks if the plugin already exists.

    Args:
      path (str): the path of the plaso source
      plugin_name (str): the name of the plugin
      sqlitePluginPathHelper (BaseSqlitePluginHelper) : the sqlite plugin helper

    Returns:
      bool: True if the plugin already exists. False if it does not.
    """
    helper = sqlitePluginPathHelper(path, plugin_name)

    return (os.path.isfile(helper.FormatterFilePath())
            or os.path.isfile(helper.ParserFilePath())
            or os.path.isfile(helper.FormatterTestFilePath())
            or os.path.isfile(helper.ParserTestFilePath())
            or os.path.isfile(helper.DatabasePath("")))

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
