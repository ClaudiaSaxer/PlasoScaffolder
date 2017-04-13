# -*- coding: utf-8 -*-
"""Model for SQL column"""
import re


class SQLColumnModel(object):
  """Class for columns of a SQL Query."""

  def __init__(self, sql_column: str, sql_column_type: str = 'None'):
    """ initializes the SQL column model.

    Args:
      sql_column (str): the column name of the SQL Query
      sql_column_type (str): the type of the SQL column
    """
    self._sql_column = sql_column
    self._sql_column_type = sql_column_type

  @property
  def SQLColumn(self) -> str:
    """the SQL column

    Returns:
      str: the column of the SQL
    """
    return self._sql_column

  @property
  def SQLColumnType(self) -> type :
    """the SQL column type

    Returns:
      type: the type of the column of the SQL
    """
    return self._sql_column_type

  def ColumnTypeAsName(self) -> str:
    """the type as the name
    example: <class 'int'> type will be returned as int
    
    Returns:
      str: the type as the name
    """
    return self._sql_column_type.__name__

  def ColumnAsSnakeCase(self) -> str:
    """SQL column name to snake case

    Returns:
      str: the column name from the SQL in snake case
    """
    substitudeFirstPart = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', self._sql_column)
    substitudeSecondPart = re.sub(
        '([a-z0-9])([A-Z])', r'\1_\2', substitudeFirstPart).lower()
    return substitudeSecondPart

  def ColumnAsDescription(self) -> str:
    """SQL column name to description

    Returns:
      str: the column name from the SQL in description form
    """
    substitudeFirstPart = re.sub('(.)([A-Z][a-z]+)', r'\g<1> \g<2>',
                                 self._sql_column)
    substitudeSecondPart = re.sub(
        '([a-z0-9])([A-Z])', r'\g<1> \g<2>', substitudeFirstPart)
    return substitudeSecondPart.title()
