# -*- coding: utf-8 -*-

def testpath(ctx,param,value):
  """save the path"""
  print("save testpath"+value)

def pluginname(ctx,param,value):
  """save the pluginname"""
  print("save pluginname"+value)

def sourcepath(ctx,param,value):
  """save the sourcpath"""
  print("save sourcepath"+value)

def generate(ctx,param,value):
  """generate files"""
  print("generate"+value)