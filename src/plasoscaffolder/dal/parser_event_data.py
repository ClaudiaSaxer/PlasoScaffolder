# -*- coding: utf-8 -*-
"""SQLite Type Helper."""
import collections
import re

from plasoscaffolder.common import type_mapper
from plasoscaffolder.dal import base_database_information
from plasoscaffolder.dal import base_explain_query_plan
from plasoscaffolder.dal import base_sql_query_execution
from plasoscaffolder.dal import base_type_helper
from plasoscaffolder.model import sql_query_column_model


class ParserEventData():
  """Class representing the type helper for SQLite."""
  _POSSIBLEQUERYSEPERATOR = [' ', ',']

  def __init__(
      self, execution: base_sql_query_execution.BaseSQLQueryExecution):
    """"""
    super().__init__()
    self._execute = execution


