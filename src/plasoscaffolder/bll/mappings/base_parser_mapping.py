# -*- coding: utf-8 -*-
""" Base class for mapper for parser file. """
import abc

from plasoscaffolder.model import parser_data_model


class BaseParserMapper(object):
  """The parser mapper base class."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetParser(self, parser_data: parser_data_model.ParserDataModel) -> str:
    """Retrieves the parser.

    Args:
      parser_data: the data for the parser

    Returns:
      str: the rendered template
    """
