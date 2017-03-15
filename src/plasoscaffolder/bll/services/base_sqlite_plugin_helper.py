# -*- coding: utf-8 -*-
from abc import ABCMeta
from abc import abstractmethod
from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSqlitePluginPathHelper


class BaseSqlitePluginHelper(metaclass=ABCMeta):
  """Class representing the base class for the sqlite plugin helper."""

  @abstractmethod
  def plugin_exists(self, path: str, plugin_name: str,
      sqlitePluginPathHelper: BaseSqlitePluginPathHelper) -> bool:
    """Checks if the plugin already exists.

    Args:
      path (str): the path of the plaso source
      plugin_name (str): the name of the plugin
      sqlitePluginPathHelper (BaseSqlitePluginHelper) : the sqlite plugin helper

    Returns:
      bool: True if the plugin already exists. False if it does not.
    """

  @abstractmethod
  def file_exists(self, path: str) -> bool:
    """Checks if the file exists.

    Args:
       path (str): the file path
    """

  @abstractmethod
  def folder_exists(self, path: str) -> bool:
    """Checks if folder exists.

    Args:
      path (str): the folder path
    """
