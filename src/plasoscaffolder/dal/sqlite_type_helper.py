# -*- coding: utf-8 -*-
"""SQLite Type Helper."""
import collections

from plasoscaffolder.common import type_mapper
from plasoscaffolder.dal import (base_database_information,
                                 base_explain_query_plan)
from plasoscaffolder.dal import base_sql_query_execution
from plasoscaffolder.dal import base_type_helper
from plasoscaffolder.model import sql_query_column_model


class SQLiteTypeHelper(base_type_helper.BaseTypeHelper):
  """Class representing the type helper for SQLite."""
  _POSSIBLEQUERYSEPERATOR = [' ', ',']

  def __init__(
      self, execution: base_sql_query_execution.BaseSQLQueryExecution,
      explain: base_explain_query_plan.BaseExplainQueryPlan,
      database_information: base_database_information.BaseDatabaseInformation):
    """Initializes the SQLite Type Helper
  
    Args:
      execution (base_sql_query_execution.BaseSQLQueryExecution): the class 
          for the execution of the SQLite queries
      explain (base_explain_query_plan.BaseExplainQueryPlan): the class for
          explain information
      database_information (base_database_information.BaseDatabaseInformation): 
          the class for information about the database
    """
    super().__init__()
    self._execute = execution
    self._explain = explain
    self._information = database_information

  def GetDuplicateColumnNames(
      self, columns: sql_query_column_model.SQLColumnModel) -> [str]:
    """Find out if the query has duplicate column names and if a alias is needed
    
    Args:
      columns (sql_query_column_model.SQLColumnModel): all columns parsed 
      from the cursor
    Returns:
      [str]: a list of all the duplicate column names, if its empty it means it
          a distinct list of columns
    """
    single_column_name_list = [column.SQLColumn for column in columns]
    duplicate_list = [column for column, count in
                      collections.Counter(single_column_name_list).items() if
                      count > 1]
    return duplicate_list

  def GetColumnInformationFromDescription(
      self, description: []) -> [sql_query_column_model.SQLColumnModel]:
    """Getting Information for the column out of the cursor.
  
    Args:
      description: the description of the cursor
  
    Returns:
      list(sql_query_column_model.SQLColumnModel): a list with all the column 
          names, the types are None
    """
    sql_column = list()
    for description in description:

      sql_column.append(
          sql_query_column_model.SQLColumnModel(description[0], type(None)))

    return sql_column

  def AddMissingTypesFromSchema(
      self, columns: [sql_query_column_model.SQLColumnModel], query: str,
  ) -> [sql_query_column_model.SQLColumnModel]:
    """Getting Information for the column out of the cursor.
    
    Args:
      columns ([sql_query_column_model.SQLColumnModel]): the columns with all 
          the column names
      query: the query
      
    Returns:
      list(sql_query_column_model.SQLColumnModel): a list with all the columns
    """
    locked = [table.lower() for table in self._explain.GetLockedTables(query)]

    if len(locked) == 1:
      return self._ColumnTypeForOnlyOneTable(locked[0], columns)
    else:
      return self._ColumnTypeForMultipleTables(locked, columns, query)

  def _ColumnTypeForOnlyOneTable(
      self, table_name: str,
      column_model: sql_query_column_model.SQLColumnModel
  ) -> [sql_query_column_model.SQLColumnModel]:
    """Getting Types for Column if there is only one table
    
    Args:
      table_name (str): the name of the table
      column_model ([sql_query_column_model.SQLColumnModel]): the column to 
          find the type for
  
    Returns:
      [sql_query_column_model.SQLColumnModel]: the column model with the types
    """
    mappings = self._information.GetTableColumnsAndType(table_name)
    for column in column_model:

      type_sqlite = mappings[column.SQLColumn].upper()
      type_sqlite_basic = type_sqlite.split("(")[0]
      type_python = type_mapper.TypeMapperSQLitePython.MAPPINGS.get(
          type_sqlite_basic, type(None))

      column.SQLColumnType = type_python
    return column_model

  def _ColumnTypeForMultipleTables(
      self, tables: [str],
      column_model: sql_query_column_model.SQLColumnModel, query: str
  ) -> [sql_query_column_model.SQLColumnModel]:
    """Getting Types for Column if there is are multiple tables

    Args:
      tables ([str]): the name of the table
      column_model ([sql_query_column_model.SQLColumnModel]): the column to 
          find the type for
      query (str): the SQL query

    Returns:
      [sql_query_column_model.SQLColumnModel]: the column model with the types
    """
    query = query.lower()

    table_and_type = {
      table: self._information.GetTableColumnsAndType(table, True) for table
      in tables}

    for column in column_model:
      column_name = column.SQLColumn.lower()

      as_column_string_start = next(filter(lambda start: start > 0, map(
          lambda space: query.find(' as {0}{1}'.format(column_name, space)),
          self._POSSIBLEQUERYSEPERATOR)), None)

      # column with alias
      if as_column_string_start:
        table_end = query.rfind('.', 0, as_column_string_start)
        table_start = self._GetPositionAfterSeparator(query, table_end)
        sqlite_column_name = query[table_end + 1:as_column_string_start]

      # column without alias
      else:
        table_end = self._GetStartOfColumnIfNotAlias(query, column_name)
        table_start = self._GetPositionAfterSeparator(query, table_end)
        sqlite_column_name = column_name

      table_name = query[table_start:table_end]
      type_sqlite = table_and_type[table_name][sqlite_column_name].upper()

      type_sqlite_basic = type_sqlite.split("(")[0]
      type_python = type_mapper.TypeMapperSQLitePython.MAPPINGS.get(
          type_sqlite_basic, type(None))
      column.SQLColumnType = type_python

    return column_model

  def _GetStartOfColumnIfNotAlias(self, query, column_name):
    """Getting the start of the column if it is not an alias column
    
    Args:
      query: the query to be searched
      column_name: the name to be searched for

    Returns: 0 if no column could be found or the starting position of the 
        column

    """
    wrong_position = query.find('.{0} as'.format(column_name))

    return next(filter(
        lambda starts: starts > 0 and starts != wrong_position,
        map(lambda space: query.find('.{0}{1}'.format(column_name, space))
            , self._POSSIBLEQUERYSEPERATOR)))

  def _GetPositionAfterSeparator(self, text, end_position: int):
    """Get the first separator position, starting at the end and searching 
     in reverse
    
    Args:
      text: the text to be searched through
      end_position: the end position the search should be started from

    Returns:
      the first separator position found in the text started from the end 
          position

    """
    all_appearances = (filter(
        lambda start: start > 0,
        map(lambda space: text.rfind(space, 0, end_position),
            self._POSSIBLEQUERYSEPERATOR)))
    return max(all_appearances) + 1
