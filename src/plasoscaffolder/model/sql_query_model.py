# -*- coding: utf-8 -*-
"""The SQL Query model class."""
from plasoscaffolder.model import sql_query_column_model


class SQLQueryModel(object):
  """A SQL Query Model."""

  def __init__(self, query: str, name: str,
               columns: [sql_query_column_model.SQLColumnModel],
               needs_customizing: bool):
    """ initializes the sql Query model.

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
    """ the SQL Query Name.

    Returns:
      str: The Name of the sql Query parser row.
    """
    return self._name

  @property
  def Query(self) -> bool:
    """ the SQL Query

    Returns:
      str: The SQL Query.
    """
    return self._query

  @property
  def NeedsCustomizing(self) -> bool:
    """ if the event for the query needs customizing

    Returns:
      bool: if the event needs customizing
    """
    return self._needs_customizing

  @property
  def Columns(self) -> [sql_query_column_model.SQLColumnModel]:
    """the columns of the query

    Returns:
      [sql_query_column_model.SQLColumnModel]: list of columns
    """
    return self._columns
