# -*- coding: utf-8 -*-
"""Model for SQL column."""
from plasoscaffolder.model import sql_query_column_model_detailed


class SQLColumnModelData(object):
  """Class for columns of a SQL Query."""

  def __init__(
      self, expected_message: {str: str},
      columns_detailed: [sql_query_column_model_detailed.SQLColumnModelDetailed]
  ):
    """initializes the SQL column model.
  
    Args:
      expected_message ({key:value}): the expected Messages for the 
          timestamps {key:value}
      columns_detailed ([
          sql_query_column_model_detailed.SQLColumnModelDetailed]): the columns
          with detailed information for the data columns
    """
    super().__init__()
    self._expected_message = expected_message
    self._columns_detailed = columns_detailed

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

  @property
  def Columns(self) -> ([sql_query_column_model_detailed.SQLColumnModelDetailed]):
    """The columns with detailed information for the data columns

    Returns:
      ([sql_query_column_model_detailed.SQLColumnModelDetailed]): the columns
    """
    return self._columns_detailed