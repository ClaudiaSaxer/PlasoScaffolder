# -*- coding: utf-8 -*-
"""Module containing helper functions for the SQLite plugin"""
import os
from abc import ABCMeta, abstractmethod

from plasoscaffolder.bll.mappings.base_init_mapping import BaseInitMapper
from plasoscaffolder.bll.services.base_file_handler import BaseFileHandler


class BaseSqlitePluginHelper(metaclass=ABCMeta):

  @abstractmethod
  def plugin_exists(self, template_path: str,
      fileHandler: BaseFileHandler, init_mapper: BaseInitMapper) -> bool:
    """Checks if the plugin already exists.

    Returns: Boolean True if the plugin already exists. False if it does not.
    """
    pass

  @abstractmethod
  def file_exists(self, path: str) -> bool:
    """Checks if the file exists

    Args:
       path the file path
    """
    pass

  @abstractmethod
  def folder_exists(self, path: str) -> bool:
    """Checks if folder exists

    Args:
      path: the folder path
    """
    pass

