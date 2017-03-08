# -*- coding: utf-8 -*-
"""Module containing helper functions for the SQLite plugin"""
import os
from os.path import join, isfile, isdir


def plugin_exists(path: os.path, plugin_name: str) -> bool:
  """ Checks if the plugin already exists.

  :param plugin_name: The name of the plugin to check.
  :param path: the plaso folder path
  :return: Boolean True if the plugin already exists. False if it does not.
  """
  return isfile(formatter_file_path(path, plugin_name)) or isfile(
    parser_file_path(path, plugin_name)) or isfile(
    formatter_test_file_path(path, plugin_name)) or isfile(
    parser_test_file_path(path, plugin_name)) or isfile(database_path(path,
    plugin_name))


def file_exists(path: os.path) -> bool:
  """ Checks if the file exists

  :param path the file path
  """
  return isfile(path)


def folder_exists(path: os.path) -> bool:
  """Checks if folder exists

  :param path the folder path
  """
  return isdir(path)


def formatter_file_path(path: os.path, plugin_name: str) -> os.path:
  """ The formatter file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return join(path, "plaso", "formatters", plugin_name + ".py")


def parser_file_path(path: os.path, plugin_name: str) -> os.path:
  """ The parser file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return join(path, "plaso", "parsers", "sqlite_plugins", plugin_name +
                                                          ".py")


def formatter_test_file_path(path: os.path, plugin_name: str) -> os.path:
  """ The formatter test file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return join(path, "tests", "formatters", plugin_name + ".py")


def parser_test_file_path(path: os.path, plugin_name: str) -> os.path:
  """ The parser test file path for the sqlite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the parser.
  :return: The path of the new file.
  """
  return join(path, "tests", "parsers", "sqlite_plugins", plugin_name +
                                                          ".py")


def database_path(path: os.path, plugin_name: str) -> os.path:
  """ The database file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return join(path, "test_data", plugin_name + ".db")

def parser_init_file_path(path: os.path) -> os.path:
  """ The parser init file path for the sqlite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :return: The path of the init file.
  """
  return join(path,"plaso", "parsers", "sqlite_plugins", "__init__.py")


def formatter_init_file_path(path: os.path) -> os.path:
  """ The parser init file path for the sqlite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :return: The path of the init file.
  """
  return join(path, "plaso","formatters", "__init__.py")
