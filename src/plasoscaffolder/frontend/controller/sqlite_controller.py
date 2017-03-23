# -*- coding: utf-8 -*-
"""File representing the Controller for SQLite plugin."""
import os

import click
from plasoscaffolder.bll.mappings import formatter_mapping
from plasoscaffolder.bll.mappings import init_mapping
from plasoscaffolder.bll.mappings import mapping_helper
from plasoscaffolder.bll.mappings import parser_mapping
from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.bll.services import sqlite_generator
from plasoscaffolder.bll.services import sqlite_plugin_helper
from plasoscaffolder.bll.services import sqlite_plugin_path_helper
from plasoscaffolder.common import base_output_handler
from plasoscaffolder.common import file_handler
from plasoscaffolder.model import event_model
from plasoscaffolder.model import sql_query_model


class SQLiteController(object):
  """Class representing the SQLite Controller."""

  def __init__(self, output_handler: base_output_handler.BaseOutputHandler(),
               plugin_helper: base_sqlite_plugin_helper.BaseSQLitePluginHelper):
    """
    Initializes the SQLite Controller
    Args:
      output_handler (BaseOutputHandler): the handler for the output
      plugin_helper (BaseSQLitePluginHelper): the helper for the SQLite plugin
    """
    super(SQLiteController, self).__init__()
    self._path = None
    self._name = None
    self._testfile = None
    self._events = None
    self._sql_query = None
    self._plugin_helper = plugin_helper
    self._output_handler = output_handler

  def SourcePath(self, unused_ctx: click.core.Context,
                 unused_param: click.core.Option,
                 value: str) -> str:
    """Saving the source path.

    Args:
      unused_ctx (click.core.Context): the click context (automatically given
      via
      callback)
      unused_param (click.core.Option): the click command (automatically
      given via
      callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the source path representing the same as value
    """
    while not self._plugin_helper.FolderExists(value):
      value = self._output_handler.PromptError(
          'Folder does not exists. Enter correct one: ')
    self._path = value
    return value

  def PluginName(self, unused_ctx: click.core.Context,
                 unused_param: click.core.Option,
                 value: str) -> str:
    """Saving the plugin_name.

    Args:
      unused_ctx (click.core.Context): the click context (automatically given
      via
      callback)
      unused_param (click.core.Option): the click command (automatically
      given via
      callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the plugin __name representing the same as value
    """
    value = self._ValidatePluginName(value)
    while self._plugin_helper.PluginExists(
        self._path, value, "",
        sqlite_plugin_path_helper.SQLitePluginPathHelper(
            self._path, value, "")):
      value = self._output_handler.PromptError(
          'Plugin exists. Choose new name: ')
      value = self._ValidatePluginName(value)

    self._name = value
    return value

  def TestPath(self, unused_ctx: click.core.Context,
               unused_param: click.core.Option,
               value: str) -> str:
    """Saving the path to the test file.

    Args:
      unused_ctx (click.core.Context): the click context (automatically given
      via
      callback)
      unused_param (click.core.Option): the click command (automatically
      given via
      callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the test file path representing the same as the value
    """
    while not self._plugin_helper.FileExists(value):
      value = self._output_handler.PromptError(
          'File does not exists. Choose another: ')
    self._testfile = value
    return value

  def Event(self, unused_ctx: click.core.Context,
            unused_param: click.core.Option,
            value: str) -> str:
    """The events of the plugin

    Args:
      unused_ctx (click.core.Context): the click context (automatically given
      via
      callback)
      unused_param (click.core.Option): the click command (automatically
      given via
      callback)
      value (str): the source path (automatically given via callback)

    Returns:
      str: the events of the plugin
    """
    event_model_list = []
    for event_name in value.title().split():
      event_model_list.append(self._CreateEventModelWithUserInput(event_name))
    self._events = event_model_list

    return event_model_list

  def SQLQuery(self, unused_ctx: click.core.Context,
               unused_param: click.core.Option,
               value: str) -> str:
    """The events of the plugin

    Args:
      unused_ctx (click.core.Context): the click context (automatically given
      via
      callback)
      unused_param (click.core.Option): the click command (automatically
      given via
      callback)
      value (str): the sql query (automatically given via callback)

    Returns:
      str: the sql query
    """
    sql_query_list = []
    for query in value.split(' | '):
      sql_query_list.append(self._CreateSQLQueryModelWithUserInput(query))
    self._sql_query = sql_query_list
    return sql_query_list

  def _CreateSQLQueryModelWithUserInput(
      self,
      query: str) -> sql_query_model.SQLQueryModel:
    """Asks the user information about the sql query

    Args:
      query (str): the sql query

    Returns:
      (sql_query_model.SQLQueryModel) a sql query model
    """
    message = 'What kind of row does this SQL query parse? Query: {0}'.format(
        query)
    name = self._output_handler.PromptInfo(text=message)
    whole_name = 'Parse{0}Row'.format(name.title())
    return sql_query_model.SQLQueryModel(query, whole_name)

  def _CreateEventModelWithUserInput(self, name: str) -> event_model.EventModel:
    """Asks the user if the event needs customizing

    Args:
      name (str): the name of the event

    Returns:
      (event_model.EventModel): a event model
    """
    message = 'Does the event {0} need customizing?'.format(name)
    needs_customizing = self._output_handler.Confirm(
        text=message, abort=False, default=False)
    return event_model.EventModel(name, needs_customizing)

  def Generate(self, template_path: str):
    """Generating the files.

    Args:
      template_path (str): the path to the template directory
    """
    self._output_handler.Confirm('Do you want to Generate the files?')

    database_suffix = os.path.splitext(self._testfile)[1][1:]
    helper = mapping_helper.MappingHelper(template_path)

    generator = sqlite_generator.SQLiteGenerator(
        self._path,
        self._name,
        self._testfile,
        self._events,
        self._output_handler,
        sqlite_plugin_helper.SQLitePluginHelper(),
        sqlite_plugin_path_helper.SQLitePluginPathHelper(
            self._path, self._name, database_suffix))

    generator.GenerateSQLitePlugin(
        template_path, file_handler.FileHandler(),
        init_mapping.InitMapper(helper),
        parser_mapping.ParserMapper(helper),
        formatter_mapping.FormatterMapper(helper),
        mapping_helper.MappingHelper(template_path))

  def _ValidatePluginName(self, plugin_name: str) -> str:
    """Validate plugin name and prompt until name is valid

    Args:
      plugin_name: the name of the plugin

    Returns:
      a valid plugin name
    """
    while not self._plugin_helper.IsValidPluginName(plugin_name):
      plugin_name = self._output_handler.PromptError(
          'Plugin is not in a valide format. Choose new name ['
          'plugin_name_...]: ')
    return plugin_name
