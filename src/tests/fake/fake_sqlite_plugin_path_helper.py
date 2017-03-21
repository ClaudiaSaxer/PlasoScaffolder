# -*- coding: utf-8 -*-
"""Fake module containing helper functions for the SQLite plugin"""
from plasoscaffolder.bll.services import base_sqlite_plugin_path_helper


class FakeSQLitePluginPathHelper(
    base_sqlite_plugin_path_helper.BaseSQLitePluginPathHelper):
  """fake for the sqlite plugin path helper"""

  def __init__(self, path: str, plugin_name: str):
    self.path = str(path)
    self.file_name = str(plugin_name)

  def FormatterFilePath(self) -> str:
    return self.file_name

  def ParserFilePath(self) -> str:
    return self.file_name

  def FormatterTestFilePath(self) -> str:
    return self.file_name

  def ParserTestFilePath(self) -> str:
    return self.file_name

  def DatabasePath(self, suffix: str) -> str:
    return self.file_name

  def ParserInitFilePath(self) -> str:
    return self.file_name

  def FormatterInitFilePath(self) -> str:
    return self.file_name
