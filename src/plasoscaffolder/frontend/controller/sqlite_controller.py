# -*- coding: utf-8 -*-
"""File representing the controller for SQLite plugin"""
import click

from plasoscaffolder.bll.services.file_handler import FileHandler
from plasoscaffolder.bll.services.sqlite_generator import SqliteGenerator
from plasoscaffolder.bll.services.sqlite_plugin_helper import plugin_exists, \
  file_exists, folder_exists


class SqliteController(object):
  """Class representing the controller for the SQLite controller."""
  def __init__(self):
    super(SqliteController, self).__init__()
    self.path = None
    self.name = None
    self.testfile = None

  def source_path(self, ctx: click.core.Context, param: click.core.Option,
      value: str) -> str:
    """Saving the source path.

    Args:
      ctx: the click context (automatically given via callback)
      param: the click command (automatically given via callback)
      value: the source path (automatically given via callback)

    Returns: the source path representing the same as value
    """
    while not folder_exists(value):
      value = click.prompt(
        click.style("Folder does not exists. Enter correct one: ", fg="red"))
    self.path = value
    return value

  def plugin_name(self, ctx: click.core.Context, param: click.core.Option,
      value: str) -> str:
    """Saving the plugin name.

    Args:
      ctx: the click context (automatically given via callback)
      param: the click command (automatically given via callback)
      value: the plugin name (automatically given via callback)

    Returns: the plugin name representing the same as value
    """
    while plugin_exists(self.path, value):
      value = click.prompt(
        click.style("Plugin exists. Choose new name: ", fg="red"))
    self.name = value
    return value

  def test_path(self, ctx: click.core.Context, param: click.core.Option,
      value: str) -> str:
    """Saving the path to the test file.

    Args:
      ctx: the click context (automatically given via callback)
      param: the click command (automatically given via callback)
      value: the test file path (automatically given via callback)

    Returns: the test file path representing the same as the value
    """
    while not file_exists(value):
      value = click.prompt(
        click.style("File does not exists. Choose another: ", fg="red"))
    self.testfile = value
    return value

  def generate(self,template_path:str):
    """Generating the files.

    Args:
      template_path: the path to the template directory
    """
    generator = SqliteGenerator(self.path, self.name, self.testfile,
      lambda x: click.echo(x))
    if not generator.init_formatter_exists or not generator.init_parser_exists:
      click.confirm(
        'At least one init file does not exist. Do you want the create them ('
        'or else abort)?',
        abort=True, default=True)

    click.confirm('Do you want to generate the files?', abort=True,
      default=True)

    generator.generate_sqlite_plugin(FileHandler, template_path)
