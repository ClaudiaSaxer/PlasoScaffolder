# -*- coding: utf-8 -*-
"""Sqlite Generator"""
import os

from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_init_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_parser_mapping
from plasoscaffolder.bll.services import base_sqlite_generator
from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper
from plasoscaffolder.common import base_file_handler
from plasoscaffolder.common import base_output_handler


class SQLiteGenerator(base_sqlite_generator.BaseSQLiteGenerator):
  """ Generator for SQLite Files """

  def __init__(
      self, path: str, name: str, database: str, events: list,
      output_handler: base_output_handler.BaseOutputHandler,
      pluginHelper: base_sqlite_plugin_helper.BaseSQLitePluginHelper,
      pathHelper=base_sqlite_plugin_path_helper.BaseSQLitePluginPathHelper):
    """Initializes a SQLite Generator.

    Args:
      path (str): the path of the plaso folder
      name (str): the name of the plugin
      database (str): the path to the database
      events (list): the events of the plugin
      output_handler (BaseOutputHandler: the output handler for the
      generation information
      pluginHelper (BaseSQLitePluginHelper): the plugin helper
      pathHelper (BaseSQLitePluginPathHelper): the plugin path helper
    """
    super().__init__()
    database_suffix = os.path.splitext(database)[1]

    self.path = path
    self.name = name
    self.database = database

    self.path_helper = pathHelper(path, name, database_suffix)
    self.output = output_handler.PrintInfo
    self.plugin_helper = pluginHelper()
    self.events = events

    self.init_formatter_exists = self.plugin_helper.FileExists(
        self.path_helper.formatter_init_file_path)
    self.init_parser_exists = self.plugin_helper.FileExists(
        self.path_helper.parser_init_file_path)

  def GenerateSQLitePlugin(
      self,
      template_path: str,
      fileHandler: base_file_handler.BaseFileHandler,
      init_mapper: base_init_mapping.BaseInitMapper,
      parser_mapper: base_parser_mapping.BaseParserMapper,
      formatter_mapper: base_formatter_mapping.BaseFormatterMapper,
      mappingHelper: base_mapping_helper.BaseMappingHelper):

    """Generate the whole sqlite plugin.

    Args:
      formatter_mapper (BaseFormatterMapper): the mapper for the formatter
      fileHandler (FileHandler): the handler for the file
      mappingHelper (BaseMappingHelper): the mapping helper
      parser_mapper (BaseParserMapper): the parser mapper
      init_mapper (BaseInitMapper): the init mapper
      template_path (str): the path to the template directory
    """

    file_handler = fileHandler()
    init_mapper = init_mapper(template_path, mappingHelper)
    parser_mapper = parser_mapper(template_path, mappingHelper)
    formatter_mapper = formatter_mapper(template_path, mappingHelper)

    file = file_handler.CreateFileFromPath
    copy = file_handler.CopyFile
    edit = file_handler.AddContent

    if self.init_formatter_exists:
      content_init_formatter = init_mapper.GetFormatterInitEdit(self.name)
    else:
      content_init_formatter = init_mapper.GetFormatterInitCreate(self.name)

    if self.init_parser_exists:
      content_init_parser = init_mapper.GetParserInitEdit(self.name)
    else:
      content_init_parser = init_mapper.GetParserInitCreate(self.name)

    content_parser = parser_mapper.GetParser(self.name, self.events)
    content_formatter = formatter_mapper.GetFormatter(self.name, self.events)

    formatter = edit(self.path_helper.formatter_file_path, content_formatter)
    parser = edit(self.path_helper.parser_file_path, content_parser)
    formatter_test = file(self.path_helper.formatter_test_file_path)
    parser_test = file(self.path_helper.parser_test_file_path)
    database = copy(self.database, self.path_helper.database_path)
    parser_init = edit(self.path_helper.parser_init_file_path,
                       content_init_parser)
    formatter_init = edit(self.path_helper.formatter_init_file_path,
                          content_init_formatter)

    self._Print(formatter, parser, formatter_test, parser_test, database,
                parser_init, formatter_init)

  def _Print(
      self, formatter: str, parser: str, formatter_test: str,
      parser_test: str, database: str, parser_init: str,
      formatter_init: str):
    """Printing the information to the generated files.

    Args:
      formatter (str): the formatter file
      parser(str): the parser file
      formatter_test(str): the formatter test file
      parser_test(str): the parser test file
      database(str): the database file
      parser_init(str): the parser init file
      formatter_init(str): the formatter init file
    """
    self._PrintCreate(formatter)
    self._PrintCreate(parser)
    self._PrintCreate(formatter_test)
    self._PrintCreate(parser_test)
    self._PrintCopy(database)
    if self.init_parser_exists:
      self._PrintEdit(parser_init)
    else:
      self._PrintCreate(parser_init)
    if self.init_formatter_exists:
      self._PrintEdit(formatter_init)
    else:
      self._PrintCreate(formatter_init)

  def _PrintCopy(self, file: str):
    """Print for copy file.

    Args:
      file (str): the file path
    """
    self.output('copy ' + file)

  def _PrintEdit(self, file: str):
    """Print for edit file.

    Args:
      file (str): the file path
    """
    self.output('edit ' + file)

  def _PrintCreate(self, file: str):
    """Print for create file.

    Args:
      file (str): the file path
    """
    self.output('create ' + file)
