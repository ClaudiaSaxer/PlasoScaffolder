# -*- coding: utf-8 -*-
"""Module representing the sqlite plugin generator"""
from plasoscaffolder.bll.services.file_handler import *
from plasoscaffolder.bll.services.sqlite_plugin_helper import *
import click


class SqliteGenerator():
  """ Generator for SQLite Files """

  def __init__(self, path, name, database):
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

  def generate_sqlite_plugin(self):
    creator = FileHandler()

    file = creator.create_file_from_path
    copy = creator.copy_file
    edit = creator.add_content

    content_init_formatter = "from plaso.formatters import " + self.name
    content_init_parser = "from plaso.parsers.sqlite_plugins import " + \
                          self.name

    formatter = file(formatter_file_path(self.path, self.name))
    parser = file(parser_file_path(self.path, self.name))
    formatter_test = file(formatter_test_file_path(self.path, self.name))
    parser_test = file(parser_test_file_path(self.path, self.name))
    database = copy(self.database, database_path(self.path, self.name))
    parser_init = edit(parser_init_file_path(self.path), content_init_parser,
      self.init_parser_exists)
    formatter_init = edit(formatter_init_file_path(self.path),
      content_init_formatter,
      self.init_formatter_exists)

    self.__print(formatter, parser, formatter_test, parser_test, database,
      parser_init, formatter_init)

  def __print(self,formatter, parser, formatter_test, parser_test, database,
      parser_init, formatter_init):
    self.__print_create(formatter)
    self.__print_create(parser)
    self.__print_create(formatter_test)
    self.__print_create(parser_test)
    self.__print_copy(database)
    if self.init_parser_exists:
      self.__print_edit(parser_init)
    else:
      self.__print_create(parser_init)
    if self.init_formatter_exists:
      self.__print_edit(formatter_init)
    else:
      self.__print_create(formatter_init)

  @staticmethod
  def __print_copy(file):
    """
    Click echo for copy file
    :param file: the file path
    """
    click.echo("copy " + file)

  @staticmethod
  def __print_edit(file):
    """
    Click echo for edit file
    :param file: the file path
    """
    click.echo("edit " + file)

  @staticmethod
  def __print_create(file):
    """
    Click echo for create file
    :param file: the file path
    """
    click.echo("create " + file)
