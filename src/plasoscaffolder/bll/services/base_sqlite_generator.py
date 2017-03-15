# -*- coding: utf-8 -*-
import abc
import os

from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper
from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSQLitePluginPathHelper
from plasoscaffolder.bll.services.sqlite_plugin_helper import \
  BaseSQLitePluginHelper
from plasoscaffolder.common.base_file_handler import BaseFileHandler
from plasoscaffolder.common.base_output_handler import BaseOutputHandler
from plasoscaffolder.common.file_handler import FileHandler


class BaseSQLiteGenerator(object):
  """Class representing the base class for the base sqlite generator."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
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

  @abc.abstractmethod
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

  @abc.abstractmethod
  def _print_copy(self, file: str):
    """Print for copy file.

    Args:
      file (str): the file path
    """

  @abc.abstractmethod
  def _print_edit(self, file: str):
    """print for edit file.

    Args:
      file (str): the file path
    """

  @abc.abstractmethod
  def _print_create(self, file: os.path):
    """print for create file.

    Args:
      file (str): the file path
    """
