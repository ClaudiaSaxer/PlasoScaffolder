# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Class for the explain query plan."""

from plasoscaffolder.dal import base_sql_query_execution


class ExplainQueryPlan(object):
  """Class representing the explain query plan."""

  def __init__(self,
               sql_execution: base_sql_query_execution.BaseSQLQueryExecution):

    """Initializes the explain query plan.

    Args:
      sql_execution (base_sql_query_execution.BaseSQLQueryExecution): the
          helper to execute a query
    """
    super().__init__()
    self._sql_execution = sql_execution

  def isReadOnly(self, query: str) -> bool:
    """Determines if the query is read only.

    Args:
      query (str): the sql query to determine if it is read only

    Returns:
      bool: true if it is read only, false if it is not
    """
    explain_query = 'EXPLAIN {0}'.format(query)
    explain_result = self._sql_execution.executeQuery(explain_query)
    if explain_result.has_error:
      return False
    opcodes = [explain_row[1] for explain_row in explain_result.data]
    has_write = 'OpenWrite' in opcodes
    self.getLockedTables(query)
    return not has_write

  def getTableForSelect(self, query: str):
    """Determines the table for the select

    Args:
      query (str): the sql query

    Returns:
      ?
    """
    explain_query = 'EXPLAIN {0}'.format(query)
    explain_result = self._sql_execution.executeQuery(explain_query)

    table_read = [(row[3], row[2]) for row in explain_result.data if
                  row[1] == 'OpenRead']
    table_lock = [(row[3], row[5]) for row in explain_result.data if
                  row[1] == 'TableLock']
    table_id_name = {}

    for read in table_read:
      for lock in table_lock:
        if lock[0] == read[0]:
          table_id_name[read[1]] = lock[1]

    # row 2 = opcode, row 2 = id von table, row 3 = order in table, row 4 =
    # order
    column_id_table = [
      (table_id_name[explain_row[2]], explain_row[3], explain_row[4]) for
      explain_row in
      explain_result.data if
      explain_row[1] == 'Column' and explain_row[2] in table_id_name]
    # column_id_table = sorted(column_id_table, key=lambda column: column[1] )
    all_information = list()

    pseudo_columns_number = [row[2] for row in explain_result.data if row[1] == 'OpenPseudo']
    if  pseudo_columns_number != []:
      id_of_result_row_info = max(pseudo_columns_number)

      what_columns = [
        (explain_row[3], explain_row[4]) for explain_row in
        explain_result.data if
        explain_row[1] == 'Column' and explain_row[2] == id_of_result_row_info]

      what_columns_in_result = [row[1] for row in what_columns]
      how_columns_are_sorted = [row[0] for row in what_columns]

      column_id_only_result = [(row[0], row[1]) for row in column_id_table
                               if row[2] in what_columns_in_result]

      columns_sorted = [element for (order, element) in sorted(
          zip(how_columns_are_sorted, column_id_only_result))]
    else:
      columns_sorted = column_id_table


    table_result = {}
    for table in table_lock:
      table_info_query = 'PRAGMA table_info({0})'.format(table[1]);
      table_info_result = self._sql_execution.executeQuery(table_info_query)
      table_result[table[1]] = table_info_result

    for column in columns_sorted:
      table_name = column[0]
      if table_result[table_name]:
        result_data = table_result[table_name].data
        column = (
          [(d[1], d[2]) for d in result_data if d[0] == column[1]][
            0])
        if column:
         all_information.append(column)

    return all_information


  def getLockedTables(self, query: str) -> [str]:
    """Determines the table that were locked during the SQL query.

    Args:
      query (str): the sql query to get the locked tables from

    Returns:
      [str]: the list of tables
    """
    explain_query = 'EXPLAIN {0}'.format(query)
    explain_result = self._sql_execution.executeQuery(explain_query)
    if explain_result.has_error or explain_result.data is None:
      return []
    tables = [explain_row[5] for explain_row in explain_result.data if
              explain_row[1] == 'TableLock']
    return tables
