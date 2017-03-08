import unittest

from plasoscaffolder.bll.mappings.init_formatter_mapping import *


class InitFormatterMappingTest(unittest.TestCase):
  def setUp(self):
    self.plugin_name = "the_one_and_only"
  def test_get_formatter_init_create(self):
    actual = get_formatter_init_create(self.plugin_name)
    expected = "# -*- coding: utf-8 -*-\nfrom plaso.formatters import "+self.plugin_name
    self.assertEqual(expected,actual)

  def test_get_formatter_init_edit(self):
    actual = get_formatter_init_edit(self.plugin_name)
    expected = "from plaso.formatters import "+self.plugin_name
    self.assertEqual(expected,actual)

if __name__ == '__main__':
  unittest.main()
