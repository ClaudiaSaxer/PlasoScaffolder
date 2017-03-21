# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
import abc


class BaseInitMapper(object):
  """Class representing Base class for the init mapper."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetFormatterInitCreate(self, plugin_name: str) -> str:
    """Renders formatter init if you want to create new init file.

    Args:
      plugin_name (str): __name of the plugin

    Returns:
      str: rendered template
    """

  @abc.abstractmethod
  def GetFormatterInitEdit(self, plugin_name: str) -> str:
    """Renders formatter init if you want to create new init file.

    Args:
      plugin_name (str): __name of the plugin

    Returns:
      str: the rendered template
    """

  @abc.abstractmethod
  def GetParserInitCreate(self, plugin_name: str) -> str:
    """Renders formatter init if you want to edit an existing init file.

    Args:
      plugin_name (str): __name of the plugin

    Returns:
      str: the rendered template
    """

  @abc.abstractmethod
  def GetParserInitEdit(self, plugin_name: str) -> str:
    """Renders parser init if you want to create new init file.

    Args:
      plugin_name (str): __name of the plugin

    Returns:
      str: the rendered template
    """

  @abc.abstractmethod
  def _RenderInit(self, file_name: str, plugin_name: str) -> str:
    """Renders parser init if you want to edit an existing init file.

    Args:
      file_name (str): __name of the file in the templates folder
      plugin_name(str): the __name of the plugin

    Returns:
      str: the rendered template
    """
