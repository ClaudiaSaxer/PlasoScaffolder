# -*- coding: utf-8 -*-
"""File representing the controller for sqlite plugin"""


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
  print("generate "+str(path)+" "+str(name)+" "+str(testfile))

