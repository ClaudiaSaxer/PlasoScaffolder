# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from plasoscaffolder.bll.services.file_handler import FileHandler
from plasoscaffolder.bll.services.sqlite_plugin_helper import *


class BaseSqliteGenerator(metaclass=ABCMeta):
  """Class representing the base class for the base sqlite generator"""

  @abstractmethod
  def generate_sqlite_plugin(self, fileHandler: FileHandler,
      template_path: str):
    """Generate the whole sqlite plugin

    Args:
      fileHandler: the Filehandler class
      template_path: the path to the template directory
    """
    pass

  @abstractmethod
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
    pass

  @abstractmethod
  def _print_copy(self, file: os.path):
    """Click echo for copy file

    Args:
      file: the file path
    """
    pass

  @abstractmethod
  def _print_edit(self, file: os.path):
    """Click echo for edit file

    Args:
      file: the file path
    """
    pass

  @abstractmethod
  def _print_create(self, file: os.path):
    """Click echo for create file

    Args:
      file: the file path
    """
    pass
