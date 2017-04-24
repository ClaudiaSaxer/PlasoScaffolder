# -*- coding: utf-8 -*-
"""Base class for mapper for test parser file."""
import abc

from plasoscaffolder.model import parser_test_data_model


class BaseParserTestMapper(object):
  """The parser test mapper base class."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetParserTest(
      self,
      parser_test_data: parser_test_data_model.ParserTestDataModel) -> str:
    """Retrieves the test parser.

    Args:
      parser_test_data: the data for the parser test

    Returns:
      str: the rendered template
    """
