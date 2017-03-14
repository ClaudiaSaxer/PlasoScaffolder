# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class BaseFileHandler(metaclass=ABCMeta):
  """ Class representing the base class for the file handler"""

  @staticmethod
  @abstractmethod
  def create_file_path(cls, path: str, name: str, suffix: str) -> str:
    """Creates the file path out of the directory path, filename and suffix.

    Args:
      path: the path to the file directory
      name: the filename
      suffix: the suffix

    Returns: the joined path to the file
    """
    pass

  @staticmethod
  @abstractmethod
  def _create_folder(cls, directory_path):
    """creates a folder only to be called if the target folder does not yet
    exists

    Args:
      directory_path: the path to the directory to create
    """
    pass

  @abstractmethod
  def create_file(self, directory_path: str, file_name: str,
      filename_suffix: str):
    """creates a empty file

    Args:
      directory_path: The path to the directory the file should be created.
      file_name: the name of the new file.
      filename_suffix: the suffix of the new file.

    Returns: the path of the created file
    """
    pass

  @abstractmethod
  def create_file_from_path(self, file_path: str) -> str:
    """creates a empty file

    Args:
      file_path: the path to the file.

    Returns: the path of the created file
    """
    pass

  @abstractmethod
  def copy_file(self, source: str, destination: str) -> str:
    """Copies a file

    Args:
      source: path of the file to copy
      destination: path to copy the file to.

    Returns: the path of the copied file
    """
    pass

  @abstractmethod
  def create_or_modify_file_with_content(self, source: str, content: str):
    """Add content to file or modify file and create folder if they dont exist

    Args:
      source: the file to edit / create
      content: the content to add to the file
    """
    pass

  @classmethod
  @abstractmethod
  def add_content(cls, source: str, content: str) -> str:
    """Add content to a file and create file if non existing

    Args:
      source: The path of the file to edit.
      content: The content to append to the file.

    Returns: The path of the edited file.
    """
    pass

  @abstractmethod
  def _create_folder_for_file_path_if_not_exist(self, file_path: str):
    """Creates folders for the given file if it does not exist

    Args:
      file_path: the path to the file

    Returns: the directory path of the created directory
    """
    pass
