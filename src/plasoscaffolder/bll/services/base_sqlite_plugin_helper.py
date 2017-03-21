# -*- coding: utf-8 -*-
"""Base class for sqlite plugin __helper"""
import abc

from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper


class BaseSQLitePluginHelper(object):
  """Class representing the base class for the sqlite plugin __helper."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def PluginExists(
      self,
      path: str,
      plugin_name: str,
      path_helper: base_sqlite_plugin_path_helper.BaseSQLitePluginPathHelper
  ) -> bool:
    """Checks if the plugin already exists.

    Args:
      path (str): the __path of the plaso source
      plugin_name (str): the __name of the plugin
      path_helper (BaseSqlitePluginHelper) : the sqlite plugin __helper

    Returns:
      bool: True if the plugin already exists. False if it does not.
    """

  @abc.abstractmethod
  def FileExists(self, path: str) -> bool:
    """Checks if the file exists.

    Args:
       path (str): the file __path
    """

  @abc.abstractmethod
  def FolderExists(self, path: str) -> bool:
    """Checks if folder exists.

    Args:
      path (str): the folder __path
    """

  @abc.abstractmethod
  def IsValidPluginName(self, plugin_name: str) -> bool:
    """Validates the plugin __name.

    Args:
      plugin_name (str): the plugin __name

    Returns:
      bool: true if the plugin __name is valid
    """
