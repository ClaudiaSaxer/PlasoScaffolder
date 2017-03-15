# -*- coding: utf-8 -*-
import os

from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper
from plasoscaffolder.bll.services.base_sqlite_generator import \
  BaseSQLiteGenerator
from plasoscaffolder.bll.services.base_sqlite_generator import \
  BaseSQLitePluginHelper
from plasoscaffolder.bll.services.base_sqlite_generator import \
  BaseSQLitePluginPathHelper
from plasoscaffolder.common.base_file_handler import BaseFileHandler
from plasoscaffolder.common.base_output_handler import BaseOutputHandler


class SQLiteGenerator(BaseSQLiteGenerator):
  """ Generator for SQLite Files """

  def __init__(self, path: str, name: str, database: str,
      output_handler: BaseOutputHandler,
      pluginHelper: BaseSQLitePluginHelper,
      pathHelper=BaseSQLitePluginPathHelper):
    """Initializes a SQLite Generator.

    Args:
      path (str): the path of the plaso folder
      name (str): the name of the plugin
      database (str): the path to the database
      output_handler (BaseOutputHandler: the output handler for the
      generation information
      pluginHelper (BaseSQLitePluginHelper): the plugin helper
      pathHelper (BaseSQLitePluginPathHelper): the plugin path helper
    """
    super().__init__()
    self.path = path
    self.name = name
    self.database = database
    self.path_helper = pathHelper(path, name)
    self.output = output_handler.print_info
    self.plugin_helper = pluginHelper()

    self.init_formatter_exists = self.plugin_helper.file_exists(
      self.path_helper.formatter_init_file_path())
    self.init_parser_exists = self.plugin_helper.file_exists(
      self.path_helper.parser_init_file_path())

  def generate_sqlite_plugin(self, template_path: str,
      fileHandler: BaseFileHandler, init_mapper: BaseInitMapper,
      mappingHelper: BaseMappingHelper):
    """Generate the whole sqlite plugin.

    Args:
      fileHandler (FileHandler): the Filehandler class
      mappingHelper (BaseMappingHelper): the mapping helper
      init_mapper (BaseInitMapper): the init mapper
      template_path (str): the path to the template directory
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
    database = copy(self.database,
      self.path_helper.database_path(os.path.splitext(self.database)[1]))
    parser_init = edit(self.path_helper.parser_init_file_path(),
      content_init_parser)
    formatter_init = edit(self.path_helper.formatter_init_file_path(),
      content_init_formatter)

    self._print(formatter, parser, formatter_test, parser_test, database,
      parser_init, formatter_init)

  def _print(self, formatter: str, parser: str, formatter_test: str,
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
    """Print for copy file.

    Args:
      file (str): the file path
    """
    self.output('copy ' + file)

  def _print_edit(self, file: str):
    """Print for edit file.

    Args:
      file (str): the file path
    """
    self.output('edit ' + file)

  def _print_create(self, file: str):
    """Print for create file.

    Args:
      file (str): the file path
    """
    self.output('create ' + file)
