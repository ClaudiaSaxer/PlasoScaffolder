# -*- coding: utf-8 -*-
"""Model for SQL column."""
from plasoscaffolder.model import sql_query_column_model


class SQLColumnModelTimestamp(sql_query_column_model.SQLColumnModel):
  """Class for columns of a SQL Query."""

  def __init__(
      self, sql_column: str, sql_column_type: type = None,
      expected_message: str = ''):
    """initializes the SQL column model.
  
    Args:
      sql_column (str): the column name of the SQL Query
      sql_column_type (str): the type of the SQL column
      expected_message ({key:value}): the expected Messages for the 
          timestamps {key:value}

    """
    super().__init__(sql_column, sql_column_type)
    self.expected_message = expected_message
    self.expected_message_short = expected_message[0:77]
