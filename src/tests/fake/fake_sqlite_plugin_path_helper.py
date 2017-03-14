# -*- coding: utf-8 -*-
"""Module containing helper functions for the SQLite plugin"""
import os

from plasoscaffolder.bll.services.base_sqlite_plugin_path_helper import \
  BaseSqlitePluginPathHelper


class FakeSqlitePluginPathHelper(BaseSqlitePluginPathHelper):
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

  def database_path(self) -> str:
    return self.file_name

  def parser_init_file_path(self) -> str:
    return self.file_name

  def formatter_init_file_path(self) -> str:
    return self.file_name
