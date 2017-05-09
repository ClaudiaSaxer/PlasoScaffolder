# -*- coding: utf-8 -*-
"""runs all tests"""
import sys
import unittest

if __name__ == '__main__':
  test_suite = unittest.TestLoader().discover('tests', pattern='*.py')
  test_suite_integration = unittest.TestLoader().discover('tests_integration',
                                                          pattern='*.py')
  all_tests = unittest.TestSuite((test_suite, test_suite_integration))

  test_results = unittest.TextTestRunner(verbosity=2).run(all_tests)
  if not test_results.wasSuccessful():
    sys.exit(1)
