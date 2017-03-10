# -*- coding: utf-8 -*-
"""Module containing helper functions for the SQLite plugin"""
import os


def plugin_exists(path: str, plugin_name: str) -> bool:
  """ Checks if the plugin already exists.

  :param plugin_name: The name of the plugin to check.
  :param path: the plaso folder path
  :return: Boolean True if the plugin already exists. False if it does not.
  """
  return os.path.isfile(formatter_file_path(path, plugin_name)) or os.path.isfile(
    parser_file_path(path, plugin_name)) or os.path.isfile(
    formatter_test_file_path(path, plugin_name)) or os.path.isfile(
    parser_test_file_path(path, plugin_name)) or os.path.isfile(database_path(path,
    plugin_name))


def file_exists(path: str) -> bool:
  """ Checks if the file exists

  :param path the file path
  """
  return os.path.isfile(path)


def folder_exists(path: str) -> bool:
  """Checks if folder exists

  :param path the folder path
  """
  return os.path.isdir(path)


def formatter_file_path(path: str, plugin_name: str) -> str:
  """ The formatter file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return os.path.join(path, "plaso", "formatters", plugin_name + ".py")


def parser_file_path(path: str, plugin_name: str) -> str:
  """ The parser file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return os.path.join(path, "plaso", "parsers", "sqlite_plugins", plugin_name +
                                                          ".py")


def formatter_test_file_path(path: str, plugin_name: str) -> str:
  """ The formatter test file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return os.path.join(path, "tests", "formatters", plugin_name + ".py")


def parser_test_file_path(path: str, plugin_name: str) -> str:
  """ The parser test file path for the sqlite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the parser.
  :return: The path of the new file.
  """
  return os.path.join(path, "tests", "parsers", "sqlite_plugins", plugin_name +
                                                          ".py")


def database_path(path: str, plugin_name: str) -> str:
  """ The database file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return os.path.join(path, "test_data", plugin_name + ".db")

def parser_init_file_path(path: str) -> str:
  """ The parser init file path for the sqlite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :return: The path of the init file.
  """
  return os.path.join(path,"plaso", "parsers", "sqlite_plugins", "__init__.py")


def formatter_init_file_path(path: str) -> str:
  """ The parser init file path for the sqlite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :return: The path of the init file.
  """
  return os.path.join(path, "plaso","formatters", "__init__.py")
