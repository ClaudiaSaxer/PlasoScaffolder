# -*- coding: utf-8 -*-
"""File representing the controller for SQLite plugin"""
import os

from plasoscaffolder.bll.services.file_creator import *
import click
from plasoscaffolder.bll.services.sqlite_plugin_helper import *


class SqliteController:
  """ Class representing the controller for the SQLite controller."""
  path = None
  name = None

  def source_path(self, ctx, param, value):
    """ Saving the source path.
    :param ctx: the click context (automatically given via callback)
    :param param: the click command (automatically given via callback)
    :param value: the source path (automatically given via callback)
    :return: the source path representing the same as value
    """
    self.path = value
    return value

  def plugin_name(self, ctx, param, value):
    """ Saving the plugin name.
    :param ctx: the click context (automatically given via callback)
    :param param: the click command (automatically given via callback)
    :param value: the plugin name (automatically given via callback)
    :return: the plugin name representing the same as value
    """
    print("save plugin name " + value)
    while plugin_exists(self.path, value):
      value = click.prompt("Plugin exists. Choose new name: ")
    self.name = value
    return value

  def test_path(self, ctx, param, value):
    """ Saving the path to the test file.
    :param ctx: the click context (automatically given via callback)
    :param param: the click command (automatically given via callback)
    :param value: the test file path (automatically given via callback)
    :return: the test file path representing the same as the value
    """
    print("save test path " + value)
    return value

  def generate(self, path, name, testfile):
    """ Generating the files.
    :param path: the path of the plaso folder
    :param name: the name of the plugin
    :param testfile: the path of the testfile
    """
    creator = FileCreator()
    file = creator.create_file_from_path

    print("generate " + file(formatter_file_path(path, name)))
    print("generate " + file(parser_file_path(path, name)))
    print("generate " + file(parser_test_file_path(path, name)))
    print("generate " + file(formatter_test_file_path(path, name)))
