# -*- coding: utf-8 -*-
""" A class to create files """
import os
from pathlib import Path

class FileHandler:
  def __init__(self,directory_name, file_name, filename_suffix):
    self.directory_name = directory_name
    self.filename = file_name
    self.filename_suffix = filename_suffix
    self.file_path = os.path.join(directory_name,file_name+"."+filename_suffix)


  def _create_folder(self):
    """ creates a folder 
    
    only to be called if the targetfolder does not yet exists"""
    os.makedirs(self.dirname)

  def create_file(self):
    """ creates a empty file """
    if not os.path.exists(self.filepath):
      self._create_folder()

    Path(self.file_path).touch()