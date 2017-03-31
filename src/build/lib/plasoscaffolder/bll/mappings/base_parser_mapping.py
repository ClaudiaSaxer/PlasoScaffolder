# -*- coding: utf-8 -*-
""" Module representing function for the different files. """
import abc

from plasoscaffolder.model import sql_query_model


class BaseParserMapper(object):
  """The parser mapper base class."""
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def GetParser(self, plugin_name: str, events: list,
                queries: [sql_query_model.SQLQueryModel]) -> str:
    """Retrieves the parser.

    Args:
      plugin_name (str): the name of the plugin
      events (list): the list of the events
      queries ([sql_query_model.SQLQueryModel]): list of queries

    Returns:
      str: the rendered template
    """
