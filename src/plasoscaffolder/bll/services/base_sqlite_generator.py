# -*- coding: utf-8 -*-
"""Baseclass for Generator for Sqlite"""
import abc
import os

from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_init_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_parser_mapping
from plasoscaffolder.common import base_file_handler


class BaseSQLiteGenerator(object):
  """Class representing the base class for the base sqlite generator."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
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
      mappingHelper (BaseMappingHelper): the mapping __helper
      parser_mapper (BaseParserMapper): the parser mapper
      init_mapper (BaseInitMapper): the init mapper
      template_path (str): the __path to the template directory
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
      file (str): the file __path
    """

  @abc.abstractmethod
  def _PrintEdit(self, file: str):
    """print for edit file.

    Args:
      file (str): the file __path
    """

  @abc.abstractmethod
  def _PrintCreate(self, file: os.path):
    """print for create file.

    Args:
      file (str): the file __path
    """
