# -*- coding: utf-8 -*-
"""Fake module containing helper functions for the SQLite plugin"""
from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSQLitePluginPathHelper


class FakeSQLitePluginPathHelper(BaseSQLitePluginPathHelper):
  """fake for the sqlite plugin path helper"""
  def __init__(self, path: str, plugin_name: str):
    self.path = str(path)
    self.file_name = str(plugin_name)

  def formatter_file_path(self) -> str:
    return self.file_name

  def parser_file_path(self) -> str:
    return self.file_name

  def formatter_test_file_path(self) -> str:
    return self.file_name

  def parser_test_file_path(self) -> str:
    return self.file_name

  def database_path(self, suffix: str) -> str:
    return self.file_name

  def parser_init_file_path(self) -> str:
    return self.file_name

  def formatter_init_file_path(self) -> str:
    return self.file_name
