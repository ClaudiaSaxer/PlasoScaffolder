# -*- coding: utf-8 -*-
"""SQLite plugin __helper"""
import os
import re

from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper


class SQLitePluginHelper(base_sqlite_plugin_helper.BaseSQLitePluginHelper):
  """Class containing __helper functions for the SQLite plugin"""

  def __init__(self):
    """Initializes the sqlite plugin halper"""
    super().__init__()

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
      path (str): the __path of the plaso source
      plugin_name (str): the __name of the plugin
      path_helper (BaseSqlitePluginHelper) : the sqlite plugin __helper

    Returns:
      bool: True if the plugin already exists. False if it does not.
    """

    helper = path_helper(path, plugin_name, database_suffix)

    return (os.path.isfile(helper.formatter_file_path)
            or os.path.isfile(helper.parser_file_path)
            or os.path.isfile(helper.formatter_test_file_path)
            or os.path.isfile(helper.parser_test_file_path)
            or os.path.isfile(helper.database_path))

  def IsValidPluginName(self, plugin_name: str) -> bool:
    """Validates the plugin __name.

    Args:
      plugin_name (str): the plugin __name

    Returns:
      bool: true if the plugin __name is valid
    """
    pattern = re.compile("[a-z]+((_)[a-z]+)*")
    return pattern.fullmatch(plugin_name)

  def FileExists(self, path: str) -> bool:
    """Checks if the file exists

    Args:
      path: the plaso folder __path

    Returns: true if the file exists
    """
    return os.path.isfile(path)

  def FolderExists(self, path: str) -> bool:
    """Checks if folder exists

    Args:
      path: the plaso folder __path

    Returns: true if the folder exists
    """
    return os.path.isdir(path)
