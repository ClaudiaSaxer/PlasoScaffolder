# -*- coding: utf-8 -*-
# pylint: disable=no-member
# pylint does not recognize connect and close as member
"""Base for sql Query validators."""
import sqlite3

from plasoscaffolder.common import type_mapper
from plasoscaffolder.dal import (base_sql_query_execution,
                                 sqlite_database_information)
from plasoscaffolder.dal import explain_query_plan
from plasoscaffolder.model import sql_query_column_model


class SQLQueryExecution(base_sql_query_execution.BaseSQLQueryExecution):
  """Class representing the SQLite Query validator."""

  def __init__(self, database_path: str):
    """Initializes the SQL Query Validator.

    Args:
      database_path (str): the path to the SQLite database schema
    """
    super().__init__()
    self._database_path = database_path
    self._connection = None
    self._explain = None
    self._database_information = None

  def tryToConnect(self) -> bool:
    """Try to open the database File.

    Returns:
      bool: if the file can be opened and is a database file
    """
    try:
      self._connection = sqlite3.connect(
          self._database_path)
      self._connection.isolation_level = None  # no autocommit mode
      self._explain = explain_query_plan.ExplainQueryPlan(self)
      # this query failes if is not a database or locked or anything went wrong
      self._connection.execute('PRAGMA schema_version')
      self._database_information = (
        sqlite_database_information.SQLiteDatabaseInformation(self))
    except sqlite3.Error:
      return False

    return True

  def executeQuery(
      self, query: str) -> base_sql_query_execution.SQLQueryData:
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.

    Returns:
      base_sql_query_execution.SQLQueryData: The data to the Query
    """
    return self._executeQuery(query, False)

  def executeQueryDetailed(
      self, query: str) -> base_sql_query_execution.SQLQueryData:
    """Executes the SQL Query and gets Detailed Information

    Args:
      query (str): The SQL Query to execute on the SQLite database.

    Returns:
      base_sql_query_execution.SQLQueryData: The data to the Query
    """
    data_from_executed_query = self._executeQuery(query, True)
    if not data_from_executed_query.has_error:
      data_from_executed_query.columns = self._addMissingTypesFromSchema(
          data_from_executed_query.columns, query)

    return data_from_executed_query

  def _old(
      self,
      data: base_sql_query_execution.SQLQueryData,
      query: str) -> base_sql_query_execution.SQLQueryData:
    """Tries to get the types from the schema for columns that have None as a 
    type

        Args:
          query (str): The SQL Query to execute on the SQLite database.
          data (base_sql_query_execution.SQLQueryData): The existing data to 
            the Query

        Returns:
          base_sql_query_execution.SQLQueryData: The data to the Query
        """
    # if there are no data examples
    """if len(query_data) == 0:
      for description in cursor.description:
        print(description)
        sql_column.append(sql_query_column_model.SQLColumnModel(
            description[0], type(None)))

    else:
      for column in range(0, len(query_data[0])):
        for data_row in query_data:
          data_type = data_row[column]
          if data_type is not None:
            break"""

    """ locked = self._explain.getLockedTables(query)

    if data.columns is not None and len(locked) == 1:
      mappings = self._database_information.getTableColumnsAndType(locked[0])
      for column in data.columns:

        if column.SQLColumnType is type(None):
          type_sqlite = mappings[column.SQLColumn].upper()
          type_sqlite_basic = type_sqlite.split("(")[0]
          if type_sqlite_basic in type_mapper.TypeMapperSQLitePython.MAPPINGS:
            type_python = type_mapper.TypeMapperSQLitePython.MAPPINGS[
              type_sqlite_basic]
            column.SQLColumnType = type_python"""

    return data

  def _executeQuery(
      self, query: str,
      detailed: bool = True) -> base_sql_query_execution.SQLQueryData:
    """Executes the SQL Query.

    Args:
      query (str): The SQL Query to execute on the SQLite database.
      detailed (bool): True if additional information about the query is needed

    Returns:
      base_sql_query_execution.SQLQueryData: The data to the Query
    """

    query_data = base_sql_query_execution.SQLQueryData()
    try:
      with self._connection:
        self._connection.execute('BEGIN')
        cursor = self._connection.execute(query)
        query_data.data = cursor.fetchall()
        if detailed:
          query_data.columns = self._getColumnInformationFromCursor(
              cursor.description)
        self._connection.execute('ROLLBACK')
    except sqlite3.Error as error:
      query_data.error_message = 'Error: {0}'.format(str(error))
      query_data.has_error = True
    except sqlite3.Warning as warning:
      query_data.error_message = 'Warning: {0}'.format(str(warning))
      query_data.has_error = True

    return query_data

  def _getColumnInformationFromCursor(
      self, description: []) -> [sql_query_column_model.SQLColumnModel]:
    """Getting Information for the column out of the cursor.

    Args:
      cursor: the cursor

    Returns:
      list(sql_query_column_model.SQLColumnModel): a list with all the columns
    """
    sql_column = list()
    for description in description:

      sql_column.append(
          sql_query_column_model.SQLColumnModel(description[0], type(None)))

    return sql_column

  def _addMissingTypesFromSchema(
      self, columns: [], query,
  ) -> [sql_query_column_model.SQLColumnModel]:
    """Getting Information for the column out of the cursor.
    
    Args:
      cursor: the cursor
      query_data: the data of the query
      
    Returns:
      list(sql_query_column_model.SQLColumnModel): a list with all the columns
    """
    # TODO description
    locked = self._explain.getLockedTables(query)

    if len(locked) == 1:
      mappings = self._database_information.getTableColumnsAndType(locked[0])
      for column in columns:

        type_sqlite = mappings[column.SQLColumn].upper()
        type_sqlite_basic = type_sqlite.split("(")[0]
        type_python = type_mapper.TypeMapperSQLitePython.MAPPINGS.get(
            type_sqlite_basic, type(None))

        column.SQLColumnType = type_python
    else:
      types = self._explain.getTableForSelect(query)

      for i in range(len(columns)):
        type_sqlite = types[i][1].upper()
        type_sqlite_basic = type_sqlite.split("(")[0]
        type_python = type_mapper.TypeMapperSQLitePython.MAPPINGS.get(
            type_sqlite_basic, type(None))
        columns[i].SQLColumnType = type_python

    return columns

  def executeReadOnlyQuery(self, query: str):
    """Executes the SQL Query if it is read only.

      Args:
        query (str): The SQL Query to execute on the SQLite database.

      Returns:
        base_sql_query_execution.SQLQueryData: The data to the Query
    """
    query_data = base_sql_query_execution.SQLQueryData()
    if self._explain.isReadOnly(query):
      query_data = self.executeQueryDetailed(query)
    else:
      query_data.data = None
      query_data.has_error = True
      query_data.error_message = 'Query has to be a single SELECT query.'
      query_data.columns = None
    return query_data
