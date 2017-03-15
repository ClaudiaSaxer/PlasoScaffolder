# -*- coding: utf-8 -*-
from abc import ABCMeta
from abc import abstractmethod


class BaseSQLitePluginPathHelper(metaclass=ABCMeta):
  """Class representing the base class for the sqlite plugin path helper"""

  def __init__(self, path: str, plugin_name: str):
    """Initializes the sqlite plugin halper.

     Args:
      path (str): the plaso folder path
      plugin_name (str): The name of the plugin to check.
    """

  @abstractmethod
  def formatter_file_path(self) -> str:
    """The formatter file path for the SQLite plugin for the plaso folder.

    Returns:
      str: path of the new file.
    """

  @abstractmethod
  def parser_file_path(self) -> str:
    """ The parser file path for the SQLite plugin for the plaso folder.

    Returns:
       str: path of the new file.
    """

  @abstractmethod
  def formatter_test_file_path(self) -> str:
    """ The formatter test file path for the SQLite plugin for the plaso folder.

    Returns:
       str: path of the new file.
    """

  @abstractmethod
  def parser_test_file_path(self) -> str:
    """ The parser test file path for the sqlite plugin for the plaso folder.

    Returns:
       str: path of the new file.
    """

  @abstractmethod
  def database_path(self) -> str:
    """The database file path for the SQLite plugin for the plaso folder.

    Returns:
      str: path of the new file.
    """

  @abstractmethod
  def parser_init_file_path(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    Returns:
       str: path of the init file.
    """

  @abstractmethod
  def formatter_init_file_path(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    References:
       str: path of the init file.
    """
