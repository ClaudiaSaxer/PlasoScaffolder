# -*- coding: utf-8 -*-
"""testing the main"""
import unittest

import plasoscaffolder


class VersionTest(unittest.TestCase):
  """the version in init test"""

  def testGetVersionDev(self):
    """testing the get version"""
    expected = '{0}_{1}'.format(
        plasoscaffolder.__version__, plasoscaffolder.VERSION_DATE)
    actual = plasoscaffolder.GetVersion()
    self.assertEqual(expected, actual)

  def testGetVersionNotDev(self):
    """testing the get version"""
    expected = plasoscaffolder.__version__
    plasoscaffolder.VERSION_DEV = False
    actual = plasoscaffolder.GetVersion()
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()
