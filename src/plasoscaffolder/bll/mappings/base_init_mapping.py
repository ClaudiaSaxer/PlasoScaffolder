# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
from abc import ABCMeta
from abc import abstractmethod


class BaseInitMapper(metaclass=ABCMeta):
  """Class representing Base class for the init mapper."""

  @abstractmethod
  def get_formatter_init_create(self, plugin_name: str) -> str:
    """Renders formatter init if you want to create new init file.

    Args:
      plugin_name (str): name of the plugin

    Returns:
      str: rendered template
    """

  @abstractmethod
  def get_formatter_init_edit(self, plugin_name: str) -> str:
    """Renders formatter init if you want to create new init file.

    Args:
      plugin_name (str): name of the plugin

    Returns:
      str: the rendered template
    """

  @abstractmethod
  def get_parser_init_create(self, plugin_name: str) -> str:
    """Renders formatter init if you want to edit an existing init file.

    Args:
      plugin_name (str): name of the plugin

    Returns:
      str: the rendered template
    """

  @abstractmethod
  def get_parser_init_edit(self, plugin_name: str) -> str:
    """Renders parser init if you want to create new init file.

    Args:
      plugin_name (str): name of the plugin

    Returns:
      str: the rendered template
    """

  @abstractmethod
  def _render_init(self, file_name: str, plugin_name: str) -> str:
    """Renders parser init if you want to edit an existing init file.

    Args:
      file_name (str): name of the file in the templates folder
      plugin_name(str): the name of the plugin

    Returns:
      str: the rendered template
    """
