# -*- coding: utf-8 -*-
"""Model for SQL column."""

from plasoscaffolder.model import sql_query_column_model


class SQLColumnModelData(sql_query_column_model.SQLColumnModel):
  """Class for columns of a SQL Query."""

  def __init__(self, sql_column: str, sql_column_type: type = None, data=None,
               expected_message=None):
    """ initializes the SQL column model.
  
    Args:
      sql_column (str): the column name of the SQL Query
      sql_column_type (str): the type of the SQL column
      data (str, str): the data for the timestamp (key, value)
      expected_message (str, str): the expected Messages for the timestamps (
          key, value)
    """
    super().__init__(sql_column, sql_column_type)
    self._expected_message = expected_message
    self._data = data

"""todo : move messages in new class as top and data as item"""
  @property
  def ExpectedMessages(self) -> (str, str):
    """The Expected Message for the timestamp
  
    Returns:
      (str,str): key (timestamp) value (data)
    """
    return self._expected_message

  @property
  def ExpectedMessagesShort(self) -> (str, str):
    """The Expected Message for the timestamp
  
    Returns:
      (str,str): key (timestamp) value (data)
    """
    return self._expected_message[0:77]

  def FirstEventPositionInEvents(self) -> int:
    """
    
    Args:
      self: 

    Returns:
    """


"""move until here"""
  def FirstDataForTimeEvent(self, timestamp: str) -> str:
    """The Data for the Time Event
    
    Args:
      timestamp: the timestamp column name
  
    Returns:
      str: the data for the timestamp
    """
    return self._data.get(timestamp, 'TODO')
