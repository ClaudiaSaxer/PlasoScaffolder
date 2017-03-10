# -*- coding: utf-8 -*-
"""Module containing helper functions for the SQLite plugin"""
import os


def plugin_exists(path: str, plugin_name: str) -> bool:
  """Checks if the plugin already exists.

  Args:
    path: the plaso folder path
    plugin_name: The name of the plugin to check.

  Returns: Boolean True if the plugin already exists. False if it does not.
  """
  return os.path.isfile(formatter_file_path(path, plugin_name)) or os.path.isfile(
    parser_file_path(path, plugin_name)) or os.path.isfile(
    formatter_test_file_path(path, plugin_name)) or os.path.isfile(
    parser_test_file_path(path, plugin_name)) or os.path.isfile(database_path(path,
    plugin_name))


def file_exists(path: str) -> bool:
  """Checks if the file exists

  Args:
     path the file path
  """
  return os.path.isfile(path)


def folder_exists(path: str) -> bool:
  """Checks if folder exists

  Args:
    path: the folder path
  """
  return os.path.isdir(path)


def formatter_file_path(path: str, plugin_name: str) -> str:
  """The formatter file path for the SQLite plugin for the plaso folder.

  Args:
    path: The path to the plaso folder.
    plugin_name: The name of the plugin.

  Returns: The path of the new file.
  """
  file_name = "{0:s}.py".format(plugin_name)
  return os.path.join(path, "plaso", "formatters", file_name)


def parser_file_path(path: str, plugin_name: str) -> str:
  """ The parser file path for the SQLite plugin for the plaso folder.

  Args:
     path: The path to the plaso folder.
     plugin_name: The name of the plugin.

  Returns: The path of the new file.
  """
  return os.path.join(path, "plaso", "parsers", "sqlite_plugins", plugin_name +
                                                          ".py")


def formatter_test_file_path(path: str, plugin_name: str) -> str:
  """ The formatter test file path for the SQLite plugin for the plaso folder.

  Args:
     path: The path to the plaso folder.
    plugin_name: The name of the plugin.

  Returns: The path of the new file.
  """
  return os.path.join(path, "tests", "formatters", plugin_name + ".py")


def parser_test_file_path(path: str, plugin_name: str) -> str:
  """ The parser test file path for the sqlite plugin for the plaso folder.

  Args:
    path: The path to the plaso folder.
    plugin_name: The name of the parser.

  Returns: The path of the new file.
  """
  return os.path.join(path, "tests", "parsers", "sqlite_plugins", plugin_name +
                                                          ".py")


def database_path(path: str, plugin_name: str) -> str:
  """The database file path for the SQLite plugin for the plaso folder.

  Args:
     path: The path to the plaso folder.
     plugin_name: The name of the plugin.

  Returns: The path of the new file.
  """
  return os.path.join(path, "test_data", plugin_name + ".db")

def parser_init_file_path(path: str) -> str:
  """ The parser init file path for the sqlite plugin for the plaso folder.

  Args:
    path: The path to the plaso folder.

  Returns: The path of the init file.
  """
  return os.path.join(path,"plaso", "parsers", "sqlite_plugins", "__init__.py")


def formatter_init_file_path(path: str) -> str:
  """ The parser init file path for the sqlite plugin for the plaso folder.

  Args:
    path: The path to the plaso folder.

  References: The path of the init file.
  """
  return os.path.join(path, "plaso","formatters", "__init__.py")
