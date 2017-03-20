# -*- coding: utf-8 -*-
"""test class"""
import os
import unittest

from plasoscaffolder.bll.mappings.mapping_helper import MappingHelper


class MyTestCase(unittest.TestCase):
  """ Class representing a test case for the mapping helper functions. """

  def setUp(self):
    self.template_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "test_template")
    self.plugin_name = "the_one_and_only"
    self.file = "test_template.jinja2"
    self.helper = MappingHelper(self.template_path)

  def test_render(self):
    """test the render """
    context = {'plugin_name': self.plugin_name}
    actual = self.helper.render_template(self.file, context)
    expected = "# -*- coding: utf-8 -*-\ntest " + self.plugin_name
    self.assertEqual(expected, actual)

  def test_generate_classname(self):
    """Test the generation of the classname from the pluginname"""
    name = "this_is_a_test"
    expected = "ThisIsATest"
    actual = self.helper.generate_class_name(name)
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
