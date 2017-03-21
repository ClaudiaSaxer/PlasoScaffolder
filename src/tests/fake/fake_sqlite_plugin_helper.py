# -*- coding: utf-8 -*-
"""Fake Module containing helper functions for the SQLite plugin"""
from plasoscaffolder.bll.mappings import base_init_mapping
from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.common import base_file_handler


class FakeSQLitePluginHelper(base_sqlite_plugin_helper.BaseSQLitePluginHelper):
  """fake for the sqlite plugin helper"""

  def PluginExists(self, _template_path: str,
                   _fileHandler: base_file_handler.BaseFileHandler,
                   _init_mapper: base_init_mapping.BaseInitMapper) -> bool:
    return False

  def FileExists(self, path: str) -> bool:
    return False

  def FolderExists(self, path: str) -> bool:
    return False

  def IsValidPluginName(self, plugin_name: str) -> bool:
    return True
