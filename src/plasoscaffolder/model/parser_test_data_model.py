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
    """
    super().__init__(plugin_name)
    self._queries = queries
    self._database_name = database_name

  @property
  def DatabaseName(self) -> str:
    """The database name.

    Returns:
      str: the name of the database
    """
    return self._database_name

  @property
  def Queries(self) -> [sql_query_model.SQLQueryModel]:
    """The queries.

    Returns:
      str: the sql queries
    """
    return self._queries
