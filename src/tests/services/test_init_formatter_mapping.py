# -*- coding: utf-8 -*-
import unittest
import os
from plasoscaffolder.bll.mappings.init_mapping import *
from tests.test_helper.path_helper import template_path


class InitMappingTest(unittest.TestCase):
  """ Class representing tests for the init mapping"""

  def setUp(self):
    self.plugin_name = "the_one_and_only"
    print(template_path())
    self.mapper = InitMapper(os.path.abspath(template_path()))

  def test_get_formatter_init_create(self):
    """test the render for creating a new formatter init file"""
    actual = self.mapper.get_formatter_init_create(self.plugin_name)
    expected = "# -*- coding: utf-8 -*-\nfrom plaso.formatters import " + \
               self.plugin_name
    self.assertEqual(expected, actual)

  def test_get_formatter_init_edit(self):
    """test the render for editing a existing formatter init file"""
    actual = self.mapper.get_formatter_init_edit(self.plugin_name)
    expected = "\nfrom plaso.formatters import " + self.plugin_name
    self.assertEqual(expected, actual)

  def test_get_parser_init_create(self):
    """test the render for creating a new parser init file"""
    actual = self.mapper.get_parser_init_create(self.plugin_name)
    expected = "# -*- coding: utf-8 -*-\nfrom plaso.parsers.sqlite_plugins " \
               "import " + self.plugin_name
    self.assertEqual(expected, actual)

  def test_get_parser_init_edit(self):
    """test the render for editing a existing parser init file"""
    actual = self.mapper.get_parser_init_edit(self.plugin_name)
    expected = "\nfrom plaso.parsers.sqlite_plugins import " + self.plugin_name
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
