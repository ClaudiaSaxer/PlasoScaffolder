# -*- coding: utf-8 -*-
from abc import ABCMeta
from abc import abstractmethod

class BaseFileHandler(metaclass=ABCMeta):
  """ Class representing the base class for the file handler."""

  @staticmethod
  @abstractmethod
  def create_file_path(cls, path: str, name: str, suffix: str) -> str:
    """Creates the file path out of the directory path, filename and suffix.

    Args:
      path (str): the path to the file directory
      name (str): the filename
      suffix (str): the suffix

    Returns:
      str: the joined path to the file
    """

  @staticmethod
  @abstractmethod
  def _create_folder(cls, directory_path):
    """Creates a folder only to be called if the target folder does not yet
    exists.

    Args:
      directory_path (str): the path to the directory to create
    """

  @abstractmethod
  def create_file(self, directory_path: str, file_name: str,
      filename_suffix: str):
    """Creates a empty file.

    Args:
      directory_path (str): The path to the directory the file should be
      created.
      file_name (str): the name of the new file.
      filename_suffix (str): the suffix of the new file.

    Returns:
      str: the path of the created file
    """

  @abstractmethod
  def create_file_from_path(self, file_path: str) -> str:
    """Creates a empty file.

    Args:
      file_path (str): the path to the file.

    Returns:
      str: the path of the created file
    """

  @abstractmethod
  def copy_file(self, source: str, destination: str) -> str:
    """Copies a file.

    Args:
      source (str): path of the file to copy
      destination (str): path to copy the file to.

    Returns:
      str: the path of the copied file
    """

  @abstractmethod
  def create_or_modify_file_with_content(self, source: str, content: str):
    """Add content to file or modify file and create folder if they don't exist.

    Args:
      source (str): the file to edit / create
      content (str): the content to add to the file
    """

  @classmethod
  @abstractmethod
  def add_content(cls, source: str, content: str) -> str:
    """Add content to a file and create file if non existing.

    Args:
      source (str): The path of the file to edit.
      content (str): The content to append to the file.

    Returns:
      str: the path of the edited file.
    """

  @abstractmethod
  def _create_folder_for_file_path_if_not_exist(self, file_path: str):
    """Creates folders for the given file if it does not exist.

    Args:
      file_path (str): the path to the file

    Returns:
      str: the directory path of the created directory
    """
