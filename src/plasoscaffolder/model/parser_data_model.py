# -*- coding: utf-8 -*-
"""The parser model class."""
from plasoscaffolder.model import sql_query_model
from plasoscaffolder.model import base_data_model


class ParserDataModel(base_data_model.BaseDataModel):
  """Class for the data for the parser template."""

  def __init__(self,
               plugin_name: str,
               queries: [sql_query_model.SQLQueryModel],
               required_tables: [str],
               database_name: str):
    """Initialises the parser data model.

    Args:
      database_name (str): the name of the database
      plugin_name (str): the name of the plugin
      queries (sql_query_model.SQLQueryModel): the queries
      required_tables ([str]): the tables that are required
    """
    super().__init__(plugin_name)
    self._queries = queries
    self._required_tables = required_tables
    self._database_name = database_name

  @property
  def DatabaseName(self) -> str:
    """The database name.

    Returns:
      str: the name of the database
    """
    return self._database_name

  @property
  def RequiredTables(self) -> str:
    """The required tables.

    Returns:
      str: the tables that are required
    """
    return self._required_tables

  @property
  def Queries(self) -> [sql_query_model.SQLQueryModel]:
    """The queries.

    Returns:
      str: the sql queries
    """
    return self._queries
