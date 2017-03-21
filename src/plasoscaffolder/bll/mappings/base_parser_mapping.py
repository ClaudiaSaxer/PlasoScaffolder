# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
import abc


class BaseParserMapper(object):
  """The parser mapper base class."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetParser(self, plugin_name: str, events: list) -> str:
    """Renders the parser.

    Args:
      plugin_name (str): the __name of the plugin
      events (list): the list of the __events

    Returns:
      str: the rendered template
    """
