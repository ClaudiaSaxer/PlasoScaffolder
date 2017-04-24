# -*- coding: utf-8 -*-
"""The SQL query model class."""
from plasoscaffolder.model import sql_query_column_model


class SQLQueryModel(object):
  """A SQL query model."""

  def __init__(self, query: str, name: str,
               columns: [sql_query_column_model.SQLColumnModel],
               needs_customizing: bool):
    """ initializes the SQL query model.

    Args:
      columns ([sql_query_column_model.SQLColumnModel]): list of columns for
          the Query
      name (str): The Name of the Query.
      query (str): The SQL Query.
      needs_customizing (bool): if the event for the query needs customizing
    """
    self._name = name
    self._query = query
    self._columns = columns
    self._needs_customizing = needs_customizing

  @property
  def Name(self) -> str:
    """The SQL query name.

    Returns:
      str: the name of the SQL query parser row.
    """
    return self._name

  @property
  def Query(self) -> bool:
    """The SQL query.

    Returns:
      str: The SQL query.
    """
    return self._query

  @property
  def NeedsCustomizing(self) -> bool:
    """If the event for the query needs customizing.

    Returns:
      bool: True If the event needs customizing
    """
    return self._needs_customizing

  @property
  def Columns(self) -> [sql_query_column_model.SQLColumnModel]:
    """The columns of the query.

    Returns:
      [sql_query_column_model.SQLColumnModel]: list of columns
    """
    return self._columns
