# -*- coding: utf-8 -*-
"""Module containing helper functions for the SQLite plugin"""
from os.path import join, isfile


def plugin_exists(path, plugin_name):
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


def formatter_file_path(path, plugin_name):
  """ The formatter file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return join(path, "plaso", "formatters", plugin_name + ".py")


def parser_file_path(path, plugin_name):
  """ The parser file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return join(path, "plaso", "parsers", "sqlite_plugins", plugin_name +
                                                          ".py")


def formatter_test_file_path(path, plugin_name):
  """ The formatter test file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return join(path, "tests", "formatters", plugin_name + ".py")


def parser_test_file_path(path, plugin_name):
  """ The parser test file path for the sqlite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the parser.
  :return: The path of the new file.
  """
  return join(path, "tests", "parsers", "sqlite_plugins", plugin_name +
                                                          ".py")


def database_path(path, plugin_name):
  """ The database file path for the SQLite plugin for the plaso folder.

  :param path: The path to the plaso folder.
  :param plugin_name: The name of the plugin.
  :return: The path of the new file.
  """
  return join(path, "test_data", plugin_name + ".db")
