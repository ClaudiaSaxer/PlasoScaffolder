import os
import unittest

from plasoscaffolder.bll.mappings.mapping_helper import MappingHelper
from tests.test_helper.path_helper import template_path


class MyTestCase(unittest.TestCase):
  """ Class representing a test case for the mapping helper functions. """

  def setUp(self):
    self.template_path = template_path()

  def test_get_template_path(self):
   """helper = MappingHelper(template_path())

    expected_first = "templates"
    expected_second = "bll"
    expected_third = "plasoscaffolder"
    actual = helper._get_template_path().split(os.sep)
    self.assertEqual(expected_first, actual[len(actual) - 1])
    self.assertEqual(expected_second, actual[len(actual) - 2])
    self.assertEqual(expected_third, actual[len(actual) - 3])"""


if __name__ == '__main__':
  unittest.main()
