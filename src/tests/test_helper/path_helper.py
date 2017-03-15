# -*- coding: utf-8 -*-
import os

__file__ = os.path.abspath(__file__)

def template_path():
  return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'plasoscaffolder','bll','templates')

