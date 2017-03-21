# -*- coding: utf-8 -*-
"""Base class for sqlite plugin __path __helper"""
import abc

class BaseSQLitePluginPathHelper(object):
  """Class representing the base class for the sqlite plugin __path __helper"""
  __metaclass__ = abc.ABCMeta

  def __init__(self):
    """Initializes the sqlite plugin halper."""
    super().__init__()
    self.formatter_file_path = None
    self.parser_file_path = None
    self.formatter_test_file_path = None
    self.parser_test_file_path = None
    self.database_path = None
    self.parser_init_file_path = None
    self.formatter_init_file_path = None
