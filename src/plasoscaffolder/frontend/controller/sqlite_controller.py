# -*- coding: utf-8 -*-
"""File representing the controller for SQLite plugin."""
import click
from plasoscaffolder.bll.mappings.init_mapping import InitMapper
from plasoscaffolder.bll.mappings.mapping_helper import MappingHelper
from plasoscaffolder.bll.services.sqlite_generator import SqliteGenerator
from plasoscaffolder.bll.services.sqlite_plugin_helper import SqlitePluginHelper
from plasoscaffolder.bll.services.sqlite_plugin_path_helper import \
  SqlitePluginPathHelper
from plasoscaffolder.common.base_output_handler import BaseOutputHandler
from plasoscaffolder.common.file_handler import FileHandler


class SqliteController(object):
  """Class representing the controller for the SQLite controller."""

  def __init__(self, outputHandler: BaseOutputHandler):
    super(SqliteController, self).__init__()
    self.path = None
    self.name = None
    self.testfile = None
    self.plugin_helper = SqlitePluginHelper()
    self.output_handler = outputHandler()

  def source_path(self, ctx: click.core.Context, param: click.core.Option,
      value: str) -> str:
    """Saving the source path.

    Args:
      ctx (click.core.Context): the click context (automatically given via callback)
      param (click.core.Option): the click command (automatically given via callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the source path representing the same as value
    """
    while not self.plugin_helper.folder_exists(value):
      value = self.output_handler.prompt_error(
        'Folder does not exists. Enter correct one: ')
    self.path = value
    return value

  def plugin_name(self, ctx: click.core.Context, param: click.core.Option,
      value: str) -> str:
    """Saving the plugin name.

    Args:
      ctx (click.core.Context): the click context (automatically given via callback)
      param (click.core.Option): the click command (automatically given via callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the plugin name representing the same as value
    """
    while self.plugin_helper.plugin_exists(self.path, value,
        SqlitePluginPathHelper):
      value = self.output_handler.prompt_error(
        'Plugin exists. Choose new name: ')
    self.name = value
    return value

  def test_path(self, ctx: click.core.Context, param: click.core.Option,
      value: str) -> str:
    """Saving the path to the test file.

    Args:
      ctx (click.core.Context): the click context (automatically given via callback)
      param (click.core.Option): the click command (automatically given via callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the test file path representing the same as the value
    """
    while not self.plugin_helper.file_exists(value):
      value = self.output_handler.prompt_error(
        'File does not exists. Choose another: ')
    self.testfile = value
    return value

  def generate(self, template_path: str):
    """Generating the files.

    Args:
      template_path (str): the path to the template directory
    """
    generator = SqliteGenerator(self.path, self.name, self.testfile,
      lambda x: self.output_handler.print_info(
        x), SqlitePluginHelper, SqlitePluginPathHelper)

    if not generator.init_formatter_exists or not generator.init_parser_exists:
      self.output_handler.confirm(
        'At least one init file does not exist. Do you want the create them ( '
        'or else abort)?')

    self.output_handler.confirm('Do you want to generate the files?')

    generator.generate_sqlite_plugin(template_path, FileHandler, InitMapper,
      MappingHelper)
