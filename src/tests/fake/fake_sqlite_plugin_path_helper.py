# -*- coding: utf-8 -*-
"""Fake module containing __helper functions for the SQLite plugin"""
from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper


class FakeSQLitePluginPathHelper(
    base_sqlite_plugin_path_helper.BaseSQLitePluginPathHelper):
  """fake for the sqlite plugin __path __helper"""

  def __init__(self, path: str, plugin_name: str, database_suffix: str):
    super().__init__()
    self.formatter_file_path = plugin_name
    self.parser_file_path = plugin_name
    self.formatter_test_file_path = plugin_name
    self.parser_test_file_path = plugin_name
    self.database_path = plugin_name
    self.parser_init_file_path = plugin_name
    self.formatter_init_file_path = plugin_name

