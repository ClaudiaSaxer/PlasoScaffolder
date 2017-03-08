# -*- coding: utf-8 -*-
""" A class to create files """
import os
from shutil import copyfile
from pathlib import Path


class FileHandler:
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
    self.__create_folder_for_file_path_if_not_exist(self,file_path)
    Path(file_path).touch()
    return file_path

  def copy_file(self, source, destination):
    """ Copies a database file

    :param source: the source path of the database
    :param destination: the destination path of the database
    :return: he path of the copied file
    """
    self.__create_folder_for_file_path_if_not_exist(self,destination)
    copyfile(source, destination)
    return destination

  def create_or_modify_file_with_content(self, source, content):
    self.__create_folder_for_file_path_if_not_exist(self,source)
    self._add_content_to_file(source, content)


  @staticmethod
  def add_content(source, content):
    """ Add content to a file and create file if non existing

    :param source: The path of the file to edit.
    :param content: The content to append to the file.
    :return: The path of the edited file.
    """
    with open(source, "a+") as file:
      file.write(content)
    return source


  @staticmethod
  def __create_folder_for_file_path_if_not_exist(self, file_path):
    """Creates folders for the given file if it does not exist"""
    if not os.path.exists(os.path.dirname(file_path)):
      self._create_folder(os.path.dirname(file_path))
