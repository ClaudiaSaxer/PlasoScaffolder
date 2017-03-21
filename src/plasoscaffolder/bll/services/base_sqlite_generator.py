# -*- coding: utf-8 -*-
"""Baseclass for Generator for Sqlite"""
import abc
import os

from plasoscaffolder.bll.mappings.base_formatter_mapping import \
  BaseFormatterMapper
from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.mappings.base_mapping_helper import BaseMappingHelper
from plasoscaffolder.bll.mappings.base_parser_mapping import BaseParserMapper
from plasoscaffolder.common.base_file_handler import BaseFileHandler


class BaseSQLiteGenerator(object):
  """Class representing the base class for the base sqlite generator."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GenerateSQLitePlugin(self, template_path: str,
                             fileHandler: BaseFileHandler,
                             init_mapper: BaseInitMapper,
                             parser_mapper: BaseParserMapper,
                             formatter_mapper: BaseFormatterMapper,
                             mappingHelper: BaseMappingHelper):
    """Generate the whole sqlite plugin.

    Args:
      formatter_mapper (BaseFormatterMapper): the mapper for the formatter
      fileHandler (FileHandler): the handler for the file
      mappingHelper (BaseMappingHelper): the mapping helper
      parser_mapper (BaseParserMapper): the parser mapper
      init_mapper (BaseInitMapper): the init mapper
      template_path (str): the path to the template directory
    """

  @abc.abstractmethod
  def _Print(self, formatter: str, parser: str, formatter_test: str,
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
  def _PrintCopy(self, file: str):
    """Print for copy file.

    Args:
      file (str): the file path
    """

  @abc.abstractmethod
  def _PrintEdit(self, file: str):
    """print for edit file.

    Args:
      file (str): the file path
    """

  @abc.abstractmethod
  def _PrintCreate(self, file: os.path):
    """print for create file.

    Args:
      file (str): the file path
    """
