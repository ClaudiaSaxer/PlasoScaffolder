# -*- coding: utf-8 -*-
"""__helper for the test"""
import os

__file__ = os.path.abspath(__file__)


def TemplatePath() -> str:
  """ generating the template __path for the tests

  Returns:
    str: the template __path

  """
  return os.path.join(
      os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
      'plasoscaffolder', 'bll', 'templates')
