# -*- coding: utf-8 -*-
"""Module representing the sqlite plugin generator"""
import os

from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper
from plasoscaffolder.bll.services.base_file_handler import BaseFileHandler
from plasoscaffolder.bll.services.base_sqlite_generator import \
  BaseSqliteGenerator, BaseSqlitePluginHelper, BaseSqlitePluginPathHelper


class SqliteGenerator(BaseSqliteGenerator):
  """ Generator for SQLite Files """

  def __init__(self, path: os.path, name: str, database: str, output,
      pluginHelper: BaseSqlitePluginHelper, pathHelper=BaseSqlitePluginPathHelper):
    """Initializes a SQLite Generator.

    Args:
      path: the path of the plaso folder
      name: the name of the plugin
      database: the path to the database
      output: the output for the generation information (str -> y)
    """
    self.path = path
    self.name = name
    self.database = database
    path_helper = pathHelper(path, name)
    helper = pluginHelper()
    self.init_formatter_exists = helper.file_exists(
      path_helper.formatter_init_file_path())
    self.init_parser_exists = helper.file_exists(
      path_helper.parser_init_file_path())
    self.output = output
    self.path_helper = path_helper

  def generate_sqlite_plugin(self, template_path: str,
      fileHandler: BaseFileHandler, init_mapper: BaseInitMapper, mappingHelper: BaseMappingHelper):
    """Generate the whole sqlite plugin

    Args:
      template_path: the path to the template directory
      fileHandler: the file handler
      init_mapper: the init mapper
    """

    file_handler = fileHandler()
    init_mapper = init_mapper(template_path, mappingHelper)

    file = file_handler.create_file_from_path
    copy = file_handler.copy_file
    edit = file_handler.add_content

    if self.init_formatter_exists:
      content_init_formatter = init_mapper.get_formatter_init_edit(self.name)
    else:
      content_init_formatter = init_mapper.get_formatter_init_create(self.name)

    if self.init_parser_exists:
      content_init_parser = init_mapper.get_parser_init_edit(self.name)
    else:
      content_init_parser = init_mapper.get_parser_init_create(self.name)

    formatter_file = self.path_helper.formatter_file_path()
    formatter = file_handler.create_file_from_path(formatter_file)
    parser = file(self.path_helper.parser_file_path())
    formatter_test = file(self.path_helper.formatter_test_file_path())
    parser_test = file(self.path_helper.parser_test_file_path())
    database = copy(self.database, self.path_helper.database_path())
    parser_init = edit(self.path_helper.parser_init_file_path(),
      content_init_parser)
    formatter_init = edit(self.path_helper.formatter_init_file_path(),
      content_init_formatter)

    self._print(formatter, parser, formatter_test, parser_test, database,
      parser_init, formatter_init)

  def _print(self, formatter: str, parser: str, formatter_test: str,
      parser_test: str, database: str, parser_init: str,
      formatter_init: str):
    """Printing the information to the generated files

    Args:
      formatter: the formatter file
      parser: the parser file
      formatter_test: the formatter test file
      parser_test: the parser test file
      database: the database file
      parser_init: the parser init file
      formatter_init: the formatter init file
    """
    self._print_create(formatter)
    self._print_create(parser)
    self._print_create(formatter_test)
    self._print_create(parser_test)
    self._print_copy(database)
    if self.init_parser_exists:
      self._print_edit(parser_init)
    else:
      self._print_create(parser_init)
    if self.init_formatter_exists:
      self._print_edit(formatter_init)
    else:
      self._print_create(formatter_init)

  def _print_copy(self, file: str):
    """Click echo for copy file

    Args:
      file: the file path
    """

    self.output("copy " + file)

  def _print_edit(self, file: str):
    """Click echo for edit file

    Args:
      file: the file path
    """
    self.output("edit " + file)

  def _print_create(self, file: str):
    """Click echo for create file

    Args:
      file: the file path
    """
    self.output("create " + file)
