# -*- coding: utf-8 -*-
import os
from abc import ABCMeta, abstractmethod


class BaseSqlitePluginPathHelper(metaclass=ABCMeta):
  """Class representing the base class for the sqlite plugin path helper"""
  def __init__(self, path: str, plugin_name: str):
    """Initializes the sqlite plugin halper

     Args:
      path: the plaso folder path
      plugin_name: The name of the plugin to check.

    """

  @abstractmethod
  def formatter_file_path(self) -> str:
    """The formatter file path for the SQLite plugin for the plaso folder.

    Returns: The path of the new file.
    """
    pass

  @abstractmethod
  def parser_file_path(self) -> str:
    """ The parser file path for the SQLite plugin for the plaso folder.

    Returns: The path of the new file.
    """
    pass

  @abstractmethod
  def formatter_test_file_path(self) -> str:
    """ The formatter test file path for the SQLite plugin for the plaso folder.

    Returns: The path of the new file.
    """
    pass

  @abstractmethod
  def parser_test_file_path(self) -> str:
    """ The parser test file path for the sqlite plugin for the plaso folder.


    Returns: The path of the new file.
    """
    pass

  @abstractmethod
  def database_path(self) -> str:
    """The database file path for the SQLite plugin for the plaso folder.


    Returns: The path of the new file.
    """
    pass

  @abstractmethod
  def parser_init_file_path(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    Returns: The path of the init file.
    """
    pass

  @abstractmethod
  def formatter_init_file_path(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    References: The path of the init file.
    """
    pass
