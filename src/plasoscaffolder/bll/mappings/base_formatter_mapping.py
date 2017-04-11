# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
import abc

from plasoscaffolder.model import formatter_data_model


class BaseFormatterMapper(object):
  """Class representing the parser mapper."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetFormatter(
      self,
      formatter_data: formatter_data_model.FormatterDataModel) -> str:
    """Retrieves the formatter.

    Args:
      formatter_data: the data for the formatter

    Returns:
      str: the rendered template
    """
