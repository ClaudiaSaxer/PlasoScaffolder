# -*- coding: utf-8 -*-
"""helper for the test"""
import os

__file__ = os.path.abspath(__file__)


def TemplatePath() -> str:
  """ generating the template path for the tests

  Returns:
    str: the template path

  """
  return os.path.join(
      os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
      'plasoscaffolder', 'bll', 'templates')


def TestDatabasePath() -> str:
  """ generating the template path for the tests

  Returns:
    str: the template path

  """
  return os.path.join(
      os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
      'tests', 'test_database')
