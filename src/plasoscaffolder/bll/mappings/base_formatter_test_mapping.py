# -*- coding: utf-8 -*-
"""Base class of mapper for formatter test file."""
import abc

from plasoscaffolder.model import formatter_data_model


class BaseFormatterTestMapper(object):
  """Class representing the parser mapper."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetFormatterTest(
      self,
      formatter_test_data: formatter_data_model.FormatterDataModel) -> str:
    """Retrieves the formatter.

    Args:
      formatter_test_data (formatter_data_model.FormatterDataModel): the data
          for the formatter test

    Returns:
      str: the rendered template
    """
