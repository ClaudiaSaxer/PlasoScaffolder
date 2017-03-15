# -*- coding: utf-8 -*-
"""Fake Module containing helper functions for the SQLite plugin"""
from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.services.base_sqlite_plugin_helper import \
  BaseSQLitePluginHelper
from plasoscaffolder.common.base_file_handler import BaseFileHandler


class FakeSQLitePluginHelper(BaseSQLitePluginHelper):

  def plugin_exists(self, template_path: str,
      fileHandler: BaseFileHandler, init_mapper: BaseInitMapper) -> bool:
    return False

  def file_exists(self, path: str) -> bool:
    return False

  def folder_exists(self, path: str) -> bool:
    return False