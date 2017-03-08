# -*- coding: utf-8 -*-
"""Module representing the sqlite plugin generator"""
from plasoscaffolder.bll.mappings.init_formatter_mapping import *
from plasoscaffolder.bll.services.sqlite_plugin_helper import *


class SqliteGenerator():
  """ Generator for SQLite Files """

  def __init__(self, path, name, database, output):
    """ Constructs the SQLite Generator

    :param path: the path of the plaso folder
    :param name: the name of the plugin
    :param database: the path to the database
    """
    self.path = path
    self.name = name
    self.database = database
    self.init_formatter_exists = file_exists(
      formatter_init_file_path(self.path))
    self.init_parser_exists = file_exists(parser_init_file_path(self.path))
    self.output = output

  def generate_sqlite_plugin(self, fileHandler):
    file_handler = fileHandler()

    file = file_handler.create_file_from_path
    copy = file_handler.copy_file
    edit = file_handler.add_content

    content_init_formatter = "from plaso.formatters import " + self.name
    content_init_parser = get_formatter_init_edit(
      self.name) if self.init_parser_exists \
      else get_formatter_init_create(
      self.name)

    formatter = file(formatter_file_path(self.path, self.name))
    parser = file(parser_file_path(self.path, self.name))
    formatter_test = file(formatter_test_file_path(self.path, self.name))
    parser_test = file(parser_test_file_path(self.path, self.name))
    database = copy(self.database, database_path(self.path, self.name))
    parser_init = edit(parser_init_file_path(self.path), content_init_parser)
    formatter_init = edit(formatter_init_file_path(self.path),
      content_init_formatter)

    self._print(formatter, parser, formatter_test, parser_test, database,
      parser_init, formatter_init)

  def _print(self, formatter, parser, formatter_test, parser_test, database,
      parser_init, formatter_init):
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

  def _print_copy(self, file):
    """
    Click echo for copy file
    :param file: the file path
    """
    self.output("copy " + file)

  def _print_edit(self, file):
    """
    Click echo for edit file
    :param file: the file path
    """
    self.output("edit " + file)

  def _print_create(self, file):
    """
    Click echo for create file
    :param file: the file path
    """
    self.output("create " + file)
