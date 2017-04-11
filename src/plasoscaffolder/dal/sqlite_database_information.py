# -*- coding: utf-8 -*-
"""Information for the SQLite Database"""
from plasoscaffolder.dal import base_database_information
from plasoscaffolder.dal import base_sql_query_execution


class SQLiteDatabaseInformation(
    base_database_information.BaseDatabaseInformation):
  """Class representing the SQLite Query validator
  """

  def __init__(self,
               sql_execution: base_sql_query_execution.BaseSQLQueryExecution):
    """Initializes the SQL Query Validator

    Args:
      sql_execution (base_sql_query_execution.BaseSQLQueryExecution): the
      helper to execute a query
    """
    super().__init__()
    self._sql_execution = sql_execution

  def getTablesFromDatabase(self) -> [str]:
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.

    Returns:
      [str]: the names of the tables"""
    query = "select name from sqlite_master where type='table' order by name"
    data = self._sql_execution.executeQuery(query)

    if data.has_error:
      return []
    else:
      return [str(data_tuple[0]) for data_tuple in data.data]
