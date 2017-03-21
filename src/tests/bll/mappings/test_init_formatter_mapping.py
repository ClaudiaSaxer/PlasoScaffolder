# -*- coding: utf-8 -*-
"""test class"""
import unittest

from plasoscaffolder.bll.mappings.init_mapping import InitMapper
from tests.fake.fake_mapping_helper import FakeMappingHelper


class InitMappingTest(unittest.TestCase):
  """ Class representing tests for the init mapping"""

  def setUp(self):
    self.plugin_name = "the_one_and_only"
    self.mapper = InitMapper("template ", FakeMappingHelper)

  def testGetFormatterInitCreate(self):
    """test the render for creating a new formatter init file"""
    actual = self.mapper.GetFormatterInitCreate(self.plugin_name)
    expected = "fake string formatter_init_create_template.jinja2"
    self.assertEqual(expected, actual)

  def testGetFormatterInitEdit(self):
    """test the render for editing a existing formatter init file"""
    actual = self.mapper.GetFormatterInitEdit(self.plugin_name)
    expected = "fake string formatter_init_edit_template.jinja2"
    self.assertEqual(expected, actual)

  def testGetParserInitCreate(self):
    """test the render for creating a new parser init file"""
    actual = self.mapper.GetParserInitCreate(self.plugin_name)
    expected = "fake string parser_init_create_template.jinja2"

    self.assertEqual(expected, actual)

  def testGetParserInitEdit(self):
    """test the render for editing a existing parser init file"""
    actual = self.mapper.GetParserInitEdit(self.plugin_name)
    expected = "fake string parser_init_edit_template.jinja2"
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
