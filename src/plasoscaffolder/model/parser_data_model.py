# -*- coding: utf-8 -*-
"""The sql Query model class."""
from plasoscaffolder.model import sql_query_model


class ParserDataModel(object):
  """Class for the data for the parser template"""

  def __init__(self, class_name: str, file_name: str,
               attributes: [str],
               events: [str], plugin_name: str,
               queries: sql_query_model.SQLQueryModel,
               required_tables: [str]):
    """Initialises the parser data model

    Args:
      class_name (str): the name of the class
      file_name (str): the name of the file
      attributes ([str]): the attributes
      events ([str]): the events
      plugin_name (str): the name of the plugin
      queries (sql_query_model.SQLQueryModel): the queries
      required_tables ([str]): the tables that are required
    """
    self._class_name = class_name
    self._file_name = file_name
    self._attributes = attributes
    self._events = events
    self._plugin_name = plugin_name
    self._queries = queries
    self._required_tables = required_tables

  @property
  def RequiredTables(self) -> str:
    """the required tables

    Returns:
      str: the tables that are required
    """
    return self._required_tables

  @property
  def Queries(self) -> [(sql_query_model.SQLQueryModel)]:
    """the queries

    Returns:
      str: the sql queries
    """
    return self._queries

  @property
  def PluginName(self) -> str:
    """the plugin name

    Returns:
      str: the name of the plugin
    """
    return self._plugin_name

  @property
  def ClassName(self) -> str:
    """the class name

    Returns:
      str: the name of the class
    """
    return self._class_name

  @property
  def FileName(self) -> str:
    """the file name

    Returns:
      str: the name of the file
    """
    return self._file_name

  @property
  def Attributes(self) -> [str]:
    """the attributes

    Returns:
      [str]: the columns of all the queries
    """
    return self._attributes

  @property
  def Events(self) -> str:
    """the events

    Returns:
      str: all the events
    """
    return self._events
