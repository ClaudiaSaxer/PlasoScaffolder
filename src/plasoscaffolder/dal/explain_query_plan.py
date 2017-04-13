# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Class for the explain query plan"""

from plasoscaffolder.dal import base_sql_query_execution


class ExplainQueryPlan(object):
  """Class representing the explain query plan"""

  def __init__(self,
               sql_execution: base_sql_query_execution.BaseSQLQueryExecution):

    """Initializes the explain query plan

    Args:
      sql_execution (base_sql_query_execution.BaseSQLQueryExecution): the
        helper to execute a query
    """
    self._sql_execution = sql_execution
    super().__init__()

  def isReadOnly(self, query: str) -> bool:
    """Determines if the query is read only.

    Returns:
      bool: true if it is read only, false if it is not"""
    explain_query = 'EXPLAIN {0}'.format(query)
    data = self._sql_execution.executeQuery(explain_query)
    if data.has_error:
      return False
    opcodes = [x[1] for x in data.data]
    has_write = "OpenWrite" in opcodes
    self.getLockedTables(query)
    return not has_write

  def getLockedTables(self, query: str) -> [str]:
    """Determines the table that were locked during the sql query.
    
    Returns:
      [str]: the list of tables"""
    explain_query = 'EXPLAIN {0}'.format(query)
    data = self._sql_execution.executeQuery(explain_query)
    if data.has_error or data.data is None:
      return []
    tables = [x[5] for x in data.data if x[1] == 'TableLock' ]
    return tables


