# -*- coding: utf-8 -*-
"""The parser test model class."""
from plasoscaffolder.model import sql_query_model
from plasoscaffolder.model import base_data_model


class ParserTestDataModel(base_data_model.BaseDataModel):
  """Class for the data for the parser test template."""

  def __init__(self,
               plugin_name: str,
               queries: [sql_query_model.SQLQueryModel],
               database_name: str):
    """Initialises the parser test data model.

    Args:
      database_name (str): the name of the database
      plugin_name (str): the name of the plugin
      queries (sql_query_model.SQLQueryModel): the queries
      count_events (int): the event counter
    """
    super().__init__(plugin_name)
    self.queries = queries
    self.database_name = database_name

