# -*- coding: utf-8 -*-
"""Fake Module containing helper functions for the SQLite plugin"""
from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper
from plasoscaffolder.dal import base_sql_query_execution


class FakeSQLitePluginHelper(base_sqlite_plugin_helper.BaseSQLitePluginHelper):
  """fake for the sqlite plugin helper"""

  def __init__(self, plugin_exists=False, folder_exists=False,
               file_exists=False, valid_name=True,
               change_bool_after_every_call_plugin_exists=False,
               change_bool_after_every_call_folder_exists=False,
               change_bool_after_every_call_file_exists=False,
               change_bool_after_every_call_valid_name=False):
    """
    Initializes the fake plugin helper
    Args:
      change_bool_after_every_call_plugin_exists (bool): if the function
      boolean should change after every call.
      change_bool_after_every_call_file_exists (bool): if the function
      boolean should change after every call.
      change_bool_after_every_call_folder_exists (bool): if the function
      boolean should change after every call.
      change_bool_after_every_call_valid_name (bool): if the function
      boolean should change after every call.
      file_exists (bool): what the FileExists function should return
      plugin_exists (bool): what the PluginExists function should return
      folder_exists (bool): what the FolderExists function should return
      valid_name (bool): what the IsValidPluginName function should return
    """
    self.change_valid_name = change_bool_after_every_call_valid_name
    self.change_file_exists = change_bool_after_every_call_file_exists
    self.change_folder_exists = change_bool_after_every_call_folder_exists
    self.change_plugin_exists = change_bool_after_every_call_plugin_exists
    self.plugin_exists = plugin_exists
    self.folder_exists = folder_exists
    self.file_exists = file_exists
    self.valid_name = valid_name

  def PluginExists(self,
                   path: str,
                   plugin_name: str,
                   database_suffix: str,
                   path_helper:
                   base_sqlite_plugin_path_helper.BaseSQLitePluginPathHelper) \
      -> bool:
    if self.change_plugin_exists:
      self.plugin_exists = not self.plugin_exists
      return not self.plugin_exists
    else:
      return self.plugin_exists

  def FileExists(self, path: str) -> bool:
    """will return true false true ... starting with the initial (against
    loops while testing)"""
    if self.change_file_exists:
      self.file_exists = not self.file_exists
      return not self.file_exists
    else:
      return self.file_exists

  def FolderExists(self, path: str) -> bool:
    """will return true false true ... starting with the initial (against
    loops while testing)"""
    if self.change_folder_exists:
      self.folder_exists = not self.folder_exists
      return not self.folder_exists
    else:
      return self.folder_exists

  def IsValidPluginName(self, plugin_name: str) -> bool:
    """will return true false true ... starting with the initial (against
    loops while testing)"""
    if self.change_valid_name:
      self.valid_name = not self.valid_name
      return not self.valid_name
    else:
      return self.valid_name

  def RunSQLQuery(self, query: str,
                  executor: base_sql_query_execution.BaseSQLQueryExecution()):
    """ Validates the sql query

    Args:
      executor (base_sql_query_execution.SQLQueryExection()) the sql executor
      query (str): the sql query 

    Returns:
      base_sql_query_execution.SQLQueryData: the data to the executed query
    """
    return executor.executeQuery(query)
