# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
import abc


class BaseFormatterMapper(object):
  """Class representing the parser mapper."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetFormatter(self, plugin_name: str, events: list) -> str:
    """Renders the formatter.

    Args:
      plugin_name (str): the Name of the plugin
      events (list): the list of the events

    Returns:
      str: the rendered template
    """
