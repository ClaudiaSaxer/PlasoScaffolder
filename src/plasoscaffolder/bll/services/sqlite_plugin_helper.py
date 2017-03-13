# -*- coding: utf-8 -*-
"""Module containing helper functions for the SQLite plugin"""
import os

from plasoscaffolder.bll.services.base_sqlite_plugin_helper import \
  BaseSqlitePluginHelper
from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSqlitePluginPathHelper


class SqlitePluginHelper(BaseSqlitePluginHelper):
  def __init__(self):
    """Initializes the sqlite plugin halper"""


  def plugin_exists(self, path: str, plugin_name: str, path_helper: BaseSqlitePluginPathHelper) -> bool:
    """Checks if the plugin already exists.

    Args:
      path: the plaso folder path
      plugin_name: The name of the plugin to check.
      helper: A Sqlite Plugin Path Helper

    Returns: Boolean True if the plugin already exists. False if it does not.
    """
    return os.path.isfile(path_helper.formatter_file_path()) or os.path.isfile(
      path_helper.parser_file_path()) or os.path.isfile(
      path_helper.formatter_test_file_path()) or os.path.isfile(
      path_helper.parser_test_file_path()) or os.path.isfile(path_helper.database_path())

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
