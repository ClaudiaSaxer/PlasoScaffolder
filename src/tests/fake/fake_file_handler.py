# -*- coding: utf-8 -*-
""" fake class to create files """
from plasoscaffolder.common.base_file_handler import BaseFileHandler


class FakeFileHandler(BaseFileHandler):
  """The fake of the file handler."""
  @classmethod
  def CreateFilePath(cls, path: str, name: str, suffix: str) -> str:
    return name

  @classmethod
  def _CreateFolder(cls, directory_path):
    return directory_path

  def CreateFile(self, directory_path: str, file_name: str,
                  filename_suffix: str):
    return file_name

  def CreateFileFromPath(self, file_path: str) -> str:
    return file_path

  def CopyFile(self, source: str, destination: str) -> str:
    return destination

  def CreateOrModifyFileWithContent(self, source: str, content: str):
    return source

  @classmethod
  def AddContent(cls, source: str, content: str) -> str:
    return source

  def CreateFolderForFilePathIfNotExist(self, file_path: str):
    return file_path
