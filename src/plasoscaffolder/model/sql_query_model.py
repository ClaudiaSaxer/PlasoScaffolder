# -*- coding: utf-8 -*-
"""The sql query model class."""


class SQLQueryModel(object):
  def __init__(self, query: str, name: str):
    """ initializes the sql query model.

    Args:
      name (str): The name of the query.
      query (str): The SQL Query.
    """
    self._name = name
    self._query = query

  @property
  def name(self) -> str:
    """ the sql query name.

    Returns:
      (str): The name of the sql query parser row.
    """
    return self._name

  @property
  def query(self) -> bool:
    """ the sql query

    Returns:
      (str): The SQL query.

    """
    return self._query
