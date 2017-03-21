# -*- coding: utf-8 -*-
"""File representing the Controller for SQLite plugin."""
import click

from plasoscaffolder.bll.mappings import formatter_mapping
from plasoscaffolder.bll.mappings import init_mapping
from plasoscaffolder.bll.mappings import mapping_helper
from plasoscaffolder.bll.mappings import parser_mapping
from plasoscaffolder.bll.services import sqlite_generator
from plasoscaffolder.bll.services import sqlite_plugin_helper
from plasoscaffolder.bll.services import sqlite_plugin_path_helper
from plasoscaffolder.common import base_output_handler
from plasoscaffolder.common import file_handler
from plasoscaffolder.common import output_handler_click


class SQLiteController(object):
  """Class representing the Controller for the SQLite Controller."""

  def __init__(self, output_handler: base_output_handler.BaseOutputHandler):
    super(SQLiteController, self).__init__()
    self.path = None
    self.name = None
    self.testfile = None
    self.events = None
    self.plugin_helper = sqlite_plugin_helper.SQLitePluginHelper()
    self.output_handler = output_handler

  def SourcePath(self, _ctx: click.core.Context, _param: click.core.Option,
                 value: str) -> str:
    """Saving the source path.

    Args:
      ctx (click.core.Context): the click context (automatically given via
      callback)
      param (click.core.Option): the click command (automatically given via
      callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the source path representing the same as value
    """
    while not self.plugin_helper.FolderExists(value):
      value = self.output_handler.PromptError(
          'Folder does not exists. Enter correct one: ')
    self.path = value
    return value

  def PluginName(self, _ctx: click.core.Context, _param: click.core.Option,
                 value: str) -> str:
    """Saving the plugin name.

    Args:
      ctx (click.core.Context): the click context (automatically given via
      callback)
      param (click.core.Option): the click command (automatically given via
      callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the plugin name representing the same as value
    """
    value = self._ValidatePluginName(value)
    while self.plugin_helper.PluginExists(
        self.path, value,
        sqlite_plugin_path_helper.SQLitePluginPathHelper):
      value = self.output_handler.PromptError(
          'Plugin exists. Choose new name: ')
      value = self._ValidatePluginName(value)

    self.name = value
    return value

  def TestPath(self, _ctx: click.core.Context, _param: click.core.Option,
               value: str) -> str:
    """Saving the path to the test file.

    Args:
      ctx (click.core.Context): the click context (automatically given via
      callback)
      param (click.core.Option): the click command (automatically given via
      callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the test file path representing the same as the value
    """
    while not self.plugin_helper.FileExists(value):
      value = self.output_handler.PromptError(
          'File does not exists. Choose another: ')
    self.testfile = value
    return value

  def Event(self, _ctx: click.core.Context, _param: click.core.Option,
            value: str) -> str:
    """The events of the plugin

    Args:
      ctx (click.core.Context): the click context (automatically given via
      callback)
      param (click.core.Option): the click command (automatically given via
      callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the events of the plugin
    """
    self.events = value.title().split()
    return self.events

  def Generate(self, template_path: str):
    """Generating the files.

    Args:
      template_path (str): the path to the template directory
    """
    generator = sqlite_generator.SQLiteGenerator(
        self.path,
        self.name,
        self.testfile,
        self.events,
        output_handler_click.OutputHandlerClick(),
        sqlite_plugin_helper.SQLitePluginHelper,
        sqlite_plugin_path_helper.SQLitePluginPathHelper)

    self.output_handler.Confirm('Do you want to Generate the files?')

    generator.GenerateSQLitePlugin(template_path, file_handler.FileHandler,
                                   init_mapping.InitMapper,
                                   parser_mapping.ParserMapper,
                                   formatter_mapping.FormatterMapper,
                                   mapping_helper.MappingHelper)

  def _ValidatePluginName(self, plugin_name: str) -> str:
    """Validate plugin name and prompt until name is valid

    Args:
      plugin_name: the name of the plugin

    Returns:
      a valid plugin name
    """
    while not self.plugin_helper.IsValidPluginName(plugin_name):
      plugin_name = self.output_handler.PromptError(
          'Plugin is not in a valide format. Choose new name ['
          'plugin_name_...]: ')
    return plugin_name
