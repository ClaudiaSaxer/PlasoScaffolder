# -*- coding: utf-8 -*-
""" Module representing function for the different files """
from abc import ABCMeta, abstractmethod


class BaseInitMapper(metaclass=ABCMeta):
  """class representing the init mapper"""

  @abstractmethod
  def get_formatter_init_create(self, plugin_name: str) -> str:
    """renders formatter init if you want to create new init file

    Args:
      plugin_name: the plugin name

    Returns: string of the rendered template
    """
    pass

  @abstractmethod
  def get_formatter_init_edit(self, plugin_name: str) -> str:
    """renders formatter init if you want to create new init file

    Args:
      plugin_name: the plugin name

    Returns: string of the rendered template
    """
    pass

  @abstractmethod
  def get_parser_init_create(self, plugin_name: str) -> str:
    """renders formatter init if you want to edit an existing init file

    Args:
      plugin_name: the plugin name

    Returns: string of the rendered template
    """
    pass

  @abstractmethod
  def get_parser_init_edit(self, plugin_name: str) -> str:
    """renders parser init if you want to create new init file

    Args:
      plugin_name: the plugin name

    Returns: string of the rendered template
    """
    pass

  @abstractmethod
  def _render_init(self, file_name: str, plugin_name: str) -> str:
    """renders parser init if you want to edit an existing init file

    Args:
      file_name: name of the file in the templates folder
      plugin_name: the name of the plugin

    Returns:string of the rendered template
    """
    pass
