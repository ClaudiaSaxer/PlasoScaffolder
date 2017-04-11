# -*- coding: utf-8 -*-
"""The sql Query model class."""
from plasoscaffolder.model import sql_query_column_model


class SQLQueryModel(object):
  "A sql Query Model."

  def __init__(self, query: str, name: str,
               columns: [sql_query_column_model.SQLColumnModel]):
    """ initializes the sql Query model.

    Args:
      columns ([sql_query_column_model.SQLColumnModel]): list of columns for the 
      Query
      name (str): The Name of the Query.
      query (str): The SQL Query.
    """
    self._name = name
    self._query = query
    self._columns = columns

  @property
  def Name(self) -> str:
    """ the sql Query Name.

    Returns:
      str: The Name of the sql Query parser row.
    """
    return self._name

  @property
  def Query(self) -> bool:
    """ the sql Query

    Returns:
      str: The SQL Query.

    """
    return self._query

  @property
  def Columns(self) -> [sql_query_column_model.SQLColumnModel]:
    """the columns of the query

    Returns:
      [sql_query_column_model.SQLColumnModel]: list of columns
    """
    return self._columns
