# -*- coding: utf-8 -*-
"""test class"""
import unittest

from plasoscaffolder.bll.mappings.mapping_helper import MappingHelper
from tests.test_helper import path_helper


class MyTestCase(unittest.TestCase):
  """ Class representing a test case for the mapping helper functions. """

  def setUp(self):
    self.template_path = path_helper.TestTemplatePath()
    yapf_path = path_helper.YapfStyleFilePath()
    self.plugin_name = "the_one_and_only"
    self.file = "test_template.jinja2"
    self.helper = MappingHelper(self.template_path, yapf_path)

  def testRender(self):
    """test the render """
    context = {'plugin_name': self.plugin_name}
    actual = self.helper.RenderTemplate(self.file, context)
    expected = "# -*- coding: utf-8 -*-\n\"\"\"{0}\"\"\"\n".format(
      self.plugin_name)
    self.assertEqual(expected, actual)

  def testGenerateClassName(self):
    """Test the generation of the classname from the pluginname"""
    name = "this_is_a_test"
    expected = "ThisIsATest"
    actual = self.helper.GenerateClassName(name)
    self.assertEqual(expected, actual)


if __name__ == '__main__':
  unittest.main()
