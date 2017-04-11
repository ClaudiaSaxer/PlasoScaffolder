import re
"""Model for sql column"""

class SQLColumnModel(object):
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
    substitudeFirstPart = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', self._sql_column)
    substitudeSecondPart = re.sub(
        '([a-z0-9])([A-Z])', r'\1_\2', substitudeFirstPart).lower()
    return substitudeSecondPart
