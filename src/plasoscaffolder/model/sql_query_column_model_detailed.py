# -*- coding: utf-8 -*-
"""Model for SQL column."""

from plasoscaffolder.model import sql_query_column_model


class SQLColumnModelDetailed(sql_query_column_model.SQLColumnModel):
  """Class for columns of a SQL Query."""

  def __init__(self, sql_column: str, sql_column_type: type = None,
               data: {str: str} = None,
               expected_message: {str: str} = None):
    """initializes the SQL column model.

    Args:
      sql_column (str): the column name of the SQL Query
      sql_column_type (str): the type of the SQL column
      data {str: str}: the data for the timestamp {key:value}
      expected_message {key:value}: the expected Messages for the 
          timestamps {key:value}
    """
    super().__init__(sql_column, sql_column_type)
    self.expected_message = expected_message
    self._data = data

  def GetFirstDataForTimeEvent(self, timestamp: str) -> str:
    """The Data for the Time Event
  
    Args:
      timestamp: the timestamp column name
  
    Returns:
      str: the data for the timestamp
    """
    return self._data.get(timestamp, 'TODO')
