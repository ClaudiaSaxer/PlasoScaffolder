# -*- coding: utf-8 -*-
"""SQLite Plugin Path Helper"""
import os

from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper


class SQLitePluginPathHelper(
    base_sqlite_plugin_path_helper.BaseSQLitePluginPathHelper):
  """Class containing helper functions for the SQLite plugin for the path"""

  def __init__(self, path: str, plugin_name: str):
    """Initializes the sqlite plugin halper.

      Args:
       path (str): the plaso folder path
       plugin_name (str): The name of the plugin to check.
     """
    super().__init__()
    self.path = path
    self.plugin_name = plugin_name
    self.file_name = '{0:s}.py'.format(self.plugin_name)

  def FormatterFilePath(self) -> str:
    """The formatter file path for the SQLite plugin for the plaso folder.

    Returns:
      str: path of the new file.
    """

    return os.path.join(self.path, 'plaso', 'formatters', self.file_name)

  def ParserFilePath(self) -> str:
    """ The parser file path for the SQLite plugin for the plaso folder.

    Returns:
      str: path of the new file.
    """
    return os.path.join(self.path, 'plaso', 'parsers', 'sqlite_plugins',
                        self.file_name)

  def FormatterTestFilePath(self) -> str:
    """ The formatter test file path for the SQLite plugin for the plaso folder.

    Returns:
      str:  path of the new file.
    """
    return os.path.join(self.path, 'tests', 'formatters', self.file_name)

  def ParserTestFilePath(self) -> str:
    """ The parser test file path for the sqlite plugin for the plaso folder.

    Returns:
      str:  path of the new file.
    """
    return os.path.join(self.path, 'tests', 'parsers', 'sqlite_plugins',
                        self.file_name)

  def DatabasePath(self, suffix: str) -> str:
    """The database file path for the SQLite plugin for the plaso folder.

    Args:
      suffix (str): the file suffix of the database file

    Returns:
      str:  path of the new file.
    """
    file_name = '{0:s}{1:s}'.format(self.plugin_name, suffix)
    return os.path.join(self.path, 'test_data', file_name)

  def ParserInitFilePath(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    Returns:
      str:  path of the init file.
    """
    return os.path.join(self.path, 'plaso', 'parsers', 'sqlite_plugins',
                        '__init__.py')

  def FormatterInitFilePath(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    References:
      str:  path of the init file.
    """
    return os.path.join(self.path, 'plaso', 'formatters', '__init__.py')
