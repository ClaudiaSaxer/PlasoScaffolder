# -*- coding: utf-8 -*-
"""The SQL query model class."""
from plasoscaffolder.model import sql_query_column_model
from plasoscaffolder.model import sql_query_column_model_data


class SQLQueryModel(object):
  """A SQL query model."""

  def __init__(self, query: str, name: str,
               columns: [sql_query_column_model.SQLColumnModel],
               timestamp_columns: [sql_query_column_model.SQLColumnModel],
               needs_customizing: bool,
               amount_events: int
               ):
    """ initializes the SQL query model.

    Args:
      columns ([sql_query_column_model.SQLColumnModel]): list of columns for
          the Query
      timestamp_columns ([sql_query_column_model.SQLColumnModel]): list of 
          columns which are timestamp events
      name (str): The Name of the Query.
      query (str): The SQL Query.
      needs_customizing (bool): if the event for the query needs customizing
      amount_events (int): amount of events as result of the query
    """
    super().__init__()
    self._name = name
    self._query = query
    self._columns = columns
    self._needs_customizing = needs_customizing
    self._timestamp_columns = timestamp_columns
    self._amount_events = amount_events

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
  def AmountEvents(self) -> int:
    """Amount of Events for the query

    Returns:
      int: the amount of events
    """
    return self._amount_events

  @property
  def Columns(self) -> [sql_query_column_model_data.SQLColumnModelData]:
    """The columns of the query.

    Returns:
      [sql_query_column_model_data.SQLColumnModelData]: list of columns with 
          data
    """
    return self._columns

  @property
  def TimestampColumns(self) -> [sql_query_column_model.SQLColumnModel]:
    """The columns of the query.

    Returns:
      [sql_query_column_model.SQLColumnModel]: list of columns
    """
    return self._timestamp_columns
