import os
import unittest

from plasoscaffolder.bll.mappings.mapping_helper import _get_template_path


class MyTestCase(unittest.TestCase):
  """ Class representing a test case for the mapping helper functions. """

  def test_get_template_path(self):
    expected_first = "templates"
    expected_second = "bll"
    expected_third = "plasoscaffolder"
    actual = _get_template_path().split(os.sep)
    self.assertEqual(expected_first, actual[len(actual) - 1])
    self.assertEqual(expected_second, actual[len(actual) - 2])
    self.assertEqual(expected_third, actual[len(actual) - 3])


if __name__ == '__main__':
  unittest.main()
