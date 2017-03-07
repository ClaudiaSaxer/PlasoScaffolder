# -*- coding: utf-8 -*-
""" A class to create files """
import os
from pathlib import Path


class FileCreator:
  """ Class handles the creation of Files"""

  def __init__(self):
    """ Constructing the FileHandler"""

  @staticmethod
  def create_file_path(path, name, suffix):
    """ Creates the file path out of the directory path, filename and suffix."""
    return os.path.join(path, name + "." + suffix)

  @staticmethod
  def _create_folder(directory_path):
    """ creates a folder 
    
    only to be called if the target folder does not yet exists"""
    os.makedirs(directory_path)

  def create_file(self, directory_path, file_name, filename_suffix):
    """ creates a empty file

    :param directory_path: The path to the directory the file should be created.
    :param file_name: the name of the new file.
    :param filename_suffix: the suffix of the new file.
    """
    file_path = self.create_file_path(directory_path, file_name,
      filename_suffix)
    if not os.path.exists(file_path):
      self._create_folder(directory_path)

    Path(file_path).touch()

  def create_file_from_path(self, file_path):
    """
    creates a empty file

    :param file_path: the path to the file.
    :return: the path of the created file
    """
    if not os.path.exists(os.path.dirname(file_path)):
      self._create_folder(os.path.dirname(file_path))

    Path(file_path).touch()

    return file_path
