# -*- coding: utf-8 -*-
"""Module representing the sqlite plugin generator"""
import os

from plasoscaffolder.bll.mappings.init_mapping import *
from plasoscaffolder.bll.services.file_handler import FileHandler
from plasoscaffolder.bll.services.sqlite_plugin_helper import *


class SqliteGenerator(object):
  """ Generator for SQLite Files """

  def __init__(self, path: os.path, name: str, database: os.path, output):
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
    self.init_formatter_exists = file_exists(
      formatter_init_file_path(self.path))
    self.init_parser_exists = file_exists(parser_init_file_path(self.path))
    self.output = output

  def generate_sqlite_plugin(self, fileHandler: FileHandler,
      template_path: str):
    """Generate the whole sqlite plugin

    Args:
      fileHandler: the Filehandler class
      template_path: the path to the template directory
    """

    file_handler = fileHandler()
    init_mapper = InitMapper(template_path)

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

    formatter_file = formatter_file_path(self.path, self.name)
    formatter = file_handler.create_file_from_path(formatter_file)
    parser = file(parser_file_path(self.path, self.name))
    formatter_test = file(formatter_test_file_path(self.path, self.name))
    parser_test = file(parser_test_file_path(self.path, self.name))
    database = copy(self.database, database_path(self.path, self.name))
    parser_init = edit(parser_init_file_path(self.path), content_init_parser)
    formatter_init = edit(formatter_init_file_path(self.path),
      content_init_formatter)

    self._print(formatter, parser, formatter_test, parser_test, database,
      parser_init, formatter_init)

  def _print(self, formatter: os.path, parser: os.path, formatter_test: os.path,
      parser_test: os.path, database: os.path, parser_init: os.path,
      formatter_init: os.path):
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

  def _print_copy(self, file: os.path):
    """Click echo for copy file

    Args:
      file: the file path
    """

    self.output("copy " + file)

  def _print_edit(self, file: os.path):
    """Click echo for edit file

    Args:
      file: the file path
    """
    self.output("edit " + file)

  def _print_create(self, file: os.path):
    """Click echo for create file

    Args:
      file: the file path
    """
    self.output("create " + file)
