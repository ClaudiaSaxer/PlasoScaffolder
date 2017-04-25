# -*- coding: utf-8 -*-
"""The Formatter Data model class."""
from plasoscaffolder.model import sql_query_model


class FormatterDataModel(object):
  """Class for the data for the formatter template."""

  def __init__(self,
               plugin_name: str,
               queries: [sql_query_model.SQLQueryModel]):
    """Initialises the formatter data model.

    Args:
      plugin_name (str): the name of the plugin
      queries (sql_query_model.SQLQueryModel): the queries
    """
    self._plugin_name = plugin_name
    self._queries = queries

  @property
  def Queries(self) -> [sql_query_model.SQLQueryModel]:
    """The queries

    Returns:
      str: the sql queries
    """
    return self._queries

  @property
  def PluginName(self) -> str:
    """The plugin name

    Returns:
      str: the name of the plugin
    """
    return self._plugin_name
