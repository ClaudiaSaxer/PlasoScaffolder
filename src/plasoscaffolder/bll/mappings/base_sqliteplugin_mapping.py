# -*- coding: utf-8 -*-
"""Base class for mapper of formatter."""
import abc

from plasoscaffolder.model import base_data_model


class BaseSQLitePluginMapper(object):
  """Class representing the parser mapper."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetRenderedTemplate(
      self,
      data: base_data_model.BaseDataModel) -> str:
    """Retrieves the formatter.

    Args:
      data (base_data_model.BaseDataModel): the data for template

    Returns:
      str: the rendered template
    """
