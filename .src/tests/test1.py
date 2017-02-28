# -*- coding: utf-8 -*-
"""Tests for nothing at all."""
import unittest

class Test2(unittest.TestCase):
  """Testing a tested function, so it is useless"""

  def testSomeTest(self):
    """blabla"""
    self.assertTrue('FOO'.isupper())

if __name__ == '__main__':
  unittest.main()
