# -*- coding: utf-8 -*-
"""The sql Query model class."""
import re


class SQLQueryModel(object):
  "A sql Query Model."

  def __init__(self, query: str, name: str, columns: []):
    """ initializes the sql Query model.

    Args:
      columns ([SQLColumns]): list of columns for the Query
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
  def Columns(self) -> []:
    """the columns of the query

    Returns:
      [SQLColumns]: list of columns
    """
    return self._columns


class SQLColumns(object):
  """class for columns of a sql Query"""

  def __init__(self, sql_column: str):
    """ initializes the sql column model.

    Args:
      sql_column (str): the column Name of the sql Query
    """
    self._sql_column = sql_column

  @property
  def SQLColumn(self) -> str:
    """the sql column

    Returns:
      str: the column of the sql
    """
    return self._sql_column

  # TODO write test
  def ColumnAsSnakeCase(self) -> str:
    """sql column name to snake case

    Returns:
      str: the column name from the sql in snake case
    """
    return '_'.join(re.findall('[A-Z][a-z]*', self._sql_column.lower()))
