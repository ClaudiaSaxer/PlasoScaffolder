# -*- coding: utf-8 -*-
import unittest

import sys

if __name__ == '__main__':
  test_suite = unittest.TestLoader().discover('tests', pattern='*.py')
  test_results = unittest.TextTestRunner(verbosity=2).run(test_suite)
  if not test_results.wasSuccessful():
    sys.exit(1)

  # Run the tool tests.
  test_suite = unittest.TestLoader().discover('tests', pattern='test_*.py')
  test_results = unittest.TextTestRunner(verbosity=2).run(test_suite)
  if not test_results.wasSuccessful():
    sys.exit(1)