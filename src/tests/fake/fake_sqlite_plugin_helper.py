# -*- coding: utf-8 -*-
"""Fake Module containing helper functions for the SQLite plugin"""
from plasoscaffolder.bll.mappings import base_init_mapping
from plasoscaffolder.bll.services import base_sqlite_plugin_helper
from plasoscaffolder.common import base_file_handler


class FakeSQLitePluginHelper(base_sqlite_plugin_helper.BaseSQLitePluginHelper):
  """fake for the sqlite plugin helper"""

  def __init__(self, plugin_exists=False, folder_exists=False,
               file_exists=False, valid_name=True,
               change_bool_after_every_call=False):
    """
    Initializes the fake plugin helper
    Args:
      change_bool_after_every_call (bool): if the fuction boolean should change
      after every call against loops while testing.
      file_exists (bool): what the FileExists function should return
      plugin_exists (bool): what the PluginExists function should return
      folder_exists (bool): what the FolderExists function should return
      valid_name (bool): what the IsValidPluginName function should return
    """
    self.change_bool_after_every_call = change_bool_after_every_call
    self.plugin_exists = plugin_exists
    self.folder_exists = folder_exists
    self.file_exists = file_exists
    self.valid_name = valid_name

  def PluginExists(self, _template_path: str,
                   _fileHandler: base_file_handler.BaseFileHandler,
                   _init_mapper: base_init_mapping.BaseInitMapper) -> bool:
    return self.plugin_exists

  def FileExists(self, path: str) -> bool:
    """will return true false true ... starting with the initial (against
    loops while testing)"""
    if self.change_bool_after_every_call:
      self.file_exists = not self.file_exists
      return not self.file_exists
    else:
      return self.file_exists

  def FolderExists(self, path: str) -> bool:
    """will return true false true ... starting with the initial (against
    loops while testing)"""
    if self.change_bool_after_every_call:
      self.folder_exists = not self.folder_exists
      return not self.folder_exists
    else:
      return self.folder_exists

  def IsValidPluginName(self, plugin_name: str) -> bool:
    """will return true false true ... starting with the initial (against
    loops while testing)"""
    if self.change_bool_after_every_call:
      self.valid_name = not self.valid_name
      return not self.valid_name
    else:
      return self.valid_name
