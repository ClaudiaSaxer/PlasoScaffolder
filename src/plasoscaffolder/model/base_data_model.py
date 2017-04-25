# -*- coding: utf-8 -*-
"""The Base data model class."""


class BaseDataModel(object):
  """Class for the data for the formatter template."""

  def __init__(self,
               plugin_name: str):
    """Initialises the base data model.

    Args:
      plugin_name (str): the name of the plugin
    """
    self._plugin_name = plugin_name

  @property
  def PluginName(self) -> str:
    """The plugin name

    Returns:
      str: the name of the plugin
    """
    return self._plugin_name
