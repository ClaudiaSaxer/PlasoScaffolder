# -*- coding: utf-8 -*-
"""Fake Module containing helper functions for the SQLite plugin"""
from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.services.base_sqlite_plugin_helper import \
  BaseSQLitePluginHelper
from plasoscaffolder.common.base_file_handler import BaseFileHandler


class FakeSQLitePluginHelper(BaseSQLitePluginHelper):
  """fake for the sqlite plugin helper"""

  def plugin_exists(self, _template_path: str,
                    _fileHandler: BaseFileHandler,
                    _init_mapper: BaseInitMapper) -> bool:
    return False

  def file_exists(self, path: str) -> bool:
    return False

  def folder_exists(self, path: str) -> bool:
    return False

  def valide_plugin_name(self, plugin_name: str) -> bool:
    return True
