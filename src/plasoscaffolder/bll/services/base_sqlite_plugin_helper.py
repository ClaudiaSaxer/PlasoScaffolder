# -*- coding: utf-8 -*-
"""Base class for sqlite plugin helper"""
import abc

from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSQLitePluginPathHelper


class BaseSQLitePluginHelper(object):
  """Class representing the base class for the sqlite plugin helper."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
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
