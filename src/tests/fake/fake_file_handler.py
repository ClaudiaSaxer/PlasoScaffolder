# -*- coding: utf-8 -*-
""" A class to create files """
from plasoscaffolder.common.base_file_handler import BaseFileHandler


class FakeFileHandler(BaseFileHandler):

  @classmethod
  def create_file_path(cls, path: str, name: str, suffix: str) -> str:
     return name

  @classmethod
  def _create_folder(cls, directory_path):
    return directory_path

  def create_file(self, directory_path: str, file_name: str, filename_suffix: str):
    return file_name

  def create_file_from_path(self, file_path: str) -> str:
    return file_path

  def copy_file(self, source:str, destination:str) -> str:
    return destination

  def create_or_modify_file_with_content(self, source: str, content: str):
    return source

  @classmethod
  def add_content(cls, source: str, content: str) -> str:
    return source

  def _create_folder_for_file_path_if_not_exist(self, file_path: str):
   return file_path
