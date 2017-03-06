# -*- coding: utf-8 -*-
""" A class to create files """
import os
from pathlib import Path

class FileHandler:
  def __init__(self,dirname, filename, filename_suffix):
    self.dirname = dirname
    self.filename = filename
    self.filename_suffix = filename_suffix
    self.filepath = os.path.join(dirname,filename+"."+filename_suffix)


  def _createfolder(self):
    """ creates a folder 
    
    only to be called if the targetfolder does not yet exists"""
    os.makedirs(self.dirname)

  def createfile(self):
    """ creates a empty file """
    if not os.path.exists(self.filepath):
      self._createfolder()

    Path(self.filepath).touch()