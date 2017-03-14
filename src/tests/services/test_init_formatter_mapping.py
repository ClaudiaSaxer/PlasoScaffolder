# -*- coding: utf-8 -*-
import unittest
import os
from plasoscaffolder.bll.mappings.init_mapping import *
from tests.fake.fake_mapping_helper import FakeMappingHelper
from tests.test_helper.path_helper import template_path


class InitMappingTest(unittest.TestCase):
  """ Class representing tests for the init mapping"""

  def setUp(self):
    self.plugin_name = "the_one_and_only"
    print(template_path())
    self.mapper = InitMapper("template ",FakeMappingHelper)

  def test_get_formatter_init_create(self):
    """test the render for creating a new formatter init file"""
    actual = self.mapper.get_formatter_init_create(self.plugin_name)
    expected = "fake string formatter_init_create_template.jinja2"
    self.assertEqual(expected, actual)

  def test_get_formatter_init_edit(self):
    """test the render for editing a existing formatter init file"""
    actual = self.mapper.get_formatter_init_edit(self.plugin_name)
    expected = "fake string formatter_init_edit_template.jinja2"
    self.assertEqual(expected, actual)

  def test_get_parser_init_create(self):
    """test the render for creating a new parser init file"""
    actual = self.mapper.get_parser_init_create(self.plugin_name)
    expected = "fake string parser_init_create_template.jinja2"

    self.assertEqual(expected, actual)

  def test_get_parser_init_edit(self):
    """test the render for editing a existing parser init file"""
    actual = self.mapper.get_parser_init_edit(self.plugin_name)
    expected = "fake string parser_init_edit_template.jinja2"
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
