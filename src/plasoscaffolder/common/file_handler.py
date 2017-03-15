# -*- coding: utf-8 -*-
import os
from pathlib import Path
from shutil import copyfile
from plasoscaffolder.common.base_file_handler import BaseFileHandler


class FileHandler(BaseFileHandler):
  """ Class handles the creation of Files"""

  def __init__(self):
    """Initializing the filehandler"""
    super().__init__()

  @classmethod
  def create_file_path(cls, path: str, name: str, suffix: str) -> str:
    """Creates the file path out of the directory path, filename and suffix.

    Args:
      path (str): the path to the file directory
      name (str): the filename
      suffix (str): the suffix

    Returns:
      str: the joined path to the file
    """
    file_name = '{0:s}.{1:s}'.format(name, suffix)
    return os.path.join(path, file_name)

  @classmethod
  def _create_folder(cls, directory_path):
    """Creates a folder only to be called if the target folder does not yet
     exists.

     Args:
       directory_path (str): the path to the directory to create
     """
    os.makedirs(directory_path)

  def create_file(self, directory_path: str, file_name: str, filename_suffix: str):
    """Creates a empty file.

    Args:
      directory_path (str): The path to the directory the file should be
      created.
      file_name (str): the name of the new file.
      filename_suffix (str): the suffix of the new file.

    Returns:
      str: the path of the created file
    """
    file_path = self.create_file_path(directory_path, file_name,
      filename_suffix)
    if not os.path.exists(file_path):
      self._create_folder(directory_path)

    Path(file_path).touch()
    return file_path

  def create_file_from_path(self, file_path: str) -> str:
    """Creates a empty file.

    Args:
      file_path (str): the path to the file.

    Returns:
      str: the path of the created file
    """
    self._create_folder_for_file_path_if_not_exist(file_path)
    Path(file_path).touch()
    return file_path

  def copy_file(self, source:str, destination:str) -> str:
    """Copies a file.

      Args:
        source (str): path of the file to copy
        destination (str): path to copy the file to.

      Returns:
        str: the path of the copied file
      """
    self._create_folder_for_file_path_if_not_exist(destination)
    copyfile(source, destination)
    return destination

  def create_or_modify_file_with_content(self, source: str, content: str):
    self._create_folder_for_file_path_if_not_exist(source)
    self._add_content_to_file(source, content)

  @classmethod
  def add_content(cls, source: str, content: str) -> str:
    """Add content to a file and create file if non existing.

    Args:
      source (str): The path of the file to edit.
      content (str): The content to append to the file.

    Returns:
      str: the path of the edited file.
    """
    with open(source, 'a') as file_object:
      file_object.write(content)

    return source

  def _create_folder_for_file_path_if_not_exist(self, file_path: str):
    """Creates folders for the given file if it does not exist.

    Args:
      file_path (str): the path to the file

    Returns:
      str: the directory path of the created directory
    """
    directory_path = os.path.dirname(file_path)
    if not os.path.exists(directory_path):
      self._create_folder(directory_path)
    return directory_path
