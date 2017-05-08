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
    self.expected_message = expected_message
    self.expected_message_short = expected_message[0:77]
    self.columns_detailed = columns_detailed
