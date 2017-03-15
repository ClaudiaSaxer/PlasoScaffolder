# -*- coding: utf-8 -*-
import os

from plasoscaffolder.bll.services.base_sqlite_plugin_helper import \
  BaseSqlitePluginHelper
from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSqlitePluginPathHelper


class SqlitePluginHelper(BaseSqlitePluginHelper):
  """Class containing helper functions for the SQLite plugin"""

  def __init__(self):
    """Initializes the sqlite plugin halper"""
    super().__init__()


  def plugin_exists(self, path: str, plugin_name: str, sqlitePluginPathHelper: BaseSqlitePluginPathHelper) -> bool:
    """Checks if the plugin already exists.

    Args:
      path (str): the path of the plaso source
      plugin_name (str): the name of the plugin
      sqlitePluginPathHelper (BaseSqlitePluginHelper) : the sqlite plugin helper

    Returns:
      bool: True if the plugin already exists. False if it does not.
    """
    helper = sqlitePluginPathHelper(path, plugin_name)
    return os.path.isfile(helper.formatter_file_path()) or os.path.isfile(
      helper.parser_file_path()) or os.path.isfile(
      helper.formatter_test_file_path()) or os.path.isfile(
      helper.parser_test_file_path()) or os.path.isfile(helper.database_path())

  def file_exists(self, path: str) -> bool:
    """Checks if the file exists

    Args:
      path: the plaso folder path

    Returns: true if the file exists
    """
    return os.path.isfile(path)

  def folder_exists(self, path: str) -> bool:
    """Checks if folder exists

    Args:
      path: the plaso folder path

    Returns: true if the folder exists
    """
    return os.path.isdir(path)
