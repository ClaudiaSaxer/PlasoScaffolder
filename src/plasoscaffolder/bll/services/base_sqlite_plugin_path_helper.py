# -*- coding: utf-8 -*-
"""Base class for sqlite plugin path helper"""
import abc


class BaseSQLitePluginPathHelper(object):
  """Class representing the base class for the sqlite plugin path helper"""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def FormatterFilePath(self) -> str:
    """The formatter file path for the SQLite plugin for the plaso folder.

    Returns:
      str: path of the new file.
    """

  @abc.abstractmethod
  def ParserFilePath(self) -> str:
    """ The parser file path for the SQLite plugin for the plaso folder.

    Returns:
       str: path of the new file.
    """

  @abc.abstractmethod
  def FormatterTestFilePath(self) -> str:
    """ The formatter test file path for the SQLite plugin for the plaso folder.

    Returns:
       str: path of the new file.
    """

  @abc.abstractmethod
  def ParserTestFilePath(self) -> str:
    """ The parser test file path for the sqlite plugin for the plaso folder.

    Returns:
       str: path of the new file.
    """

  @abc.abstractmethod
  def DatabasePath(self, suffix: str) -> str:
    """The database file path for the SQLite plugin for the plaso folder.

    Args:
      suffix (str): the suffix of the database file

    Returns:
      str: path of the new file.
    """

  @abc.abstractmethod
  def ParserInitFilePath(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    Returns:
       str: path of the init file.
    """

  @abc.abstractmethod
  def FormatterInitFilePath(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    References:
       str: path of the init file.
    """
