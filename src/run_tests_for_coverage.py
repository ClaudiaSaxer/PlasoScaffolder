# -*- coding: utf-8 -*-
"""runs all tests"""
import os
import sys
import unittest

if __name__ == '__main__':
  unittest_path = '{0}{1}{2}'.format('tests',os.sep,'unittests')
  test_suite = unittest.TestLoader().discover(unittest_path, pattern='*.py')
  test_results = unittest.TextTestRunner(verbosity=2).run(test_suite)
  if not test_results.wasSuccessful():
    sys.exit(1)
