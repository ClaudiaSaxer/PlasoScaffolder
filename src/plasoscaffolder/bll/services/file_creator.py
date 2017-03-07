# -*- coding: utf-8 -*-
""" A class to create files """
import os
from pathlib import Path


class FileCreator:
  """Class handles the creation of Files"""

  def __init__(self, directory_path, file_name, filename_suffix):
    """
    Constructing the FileHandler

    :param directory_path: The path to the directory the file should be created.
    :param file_name: the name of the new file.
    :param filename_suffix: the suffix of the new file.
    """
    self.directory_path = directory_path
    self.filename = file_name
    self.filename_suffix = filename_suffix
    self.file_path = self.create_file_path(directory_path, file_name,
      filename_suffix)

  @staticmethod
  def create_file_path(path, name, suffix):
    """creates the filepath out of the direcotry path, filename and suffix"""
    return os.path.join(path, name + "." + suffix)

  def _create_folder(self):
    """ creates a folder 
    
    only to be called if the targetfolder does not yet exists"""
    os.makedirs(self.directory_path)

  def create_file(self):
    """ creates a empty file """
    if not os.path.exists(self.file_path):
      self._create_folder()

    Path(self.file_path).touch()
