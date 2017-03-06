# -*- coding: utf-8 -*-
"""File representing the controller for sqlite plugin"""
from .file_handler import *
import os 

def testpath(ctx, param, value):
  """save the path"""
  print("save testpath "+value)
  return value

def pluginname(ctx, param, value):
  """save the pluginname"""
  print("save pluginname "+value)
  return value

def sourcepath(ctx, param, value):
  """save the sourcpath"""
  print("save sourcepath "+value)
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




  