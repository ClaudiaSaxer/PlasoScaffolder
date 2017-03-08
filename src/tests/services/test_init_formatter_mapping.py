# -*- coding: utf-8 -*-
import unittest
from plasoscaffolder.bll.mappings.init_mapping import *


class InitMappingTest(unittest.TestCase):
  """ Class representing tests for the init mapping"""

  def setUp(self):
    self.plugin_name = "the_one_and_only"

  def test_get_formatter_init_create(self):
    """test the render for creating a new formatter init file"""
    actual = get_formatter_init_create(self.plugin_name)
    expected = "# -*- coding: utf-8 -*-\nfrom plaso.formatters import " + \
               self.plugin_name
    self.assertEqual(expected, actual)

  def test_get_formatter_init_edit(self):
    """test the render for editing a existing formatter init file"""
    actual = get_formatter_init_edit(self.plugin_name)
    expected = "\nfrom plaso.formatters import " + self.plugin_name
    self.assertEqual(expected, actual)

  def test_get_parser_init_create(self):
    """test the render for creating a new parser init file"""
    actual = get_parser_init_create(self.plugin_name)
    expected = "# -*- coding: utf-8 -*-\nfrom plaso.parsers.sqlite_plugins " \
               "import " + self.plugin_name
    self.assertEqual(expected, actual)

  def test_get_parser_init_edit(self):
    """test the render for editing a existing parser init file"""
    actual = get_parser_init_edit(self.plugin_name)
    expected = "\nfrom plaso.parsers.sqlite_plugins import " + self.plugin_name
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
