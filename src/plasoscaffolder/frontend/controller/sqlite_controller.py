# -*- coding: utf-8 -*-
"""File representing the controller for SQLite plugin"""
from plasoscaffolder.bll.services.sqlite_generator import SqliteGenerator
from plasoscaffolder.bll.services.sqlite_plugin_helper import plugin_exists, \
  file_exists, folder_exists
import click


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
    while not folder_exists(value):
      value = click.prompt(
        click.style("Folder does not exists. Enter correct one: ", fg="red"))
    self.path = value
    return value

  def plugin_name(self, ctx, param, value):
    """ Saving the plugin name.
    :param ctx: the click context (automatically given via callback)
    :param param: the click command (automatically given via callback)
    :param value: the plugin name (automatically given via callback)
    :return: the plugin name representing the same as value
    """
    print(value)
    print(self.path)

    while plugin_exists(self.path, value):
      value = click.prompt(
        click.style("Plugin exists. Choose new name: ", fg="red"))
    self.name = value
    return value

  def test_path(self, ctx, param, value):
    """ Saving the path to the test file.
    :param ctx: the click context (automatically given via callback)
    :param param: the click command (automatically given via callback)
    :param value: the test file path (automatically given via callback)
    :return: the test file path representing the same as the value
    """
    while not file_exists(value):
      value = click.prompt(
        click.style("File does not exists. Choose another: ", fg="red"))
    return value

  def generate(self, path, name, testfile):
    """ Generating the files.
    :param path: the path of the plaso folder
    :param name: the name of the plugin
    :param testfile: the path of the testfile
    """
    generator = SqliteGenerator(path, name, testfile)
    if not generator.init_formatter_exists or not generator.init_parser_exists :
      click.confirm(
        'At least one init file does not exist. Do you want the create them (or else abort)?',
        abort=True, default=True)

    click.confirm('Do you want to generate the files?', abort=True,
      default=True)

    generator.generate_sqlite_plugin()
