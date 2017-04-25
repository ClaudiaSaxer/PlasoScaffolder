# -*- coding: utf-8 -*-
"""Model for SQL column."""
import re


class SQLColumnModel(object):
  """Class for columns of a SQL Query."""

  def __init__(self, sql_column: str, sql_column_type: type=None):
    """ initializes the SQL column model.

    Args:
      sql_column (str): the column name of the SQL Query
      sql_column_type (str): the type of the SQL column
    """
    self._sql_column = sql_column
    self._sql_column_type = sql_column_type

  @property
  def SQLColumn(self) -> str:
    """The SQL column.

    Returns:
      str: the column of the SQL
    """
    return self._sql_column

  @property
  def SQLColumnType(self) -> type:
    """The SQL column type.

    Returns:
      type: the type of the column of the SQL
    """
    return self._sql_column_type

  @SQLColumnType.setter
  def SQLColumnType(self, value):
    """Setts the sql column type if it is not none and a type"""
    if value is not None and type(value) is type:
      self._sql_column_type = value

  def ColumnTypeAsName(self) -> str:
    """The type as the name.
    example: <class 'int'> type will be returned as int

    Returns:
      str: the type as the name
    """
    return self._sql_column_type.__name__

  def ColumnAsSnakeCase(self) -> str:
    """SQL column name to snake case.

    Returns:
      str: the column name from the SQL in snake case
    """
    if re.fullmatch("[a-zA-Z0-9]*", self._sql_column):
      substitute_first_part = re.sub('(.)([A-Z][a-z]+)', r'\1_\2',
                                     self._sql_column)
      substitute_second_part = re.sub(
          '([a-z0-9])([A-Z])', r'\1_\2', substitute_first_part).lower()
      return substitute_second_part
    else:
      return self._sql_column.lower()

  def ColumnAsDescription(self) -> str:
    """SQL column name to description.

    Returns:
      str: the column name from the SQL in description form
    """
    substitute_first_part = re.sub('(.)([A-Z][a-z]+)', r'\g<1> \g<2>',
                                   self._sql_column)
    substitute_second_part = re.sub(
        '([a-z0-9])([A-Z])', r'\g<1> \g<2>', substitute_first_part)
    return substitute_second_part.title()
