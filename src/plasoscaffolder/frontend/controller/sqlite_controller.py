# -*- coding: utf-8 -*-
"""File representing the controller for sqLite plugin"""
from plasoscaffolder.frontend.sqliteplugin.file_handler import *
import os 

def test_path(ctx, param, value):
  """save the path"""
  print("save test path "+value)
  return value

def plugin_name(ctx, param, value):
  """save the plugin name"""
  print("save plugin name "+value)
  return value

def source_path(ctx, param, value):
  """save the source path"""
  print("save source path "+value)
  return value

def generate(path, name, testfile):
  """generate files"""
  formatterfile = FileHandler( os.path.join(path,"plaso","formatters"),name,"py")
  formatterfile.createfile()
  parserfile = FileHandler( os.path.join(path,"plaso","parsers","sqlite_plugins"),name,"py")
  parserfile.createfile()
  formatterfiletest = FileHandler( os.path.join(path,"tests","formatters"),name,"py")
  formatterfiletest.createfile()
  parserfiletest = FileHandler( os.path.join(path,"tests","parsers","sqlite_plugins"),name,"py")
  parserfiletest.createfile()

  print("generate "+formatterfile.filepath)
  print("generate "+parserfile.filepath)
  print("generate "+formatterfiletest.filepath)
  print("generate "+parserfiletest.filepath)




  