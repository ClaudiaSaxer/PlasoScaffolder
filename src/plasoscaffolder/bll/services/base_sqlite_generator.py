# -*- coding: utf-8 -*-
"""Baseclass for a Generator for Sqlite"""
import abc
import os

from plasoscaffolder.bll.mappings import base_formatter_mapping
from plasoscaffolder.bll.mappings import base_init_mapping
from plasoscaffolder.bll.mappings import base_mapping_helper
from plasoscaffolder.bll.mappings import base_parser_mapping
from plasoscaffolder.common import base_file_handler
from plasoscaffolder.dal import base_database_information


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
      mappingHelper: base_mapping_helper.BaseMappingHelper,
      database_information: base_database_information.BaseDatabaseInformation):
    """Generate the whole sqlite plugin.

    Args:
      template_path (str): the path to the template directory
      fileHandler (FileHandler): the handler for the file
      init_mapper (BaseInitMapper): the init mapper
      parser_mapper (BaseParserMapper): the parser mapper
      formatter_mapper (BaseFormatterMapper): the mapper for the formatter
      mappingHelper (BaseMappingHelper): the mapping helper
      database_information (BaseDatabaseInformation): helper class for
      information about the database
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
