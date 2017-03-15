# -*- coding: utf-8 -*-
import os

from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSQLitePluginPathHelper


class SQLitePluginPathHelper(BaseSQLitePluginPathHelper):
  """Class containing helper functions for the SQLite plugin for the path"""

  def __init__(self, path: str, plugin_name: str):
    """Initializes the sqlite plugin halper.

      Args:
       path (str): the plaso folder path
       plugin_name (str): The name of the plugin to check.
     """
    super().__init__(path, plugin_name)
    self.path = path
    self.plugin_name = plugin_name
    self.file_name = '{0:s}.py'.format(self.plugin_name)

  def formatter_file_path(self) -> str:
    """The formatter file path for the SQLite plugin for the plaso folder.

    Returns:
      str: path of the new file.
    """

    return os.path.join(self.path, 'plaso', 'formatters', self.file_name)

  def parser_file_path(self) -> str:
    """ The parser file path for the SQLite plugin for the plaso folder.

    Returns:
      str: path of the new file.
    """
    return os.path.join(self.path, 'plaso', 'parsers', 'sqlite_plugins',
      self.file_name)

  def formatter_test_file_path(self) -> str:
    """ The formatter test file path for the SQLite plugin for the plaso folder.

    Returns:
      str:  path of the new file.
    """
    return os.path.join(self.path, 'tests', 'formatters', self.file_name)

  def parser_test_file_path(self) -> str:
    """ The parser test file path for the sqlite plugin for the plaso folder.

    Returns:
      str:  path of the new file.
    """
    return os.path.join(self.path, 'tests', 'parsers', 'sqlite_plugins',
      self.file_name)

  def database_path(self) -> str:
    """The database file path for the SQLite plugin for the plaso folder.

    Returns:
      str:  path of the new file.
    """
    return os.path.join(self.path, 'test_data', self.plugin_name + '.db')

  def parser_init_file_path(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    Returns:
      str:  path of the init file.
    """
    return os.path.join(self.path, 'plaso', 'parsers', 'sqlite_plugins',
      '__init__.py')

  def formatter_init_file_path(self) -> str:
    """ The parser init file path for the sqlite plugin for the plaso folder.

    References:
      str:  path of the init file.
    """
    return os.path.join(self.path, 'plaso', 'formatters', '__init__.py')
